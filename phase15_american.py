"""Phase 15 — American options under BSM via one-driver complex GBM geometry.

Exact machinery (Black–Scholes–Merton, continuous dividend yield q >= 0):

* European prices (dividend-adjusted Black–Scholes).
* Perpetual American prices (McDonald–Schroder closed form).
* Early-exercise-premium (EEP) representation of Kim (1990) /
  Jacka (1991) / Carr–Jarrow–Myneni (1992), written against a generic
  exercise boundary given as a function of time to maturity.
* Nonlinear Volterra integral equation for the exercise boundary and a
  reference fixed-point/Newton solver.
* Phase-affine boundary family with closed-form perpetual EEP (drifted
  Brownian resolvent) — the building block behind Ju (1998).
* Logarithmic-spiral boundary family anchored exactly at the maturity
  boundary and the perpetual boundary (the Phase 15 ansatz).
* Benchmarks: Barone-Adesi–Whaley (1987) quadratic approximation,
  Ju–Zhong multipiece quadratic approximation, CRR binomial tree with
  Richardson extrapolation, implicit log-space finite differences (PSOR).

All formulas use the convention b(tau) = boundary as a function of time to
maturity tau = T - t, with b(0+) the boundary at maturity.
"""

from __future__ import annotations

import math

import numpy as np
from scipy import integrate, optimize, special

SQRT2 = math.sqrt(2.0)


def _phi(x):
    """Standard normal cdf, scalar or array."""
    return 0.5 * (1.0 + special.erf(np.asarray(x, dtype=float) / SQRT2))


def _phi_pdf(x):
    return np.exp(-0.5 * np.asarray(x, dtype=float) ** 2) / math.sqrt(2.0 * math.pi)


# ---------------------------------------------------------------------------
# European Black–Scholes with dividend yield
# ---------------------------------------------------------------------------

def bs_d12(S, K, r, q, sigma, tau):
    v = sigma * math.sqrt(tau)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * tau) / v
    return d1, d1 - v


def bs_european(S, K, r, q, sigma, tau, kind):
    """European price; kind in {'call','put'}. Exact at tau == 0 as payoff."""
    if tau <= 0.0:
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    d1, d2 = bs_d12(S, K, r, q, sigma, tau)
    if kind == "call":
        return S * math.exp(-q * tau) * _phi(d1) - K * math.exp(-r * tau) * _phi(d2)
    return K * math.exp(-r * tau) * _phi(-d2) - S * math.exp(-q * tau) * _phi(-d1)


# ---------------------------------------------------------------------------
# Perpetual American options (closed form)
# ---------------------------------------------------------------------------

def perpetual_roots(r, q, sigma):
    """Roots s_- < 0 < 1 < s_+ of (sigma^2/2)s(s-1) + (r-q)s - r = 0.

    Requires r > 0. For q = 0 the call root is still finite but the call
    boundary is at infinity (never optimal to exercise); handled by callers.
    """
    a = 0.5 * sigma * sigma
    b = r - q - a
    disc = math.sqrt(b * b + 4.0 * a * r)
    return (-b - disc) / (2.0 * a), (-b + disc) / (2.0 * a)


def perpetual_american(S, K, r, q, sigma, kind):
    """Perpetual American price and boundary (McDonald–Schroder)."""
    s_minus, s_plus = perpetual_roots(r, q, sigma)
    if kind == "call":
        if q <= 0.0:
            return S, math.inf  # never exercise with no dividends
        b_inf = K * s_plus / (s_plus - 1.0)
        if S >= b_inf:
            return S - K, b_inf
        return (b_inf - K) * (S / b_inf) ** s_plus, b_inf
    b_inf = K * s_minus / (s_minus - 1.0)
    if S <= b_inf:
        return K - S, b_inf
    return (K - b_inf) * (S / b_inf) ** s_minus, b_inf


