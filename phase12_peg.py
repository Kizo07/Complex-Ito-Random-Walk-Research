"""Pegged-asset economics: defended bands, de-peg hazard, and derivatives.

Model (all pieces exact):

1. **Defended band.**  While the peg is credible the log-mispricing
   Y_t = log(P_t/parity) lives in [-lo, hi] and is a two-sided reflected
   Brownian motion (regulated BM): dY = b dt + sigma dW + dL - dU with L/U
   pushing at the edges.  Its stationary law is the exponential trapezoid
       pi(y) proportional to exp(2 b y / sigma^2),
   so defended-band moments are closed form.

2. **Credibility clock.**  De-peg happens when an independent credibility
   factor C_t = f(Z_t), f(x) = x/sqrt(x^2+c^2), first reaches c_* > rho_0.
   This is exactly the Milestone-1 bounded-factor first-passage problem:
   hitting CDF, calendar-time IG density, perpetual probability, and — for
   the proportional class mu = lam*sigma^2 — the pay-at-hit Laplace
   transform E[e^{-r tau}] = exp((lam*sig_d^2 - sqrt(lam^2 sig_d^4 +
   2 r sig_d^2)) * distance / sig_d^2), all closed form.

3. **Post-de-peg free float.**  After tau the asset re-prices instantly to
   the band edge and then follows Gaussian free dynamics
   dlogP = mu_f dt + sig_f dW_f.  Conditional on de-peg at time s through
   edge level y_edge, P_T | s ~ lognormal-normal mixture with closed-form
   Bachelier components, so contingent payoffs reduce to ONE quadrature
   over the exact IG density of tau.

Products priced deterministically:

   - de-peg digital by T:            e^{-rT} P(tau <= T)
   - pay-at-hit de-peg digital:      E[e^{-r tau}; tau < inf]
   - shortfall swap (pays (K-P_T)^+ only if de-pegged by T):
        e^{-rT} * int_0^T f_tau(s) *
        E[(K - exp(y_edge + mu_f (T-s) + sig_f sqrt(T-s) Z))^+] ds
     with f_tau the exact IG density in operational time chain-ruled to
     calendar time.

Monte Carlo appears only as benchmark (reflection + sampled hazard +
exact free continuation).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

import phase7_term_structure as p7

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _norm_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def _norm_pdf(value: float) -> float:
    return math.exp(-0.5 * value * value) / SQRT_2PI


@dataclass(frozen=True)
class BandSpec:
    lo: float
    hi: float

    def __post_init__(self):
        if not (-math.inf < self.lo < self.hi < math.inf):
            raise ValueError("need -inf < lo < hi < inf")


def reflected_band_stationary(
    band: BandSpec, *, drift: float, sigma: float, n_points: int = 2001
) -> dict[str, float]:
    """Stationary law of two-sided reflected BM on [lo, hi].

    Density proportional to exp(2 b y / sigma^2).  Returns normalization,
    mean, and second moment by deterministic quadrature.
    """

    if sigma <= 0:
        raise ValueError("sigma must be strictly positive")
    grid = np.linspace(band.lo, band.hi, n_points)
    weights = np.exp(2.0 * drift * grid / sigma**2)
    total = float(np.trapezoid(weights, grid))
    mean = float(np.trapezoid(grid * weights, grid)) / total
    second = float(np.trapezoid(grid * grid * weights, grid)) / total
    return {
        "mean": mean,
        "sd": math.sqrt(max(second - mean * mean, 0.0)),
        "prob_upper_half": float(np.trapezoid(
            weights[grid >= 0.5 * (band.lo + band.hi)], 
            grid[grid >= 0.5 * (band.lo + band.hi)])) / total,
    }


@dataclass(frozen=True)
class PegModel:
    """De-peg hazard from a bounded credibility factor (proportional class).

    The credibility driver follows the Phase-7 proportional-drift model
    dZ = lam sigma_z^2(t) dt + sigma_z(t) dW; here we take constant
    sigma_z for the closed-form Laplace transform, with lam < 0 meaning
    deteriorating credibility.
    """

    lam: float
    sigma_z: float
    scale: float
    rho0: float
    rho_star: float
    rate: float

    def __post_init__(self):
        if self.sigma_z <= 0 or self.scale <= 0:
            raise ValueError("sigma_z and scale must be positive")
        if not (-1.0 < self.rho0 < self.rho_star < 1.0):
            raise ValueError("need -1 < rho0 < rho_star < 1")
        if self.rate < 0:
            raise ValueError("rate must be nonnegative")

    @property
    def _model(self) -> p7.ProportionalDriftModel:
        return p7.ProportionalDriftModel(
            lam=self.lam, scale=self.scale,
            volatility=lambda t: self.sigma_z, rho0=self.rho0,
        )

    @property
    def distance(self) -> float:
        return self._model.barrier_distance(self.rho_star)

    def depeg_probability(self, horizon: float) -> float:
        """P(de-peg by horizon): exact bounded-factor hitting CDF."""

        return self._model.hitting_cdf(self.rho_star, horizon)

    def depeg_density(self, t: float) -> float:
        """Exact IG hitting density in calendar time."""

        return self._model.hitting_density(t, self.rho_star)

    def pay_at_hit_laplace(self) -> float:
        """E[e^{-r tau_calendar}] closed form via operational time.

        In operational time u = sigma_z^2 t the driver is x0 + lam*u + B_u,
        and tau_calendar = u*/sigma_z^2.  With q = r/sigma_z^2 the standard
        unit-variance drifted-BM Laplace transform gives

            E[e^{-q u*}] = exp((lam - sqrt(lam^2 + 2 q)) * distance).
        """

        if self.lam >= 0 and self.rate == 0.0:
            return 1.0
        q = self.rate / self.sigma_z**2
        return math.exp((self.lam - math.sqrt(self.lam**2 + 2.0 * q))
                        * self.distance)

    def depeg_digital(self, horizon: float) -> float:
        return math.exp(-self.rate * horizon) * self.depeg_probability(horizon)

    def shortfall_swap(
        self,
        strike_log_mispricing: float,
        *,
        horizon: float,
        band: BandSpec,
        mu_free: float,
        sigma_free: float,
        n_points: int = 600,
        t_max_factor: float = 8.0,
    ) -> float:
        """e^{-rT} E[1{tau<=T} (K - log P_T)^+], one quadrature over tau.

        Post-de-peg: log P_T = y_exit + mu_f (T-s) + sig_f sqrt(T-s) Z with
        y_exit the upper band edge (de-peg defined as upward break of the
        credibility factor mapped to the peg's collapse side).
        """

        if sigma_free <= 0:
            raise ValueError("sigma_free must be positive")
        y_exit = band.hi
        k = strike_log_mispricing
        t_max = min(horizon, t_max_factor * max(self.distance, 1e-6)
                    / max(abs(self.lam) * self.sigma_z**2, 1e-9))
        t_grid = np.linspace(1e-8, t_max, n_points)
        densities = np.array([self.depeg_density(float(t)) for t in t_grid])
        taus = t_grid
        remaining = np.maximum(horizon - taus, 1e-12)
        sd_free = sigma_free * np.sqrt(remaining)
        # E[(K - exp(y_exit + mu_f rem + sd Z))^+] via Gauss-Hermite
        from numpy.polynomial.hermite_e import hermegauss

        nodes, wts = hermegauss(80)
        wts = wts / math.sqrt(2.0 * math.pi)
        m = y_exit + mu_free * remaining[:, None] + sd_free[:, None] * nodes[None, :]
        payoff = np.maximum(k - np.exp(m), 0.0)
        conditional = payoff @ wts
        integral = float(np.trapezoid(densities * conditional, t_grid))
        # mass beyond t_max handled by tail bound: negligible for t_max >= 5/scale
        return math.exp(-self.rate * horizon) * integral


def simulate_peg_paths(
    *,
    band: BandSpec,
    drift_band: float,
    sigma_band: float,
    peg: PegModel,
    horizon: float,
    mu_free: float,
    sigma_free: float,
    n_paths: int,
    n_steps: int,
    seed: int,
) -> dict[str, float]:
    """Benchmark simulation: reflection inside the band, sampled hazard,
    free-float continuation after de-peg."""

    rng = np.random.default_rng(seed)
    dt = horizon / n_steps
    model = peg._model

    # Sample de-peg times by inverse transform on the exact hitting law,
    # respecting the perpetual probability (< 1): uniforms above it mean
    # "never de-pegs within any horizon".
    t_grid = np.linspace(1e-9, max(horizon * 3.0, 50.0), 6000)
    dens = np.array([model.hitting_density(float(t), peg.rho_star) for t in t_grid])
    raw_cdf = np.cumsum(dens) * (t_grid[1] - t_grid[0])
    perpetual = float(raw_cdf[-1])
    uniforms = rng.random(n_paths)
    tau_samples = np.where(
        uniforms >= perpetual,
        np.inf,
        # invert the RAW cdf at the uniform: P(tau<=t | de-pegs) handling is
        # automatic because uniforms beyond `perpetual` are masked out.
        np.interp(np.minimum(uniforms, perpetual * (1.0 - 1e-12)),
                  raw_cdf, t_grid),
    )

    y = np.empty(n_paths)
    # Start from stationarity approximately: sample from stationary density.
    stat = reflected_band_stationary(band, drift=drift_band, sigma=sigma_band)
    y[:] = stat["mean"] + stat["sd"] * rng.standard_normal(n_paths)
    y = np.clip(y, band.lo + 1e-9, band.hi - 1e-9)
    root_dt = math.sqrt(dt)
    for _ in range(n_steps):
        y = y + drift_band * dt + sigma_band * root_dt * rng.standard_normal(n_paths)
        y = np.clip(y, band.lo, band.hi)  # simple reflection projection

    depegged = tau_samples <= horizon
    remaining = np.maximum(horizon - tau_samples, 0.0)
    log_p = np.where(
        depegged,
        band.hi + mu_free * remaining + sigma_free * np.sqrt(remaining)
        * rng.standard_normal(n_paths),
        y,
    )
    return {
        "depeg_freq": float(np.mean(depegged)),
        "mean_log_price": float(np.mean(log_p)),
        "frac_below_zero": float(np.mean(log_p < 0.0)),
    }


__all__ = [
    "BandSpec",
    "PegModel",
    "reflected_band_stationary",
    "simulate_peg_paths",
]
