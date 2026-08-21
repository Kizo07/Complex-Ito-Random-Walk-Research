"""Vanilla spread/basket options under stochastic correlation: COS on the clock.

Model (Milestone 3, forward measure, Bachelier convention):

    dF1 = sigma1 dW1,
    dF2 = sigma2 (rho_t dW1 + sqrt(1 - rho_t**2) dW2),
    rho_t = X_t / sqrt(X_t**2 + c**2),   X_t = x0 + drift*t + vol*W_t,

with the correlation driver W independent of (W1, W2).  For any linear
combination Z = alpha1 F1 + alpha2 F2, conditional Gaussianity plus the
Dambis-Dubins-Schwarz theorem give

    Z_T | rho  ~  N(z0, v),   v = beta*T + alpha*A_T,
    beta = alpha1**2 sigma1**2 + alpha2**2 sigma2**2,
    alpha = 2 alpha1 alpha2 sigma1 sigma2,   A_T = int_0^T rho_s ds.

The new content of this module is the **exact one-dimensional characteristic
function of Z_T**: because A_T has bounded support, its Laplace transform

    L_A(s) = E[exp(-s A_T)],   s real,

exists for every real s and is computed by ONE forward Feynman-Kac solve
with the *real* potential -s f(x) (no oscillation).  Then

    phi_Z(u) = exp(i u z0 - u**2 beta T / 2) * L_A(alpha u**2 / 2),

and European vanilla prices follow by the Fang-Oosterlee COS inversion
(Fang & Oosterlee 2008, SIAM J. Sci. Comput. 31:826-848).  The pricing path
is fully deterministic: N COS modes each cost one sparse CN PDE solve.

Semi-analytic Greeks follow from the clock density of Milestone 4:
delta = E[Phi(d(v))], gamma = E[phi(d)/sqrt(v)],
vega_sigma_i = E[phi(d)/(2 sqrt(v)) * dv/dsigma_i], with
dv/dsigma_1 = 2 alpha1 sigma1 T + 2 alpha2 sigma1 A_T and symmetric for i=2.
"""

from __future__ import annotations

import math
from typing import Callable

import numpy as np
from scipy.optimize import brentq

import phase7_term_structure as p7

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _standard_normal_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def _standard_normal_pdf(value: float) -> float:
    return math.exp(-0.5 * value * value) / SQRT_2PI


def mgf_A(
    s: float,
    *,
    maturity: float,
    x0: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    scale: float,
    n_steps: int = 300,
    n_grid: int = 800,
    margin: float = 8.0,
) -> float:
    """L_A(s) = E[exp(-s A_T)] via forward FK with real potential -s f(x).

    Exists for every real s because |A_T| < T (bounded factor); the result
    satisfies |L_A(s)| <= e^{|s| T}.  Real potential means no oscillation:
    this is numerically gentler than the characteristic-function route.
    """

    if not math.isfinite(s):
        raise ValueError("s must be finite")
    interior, _h = p7.fk_grid_domain(
        maturity, x0, drift=drift, volatility=volatility,
        n_grid=n_grid, margin=margin,
    )
    q_values = -s * interior / np.sqrt(interior**2 + scale**2)
    value = p7.forward_fk_tilted_mass(
        q_values.astype(complex),
        interior=interior,
        maturity=maturity,
        x0=x0,
        drift=drift,
        volatility=volatility,
        n_steps=n_steps,
    )
    if abs(value.imag) > 1e-8 * max(1.0, abs(value.real)):
        raise ArithmeticError(f"real-potential solve produced imaginary part {value.imag}")
    bound = math.exp(abs(s) * maturity)
    if not (-1e-6 <= value.real <= bound + 1e-6):
        raise ArithmeticError(f"L_A({s}) = {value.real} outside [0, e^|s|T]")
    return float(value.real)


