"""Continuous corridor occupation laws and prices via the FK resolvent.

The corridor occupation time

    O_T = integral_0^T 1{x_lower <= X_t <= x_upper} dt,

with X drifted Brownian motion, is the occupation time of the correlation
band {rho_lower <= rho_t <= rho_upper} under the conjugate map
x(rho) = scale*rho/sqrt(1-rho**2).  O_T has bounded support [0, T], so its
density is the Fourier series

    p(o) = (1/T) * [1 + 2 Re sum_{k>=1} phi(2 pi k / T) exp(-i 2 pi k o / T)],

with phi from the Milestone 4 Feynman-Kac solver with an indicator
potential.  Everything in the pricing path is deterministic.
"""

from __future__ import annotations

import math

import numpy as np
import scipy.sparse as sp
from scipy.integrate import quad

from phase6_fk import fk_characteristic

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _standard_normal_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def corridor_potential(x_lower: float, x_upper: float):
    """Return the indicator potential 1{x_lower <= x <= x_upper} as a callable."""

    if not (math.isfinite(x_lower) and math.isfinite(x_upper)) and not (
        x_lower == -math.inf or x_upper == math.inf
    ):
        raise ValueError("corridor bounds must be finite or infinite")
    if not x_lower < x_upper:
        raise ValueError("need x_lower < x_upper")

    def potential(grid: np.ndarray) -> np.ndarray:
        return ((grid >= x_lower) & (grid <= x_upper)).astype(float)

    return potential


def corridor_characteristic(
    xi: float,
    *,
    maturity: float,
    x_lower: float,
    x_upper: float,
    x0: float,
    drift: float,
    volatility: float,
    n_grid: int = 800,
    margin: float = 8.0,
) -> complex:
    """phi(xi) = E[exp(i xi O_T)] for the corridor occupation time."""

    return fk_characteristic(
        xi,
        maturity=maturity,
        x0=x0,
        drift=drift,
        volatility=volatility,
        scale=1.0,  # unused with an explicit potential
        n_grid=n_grid,
        margin=margin,
        potential=corridor_potential(x_lower, x_upper),
    )


