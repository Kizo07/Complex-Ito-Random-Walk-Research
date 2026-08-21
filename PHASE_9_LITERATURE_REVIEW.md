# Phase 9 — Literature review and novelty audit: estimation of stochastic correlation models

**Date:** 2026-08-21
**Status:** web-verified audit for Phase 9 scope. Snippet/abstract-level
unless marked ✔.

---

## 1. What this phase adds

1. **A structural identifiability theorem**: the bounded-factor correlation
   model \(\rho_t=f(X_t)\), \(f(x)=x/\sqrt{x^2+c^2}\),
   \(dX=\mu\,dt+\sigma\,dW\) is *scale-observationally-equivalent* —
   \((c,\mu,\sigma)\sim(\lambda c,\mu/\lambda,\sigma/\lambda)\) induce
   identical laws for every observable correlation functional (and, since
   the DDS clock \(v=\beta T+\alpha A_T\) depends only on the \(\rho\)-path,
   for every derivative price as well). Only the ratios \(\mu/c,\sigma/c\)
   are identified from correlation observations.
2. **Exact closed-form MLE** of those ratios: in the normalized coordinate
   \(x=\rho/\sqrt{1-\rho^2}\) increments are exactly Gaussian, so the MLE is
   OLS — no optimization at all — with consistent Jacobian for the observed
   series.
3. **Diagnostics that match the failure modes**: marginal PIT/KS plus
   PIT–state correlation (marginal KS can miss dynamic misspecification).
4. **First systematic attenuation quantification** for window-estimated
   correlations in this model class.
5. An empirical study on four liquid S&P 500 pairs (2015–2026, local store).

## 2. Prior art found

- **Teng, Ehrhardt & Günther (2016, JMIV)** ✔ and the follow-up review
  (Springer 2018): tanh(OU) stochastic correlation processes. Their own
  text: *"Considering the density function (39), it will be tedious to
  determine its likelihood-function"* — they calibrate by fitting the
  **stationary** density to a histogram via nonlinear least squares. No
  finite-time-transition likelihood, no exact MLE, no identifiability
  analysis.
- **Kumar, Márkus & Hári (2021, CVA/wrong-way-risk)** ✔: back-transforms the
  estimated correlation process and applies *ordinary least squares to the
  OU in Fisher space* — ad hoc QMLE without Jacobian consistency or
  diagnostics.
- **Aas et al. (2010, dynamic copulas)** ✔: latent dependence processes
  estimated by efficient importance sampling — computationally heavy MC
  inference, no closed-form likelihood.
- **Aït-Sahalia et al. (correlation inference for semimartingales)** ✔:
  high-frequency estimation of a CONSTANT correlation parameter — different
  problem (no stochastic correlation dynamics).
- Barndorff-Nielsen–Shephard-style realised-volatility quasi-likelihood ✔:
  the template for handling noisy proxies; not applied to bounded
  correlation factors.
- Searches for "exact maximum likelihood stochastic correlation",
  "identifiability bounded correlation process", "realized correlation
  attenuation stochastic correlation model" returned no competitor for any
  of the five items above.

## 3. Novelty boundary

**Cannot be claimed:** Gaussian QMLE for transformed diffusions generally;
realized-correlation measurement-error ideas; PIT/KS machinery; DCC-type
filtering.

**Can be claimed:** the scale observational-equivalence theorem (with its
consequence that even derivative prices cannot break the degeneracy);
the resulting two-parameter exact MLE; the conditional-uniformity diagnostic
argument; the attenuation factors; the first exact-MLE-based empirical study
of a bounded-factor correlation model.

## 4. Verification tasks

✔ Teng et al. stationary-density calibration quote (full text fetched).
✔ Kumar et al. back-transformed OLS description (arXiv HTML fetched).
✔ Aas et al. EIS approach (Wiley abstract).
✔ Negative searches recorded above; re-run before manuscript submission.
