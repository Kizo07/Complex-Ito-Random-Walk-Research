[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Tests](https://img.shields.io/badge/tests-192%2F192-brightgreen)
![Phases](https://img.shields.io/badge/phases-13%20complete-blue)
![Reproducibility](https://img.shields.io/badge/seed-20260821-informational)

# Complex–Itô Random-Walk Research

A research program in two acts. **Act I (Phases 1–5)** builds a rigorous
bridge between complex polar form, Brownian quadratic variation, Itô's
lemma, and random walks. **Act II (Phases 6–13)** applies that machinery to
finance: an *exact-law framework for stochastic correlation* in which a
bounded coordinate $\rho_t=X_t/\sqrt{X_t^2+c^2}$ makes every object a
derivatives desk needs — transition densities, barrier laws, occupation
clocks, vanilla and multi-asset prices, estimators, matrix-valued
extensions, jump drivers, and de-peg derivatives — available in closed form
or as deterministic quadrature.

Every claim is verified: **192/192 unit tests**, every notebook executed
from a clean kernel with fixed seed `20260821`, all novelty claims audited
against the literature with per-phase boundary statements.

## Headline results

| # | Result | Phase |
|---|--------|-------|
| 1 | Quadratic variation, not $i^2=-1$, drives the Itô correction term | 1 |
| 2 | Planar Brownian motion has Bessel radius and independent winding angle | 2 |
| 3 | Logarithmic-spiral embedding: one driver, stochastic radius, lossless recovery of the scalar state | 3 |
| 4 | Geometric Brownian motion is natively complex: modulus = GBM, phase = drifted Brownian motion | 4 |
| 5 | One-phase Euler coordinates: classification of exact nonradial representations and their pricing conjugacy | 5 |
| 6 | Exact bounded correlation: transitions, first passage, corridors, DDS clock law | 6 |
| 7 | Static inheritance + proportional-drift class; forward-FK discovery | 7 |
| 8 | Exact spread/basket characteristic function; opposite-curvature implied-correlation smiles | 8 |
| 9 | Scale observational equivalence + closed-form exact MLE | 9 |
| 10 | Phase-Gram: correlation matrices with exact finite-time law | 10 |
| 11 | Lévy drivers: clock survives via FK-PIDE; asymmetry flips its drift sign | 11 |
| 12 | De-peg derivatives priced in closed form on defended bands | 12 |

---

## Phase 1 — The complex exponential bridge

**Question.** Is the analogy $(dW)^2=dt \leftrightarrow i^2=-1$ rigorous?

**Findings.**
- For $Z_t=r_0e^{iX_t}$ with arithmetic diffusion $X_t=\mu t+\sigma W_t$,
  Itô's lemma gives $dZ_t=(i\mu-\tfrac{\sigma^2}{2})Z_t\,dt+i\sigma Z_t\,dW_t$:
  quadratic variation produces exactly the drift needed to keep the radius constant.
- The rule is not that $(dW)^2$ *acts like* $i^2=-1$; the Itô square of the
  stochastic increment satisfies $(i\sigma Z\,dW)^2=-\sigma^2Z^2\,dt$.

**Documents.** [`FINAL_SYNTHESIS.md`](FINAL_SYNTHESIS.md) ·
[`SIMULATION_RESULTS.md`](SIMULATION_RESULTS.md) ·
[`LITERATURE_REVIEW.md`](LITERATURE_REVIEW.md)

## Phase 2 — Planar Brownian motion beyond the circle

**Question.** Can the radius itself be stochastic?

**Findings.**
- Planar Brownian motion $Z_t=Z_0+\sigma(W^1+iW^2)$ decomposes into a
  Bessel-type radius $dR_t=\frac{\sigma^2}{2R_t}dt+\sigma\,dB^R_t$ and an
  independently driven unwrapped winding angle.
- Exact finite-step multiplicative form for discrete complex random walks,
  with the Itô limit established.

**Documents.** [`PHASE_2_SYNTHESIS.md`](PHASE_2_SYNTHESIS.md) ·
[`PHASE_2_SIMULATION_RESULTS.md`](PHASE_2_SIMULATION_RESULTS.md)

## Phase 3 — A faithful one-driver embedding

**Question.** Planar Brownian motion uses two drivers; can the radius be
stochastic while keeping the original single Brownian driver?

**Findings.**
- The logarithmic spiral $Z_t=Z_0e^{c(X_t-X_0)}$ ($c=\alpha+i\beta$,
  $\alpha\beta\ne0$) makes both radius and angle stochastic, both driven by
  the same $W_t$: $\log(R_t/R_0)=\alpha(X_t-X_0)$,
  $\Theta_t-\Theta_0=\beta(X_t-X_0)$.
- The representation is injective — the scalar state is recovered losslessly
  as $X_t=X_0+\alpha^{-1}\log(R_t/R_0)$.

**Documents.** [`PHASE_3_SYNTHESIS.md`](PHASE_3_SYNTHESIS.md) ·
[paper/phase3](paper/phase3/index.qmd)

## Phase 4 — Native complex geometric Brownian motion

**Question.** Is GBM itself natively complex without mapping an external
state variable?

**Findings.**
- Yes: one complex Euler-form exponential represents GBM directly — modulus
  $R_t=|\mathcal Z_0|\exp[(\mu-\tfrac{\sigma^2}2)t+\sigma W_t]$ (GBM), phase
  $\Theta_t=\Theta_0+\omega t+\beta W_t$ (drifted Brownian).
- Coordinate-free formulation for general complex diffusions: drift,
  covariance, anisotropy, and noise rank classified.

**Documents.** [`PHASE_4_SYNTHESIS.md`](PHASE_4_SYNTHESIS.md) ·
[paper/phase4](paper/phase4/index.qmd)

## Phase 5 — One-phase Euler coordinates

**Question.** Which affine complex processes admit an exact representation
containing only the stochastic phase?

**Findings.**
- Complete classification: for $Z_t=Z_0+at+bW_t$, the Euler lift
  $\mathcal Z_t=Z_0[1+i(X_t-X_0)/c]=Z_0\sec(\theta_t)e^{i\theta_t}$ stores
  the full state in the phase alone; the radius $r(\theta)=\sec\theta$ is a
  deterministic function of it.
- Constant radius requires changing the represented state (e.g., Cayley
  transform); the phase combines the state but removes neither time nor
  randomness from the law.
- Rigidity/group-structure results and pricing conjugacy; numerical
  consequences for discretization.

**Documents.** [`PHASE_5_SYNTHESIS.md`](PHASE_5_SYNTHESIS.md) ·
[paper/one-phase-euler](paper/one-phase-euler/index.qmd)

## Phase 6 — Exact bounded correlation

**Question.** Can stochastic correlation be made exactly solvable?
$\rho_t=X_t/\sqrt{X_t^2+c^2}$ with Gaussian $X$.

**Findings.**
- Closed-form transition density; reflection-principle first-passage laws;
  scale-function band exits; corridor occupation laws with explicit atom
  separation (arcsine anchor).
- DDS theorem: any asset spread/basket has variance clock
  $v=\beta T+\alpha A_T$ with $A_T=\int\rho$; the full clock law computed by
  FK resolvent + Fourier series.
- Sign corollary: deteriorating credibility raises spread-barrier prices and
  lowers basket-barrier prices.
- OU driver: stationary density exact; stationarity–tractability
  classification proven.

**Documents.** Milestones
[`1–6`](PHASE_6_MILESTONE_1_FIRST_PASSAGE.md) ·
[paper/phase6](paper/phase6/index.qmd)

## Phase 7 — Time-inhomogeneous exactness

**Question.** Which laws survive deterministic coefficient curves
$dX=\mu(t)dt+\sigma(t)dW$?

**Findings.**
- Static inheritance: all finite-marginal/transition laws are the constant-
  coefficient formulas under $m(t)=x_0+\int\mu$, $v(t)=\int\sigma^2$ —
  including the exact quantile term structure $q_\alpha(t)$.
- Proportional-drift class $\mu(t)=\lambda\sigma^2(t)$: every reflection law
  survives with $t\to v(T)$ and depends on $\sigma(\cdot)$ only through
  integrated variance.
- **Forward-FK discovery**: the backward Feynman–Kac equation fails off
  constant coefficients (drift-only counterexample); the forward
  Fokker–Planck-with-potential equation is implemented as the shared engine.
- Bootstrap of $(c,\lambda^{\mathbb Q})$ from correlation-digital quotes to
  $10^{-8}$ accuracy.

**Documents.** [`PHASE_7_SYNTHESIS.md`](PHASE_7_SYNTHESIS.md) ·
[`phase7_term_structure.py`](phase7_term_structure.py) ·
[paper/phase7](paper/phase7/index.qmd)

## Phase 8 — Fourier pricing under stochastic correlation

**Question.** Can European spread/basket options be priced deterministically?

**Findings.**
- Exact one-dimensional characteristic function
  $\phi_Z(u)=e^{-rT}e^{iuz_0-u^2\beta T/2}\,L_A(\alpha u^2/2)$ where
  $L_A(s)=E[e^{-sA_T}]$ exists for all real $s$ (bounded factor).
- Deterministic pricing via COS inversion or clock-density quadrature;
  Monte Carlo agreement within ~1 SE across strikes; semi-analytic Greeks.
- Implied-correlation smiles are symmetric with **opposite curvature**
  (spreads −2.4e-3, baskets +1.8e-3); ATM level equals $E[A_T]$.

**Documents.** [`PHASE_8_SYNTHESIS.md`](PHASE_8_SYNTHESIS.md) ·
[`phase8_cos.py`](phase8_cos.py) · [paper/phase8](paper/phase8/index.qmd)

## Phase 9 — Estimation and identifiability

**Question.** What can actually be estimated?

**Findings.**
- Scale observational equivalence: $(c,\mu,\sigma)\sim(\lambda c,
  \mu/\lambda,\sigma/\lambda)$ are indistinguishable from observations
  *and* derivative prices; identified space is $\{(\mu/c,\sigma/c)\}$.
- Closed-form exact MLE (OLS in the normalized coordinate); Fisher-space
  competitors with consistent Jacobians.
- PIT–state-correlation diagnostic catches dynamic misspecification that
  marginal KS misses ($z=8$ vs $p=0.53$).
- Window-smoothed proxies attenuate measured dynamics ~4× at 60 days.
  Empirics: four S&P pairs, vol ratios 0.84–1.55, drift ratios ≈ 0.

**Documents.** [`PHASE_9_SYNTHESIS.md`](PHASE_9_SYNTHESIS.md) ·
[`phase9_estimation.py`](phase9_estimation.py) ·
[paper/phase9](paper/phase9/index.qmd)

## Phase 10 — Correlation matrices: Phase-Gram

**Question.** Do exact laws extend from pairs to whole correlation matrices?

**Findings.**
- Driving canonical triangular angles with independent Brownian motions
  gives PSD/unit-diagonal processes **by construction**.
- Exact finite-time law: every European functional is a
  $d=n(n-1)/2$-dimensional Gauss–Hermite integral; pairwise marginals closed
  form.
- Analytic entry drifts with endogenous curvature mean-reversion, verified
  against MC to third decimals.

**Documents.** [`PHASE_10_SYNTHESIS.md`](PHASE_10_SYNTHESIS.md) ·
[`phase10_matrix.py`](phase10_matrix.py) ·
[paper/phase10](paper/phase10/index.qmd)

## Phase 11 — Lévy-powered drivers

**Question.** Does exactness survive jump-driven correlation?

**Findings.**
- Marginals stay exact (Gil–Pelaez pushforward); the clock transform
  survives via backward FK-PIDE; reflection-principle barrier laws die.
- Variance-matched VG halves $E[A_T]$ (0.073 → 0.035); NIG with $\beta<0$
  flips its sign — invisible to marginal-only analysis.
- Solver verified against integrated-exponent closed forms and the tiny-jump
  Gaussian limit.

**Documents.** [`PHASE_11_SYNTHESIS.md`](PHASE_11_SYNTHESIS.md) ·
[`phase11_levy.py`](phase11_levy.py) · [paper/phase11](paper/phase11/index.qmd)

## Phase 12 — Pegged-asset economics

**Question.** Can de-peg risk be priced in closed form?

**Findings.**
- Defended band (reflected BM, exponential-trapezoid stationary law) +
  bounded-factor credibility clock: de-peg CDF/density/perpetual mass all
  closed form.
- Pay-at-hit transform $E[e^{-r\tau}]=\exp((\lambda-\sqrt{\lambda^2+2r/
  \sigma_z^2})\Delta)$, verified to $10^{-6}$.
- Shortfall swaps price as a single quadrature over the exact IG density;
  de-peg probabilities are perpetual-capped and strongly concave in horizon.

**Documents.** [`PHASE_12_SYNTHESIS.md`](PHASE_12_SYNTHESIS.md) ·
[`phase12_peg.py`](phase12_peg.py) · [paper/phase12](paper/phase12/index.qmd)

## Phase 13 — Consolidation

Flagship manuscript assembling the theory, the five headline claims, master
verification tables, and limitations register.

**Documents.**
[`PHASE_13_FLAGSHIP_MANUSCRIPT.md`](PHASE_13_FLAGSHIP_MANUSCRIPT.md)

---

## Technical papers

Quarto manuscripts, rendered HTML + PDF under each `output/` directory:

| Paper | Source |
|-------|--------|
| A Faithful One-Driver Complex Embedding of Arithmetic Brownian Motion | [`paper/phase3`](paper/phase3/index.qmd) |
| Native Complex Geometric Brownian Motion | [`paper/phase4`](paper/phase4/index.qmd) |
| One-Phase Euler Coordinates for Affine Brownian Factors | [`paper/one-phase-euler`](paper/one-phase-euler/index.qmd) |
| Exact Bounded Correlation | [`paper/phase6`](paper/phase6/index.qmd) |
| Exact Term Structure of Stochastic Correlation | [`paper/phase7`](paper/phase7/index.qmd) |
| Fourier Pricing of Spread and Basket Options under Stochastic Correlation | [`paper/phase8`](paper/phase8/index.qmd) |
| What Can Be Estimated? Scale Observational Equivalence and Exact MLE | [`paper/phase9`](paper/phase9/index.qmd) |
| Phase-Gram: Correlation Matrices with Exact Finite-Time Law | [`paper/phase10`](paper/phase10/index.qmd) |
| Lévy-Powered Bounded Factors | [`paper/phase11`](paper/phase11/index.qmd) |
| The Economics of De-Peg | [`paper/phase12`](paper/phase12/index.qmd) |

## Verification and reproducibility

```bash
conda activate phase3-paper            # Python 3.12, numpy/scipy/matplotlib
python -m unittest discover -s tests   # 192 tests
quarto render paper/phaseN             # any manuscript, N in {3,4,6..12}
```

- Full suite green on 2026-08-21 (182 s).
- Notebooks executed from clean kernels, seed `20260821`; Monte Carlo
  standard errors reported wherever simulation appears.
- Numerical convergence checked across at least two grid/time-step sizes.

## Repository layout

```
├── PHASE_{1..13}_*.md        # plans, literature reviews, simulation
│                             #   records, syntheses per phase
├── PHASE_13_FLAGSHIP_MANUSCRIPT.md
├── phase{6..12}_*.py         # research modules (one per phase ≥ 6)
├── tests/                    # unit suites for every module
├── notebooks/                # builders + executed discovery notebooks
├── paper/                    # Quarto manuscripts (HTML + PDF outputs)
└── .agent/                   # session status, handoffs, reviews
```

## License

Released under the [MIT License](LICENSE).
