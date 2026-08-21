# Session handoff — 2026-08-21 — Complex-Ito-Random-Walk-Research phases 7–13

## What was done

Executed the approved PHASE_7_13_PROGRAM_PLAN end-to-end:

- Phase 7 time-inhomogeneous exactness: static-inheritance theorem,
  proportional-drift barrier class (parsimony corollary verified), exact
  quantile term structure, bootstrap; DISCOVERED + FIXED the backward-FK
  failure for non-autonomous drivers (forward Fokker-Planck-with-potential
  is now the shared engine in phase7.fk_characteristic_inhom and
  phase7.forward_fk_tilted_mass).
- Phase 8 COS-on-the-clock: mgf_A real-potential resolvent, exact CF of
  Z_T, COS pricer (payoff coefficients generalized to out-of-band strikes),
  clock-density-quadrature alternative (robust route), implied-correlation
  smiles (opposite curvature spread vs basket), semi-analytic Greeks.
- Phase 9 estimation: scale observational equivalence theorem (only mu/c,
  sigma/c identified); closed-form OLS MLE; Fisher-RW/OU competitors with
  consistent Jacobians; PIT + pit_state_correlation diagnostics; empirical
  study on XOM/CVX, JPM/BAC, KO/PEP, AAPL/MSFT from local alpha-engine
  store; attenuation study (~4x at 60d windows).
- Phase 10 Phase-Gram: Gaussian-driven triangular angles; exact matrix laws
  via product Gauss-Hermite; analytic R23 Itô drift verified vs MC.
- Phase 11 Levy: VG/NIG exact samplers, Gil-Pelaez marginals, backward
  FK-PIDE solver (implicit Euler, one LU, small-jump compensation +
  effective diffusion); jump asymmetry flips clock drift sign.
- Phase 12 pegged assets: defended-band stationarity, bounded-factor de-peg
  clock, closed-form pay-at-hit Laplace exp((lam-sqrt(lam^2+2r/sig_z^2))*b),
  shortfall swaps via single quadrature; perpetual-mass-corrected inverse
  transform sampler.
- Phase 13 consolidation: flagship manuscript, README update, this handoff.

## Verification status

- python -m unittest discover -s tests => 192/192 OK (182 s) on 2026-08-21.
- Notebooks phase7..phase12 executed clean from clean kernels (seed
  20260821). Runtime ~9 min total.

## Key decisions & gotchas (do not re-litigate)

1. BACKWARD FK IS WRONG for time-dependent coefficients — any new PDE work
   must use phase7.forward_fk_tilted_mass / fk_characteristic_inhom.
2. Bounded-factor models are scale-observationally-equivalent; never fit a
   free c from correlation data alone (Phase-7 bootstrap is exempt:
   exogenous sigma(t) breaks the degeneracy).
3. VG gamma subordinator uses scale=nu (E[G]=t). The exponent functions in
   phase11 are CHARACTERISTIC exponents (real argument = frequency).
4. Infinite-activity Levy PIDE: exclude ONE grid step only; fold excluded
   mass into compensating drift + effective diffusion. Do not add
   m1_trunc*d1 on top of shifted weights (double-counts first moment).
5. Inverse-transform sampling of hazards with mass at infinity: invert RAW
   cdf against uniforms masked at perpetual probability (normalizing
   corrupts frequencies).
6. LSP/pyright errors about sp.diags lists / brentq unions are false
   positives; runtime is fine.

## How to resume

- New phases: follow the per-phase structure (literature review -> module ->
  tests -> builder notebook -> execute -> results -> synthesis).
- Run tests: conda activate phase3-paper; python -m unittest discover -s tests
- Rebuild any notebook: python notebooks/build_phaseNN_*.py then nbclient
  execute (pattern in .agent or existing builders).

## Environment warnings

- pyarrow was pip-installed into phase3-paper (needed for alpha-engine
  parquet). duckdb NOT available in that env.
- phase12 shortfall swap strikes are fractions of parity (levels), not log
  units.
