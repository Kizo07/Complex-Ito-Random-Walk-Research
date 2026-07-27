"""Exact laws for the bounded correlation coordinate of a drifted Brownian factor.

The traded/estimated factor is real:

    X_t = x_0 + mu*t + sigma*W_t,   c > 0.

The one-phase Euler coordinate is theta_t = arctan(X_t / c) in (-pi/2, pi/2),
and the bounded correlation coordinate is

    rho_t = sin(theta_t) = X_t / sqrt(X_t**2 + c**2)  in (-1, 1).

Because rho is a strictly increasing deterministic function of X, every
first-passage statement for rho to a level rho* is *exactly* a first-passage
statement for the drifted Brownian motion X to the conjugate level

    x* = c * rho* / sqrt(1 - rho**2),

so the reflection principle gives closed-form correlation-barrier laws.
All formulas in this module are exact distributional identities, not
discretizations.
"""

from __future__ import annotations

import math


def _validate_scale(scale: float) -> None:
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")


def _validate_rho(rho: float) -> None:
    if not math.isfinite(rho) or not (-1.0 < rho < 1.0):
        raise ValueError("rho must lie in (-1, 1)")


def _standard_normal_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def rho_from_x(x: float, *, scale: float) -> float:
    """Return rho = x / sqrt(x**2 + scale**2) = sin(arctan(x / scale))."""

    _validate_scale(scale)
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    return x / math.sqrt(x * x + scale * scale)


def x_from_rho(rho: float, *, scale: float) -> float:
    """Return the conjugate level x = scale * rho / sqrt(1 - rho**2)."""

    _validate_scale(scale)
    _validate_rho(rho)
    return scale * rho / math.sqrt(1.0 - rho * rho)


def rho_ito_drift(rho: float, *, drift: float, volatility: float, scale: float) -> float:
    """Ito drift of rho_t under dX = drift*dt + volatility*dW.

    With f(x) = x / sqrt(x**2 + scale**2),
    f'(x)  = scale**2 / (x**2 + scale**2)**(3/2) = (1 - rho**2)**(3/2) / scale,
    f''(x) = -3 * rho * (1 - rho**2)**2 / scale**2.
    """

    _validate_scale(scale)
    _validate_rho(rho)
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility < 0.0:
        raise ValueError("volatility must be finite and nonnegative")
    one_minus_sq = 1.0 - rho * rho
    return (
        (drift / scale) * one_minus_sq**1.5
        - 1.5 * (volatility**2 / scale**2) * rho * one_minus_sq**2
    )


def rho_ito_diffusion(rho: float, *, volatility: float, scale: float) -> float:
    """Ito diffusion coefficient of rho_t: (volatility/scale)*(1-rho**2)**(3/2)."""

    _validate_scale(scale)
    _validate_rho(rho)
    if not math.isfinite(volatility) or volatility < 0.0:
        raise ValueError("volatility must be finite and nonnegative")
    return (volatility / scale) * (1.0 - rho * rho) ** 1.5


def rho_transition_density(
    rho: float,
    *,
    maturity: float,
    rho0: float,
    drift: float,
    volatility: float,
    scale: float,
) -> float:
    """Exact time-t density of rho_t (Gaussian in the conjugate coordinate).

    p_t(rho) = (scale / (1-rho**2)**(3/2)) * Normal_pdf(x(rho); x0+drift*t, volatility**2*t)
    with x(rho) = scale*rho/sqrt(1-rho**2).  The factor scale/(1-rho**2)**(3/2)
    is the Jacobian dx/d(rho).
    """

    _validate_scale(scale)
    _validate_rho(rho)
    _validate_rho(rho0)
    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    x = x_from_rho(rho, scale=scale)
    x0 = x_from_rho(rho0, scale=scale)
    sd = volatility * math.sqrt(maturity)
    z = (x - x0 - drift * maturity) / sd
    jacobian = scale / (1.0 - rho * rho) ** 1.5
    return jacobian * math.exp(-0.5 * z * z) / (sd * math.sqrt(2.0 * math.pi))


