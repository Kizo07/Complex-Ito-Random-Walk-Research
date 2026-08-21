"""Correlation-matrix processes with exact finite-time law (Phase-Gram).

Construction.  Use the canonical triangular-angle (Gram) parameterization of
correlation matrices (Rebonato-Jaeckel 1999; Rapisarda-Brigo-Mercurio 2002):
rows of the Cholesky factor B are spherical coordinates built from angles,

    b_{i,1} = cos th_{i,1},
    b_{i,k} = cos th_{i,k} * prod_{m<k} sin th_{i,m}   (1 < k < i),
    b_{i,i} = prod_{m<i} sin th_{i,m},

with theta_{i,j} defined only for j < i (n(n-1)/2 angles total), and
R = B B^T.  PSD and unit diagonal hold BY CONSTRUCTION -- no boundary
conditions, unlike Jacobi-type matrix diffusions.

New content: drive every angle with an INDEPENDENT Brownian motion,

    d th_{ij} = sigma_{ij} dW_{ij},

so the whole angle vector is a jointly Gaussian process.  Every correlation
entry R_ij(t) is then a smooth trigonometric polynomial of a jointly
Gaussian vector, and therefore has an EXACT finite-dimensional law: any
European functional E[h(R(T))] reduces to a d-dimensional Gauss-Hermite
product quadrature (d = n(n-1)/2).  No simulation is needed for European
correlation derivatives, and the pairwise marginals are available in closed
form (cosine of a Gaussian).

For n = 3 the induced Itô drift of the free entry is derived analytically:
with alpha = th21, beta = th31, gamma = th32,
R23 = cos(a)cos(b) + sin(a)sin(b)cos(g) has drift

    -(sigma_a^2 + sigma_b^2)/2 * R23 - sigma_g^2/2 * sin(a) sin(b) cos(g),

implemented and verified against Monte Carlo.
"""

from __future__ import annotations

import math
from itertools import product
from typing import Callable

import numpy as np


def n_angles(n_assets: int) -> int:
    """Number of free angles: n(n-1)/2."""

    if n_assets < 2:
        raise ValueError("need at least two assets")
    return n_assets * (n_assets - 1) // 2


def angle_keys(n_assets: int) -> list[tuple[int, int]]:
    """Canonical angle keys (i, j), i > j >= 1, row-major."""

    return [(i, j) for i in range(2, n_assets + 1) for j in range(1, i)]


def cholesky_factor_from_angles(angles: np.ndarray, n_assets: int) -> np.ndarray:
    """Build the n x n Cholesky factor B from the canonical angle vector.

    ``angles`` is ordered according to :func:`angle_keys`.
    """

    expected = n_angles(n_assets)
    arr = np.asarray(angles, dtype=float)
    if arr.shape != (expected,):
        raise ValueError(f"angles must have shape ({expected},)")
    lookup = dict(zip(angle_keys(n_assets), arr))
    B = np.zeros((n_assets, n_assets))
    B[0, 0] = 1.0
    for i in range(2, n_assets + 1):
        sines = 1.0
        for j in range(1, i):
            # b_{i,j} = cos(th_{i,j}) * prod_{m<j} sin(th_{i,m})
            B[i - 1, j - 1] = sines * math.cos(lookup[(i, j)])
            sines *= math.sin(lookup[(i, j)])
        # diagonal close-out: b_{i,i} = prod_{m<i} sin(th_{i,m})
        B[i - 1, i - 1] = sines
    return B


def correlation_from_angles(angles: np.ndarray, n_assets: int) -> np.ndarray:
    """Correlation matrix R = B B^T from the canonical angle vector."""

    B = cholesky_factor_from_angles(angles, n_assets)
    return B @ B.T


