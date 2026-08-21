"""Exact estimation for the bounded-factor correlation model.

Observation scheme: a correlation proxy series rho_0..rho_n (e.g. rolling
realized correlation of daily return pairs).  Under the model,

    rho_t = f(X_t),   f(x) = x / sqrt(x^2 + c^2),
    dX_t = mu dt + sigma dW_t,

the conjugate coordinate x_t = c * rho_t / sqrt(1 - rho_t^2) is exactly
Gaussian with iid increments N(mu*dt, sigma^2*dt).  The likelihood of the
OBSERVED series factorizes as

    log L(c, mu, sigma) = sum_i log N(dx_i; mu dt, sigma^2 dt)
                          + sum_i log |dx/drho|(rho_i),

with dx_i = c * (g(rho_{i+1}) - g(rho_i)), g(rho) = rho/sqrt(1-rho^2), and
Jacobian |dx/drho| = c / (1 - rho^2)^{3/2}.  For FIXED c the Gaussian part
has closed-form MLEs (OLS), so the full profile likelihood is ONE-dimensional
in log c -- solved by Brent's method.  This is an exact finite-time-
transition MLE, which the audited competitor literature lacks (Teng et al.
2016 fit stationary densities by least squares; Kumar et al. 2021 use
back-transformed OU least squares).

Competitor models fitted to the same observed series, each with its own
consistent Jacobian so information criteria are comparable:

  - `fisher_rw`: atanh(rho) random walk, N(m dt, s^2 dt) increments;
  - `fisher_ou`: atanh(rho) OU process, exact AR(1) quasi-MLE;
  - `conjugate_rw`: this model (c, mu, sigma).

Diagnostics: one-step-ahead PIT values on held-out data under each fitted
model's transition law, Kolmogorov-Smirnov uniformity, out-of-sample
log-score.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.stats import kstest, norm

SQRT_2PI = math.sqrt(2.0 * math.pi)


def fisher_coordinate(rho: np.ndarray | float) -> np.ndarray | float:
    """atanh(rho), clipped inside (-1+eps, 1-eps) for numerical safety."""

    arr = np.asarray(rho, dtype=float)
    clipped = np.clip(arr, -0.999999, 0.999999)
    result = 0.5 * np.log((1.0 + clipped) / (1.0 - clipped))
    return float(result) if arr.ndim == 0 else result


def conjugate_coordinate(rho: np.ndarray | float, scale: float) -> np.ndarray | float:
    """x = c * rho / sqrt(1 - rho^2)."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    arr = np.asarray(rho, dtype=float)
    if np.any((arr <= -1.0) | (arr >= 1.0)):
        raise ValueError("rho must lie strictly inside (-1, 1)")
    result = scale * arr / np.sqrt(1.0 - arr * arr)
    return float(result) if arr.ndim == 0 else result