def brownian_hitting_cdf(maturity: float, *, distance: float, drift: float, volatility: float) -> float:
    """P(tau <= T) for drifted Brownian motion hitting an upper level at given distance.

    For Y_t = drift*t + volatility*W_t and level distance > 0 above the start,

        P(tau <= T) = Phi((drift*T - distance)/(volatility*sqrt(T)))
                    + exp(2*drift*distance/volatility**2)
                      * Phi(-(drift*T + distance)/(volatility*sqrt(T))).
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    root_t = math.sqrt(maturity)
    first = _standard_normal_cdf((drift * maturity - distance) / (volatility * root_t))
    second = (
        math.exp(2.0 * drift * distance / volatility**2)
        * _standard_normal_cdf(-(drift * maturity + distance) / (volatility * root_t))
    )
    return first + second


def brownian_hitting_density(t: float, *, distance: float, drift: float, volatility: float) -> float:
    """(Possibly defective) inverse-Gaussian density of the hitting time.

        f(t) = distance / (volatility * sqrt(2*pi*t**3))
               * exp(-(distance - drift*t)**2 / (2*volatility**2*t)).

    Integrates to min(1, exp(2*drift*distance/volatility**2)).
    """

    if not math.isfinite(t) or t <= 0.0:
        raise ValueError("t must be finite and strictly positive")
    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    return (
        distance
        / (volatility * math.sqrt(2.0 * math.pi * t**3))
        * math.exp(-((distance - drift * t) ** 2) / (2.0 * volatility**2 * t))
    )


def perpetual_hitting_probability(*, distance: float, drift: float, volatility: float) -> float:
    """P(tau < infinity) = 1 for drift >= 0, else exp(2*drift*distance/volatility**2)."""

    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    if drift >= 0.0:
        return 1.0
    return math.exp(2.0 * drift * distance / volatility**2)


def first_exit_probability_upper(
    *, start: float, lower: float, upper: float, drift: float, volatility: float
) -> float:
    """P(hit upper before lower) for drifted Brownian motion via the scale function.

    Scale function s(x) = exp(-2*drift*x/volatility**2) (s(x) = x when drift = 0):

        P = (s(start) - s(lower)) / (s(upper) - s(lower)).
    """

    if not (lower < start < upper):
        raise ValueError("need lower < start < upper")
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    if drift == 0.0:
        return (start - lower) / (upper - lower)
    rate = -2.0 * drift / volatility**2
    s_start = math.exp(rate * start)
    s_lower = math.exp(rate * lower)
    s_upper = math.exp(rate * upper)
    return (s_start - s_lower) / (s_upper - s_lower)


def correlation_barrier_distance(
    *, rho0: float, rho_star: float, scale: float
) -> float:
    """Signed conjugate distance x(rho_star) - x(rho0) between two correlation levels."""

    _validate_rho(rho0)
    _validate_rho(rho_star)
    return x_from_rho(rho_star, scale=scale) - x_from_rho(rho0, scale=scale)


def _validate_rate(rate: float) -> None:
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")


def _validate_driver(drift: float, volatility: float) -> None:
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")


def discounted_hitting_laplace(
    maturity: float, *, distance: float, drift: float, volatility: float, rate: float
) -> float:
    """E[exp(-rate*tau) * 1{tau <= T}] for drifted Brownian first passage.

    With gamma = sqrt(drift**2 + 2*rate*volatility**2),

        E = exp(-distance*(gamma - drift)/volatility**2)
            * [Phi((gamma*T - distance)/(volatility*sqrt(T)))
               + exp(2*gamma*distance/volatility**2)
                 * Phi(-(gamma*T + distance)/(volatility*sqrt(T)))].

    At rate = 0 this reduces to the hitting CDF; as T -> infinity it reduces
    to the classical Laplace transform exp(-distance*(gamma-drift)/volatility**2).
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    _validate_driver(drift, volatility)
    _validate_rate(rate)
    gamma = math.sqrt(drift * drift + 2.0 * rate * volatility**2)
    root_t = math.sqrt(maturity)
    prefactor = math.exp(-distance * (gamma - drift) / volatility**2)
    first = _standard_normal_cdf((gamma * maturity - distance) / (volatility * root_t))
    second = (
        math.exp(2.0 * gamma * distance / volatility**2)
        * _standard_normal_cdf(-(gamma * maturity + distance) / (volatility * root_t))
    )
    return prefactor * (first + second)


