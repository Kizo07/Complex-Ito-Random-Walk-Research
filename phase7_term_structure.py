"""Time-inhomogeneous exactness and the correlation term structure.

Driver with deterministic coefficient curves:

    dX_t = mu(t) dt + sigma(t) dW_t,   X_0 = x0,   c > 0,

mean curve m(t) = x0 + int_0^t mu(s) ds, integrated variance v(t) = int_0^t
sigma(s)**2 ds.  The bounded correlation coordinate is

    rho_t = f(X_t),   f(x) = x / sqrt(x**2 + c**2).

Two exactness layers are implemented:

1. Static inheritance (Theorem 1): every law depending on finitely many
   marginals/transitions of the Gaussian driver is a closed form with m, v.
   Transition densities, expiry digitals, forward-start digitals, discrete
   range accruals, and the quantile term structure q_alpha(t).

2. Proportional-drift barrier class (Theorem 2): if mu(t) = lam * sigma(t)**2,
   then in operational time u = v(t) the driver is exactly drifted Brownian
   motion x0 + lam*u + B_u (Dambis-Dubins-Schwarz), so every reflection-
   principle law of Milestones 1-2 survives with calendar time replaced by
   integrated variance.  Barrier laws depend on sigma(.) only through v(t).

Off this class, constant-level hitting becomes curved-boundary crossing in
operational time; no closed form exists in the known catalog (Durbin 1992;
Pötzelberger-Wang 2001; Kahale 2008).  A deterministic Crank-Nicolson FK
solver is provided for the clock characteristic function under general
deterministic coefficients.

All pricing-path quantities are deterministic (quadrature/PDE); Monte Carlo
appears only in notebooks as an independent benchmark.
"""

from __future__ import annotations

import math
from typing import Callable

import numpy as np
import scipy.sparse as sp
from scipy.integrate import quad
from scipy.optimize import least_squares

SQRT_2PI = math.sqrt(2.0 * math.pi)


def _standard_normal_cdf(value: float) -> float:
    return 0.5 * (1.0 + math.erf(value / math.sqrt(2.0)))


def _standard_normal_ppf(probability: float) -> float:
    if not (0.0 < probability < 1.0):
        raise ValueError("probability must lie in (0, 1)")
    # High-accuracy inverse via scipy is avoided here to keep the module
    # dependency-light; erfinv-based implementation below is exact to 1e-12.
    from scipy.special import ndtri

    return float(ndtri(probability))


def _validate_curve(func: Callable[[float], float], name: str) -> None:
    if not callable(func):
        raise ValueError(f"{name} must be callable in time")
    for probe in (1e-6, 0.5, 1.0):
        value = float(func(probe))
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite on (0, inf)")


def _validate_rho(rho: float) -> None:
    if not math.isfinite(rho) or not (-1.0 < rho < 1.0):
        raise ValueError("rho must lie in (-1, 1)")