def linear_combo_characteristic(
    u: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    beta: float,
    alpha: float,
    x0: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    scale: float,
    n_steps: int = 300,
    n_grid: int = 800,
    margin: float = 8.0,
) -> complex:
    """Exact characteristic function of the discounted Z_T under the clock.

    phi(u) = E[e^{-rT} e^{i u Z_T}]
           = e^{-rT} e^{i u z0 - u^2 beta T / 2} L_A(alpha u^2 / 2).
    """

    if not math.isfinite(u):
        raise ValueError("u must be finite")
    laplace = mgf_A(
        0.5 * u * u * alpha,
        maturity=maturity, x0=x0, drift=drift, volatility=volatility,
        scale=scale, n_steps=n_steps, n_grid=n_grid, margin=margin,
    )
    return (
        math.exp(-rate * maturity)
        * np.exp(1j * u * z0 - 0.5 * u * u * beta * maturity)
        * laplace
    )


def bachelier_call(z0: float, var: float, strike: float) -> float:
    """Bachelier call price for N(z0, var) at zero discount."""

    if not math.isfinite(var) or var < 0.0:
        raise ValueError("var must be finite and nonnegative")
    if var == 0.0:
        return max(z0 - strike, 0.0)
    sd = math.sqrt(var)
    d = (z0 - strike) / sd
    return sd * _standard_normal_pdf(d) + (z0 - strike) * _standard_normal_cdf(d)


def bachelier_put(z0: float, var: float, strike: float) -> float:
    """Bachelier put price for N(z0, var) at zero discount."""

    if not math.isfinite(var) or var < 0.0:
        raise ValueError("var must be finite and nonnegative")
    if var == 0.0:
        return max(strike - z0, 0.0)
    sd = math.sqrt(var)
    d = (z0 - strike) / sd
    return sd * _standard_normal_pdf(d) + (strike - z0) * _standard_normal_cdf(d)


def cos_call_price(
    strike: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    beta: float,
    alpha: float,
    x0: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    scale: float,
    n_modes: int = 128,
    truncation: float = 10.0,
    n_steps: int = 300,
    n_grid: int = 800,
    margin: float = 8.0,
) -> float:
    """COS price of a call on Z = alpha1 F1 + alpha2 F2 at expiry T.

    V = e^{-rT} sum'_{k=0}^{N-1} Re[phi_Z(theta_k) e^{-i k pi a/(b-a)}] W_k,
    theta_k = k pi / (b - a), with payoff coefficients (derived in-module)

        W_0 = (b - K)^2 / 2,
        W_k = ((-1)^k - cos(theta_k (K - a))) / theta_k**2,  k >= 1,

    where the prime halves the k = 0 weight and [a, b] is the truncation
    interval z0 +/- truncation * sqrt(beta*T + |alpha|*T).
    """

    if not math.isfinite(strike):
        raise ValueError("strike must be finite")
    if n_modes < 16:
        raise ValueError("n_modes must be at least 16")
    v_max = beta * maturity + abs(alpha) * maturity
    half = truncation * math.sqrt(max(v_max, 1e-12))
    a, b = z0 - half, z0 + half
    span = b - a

    ks = np.arange(n_modes)
    thetas = ks * math.pi / span
    phi = np.array([
        linear_combo_characteristic(
            float(t),
            z0=z0, maturity=maturity, rate=rate, beta=beta, alpha=alpha,
            x0=x0, drift=drift, volatility=volatility, scale=scale,
            n_steps=n_steps, n_grid=n_grid, margin=margin,
        )
        for t in thetas
    ])
    # Raw payoff cosine coefficients G_k = int_a^b (z-K)^+ cos(theta_k(z-a)) dz
    # for arbitrary strike relative to the truncation band:
    #   K >= b : payoff vanishes on [a, b] (band too narrow -> error),
    #   a <= K <= b : G_0=(b-K)^2/2,  G_k=((-1)^k - cos(theta_k(K-a)))/theta_k^2,
    #   K < a : payoff is z-K on the whole band,
    #         G_0=((b-K)^2-(a-K)^2)/2,  G_k=((-1)^k - 1)/theta_k^2.
    if strike >= b:
        raise ValueError(
            "strike at or above the truncation upper edge; increase truncation"
        )
    w = np.empty(n_modes)
    if strike >= a:
        w[0] = 0.5 * (b - strike) ** 2
        w[1:] = ((-1.0) ** ks[1:] - np.cos(thetas[1:] * (strike - a))) / thetas[1:] ** 2
    else:
        w[0] = 0.5 * ((b - strike) ** 2 - (a - strike) ** 2)
        w[1:] = ((-1.0) ** ks[1:] - 1.0) / thetas[1:] ** 2
    terms = np.real(phi * np.exp(-1j * thetas * a)) * w
    # Standard COS convention: the k = 0 term carries half weight, and every
    # coefficient carries the factor 2 / span.
    terms[0] *= 0.5
    return max(float(np.sum(terms)) * (2.0 / span), 0.0)


