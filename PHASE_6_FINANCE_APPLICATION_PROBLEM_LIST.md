# Phase 6 — Candidate open problems in financial economics and derivative pricing for the one-phase Euler framework

**Date:** 2026-07-27
**Status:** candidate list, pre-selection
**Inputs:** `single-phase-euler-representation.md`, `exact_one_phase_euler_representation_additive_brownian_motion.md`, `paper/one-phase-euler/RESEARCH_NOTES.md`, `phase5_finance.py`

---

## 0. What the research actually provides (asset inventory)

Any application must consume one or more of these concrete, verified assets. Claims not backed by this list are excluded per project standards.

- **A1 — Exact bounded-diffusion conjugacy.** \(\theta_t=\arctan(X_t/c)\) maps an arithmetic (drifted) Brownian factor \(X_t\) to a diffusion on the bounded interval \((-\pi/2,\pi/2)\) with *closed-form Gaussian-in-tangent transition density* (§14 of the exact-representation note), explicit generator with \(\cos^2\theta\) damping, known scale function \(s(\theta)\propto e^{-(2\lambda/\nu)\tan(\theta-\varphi)}\), and unattainable endpoints maintained without boundary conditions.
- **A2 — Exact first-passage conjugacy.** Level crossings of \(X\) are level crossings of \(\theta\) at a known angle, so all reflection-principle results for Brownian motion (hitting probabilities, running maxima laws, barrier parity) transfer exactly to the phase coordinate.
- **A3 — Classification and rigidity theorems.** A time-independent genuine one-phase representation of \(Z_t=Z_0+at+bW_t\) exists iff \(a/b\in\mathbb R\) and \(b/Z_0\notin\mathbb R\); lines (additive) and logarithmic spirals (multiplicative) exhaust the constant-coefficient polar graphs. This is a *model-selection* tool: it tells you exactly which SDE families admit the phase-only form.
- **A4 — Cayley unit-circle compactification.** Lossless, constant-radius, injective encoding of the real factor, with the missing point inaccessible in finite time.
- **A5 — Design dictionary / exact solvability.** Any polar graph \(r(\theta)\) yields a one-driver process; the two named families give constant-coefficient dynamics, the rest give state-dependent coefficients that are still exactly simulable through the conjugate Brownian coordinate (exact, not Euler–Maruyama, transitions).
- **A6 — Phase-first Markov formulation.** The phase can be defined as the primitive state by its martingale problem on a bounded interval, with no explicit Brownian driver — useful when the *estimable object* is the bounded coordinate rather than the level.

Established negative results that constrain applications (from the Phase 5 audit and `RESEARCH_NOTES.md` §9, §12):

