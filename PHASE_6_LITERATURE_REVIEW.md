# Phase 6 (P1) — Stochastic correlation: initial literature audit and refined problem statement

**Date:** 2026-07-27
**Status:** initial audit — **all source claims below are provisional** (search-engine results and abstracts). Per project standards, nothing here may be cited in a manuscript until verified against the original papers. Items marked ✔ are direct quotes from fetched abstracts/PDFs; the rest are snippet-level and need full-text verification.

---

## 1. Prior art found

### 1.1 Transform-based bounded correlation (closest neighbors)

- **van Emmerich (2006), "Modelling correlation as a stochastic process"** (Bergische Universität Wuppertal preprint 06/03). One of the first continuous-time correlation models: a bounded functional of Brownian motion, and also a Jacobi-process version. Cited as such by Majumdar (2024) ✔ and Márkus (2021) ✔.
- **Teng, Ehrhardt, Günther (2014 preprint / 2016, *J. Math. Industry*)**, "Modelling stochastic correlation." Correlation via a **hyperbolic-tangent transformation of a modified Ornstein–Uhlenbeck process** ✔ ([Springer open access](https://link.springer.com/content/pdf/10.1186/s13362-016-0018-4.pdf)). The Fisher transform \(P=\operatorname{arctanh}(\rho)\) makes the correlation state a diffusion on \(\mathbb R\). ~61 citations.
- **HU-Berlin PhD thesis** (BSDEs/cross-hedging): models correlation through the bijection
  \[b(x)=\frac{x}{\sqrt{1-x^{2}}}\]
  with \(b(\rho_t)\) an OU process. **Note: \(b(x)=\tan(\arcsin x)\) — this is exactly the secant/tangent family of the one-phase framework with \(\rho=\sin\theta\).** This is the single closest prior construction to our phase map; it must be obtained and read before any novelty claim.
- Kumar (2021) PhD thesis (ELTE): \(\rho_t=\tanh(G_t)\), \(G\) OU; states the desiderata explicitly — fluctuation around a constant in the mean-reversion sense, boundaries \(\pm1\) non-attractive and unattainable ✔.

### 1.2 Intrinsic bounded diffusions

- **Jacobi process** (van Emmerich 2006; Ma 2009; Zetocha 2015; Ahdida–Alfonsi): bounded, mean-reverting, but **no closed-form transition density** ✔ (stated explicitly in [this paper](https://www.scirp.org/journal/paperinformation?paperid=76693)); likelihood and pricing need spectral/eigenfunction expansions.
- **Diffusion on the circle — Majumdar (2024)** ([arXiv:2412.06343](https://arxiv.org/abs/2412.06343)): Brownian motion on the circle and the **von Mises diffusion** as correlation models; von Mises diffusion has no closed-form transition density; the paper derives an *approximate* likelihood ✔. Direct conceptual neighbor of our Cayley constant-radius phase; must be cited and differentiated.
- Jacobi stochastic volatility ([arXiv:1605.07099](https://arxiv.org/pdf/1605.07099)): Gram–Charlier series pricing — the standard "bounded factor, series pricing" pattern.

### 1.3 The pricing gap (the open side)

- Existing transform/Jacobi correlation models are "tractable for European vanilla options, but not for the exotic options" ✔ ([arXiv:1701.02821](https://arxiv.org/pdf/1701.02821)); **Higgins (2014)** develops only an *analytical approximation* for barrier and one-touch options under stochastic correlation, via semi-static vega replication.
- Correlation smile in multi-asset equity options is documented (Fengler–Herwartz–Werner; CDO implied-correlation smile literature); constant-correlation local-vol multi-asset models cannot reproduce index smiles (pairwise local correlation literature: Ahdida–Alfonsi, Bossu, Brockhaus, Zetocha).
- **OU first-passage has no closed-form solution** (classical); hence tanh-of-OU correlation models inherit no exact hitting laws for correlation barriers. For arithmetic-Brownian drivers, first-passage is exact via the reflection principle.

---

## 2. Novelty boundary (what cannot be claimed)

1. "Bounded correlation via an invertible transform of a Gaussian factor" — **prior art** (van Emmerich 2006; Teng et al. 2016; Kumar 2021).
2. The specific tangent-arc family \(\rho=\sin\theta\), \(\tan\theta\) Gaussian-factor-driven — **essentially prior art** via \(b(x)=x/\sqrt{1-x^2}\) (HU-Berlin thesis), pending full-text verification. The arctan phase map itself is not new (Phase 5 audit: Särkkä–Solin; Duffie–Kan).
3. "First exact-likelihood bounded correlation model" — false: any invertible transform of a density-known driver trivially has an exact likelihood.
4. Circular/circle-valued correlation modeling — prior art (Majumdar 2024).

## 3. What survives as open (differentiated, checkable)

**O1 — Exact and semi-analytic pricing of path-dependent multi-asset options under stochastic correlation.**
Barrier, one-touch, corridor, and range products on two assets with stochastic \(\rho_t\) currently have only approximations (Higgins 2014). The Brownian-driver phase family carries *exact* hitting and occupation laws through the reflection principle (asset A2 of the framework). Target result: closed-form or one-dimensional-integral prices for correlation-dependent touch/barrier payoffs where today only approximations exist.

**O2 — The stationarity–tractability frontier, classified.**
Every existing bounded-correlation model sits on a trade-off:

| model family | mean-reverting | closed-form transition density | exact first-passage laws |
|---|---|---|---|
| Jacobi | yes | no (spectral series) | no |
| tanh(OU) (Teng et al.) | yes | yes (via transform) | no (OU hitting) |
| von Mises diffusion (Majumdar) | yes | no (approximation) | no |
| **arctan/tan phase of drifted BM (this framework)** | **no** | **yes** | **yes** |
| arctan/tan phase of OU (natural extension) | yes | yes | no |

The classification machinery of the one-phase framework (which drivers/maps give which tractability properties, and *only* those) can make this table a theorem rather than folklore. The non-stationarity of the Brownian-driver phase is an honest economic cost and must be stated, not hidden.

**O3 — Correlation-band events as exact objects.**
Knock-in/knock-out structures on correlation itself (correlation ranges, dispersion trades with correlation barriers) need hitting laws of \(\rho_t\) to levels — exact only for the Brownian-driver phase family. Related to O1 but concerns payoffs written directly on correlation.

## 4. Refined problem statement (recommended scope)

> **A stochastic-correlation framework in which the correlation phase is the arctan/secant one-phase coordinate of a scalar Gaussian factor, delivering (i) the exact bounded transition law, (ii) exact first-passage and occupation laws for correlation barriers — unavailable in every mean-reverting competitor — and (iii) semi-analytic prices for barrier/touch multi-asset options that today admit only approximations; with an explicit classification of which driver choices (Brownian vs. mean-reverting) buy which tractability properties, and an honest statement of the stationarity cost.**

Explicitly out of scope: claiming a new correlation model per se; estimation as the main contribution (exact likelihood is trivial for transform models); matrix-valued correlation dynamics (rank-one restriction of the framework; possible future work via the Phase 4 rigidity results).

## 5. Verification tasks before any manuscript claim

1. Obtain and read: van Emmerich (2006) preprint; Teng–Ehrhardt–Günther (2016, open access); the HU-Berlin thesis section on \(b(x)=x/\sqrt{1-x^2}\); Majumdar (2024, arXiv); Higgins (2014); Zetocha (2015).
2. Confirm whether *any* published model uses \(\rho_t=\sin\theta_t\) or \(\arctan\) of a Gaussian factor with exact transition density for pricing (not just simulation).
3. Confirm the claim "OU first-passage is not closed-form" against the primary literature (Ricciardi–Sato; Alili–Patie–Pedersen) for the comparison table.
4. Confirm Higgins (2014) is still the state of the art for barrier/touch options under stochastic correlation (forward citation search).
5. Check whether the correlation-risk-premium literature (Driessen–Maenhout–Vilkov; Buraschi–Porchia–Trojani) already prices correlation barrier events.

## 5a. Verification progress (2026-07-27)

- **Teng–Ehrhardt–Günther (2016)** — **verified full-text** ([Springer, open access](https://link.springer.com/article/10.1186/s13362-016-0018-4)). Key corrections to §1.1:
  (i) their driver is a *modified* OU, \(dX_t=\kappa(\mu-\tanh X_t)dt+\sigma dW_t\), which itself has no closed-form transition law; consequently **their closed-form density is the stationary density only**, not the finite-time transition density. Our exact finite-time kernel survives as a differentiator.
  (ii) They *explicitly considered and rejected* an arctan-type correlation map \(\rho=\frac{2}{\pi}\arctan(\frac{\pi}{2}x)\) ("rather complicate … tedious"; tail-estimation critique). Our \(\rho=\sin(\arctan(X/c))=X/\sqrt{X^2+c^2}\) is a different member of the arctan family, but the rejection must be cited and answered: our boundaries are approached polynomially (\(1-\rho\sim (2x^2)^{-1}\)), even more slowly than tanh's exponential — an honest cost for estimation, to be addressed at the estimation stage.
  (iii) Their quanto pricing is conditional Monte Carlo around Black–Scholes — no exact results for path-dependent payoffs. The O1 pricing gap is confirmed in their framework.
- **Higgins (2014)** — arXiv:1404.4028, **scope correction**: it concerns *spot/volatility* correlation (Heston-type), not asset–asset correlation; its semi-static vega-replication approximation for barrier/one-touch options is evidence for the exotics gap in that adjacent market, not a multi-asset benchmark. Snippet-level; full text pending.
- **Majumdar (2024)** — abstract verified (von Mises diffusion on the circle; no closed-form transition density; approximate likelihood derived). Full text pending.
- **van Emmerich (2006)** — content verified *second-hand* through Teng et al. (2016) §2.3, which derives the van Emmerich SDE \(d\rho=\kappa^*(\mu^*-\rho)dt+\sigma^*\sqrt{1-\rho^2}\,dW\) as a special case of the tanh transform and quotes its boundary condition \(\kappa^*\ge\sigma^*/(1\pm\mu^*)\). Original preprint still to be obtained.
- **OU first passage** — classical negative result (Ricciardi–Sato; Alili–Patie–Pedersen representations are series/special-function only). Treated as established; primary-source citation to be added at manuscript stage.
- **HU-Berlin thesis** — direct quote obtained from extracted PDF text ("we will choose as bijection \(b(x)=x/\sqrt{1-x^2}\)"), i.e. \(\tan\circ\arcsin\) with an OU driver — the closest neighbor to our construction. Full bibliographic details pending.

## 6. Milestone 1 (mathematical, pre-economic)

Derive and numerically verify the exact law of the first passage of \(\rho_t=\sin\theta_t\) (equivalently \(\theta_t\)) to a correlation level, under the drifted-Brownian driver, via the reflection principle through the tangent conjugacy; cross-check against Monte Carlo with fixed seeds under project notebook standards (conda env `phase3-paper`). This is the atomic result underlying O1–O3 and is achievable with machinery already verified in Phase 5.
