# Phase 11 — Synthesis: Lévy-powered bounded factors

**Date:** 2026-08-21
**Status:** complete — 9/9 unit tests, clean notebook, PIDE vs MC within
~1–2 SE at all frequencies, closed-form anchors verified.

---

## 1. The question and the answer

*Does the exact-law program survive jump-driven correlation?* Two of the
three layers do, one dies honestly:

| layer | Gaussian driver | Lévy driver |
|---|---|---|
| marginal laws | exact closed form | **exact** (Gil–Pelaez pushforward) |
| clock transform \(E[e^{i\xi A_T}]\) | forward FK-PDE (Phase 7 fix) | **exact via backward FK-PIDE** — valid precisely because time-homogeneous Lévy drivers keep semigroup time-translation invariance (the Phase-7 pitfall is a *time-dependence* phenomenon) |
| reflection-principle barrier laws | exact (Milestones 1–2) | **dead** — jumps cross levels without touching; barrier laws need absorbing-type PIDEs |

## 2. Technical contributions

1. Implicit-Euler FK-PIDE solver with a single precomputed LU (the operator
   is time-independent), localized domains with jump-aware margins.
2. Infinite-activity handling by the small-jump approximation: excluded
   sub-grid mass enters as a compensating drift plus an effective diffusion;
   verified against the linear-potential closed form
   \(\exp(iu(x_0T+bT^2/2)+T\int_0^1\psi(uT(1-r))dr)\) and against the tiny-
   jump limit of the Phase-7 Gaussian solver.
3. Exact VG/NIG samplers validated against their own exponents — which
   caught two convention bugs (gamma-subordinator scale; characteristic-
   exponent call conventions) that would have silently corrupted everything.

## 3. Scientific findings

1. **Jump asymmetry halves the correlation-clock mean**: variance-matched
   VG (\(\theta=-0.12\)) gives \(E[A_T]=0.0350\) vs Gaussian 0.0730.
   Marginal calibration of the driver does NOT pin down path-dependent
   correlation risk.
2. **Sign flip**: NIG with \(\beta<0\) produces negative clock drift
   (Im \(\phi_A<0\)) — negative average correlation from a driver whose
   marginals match a positive-correlation Gaussian model. A clean, testable
   jump signature.
3. Consequence for practice: any hedging/calibration of correlation
   derivatives under jumps must price with the PIDE transform; Gaussian
   calibrations systematically misstate both level and skew of correlation-
   risk timing.

## 4. Novelty boundary (post-audit)

Claimed as new: first Lévy-driven bounded-factor correlation model with an
exact pricing stack; survival/collapse analysis of the exact-law program
under jumps; quantified jump-asymmetry effects on the correlation clock.
Not claimed: Gil–Pelaez inversion, FK-PIDE theory, small-jump schemes,
VG/NIG simulation.

## 5. Deliverables

`PHASE_11_LITERATURE_REVIEW.md`, `phase11_levy.py`,
`tests/test_phase11_levy.py` (9/9),
`notebooks/build_phase11_levy.py` + executed notebook (~321 s, seed
20260821), `PHASE_11_SIMULATION_RESULTS.md`, `phase11_figures/`.
