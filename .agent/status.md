# Status

Last updated: 2026-08-21 (Phases 7–13 complete)

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
