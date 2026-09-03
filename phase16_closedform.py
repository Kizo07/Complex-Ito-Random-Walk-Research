"""Phase 16 — Toward closed-form American option prices.

Core result: the early-exercise-premium integral of Phase 15 becomes
CLOSED FORM when the exercise boundary is phase-affine (log-boundary
affine in time to maturity), via the drifted-Brownian occupation
resolvent.  Multipiece phase-affine boundaries then give American prices
as finite sums of closed-form terms — no numerical quadrature.

The key special function:

    J(τ; a, m, λ) = ∫_0^τ e^{-λs} Φ((a + m s)/√s) ds,   λ > 0,

the discounted occupation functional of drifted Brownian motion
X_s = W_s + m s against the half-line {X ≥ -a}.  Closed form:

    J = R(a;λ,m)
        - e^{-λτ} [1/(ν(ν+m)) + 1/(ν(ν-m))] Φ((a+mτ)/√τ)
        + e^{-(m+ν)a} Φ((a-ντ)/√τ) / (ν(ν+m))
        - e^{(ν-m)a} Φ((-a-ντ)/√τ) / (ν(ν-m))

with ν = √(m²+2λ) and the perpetual resolvent

    R(a;λ,m) = 1/λ - e^{-(m+ν)a}/(ν(ν+m))     (a ≥ 0)
    R(a;λ,m) = e^{(ν-m)a}/(ν(ν-m))            (a < 0).

Checks: J(0+)=0, J(∞)=R, J(a→+∞)=(1-e^{-λτ})/λ, J(a→-∞)=0.
"""

from __future__ import annotations

import math

import numpy as np
from scipy import optimize, special

from phase15_american import (
    boundary_at_maturity,
    boundary_equation_residual,
    bs_european,
    perpetual_american,
)


def _phi(x):
    return 0.5 * (1.0 + special.erf(np.asarray(x, dtype=float) / math.sqrt(2.0)))


def _exp_times_phi(c, z):
    """exp(c) * Φ(z), stable for extreme arguments via log_ndtr."""
    z = float(z)
    if z > -30.0:
        return math.exp(c) * float(special.ndtr(z))
    return math.exp(c + float(special.log_ndtr(z)))


def occupation_J(tau, a, m, lam):
    """Closed form of ∫_0^τ e^{-λs} Φ((a + m s)/√s) ds, λ > 0."""
    if tau <= 0.0:
        return 0.0
    if lam <= 0.0:
        raise ValueError("occupation_J requires lam > 0")
    a = float(a)
    nu = math.sqrt(m * m + 2.0 * lam)
    sqrt_t = math.sqrt(tau)
    # use cancellation-free reciprocals:
    # 1/(ν(ν+m)) = (ν-m)/(2λν),  1/(ν(ν-m)) = (ν+m)/(2λν)
    inv_plus = (nu - m) / (2.0 * lam * nu)
    inv_minus = (nu + m) / (2.0 * lam * nu)
    if a >= 0.0:
        R = 1.0 / lam - math.exp(-(m + nu) * a) * inv_plus
    else:
        R = math.exp((nu - m) * a) * inv_minus
    sqrt_lam_t = lam * tau
    term_mid = -math.exp(-sqrt_lam_t) * (inv_plus + inv_minus) * float(
        special.ndtr((a + m * tau) / sqrt_t))
    term3 = _exp_times_phi(-(m + nu) * a, (a - nu * tau) / sqrt_t) * inv_plus
    term4 = -_exp_times_phi((nu - m) * a, (-a - nu * tau) / sqrt_t) * inv_minus
    return R + term_mid + term3 + term4


# ---------------------------------------------------------------------------
# Closed-form EEP for a single phase-affine boundary piece
# ---------------------------------------------------------------------------

