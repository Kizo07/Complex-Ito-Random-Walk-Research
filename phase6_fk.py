"""Feynman-Kac resolvent computation of the full law of A_T = integral rho_s ds.

For xi real, u(t, x) = E_x[exp(i * xi * integral_0^t f(X_s) ds)] with
f(x) = x / sqrt(x**2 + scale**2) solves

    du/dt = (vol**2/2) u_xx + drift u_x + i xi f(x) u,   u(0, x) = 1.

The support of A_T is bounded in (-T, T), so the density of A_T is the
Fourier series

    p(a) = (1 / 2T) * sum_k phi(k pi / T) exp(-i k pi a / T),

with phi the PDE solution at (T, x0).  The PDE is discretized on a truncated
domain with homogeneous Dirichlet data (error at x0 bounded by the
boundary-reach probability; checked by doubling the margin) and integrated in
time by Krylov exponentiation (scipy.sparse.linalg.expm_multiply).

All pricing-path quantities here are deterministic; Monte Carlo appears only
in the notebook as an independent benchmark.
"""

from __future__ import annotations

import math

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

from phase6_joint import driftless_touch_probability

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _validate_driver(x0: float, drift: float, volatility: float, scale: float) -> None:
    if not math.isfinite(x0) or not math.isfinite(drift):
        raise ValueError("x0 and drift must be finite")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")


def _default_half_width(maturity: float, volatility: float, margin: float) -> float:
    return margin * volatility * math.sqrt(maturity) + 1.0


