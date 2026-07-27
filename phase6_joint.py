"""Joint two-asset barrier pricing under the bounded stochastic correlation.

Model (forward measure, normal/Bachelier convention):

    dF1 = sigma1 dW1,
    dF2 = sigma2 (rho_t dW1 + sqrt(1-rho_t**2) dW2),
    rho_t = X_t / sqrt(X_t**2 + scale**2),   X_t = x0 + drift*t + vol*W_t,

with W independent of (W1, W2).  For any linear combination
Z = alpha1 F1 + alpha2 F2, the Dambis-Dubins-Schwarz theorem gives,
conditionally on the correlation path,

    Z_t =law z0 + B_{v(t)},   v(t) = integral_0^t q(rho_s) ds,
    q(rho) = alpha1**2 sigma1**2 + alpha2**2 sigma2**2
             + 2 alpha1 alpha2 sigma1 sigma2 rho.

Barrier prices therefore collapse to one-dimensional expectations over the
scalar clock v(T; rho).  This module computes exact clock moments by
deterministic Gauss quadrature (not Monte Carlo) and moment-matched
one-dimensional prices; exact simulation benchmarks live in the notebook.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.stats import gamma as gamma_distribution

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _validate_common(maturity: float, volatility: float) -> None:
    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(volatility) or volatility < 0.0:
        raise ValueError("volatility must be finite and nonnegative")


def _f(x: np.ndarray, scale: float) -> np.ndarray:
    return x / np.sqrt(x * x + scale * scale)


def q_variance(rho, *, alpha1: float, alpha2: float, sigma1: float, sigma2: float):
    """Instantaneous variance of Z = alpha1 F1 + alpha2 F2 at correlation rho.

    Accepts scalars or numpy arrays (elementwise).
    """

    if not (math.isfinite(sigma1) and sigma1 > 0.0):
        raise ValueError("sigma1 must be finite and strictly positive")
    if not (math.isfinite(sigma2) and sigma2 > 0.0):
        raise ValueError("sigma2 must be finite and strictly positive")
    rho_arr = np.asarray(rho, dtype=float)
    if np.any((rho_arr < -1.0) | (rho_arr > 1.0)):
        raise ValueError("rho must lie in [-1, 1]")
    result = (
        alpha1**2 * sigma1**2
        + alpha2**2 * sigma2**2
        + 2.0 * alpha1 * alpha2 * sigma1 * sigma2 * rho_arr
    )
    return float(result) if result.ndim == 0 else result


def _rho_mean(t: float, *, x0: float, drift: float, volatility: float, scale: float,
              nodes: np.ndarray, weights: np.ndarray) -> float:
    """E[rho_t] by Gauss-Hermite quadrature (exact for the Gaussian factor)."""

    sd = volatility * math.sqrt(t)
    values = _f(x0 + drift * t + sd * nodes, scale)
    return float(np.dot(weights, values) / SQRT_2PI)


def _rho_product_mean(
    s: float, t: float, *, x0: float, drift: float, volatility: float, scale: float,
    nodes: np.ndarray, weights: np.ndarray,
) -> float:
    """E[rho_s rho_t] for s < t by tensor Gauss-Hermite quadrature."""

    sd_s = volatility * math.sqrt(s)
    sd_d = volatility * math.sqrt(t - s)
    x_s = x0 + drift * s + sd_s * nodes
    # X_t = X_s + drift*(t-s) + volatility*sqrt(t-s)*Z2, independent increment.
    values = _f(x_s[:, None], scale) * _f(
        x_s[:, None] + drift * (t - s) + sd_d * nodes[None, :], scale
    )
    return float(weights @ values @ weights / (2.0 * math.pi))


def occupation_moments(
    maturity: float,
    *,
    x0: float,
    drift: float,
    volatility: float,
    scale: float,
    gh_order: int = 64,
    gl_order: int = 64,
) -> tuple[float, float]:
    """Return (E[A_T], Var(A_T)) for A_T = integral_0^T rho_s ds.

    Deterministic Gauss quadrature throughout: Gauss-Hermite over the Gaussian
    factor(s), Gauss-Legendre over the time simplex.  Convergence across
    orders is checked in the test suite; these are not Monte Carlo estimates.
    """

    _validate_common(maturity, volatility)
    if not math.isfinite(x0) or not math.isfinite(drift):
        raise ValueError("x0 and drift must be finite")
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if gh_order < 8 or gl_order < 8:
        raise ValueError("quadrature orders must be at least 8")

    gh_nodes, gh_weights = hermegauss(gh_order)
    gl_nodes, gl_weights = leggauss(gl_order)
    times = 0.5 * maturity * (gl_nodes + 1.0)
    time_weights = 0.5 * maturity * gl_weights

    means = np.array([
        _rho_mean(t, x0=x0, drift=drift, volatility=volatility, scale=scale,
                  nodes=gh_nodes, weights=gh_weights)
        for t in times
    ])
    mean_a = float(np.dot(time_weights, means))

    # Var(A_T) = 2 * integral over s < t of Cov(rho_s, rho_t).  Integrate the
    # triangle directly: for each s, a Gauss-Legendre rule mapped to [s, T].
    # (Masking a square rule below the diagonal would introduce a ridge along
    # s = t and destroy the convergence rate.)
    var_half = 0.0
    for i, s in enumerate(times):
        span = maturity - s
        if span <= 0.0:
            continue
        t_local = 0.5 * span * (gl_nodes + 1.0) + s
        t_weights = 0.5 * span * gl_weights
        means_t = np.array([
            _rho_mean(t, x0=x0, drift=drift, volatility=volatility, scale=scale,
                      nodes=gh_nodes, weights=gh_weights)
            for t in t_local
        ])
        products = np.array([
            _rho_product_mean(
                s, t, x0=x0, drift=drift, volatility=volatility, scale=scale,
                nodes=gh_nodes, weights=gh_weights,
            )
            for t in t_local
        ])
        covariances = products - means[i] * means_t
        var_half += time_weights[i] * float(np.dot(t_weights, covariances))
    var_a = 2.0 * var_half
    return mean_a, max(var_a, 0.0)


def clock_moments(
    maturity: float,
    *,
    alpha1: float,
    alpha2: float,
    sigma1: float,
    sigma2: float,
    x0: float,
    drift: float,
    volatility: float,
    scale: float,
    gh_order: int = 64,
    gl_order: int = 64,
) -> tuple[float, float]:
    """Return (E[v(T)], Var(v(T))) for the DDS clock of Z = alpha1 F1 + alpha2 F2."""

    _validate_common(maturity, volatility)
    if alpha1 == 0.0 and alpha2 == 0.0:
        raise ValueError("at least one alpha must be nonzero")
    base = alpha1**2 * sigma1**2 + alpha2**2 * sigma2**2
    coeff = 2.0 * alpha1 * alpha2 * sigma1 * sigma2
    if coeff == 0.0:
        return base * maturity, 0.0
    mean_a, var_a = occupation_moments(
        maturity, x0=x0, drift=drift, volatility=volatility, scale=scale,
        gh_order=gh_order, gl_order=gl_order,
    )
    return base * maturity + coeff * mean_a, coeff**2 * var_a


def driftless_touch_probability(distance: float, clock: float) -> float:
    """P(sup_{u<=v} B_u >= distance) = 2(1 - Phi(distance/sqrt(v))), v > 0."""

    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    if not math.isfinite(clock) or clock <= 0.0:
        raise ValueError("clock must be finite and strictly positive")
    return 2.0 * (1.0 - 0.5 * (1.0 + math.erf(distance / math.sqrt(2.0 * clock))))


def gamma_touch_price(
    distance: float,
    *,
    maturity: float,
    rate: float,
    mean_clock: float,
    var_clock: float,
) -> float:
    """Moment-matched one-touch price E[2(1-Phi(d/sqrt(v)))] over a Gamma clock.

    The Gamma law is matched to (mean_clock, var_clock); with var_clock = 0
    the clock is deterministic and the price is exact.  Accuracy of the
    moment match itself is measured against exact simulation in the notebook,
    per parameter set -- no blanket claim is made here.
    """

    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    if not math.isfinite(mean_clock) or mean_clock <= 0.0:
        raise ValueError("mean_clock must be finite and strictly positive")
    if not math.isfinite(var_clock) or var_clock < 0.0:
        raise ValueError("var_clock must be finite and nonnegative")
    discount = math.exp(-rate * maturity)
    if var_clock == 0.0:
        return discount * driftless_touch_probability(distance, mean_clock)
    shape = mean_clock**2 / var_clock
    theta = var_clock / mean_clock

    def integrand(v: float) -> float:
        return driftless_touch_probability(distance, v) * gamma_distribution.pdf(v, shape, scale=theta)

    value, _ = quad(integrand, 0.0, np.inf, epsabs=1e-13)
    return discount * value


__all__ = [
    "clock_moments",
    "driftless_touch_probability",
    "gamma_touch_price",
    "occupation_moments",
    "q_variance",
]