- **N1.** Exact round-trip Monte Carlo is *unchanged* by the coordinate map; no automatic variance reduction.
- **N2.** \(\arctan\) compactification of pricing PDEs is prior art (Duffie–Kan 1996; in 't Hout–Snoeijer 2021); arctan of Brownian motion is a known exact SDE example (Särkkä–Solin 2019). Novelty must come from the classification, the exact kernels, or a new financial structure — not from the transform itself.
- **N3.** One phase cannot losslessly encode genuine two-factor noise; applications must have a real one-driver structure or accept a projection.

---

## 1. Candidate problem list

Each entry: the open problem, why it is open, which assets apply, an honest feasibility/novelty assessment, and the literature that must be checked before claiming anything.

### P1. Tractable stochastic correlation for multi-asset derivatives

**Problem.** Multi-asset pricing (basket, spread, quanto, worst-of options) needs stochastic correlation \(\rho_t\in(-1,1)\). There is no widely accepted model combining (i) bounded state in \((-1,1)\), (ii) closed-form transition density, (iii) closed-form or semi-closed-form derivative prices. The correlation smile is documented but not explained by a standard tractable model; Jacobi-diffusion correlation models require eigenfunction/spectral expansions for their densities.

**Assets used.** A1, A2, A3, A5. Take \(\rho_t=\sin\theta_t\) (or \(\tanh\)-type maps) with \(\theta_t\) the arctan-of-Brownian phase: a bounded correlation diffusion whose transition density is a *single Gaussian in a tangent variable*, not a spectral series. The classification theorem (A3) delimits exactly which joint \((S_1,S_2,\rho)\) SDE structures admit the one-phase form.

**Why it fits.** Correlation is the canonical bounded scalar factor in finance; the research's core object is a bounded scalar factor with an exact law. The gap (closed-form density vs. Jacobi spectral expansions) is concrete and checkable.

**Feasibility/novelty.** High feasibility: the one-asset phase theory is done; the work is embedding it into a two-asset pricing framework, deriving the joint characteristic structure, and checking the martingale/no-arbitrage conditions on \(\rho_t\). Novelty risk: moderate — stochastic correlation is a crowded field (e.g., Jacobi and Wishart-based models), so the differentiator must be the exact closed-form kernel and exact simulation, stated precisely.

**Literature to audit.** Jacobi correlation models for basket options; Wishart affine correlation; correlation smile empirical literature; bounded-factor diffusions in term-structure modeling.

### P2. Derivative pricing under target zones, currency bands, and pegged assets (including stablecoin de-peg risk)

**Problem.** Exchange-rate target zones (Krugman 1991 lineage) model a band-limited underlying, but *derivative* pricing on banded/ pegged underlyings is underdeveloped: options whose underlying cannot leave a band, instruments paying on band defense or band breach, and the currently unsolved practical problem of pricing stablecoin de-peg risk (no standard no-arbitrage model; ad-hoc hazard-rate approaches dominate). First-passage and occupation laws inside the band drive every payoff of this kind.

**Assets used.** A1, A2, A4, A6. The phase coordinate is *itself* a band-limited underlying with unattainable or (via killing) attainable endpoints; A2 gives exact hitting/occupation laws for free from the Brownian reflection principle; a killed phase diffusion is a natural de-peg model where de-peg = first arrival at the band edge, with closed-form survival probabilities.

**Why it fits.** This is the only candidate where the *boundedness itself* is the economic phenomenon, not a numerical convenience. Exact first-passage conjugacy is a differentiated, verifiable asset.

**Feasibility/novelty.** High feasibility, lowest mathematical risk of the list: the probability machinery already exists in the notes and only needs an economic model wrapped around it (band defense policy, credible vs. incredible bands, killing at the boundary). Novelty risk: low for the Krugman-style economics (well-trodden in the 1990s), but the derivative-pricing and stablecoin angle appears genuinely sparse. Must audit before claiming.

**Literature to audit.** Krugman (1991); Bertola–Caballero and Svensson target-zone follow-ups; EUR/CHF floor and HKD band empirical work; stablecoin de-peg modeling papers (mostly 2022+); barrier option theory in normal models.

### P3. Exact simulation and unbiased Greeks for conjugate diffusion classes

**Problem.** Unbiased Monte Carlo simulation of general diffusions (Beskos–Roberts exact algorithm) is powerful but technically heavy; most finance diffusions are still simulated by Euler–Maruyama with bias. The open methodological question: which financially relevant SDEs are *monotonely conjugate to Brownian motion* and therefore exactly simulable by transform, and can that conjugacy be exploited for pathwise Greeks and likelihood-based estimation?

**Assets used.** A1, A5, A6. The design dictionary generates exactly simulable state-dependent-coefficient models; the exact phase kernel gives exact likelihoods (useful for estimation, not just simulation).

**Feasibility/novelty.** High feasibility, but weakest novelty: sits directly against Beskos–Roberts (2005) and the Lamperti-transform literature, and N1 caps the Monte Carlo gains. Would need a sharp angle (e.g., exact MLE for discretely observed bounded factors) to stand.

**Literature to audit.** Beskos–Roberts exact algorithm; Lamperti/Doss–Sussmann/Zvonkin (already audited in Phase 5); exact MLE for diffusions.

### P4. Risk-neutral density recovery as a compactified inverse problem

**Problem.** Recovering risk-neutral densities from option prices is a classical ill-posed inverse problem (Breeden–Litzenberger and descendants); instability in the tails is the main defect. Mapping the underlying to the bounded phase \((-\pi/2,\pi/2)\) turns the problem into a well-conditioned expansion on a compact interval with automatic tail behavior and natural rational spectral bases (Boyd).

**Assets used.** A1, A4; A6 for the forward model.

**Feasibility/novelty.** Moderate feasibility (numerical-method paper). Novelty risk: moderate-high — compactification in PDE pricing is prior art (N2), so the contribution would have to be the *inverse* problem specifically, with measured stability gains, not the map.

**Literature to audit.** Breeden–Litzenberger; nonparametric RND estimation; Boyd rational Chebyshev on mapped intervals; in 't Hout–Snoeijer.

### P5. American and free-boundary problems in bounded phase coordinates

**Problem.** No closed-form American put exists even in the normal model; free-boundary numerics on unbounded domains require artificial truncation. The phase map is a built-in front-fixing-style compactification with the far field at \(\pm\pi/2\).

**Assets used.** A1, A2.

**Feasibility/novelty.** Low novelty for numerics (compactification is prior art, N2); a long shot analytically. Included for completeness; not recommended.

### P6. Arithmetic Asian options via phase coordinates

**Problem.** No Black–Scholes-type closed form for arithmetic-average options (Zhang 2003, audited in Phase 5). The integral of \(c\tan\theta_t\) against the exact phase kernel might yield new exact representations or sharper bounds on the bounded domain.

**Assets used.** A1, A6.

**Feasibility/novelty.** Famous and high-value, but the phase map does not linearize the time integral of the state; probability of a closed form is low. Could yield new bounds. Not recommended as the primary target.

### P7. Model-invariance of the phase representation under equivalent measure changes

**Problem.** Girsanov changes drift, not diffusion direction — so the classification conditions \(a/b\in\mathbb R\), \(b/Z_0\notin\mathbb R\) behave in a specific, checkable way under change of numéraire. Open question: which pricing models remain inside the exactly phase-representable class under the risk-neutral and forward measures, and is that invariance itself a useful modeling axiom?

**Assets used.** A3 primarily.

**Feasibility/novelty.** Small, clean, theorem-shaped — but likely a *section* of another paper rather than a standalone problem. Recommended as a component of whichever problem is selected, not as the target.

### P8. Bounded volatility factors with exact laws

**Problem.** Volatility-of-vol and volatility level are empirically bounded; Jacobi-type bounded volatility models exist but share the spectral-density burden of P1. A phase-driven volatility factor has an exact kernel.

**Assets used.** A1, A5.

**Feasibility/novelty.** Feasible but crowded (Heston descendants, Jacobi vol, rough vol). The exact-kernel differentiator is weaker here than in correlation because volatility is latent, so estimation — not pricing — is the bottleneck, and the exact likelihood (A1) is the actual asset. Foldable into P1.

### P9. Occupation-time and range-accrual derivatives on bounded factors

**Problem.** Range accruals and corridor products pay on occupation time of a band; closed-form occupation laws are scarce outside Brownian motion. The phase conjugacy transfers Brownian occupation/arc-sine laws exactly.

**Assets used.** A2, A1.

**Feasibility/novelty.** Feasible, niche. Likely a corollary of P2 rather than a standalone.

---

## 2. Comparison and shortlist

| | Tractability now | Openness of problem | Differentiation vs. prior art | Economic relevance | Risk |
|---|---|---|---|---|---|
| P1 stochastic correlation | high | high | medium (crowded field, exact kernel is the wedge) | high (multi-asset desks, correlation smile) | medium |
| P2 target zones / de-peg | **highest** | medium-high | **high** (derivative side sparse) | high and current (stablecoins, bands) | **low** |
| P3 exact simulation | high | medium | low (Beskos–Roberts) | medium | low payoff |
| P4 RND recovery | medium | medium | medium | medium | medium |
| P5 American | medium | high | low | high | high risk, low payoff |
| P6 Asian | low | high | medium | high | very high risk |
| P8 bounded vol | medium | medium | low-medium | medium | foldable into P1 |

**Shortlist: P1, P2.** P7 should be included as a theorem-section inside either.

**Recommendation: P2 — target zones / pegged-asset and de-peg derivative pricing**, on three grounds:

1. *Asset–problem match is exact.* The economic object (a band-limited underlying, hitting and occupation of band edges) is isomorphic to the mathematical object already built (a bounded phase diffusion with exact transition, hitting, and occupation laws via A1–A2). No new probability is needed to get first results; the work is economic modeling and pricing, which is where the open problems actually are.
2. *Lowest novelty risk.* P1 competes head-on with a large, active stochastic-correlation literature where the burden of proof is heavy. The derivative-pricing side of target zones and especially stablecoin de-peg risk is sparse and current.
3. *Verifiable milestones exist early* (closed-form survival/de-peg probabilities vs. Monte Carlo; band-option prices vs. PDE benchmarks), matching the project's verification standards.

P1 is the strong fallback and could follow P2, since the bounded-factor machinery is shared.

---

## 3. Immediate next steps after selection (for either P1 or P2)

1. Literature audit at the Phase-5 standard (original sources, no snippets) for the selected problem; record in a `PHASE_6_LITERATURE_REVIEW.md`.
2. Precise problem statement with the economic model, the SDE, the measure, and the exact claim to be proved.
3. Reproducible notebook plan under the project notebook standards (conda env `phase3-paper`, fixed seeds, MC cross-checks).
4. Milestone 1 deliverable: one exact closed-form result verified numerically, before any breadth expansion.
