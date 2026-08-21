# Phase 10 — Literature review and novelty audit: correlation-matrix processes with exact law

**Date:** 2026-08-21
**Status:** web-verified audit for Phase 10 scope. Snippet/abstract-level
unless marked ✔.

---

## 1. What this phase adds

The **Phase-Gram construction**: drive the canonical triangular angles of
the Gram parameterization of correlation matrices (Rebonato–Jäckel 1999;
Rapisarda–Brigo–Mercurio 2002) with *independent Brownian motions*. Claims:

1. \(R_t=B(\theta_t)B(\theta_t)^\top\) is a valid correlation matrix at all
   times **by construction** (PSD, unit diagonal) — no boundary/no-touch
   conditions, in contrast to Jacobi-type matrix diffusions which require
   repulsion parameters and spectral care.
2. The angle vector is jointly Gaussian with independent coordinates, so
   the finite-time law of the ENTIRE matrix is exact: every European
   functional \(\mathbb E[h(R_T)]\) is a \(d=n(n-1)/2\)-dimensional
   Gauss–Hermite product integral; pairwise marginals are closed form
   (\(\cos\) of a Gaussian).
3. Induced Itô drifts on entries are explicit trigonometric polynomials
   (derived for \(n=3\)); the process mean-reverts endogenously through the
   curvature term \(-\tfrac12(\sigma_\alpha^2+\sigma_\beta^2)R_{23}\).

## 2. Prior art found

- **Rebonato & Jäckel (1999)** ✔: angles parameterization \(B(\theta)\),
  static, for rank reduction of correlation matrices ("the θ's are
  completely free … always symmetric, positive semidefinite and with ones
  in the diagonal").
- **Rapisarda, Brigo & Mercurio (2002), "Parameterizing correlations: a
  geometric interpretation"** ✔ (Imperial College PDF fetched): canonical
  "triangular angles" fixing the initial versor, one-to-one map with
  exactly \(M(M-1)/2\) angles. **Static calibration tool** for the LIBOR
  market model.
- **Brigo–Mercurio, "The basis goes stochastic"**: stochastic basis/angles
  lineage exists, but pricing is by Monte Carlo; no exact-law claim.
- Jacobi/correlation-matrix diffusions: Bru (1991), Ahdida–Alfonsi (2013)
  ✔-level: exact simulation schemes and well-posedness, but finite-time
  entry laws are not closed form and boundary behavior requires parameter
  restrictions.
- Wishart-based correlation models (da Fonseca et al.): affine-ish moments,
  no exact entry densities.
- Searches for "stochastic triangular angles correlation matrix exact
  distribution", "Gaussian driven angles correlation matrix Gauss-Hermite"
  returned no instance of Gaussian-driven triangular angles with exact-law
  pricing.

## 3. Novelty boundary

**Cannot be claimed:** the Gram/angle parameterization itself (Rebonato–
Jäckel; RBM); PSD-by-construction observation (their selling point too);
Gauss–Hermite quadrature; Jacobi diffusion theory.

**Can be claimed:** the Gaussian-driven stochastic triangular-angle process
with its exact finite-dimensional law; closed-form pairwise marginals and
entry drifts; deterministic European pricing of multi-asset correlation
derivatives (digitals/calls on entries, average-correlation payoffs) where
the audited literature uses Monte Carlo; the endogenous mean reversion via
Itô curvature.

## 4. Verification tasks

✔ Rebonato–Jäckel/RBM quotes confirming the static character of the angle
parameterization (Imperial PDF).
✔ Negative searches recorded above; re-run before manuscript submission.