def cos_put_price(
    strike: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    beta: float,
    alpha: float,
    x0: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    scale: float,
    n_modes: int = 128,
    truncation: float = 10.0,
    n_steps: int = 300,
    n_grid: int = 800,
    margin: float = 8.0,
) -> float:
    """COS price of a put on Z via put-call parity from the call price."""

    call = cos_call_price(
        strike,
        z0=z0, maturity=maturity, rate=rate, beta=beta, alpha=alpha,
        x0=x0, drift=drift, volatility=volatility, scale=scale,
        n_modes=n_modes, truncation=truncation,
        n_steps=n_steps, n_grid=n_grid, margin=margin,
    )
    return call - math.exp(-rate * maturity) * (z0 - strike)


def constant_rho_call(
    strike: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    rho_const: float,
    sigma1: float,
    sigma2: float,
    alpha1: float,
    alpha2: float,
) -> float:
    """Discounted Bachelier call on Z at constant correlation rho_const."""

    if not (-1.0 <= rho_const <= 1.0):
        raise ValueError("rho_const must lie in [-1, 1]")
    beta = alpha1**2 * sigma1**2 + alpha2**2 * sigma2**2
    coeff = 2.0 * alpha1 * alpha2 * sigma1 * sigma2
    var = (beta + coeff * rho_const) * maturity
    if var <= 0.0:
        raise ValueError("constant-correlation variance must be positive")
    return math.exp(-rate * maturity) * bachelier_call(z0, var, strike)


def implied_correlation(
    target_price: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    sigma1: float,
    sigma2: float,
    alpha1: float,
    alpha2: float,
    strike: float,
) -> float:
    """Constant correlation reproducing a Bachelier call price (Brent)."""

    def objective(rho: float) -> float:
        return constant_rho_call(
            strike,
            z0=z0, maturity=maturity, rate=rate, rho_const=rho,
            sigma1=sigma1, sigma2=sigma2, alpha1=alpha1, alpha2=alpha2,
        ) - target_price

    lo = constant_rho_call(
        strike, z0=z0, maturity=maturity, rate=rate, rho_const=-0.999999,
        sigma1=sigma1, sigma2=sigma2, alpha1=alpha1, alpha2=alpha2,
    )
    hi = constant_rho_call(
        strike, z0=z0, maturity=maturity, rate=rate, rho_const=0.999999,
        sigma1=sigma1, sigma2=sigma2, alpha1=alpha1, alpha2=alpha2,
    )
    # For baskets (alpha > 0) prices increase in rho; for spreads they
    # decrease -- compare against the unordered range.
    if not (min(lo, hi) - 1e-12 <= target_price <= max(lo, hi) + 1e-12):
        raise ValueError("target price outside the constant-correlation price range")
    root = brentq(objective, -0.999999, 0.999999, xtol=1e-12)
    return float(root)


def implied_correlation_basket(
    target_price: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    sigma1: float,
    sigma2: float,
    strike: float,
) -> float:
    """Constant correlation reproducing a basket call price (weights +1, +1)."""

    return implied_correlation(
        target_price,
        z0=z0, maturity=maturity, rate=rate,
        sigma1=sigma1, sigma2=sigma2,
        alpha1=1.0, alpha2=1.0, strike=strike,
    )