def eep_affine_closed(S, tau, A, gamma, K, r, q, sigma, kind):
    """Closed-form EEP for boundary ln b(u) = A - gamma·u (u = time to maturity).

    Call: qS·J(τ; x/σ, m1, q) - rK·J(τ; x/σ, m2, r)
    Put:  rK·[(1-e^{-rτ})/r - J(τ; x/σ, m2, r)]
          - qS·[(1-e^{-qτ})/q - J(τ; x/σ, m1, q)]
    with x = ln S - A + gamma·tau.
    """
    if tau <= 0.0:
        return 0.0
    x = math.log(S) - A + gamma * tau
    a = x / sigma
    m1 = (r - q + 0.5 * sigma * sigma - gamma) / sigma
    m2 = (r - q - 0.5 * sigma * sigma - gamma) / sigma
    if kind == "call":
        t1 = q * S * occupation_J(tau, a, m1, q) if q > 0 else 0.0
        t2 = r * K * occupation_J(tau, a, m2, r)
        return t1 - t2
    t1 = r * K * ((1.0 - math.exp(-r * tau)) / r
                  - occupation_J(tau, a, m2, r))
    if q > 0:
        t2 = q * S * ((1.0 - math.exp(-q * tau)) / q
                      - occupation_J(tau, a, m1, q))
    else:
        t2 = 0.0
    return t1 - t2


# ---------------------------------------------------------------------------
# Multipiece phase-affine boundaries
# ---------------------------------------------------------------------------

def ppa_boundary_pieces(knots_u, knots_v):
    """Return (A_j, gamma_j) pieces for ln b(u) = A_j - gamma_j u on
    (u_{j-1}, u_j], with continuity at the knots."""
    pieces = []
    for j in range(1, len(knots_u)):
        du = knots_u[j] - knots_u[j - 1]
        gamma = (knots_v[j - 1] - knots_v[j]) / du
        A = knots_v[j - 1] + gamma * knots_u[j - 1]
        pieces.append((A, gamma))
    return pieces


def ppa_boundary_func(knots_u, knots_v):
    """Continuous piecewise-affine log-boundary as a function of u."""
    pieces = ppa_boundary_pieces(knots_u, knots_v)

    def b(u):
        if u <= knots_u[0]:
            return math.exp(knots_v[0])
        for j, (A, gamma) in enumerate(pieces, start=1):
            if u <= knots_u[j]:
                return math.exp(A - gamma * u)
        A, gamma = pieces[-1]
        return math.exp(A - gamma * u)

    return b


def eep_ppa_closed(S, tau, knots_u, knots_v, K, r, q, sigma, kind):
    """Closed-form EEP for a multipiece phase-affine boundary.

    Sums the affine-piece closed forms over elapsed-time slices; each
    slice (s_j^-, s_j^+) contributes J(s_j^+) - J(s_j^-).
    """
    if tau <= 0.0:
        return 0.0
    pieces = ppa_boundary_pieces(knots_u, knots_v)
    total = 0.0
    for j, (A, gamma) in enumerate(pieces, start=1):
        u_lo, u_hi = knots_u[j - 1], knots_u[j]
        # elapsed-time slice: u = tau - s in (u_lo, u_hi]
        s_lo = max(0.0, tau - u_hi)
        s_hi = tau - u_lo
        if s_hi <= 0.0:
            break
        s_hi = min(s_hi, tau)
        if s_hi <= s_lo:
            continue
        x = math.log(S) - A + gamma * tau
        a = x / sigma
        m1 = (r - q + 0.5 * sigma * sigma - gamma) / sigma
        m2 = (r - q - 0.5 * sigma * sigma - gamma) / sigma
        if kind == "call":
            j1 = (occupation_J(s_hi, a, m1, q)
                  - occupation_J(s_lo, a, m1, q)) if q > 0 else 0.0
            j2 = (occupation_J(s_hi, a, m2, r)
                  - occupation_J(s_lo, a, m2, r))
            total += q * S * j1 - r * K * j2
        else:
            seg = (s_hi - s_lo)

            def int_phi(m_):
                return (occupation_J(s_hi, a, m_, r)
                        - occupation_J(s_lo, a, m_, r))

            t1 = r * K * ((math.exp(-r * s_lo) - math.exp(-r * s_hi)) / r
                          - int_phi(m2))
            if q > 0:
                t2 = q * S * ((math.exp(-q * s_lo) - math.exp(-q * s_hi)) / q
                              - (occupation_J(s_hi, a, m1, q)
                                 - occupation_J(s_lo, a, m1, q)))
            else:
                t2 = 0.0
            total += t1 - t2
            _ = seg
    return total


