# Phase 9 — Synthesis: exact estimation and the empirical study

**Date:** 2026-08-21
**Status:** complete — 14/14 unit tests, clean notebook on real data,
structural identifiability theorem proved and exploited.

---

## 1. The structural theorem (the phase's headline)

**Scale observational equivalence.** For the bounded-factor correlation
model, the parameter triples \((c,\mu,\sigma)\) and
\((\lambda c,\mu/\lambda,\sigma/\lambda)\) induce *identical* laws for every
observable correlation functional — and, because the DDS clock
\(v=\beta T+\alpha A_T\) is a functional of the \(\rho\)-path alone, for
every correlation-derivative price as well. Only the ratios
\(\mu/c\) (drift ratio) and \(\sigma/c\) (volatility ratio) exist in the
identified parameter space.

Consequences drawn in-project:
- The correct estimator works in the normalized coordinate
  \(x=\rho/\sqrt{1-\rho^2}\), where increments are exactly Gaussian and the
  exact MLE of \((\mu/c,\sigma/c)\) is **closed-form OLS** — no optimization.
- A free-scale profile likelihood is flat along a valley; any reported
  "MLE of \(c\)" from correlation data alone is an initialization artifact.
  (The Phase-7 bootstrap is exempt: there \(\sigma(\cdot)\) is exogenously
  known, which breaks the degeneracy through the time-scale ruler.)
- Prior-art calibration practice (stationary-density least squares,
  back-transformed OLS) implicitly estimated ratios without stating the
  equivalence; the theorem makes it explicit and explains why.

## 2. Diagnostics that match failure modes

Marginal PIT/KS tests calibration but can be blind to dynamic
misspecification whose u-marginal stays near-uniform (demonstrated: RW fit
to mean-reverting data, KS p=0.53 while corr(u, state)=−0.148 ≈ 8σ). The
PIT–state-correlation diagnostic is added to the toolkit and is what
separates models out-of-sample.

## 3. Empirical findings (four S&P 500 pairs, 2015–2026)

1. Realized correlations are high and persistent
   (means 0.55–0.85, sd 0.10–0.22).
2. Exact-MLE volatility ratios by pair: XOM/CVX 1.17, JPM/BAC 1.55,
   KO/PEP 0.91, AAPL/MSFT 0.84 (attenuated lower bounds, Section 4).
   Drift ratios are statistically indistinguishable from zero at daily
   frequency (SE ≈ 0.11/yr).
3. Fisher-space OU wins AIC everywhere with weak reversion
   (\(\kappa\approx1.4–2.3\)/yr) — persistence largely inherited from
   overlapping-window smoothing.
4. **Attenuation law**: window noise damps measured dynamics ~4× at the
   standard 60-day window (factor 0.253); short windows can inflate it
   (1.21 at 20 days). Any calibration from smoothed proxies must invert
   this curve before quoting dynamics.
5. All iid-increment models reject marginal KS out-of-sample on smoothed
   proxies — an observation-scheme violation, not a model rejection;
   recorded as the honest limitation motivating state-space filtering of
   the proxy noise (future work).

## 4. Novelty boundary (post-audit)

Claimed as new: the scale observational-equivalence theorem; the two-
parameter closed-form exact MLE; the conditional-uniformity diagnostic; the
attenuation quantification; the first exact-MLE empirical study of a
bounded-factor correlation model. Not claimed: QMLE generally, realized-
volatility proxy methodology, PIT/KS machinery, copula filtering.

## 5. Deliverables

`PHASE_9_LITERATURE_REVIEW.md`, `phase9_estimation.py`,
`tests/test_phase9_estimation.py` (14/14),
`notebooks/build_phase9_estimation.py` + executed notebook (~6 s,
seed 20260821), `PHASE_9_SIMULATION_RESULTS.md`, `phase9_figures/`.
