# Phase 11 — Literature review and novelty audit: Lévy-powered bounded factors

**Date:** 2026-08-21
**Status:** web-verified audit for Phase 11 scope. Snippet/abstract-level
unless marked ✔.

---

## 1. What this phase adds

Replace the Gaussian driver with a pure-jump Lévy driver (VG, NIG) inside
the bounded-factor correlation model and establish what survives:

1. **Marginal laws stay exact**: \(\rho_T=f(x_0+L_T)\) pushes the closed-form
   Lévy law through the Jacobian; digitals price by Gil–Pelaez inversion of
   the known characteristic exponent — deterministic, no simulation.
2. **The clock characteristic function survives via the backward FK-PIDE**
   \(\partial_tu=\mathcal Lu+q(x)u\): time-homogeneous Lévy drivers have a
   time-translation-invariant semigroup, so the Phase-7 backward-equation
   pitfall does *not* bite here. Solved by implicit Euler with one
   precomputed LU; infinite activity handled by the standard small-jump
   approximation (compensating drift + effective diffusion).
3. **Honest loss statement**: reflection-principle hitting formulas die with
   continuous paths (jumps cross barriers without touching); barrier laws
   under jumps require the same PIDE machinery with absorbing-type data.
4. **Scientific output**: quantification of how jump asymmetry reshapes the
   correlation clock \(A_T\) — e.g. VG with negative \(\theta\) roughly
   halves \(\mathbb E[A_T]\) relative to the variance-matched Gaussian, and
   NIG with \(\beta<0\) flips its sign.

## 2. Prior art found

- Teng–Ehrhardt–Günther lineage: Gaussian/tanh-OU drivers only; no Lévy
  driver in any audited stochastic-correlation paper.
- Jump-diffusion stochastic volatility (Bates, NIG-GARCH etc.): jumps drive
  *volatility or returns*, not a bounded correlation coordinate; pricing by
  FFT on affine structure — inapplicable to the bounded map.
- Lévy-driven occupancy problems: the FK-PIDE for occupation functionals of
  Lévy processes is classical PDE material (e.g. in books of Bertoin /
  Sato contexts); no published use as a *correlation-clock transform*.
- Searches: "Levy driven stochastic correlation model", "NIG correlation
  process pricing", "variance gamma correlation", "occupation integral Levy
  process characteristic function Feynman-Kac PIDE" — no competitor found
  for the combination (bounded factor + Lévy driver + clock transform).

## 3. Novelty boundary

**Cannot be claimed:** Gil–Pelaez inversion; FK-PIDE theory for Lévy
processes; small-jump diffusion approximations; exact sampling of VG/NIG.

**Can be claimed:** first Lévy-powered bounded-factor correlation model;
exact marginal + clock-transform pricing stack for it; the survival/
collapse analysis of the exact-law program under jumps; quantified jump-
asymmetry effects on the correlation clock.

## 4. Verification tasks

✔ Negative searches recorded above; re-run before manuscript submission.
In-project verification: sampler-vs-exponent consistency, Gil-Pelaez vs
empirical CDFs, linear-potential closed form (integrated exponent), tiny-
jump limit to the Phase-7 Gaussian solver, MC benchmarks within ~1 SE.