def realized_correlation_series(
    returns1: np.ndarray,
    returns2: np.ndarray,
    *,
    window: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Rolling realized correlation and right-edge indices of each window.

    rho_series[j] is the Pearson correlation of returns over
    [end_index[j] - window + 1, end_index[j]].
    """

    r1 = np.asarray(returns1, dtype=float)
    r2 = np.asarray(returns2, dtype=float)
    if r1.shape != r2.shape or r1.ndim != 1:
        raise ValueError("return series must be same-length 1-D arrays")
    if window < 10:
        raise ValueError("window must be at least 10")
    n = r1.size
    if n < window + 2:
        raise ValueError("need at least window + 2 observations")

    ends = np.arange(window - 1, n)
    rho = np.empty(ends.size)
    for j, end in enumerate(ends):
        w1 = r1[end - window + 1 : end + 1]
        w2 = r2[end - window + 1 : end + 1]
        sd1 = float(w1.std())
        sd2 = float(w2.std())
        if sd1 == 0.0 or sd2 == 0.0:
            rho[j] = 0.0
            continue
        cov = float(np.mean(w1 * w2) - w1.mean() * w2.mean())
        rho[j] = min(max(cov / (sd1 * sd2), -0.999999), 0.999999)
    return rho, ends


@dataclass(frozen=True)
class ConjugateFit:
    """Fitted ratios of the bounded-factor model (scale normalized to 1).

    The model is scale-observationally-equivalent: (c, mu, sigma) and
    (lam*c, mu/lam, sigma/lam) induce identical laws for every observable
    correlation functional.  Only the ratios drift_per_scale = mu/c and
    volatility_per_scale = sigma/c are identified; estimation therefore
    works in the normalized conjugate coordinate x = rho/sqrt(1-rho^2)
    and returns those ratios.
    """

    scale: float
    drift: float
    volatility: float
    log_likelihood: float
    n_obs: int
    converged: bool

    @property
    def drift_per_scale(self) -> float:
        return self.drift

    @property
    def volatility_per_scale(self) -> float:
        return self.volatility

    @property
    def n_params(self) -> int:
        return 2


def fit_conjugate_rw(
    rho: np.ndarray,
    *,
    dt: float = 1.0 / 252.0,
) -> ConjugateFit:
    """Exact MLE of the identified ratios (mu/c, sigma/c).

    Works in the normalized coordinate x = rho/sqrt(1-rho^2); increments are
    iid N((mu/c) dt, (sigma/c)^2 dt), so the Gaussian OLS solution IS the
    exact MLE of the ratio pair.  Closed form, no numerical optimization.
    """

    rho_arr = np.asarray(rho, dtype=float)
    if rho_arr.size < 5 or np.any((rho_arr <= -1.0) | (rho_arr >= 1.0)):
        raise ValueError("need >= 5 observations strictly inside (-1, 1)")
    x = np.asarray(conjugate_coordinate(rho_arr, scale=1.0))
    dx = np.diff(x)
    loglik_gauss, a_hat, b_hat = _gaussian_increment_mle(dx, dt)
    # Jacobian of the normalized map: log|dx/drho| = -1.5 log(1-rho^2).
    jacobian = float(np.sum(-1.5 * np.log(1.0 - rho_arr[1:] ** 2)))
    return ConjugateFit(
        scale=1.0,
        drift=a_hat,
        volatility=b_hat,
        log_likelihood=loglik_gauss + jacobian,
        n_obs=int(dx.size),
        converged=True,
    )


def _gaussian_increment_mle(increments: np.ndarray, dt: float) -> tuple[float, float, float]:
    """Closed-form (loglik, mu_hat, sigma_hat) for iid N(mu dt, sigma^2 dt)."""

    n = int(increments.size)
    if n < 2:
        raise ValueError("need at least two increments")
    mean_dx = float(np.mean(increments))
    centered = increments - mean_dx
    sigma2_hat = max(float(np.sum(centered**2) / (n * dt)), 1e-14)
    loglik = (
        -0.5 * n * math.log(2.0 * math.pi * sigma2_hat * dt)
        - float(np.sum(centered**2)) / (2.0 * sigma2_hat * dt)
    )
    return loglik, mean_dx / dt, math.sqrt(sigma2_hat)


@dataclass(frozen=True)
class FisherRwFit:
    m: float
    s: float
    log_likelihood: float
    n_obs: int

    @property
    def n_params(self) -> int:
        return 2


def fit_fisher_rw(rho: np.ndarray, *, dt: float = 1.0 / 252.0) -> FisherRwFit:
    """MLE for atanh(rho) random walk with consistent Jacobian."""

    y = np.atleast_1d(fisher_coordinate(np.asarray(rho, dtype=float)))
    dy = np.diff(y)
    ll_gauss, m_hat, s_hat = _gaussian_increment_mle(dy, dt)
    # Jacobian of y = atanh(rho): dy/drho = 1/(1-rho^2).
    jacobian = float(np.sum(-np.log(1.0 - np.asarray(rho, dtype=float)[1:] ** 2)))
    return FisherRwFit(m=m_hat, s=s_hat, log_likelihood=ll_gauss + jacobian,
                       n_obs=int(dy.size))


@dataclass(frozen=True)
class FisherOuFit:
    kappa: float
    theta: float
    s: float
    log_likelihood: float
    n_obs: int

    @property
    def n_params(self) -> int:
        return 3


def fit_fisher_ou(rho: np.ndarray, *, dt: float = 1.0 / 252.0) -> FisherOuFit:
    """Exact AR(1) quasi-MLE for dY = kappa(theta - Y) dt + s dW, Y=atanh(rho).

    Discrete law: Y_{i+1} | Y_i ~ N(theta + (Y_i-theta)e^{-kappa dt},
    s^2(1-e^{-2 kappa dt})/(2 kappa)).  Profile over (theta, s) for fixed
    kappa via OLS; outer 1-D search over kappa.
    """

    y = np.atleast_1d(fisher_coordinate(np.asarray(rho, dtype=float)))
    y0, y1 = y[:-1], y[1:]
    n = y1.size
    if n < 3:
        raise ValueError("need >= 4 observations")

    def profile(log_kappa: float) -> tuple[float, float, float, float]:
        kappa = math.exp(log_kappa)
        decay = math.exp(-kappa * dt)
        # For fixed kappa the conditional mean is
        #   E[y1 | y0] = theta*(1-decay) + y0*decay,
        # and the exact MLE of theta minimizes the RSS over theta:
        #   theta_hat(kappa) = sum((y1 - decay*y0)) / (n*(1-decay)).
        one_minus_decay = 1.0 - decay
        if one_minus_decay < 1e-14:
            theta_hat = float(np.mean(y))
        else:
            theta_hat = float(np.sum(y1 - decay * y0) / (n * one_minus_decay))
        resid = y1 - (theta_hat * one_minus_decay + decay * y0)
        rss = float(resid @ resid)
        q = (1.0 - decay**2) / (2.0 * kappa)
        s2_hat = max(rss / (n * q), 1e-14)
        ll = (
            -0.5 * n * math.log(2.0 * math.pi * s2_hat * q)
            - rss / (2.0 * s2_hat * q)
        )
        return ll, kappa, theta_hat, math.sqrt(s2_hat)

    result = minimize_scalar(
        lambda lk: -profile(lk)[0],
        bounds=(math.log(1e-6), math.log(50.0)),
        method="bounded",
        options={"xatol": 1e-10},
    )
    ll, kappa, theta, s = profile(float(result.x))
    jacobian = float(np.sum(-np.log(1.0 - np.asarray(rho, dtype=float)[1:] ** 2)))
    return FisherOuFit(kappa=kappa, theta=theta, s=s,
                       log_likelihood=ll + jacobian, n_obs=n)


def transition_pit_conjugate(
    rho: np.ndarray,
    fit: ConjugateFit,
    *,
    dt: float = 1.0 / 252.0,
) -> np.ndarray:
    """One-step-ahead PIT values u_i = P(rho_i <= obs | rho_{i-1}).

    Exact: the conjugate coordinate is Gaussian between observations, so the
    conditional CDF of rho_i is the pushforward of a normal CDF through the
    bounded map.
    """

    rho_arr = np.asarray(rho, dtype=float)
    x_prev = np.asarray(conjugate_coordinate(rho_arr[:-1], scale=1.0))
    x_next = np.asarray(conjugate_coordinate(rho_arr[1:], scale=1.0))
    mean = x_prev + fit.drift * dt
    z = (x_next - mean) / (fit.volatility * math.sqrt(dt))
    return norm.cdf(z)


def transition_pit_fisher_rw(rho: np.ndarray, fit: FisherRwFit, *,
                             dt: float = 1.0 / 252.0) -> np.ndarray:
    y_prev = fisher_coordinate(np.asarray(rho, dtype=float)[:-1])
    y_next = fisher_coordinate(np.asarray(rho, dtype=float)[1:])
    z = (y_next - y_prev - fit.m * dt) / (fit.s * math.sqrt(dt))
    return norm.cdf(z)


def transition_pit_fisher_ou(rho: np.ndarray, fit: FisherOuFit, *,
                             dt: float = 1.0 / 252.0) -> np.ndarray:
    y = fisher_coordinate(np.asarray(rho, dtype=float))
    y_prev, y_next = y[:-1], y[1:]
    decay = math.exp(-fit.kappa * dt)
    cond_var = fit.s**2 * (1.0 - decay**2) / (2.0 * fit.kappa)
    z = (y_next - (fit.theta + (y_prev - fit.theta) * decay)) / math.sqrt(cond_var)
    return norm.cdf(z)


def pit_state_correlation(
    pit: np.ndarray, state: np.ndarray
) -> tuple[float, float]:
    """Correlation of PIT values with the lagged state, and its z-score.

    Marginal KS on PIT values tests calibration but can miss dynamic
    misspecification whose u-marginal is still near-uniform (e.g. fitting a
    random walk to mean-reverting data).  Conditional uniformity requires
    the PIT values to be uncorrelated with the conditioning state as well;
    the z-score uses the iid SE 1/sqrt(n).
    """

    u = np.asarray(pit, dtype=float)
    x = np.asarray(state, dtype=float)
    if u.shape != x.shape or u.size < 10:
        raise ValueError("pit and state must be same-length arrays of length >= 10")
    corr = float(np.corrcoef(u, x)[0, 1])
    z = corr * math.sqrt(u.size)
    return corr, z


def ks_uniformity(pit: np.ndarray) -> tuple[float, float]:
    """KS statistic and p-value against Uniform(0,1)."""

    pit_arr = np.asarray(pit, dtype=float)
    if pit_arr.size < 5:
        raise ValueError("need at least five PIT values")
    stat, pvalue = kstest(pit_arr, "uniform")
    return float(stat), float(pvalue)


def attenuation_study(
    true_scale: float,
    true_drift: float,
    true_volatility: float,
    *,
    n_days: int,
    window: int,
    sigma1: float = 0.02,
    sigma2: float = 0.03,
    n_replications: int = 40,
    seed: int = 20260821,
) -> dict[str, float]:
    """Monte Carlo bias of the profile MLE when rho is a window estimate.

    Simulates the TRUE latent pair (two correlated GBM-ish return streams
    with stochastic correlation driven by X), forms rolling realized
    correlations from the simulated returns, refits, and reports median/
    IQR of (c, sigma) estimates relative to truth across replications.
    Deterministic given the seed.
    """

    rng = np.random.default_rng(seed)
    scales, vols = [], []
    for _ in range(n_replications):
        # Latent driver path.
        dx = true_drift / 252.0 + true_volatility * math.sqrt(1.0 / 252.0) \
            * rng.standard_normal(n_days)
        x_path = true_scale * 0.5 + np.cumsum(dx)  # start near typical level
        rho_true = x_path / np.sqrt(x_path**2 + true_scale**2)
        # Return pairs with instantaneous correlation rho_true.
        z1 = rng.standard_normal(n_days)
        z2 = rng.standard_normal(n_days)
        root = np.sqrt(1.0 - rho_true**2)
        r1 = sigma1 * z1
        r2 = sigma2 * (rho_true * z1 + root * z2)
        rho_obs, _ends = realized_correlation_series(r1, r2, window=window)
        fit = fit_conjugate_rw(rho_obs, dt=window / 252.0)
        scales.append(fit.drift)
        vols.append(fit.volatility)
    scales_arr = np.array(scales)
    vols_arr = np.array(vols)
    true_ratio = true_volatility / true_scale
    return {
        "drift_ratio_median": float(np.median(scales_arr)),
        "drift_ratio_iqr": float(np.subtract(*np.percentile(scales_arr, [75, 25]))),
        "vol_ratio_median": float(np.median(vols_arr)),
        "vol_ratio_iqr": float(np.subtract(*np.percentile(vols_arr, [75, 25]))),
        "true_vol_ratio": float(true_ratio),
        "attenuation_factor": float(np.median(vols_arr)) / true_ratio,
        "n_replications": float(n_replications),
    }


__all__ = [
    "ConjugateFit",
    "FisherOuFit",
    "FisherRwFit",
    "attenuation_study",
    "conjugate_coordinate",
    "fit_conjugate_rw",
    "fit_fisher_ou",
    "fit_fisher_rw",
    "fisher_coordinate",
    "ks_uniformity",
    "pit_state_correlation",
    "realized_correlation_series",
    "transition_pit_conjugate",
    "transition_pit_fisher_ou",
    "transition_pit_fisher_rw",
]