def boundary_at_maturity(K, r, q, kind):
    """Classical boundary limit b(0+) (Kim 1990; Jacka 1991).

    Call: K * max(1, r/q) (infinite when q = 0: never exercise).
    Put:  K * min(1, r/q).

    Derivation near expiry: exercising the call at spot S gains the dividend
    flow qS against the interest rK on the strike, so exercise is optimal iff
    qS >= rK; the put follows by McDonald–Schroder duality.
    """
    if kind == "call":
        if q <= 0.0:
            return math.inf
        return K * max(1.0, r / q)
    if q <= 0.0:
        return K
    return K * min(1.0, r / q)


# ---------------------------------------------------------------------------
# Early-exercise premium representation
# ---------------------------------------------------------------------------

def d12_boundary(S, B, s, r, q, sigma):
    """Black–Scholes d1, d2 with spot S, 'strike' B, horizon s.

    All arguments may be numpy arrays (broadcastable).
    """
    S = np.asarray(S, dtype=float)
    B = np.asarray(B, dtype=float)
    s = np.asarray(s, dtype=float)
    v = sigma * np.sqrt(s)
    d1 = (np.log(S / B) + (r - q + 0.5 * sigma * sigma) * s) / v
    return d1, d1 - v


def eep(S, tau, boundary, K, r, q, sigma, kind, n_quad=64):
    """Early-exercise premium given boundary b(.) as function of time to maturity.

    call:  ∫_0^tau [q S e^{-qs} Φ(d1) - rK e^{-rs} Φ(d2)] ds
    put:   ∫_0^tau [rK e^{-rs} Φ(-d2) - q S e^{-qs} Φ(-d1)] ds
    with d1,d2 evaluated at spot S, boundary b(tau - s), horizon s.
    Gauss–Legendre quadrature (nodes avoid s = 0).
    """
    if tau <= 0.0:
        return 0.0
    xs, ws = np.polynomial.legendre.leggauss(n_quad)
    s_nodes = 0.5 * tau * (xs + 1.0)
    B_nodes = np.array([boundary(tau - s) for s in s_nodes])
    d1, d2 = d12_boundary(S, B_nodes, s_nodes, r, q, sigma)
    if kind == "call":
        vals = (q * S * np.exp(-q * s_nodes) * _phi(d1)
                - r * K * np.exp(-r * s_nodes) * _phi(d2))
    else:
        vals = (r * K * np.exp(-r * s_nodes) * _phi(-d2)
                - q * S * np.exp(-q * s_nodes) * _phi(-d1))
    return 0.5 * tau * float(np.dot(ws, vals))


def american_from_boundary(S, tau, boundary, K, r, q, sigma, kind, n_quad=64):
    """European + EEP, clipped by intrinsic + European floor."""
    if tau <= 0.0:
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    euro = bs_european(S, K, r, q, sigma, tau, kind)
    prem = eep(S, tau, boundary, K, r, q, sigma, kind, n_quad=n_quad)
    price = euro + prem
    intrinsic = max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    return max(price, euro, intrinsic)


# ---------------------------------------------------------------------------
# Volterra integral equation for the boundary (reference solver)
# ---------------------------------------------------------------------------

def boundary_equation_residual(b_tau, tau, boundary, K, r, q, sigma, kind,
                               n_quad=48):
    """Value-matching residual at time to maturity tau with spot b_tau.

    F(tau) = b - K - V_E(b, tau) - EEP(b at spot, boundary, tau).
    """
    euro = bs_european(b_tau, K, r, q, sigma, tau, kind)
    prem = eep(b_tau, tau, boundary, K, r, q, sigma, kind, n_quad=n_quad)
    intrinsic = (b_tau - K) if kind == "call" else (K - b_tau)
    return intrinsic - euro - prem


