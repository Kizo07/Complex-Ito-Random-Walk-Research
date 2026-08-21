# Phase 10 — Synthesis: correlation-matrix processes with exact finite-time law

**Date:** 2026-08-21
**Status:** complete — 11/11 unit tests, clean notebook, GH vs MC within
~1–3.5 SE across all payoffs, analytic drifts verified.

---

## 1. The construction and why it matters

The **Phase-Gram process**: take the canonical triangular-angle Gram
parameterization of correlation matrices (Rebonato–Jäckel; Rapisarda–Brigo–
Mercurio) — static calibration machinery in the audited literature — and
drive every angle with an independent Brownian motion.

Three structural payoffs, each verified computationally:

1. **Constraint-free admissibility.** \(R_t=B(\theta_t)B(\theta_t)^\top\) is
   PSD with unit diagonal for every angle configuration; no repulsion
   parameters or boundary care (contrast Jacobi matrix diffusions).
2. **Exact finite-time law.** Angles are jointly Gaussian ⇒ every European
   functional of the whole matrix is a \(d=n(n-1)/2\)-dimensional
   Gauss–Hermite product integral; pairwise marginals are closed form.
   This is the multi-asset completion of the single-pair exactness program
   of Phases 3–8: correlation-matrix derivatives (digitals/calls on entries,
   average-correlation payoffs) become deterministic quadratures.
3. **Endogenous mean reversion.** The induced entry drifts are explicit;
   for the free 3-asset entry,
   \(\mu_{R_{23}}=-\tfrac12(\sigma_\alpha^2+\sigma_\beta^2)R_{23}
   -\tfrac12\sigma_\gamma^2\sin\alpha\sin\beta\cos\gamma\) — curvature
   mean-reverts entries toward zero without any reversion parameter, and
   matches Monte Carlo to third decimals at all tested states.

## 2. Honest limitations

- Product-rule GH scales as \((n_{\text{pts}})^d\): comfortable to \(d=4\!-\!5\)
  (n ≤ 4); larger n needs sparse grids or the MC benchmark route.
- Angle volatilities are free parameters; calibrating them to quoted
  correlation derivatives is the natural next step (the exact law makes
  this a likelihood/least-squares problem on closed-form prices).
- The Gaussian driver has no stationary law; long-horizon behavior is
  diffusive by design (as in Phase 3's base model).

## 3. Novelty boundary (post-audit)

Claimed as new: Gaussian-driven stochastic triangular angles with exact
finite-dimensional matrix law; deterministic European pricing of
correlation-matrix derivatives; closed-form pairwise marginals and entry
drifts; endogenous curvature mean reversion. Not claimed: the angle
parameterization (Rebonato–Jäckel/RBM), PSD-by-construction observation,
GH quadrature, Jacobi/Wishart diffusion theory.

## 4. Deliverables

`PHASE_10_LITERATURE_REVIEW.md`, `phase10_matrix.py`,
`tests/test_phase10_matrix.py` (11/11),
`notebooks/build_phase10_matrix.py` + executed notebook (~8 s, seed
20260821), `PHASE_10_SIMULATION_RESULTS.md`, `phase10_figures/`.
