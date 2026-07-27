"""OU-driver bounded correlation: exact statics and clock moments.

Driver (mean-reverting):

    dX_t = kappa * (x_bar - X_t) dt + vol dW_t,   kappa > 0,

correlation coordinate rho_t = X_t / sqrt(X_t**2 + scale**2).

Exact (closed form): transition density, stationary density, digital price.
Exact (deterministic quadrature): occupation/clock moments, via the OU
bivariate Gaussian law

    X_t = x_bar + exp(-kappa*(t-s)) (X_s - x_bar) + independent increment.

First-passage laws are NOT closed form under OU (classical); they are
computed deterministically through the Milestone 4 FK resolvent with the
callable drift lambda g: kappa*(x_bar - g).  The kappa -> 0+ limit recovers
every Brownian-driver formula of Milestones 1-4 and is enforced by tests.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from numpy.polynomial.legendre import leggauss

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _validate(kappa: float, x_bar: float, volatility: float, scale: float) -> None:
    if not math.isfinite(kappa) or kappa < 0.0:
        raise ValueError("kappa must be finite and nonnegative")
    if not math.isfinite(x_bar):
        raise ValueError("x_bar must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")


def ou_transition_mean_var(
    maturity: float, *, x0: float, kappa: float, x_bar: float, volatility: float
) -> tuple[float, float]:
    """Mean and variance of X_t under OU (kappa = 0 gives the BM limit)."""

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(x0):
        raise ValueError("x0 must be finite")
    if kappa == 0.0:
        return x0, volatility**2 * maturity
    mean = x_bar + (x0 - x_bar) * math.exp(-kappa * maturity)
    var = volatility**2 / (2.0 * kappa) * (1.0 - math.exp(-2.0 * kappa * maturity))
    return mean, var


def ou_stationary_mean_var(*, kappa: float, x_bar: float, volatility: float) -> tuple[float, float]:
    """Stationary mean and variance of OU."""

    if not math.isfinite(kappa) or kappa <= 0.0:
        raise ValueError("kappa must be finite and strictly positive for a stationary law")
    return x_bar, volatility**2 / (2.0 * kappa)


def _x_from_rho(rho: float, scale: float) -> float:
    if not (-1.0 < rho < 1.0):
        raise ValueError("rho must lie in (-1, 1)")
    return scale * rho / math.sqrt(1.0 - rho * rho)


def ou_rho_transition_density(
    rho: float,
    *,
    maturity: float,
    x0: float,
    kappa: float,
    x_bar: float,
    volatility: float,
    scale: float,
) -> float:
    """Exact time-t density of rho_t under the OU driver."""

    _validate(kappa, x_bar, volatility, scale)
    mean, var = ou_transition_mean_var(
        maturity, x0=x0, kappa=kappa, x_bar=x_bar, volatility=volatility
    )
    x = _x_from_rho(rho, scale)
    jacobian = scale / (1.0 - rho * rho) ** 1.5
    z = (x - mean) / math.sqrt(var)
    return jacobian * math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi * var)


def ou_rho_stationary_density(
    rho: float, *, kappa: float, x_bar: float, volatility: float, scale: float
) -> float:
    """Exact stationary density of rho under the OU driver."""

    _validate(kappa, x_bar, volatility, scale)
    mean, var = ou_stationary_mean_var(kappa=kappa, x_bar=x_bar, volatility=volatility)
    x = _x_from_rho(rho, scale)
    jacobian = scale / (1.0 - rho * rho) ** 1.5
    z = (x - mean) / math.sqrt(var)
    return jacobian * math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi * var)


def ou_digital_price(
    rho_star: float,
    *,
    maturity: float,
    x0: float,
    kappa: float,
    x_bar: float,
    volatility: float,
    scale: float,
    rate: float,
) -> float:
    """Price of 1{rho_T >= rho_star} at T under OU: Gaussian tail, exact."""

    _validate(kappa, x_bar, volatility, scale)
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    mean, var = ou_transition_mean_var(
        maturity, x0=x0, kappa=kappa, x_bar=x_bar, volatility=volatility
    )
    x_star = _x_from_rho(rho_star, scale)
    probability = 0.5 * (1.0 + math.erf((mean - x_star) / math.sqrt(2.0 * var)))
    return math.exp(-rate * maturity) * probability


def _f(x: np.ndarray, scale: float) -> np.ndarray:
    return x / np.sqrt(x * x + scale * scale)


def ou_occupation_moments(
    maturity: float,
    *,
    x0: float,
    kappa: float,
    x_bar: float,
    volatility: float,
    scale: float,
    gh_order: int = 64,
    gl_order: int = 64,
) -> tuple[float, float]:
    """Return (E[A_T], Var(A_T)) for A_T = integral_0^T rho_s ds under OU.

    Same triangle-aware Gauss quadrature as the BM case, with the OU
    bivariate law: X_t = m_t + e^{-kappa (t-s)} sd_s Z1 + sd_tilde Z2 with
    sd_tilde**2 = vol**2/(2 kappa) (1 - e^{-2 kappa (t-s)}).
    """

    _validate(kappa, x_bar, volatility, scale)
    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(x0):
        raise ValueError("x0 must be finite")
    if gh_order < 8 or gl_order < 8:
        raise ValueError("quadrature orders must be at least 8")

    gh_nodes, gh_weights = hermegauss(gh_order)
    gl_nodes, gl_weights = leggauss(gl_order)
    times = 0.5 * maturity * (gl_nodes + 1.0)
    time_weights = 0.5 * maturity * gl_weights

    stats = [ou_transition_mean_var(t, x0=x0, kappa=kappa, x_bar=x_bar, volatility=volatility)
             for t in times]

    def rho_mean_at(index: int) -> float:
        mean, var = stats[index]
        values = _f(mean + math.sqrt(var) * gh_nodes, scale)
        return float(np.dot(gh_weights, values) / SQRT_2PI)

    means = np.array([rho_mean_at(i) for i in range(gl_order)])
    mean_a = float(np.dot(time_weights, means))

    var_half = 0.0
    for i, s in enumerate(times):
        span = maturity - s
        if span <= 0.0:
            continue
        mean_s, var_s = stats[i]
        sd_s = math.sqrt(var_s)
        t_local = 0.5 * span * (gl_nodes + 1.0) + s
        t_weights = 0.5 * span * gl_weights
        means_t = np.array([
            float(np.dot(gh_weights, _f(m + math.sqrt(v) * gh_nodes, scale)) / SQRT_2PI)
            for (m, v) in (ou_transition_mean_var(t, x0=x0, kappa=kappa, x_bar=x_bar,
                                                  volatility=volatility) for t in t_local)
        ])
        covariances = np.empty(t_local.size)
        for j, t in enumerate(t_local):
            gap = t - s
            decay = math.exp(-kappa * gap) if kappa > 0.0 else 1.0
            if kappa > 0.0:
                sd_innov = math.sqrt(volatility**2 / (2.0 * kappa) * (1.0 - decay**2))
            else:
                sd_innov = volatility * math.sqrt(gap)
            mean_t = ou_transition_mean_var(t, x0=x0, kappa=kappa, x_bar=x_bar,
                                            volatility=volatility)[0]
            x_s = mean_s + sd_s * gh_nodes
            x_t = mean_t + decay * sd_s * gh_nodes[:, None] + sd_innov * gh_nodes[None, :]
            product = float(gh_weights @ (_f(x_s, scale)[:, None] * _f(x_t, scale)) @ gh_weights
                            / (2.0 * math.pi))
            covariances[j] = product - means[i] * means_t[j]
        var_half += time_weights[i] * float(np.dot(t_weights, covariances))
    var_a = 2.0 * var_half
    return mean_a, max(var_a, 0.0)


def ou_clock_moments(
    maturity: float,
    *,
    alpha1: float,
    alpha2: float,
    sigma1: float,
    sigma2: float,
    x0: float,
    kappa: float,
    x_bar: float,
    volatility: float,
    scale: float,
    gh_order: int = 64,
    gl_order: int = 64,
) -> tuple[float, float]:
    """Return (E[v(T)], Var(v(T))) for the DDS clock under the OU driver."""

    if alpha1 == 0.0 and alpha2 == 0.0:
        raise ValueError("at least one alpha must be nonzero")
    base = alpha1**2 * sigma1**2 + alpha2**2 * sigma2**2
    coeff = 2.0 * alpha1 * alpha2 * sigma1 * sigma2
    if coeff == 0.0:
        return base * maturity, 0.0
    mean_a, var_a = ou_occupation_moments(
        maturity, x0=x0, kappa=kappa, x_bar=x_bar, volatility=volatility, scale=scale,
        gh_order=gh_order, gl_order=gl_order,
    )
    return base * maturity + coeff * mean_a, coeff**2 * var_a


def ou_fk_characteristic(
    xi: float,
    *,
    maturity: float,
    x0: float,
    kappa: float,
    x_bar: float,
    volatility: float,
    scale: float,
    n_grid: int = 800,
    margin: float = 8.0,
) -> complex:
    """phi(xi) = E[exp(i xi A_T)] under OU via the FK resolvent (callable drift)."""

    from phase6_fk import fk_characteristic

    _validate(kappa, x_bar, volatility, scale)
    return fk_characteristic(
        xi,
        maturity=maturity,
        x0=x0,
        drift=lambda g: kappa * (x_bar - g),
        volatility=volatility,
        scale=scale,
        n_grid=n_grid,
        margin=margin,
    )


__all__ = [
    "ou_clock_moments",
    "ou_digital_price",
    "ou_fk_characteristic",
    "ou_occupation_moments",
    "ou_rho_stationary_density",
    "ou_rho_transition_density",
    "ou_stationary_mean_var",
    "ou_transition_mean_var",
]