def american_ppa_from_knots(S, tau, knots_u, knots_v, K, r, q, sigma, kind):
    """European + closed-form multipiece EEP."""
    if tau <= 0.0:
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    euro = bs_european(S, K, r, q, sigma, tau, kind)
    prem = eep_ppa_closed(S, tau, knots_u, knots_v, K, r, q, sigma, kind)
    price = euro + prem
    intrinsic = max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    return max(price, euro, intrinsic)


# ---------------------------------------------------------------------------
# Sequential collocation for the PPA knot values
# ---------------------------------------------------------------------------

def solve_ppa_boundary(K, r, q, sigma, T, kind, m=6, verbose=False,
                       knots_u_override=None):
    """Sequential value-matching collocation for the PPA knot values.

    Knots u_j in time to maturity (default: mild clustering near 0, or an
    explicit placement via knots_u_override); v_0 = ln b(0+) fixed at the
    maturity anchor; each v_j solves value matching at u_j with the earlier
    pieces held fixed (causality).  Returns (knots_u, knots_v).
    """
    if kind == "call" and q <= 0.0:
        raise ValueError("call with q <= 0 has no finite boundary")
    if knots_u_override is not None:
        knots_u = list(knots_u_override)
        m = len(knots_u) - 1
    else:
        us = np.linspace(0.0, 1.0, m + 1)
        knots_u = list(T * us ** 1.5)
    b0 = boundary_at_maturity(K, r, q, kind)
    knots_v = [math.log(b0)]

    def boundary_so_far(vj):
        vs = knots_v + [vj]
        return ppa_boundary_func(knots_u[:len(vs)], vs)

    for j in range(1, m + 1):
        u_j = knots_u[j]

        def resid(vj):
            bd = boundary_so_far(vj)
            y = bd(u_j)
            return boundary_equation_residual(y, u_j, bd, K, r, q, sigma,
                                              kind, n_quad=40)

        lo = knots_v[j - 1] - 8.0 * sigma * math.sqrt(u_j) - 0.5
        hi = knots_v[j - 1] + 8.0 * sigma * math.sqrt(u_j) + 0.5

        def bracketed():
            return resid(lo) * resid(hi) <= 0

        guard = 0
        while not bracketed() and guard < 24:
            lo = knots_v[j - 1] - (8.0 + 3 * guard) * sigma * math.sqrt(u_j) - 0.5
            hi = knots_v[j - 1] + (8.0 + 3 * guard) * sigma * math.sqrt(u_j) + 0.5
            guard += 1
        if not bracketed():
            knots_v.append(knots_v[-1])
            if verbose:
                print(f"  piece {j}: no bracket, flat step")
            continue
        vj = optimize.brentq(resid, lo, hi, xtol=1e-12, rtol=1e-13)
        knots_v.append(float(vj))
        if verbose:
            print(f"  piece {j}: u={u_j:.4f} b={math.exp(vj):.4f}")
    return knots_u, knots_v