def boundary_residual_vec(ys, tau, B_nodes, s_nodes, w_factor, K, r, q,
                          sigma, kind):
    """Vectorized residuals for many spots ys at fixed tau.

    B_nodes = boundary at tau - s_nodes; w_factor = 0.5 * tau * GL weights.
    """
    ys = np.asarray(ys, dtype=float)
    v = sigma * np.sqrt(s_nodes)                      # (n,)
    d1 = (np.log(ys[:, None] / B_nodes[None, :])
          + (r - q + 0.5 * sigma * sigma) * s_nodes[None, :]) / v[None, :]
    d2 = d1 - v[None, :]
    if kind == "call":
        euro = (ys * math.exp(-q * tau) * _phi(
            (np.log(ys / K) + (r - q + 0.5 * sigma * sigma) * tau)
            / (sigma * math.sqrt(tau)))
            - K * math.exp(-r * tau) * _phi(
                (np.log(ys / K) + (r - q - 0.5 * sigma * sigma) * tau)
                / (sigma * math.sqrt(tau))))
        vals = (q * ys[:, None] * np.exp(-q * s_nodes)[None, :] * _phi(d1)
                - r * K * np.exp(-r * s_nodes)[None, :] * _phi(d2))
        prem = vals @ w_factor
        return (ys - K) - euro - prem
    euro = (K * math.exp(-r * tau) * _phi(
        -((np.log(ys / K) + (r - q - 0.5 * sigma * sigma) * tau)
          / (sigma * math.sqrt(tau))))
        - ys * math.exp(-q * tau) * _phi(
            -((np.log(ys / K) + (r - q + 0.5 * sigma * sigma) * tau)
              / (sigma * math.sqrt(tau)))))
    vals = (r * K * np.exp(-r * s_nodes)[None, :] * _phi(-d2)
            - q * ys[:, None] * np.exp(-q * s_nodes)[None, :] * _phi(-d1))
    prem = vals @ w_factor
    return (K - ys) - euro - prem


def boundary_history_eval(taus, bvals, i, args):
    """Boundary at `args` (< tau_i) using only solved history [0, i).

    Mirrors the solve-time convention: piecewise-linear interpolation on
    taus[:i] with linear extrapolation from the last two solved points for
    the tail interval (tau_{i-1}, tau_i).
    """
    args = np.asarray(args, dtype=float)
    out = np.interp(args, taus[:i], bvals[:i])
    if i >= 2:
        tail = args > taus[i - 1]
        if np.any(tail):
            sl = ((bvals[i - 1] - bvals[i - 2])
                  / (taus[i - 1] - taus[i - 2]))
            out[tail] = bvals[i - 1] + sl * (args[tail] - taus[i - 1])
    return out


def boundary_residual_grid(i, taus, bvals, K, r, q, sigma, kind, n_quad=48):
    """Value-matching residual at grid point i under solve-time conventions."""
    tau_i = taus[i]
    if tau_i <= 0.0:
        return 0.0
    xs, ws = np.polynomial.legendre.leggauss(n_quad)
    s_nodes = 0.5 * tau_i * (xs + 1.0)
    B_nodes = boundary_history_eval(taus, bvals, i, tau_i - s_nodes)
    w_factor = 0.5 * tau_i * ws
    d1, d2 = d12_boundary(bvals[i], B_nodes, s_nodes, r, q, sigma)
    euro = bs_european(bvals[i], K, r, q, sigma, tau_i, kind)
    if kind == "call":
        prem = float(np.dot(
            w_factor,
            q * bvals[i] * np.exp(-q * s_nodes) * _phi(d1)
            - r * K * np.exp(-r * s_nodes) * _phi(d2)))
        return (bvals[i] - K) - euro - prem
    prem = float(np.dot(
        w_factor,
        r * K * np.exp(-r * s_nodes) * _phi(-d2)
        - q * bvals[i] * np.exp(-q * s_nodes) * _phi(-d1)))
    return (K - bvals[i]) - euro - prem