def x_from_rho(rho: float, *, scale: float) -> float:
    """Conjugate level x = scale * rho / sqrt(1 - rho**2)."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    _validate_rho(rho)
    return scale * rho / math.sqrt(1.0 - rho * rho)


def rho_from_x(x: float, *, scale: float) -> float:
    """Bounded map rho = x / sqrt(x**2 + scale**2)."""

    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    return x / math.sqrt(x * x + scale * scale)


# ---------------------------------------------------------------------------
# Curves m(t), v(t)
# ---------------------------------------------------------------------------


def mean_curve(
    times: np.ndarray | list[float],
    *,
    x0: float,
    drift: Callable[[float], float],
) -> np.ndarray:
    """m(t_i) = x0 + int_0^{t_i} mu(s) ds by adaptive quadrature."""

    _validate_curve(drift, "drift")
    out = np.empty(len(times))
    for i, t in enumerate(times):
        if not math.isfinite(t) or t < 0.0:
            raise ValueError("times must be finite and nonnegative")
        integral, _ = quad(drift, 0.0, t, epsabs=1e-12, limit=200)
        out[i] = x0 + integral
    return out


def variance_curve(
    times: np.ndarray | list[float],
    *,
    volatility: Callable[[float], float],
) -> np.ndarray:
    """v(t_i) = int_0^{t_i} sigma(s)**2 ds by adaptive quadrature."""

    _validate_curve(volatility, "volatility")

    def integrand(s: float) -> float:
        value = float(volatility(s))
        if value < 0.0 or not math.isfinite(value):
            raise ValueError("volatility must be finite and nonnegative")
        return value * value

    out = np.empty(len(times))
    for i, t in enumerate(times):
        if not math.isfinite(t) or t < 0.0:
            raise ValueError("times must be finite and nonnegative")
        integral, _ = quad(integrand, 0.0, t, epsabs=1e-12, limit=200)
        out[i] = integral
    return out


def interval_coefficients(
    start: float,
    end: float,
    *,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
) -> tuple[float, float]:
    """Return (M_st, V_st) = (int_s^t mu, int_s^t sigma**2), s < t."""

    if not (0.0 <= start < end):
        raise ValueError("need 0 <= start < end")
    mean_total = mean_curve([start, end], x0=0.0, drift=drift)
    var_total = variance_curve([start, end], volatility=volatility)
    return float(mean_total[1] - mean_total[0]), float(var_total[1] - var_total[0])


# ---------------------------------------------------------------------------
# Theorem 1: static inheritance
# ---------------------------------------------------------------------------


def rho_transition_density_inhom(
    rho: float,
    *,
    start: float,
    maturity: float,
    rho_start: float,
    scale: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
) -> float:
    """Exact density of rho_maturity given rho_start observed at `start`.

    p = Jacobian * Normal_pdf(x(rho); x(rho_start) + M_st, V_st).
    """

    _validate_rho(rho)
    _validate_rho(rho_start)
    mean_st, var_st = interval_coefficients(
        start, maturity, drift=drift, volatility=volatility
    )
    if var_st <= 0.0:
        raise ValueError("integrated variance over (start, maturity) must be positive")
    x = x_from_rho(rho, scale=scale)
    x_start = x_from_rho(rho_start, scale=scale)
    z = (x - x_start - mean_st) / math.sqrt(var_st)
    jacobian = scale / (1.0 - rho * rho) ** 1.5
    return jacobian * math.exp(-0.5 * z * z) / (math.sqrt(var_st) * SQRT_2PI)


def digital_price_inhom(
    rho_star: float,
    *,
    maturity: float,
    rho0: float,
    scale: float,
    rate: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
) -> float:
    """Price of 1{rho_T >= rho_star} at T: e^{-rT} Phi((m(T)-x*)/sqrt(v(T)))."""

    _validate_rho(rho_star)
    _validate_rho(rho0)
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    m_t = float(mean_curve([maturity], x0=x_from_rho(rho0, scale=scale), drift=drift)[0])
    v_t = float(variance_curve([maturity], volatility=volatility)[0])
    if v_t <= 0.0:
        raise ValueError("integrated variance must be positive")
    x_star = x_from_rho(rho_star, scale=scale)
    return math.exp(-rate * maturity) * _standard_normal_cdf((m_t - x_star) / math.sqrt(v_t))


def forward_digital_price_conditional(
    rho_star: float,
    *,
    start: float,
    maturity: float,
    rho_start_observed: float,
    scale: float,
    rate: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
) -> float:
    """Value at `start` (rho_start observed) of 1{rho_T >= rho_star} at T.

    Exact: Gaussian transition kernel between start and maturity.
    """

    _validate_rho(rho_star)
    _validate_rho(rho_start_observed)
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
    mean_st, var_st = interval_coefficients(
        start, maturity, drift=drift, volatility=volatility
    )
    if var_st <= 0.0:
        raise ValueError("integrated variance over (start, maturity) must be positive")
    x_star = x_from_rho(rho_star, scale=scale)
    x_s = x_from_rho(rho_start_observed, scale=scale)
    probability = _standard_normal_cdf((x_s + mean_st - x_star) / math.sqrt(var_st))
    return math.exp(-rate * (maturity - start)) * probability


def range_accrual_price_inhom(
    rho_lower: float,
    rho_upper: float,
    *,
    pay_dates: tuple[float, ...] | list[float],
    rho0: float,
    scale: float,
    rate: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
) -> float:
    """Sum_i e^{-r t_i} P(rho_lower <= rho_{t_i} <= rho_upper), exact per date."""

    _validate_rho(rho0)
    if not (-1.0 <= rho_lower < rho_upper <= 1.0):
        raise ValueError("need -1 <= rho_lower < rho_upper <= 1")
    if not math.isfinite(rate) or rate < 0.0:
        raise ValueError("rate must be finite and nonnegative")
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
        m_t = float(mean_curve([date], x0=x0, drift=drift)[0])
        v_t = float(variance_curve([date], volatility=volatility)[0])
        sd = math.sqrt(v_t)
        upper_cdf = _standard_normal_cdf((x_upper - m_t) / sd)
        lower_cdf = _standard_normal_cdf((x_lower - m_t) / sd)
        total += math.exp(-rate * date) * (upper_cdf - lower_cdf)
    return total


def quantile_term_structure(
    alphas: np.ndarray | list[float],
    times: np.ndarray | list[float],
    *,
    rho0: float,
    scale: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
) -> np.ndarray:
    """Exact correlation quantile curves q_alpha(t) = f(m(t) + sqrt(v(t)) z_alpha).

    Returns an array of shape (len(alphas), len(times)).
    """

    _validate_rho(rho0)
    m_t = mean_curve(times, x0=x_from_rho(rho0, scale=scale), drift=drift)
    v_t = variance_curve(times, volatility=volatility)
    alphas_arr = np.asarray(alphas, dtype=float)
    if np.any((alphas_arr <= 0.0) | (alphas_arr >= 1.0)):
        raise ValueError("alphas must lie in (0, 1)")
    z = np.array([_standard_normal_ppf(a) for a in alphas_arr])
    grid = m_t[None, :] + np.sqrt(v_t)[None, :] * z[:, None]
    return grid / np.sqrt(grid * grid + scale * scale)


# ---------------------------------------------------------------------------
# Theorem 2: proportional-drift barrier class mu(t) = lam * sigma(t)**2
# ---------------------------------------------------------------------------


class ProportionalDriftModel:
    """Barrier laws for mu(t) = lam * sigma(t)**2, exact in operational time.

    With u = v(T) the driver is x0 + lam*u + B_u; all laws below are the
    Milestone 1 formulas with calendar time replaced by integrated variance.
    """

    def __init__(
        self,
        *,
        lam: float,
        scale: float,
        volatility: Callable[[float], float],
        rho0: float,
    ) -> None:
        if not math.isfinite(lam):
            raise ValueError("lam must be finite")
        if not math.isfinite(scale) or scale <= 0.0:
            raise ValueError("scale must be finite and strictly positive")
        _validate_curve(volatility, "volatility")
        _validate_rho(rho0)
        self.lam = lam
        self.scale = scale
        self.volatility = volatility
        self.rho0 = rho0
        self.x0 = x_from_rho(rho0, scale=scale)

    def integrated_variance(self, maturity: float) -> float:
        if not math.isfinite(maturity) or maturity <= 0.0:
            raise ValueError("maturity must be finite and strictly positive")
        return float(variance_curve([maturity], volatility=self.volatility)[0])

    def barrier_distance(self, rho_star: float) -> float:
        _validate_rho(rho_star)
        return x_from_rho(rho_star, scale=self.scale) - self.x0

    def hitting_cdf(self, rho_star: float, maturity: float) -> float:
        """P(tau_rho <= T) with u = v(T)."""

        distance = self.barrier_distance(rho_star)
        if distance <= 0.0:
            raise ValueError("need rho_star > rho0 for an upper barrier")
        u = self.integrated_variance(maturity)
        root_u = math.sqrt(u)
        first = _standard_normal_cdf((self.lam * u - distance) / root_u)
        second = (
            math.exp(2.0 * self.lam * distance)
            * _standard_normal_cdf(-(self.lam * u + distance) / root_u)
        )
        return first + second

    def hitting_density(self, t: float, rho_star: float) -> float:
        """Defective IG density of tau in calendar time: f_u(u) * du/dt."""

        distance = self.barrier_distance(rho_star)
        if distance <= 0.0:
            raise ValueError("need rho_star > rho0 for an upper barrier")
        if not math.isfinite(t) or t <= 0.0:
            raise ValueError("t must be finite and strictly positive")
        u = self.integrated_variance(t)
        density_u = (
            distance
            / (math.sqrt(2.0 * math.pi * u**3))
            * math.exp(-((distance - self.lam * u) ** 2) / (2.0 * u))
        )
        sigma_sq = float(self.volatility(t)) ** 2
        return density_u * sigma_sq

    def perpetual_hitting_probability(self, rho_star: float) -> float:
        distance = self.barrier_distance(rho_star)
        if distance <= 0.0:
            raise ValueError("need rho_star > rho0 for an upper barrier")
        if self.lam >= 0.0:
            return 1.0
        return math.exp(2.0 * self.lam * distance)

    def band_exit_probability_upper(
        self, *, rho_lower: float, rho_upper: float
    ) -> float:
        """P(exit band through rho_upper first) via the scale function."""

        _validate_rho(rho_lower)
        _validate_rho(rho_upper)
        x_lower = x_from_rho(rho_lower, scale=self.scale)
        x_upper = x_from_rho(rho_upper, scale=self.scale)
        if not (x_lower < self.x0 < x_upper):
            raise ValueError("need rho_lower < rho0 < rho_upper")
        if self.lam == 0.0:
            return (self.x0 - x_lower) / (x_upper - x_lower)
        rate = -2.0 * self.lam
        s_start = math.exp(rate * self.x0)
        s_lower = math.exp(rate * x_lower)
        s_upper = math.exp(rate * x_upper)
        return (s_start - s_lower) / (s_upper - s_lower)

    def digital_price(self, rho_star: float, *, maturity: float, rate: float) -> float:
        """Expiry digital under the proportional class (static layer)."""

        _validate_rho(rho_star)
        if not math.isfinite(rate) or rate < 0.0:
            raise ValueError("rate must be finite and nonnegative")
        u = self.integrated_variance(maturity)
        x_star = x_from_rho(rho_star, scale=self.scale)
        return math.exp(-rate * maturity) * _standard_normal_cdf(
            (self.x0 + self.lam * u - x_star) / math.sqrt(u)
        )


# ---------------------------------------------------------------------------
# FK clock characteristic function under deterministic coefficient curves
# ---------------------------------------------------------------------------


def fk_characteristic_inhom(
    xi: float,
    *,
    maturity: float,
    x0: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    scale: float,
    n_steps: int = 400,
    n_grid: int = 600,
    margin: float = 8.0,
    potential=None,
) -> complex:
    """phi(xi) = E[exp(i xi int_0^T f(X_s) ds)] via the FORWARD Feynman-Kac PDE.

    For a driver with deterministic coefficient curves the *backward* equation
    du/dt = L_t u + i xi f(x) u is NOT satisfied by
    u(t,x) = E_x[exp(i xi int_0^t f(X_s) ds)] (time-translation invariance
    fails; counterexample: sigma = 0, mu(t) = t, where the true solution
    exp(i xi (x t + t^3/6)) violates the equation).  The correct primitive is
    the forward Feynman-Kac (Fokker-Planck with potential) equation for the
    tilted density p(t, x):

        dp/dt = 0.5 sigma(t)^2 p_xx - mu(t) p_x + i xi f(x) p,
        p(0, x) = delta(x - x0),

    started from a narrow normalized Gaussian bump; then
    phi(xi) = int p(T, x) dx.  Dirichlet boundaries truncate the domain;
    leaked mass equals paths reaching the boundary, O(exp(-margin**2 / 2))
    (verify by doubling the margin).  Crank-Nicolson stepping with
    midpoint-frozen coefficients is second order in space and time.
    Pass ``potential`` (callable on the interior grid) for other occupation
    functionals, e.g. lambda x: x for the closed-form Gaussian check.
    """

    if not math.isfinite(xi):
        raise ValueError("xi must be finite")
    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if n_steps < 8:
        raise ValueError("n_steps must be at least 8")
    if n_grid < 64:
        raise ValueError("n_grid must be at least 64")
    if margin < 4.0:
        raise ValueError("margin must be at least 4 for localization")
    _validate_curve(drift, "drift")
    _validate_curve(volatility, "volatility")
    if not math.isfinite(scale) or scale <= 0.0:
        raise ValueError("scale must be finite and strictly positive")

    center = x0 + float(mean_curve([maturity], x0=0.0, drift=drift)[0])
    half_width = margin * math.sqrt(float(variance_curve([maturity], volatility=volatility)[0])) + 1.0
    grid = np.linspace(center - half_width, center + half_width, n_grid)
    h = grid[1] - grid[0]
    interior = grid[1:-1]
    n_in = interior.size

    d2 = sp.diags(
        [np.ones(n_in - 1) / h**2, -2.0 * np.ones(n_in) / h**2, np.ones(n_in - 1) / h**2],
        [-1, 0, 1], format="csc",
    )
    # Forward drift term: -mu(t) p_x.
    d1_fwd = sp.diags(
        [np.ones(n_in - 1) / (2.0 * h), -np.ones(n_in - 1) / (2.0 * h)],
        [-1, 1], format="csc",
    )
    if potential is None:
        values = interior / np.sqrt(interior**2 + scale**2)
    else:
        values = np.asarray(potential(interior), dtype=float)
        if values.shape != interior.shape:
            raise ValueError("potential must return an array of the interior grid shape")
        if not np.all(np.isfinite(values)):
            raise ValueError("potential must be finite on the grid")
    potential_diag = sp.diags(1j * xi * values, 0, format="csc")

    # Narrow Gaussian bump as a discrete delta, normalized on the grid.
    epsilon = 3.0 * h
    bump = np.exp(-0.5 * ((interior - x0) / epsilon) ** 2)
    bump /= np.trapezoid(bump, interior)

    step = maturity / n_steps
    identity = sp.identity(n_in, format="csc")
    p = bump.astype(complex)
    for k in range(n_steps):
        t_mid = (k + 0.5) * step
        sigma_mid = float(volatility(t_mid))
        mu_mid = float(drift(t_mid))
        operator = (0.5 * sigma_mid**2) * d2 + mu_mid * d1_fwd + potential_diag
        lhs = (identity - 0.5 * step * operator).tocsc()
        rhs = (identity + 0.5 * step * operator).tocsc()
        p = sp.linalg.spsolve(lhs, rhs @ p)

    return complex(np.trapezoid(p, interior))


def forward_fk_tilted_mass(
    q_values: np.ndarray,
    *,
    interior: np.ndarray,
    maturity: float,
    x0: float,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    n_steps: int = 400,
) -> complex:
    """int p(T, x) dx for dp/dt = L_t^* p + q(x) p, p(0) = delta bump at x0.

    General real-or-complex static potential q on the provided interior grid;
    the caller owns domain localization.  This is the shared engine for the
    characteristic function (q = i xi f) and the real-potential resolvent
    used in Phase 8 (q = -lam f).
    """

    if not math.isfinite(maturity) or maturity <= 0.0:
        raise ValueError("maturity must be finite and strictly positive")
    if n_steps < 8:
        raise ValueError("n_steps must be at least 8")
    _validate_curve(drift, "drift")
    _validate_curve(volatility, "volatility")
    q_arr = np.asarray(q_values)
    if q_arr.shape != interior.shape:
        raise ValueError("q_values must match the interior grid shape")
    if not np.all(np.isfinite(q_arr.real)) or not np.all(np.isfinite(q_arr.imag)):
        raise ValueError("q_values must be finite")

    h = float(interior[1] - interior[0])
    n_in = interior.size
    d2 = sp.diags(
        [np.ones(n_in - 1) / h**2, -2.0 * np.ones(n_in) / h**2, np.ones(n_in - 1) / h**2],
        [-1, 0, 1], format="csc",
    )
    d1_fwd = sp.diags(
        [np.ones(n_in - 1) / (2.0 * h), -np.ones(n_in - 1) / (2.0 * h)],
        [-1, 1], format="csc",
    )
    potential_diag = sp.diags(q_arr, 0, format="csc")

    epsilon = 3.0 * h
    bump = np.exp(-0.5 * ((interior - x0) / epsilon) ** 2)
    bump /= np.trapezoid(bump, interior)

    step = maturity / n_steps
    identity = sp.identity(n_in, format="csc")
    p = bump.astype(complex)
    for k in range(n_steps):
        t_mid = (k + 0.5) * step
        sigma_mid = float(volatility(t_mid))
        mu_mid = float(drift(t_mid))
        operator = (0.5 * sigma_mid**2) * d2 + mu_mid * d1_fwd + potential_diag
        lhs = (identity - 0.5 * step * operator).tocsc()
        rhs = (identity + 0.5 * step * operator).tocsc()
        p = sp.linalg.spsolve(lhs, rhs @ p)
    return complex(np.trapezoid(p, interior))


def fk_grid_domain(
    maturity: float,
    x0: float,
    *,
    drift: Callable[[float], float],
    volatility: Callable[[float], float],
    n_grid: int = 600,
    margin: float = 8.0,
) -> tuple[np.ndarray, float]:
    """Return (interior_grid, h) for the localized FK domain."""

    if n_grid < 64:
        raise ValueError("n_grid must be at least 64")
    if margin < 4.0:
        raise ValueError("margin must be at least 4 for localization")
    _validate_curve(drift, "drift")
    _validate_curve(volatility, "volatility")
    center = x0 + float(mean_curve([maturity], x0=0.0, drift=drift)[0])
    half_width = margin * math.sqrt(float(variance_curve([maturity], volatility=volatility)[0])) + 1.0
    grid = np.linspace(center - half_width, center + half_width, n_grid)
    return grid[1:-1], float(grid[1] - grid[0])


# ---------------------------------------------------------------------------
# Term-structure bootstrap of (c, lam) from digital quotes
# ---------------------------------------------------------------------------


def bootstrap_proportional(
    quotes: list[tuple[float, float, float]],
    *,
    rho0: float,
    rate: float,
    volatility: Callable[[float], float],
    initial_guess: tuple[float, float] = (1.0, 0.3),
) -> dict[str, float]:
    """Fit (scale c, lam) to correlation-digital quotes (T_j, rho*_j, price_j).

    Prices are model digital prices under the proportional class; the fit is
    nonlinear least squares over two parameters (deterministic).  Returns the
    fitted parameters plus residual diagnostics.
    """

    if len(quotes) < 2:
        raise ValueError("need at least two quotes to identify (c, lam)")
    _validate_rho(rho0)

    def residuals(params: np.ndarray) -> np.ndarray:
        log_scale, lam = params
        model = ProportionalDriftModel(
            lam=lam, scale=math.exp(log_scale), volatility=volatility, rho0=rho0
        )
        out = []
        for maturity, rho_star, price in quotes:
            model_price = model.digital_price(rho_star, maturity=maturity, rate=rate)
            out.append(model_price - price)
        return np.array(out)

    result = least_squares(
        residuals,
        x0=np.array([math.log(initial_guess[0]), initial_guess[1]]),
        method="lm",
        xtol=1e-14,
        ftol=1e-14,
    )
    cost = float(np.sum(result.fun**2))
    return {
        "scale": math.exp(float(result.x[0])),
        "lam": float(result.x[1]),
        "sum_squared_residuals": cost,
        "max_abs_residual": float(np.max(np.abs(result.fun))),
        "success": bool(result.success),
    }


__all__ = [
    "ProportionalDriftModel",
    "bootstrap_proportional",
    "digital_price_inhom",
    "fk_characteristic_inhom",
    "fk_grid_domain",
    "forward_digital_price_conditional",
    "forward_fk_tilted_mass",
    "interval_coefficients",
    "mean_curve",
    "quantile_term_structure",
    "range_accrual_price_inhom",
    "rho_from_x",
    "rho_transition_density_inhom",
    "variance_curve",
    "x_from_rho",
]