def solve_ppa_pinned(K, r, q, sigma, T, kind, m=10, pin_threshold=1.5):
    """PPA knots with perpetual pinning for long maturities.

    For T >= pin_threshold the last knot is pinned at the perpetual
    boundary ln b_inf (the true boundary approaches b_inf only slowly and
    generally not as a pure exponential, so the pin is the stable
    long-maturity closure); the interior knots are collocated.  The
    threshold sits at 1.5 because boundaries at T <= 1 have not yet
    flattened enough for the pin to beat a free collocation.
    """
    us = list(T * np.linspace(0.0, 1.0, m + 1) ** 1.5)
    if T >= pin_threshold:
        ku, kv = solve_ppa_boundary(K, r, q, sigma, T, kind, m=m - 1,
                                    knots_u_override=us[:-1])
        _, b_inf = perpetual_american(K, K, r, q, sigma, kind)
        return us, kv + [math.log(b_inf)]
    return solve_ppa_boundary(K, r, q, sigma, T, kind, m=m,
                              knots_u_override=us)


def american_ppa_auto(S, K, r, q, sigma, T, kind, m=10):
    """Recommended Phase 16 configuration: pinned PPA, closed-form price.

    Returns (price, knots_u, knots_v).
    """
    if T <= 0.0:
        return (max(S - K, 0.0) if kind == "call" else max(K - S, 0.0),
                None, None)
    if kind == "call" and q <= 0.0:
        return bs_european(S, K, r, q, sigma, T, kind), None, None
    knots_u, knots_v = solve_ppa_pinned(K, r, q, sigma, T, kind, m=m)
    price = american_ppa_from_knots(S, T, knots_u, knots_v, K, r, q, sigma,
                                    kind)
    return price, knots_u, knots_v


def american_ppa(S, K, r, q, sigma, T, kind, m=6, knots=None):
    """Phase 16 PPA pricing formula: European + closed-form multipiece EEP.

    Returns (price, knots_u, knots_v).
    """
    if T <= 0.0:
        return (max(S - K, 0.0) if kind == "call" else max(K - S, 0.0),
                None, None)
    if kind == "call" and q <= 0.0:
        return bs_european(S, K, r, q, sigma, T, kind), None, None
    if knots is None:
        knots_u, knots_v = solve_ppa_boundary(K, r, q, sigma, T, kind, m=m)
    else:
        knots_u, knots_v = knots
    price = american_ppa_from_knots(S, T, knots_u, knots_v, K, r, q, sigma,
                                    kind)
    return price, knots_u, knots_v


# ---------------------------------------------------------------------------
# Adaptive knot placement
# ---------------------------------------------------------------------------

def ppa_residual_profile(knots_u, knots_v, K, r, q, sigma, T, kind,
                         n_scan=60):
    """Value-matching residual of a PPA boundary on a tau scan.

    Uses the closed-form EEP, so the scan is cheap.
    """
    bd = ppa_boundary_func(knots_u, knots_v)
    taus = np.linspace(1e-4, T, n_scan)
    res = np.empty_like(taus)
    for i, tau in enumerate(taus):
        y = bd(float(tau))
        prem = eep_ppa_closed(y, float(tau), knots_u, knots_v, K, r, q,
                              sigma, kind)
        euro = bs_european(y, K, r, q, sigma, float(tau), kind)
        intrinsic = (y - K) if kind == "call" else (K - y)
        res[i] = intrinsic - euro - prem
    return taus, res


def solve_ppa_adaptive(K, r, q, sigma, T, kind, m0=4, n_extra=6):
    """Greedy adaptive PPA: insert knots at worst-residual locations.

    Starts from m0 clustered knots, then repeatedly inserts a knot at the
    argmax of |value-matching residual| (cheap, closed-form EEP) and
    re-solves.  Returns (knots_u, knots_v).
    """
    ku, kv = solve_ppa_boundary(K, r, q, sigma, T, kind, m=m0)
    for _ in range(n_extra):
        taus, res = ppa_residual_profile(ku, kv, K, r, q, sigma, T, kind)
        j = int(np.argmax(np.abs(res)))
        new_u = float(taus[j])
        if min(abs(new_u - u) for u in ku) < 1e-4 * T:
            break
        ku = sorted(ku + [new_u])
        ku, kv = solve_ppa_boundary(K, r, q, sigma, T, kind,
                                    knots_u_override=ku)
    return ku, kv
