"""Financial formulas for canonical one-phase Euler coordinates.

The functions in this module keep the auxiliary complex coordinate separate
from the financial interpretation.  The traded or priced factor is real:

    X_t = c tan(theta_t),  c > 0.

The phase is an invertible coordinate on ``(-pi/2, pi/2)``.
"""

from __future__ import annotations

import math


def _validate_option_inputs(
    *,
    normal_volatility: float,
    maturity: float,
    discount: float,
) -> float:
    """Validate normal-option inputs and return terminal standard deviation."""

    if not math.isfinite(normal_volatility) or normal_volatility < 0.0:
        raise ValueError("normal_volatility must be finite and nonnegative")
    if not math.isfinite(maturity) or maturity < 0.0:
        raise ValueError("maturity must be finite and nonnegative")
    if not math.isfinite(discount) or discount <= 0.0:
        raise ValueError("discount must be finite and strictly positive")
    return normal_volatility * math.sqrt(maturity)


def _standard_normal_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def _standard_normal_pdf(value: float) -> float:
    return math.exp(-0.5 * value * value) / math.sqrt(2.0 * math.pi)


def bachelier_call_price(
    forward: float,
    strike: float,
    *,
    normal_volatility: float,
    maturity: float,
    discount: float = 1.0,
) -> float:
    """Return the discounted Bachelier price of a European call."""

    standard_deviation = _validate_option_inputs(
        normal_volatility=normal_volatility,
        maturity=maturity,
        discount=discount,
    )
    if not math.isfinite(forward) or not math.isfinite(strike):
        raise ValueError("forward and strike must be finite")
    intrinsic = forward - strike
    if standard_deviation == 0.0:
        return discount * max(intrinsic, 0.0)
    standardized_moneyness = intrinsic / standard_deviation
    return discount * (
        intrinsic * _standard_normal_cdf(standardized_moneyness)
        + standard_deviation * _standard_normal_pdf(standardized_moneyness)
    )


def bachelier_call_delta(
    forward: float,
    strike: float,
    *,
    normal_volatility: float,
    maturity: float,
    discount: float = 1.0,
) -> float:
    """Return the derivative of the discounted call price with respect to forward."""

    standard_deviation = _validate_option_inputs(
        normal_volatility=normal_volatility,
        maturity=maturity,
        discount=discount,
    )
    if not math.isfinite(forward) or not math.isfinite(strike):
        raise ValueError("forward and strike must be finite")
    intrinsic = forward - strike
    if standard_deviation == 0.0:
        if intrinsic > 0.0:
            return discount
        if intrinsic < 0.0:
            return 0.0
        return 0.5 * discount
    return discount * _standard_normal_cdf(intrinsic / standard_deviation)


def bachelier_call_gamma(
    forward: float,
    strike: float,
    *,
    normal_volatility: float,
    maturity: float,
    discount: float = 1.0,
) -> float:
    """Return the second forward derivative of the discounted call price."""

    standard_deviation = _validate_option_inputs(
        normal_volatility=normal_volatility,
        maturity=maturity,
        discount=discount,
    )
    if not math.isfinite(forward) or not math.isfinite(strike):
        raise ValueError("forward and strike must be finite")
    if standard_deviation == 0.0:
        return 0.0
    standardized_moneyness = (forward - strike) / standard_deviation
    return (
        discount
        * _standard_normal_pdf(standardized_moneyness)
        / standard_deviation
    )


def phase_bachelier_call_price(
    theta: float,
    *,
    scale: float,
    strike: float,
    normal_volatility: float,
    maturity: float,
    discount: float = 1.0,
) -> float:
    """Evaluate a Bachelier call after the exact map ``forward = scale*tan(theta)``."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if not math.isfinite(theta) or not (-math.pi / 2.0 < theta < math.pi / 2.0):
        raise ValueError("theta must lie in (-pi/2, pi/2)")
    return bachelier_call_price(
        scale * math.tan(theta),
        strike,
        normal_volatility=normal_volatility,
        maturity=maturity,
        discount=discount,
    )


def scalar_delta_from_phase(
    theta: float,
    *,
    scale: float,
    phase_first: float,
) -> float:
    """Convert ``v_theta`` into ``V_x`` for ``x = scale*tan(theta)``."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if not math.isfinite(theta) or not (-math.pi / 2.0 < theta < math.pi / 2.0):
        raise ValueError("theta must lie in (-pi/2, pi/2)")
    if not math.isfinite(phase_first):
        raise ValueError("phase_first must be finite")
    return math.cos(theta) ** 2 * phase_first / scale


def scalar_gamma_from_phase(
    theta: float,
    *,
    scale: float,
    phase_first: float,
    phase_second: float,
) -> float:
    """Convert ``(v_theta, v_theta_theta)`` into ``V_xx``."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if not math.isfinite(theta) or not (-math.pi / 2.0 < theta < math.pi / 2.0):
        raise ValueError("theta must lie in (-pi/2, pi/2)")
    if not math.isfinite(phase_first) or not math.isfinite(phase_second):
        raise ValueError("phase derivatives must be finite")
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return (
        cosine**4 * phase_second
        - 2.0 * sine * cosine**3 * phase_first
    ) / scale**2


def phase_generator_action(
    theta: float,
    *,
    drift: float,
    volatility: float,
    scale: float,
    phase_first: float,
    phase_second: float,
) -> float:
    """Apply the phase generator to supplied first and second derivatives."""

    if not math.isfinite(phase_first) or not math.isfinite(phase_second):
        raise ValueError("phase derivatives must be finite")
    phase_drift, phase_diffusion = canonical_phase_coefficients(
        theta,
        drift=drift,
        volatility=volatility,
        scale=scale,
    )
    return (
        phase_drift * phase_first
        + 0.5 * phase_diffusion**2 * phase_second
    )


def canonical_phase_coefficients(
    theta: float,
    *,
    drift: float,
    volatility: float,
    scale: float,
) -> tuple[float, float]:
    """Return Itô drift and diffusion for ``theta = arctan(X / scale)``."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if not math.isfinite(drift):
        raise ValueError("drift must be finite")
    if not math.isfinite(volatility) or volatility < 0.0:
        raise ValueError("volatility must be finite and nonnegative")
    if not math.isfinite(theta) or not (-math.pi / 2.0 < theta < math.pi / 2.0):
        raise ValueError("theta must lie in (-pi/2, pi/2)")

    cosine = math.cos(theta)
    sine = math.sin(theta)
    phase_drift = (
        (drift / scale) * cosine**2
        - (volatility**2 / scale**2) * sine * cosine**3
    )
    phase_diffusion = (volatility / scale) * cosine**2
    return phase_drift, phase_diffusion


__all__ = [
    "bachelier_call_delta",
    "bachelier_call_gamma",
    "bachelier_call_price",
    "canonical_phase_coefficients",
    "phase_bachelier_call_price",
    "phase_generator_action",
    "scalar_delta_from_phase",
    "scalar_gamma_from_phase",
]