def correlation_digital_price(
    rho_star: float,
    *,
    maturity: float,
    rho0: float,
    drift: float,
    volatility: float,
    scale: float,
    rate: float,
) -> float:
    """Price of a digital paying 1{rho_T >= rho_star} at time T."""

    _validate_scale(scale)
    _validate_rho(rho0)
    _validate_rho(rho_star)
    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    _validate_driver(drift, volatility)
    _validate_rate(rate)
    distance = correlation_barrier_distance(rho0=rho0, rho_star=rho_star, scale=scale)
    probability = _standard_normal_cdf(
        (drift * maturity - distance) / (volatility * math.sqrt(maturity))
    )
    return math.exp(-rate * maturity) * probability


def one_touch_price_at_expiry(
    rho_star: float,
    *,
    maturity: float,
    rho0: float,
    drift: float,
    volatility: float,
    scale: float,
    rate: float,
) -> float:
    """Price of a one-touch paying 1{tau <= T} at expiry T (rho_star > rho0)."""

    _validate_scale(scale)
    _validate_rho(rho0)
    _validate_rho(rho_star)
    _validate_rate(rate)
    if rho_star <= rho0:
        raise ValueError("one-touch requires rho_star > rho0")
    distance = correlation_barrier_distance(rho0=rho0, rho_star=rho_star, scale=scale)
    return math.exp(-rate * maturity) * brownian_hitting_cdf(
        maturity, distance=distance, drift=drift, volatility=volatility
    )


def one_touch_price_at_hit(
    rho_star: float,
    *,
    maturity: float,
    rho0: float,
    drift: float,
    volatility: float,
    scale: float,
    rate: float,
) -> float:
    """Price of a one-touch paying 1 at the hitting time, if hit by T (rho_star > rho0)."""

    _validate_scale(scale)
    _validate_rho(rho0)
    _validate_rho(rho_star)
    _validate_rate(rate)
    if rho_star <= rho0:
        raise ValueError("one-touch requires rho_star > rho0")
    distance = correlation_barrier_distance(rho0=rho0, rho_star=rho_star, scale=scale)
    return discounted_hitting_laplace(
        maturity, distance=distance, drift=drift, volatility=volatility, rate=rate
    )


def range_accrual_price(
    rho_lower: float,
    rho_upper: float,
    *,
    pay_dates: tuple[float, ...] | list[float],
    rho0: float,
    drift: float,
    volatility: float,
    scale: float,
    rate: float,
) -> float:
    """Price of sum_i 1{rho_lower <= rho_{t_i} <= rho_upper} paid at each t_i.

    Either level may be given as -1 or 1 (open band end), recovering a
    one-sided digital on that date.
    """

    _validate_scale(scale)
    _validate_rho(rho0)
    if not (-1.0 <= rho_lower < rho_upper <= 1.0):
        raise ValueError("need -1 <= rho_lower < rho_upper <= 1")
    _validate_driver(drift, volatility)
    _validate_rate(rate)
    if len(pay_dates) == 0:
        raise ValueError("pay_dates must be nonempty")
    x0 = x_from_rho(rho0, scale=scale)
    x_lower = x_from_rho(rho_lower, scale=scale) if rho_lower > -1.0 else -math.inf
    x_upper = x_from_rho(rho_upper, scale=scale) if rho_upper < 1.0 else math.inf
    total = 0.0
    previous = 0.0
    for date in pay_dates:
        if not math.isfinite(date) or date <= 0.0 or date <= previous:
            raise ValueError("pay_dates must be strictly increasing and positive")
        previous = date
        sd = volatility * math.sqrt(date)
        upper_cdf = _standard_normal_cdf((x_upper - x0 - drift * date) / sd)
        lower_cdf = _standard_normal_cdf((x_lower - x0 - drift * date) / sd)
        total += math.exp(-rate * date) * (upper_cdf - lower_cdf)
    return total


__all__ = [
    "brownian_hitting_cdf",
    "brownian_hitting_density",
    "correlation_barrier_distance",
    "correlation_digital_price",
    "discounted_hitting_laplace",
    "first_exit_probability_upper",
    "one_touch_price_at_expiry",
    "one_touch_price_at_hit",
    "perpetual_hitting_probability",
    "range_accrual_price",
    "rho_from_x",
    "rho_ito_diffusion",
    "rho_ito_drift",
    "rho_transition_density",
    "x_from_rho",
]
