# Status

Last updated: 2026-09-03 (Phase 16 complete — toward closed-form American prices)

## Phase 16 (2026-09-03)

- Closed-form occupation resolvent J(tau; a, m, lambda) validated to
  machine precision; multipiece phase-affine (PPA) boundaries give
  quadrature-free American prices (sequential collocation + perpetual
  pinning, m=10 recommended, ~0.07 s).
- Extended grid (revised vs tree oracle): PPA RMSE 0.0146 / MAE 0.0026
  vs BAW 0.279 / 0.162 (90 configs x 5 spots); Phase 15 spiral
  (revised family) RMSE 0.0017.
- Structural findings: non-exponential perpetual approach (r=q
  degeneracy of the linearized memory kernel); Tier B parameter-surface
  attempt documented as open.
- 227/227 tests green; notebooks re-executed 2026-09-03 after the
  review revisions (Phase 15 Revision 2 + Phase 16 aligned).
- Paper: paper/phase16/output/phase16-toward-closed-form-american.pdf.

## Phase 15 (2026-09-03)

- American calls/puts under BSM with dividend yield via Phase 3/4
  complex-GBM phase-barrier geometry.
- `phase15_american.py`: EEP machinery, causal level-set Volterra
  reference solver, collocated logarithmic-spiral pricing formula,
  BAW/CRR/PDE benchmarks.
- Validated: Ju-exhibit TRUE values (<=2.2e-3), McDonald-Schroder
  symmetry (<=2.4e-3), 206/206 tests, executed notebook seed 20260902.
- Spiral formula RMSE 0.016 vs BAW 0.285 vs CRR-Richardson 0.019 on the
  90-configuration grid.
- Paper: paper/phase15/output/phase15-american-options-complex-gbm.pdf.

## Current state

- Phases 1–13 COMPLETE. Flagship manuscript: `PHASE_13_FLAGSHIP_MANUSCRIPT.md`.
- Full test suite: 192/192 green (`python -m unittest discover -s tests`,
  conda env `phase3-paper`).
- All notebooks executed clean from clean kernels, seed 20260821.
- Program plan `PHASE_7_13_PROGRAM_PLAN.md` fully executed.

## Headline results (phases 7–13)

1. Forward-FK primality: backward FK equation fails for deterministic
   coefficient curves (drift-only counterexample); forward Fokker–Planck-
   with-potential is the correct engine (phase7).
2. Scale observational equivalence: only (mu/c, sigma/c) identifiable from
   correlation observations AND derivative prices; closed-form ratio MLE
   (phase9).
3. Exact 1-D characteristic function of spread/basket returns under
   stochastic correlation; deterministic COS pricing; opposite-curvature
   implied-correlation smiles with ATM level = E[A_T] (phase8).
4. Phase-Gram: Gaussian-driven triangular angles give correlation-matrix
   processes with exact finite-time law, PSD by construction (phase10).
5. Levy-powered drivers: marginals + clock survive via FK-PIDE; jump
   asymmetry flips clock drift sign (phase11).
6. Pegged assets: defended bands + bounded-factor de-peg clock; full
   deterministic de-peg derivative stack incl. closed-form pay-at-hit
   Laplace transform (phase12).

## Environment

- conda env `phase3-paper` (Python 3.12.13, numpy 2.5.1, scipy 1.18.0).
- pyarrow installed into phase3-paper on 2026-08-21 for alpha-engine data.
- Empirical data read directly from
  `/home/fire/Documents/alpha_engine/data/prices/*.parquet`.
