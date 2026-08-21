# Phase 12 — Synthesis: pegged-asset economics

**Date:** 2026-08-21
**Status:** complete — 7/7 unit tests, clean notebook, simulation vs exact
within ~1 SE.

---

## 1. The construction

The bounded-factor framework, built for correlation, transfers verbatim to
**pegged-asset credit**: the de-peg event is first passage of an
independent credibility factor through a threshold, and every law needed by
a derivatives desk is already in the project's toolbox:

- defended-band stationarity (exponential trapezoid, closed form);
- de-peg CDF / IG density / perpetual mass (Milestone 1);
- pay-at-hit Laplace transform, derived here in bounded-factor coordinates:
  \(E[e^{-r\tau}]=\exp\big((\lambda-\sqrt{\lambda^2+2r/\sigma_z^2})\,
  \Delta\big)\) — note the clean appearance of the raw \(\lambda\) and the
  discount rate entering only as \(r/\sigma_z^2\) (operational-time
  structure made explicit; verified to \(10^{-6}\) against exact-density
  quadrature after two sign/scale errors were caught by the anchors);
- hazard-contingent shortfall swaps: ONE quadrature over the exact IG
  density times closed-form Gaussian components.

## 2. Findings worth keeping

1. The full derivative stack prices **deterministically** — no Monte Carlo
   anywhere on the pricing path; simulation only validates.
2. De-peg probabilities are strongly concave in horizon
   (1.7% / 7.7% / 17.8% / 31.7% at 0.5/1/2/5y for the reference calibration):
   the perpetual mass 48.9% caps long-dated digitals, a feature any
   exponential-hazard model misses.
3. Implementation lessons recorded: inverse-transform sampling of a hazard
   with mass at infinity must invert the RAW cdf against uniforms masked at
   the perpetual probability; normalizing rescales uniforms and silently
   doubles frequencies.

## 3. Novelty boundary (post-audit)

Claimed as new: the two-factor defended-band/de-peg-clock model with fully
deterministic derivative pricing; the bounded-coordinate pay-at-hit
transform; the hazard-consistent shortfall-swap formula. Not claimed:
reflected-BM theory, Krugman target zones, first-passage transforms,
Bachelier components.

## 4. Deliverables

`PHASE_12_LITERATURE_REVIEW.md`, `phase12_peg.py`,
`tests/test_phase12_peg.py` (7/7),
`notebooks/build_phase12_peg.py` + executed notebook (~2.5 s,
seed 20260821), `PHASE_12_SIMULATION_RESULTS.md`, `phase12_figures/`.
