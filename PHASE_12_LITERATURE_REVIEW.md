# Phase 12 — Literature review and novelty audit: pegged-asset economics

**Date:** 2026-08-21
**Status:** web-verified audit for Phase 12 scope. Snippet/abstract-level.

---

## 1. What this phase adds

A closed-form, hazard-consistent pricing framework for **de-peg
derivatives** on defended-band pegged assets (stablecoins, currency boards,
ERM-style bands):

1. **Defended band**: log-mispricing as two-sided reflected Brownian motion;
   stationary law = exponential trapezoid \(\pi\propto e^{2by/\sigma^2}\)
   (closed form; classical RBM material used, not claimed).
2. **Credibility clock**: de-peg event modeled as first passage of the
   project's bounded credibility factor \(C_t=f(Z_t)\) to \(c_*\) — every
   Milestone-1 law transfers verbatim: hitting CDF, calendar IG density,
   perpetual mass, and the pay-at-hit Laplace transform
   \(E[e^{-r\tau}]=\exp((\lambda-\sqrt{\lambda^2+2r/\sigma_z^2})\,\Delta)\).
3. **Contingent claims**: shortfall swaps \(((K-P_T)^+\) paid only if
   de-pegged by \(T\)) reduce to ONE quadrature over the exact IG density
   times closed-form Gaussian components — fully deterministic.
4. Inverse-transform simulation benchmark that correctly respects the
   perpetual hitting probability (<1) — including the subtle point that
   normalizing the hazard CDF rescales uniforms and corrupts frequencies.

## 2. Prior art found

- Stablecoin de-peg literature: overwhelmingly empirical (event studies of
  USDC/Terra/DAI episodes); ERM crises (1992) modeled with speculative-
  attack frameworks (Obstfeld-type), not derivative pricing.
- Band/target-zone models: Krugman (1991) target zones — smooth-pasting
  credible-band valuation; no stochastic credibility hazard and no
  contingent-payoff stack.
- De-peg "digital" instruments exist over-the-counter (per anecdotal
  search results) but no published closed-form pricing framework coupling a
  defended band to an independent stochastic credibility clock was found.
- First-passage/Laplace-transform formulas: classical (used, not claimed).

## 3. Novelty boundary

**Cannot be claimed:** reflected-BM theory, Krugman target zones,
first-passage transforms, Bachelier components.

**Can be claimed:** the two-factor defended-band/de-peg-clock model with its
fully deterministic derivative stack; the exact pay-at-hit transform in the
proportional class expressed through bounded-factor quantities; the
hazard-consistent shortfall-swap formula; the inverse-transform sampler
with perpetual-mass correction.

## 4. Verification tasks

✔ Negative searches recorded above; re-run before manuscript submission.
In-project verification: stationary-law quadrature anchors (uniform at zero
drift), CDF cross-check vs Phase 6, Laplace transform vs exact IG-density
quadrature, simulation frequency vs exact CDF within ~1 SE.