def fk_characteristic(
    xi: float,
    *,
    maturity: float,
    x0: float,
    drift,
    volatility: float,
    scale: float,
    n_grid: int = 800,
    margin: float = 8.0,
    potential=None,
) -> complex:
    """Characteristic function phi(xi) = E[exp(i xi A_T)] via the FK PDE.

    A_T = integral_0^T g(X_s) ds, where g defaults to the bounded correlation
    map f(x) = x/sqrt(x**2 + scale**2); pass ``potential`` (a callable on the
    interior grid, must be bounded) for other occupation functionals, e.g. a
    corridor indicator.  ``drift`` may be a constant or a callable on the
    interior grid (e.g. lambda g: kappa*(x_bar - g) for an OU driver).
    Solved on [x0 + E[X_T] +/- half_width], half_width =
    margin*volatility*sqrt(T) + 1, with second-order central differences and
    Krylov time integration.
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if not math.isfinite(x0):
        raise ValueError("x0 must be finite")
    if callable(drift):
        drift_values_mode = "callable"
    elif math.isfinite(drift):
        drift_values_mode = "constant"
    else:
        raise ValueError("drift must be finite or a callable on the grid")
    if not math.isfinite(volatility) or volatility <= 0.0:
        raise ValueError("volatility must be finite and strictly positive")
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if not math.isfinite(xi):
        raise ValueError("xi must be finite")
    if n_grid < 64:
        raise ValueError("n_grid must be at least 64")
    if margin < 4.0:
        raise ValueError("margin must be at least 4 for localization")

    drift_at_x0 = float(drift(np.array([x0]))[0]) if drift_values_mode == "callable" else drift
    center = x0 + drift_at_x0 * maturity
    half_width = _default_half_width(maturity, volatility, margin)
    x_lo, x_hi = center - half_width, center + half_width
    grid = np.linspace(x_lo, x_hi, n_grid)
    h = grid[1] - grid[0]

    # Interior nodes; Dirichlet boundaries fixed at 0.
    interior = grid[1:-1]
    n_in = interior.size
    main = -2.0 * np.ones(n_in) / h**2
    off = np.ones(n_in - 1) / h**2
    d2 = sp.diags([off, main, off], [-1, 0, 1], format="csc")
    d1_off_up = np.ones(n_in - 1) / (2.0 * h)
    d1_off_dn = -np.ones(n_in - 1) / (2.0 * h)
    d1 = sp.diags([d1_off_dn, d1_off_up], [-1, 1], format="csc")
    if potential is None:
        values = interior / np.sqrt(interior**2 + scale**2)
    else:
        values = np.asarray(potential(interior), dtype=float)
        if values.shape != interior.shape:
            raise ValueError("potential must return an array of the interior grid shape")
        if not np.all(np.isfinite(values)):
            raise ValueError("potential must be finite on the grid")
    potential_diag = 1j * xi * values
    if drift_values_mode == "callable":
        convection = sp.diags(drift(interior), 0, format="csc") * d1
    else:
        convection = drift * d1
    operator = (0.5 * volatility**2) * d2 + convection + sp.diags(potential_diag, 0, format="csc")

    u0 = np.ones(n_in, dtype=complex)
    solution = expm_multiply(operator, u0, start=0.0, stop=maturity, num=2)[-1]
    # Linear interpolation at x0 (nearest-node lookup would inject an O(h)
    # jitter that changes sign with grid alignment).
    position = (x0 - interior[0]) / h
    left = int(np.clip(np.floor(position), 0, n_in - 2))
    weight = position - left
    return complex((1.0 - weight) * solution[left] + weight * solution[left + 1])


def clock_density_grid(
    *,
    maturity: float,
    x0: float,
    drift: float,
    volatility: float,
    scale: float,
    n_modes: int = 96,
    n_points: int = 801,
    n_grid: int = 800,
    margin: float = 8.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Return (a_grid, p_grid): the truncated-Fourier density of A_T.

    a_grid covers [-T, T]; p_grid is the n_modes-truncated Fourier series.
    Small negative values from truncation are not clipped; they are a
    convergence diagnostic reported by the caller.
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if n_modes < 8:
        raise ValueError("n_modes must be at least 8")
    if n_points < 101:
        raise ValueError("n_points must be at least 101")

    phis = np.empty(n_modes + 1, dtype=complex)
    phis[0] = 1.0
    for k in range(1, n_modes + 1):
        phis[k] = fk_characteristic(
            k * math.pi / maturity,
            maturity=maturity, x0=x0, drift=drift,
            volatility=volatility, scale=scale,
            n_grid=n_grid, margin=margin,
        )
    a_grid = np.linspace(-maturity, maturity, n_points)
    phases = np.exp(-1j * np.outer(a_grid, np.arange(1, n_modes + 1) * math.pi / maturity))
    p_grid = (1.0 + 2.0 * np.real(phases @ phis[1:])) / (2.0 * maturity)
    return a_grid, p_grid


def fk_touch_price(
    distance: float,
    *,
    maturity: float,
    rate: float,
    beta: float,
    alpha: float,
    a_grid: np.ndarray,
    p_grid: np.ndarray,
) -> float:
    """Price e^{-rT} E[2(1 - Phi(d/sqrt(beta*T + alpha*A_T)))] on a density grid.

    beta = alpha1**2 sigma1**2 + alpha2**2 sigma2**2 and
    alpha = 2 alpha1 alpha2 sigma1 sigma2 are the affine clock coefficients of
    Milestone 3.  Clock values at or below zero are assigned payoff 1 (the
    barrier is already crossed); mathematically the clock is a variance and
    cannot go negative -- the guard is a numerical safety net only.
    """

    if not math.isfinite(distance) or distance <= 0.0:
        raise ValueError("distance must be finite and strictly positive")
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    clocks = beta * maturity + alpha * a_grid
    payoff = np.where(
        clocks > 0.0,
        np.array([
            driftless_touch_probability(distance, v) if v > 0.0 else 1.0
            for v in clocks
        ]),
        1.0,
    )
    return math.exp(-rate * maturity) * float(np.trapezoid(payoff * p_grid, a_grid))


__all__ = [
    "clock_density_grid",
    "fk_characteristic",
    "fk_touch_price",
]