def solve_boundary(K, r, q, sigma, T, kind, n_grid=200, n_quad=48,
                   delta=1e-6, cluster=1.5, verbose=False):
    """Solve the boundary integral equation sequentially on tau in (0, T].

    The Volterra equation is causal: the equation at tau_i involves the
    boundary only at arguments < tau_i, so points are solved in increasing
    tau order against the already-solved history.

    Residual structure: for the call, F(y) < 0 for y < b(tau) and
    F(y) = 0 for all y >= b(tau) (deep ITM calls exercise immediately, so
    the EEP representation reproduces intrinsic value identically above the
    boundary).  The boundary is therefore the point where F *reaches* zero
    from below, not a sign change.  We solve F(y) = -delta*K (a genuine
    crossing) and correct linearly with the local derivative; delta -> 0
    recovers the boundary (the price itself is stationary to first order in
    boundary errors, so residual error is doubly benign).

    Returns (taus, b_values) including tau = 0 with the maturity boundary.
    """
    if kind == "call" and q <= 0.0:
        raise ValueError("call with q <= 0 has no finite boundary")
    # mild clustering near tau = 0 where the boundary moves fastest; the
    # exponent must stay gentle: the integral equation loses traction as
    # tau -> 0 and over-clustered points land inside the noise floor
    us = np.linspace(0.0, 1.0, n_grid)
    taus = T * us ** cluster
    b0 = boundary_at_maturity(K, r, q, kind)
    grid_b = np.empty(n_grid)
    grid_b[0] = b0

    xs_gl, ws_gl = np.polynomial.legendre.leggauss(n_quad)
    _, b_inf = perpetual_american(K, K, r, q, sigma, kind)
    n_scan = 600

    def resid_at(y, tau_i, s_nodes, B_nodes, w_factor):
        d1, d2 = d12_boundary(y, B_nodes, s_nodes, r, q, sigma)
        if kind == "call":
            euro = bs_european(y, K, r, q, sigma, tau_i, "call")
            prem = float(np.dot(
                w_factor,
                q * y * np.exp(-q * s_nodes) * _phi(d1)
                - r * K * np.exp(-r * s_nodes) * _phi(d2)))
            return (y - K) - euro - prem
        euro = bs_european(y, K, r, q, sigma, tau_i, "put")
        prem = float(np.dot(
            w_factor,
            r * K * np.exp(-r * s_nodes) * _phi(-d2)
            - q * y * np.exp(-q * s_nodes) * _phi(-d1)))
        return (K - y) - euro - prem

    for i in range(1, n_grid):
        tau_i = taus[i]
        s_nodes = 0.5 * tau_i * (xs_gl + 1.0)
        args = tau_i - s_nodes
        # interpolate on solved history only; linearly extrapolate the tiny
        # tail (tau_{i-1}, tau_i) from the last two solved points
        B_nodes = np.interp(args, taus[:i], grid_b[:i])
        if i >= 2:
            tail = args > taus[i - 1]
            if np.any(tail):
                sl = ((grid_b[i - 1] - grid_b[i - 2])
                      / (taus[i - 1] - taus[i - 2]))
                B_nodes[tail] = grid_b[i - 1] + sl * (args[tail]
                                                      - taus[i - 1])
        w_factor = 0.5 * tau_i * ws_gl

        def H(y):
            return resid_at(y, tau_i, s_nodes, B_nodes, w_factor) + delta * K

        prev = grid_b[i - 1]
        # adaptive scan window around the previous boundary, wide enough
        # for the local diffusion scale sigma*sqrt(tau_i), oriented along
        # the monotone direction toward the perpetual limit
        w = 8.0 * sigma * math.sqrt(tau_i) + 0.05
        down = (kind == "put") or (b_inf < b0)
        if down:
            scan = prev * np.exp(np.linspace(-w, 0.0, n_scan))
        else:
            scan = prev * np.exp(np.linspace(0.0, w, n_scan))
        F_scan = boundary_residual_vec(scan, tau_i, B_nodes, s_nodes,
                                       w_factor, K, r, q, sigma, kind)
        # require the put residual to have risen into its positive hump
        # first (the degenerate endpoint F(0+) = 0 is noise-contaminated)
        if kind == "put":
            feas = np.arange(len(scan)) > int(np.argmax(F_scan))
            idx_feas = np.where(feas)[0]
            if len(idx_feas) == 0:
                grid_b[i] = prev
                continue
            F_sub = F_scan[idx_feas]
            scan_sub = scan[idx_feas]
        else:
            F_sub = F_scan
            scan_sub = scan
        if kind == "call":
            cross = np.where(F_sub > -delta * K)[0]
        else:
            cross = np.where(F_sub < -delta * K)[0]
        if len(cross) == 0:
            grid_b[i] = prev
            continue
        j = int(cross[0])
        if j == 0:
            # already on the level set at the previous point: flat step
            grid_b[i] = prev
            continue
        lo = scan_sub[j - 1]
        hi = scan_sub[j]
        if H(lo) * H(hi) > 0.0:
            grid_b[i] = prev
            continue
        y_delta = optimize.brentq(H, lo, hi, xtol=1e-14, rtol=8.9e-16)
        # linear correction from level -delta*K back to zero
        hh = max(1e-6 * K, 1e-4 * y_delta)
        slope = (resid_at(y_delta + hh, tau_i, s_nodes, B_nodes, w_factor)
                 - resid_at(y_delta - hh, tau_i, s_nodes, B_nodes, w_factor))
        if abs(slope) > 1e-12:
            y_corr = y_delta + (delta * K) * (2.0 * hh) / slope
        else:
            y_corr = y_delta
        # defensive sanity: the boundary is monotone toward the perpetual
        # limit; clip noise-driven violations
        prev = grid_b[i - 1]
        if kind == "call":
            if b_inf >= b0:
                y_corr = min(max(y_corr, prev), b_inf * 1.001)
            else:
                y_corr = max(min(y_corr, prev), b_inf * 0.999)
        else:
            y_corr = min(max(y_corr, max(b_inf * 0.99, 1e-6)), prev)
        grid_b[i] = y_corr
        if verbose and (i % max(1, n_grid // 10) == 0 or i == n_grid - 1):
            print(f"  tau={tau_i:.5f} b={y_corr:.6f} "
                  f"(level root {y_delta:.6f})")
    return taus, grid_b


# ---------------------------------------------------------------------------
# Phase-affine boundaries and the closed-form perpetual EEP
# ---------------------------------------------------------------------------

def phase_affine_boundary(b1, gamma):
    """b(tau) = b1 * exp(-gamma * tau): log-boundary affine in time to maturity."""
    return lambda tau: b1 * math.exp(-gamma * tau)


def resolvent_half_line(x, lam, drift):
    """∫_0^∞ e^{-λs} P(W_s + drift·s ≥ -x) ds  (closed form).

    Resolvent of drifted Brownian motion applied to 1_{[-x,∞)} at 0.
    """
    nu = math.sqrt(drift * drift + 2.0 * lam)
    if x >= 0.0:
        return 1.0 / lam - (nu - drift) / (2.0 * lam * nu) * math.exp(-(drift + nu) * x)
    return 1.0 / lam - resolvent_half_line(-x, lam, -drift)


def eep_phase_affine_perpetual(S, b1, gamma, K, r, q, sigma, kind):
    """Closed-form EEP over infinite horizon for log-boundary ln b1 - gamma τ.

    Derived in the Phase 15 notes via the drifted-Brownian resolvent.
    Call term 1: q S ∫ e^{-q s} Φ(d1) ds with d1 = [a + m1 s]/(σ√s)
    """
    a1 = math.log(S / b1)
    if kind == "call":
        m1 = (r - q + 0.5 * sigma * sigma - gamma) / sigma
        m2 = (r - q - 0.5 * sigma * sigma - gamma) / sigma
        x1 = a1 / sigma
        x2 = a1 / sigma
        t1 = q * S * resolvent_half_line(x1, q, m1) if q > 0 else 0.0
        t2 = r * K * resolvent_half_line(x2, r, m2)
        return t1 - t2
    m1 = (r - q + 0.5 * sigma * sigma - gamma) / sigma
    m2 = (r - q - 0.5 * sigma * sigma - gamma) / sigma
    x = a1 / sigma
    # Φ(-d) = P(W + m s <= ...) complement
    t1 = r * K * (1.0 / r - resolvent_half_line(x, r, m2))
    t2 = q * S * (1.0 / q - resolvent_half_line(x, q, m1)) if q > 0 else 0.0
    return t1 - t2


# ---------------------------------------------------------------------------
# Logarithmic-spiral boundary family (Phase 15 ansatz)
# ---------------------------------------------------------------------------

def spiral_boundary(tau, b0, b_inf, kappa):
    """ln b(τ) = ln b_∞ + (ln b_0 - ln b_∞) e^{-κ τ}; exact at both anchors."""
    if not math.isfinite(b0) or not math.isfinite(b_inf):
        raise ValueError("spiral needs finite anchors")
    return b_inf * math.exp((math.log(b0 / b_inf)) * math.exp(-kappa * tau))


def make_spiral(K, r, q, sigma, kind, kappa):
    """Return the anchored spiral boundary for the parameter set."""
    b0 = boundary_at_maturity(K, r, q, kind)
    _, b_inf = perpetual_american(K, K, r, q, sigma, kind)
    return lambda tau: spiral_boundary(tau, b0, b_inf, kappa)


# ---------------------------------------------------------------------------
# Refined spiral family: universal short-maturity asymptotics included
# ---------------------------------------------------------------------------

ASYM_EPS = 1e-14


def spiral_refined_boundary(tau, b0, b_inf, sigma, eta, k1, k2):
    """Refined spiral boundary, exact at both asymptotic limits.

    ln b(τ) = ln b_∞ + ln(b_0/b_∞) e^{-k1 τ}
              + η σ √(2τ |ln max(τ,ε)|) e^{-k2 τ}

    The square-root term is the short-maturity law: the shape
    √(τ|ln τ|) (infinite slope at maturity) is universal; its effective
    coefficient depends on r−q at accessible maturities and is absorbed
    by η (η = +1 for calls, −1 for puts; the magnitude is fixed by
    collocation).  The exponential cutoff restores the perpetual limit.
    k1, k2 are fixed by collocation (see spiral_collocation).
    """
    tau = float(tau)
    if tau <= 0.0:
        return b0
    t_safe = max(tau, ASYM_EPS)
    ln_b = (math.log(b_inf) + math.log(b0 / b_inf) * math.exp(-k1 * tau)
            + eta * sigma * math.sqrt(2.0 * tau * abs(math.log(t_safe)))
            * math.exp(-k2 * tau))
    return math.exp(ln_b)


def spiral_collocation(K, r, q, sigma, T, kind, n_quad=48,
                       nodes=(0.25, 0.5, 0.75)):
    """Fix (k1, k2, eta) of the refined spiral without any boundary fitting.

    Collocation: the value-matching residual of the boundary integral
    equation is driven to zero (bounded least squares, multi-start) at
    fractional times to maturity.  eta rescales the universal
    short-maturity asymptotic term (eta = 1 is the leading law).

    Returns (k1, k2, eta, info).
    """
    b0 = boundary_at_maturity(K, r, q, kind)
    _, b_inf = perpetual_american(K, K, r, q, sigma, kind)
    eta0 = 1.0 if kind == "call" else -1.0

    def bd(tau, k1, k2, eta):
        return spiral_refined_boundary(tau, b0, b_inf, sigma, eta0 * eta,
                                       k1, k2)

    def residuals(params):
        k1, k2, eta = params
        out = []
        for f in nodes:
            tc = f * T
            y = bd(tc, k1, k2, eta)
            bdl = lambda tau, k1=k1, k2=k2, eta=eta: bd(tau, k1, k2, eta)
            out.append(boundary_equation_residual(y, tc, bdl, K, r, q,
                                                  sigma, kind, n_quad))
        return np.array(out)

    def obj(params):
        v = residuals(params)
        return float(v @ v)

    best = None
    for x0 in [(0.8, 1.1, 1.0), (0.5, 2.0, 0.6), (1.2, 0.8, 1.3),
               (0.3, 1.5, 1.8)]:
        res = optimize.minimize(obj, x0=x0,
                                bounds=[(1e-3, 60.0), (1e-3, 60.0),
                                        (0.0, 2.5)],
                                method="L-BFGS-B")
        if best is None or res.fun < best[1]:
            best = (res.x, res.fun)
    k1, k2, eta = best[0]
    return float(k1), float(k2), float(eta), {"objective": best[1]}


def american_spiral(S, K, r, q, sigma, T, kind, n_quad=64, params=None):
    """Phase 15 spiral pricing formula.

    American price = European + early-exercise premium evaluated on the
    collocated refined-spiral boundary.  Returns (price, k1, k2, eta).
    """
    if T <= 0.0:
        return (max(S - K, 0.0) if kind == "call" else max(K - S, 0.0),
                None, None, None)
    if kind == "call" and q <= 0.0:
        return bs_european(S, K, r, q, sigma, T, kind), None, None, None
    if params is None:
        k1, k2, eta, _ = spiral_collocation(K, r, q, sigma, T, kind)
    else:
        k1, k2, eta = params
    b0 = boundary_at_maturity(K, r, q, kind)
    _, b_inf = perpetual_american(K, K, r, q, sigma, kind)
    eta0 = 1.0 if kind == "call" else -1.0
    bd = lambda tau: spiral_refined_boundary(tau, b0, b_inf, sigma,
                                             eta0 * eta, k1, k2)
    price = american_from_boundary(S, T, bd, K, r, q, sigma, kind,
                                   n_quad=n_quad)
    return price, k1, k2, eta


# ---------------------------------------------------------------------------
# Barone-Adesi & Whaley (1987) quadratic approximation (with dividends)
# ---------------------------------------------------------------------------

def baw(S, K, r, q, sigma, tau, kind):
    """Barone-Adesi–Whaley quadratic approximation."""
    if tau <= 0.0:
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    if kind == "call" and q <= 0.0:
        return bs_european(S, K, r, q, sigma, tau, kind)
    m = 2.0 * r / (sigma * sigma)
    n = 2.0 * (r - q) / (sigma * sigma)
    h = 1.0 - math.exp(-r * tau)
    phi = 1.0 if kind == "call" else -1.0
    lam = (-(n - 1.0) + phi * math.sqrt((n - 1.0) ** 2 + 4.0 * m / h)) / 2.0

    def critical(Sstar):
        d1, d2 = bs_d12(Sstar, K, r, q, sigma, tau)
        euro = bs_european(Sstar, K, r, q, sigma, tau, kind)
        lhs = phi * (Sstar - K)
        rhs = euro + (1.0 - math.exp(-q * tau)) * 0.0  # keep explicit
        # smooth fit: phi = phi e^{-qτ} Φ(φ d1) + λ(φ(S*-K) - V_E)/S*
        return (phi * math.exp(-q * tau) * _phi(phi * d1)
                + lam * (phi * (Sstar - K) - euro) / Sstar - phi)

    # bracket for S*
    if kind == "call":
        lo = K
        hi = K * 100.0
    else:
        lo = K * 1e-6
        hi = K
    try:
        flo = critical(lo + 1e-12 * K)
        fhi = critical(hi)
        if flo * fhi > 0:
            # fall back: wide scan
            grid = np.geomspace(max(lo, K * 1e-6), hi, 400)
            vals = [critical(x) for x in grid]
            idx = next((i for i in range(len(grid) - 1)
                        if vals[i] * vals[i + 1] < 0), None)
            if idx is None:
                return bs_european(S, K, r, q, sigma, tau, kind)
            Sstar = optimize.brentq(critical, grid[idx], grid[idx + 1],
                                    xtol=1e-12, rtol=1e-13)
        else:
            Sstar = optimize.brentq(critical, lo + 1e-12 * K, hi,
                                    xtol=1e-12, rtol=1e-13)
    except ValueError:
        return bs_european(S, K, r, q, sigma, tau, kind)
    if phi * (Sstar - S) <= 0.0:
        return phi * (S - K)
    euro = bs_european(S, K, r, q, sigma, tau, kind)
    A = phi * (Sstar - K) - bs_european(Sstar, K, r, q, sigma, tau, kind)
    prem = A * (S / Sstar) ** lam
    return euro + prem


# ---------------------------------------------------------------------------
# CRR binomial tree with Richardson extrapolation
# ---------------------------------------------------------------------------

def crr_american(S, K, r, q, sigma, tau, kind, N):
    """Cox–Ross–Rubinstein American price with N steps."""
    dt = tau / N
    u = math.exp(sigma * math.sqrt(dt))
    d = 1.0 / u
    p = (math.exp((r - q) * dt) - d) / (u - d)
    disc = math.exp(-r * dt)
    idx = np.arange(N + 1)
    ST = S * u ** (N - idx) * d ** idx
    if kind == "call":
        V = np.maximum(ST - K, 0.0)
    else:
        V = np.maximum(K - ST, 0.0)
    pay = np.maximum if kind == "call" else np.maximum
    for _ in range(N):
        V_hold = disc * (p * V[:-1] + (1.0 - p) * V[1:])
        ST = ST[:-1] / u
        intrinsic = (ST - K) if kind == "call" else (K - ST)
        V = np.maximum(V_hold, intrinsic)
    return float(V[0])


def crr_richardson(S, K, r, q, sigma, tau, kind, Ns=(1000, 2000, 4000)):
    """Second-order Richardson extrapolation in 1/N on CRR prices."""
    prices = [crr_american(S, K, r, q, sigma, tau, kind, N) for N in Ns]
    hs = [1.0 / N for N in Ns]
    # fit price = a + b h + c h^2, report a
    A = np.vstack([np.ones(3), hs, np.array(hs) ** 2]).T
    coef = np.linalg.solve(A, prices)
    return float(coef[0])


# ---------------------------------------------------------------------------
# Implicit finite differences on log-price (PSOR)
# ---------------------------------------------------------------------------

def pde_american(S, K, r, q, sigma, tau, kind, n_space=1200, n_time=2400,
                 span_std=6.0):
    """Implicit log-space FD with projected SOR for the exercise constraint."""
    if tau <= 0.0:
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    x0 = math.log(S)
    width = span_std * sigma * math.sqrt(tau) + 2.0 * abs(r - q) * tau + 3.0
    x_min = math.log(K) - width
    x_max = math.log(K) + width
    M = n_space
    dx = (x_max - x_min) / (M - 1)
    x = np.linspace(x_min, x_max, M)
    dt = tau / n_time

    Ei = np.exp(x)
    intrinsic = np.maximum(Ei - K, 0.0) if kind == "call" else np.maximum(K - Ei, 0.0)

    nu = r - q - 0.5 * sigma * sigma
    a = 0.5 * sigma * sigma / (dx * dx)
    bcoef = nu / (2.0 * dx)
    # (-L + r) u_j = diag*u_j + lower*u_{j-1} + upper*u_{j+1}
    lower = -(a - bcoef)
    upper = -(a + bcoef)
    diag = 2.0 * a + r

    V = intrinsic.copy()

    def bc_values():
        if kind == "call":
            return 0.0, Ei[-1] - K
        return K - Ei[0], 0.0

    n = M - 2
    diag_t = diag + 1.0 / dt
    omega = 1.55
    for _ in range(n_time):
        lo_bc, hi_bc = bc_values()
        rhs = V[1:-1] / dt
        rhs[0] -= lower * lo_bc
        rhs[-1] -= upper * hi_bc
        Vn = V[1:-1].copy()
        for _s in range(80):
            change = 0.0
            for j in range(n):
                lv = Vn[j - 1] if j > 0 else lo_bc
                uv = Vn[j + 1] if j < n - 1 else hi_bc
                gs = (rhs[j] - lower * lv - upper * uv) / diag_t
                upd = Vn[j] + omega * (gs - Vn[j])
                proj = max(upd, intrinsic[j + 1])
                change = max(change, abs(proj - Vn[j]))
                Vn[j] = proj
            if change < 1e-11:
                break
        Vnew = np.empty(M)
        Vnew[0] = lo_bc
        Vnew[-1] = hi_bc
        Vnew[1:-1] = Vn
        V = Vnew
    return float(np.interp(x0, x, V))
