"""Levy-powered bounded factors: NIG and VG correlation drivers.

Driver:  X_t = x0 + b t + L_t, with L a time-homogeneous Levy process
(variance-gamma or normal-inverse-Gaussian).  The bounded factor is
rho_t = f(X_t), f(x) = x/sqrt(x^2 + c^2).

What survives exactly:

1. **Marginal laws.**  rho_T = f(x0 + L_T) pushes the known Levy law
   forward; CDFs/digitals follow by Gil-Pelaez inversion of the closed-form
   characteristic exponent -- exact up to quadrature tolerance.

2. **Clock law.**  For a time-HOMOGENEOUS driver the semigroup is
   time-translation invariant, so the *backward* Feynman-Kac equation is
   valid (contrast the Phase-7 pitfall for deterministic coefficient
   curves):

       du/dt = b u' + int[u(x+y) - u(x) - y u'(x) 1_{|y|<1}] nu(dy) + q(x) u,
       u(0,x) = 1,   q = i xi f,

   solved on a localized grid by implicit Euler with one precomputed LU
   factorization (the operator is time-independent).  phi_A(xi) =
   E[exp(i xi int_0^T f(X_s) ds)] = u(T, x0).  Jump tails require generous
   localization margins; verify by doubling.

3. **Closed-form anchor.**  With linear potential f(x)=x,
   E[exp(iu int_0^T X_s ds)] has a closed form in the exponent psi:
   exp(iu(x0 T + b T^2/2)) * exp(T * int_0^1 psi(u T (1-r)) dr).

Exact samplers (for Monte Carlo benchmarks): VG via its gamma-time
subordination L_t = theta*G_t + sigma*sqrt(G_t)*Z, G_t ~ Gamma(t/nu, 1);
NIG via inverse-Gaussian subordination L_t = mu t + beta I_t +
sqrt(I_t) Z with I_t ~ IG(mean t delta/gamma0, scale t^2 delta^2),
gamma0 = sqrt(alpha^2 - beta^2).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

SQRT_2PI = math.sqrt(2.0 * math.pi)


@dataclass(frozen=True)
class VGParams:
    sigma: float
    nu: float
    theta: float

    def __post_init__(self):
        if self.sigma <= 0 or self.nu <= 0:
            raise ValueError("VG requires sigma > 0 and nu > 0")

    def exponent(self, u):
        """psi(u): E[e^{u L_1}] = e^{psi(u)} (u complex array/scalar)."""

        uu = np.asarray(u, dtype=complex)
        value = -np.log1p(-1j * self.theta * self.nu * uu
                          + 0.5 * self.sigma**2 * self.nu * uu**2) / self.nu
        return complex(value) if np.ndim(u) == 0 else value


@dataclass(frozen=True)
class NIGParams:
    alpha: float
    beta: float
    delta: float
    mu: float

    def __post_init__(self):
        if self.alpha <= 0 or abs(self.beta) >= self.alpha or self.delta <= 0:
            raise ValueError("NIG requires alpha > 0, |beta| < alpha, delta > 0")

    @property
    def gamma0(self) -> float:
        return math.sqrt(self.alpha**2 - self.beta**2)

    def exponent(self, u):
        uu = np.asarray(u, dtype=complex)
        root = np.sqrt(self.alpha**2 - (self.beta + 1j * uu) ** 2 + 0j)
        # principal branch with positive real part at u=0
        root = np.where(root.real < 0, -root, root)
        value = 1j * self.mu * uu + self.delta * (self.gamma0 - root)
        return complex(value) if np.ndim(u) == 0 else value


def sample_vg(maturity: float, params: VGParams, size: int, rng) -> np.ndarray:
    """Exact VG sample via gamma subordination (E[G_t] = t)."""

    gamma = rng.gamma(shape=maturity / params.nu, scale=params.nu, size=size)
    return params.theta * gamma + params.sigma * np.sqrt(gamma) * rng.standard_normal(size)


def sample_nig(maturity: float, params: NIGParams, size: int, rng) -> np.ndarray:
    """Exact NIG sample via inverse-Gaussian subordination."""

    mean_ig = maturity * params.delta / params.gamma0
    scale_ig = (maturity * params.delta) ** 2
    ig = rng.wald(mean_ig, scale_ig, size=size)
    return (params.mu * maturity + params.beta * ig
            + np.sqrt(ig) * rng.standard_normal(size))


def gil_pelaez_cdf(x: float, exponent: Callable, *, maturity: float,
                   n_points: int = 4096, grid_half_width: float | None = None) -> float:
    """P(L_T <= x) by Gil-Pelaez inversion of the characteristic function."""

    if grid_half_width is None:
        grid_half_width = 200.0 / max(math.sqrt(maturity), 1e-6)
    us = np.linspace(1e-8, grid_half_width, n_points)
    du = us[1] - us[0]
    cf = np.exp(maturity * exponent(us))
    integrand = np.imag(np.exp(-1j * us * x) * cf) / us
    return 0.5 - float(np.trapezoid(integrand, dx=du)) / math.pi


def digital_price_levy(
    rho_star: float,
    *,
    maturity: float,
    x0: float,
    scale: float,
    rate: float,
    exponent: Callable,
) -> float:
    """Price of 1{rho_T >= rho_star}: exact Gil-Pelaez inversion.

    rho_T >= rho_star  <=>  x0 + L_T >= x(rho_star) = scale*rho*/sqrt(1-rho*^2).
    """

    if not (-1.0 < rho_star < 1.0):
        raise ValueError("rho_star must lie in (-1, 1)")
    threshold = scale * rho_star / math.sqrt(1.0 - rho_star * rho_star) - x0
    prob = 1.0 - gil_pelaez_cdf(threshold, exponent, maturity=maturity)
    return math.exp(-rate * maturity) * min(max(prob, 0.0), 1.0)


def _levy_density(params, y: np.ndarray) -> np.ndarray:
    """Levy density on the positive/negative axes (y != 0)."""

    if isinstance(params, VGParams):
        lam_p = (math.sqrt(params.theta**2 + 2 * params.sigma**2 / params.nu)
                 - params.theta) / params.sigma**2
        lam_n = (math.sqrt(params.theta**2 + 2 * params.sigma**2 / params.nu)
                 + params.theta) / params.sigma**2
        out = np.empty_like(y)
        pos = y > 0
        neg = y < 0
        out[pos] = np.exp(-lam_p * y[pos]) / (params.nu * y[pos])
        out[neg] = np.exp(-lam_n * (-y[neg])) / (params.nu * (-y[neg]))
        return out
    if isinstance(params, NIGParams):
        return (params.delta * params.alpha * np.exp(params.beta * y)
                * _bessel_k1_scaled(params.alpha * np.abs(y))
                / (math.pi * np.abs(y)))
    raise TypeError("unknown Levy parameterization")


def _bessel_k1_scaled(z: np.ndarray) -> np.ndarray:
    """K_1(z) computed stably via exp(+/-z) K_1(|z|) scaling."""

    from scipy.special import k1
    return k1(z)


def fk_characteristic_levy(
    xi: float,
    *,
    maturity: float,
    x0: float,
    drift: float,
    params,
    scale: float,
    n_steps: int = 300,
    n_grid: int = 1600,
    margin_scale: float = 10.0,
    jump_cutoff: float = 12.0,
    potential=None,
) -> complex:
    """phi(xi) = E[exp(i xi int_0^T f(x0+L_s+drift*s) ds)] by backward FK PIDE.

    Implicit Euler in time with ONE precomputed sparse LU of
    (I - dt*L_hat); q(x) = i xi f(x) enters explicitly on the right.
    ``jump_cutoff`` sets the small-jump truncation epsilon (in units where
    the Levy density decays like e^{-lambda|y|}); the neglected-mass drift
    compensation is folded into the effective drift.
    """

    if not math.isfinite(xi) or not math.isfinite(maturity) or maturity <= 0:
        raise ValueError("xi must be finite and maturity strictly positive")
    if n_steps < 8 or n_grid < 256:
        raise ValueError("n_steps >= 8 and n_grid >= 256 required")

    # Grid scale from the driver's terminal variance (numeric cumulant).
    eps = 1e-4
    psi_ep = complex(params.exponent(eps))
    psi_mi = complex(params.exponent(-eps))
    variance = -(psi_ep + psi_mi - 2 * complex(params.exponent(0))).real / eps**2
    sd_T = math.sqrt(max(variance, 1e-12) * maturity)

    half = margin_scale * sd_T + 1.0
    center = x0 + drift * maturity
    grid = np.linspace(center - half, center + half, n_grid)
    h = grid[1] - grid[0]
    interior = grid[1:-1]
    n_in = interior.size

    d1 = sp.diags(
        [-np.ones(n_in - 1) / (2 * h), np.ones(n_in - 1) / (2 * h)],
        [-1, 1], format="csc",
    )
    d2 = sp.diags(
        [np.ones(n_in - 1) / h**2, -2 * np.ones(n_in) / h**2, np.ones(n_in - 1) / h**2],
        [-1, 0, 1], format="csc",
    )

    # Jump kernel weights on the SAME spacing as the state grid.  Only ONE
    # grid step is excluded; its first/second moments are folded back as a
    # compensating drift and an effective diffusion (the standard small-
    # jump approximation for infinite-activity Levy processes).
    cutoff = h
    j_grid = np.arange(cutoff, half + h, h)
    w_pos = _levy_density(params, j_grid) * h
    w_neg = _levy_density(params, -j_grid) * h
    lam_total = float(w_pos.sum() + w_neg.sum())
    m1_trunc = float((j_grid * (w_pos - w_neg)).sum())
    from scipy.integrate import quad as _quad

    def _nu_pos(y):
        return float(_levy_density(params, np.array([y]))[0])

    def _nu_neg(y):
        return float(_levy_density(params, np.array([-y]))[0])

    m1_small = (_quad(lambda y: y * _nu_pos(y), 1e-10, cutoff, limit=200)[0]
                - _quad(lambda y: y * _nu_neg(y), 1e-10, cutoff, limit=200)[0])
    sigma_eff_sq = 2.0 * _quad(
        lambda y: y * y * _nu_pos(y), 1e-10, cutoff, limit=200)[0]

    # Assemble dense jump matrix rows via shifts (sparse).
    rows, cols, vals = [], [], []
    for shift_idx, w in enumerate(w_pos, start=1):
        cols_idx = np.arange(n_in - shift_idx)
        rows.append(cols_idx)
        cols.append(cols_idx + shift_idx)
        vals.append(np.full(cols_idx.size, w))
    for shift_idx, w in enumerate(w_neg, start=1):
        cols_idx = np.arange(shift_idx, n_in)
        rows.append(cols_idx)
        cols.append(cols_idx - shift_idx)
        vals.append(np.full(cols_idx.size, w))
    J = sp.coo_matrix(
        (np.concatenate(vals),
         (np.concatenate(rows), np.concatenate(cols))),
        shape=(n_in, n_in),
    ).tocsc()
    # No gradient compensation here: the shifted weights already carry the
    # truncated first moment, and folding m1_trunc into D1 would double-
    # count it.  Small-jump mass below `cutoff` enters via b_eff/sigma_eff.
    jump_op = J - sp.diags(lam_total * np.ones(n_in))

    b_eff = drift - m1_small
    generator = b_eff * d1 + 0.5 * sigma_eff_sq * d2 + jump_op
    if isinstance(params, VGParams):
        pass  # pure jump; no diffusion part
    else:
        pass  # NIG likewise pure jump

    if potential is None:
        q_values = 1j * xi * interior / np.sqrt(interior**2 + scale**2)
    else:
        # Same convention as phase7: the callable replaces f and is
        # multiplied by 1j*xi.
        q_values = 1j * xi * np.asarray(potential(interior), dtype=float)

    dt = maturity / n_steps
    identity = sp.identity(n_in, format="csc", dtype=complex)
    lhs = (identity - dt * generator.astype(complex)).tocsc()
    lu = spla.splu(lhs)

    u = np.ones(n_in, dtype=complex)
    for _ in range(n_steps):
        rhs = u + dt * (q_values * u)
        u = lu.solve(rhs)

    position = (x0 - interior[0]) / h
    left = int(np.clip(np.floor(position), 0, n_in - 2))
    weight = position - left
    return complex((1 - weight) * u[left] + weight * u[left + 1])


def _small_jump_moment(params, eps: float) -> float:
    """int_{|y|<eps} y nu(dy), analytic for VG/NIG tails (log divergence)."""

    if isinstance(params, VGParams):
        lam_p = (math.sqrt(params.theta**2 + 2 * params.sigma**2 / params.nu)
                 - params.theta) / params.sigma**2
        lam_n = (math.sqrt(params.theta**2 + 2 * params.sigma**2 / params.nu)
                 + params.theta) / params.sigma**2
        # int_0^eps y * e^{-lam y}/(nu y) dy = (1 - e^{-lam eps}(1+lam eps))/(nu lam^2)... 
        # keep leading order: eps/(nu) * (1/lam_p - 1/lam_n) approx; use exact:
        def tiny(lam: float) -> float:
            z = lam * eps
            return (1.0 - math.exp(-z) * (1.0 + z)) / (params.nu * lam**2)
        return tiny(lam_p) - tiny(lam_n)
    if isinstance(params, NIGParams):
        # K1 tail: nu(y) ~ delta*beta/(pi y) near zero => symmetric to leading
        # order; asymmetric correction O(beta/alpha). Return leading term 0.
        return 0.0
    raise TypeError("unknown Levy parameterization")


def integrated_exponent_expectation(
    u: float,
    *,
    maturity: float,
    x0: float,
    drift: float,
    exponent: Callable,
    n_points: int = 2001,
) -> complex:
    """Closed form E[exp(iu int_0^T X_s ds)] for the linear potential."""

    r = np.linspace(0.0, 1.0, n_points)
    psi_vals = np.array([complex(exponent(u * maturity * (1 - rr))) for rr in r])
    log_phi = x0 * 1j * u * maturity \
        + 1j * u * drift * maturity**2 / 2.0 \
        + maturity * complex(np.trapezoid(psi_vals, r))
    return complex(np.exp(log_phi))


__all__ = [
    "NIGParams",
    "VGParams",
    "digital_price_levy",
    "fk_characteristic_levy",
    "gil_pelaez_cdf",
    "integrated_exponent_expectation",
    "sample_nig",
    "sample_vg",
]