def corridor_survival_atom(
    *,
    maturity: float,
    x_lower: float,
    x_upper: float,
    x0: float,
    drift: float,
    volatility: float,
    n_grid: int = 1600,
) -> float:
    """Atom at O_T = T: probability of never leaving the corridor by T.

    Bounded corridor: absorbing-boundary PDE on [x_lower, x_upper] with zero
    potential, u(T, x0).  Unbounded corridor: the Milestone 1 perpetual
    first-passage formula.  Requires x_lower < x0 < x_upper.
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    if not (x_lower <= x0 <= x_upper):
        raise ValueError("need x_lower <= x0 <= x_upper")

    if x0 == x_lower or x0 == x_upper:
        return 0.0  # boundary start leaves immediately, no atom at T

    if not math.isfinite(x_lower) and math.isfinite(x_upper):
        # Corridor (-inf, x_upper]: atom = never cross up to x_upper.
        if drift >= 0.0:
            return 0.0
        return 1.0 - math.exp(2.0 * drift * (x_upper - x0) / volatility**2)
    if not math.isfinite(x_upper) and math.isfinite(x_lower):
        # Corridor [x_lower, +inf): atom = never cross down to x_lower.
        if drift <= 0.0:
            return 0.0
        return 1.0 - math.exp(-2.0 * drift * (x0 - x_lower) / volatility**2)
    if not math.isfinite(x_lower) and not math.isfinite(x_upper):
        return 1.0

    # Crank-Nicolson time-stepping (unconditionally stable; the expm route is
    # slow here because the corridor grid is stiff).
    grid = np.linspace(x_lower, x_upper, n_grid)
    h = grid[1] - grid[0]
    interior = grid[1:-1]
    n_in = interior.size
    d2 = sp.diags(
        [np.ones(n_in - 1) / h**2, -2.0 * np.ones(n_in) / h**2, np.ones(n_in - 1) / h**2],
        [-1, 0, 1], format="csc",
    )
    d1 = sp.diags(
        [-np.ones(n_in - 1) / (2.0 * h), np.ones(n_in - 1) / (2.0 * h)],
        [-1, 1], format="csc",
    )
    operator = 0.5 * volatility**2 * d2 + drift * d1
    n_steps = min(50000, max(200, int(round(maturity / h))))
    step = maturity / n_steps
    identity = sp.identity(n_in, format="csc")
    lhs = (identity - 0.5 * step * operator).tocsc()
    rhs = identity + 0.5 * step * operator
    factorized = sp.linalg.factorized(lhs)
    u = np.ones(n_in)
    for _ in range(n_steps):
        u = factorized(rhs @ u)
    position = (x0 - interior[0]) / h
    left = int(np.clip(np.floor(position), 0, n_in - 2))
    weight = position - left
    return float((1.0 - weight) * u[left] + weight * u[left + 1])


def corridor_density_grid(
    *,
    maturity: float,
    x_lower: float,
    x_upper: float,
    x0: float,
    drift: float,
    volatility: float,
    n_modes: int = 96,
    n_points: int = 801,
    n_grid: int = 800,
    margin: float = 8.0,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return (o_grid, p_grid, atom): continuous-part density of O_T and the atom at T.

    The atom P(O_T = T) is computed deterministically and subtracted from
    every Fourier mode, so p_grid integrates to 1 - atom and converges
    quickly.  Prices reassemble both parts.  Starting outside the corridor
    (which adds an atom at 0) is rejected explicitly.
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not (x_lower <= x0 <= x_upper):
        raise ValueError("need x_lower <= x0 <= x_upper (inside or boundary start)")
    if n_modes < 8:
        raise ValueError("n_modes must be at least 8")
    if n_points < 101:
        raise ValueError("n_points must be at least 101")
    atom = corridor_survival_atom(
        maturity=maturity, x_lower=x_lower, x_upper=x_upper,
        x0=x0, drift=drift, volatility=volatility,
    )
    phis = np.empty(n_modes + 1, dtype=complex)
    phis[0] = 1.0
    for k in range(1, n_modes + 1):
        # At xi_k = 2 pi k / T the atom contributes exp(i xi_k T) = 1 times
        # its mass; subtract it to leave the continuous part's transform.
        phis[k] = corridor_characteristic(
            2.0 * math.pi * k / maturity,
            maturity=maturity, x_lower=x_lower, x_upper=x_upper,
            x0=x0, drift=drift, volatility=volatility,
            n_grid=n_grid, margin=margin,
        ) - atom
    o_grid = np.linspace(0.0, maturity, n_points)
    phases = np.exp(-2j * math.pi * np.outer(o_grid, np.arange(1, n_modes + 1)) / maturity)
    p_grid = (1.0 - atom + 2.0 * np.real(phases @ phis[1:])) / maturity
    return o_grid, p_grid, atom


def mean_occupation(
    maturity: float,
    *,
    x_lower: float,
    x_upper: float,
    x0: float,
    drift: float,
    volatility: float,
) -> float:
    """E[O_T] = integral_0^T P(X_t in [x_lower, x_upper]) dt (exact quadrature)."""

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")

    def integrand(t: float) -> float:
        sd = volatility * math.sqrt(t)
        upper = _standard_normal_cdf((x_upper - x0 - drift * t) / sd)
        lower = _standard_normal_cdf((x_lower - x0 - drift * t) / sd)
        return upper - lower

    value, _ = quad(integrand, 0.0, maturity, epsabs=1e-12, limit=200)
    return value


def corridor_digital_price(
    kappa: float,
    *,
    maturity: float,
    rate: float,
    o_grid: np.ndarray,
    p_grid: np.ndarray,
    atom: float = 0.0,
) -> float:
    """Price of 1{O_T >= kappa*T} paid at T (continuous part + atom at T)."""

    if not (0.0 < kappa < 1.0):
        raise ValueError("kappa must lie in (0, 1)")
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    if not (0.0 <= atom < 1.0):
        raise ValueError("atom must lie in [0, 1)")
    tail = np.clip(o_grid - kappa * maturity, 0.0, None) > 0.0
    continuous = float(np.trapezoid(p_grid * tail.astype(float), o_grid))
    return math.exp(-rate * maturity) * (continuous + atom)


def corridor_call_price(
    kappa: float,
    *,
    maturity: float,
    rate: float,
    o_grid: np.ndarray,
    p_grid: np.ndarray,
    atom: float = 0.0,
) -> float:
    """Price of (O_T/T - kappa)^+ paid at T (continuous part + atom at T)."""

    if not (0.0 < kappa < 1.0):
        raise ValueError("kappa must lie in (0, 1)")
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    if not (0.0 <= atom < 1.0):
        raise ValueError("atom must lie in [0, 1)")
    payoff = np.clip(o_grid / maturity - kappa, 0.0, None)
    continuous = float(np.trapezoid(payoff * p_grid, o_grid))
    return math.exp(-rate * maturity) * (continuous + atom * (1.0 - kappa))


def arcsine_cdf(fraction: float) -> float:
    """Levy arcsine CDF of the occupation fraction of a half-line (driftless)."""

    if not (0.0 <= fraction <= 1.0):
        raise ValueError("fraction must lie in [0, 1]")
    return (2.0 / math.pi) * math.asin(math.sqrt(fraction))


__all__ = [
    "arcsine_cdf",
    "corridor_call_price",
    "corridor_characteristic",
    "corridor_density_grid",
    "corridor_digital_price",
    "corridor_potential",
    "corridor_survival_atom",
    "mean_occupation",
]