def clock_density_greeks(
    strike: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    beta: float,
    alpha: float,
    sigma1: float,
    sigma2: float,
    alpha1: float,
    alpha2: float,
    a_grid: np.ndarray,
    p_grid: np.ndarray,
) -> dict[str, float]:
    """Delta/Gamma/vegas from the Milestone-4 clock density of A_T.

    With g(v) the undiscounted Bachelier call in variance v,
    d = (z0 - K)/sqrt(v):
        delta      = E[Phi(d)]
        gamma      = E[phi(d)/sqrt(v)]
        vega_s1    = E[phi(d)/(2 sqrt(v)) * (2 alpha1 sigma1 T + 2 alpha2 sigma1 A_T)]
        vega_s2    = symmetric.
    All discounted by e^{-rT}; the clock density integrates to 1.
    """

    clocks = beta * maturity + alpha * a_grid
    if np.any(clocks <= 0.0):
        raise ValueError("clock grid must be strictly positive for Greeks")
    root_v = np.sqrt(clocks)
    d = (z0 - strike) / root_v
    pdf_d = np.exp(-0.5 * d * d) / SQRT_2PI
    from scipy.special import ndtr

    delta = float(np.trapezoid(ndtr(d) * p_grid, a_grid))
    gamma = float(np.trapezoid(pdf_d / root_v * p_grid, a_grid))
    # v = beta*T + alpha*A_T with beta = a1^2 s1^2 + a2^2 s2^2 and
    # alpha = 2 a1 a2 s1 s2, so
    #   dv/ds1 = 2 a1^2 s1 T + 2 a1 a2 s2 A_T,
    #   dv/ds2 = 2 a2^2 s2 T + 2 a1 a2 s1 A_T.
    dv_d1 = 2.0 * alpha1**2 * sigma1 * maturity + 2.0 * alpha1 * alpha2 * sigma2 * a_grid
    dv_d2 = 2.0 * alpha2**2 * sigma2 * maturity + 2.0 * alpha1 * alpha2 * sigma1 * a_grid
    vega_common = pdf_d / (2.0 * root_v) * p_grid
    vega1 = float(np.trapezoid(vega_common * dv_d1, a_grid))
    vega2 = float(np.trapezoid(vega_common * dv_d2, a_grid))
    disc = math.exp(-rate * maturity)
    return {
        "delta": disc * delta,
        "gamma": disc * gamma,
        "vega_sigma1": disc * vega1,
        "vega_sigma2": disc * vega2,
    }


def clock_quadrature_call_price(
    strike: float,
    *,
    z0: float,
    maturity: float,
    rate: float,
    beta: float,
    alpha: float,
    x0: float,
    drift: float,
    volatility: float,
    scale: float,
    n_modes: int = 64,
    n_points: int = 801,
    n_grid: int = 600,
    margin: float = 8.0,
) -> tuple[float, tuple[np.ndarray, np.ndarray]]:
    """Deterministic call price by quadrature over the Milestone-4 clock law.

    V = e^{-rT} int Bachelier(z0, beta*T + alpha*a, K) p_{A_T}(a) da, with
    p_{A_T} the truncated-Fourier density built from oscillating-frequency
    characteristic values phi_A(xi) at real xi only (|phi_A| <= 1).  This
    route avoids the exponential tilting that makes the real-potential
    resolvent L_A(s) delicate at large |s| and is therefore the primary
    deterministic pricer; the resolvent/COS route is exact in the same
    regime and cheaper when many strikes share one characteristic function.
    Returns the price and the (a_grid, p_grid) used.
    """

    import phase6_fk as p6f

    if not math.isfinite(strike):
        raise ValueError("strike must be finite")
    if not math.isfinite(drift):
        raise ValueError("drift must be a finite constant for this route")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be a finite positive constant")
    a_grid, p_grid = p6f.clock_density_grid(
        maturity=maturity, x0=x0, drift=drift, volatility=volatility,
        scale=scale, n_modes=n_modes, n_points=n_points, n_grid=n_grid,
        margin=margin,
    )
    clocks = beta * maturity + alpha * a_grid
    payoff = np.array([
        bachelier_call(z0, max(float(v), 1e-12), strike) for v in clocks
    ])
    price = math.exp(-rate * maturity) * float(np.trapezoid(payoff * p_grid, a_grid))
    return price, (a_grid, p_grid)


__all__ = [
    "bachelier_call",
    "bachelier_put",
    "clock_density_greeks",
    "constant_rho_call",
    "cos_call_price",
    "cos_put_price",
    "implied_correlation",
    "linear_combo_characteristic",
    "mgf_A",
]
