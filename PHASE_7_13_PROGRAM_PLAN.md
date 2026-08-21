# Phases 7–13 program plan: expanding the exact bounded-factor framework

**Date:** 2026-08-21
**Status:** approved scope for the session (user-directed autonomous run)
**Inputs:** Phases 1–6 deliverables; `PHASE_6_FINANCE_APPLICATION_PROBLEM_LIST.md`
deferred items; 2026-08 novelty re-audit (web-verified, recorded per phase in
each `PHASE_{7..13}_LITERATURE_REVIEW.md`).

---

## 0. What is genuinely innovative (filter result)

The project's defensible core, confirmed against 2024–2026 literature:

1. **Exact-kernel bounded factors.** The conjugate correlation
   \(\rho_t=X_t/\sqrt{X_t^2+c^2}\) of a Gaussian factor is, per the Phase 6
   audit and the 2026-08 re-check, still the only bounded stochastic-correlation
   model with a *single-expression finite-time transition density* and
   *reflection-principle first-passage laws*. Closest competitors (Majumdar
   2024 circle diffusion; Teng–Ehrhardt–Günther tanh-OU; Jacobi/Wishart) have
   stationary-only, spectral, or approximate laws.
2. **Clock reductions.** The DDS variance-clock collapse of joint two-asset
   barrier claims to one scalar functional \(A_T=\int\rho\) (Phase 6 M3) and its
   exact full law via FK/Fourier (M4) have no published counterpart applied to
   multi-asset pricing.
3. **The classification/rigidity theory** (Phase 5) as a model-selection tool.

Everything else (complex Itô algebra, polar forms, Cayley maps) is rigorous
synthesis of known ingredients — valuable, but not where new ground lies.

## 1. Program: seven phases that expand the innovative core

Each phase follows the established structure: plan → literature review →
module + unit tests (`unittest`, conda env `phase3-paper`) → deterministic
notebook builder + executed notebook → simulation-results record → synthesis.

| Phase | Title | New content | Consumes |
|---|---|---|---|
| 7 | Time-inhomogeneous exactness and the correlation term structure | Deterministic \(\mu(t),\sigma(t)\): every density-based law survives with integrated coefficients; exact distributional term structure \(q_\alpha(t)=f(m(t)+\sqrt{v(t)}\Phi^{-1}(\alpha))\); forward-start digitals; term-structure bootstrap of \((c,\mu^{\mathbb Q})\) | A1, A2 |
| 8 | Vanilla spread/basket options under stochastic correlation: COS-on-the-clock | Conditional-Bachelier reduction \(V=\mathbb E[h(q_0T+q_1A_T)]\); Fourier-series clock density ⇒ semi-analytic vanilla prices, Greeks, implied-correlation smile signature | A2, M3/M4 machinery |
| 9 | Exact estimation and an empirical study on equity pair correlations | Exact Gaussian-profile MLE of \((\mu,\sigma,c)\); competitor models (constant, OU-tanh QMLE); PIT density-forecast tests; first estimation study of the model on real S&P500 pair data (local alpha-engine store) | A1, A6 |
| 10 | Correlation-matrix processes with exact finite-time law | Phase-Gram construction \(R_{ij}=\langle u_i(\theta),u_j(\theta)\rangle\) on even-dimensional spheres: a.s. PSD by Gram construction, exact multivariate-normal pushforward density, explicit Itô dynamics, exact panel likelihood | A1, A5 |
| 11 | Jump-driven exactness: Lévy-powered bounded factors | \(\rho_t=f(L_t)\), \(L\) NIG/VG: exact characteristic function ⇒ exact transition densities by 1-D Fourier inversion; closed-form digitals; honest barrier status (no reflection principle); crash-tail comparison vs Brownian driver | A1, A5 |
| 12 | Pegged-asset economics: de-peg derivatives and defended bands | Killed phase diffusion = de-peg model: survival probabilities, perpetual exit odds, de-peg swaps/digitals/accruals in closed form; reflected (defended) band stationary law; stablecoin/target-zone application layer | A1, A2, A4 |
| 13 | Flagship consolidation: the exact bounded-factor framework | Unified manuscript; conjugacy dictionary (driver × map × exact contents); full-suite verification; grand synthesis and future-work map | all |

## 2. Standards (inherited)

- All writes under `/home/fire/Documents/Complex-Ito-Random-Walk-Research`.
- Conda env `phase3-paper` (Python 3.12.13); no environment changes.
- Fixed seeds; MC standard errors reported; analytic-vs-MC cross-checks;
  two discretization levels where numerics are approximate.
- Distinguish exact identities / closed forms / quadrature-exact /
  numerical methods; state every structural assumption (e.g. independence of
  the correlation driver) and every cost (non-stationarity, rank caps,
  polynomial tails).
- Notebooks execute top-to-bottom from a clean kernel; deterministic builders;
  executed outputs saved.
- Novelty claims only after the per-phase literature audit; excluded claims
  listed explicitly.

## 3. Acceptance gates

Per phase:
1. Unit tests pass (`python -m unittest`) with cross-module consistency
   anchors to Phase 6 formulas at overlapping scope.
2. Notebook executes clean, zero errors, moderate runtime (< ~120 s).
3. At least one closed form verified against independent Monte Carlo within
   ~2 standard errors.
4. Literature review records verified sources and a novelty boundary.

Program-level (Phase 13):
5. Full test suite green across phases 4–12 modules.
6. Unified manuscript renders (Quarto if available; Markdown fallback).
7. README/status/handoff updated.