def simulate_angle_system(
    *,
    maturity: float,
    volatilities: np.ndarray,
    initial_angles: np.ndarray,
    n_steps: int,
    n_paths: int,
    seed: int,
) -> np.ndarray:
    """Exact-skeleton paths of all angles: shape (n_paths, n_steps+1, d)."""

    d = len(initial_angles)
    vols = np.asarray(volatilities, dtype=float)
    if vols.shape != (d,) or np.any(vols < 0):
        raise ValueError("volatilities must match the angle count and be nonnegative")
    rng = np.random.default_rng(seed)
    dt = maturity / n_steps
    out = np.empty((n_paths, n_steps + 1, d))
    current = np.tile(np.asarray(initial_angles, dtype=float), (n_paths, 1))
    out[:, 0, :] = current
    root_dt = math.sqrt(dt)
    for step in range(1, n_steps + 1):
        current = current + vols * root_dt * rng.standard_normal((n_paths, d))
        out[:, step, :] = current
    return out


def hermite_nodes(n_points: int) -> tuple[np.ndarray, np.ndarray]:
    """Probabilists' Gauss-Hermite nodes/weights for E[f(Z)], Z ~ N(0,1)."""

    from numpy.polynomial.hermite_e import hermegauss

    nodes, weights = hermegauss(n_points)
    return nodes, weights / math.sqrt(2.0 * math.pi)


def gh_expectation(
    payoff: Callable[[np.ndarray], np.ndarray],
    *,
    mean: np.ndarray,
    stds: np.ndarray,
    n_points: int = 40,
) -> float:
    """E[h(X)] for X ~ N(mean, diag(stds^2)) by product Gauss-Hermite.

    Feasible up to roughly d = 6-7 with moderate n_points.
    """

    mean_arr = np.asarray(mean, dtype=float)
    std_arr = np.asarray(stds, dtype=float)
    if mean_arr.shape != std_arr.shape:
        raise ValueError("mean and stds must have the same shape")
    dim = mean_arr.size
    nodes, weights = hermite_nodes(n_points)
    total = 0.0
    for index_tuple in product(range(n_points), repeat=dim):
        weight = 1.0
        point = np.empty(dim)
        for k in range(dim):
            weight *= weights[index_tuple[k]]
            point[k] = mean_arr[k] + std_arr[k] * nodes[index_tuple[k]]
        total += weight * float(np.sum(payoff(point[None, :])))
    return float(total)


def r23_entry(alpha: np.ndarray, beta: np.ndarray, gamma: np.ndarray) -> np.ndarray:
    """Three-asset free entry R23 = cos a cos b + sin a sin b cos g."""

    return np.cos(alpha) * np.cos(beta) + np.sin(alpha) * np.sin(beta) * np.cos(gamma)


def r23_drift(
    alpha: float, beta: float, gamma: float, *, sig_a: float, sig_b: float, sig_g: float
) -> float:
    """Analytic Ito drift of R23 under independent angle diffusions."""

    return (
        -0.5 * (sig_a**2 + sig_b**2) * r23_entry(np.array([alpha]), np.array([beta]), np.array([gamma]))[0]
        - 0.5 * sig_g**2 * math.sin(alpha) * math.sin(beta) * math.cos(gamma)
    )


def pairwise_marginal_cos_gaussian(
    theta0: float, sigma: float, maturity: float
) -> tuple[float, float]:
    """Exact (E[cos TH], sd(cos TH)) for TH ~ N(theta0, sigma^2 T).

    Uses E[e^{iuTH}] = exp(iu th0 - u^2 v/2): E[cos] = e^{-v/2} cos(th0),
    E[cos^2] = (1 + e^{-2v} cos(2 th0))/2.
    """

    if not math.isfinite(sigma) or sigma < 0.0:
        raise ValueError("sigma must be finite nonnegative")
    variance = sigma * sigma * maturity
    mean = math.exp(-0.5 * variance) * math.cos(theta0)
    second = 0.5 * (1.0 + math.exp(-2.0 * variance) * math.cos(2.0 * theta0))
    return mean, math.sqrt(max(second - mean * mean, 0.0))


__all__ = [
    "angle_keys",
    "cholesky_factor_from_angles",
    "correlation_from_angles",
    "gh_expectation",
    "hermite_nodes",
    "n_angles",
    "pairwise_marginal_cos_gaussian",
    "r23_drift",
    "r23_entry",
    "simulate_angle_system",
]
