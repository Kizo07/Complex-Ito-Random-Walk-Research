# Phase 7 — Synthesis: time-inhomogeneous exactness and the correlation term structure

**Date:** 2026-08-21
**Status:** complete — 21/21 unit tests, clean notebook, all analytic-vs-MC
checks within tolerance.

---

## 1. What was asked

Extend the exact bounded-factor framework from constant driver coefficients
\((\mu,\sigma)\) to deterministic curves \((\mu(t),\sigma(t))\), and extract
the correlation *term structure* objects that become computable.

## 2. The two theorems

### Theorem 1 (static inheritance)

Let \(dX_t=\mu(t)dt+\sigma(t)dW_t\), \(m(t)=x_0+\int_0^t\mu\),
\(v(t)=\int_0^t\sigma^2\), \(\rho_t=f(X_t)\), \(f(x)=x/\sqrt{x^2+c^2}\).
Every law of \(\rho\) that depends on finitely many marginals or transitions
of \(X\) is a single closed form with \((m(t),v(t))\) in place of
\((x_0+\mu t,\sigma^2t)\):

- transition density: Jacobian × Gaussian pdf in the conjugate coordinate;
- expiry digitals \(e^{-rT}\Phi((m(T)-x(\rho^*))/\sqrt{v(T)})\);
- forward-start digitals (conditional form at \(s\), tower-consistent);
- discrete range accruals (exact per monitoring date);
- **quantile term structure**
  \(q_\alpha(t)=f\!\big(m(t)+\sqrt{v(t)}\,\Phi^{-1}(\alpha)\big)\) — an exact,
  continuous, monotone-in-\(\alpha\) description of the correlation surface
  that no audited competitor provides.

### Theorem 2 (proportional-drift barrier class)

If \(\mu(t)=\lambda\sigma^2(t)\) a.e., then in operational time \(u=v(t)\)
the driver is exactly drifted Brownian motion \(x_0+\lambda u+B_u\) (DDS), so
every reflection-principle law of Milestones 1–2 survives verbatim with
calendar time replaced by integrated variance:

\[
\mathbb P(\tau_{\rho^*}\le T)=
\Phi\!\Big(\frac{\lambda u-b}{\sqrt u}\Big)+e^{2\lambda b}
\Phi\!\Big(-\frac{\lambda u+b}{\sqrt u}\Big),
\qquad u=v(T),\ b=x(\rho^*)-x_0 .
\]

**Parsimony corollary:** barrier laws depend on \(\sigma(\cdot)\) only
through \(u=v(T)\); \((c,\lambda)\) determine all barrier prices and
\(\sigma(\cdot)\) merely warps calendar time. Verified operationally:
rescaling one volatility curve to match another's integrated variance leaves
the exact CDF bit-identical and both MC benchmarks within 1 SE.

**Boundary of the class.** Off proportionality, constant-level hitting
becomes curved-boundary crossing in operational time; per the audited
catalog (Daniels; Durbin; Wang–Pötzelberger; Kahale) no closed forms exist
beyond affine boundaries and isolated special families. Proportionality is
therefore the *only* general deterministic-coefficient class that inherits
the full reflection toolkit (necessity stated within the known catalog).

**Honest cost.** Pay-at-hit discounted laws lose closed form off constant
\(\sigma\): \(E[e^{-r\tau}]\) maps through \(v^{-1}\) and is affine-only in
operational time when \(r>0\).

## 3. The Feynman–Kac pitfall (found, diagnosed, fixed)

The naive extension of the Milestone-4 engine — backward equation
\(\partial_tu=L_tu+i\xi f(x)u\) with \(L_t=\frac12\sigma^2(t)\partial_{xx}+
\mu(t)\partial_x\) — is **wrong** for deterministic coefficient curves.
Counterexample (\(\sigma=0,\mu(t)=t\)): the true solution
\(e^{i\xi(xt+t^3/6)}\) violates the equation by \(i\xi\tfrac{t^2}{2}u\).
The classical derivation silently uses time-translation invariance of the
propagator; deterministic curves destroy it. The failure is invisible to
marginal-moment checks (it preserved \(E[\rho_s]\)-type quantities) and
appeared only when validating the full path-functional law against Monte
Carlo — exactly the verification discipline the project mandates.

**Correct primitive:** the *forward* Feynman–Kac (Fokker–Planck with
potential) equation for the tilted density,

\[
\partial_tp=\tfrac12\sigma^2(t)p_{xx}-\mu(t)p_x+i\xi f(x)p,\qquad
p(0,x)=\delta(x-x_0),\qquad \phi(\xi)=\int p(T,x)\,dx ,
\]

implemented by Crank–Nicolson on a localized domain. Verified against
(i) the Phase-6 solver at constant coefficients, (ii) a closed-form Gaussian
case with variable coefficients (linear potential), (iii) clean second-order
grid convergence, (iv) MC within 4 SE at three frequencies, and (v)
\(E[A_T]\) agreement with exact marginal quadrature to \(2\cdot10^{-5}\).

This also retro-explains why Phase 6 could safely use the backward equation:
with constant coefficients both routes coincide.

## 4. Term-structure bootstrap

Correlation-digital quotes \((T_j,\rho_j^*,\text{price}_j)\) identify
\((c,\lambda^{\mathbb Q})\) by two-parameter least squares under the
proportional class; synthetic recovery is exact to \(10^{-8}\) with a
single-funnel objective landscape. This is the first audited pipeline that
prices *and* inverts correlation term-structure quotes in closed form.

## 5. Novelty boundary (post-audit)

Claimed as new: the static-inheritance statement organized as a theorem with
exact quantile term structure and forward-start digitals for a bounded
correlation; the proportional-drift barrier class with its parsimony
corollary; the bootstrap pipeline; the forward-FK primitive together with
the explicit counterexample against the naive backward extension.
Not claimed: DDS/time-change theory, curved-boundary numerics, Gaussian
marginals of deterministic-coefficient diffusions (all classical).

## 6. Deliverables

`PHASE_7_LITERATURE_REVIEW.md`, `phase7_term_structure.py`,
`tests/test_phase7_term_structure.py` (21/21),
`notebooks/build_phase7_term_structure.py` + executed
`phase7_term_structure.ipynb` (~21 s, seed 20260821),
`PHASE_7_SIMULATION_RESULTS.md`, `phase7_figures/` (5 figures).
