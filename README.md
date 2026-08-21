[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Tests](https://img.shields.io/badge/tests-192%2F192-brightgreen)
![Phases](https://img.shields.io/badge/phases-13%20complete-blue)
![Reproducibility](https://img.shields.io/badge/seed-20260821-informational)

# Complex–Itô Random-Walk Research

A research program that starts from a rigorous bridge between complex polar
form, Brownian quadratic variation, Itô's lemma, and random walks — and
grows into an **exact-law framework for stochastic correlation**: a
bounded-factor construction $ho_t=X_t/\sqrt{X_t^2+c^2}$ in which every
object a derivatives desk needs is available in closed form or as a
deterministic quadrature.

## Headline results

| # | Result | Phase |
|---|--------|-------|
| 1 | Complex embedding of arithmetic Brownian motion with stochastic radius | 1–4 |
| 2 | One-phase Euler coordinates: exact classification & pricing conjugacy | 5 |
| 3 | Exact bounded correlation: transitions, barriers, corridors, clock law | 6 |
| 4 | Static inheritance + proportional-drift class; **forward-FK discovery** (backward equation fails off constant coefficients) | 7 |
| 5 | Exact 1-D characteristic function of spread/basket returns; COS pricing; **opposite-curvature implied-correlation smiles** | 8 |
| 6 | **Scale observational equivalence** theorem + closed-form exact MLE; empirical study on S&P pairs | 9 |
| 7 | **Phase-Gram**: Gaussian-driven triangular angles → correlation matrices with exact finite-time law | 10 |
| 8 | Lévy-powered drivers: marginals & clock survive via FK-PIDE; jump asymmetry flips the clock drift sign | 11 |
| 9 | Pegged assets: defended bands, credibility clocks, closed-form de-peg derivatives | 12 |

Everything is verified: **192/192 unit tests**, every notebook executed from
a clean kernel with fixed seed `20260821`, all claims web-audited against
the literature with per-phase novelty boundaries.

## Technical papers

Rendered manuscripts (Quarto, HTML + PDF under each `output/` directory):

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

Consolidated theory statement: [`PHASE_13_FLAGSHIP_MANUSCRIPT.md`](PHASE_13_FLAGSHIP_MANUSCRIPT.md).

## Repository layout

```
├── PHASE_{1..12}_*.md        # per-phase plans, literature reviews,
│                             #   simulation records, syntheses
├── PHASE_13_FLAGSHIP_MANUSCRIPT.md
├── phase{6..12}_*.py         # research modules (one per phase ≥ 6)
├── tests/                    # 192 unit tests across all modules
├── notebooks/                # builders + executed discovery notebooks
├── paper/                    # Quarto manuscripts (HTML + PDF outputs)
└── .agent/                   # session status, handoffs, reviews
```

## Getting started

```bash
conda activate phase3-paper     # Python 3.12, numpy/scipy/matplotlib
python -m unittest discover -s tests      # 192 tests
quarto render paper/phaseN                # any manuscript, N in {3,4,6..12}
```

---

This folder develops and numerically checks a rigorous bridge between complex
polar form, Brownian quadratic variation, Itô's lemma, and random walks.

## Phase 1 reading order

1. [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) — objectives and research phases.
2. [`01_ITO_ALGEBRA.md`](01_ITO_ALGEBRA.md) — why $(dW)^2=dt$.
3. [`02_ARITHMETIC_DIFFUSION.md`](02_ARITHMETIC_DIFFUSION.md) — the additive
   random-walk benchmark.
4. [`03_STOCHASTIC_EXPONENTIAL.md`](03_STOCHASTIC_EXPONENTIAL.md) — the
   algebraic exponential bridge.
5. [`04_STOCHASTIC_POLAR_FORM.md`](04_STOCHASTIC_POLAR_FORM.md) — pure
   stochastic rotation and the general amplitude–phase formula.
6. [`05_PLANAR_BROWNIAN_POLAR_COORDINATES.md`](05_PLANAR_BROWNIAN_POLAR_COORDINATES.md)
   — the polar SDEs of a two-dimensional random walk.
7. [`notebooks/ito_complex_bridge.ipynb`](notebooks/ito_complex_bridge.ipynb)
   — executed Monte Carlo and numerical checks.
8. [`SIMULATION_RESULTS.md`](SIMULATION_RESULTS.md) — reproducibility record
   and headline numerical results.
9. [`LITERATURE_REVIEW.md`](LITERATURE_REVIEW.md) — verified sources and
   research positioning.
10. [`FINAL_SYNTHESIS.md`](FINAL_SYNTHESIS.md) — the concise answer and formula
   classification.
11. [`.agent/reviews/TASK-001-opencode-glm52-review.md`](.agent/reviews/TASK-001-opencode-glm52-review.md)
    — independent GLM 5.2 mathematical review and provenance.

## Phase 2 reading order

Phase 2 replaces the fixed-radius circle model with a full planar diffusion:

1. [`PHASE_2_PLAN.md`](PHASE_2_PLAN.md) — approved scope and acceptance
   criteria.
2. [`06_COMPLEX_QUADRATIC_VARIATION.md`](06_COMPLEX_QUADRATIC_VARIATION.md)
   — why $[Z,Z]$ and $[Z,\overline Z]$ are different.
3. [`07_STOCHASTIC_RADIUS_AND_PLANAR_EXPONENTIAL.md`](07_STOCHASTIC_RADIUS_AND_PLANAR_EXPONENTIAL.md)
   — Bessel radius, winding angle, and the full stochastic polar exponential.
4. [`08_GENERAL_COMPLEX_DIFFUSIONS.md`](08_GENERAL_COMPLEX_DIFFUSIONS.md)
   — drift, general covariance, anisotropy, correlation, and noise rank.
5. [`09_DISCRETE_COMPLEX_RANDOM_WALK.md`](09_DISCRETE_COMPLEX_RANDOM_WALK.md)
   — exact finite-step multiplicative form and its Itô limit.
6. [`notebooks/phase2_stochastic_radius.ipynb`](notebooks/phase2_stochastic_radius.ipynb)
   — executed Phase 2 Monte Carlo and convergence checks.
7. [`PHASE_2_SIMULATION_RESULTS.md`](PHASE_2_SIMULATION_RESULTS.md) —
   reproducibility record and numerical results.
8. [`PHASE_2_LITERATURE_REVIEW.md`](PHASE_2_LITERATURE_REVIEW.md) — verified
   planar Brownian, winding, stochastic-logarithm, and numerical sources.
9. [`PHASE_2_SYNTHESIS.md`](PHASE_2_SYNTHESIS.md) — the full answer beyond
   Brownian motion on a circle.
10. [`.agent/reviews/TASK-002-opencode-glm52-review.md`](.agent/reviews/TASK-002-opencode-glm52-review.md)
    — independent GLM 5.2 mathematical review and provenance.

## Phase 3 reading order

Phase 3 answers the dimensional critique by returning to the original scalar
Brownian driver and constructing an injective complex representation with
stochastic radius:

1. [`complex_brownian_motion_critique.md`](complex_brownian_motion_critique.md)
   — the distinction between scalar and planar Brownian motion that motivates
   this phase.
2. [`PHASE_3_PLAN.md`](PHASE_3_PLAN.md) — approved scope and acceptance
   criteria.
3. [`10_SCALAR_POLAR_FORM_AND_ZERO_CROSSINGS.md`](10_SCALAR_POLAR_FORM_AND_ZERO_CROSSINGS.md)
   — the literal real-axis polar form, stopping at zero, and Tanaka local
   time.
4. [`11_ONE_DRIVER_LOGARITHMIC_SPIRAL.md`](11_ONE_DRIVER_LOGARITHMIC_SPIRAL.md)
   — the faithful one-driver exponential with stochastic radius and angle.
5. [`12_EMBEDDING_RANK_AND_MODEL_EQUIVALENCE.md`](12_EMBEDDING_RANK_AND_MODEL_EQUIVALENCE.md)
   — the general rank-one theorem and precise meanings of representation.
6. [`PHASE_3_LITERATURE_REVIEW.md`](PHASE_3_LITERATURE_REVIEW.md) — verified
   Itô, local-time, stochastic-logarithm, planar-comparison, and numerical
   sources.
7. [`notebooks/phase3_one_driver_complex_embedding.ipynb`](notebooks/phase3_one_driver_complex_embedding.ipynb)
   — executed pathwise, moment, rank, convergence, and local-time checks.
8. [`PHASE_3_SIMULATION_RESULTS.md`](PHASE_3_SIMULATION_RESULTS.md) —
   reproducibility record and numerical results.
9. [`PHASE_3_SYNTHESIS.md`](PHASE_3_SYNTHESIS.md) — final distinction between
   faithful one-driver representation and rank-two planar Brownian motion.
10. [`.agent/reviews/TASK-003-opencode-glm52-review.md`](.agent/reviews/TASK-003-opencode-glm52-review.md)
    — independent GLM 5.2 review after implementation.

## Phase 3 technical paper

The Phase 3 result is also available as a research-paper-style treatment with
an executed discovery notebook and reproducible PDF/HTML renders:

1. [`PHASE_3_TECHNICAL_PAPER_PLAN.md`](PHASE_3_TECHNICAL_PAPER_PLAN.md) —
   paper scope, section architecture, visualization plan, and acceptance
   criteria.
2. [`paper/phase3/index.qmd`](paper/phase3/index.qmd) — canonical Quarto
   manuscript.
3. [`paper/phase3/notebooks/phase3_discovery.ipynb`](paper/phase3/notebooks/phase3_discovery.ipynb)
   — executed computational narrative showing how the construction was found
   and tested.
4. [`paper/phase3/output/phase3-one-driver-complex-embedding.pdf`](paper/phase3/output/phase3-one-driver-complex-embedding.pdf)
   — final 23-page PDF.
5. [`paper/phase3/output/phase3-one-driver-complex-embedding.html`](paper/phase3/output/phase3-one-driver-complex-embedding.html)
   — browser-readable companion.
6. [`.agent/reviews/TASK-004-opencode-glm52-review.md`](.agent/reviews/TASK-004-opencode-glm52-review.md)
   — independent GLM 5.2 mathematical and numerical review.

## Phase 4 reading order

Phase 4 defines complex geometric Brownian motion natively, without first
constructing Cartesian coordinates or transforming a pre-existing state
process. Its modulus is exactly GBM and its imaginary exponent supplies
rotation:

1. [`PHASE_4_COORDINATE_FREE_COMPLEX_GBM_PLAN.md`](PHASE_4_COORDINATE_FREE_COMPLEX_GBM_PLAN.md)
   — approved scope, candidate constructions, and acceptance criteria.
2. [`PHASE_4_LITERATURE_REVIEW.md`](PHASE_4_LITERATURE_REVIEW.md) — source
   audit establishing complex GBM and complex stochastic exponentials as
   existing theory.
3. [`13_COORDINATE_FREE_COMPLEX_GBM.md`](13_COORDINATE_FREE_COMPLEX_GBM.md) —
   native definition, exact GBM modulus, phase, SDE, transitions, and moments.
4. [`14_COMPLEX_LOG_DRIVER_AND_STOCHASTIC_EXPONENTIAL.md`](14_COMPLEX_LOG_DRIVER_AND_STOCHASTIC_EXPONENTIAL.md)
   — ordinary exponential, Doléans exponential, stochastic logarithm, Itô
   correction, and complex brackets.
5. [`15_PHASE_4_EQUIVALENCE_RANK_AND_LIMITS.md`](15_PHASE_4_EQUIVALENCE_RANK_AND_LIMITS.md)
   — Phase 3 equivalence, fixed-spiral condition, rank-one obstruction, and
   two-driver boundary.
6. [`phase4_model.py`](phase4_model.py) and
   [`tests/test_phase4_model.py`](tests/test_phase4_model.py) — tested
   computational formulas.
7. [`notebooks/phase4_coordinate_free_complex_gbm.ipynb`](notebooks/phase4_coordinate_free_complex_gbm.ipynb)
   — executed exactness, rotation, covariance, moment, convergence, and
   quadratic-variation checks.
8. [`PHASE_4_SIMULATION_RESULTS.md`](PHASE_4_SIMULATION_RESULTS.md) —
   reproducibility record and numerical results.
9. [`PHASE_4_SYNTHESIS.md`](PHASE_4_SYNTHESIS.md) — concise final derivation
   and interpretation.
10. [`.agent/reviews/TASK-005-opencode-glm52-review.md`](.agent/reviews/TASK-005-opencode-glm52-review.md)
    — independent GLM 5.2 review after implementation.

## Phase 4 technical paper

The Phase 4 result is also developed as an independently renderable research
paper with a primary-source audit, executed discovery notebook, and
publication PDF/HTML:

1. [`docs/superpowers/specs/2026-07-24-phase4-technical-paper-design.md`](docs/superpowers/specs/2026-07-24-phase4-technical-paper-design.md)
   — approved paper design and contribution boundary.
2. [`docs/superpowers/plans/2026-07-24-phase4-technical-paper.md`](docs/superpowers/plans/2026-07-24-phase4-technical-paper.md)
   — implementation and verification plan.
3. [`paper/phase4/RESEARCH_NOTES.md`](paper/phase4/RESEARCH_NOTES.md) —
   primary-source, claim, and novelty audit.
4. [`paper/phase4/index.qmd`](paper/phase4/index.qmd) — canonical Quarto
   manuscript.
5. [`paper/phase4/notebooks/phase4_discovery.ipynb`](paper/phase4/notebooks/phase4_discovery.ipynb)
   — executed derivation, simulation, and visualization record.
6. [`paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf`](paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf)
   — letter-size technical paper.
7. [`paper/phase4/output/phase4-native-complex-geometric-brownian-motion.html`](paper/phase4/output/phase4-native-complex-geometric-brownian-motion.html)
   — browser-readable companion.
8. [`.agent/reviews/TASK-006-opencode-glm52-review.md`](.agent/reviews/TASK-006-opencode-glm52-review.md)
   — independent GLM 5.2 review after final verification.

## Phase 5 reading order

Phase 5 gives the exact answer to the requested one-stochastic-phase problem
for additive complex Brownian motion. It classifies when the phase can be a
time-independent, lossless state coordinate; derives its SDE, generator,
kernel, boundaries, and transported group law; and tests whether the
coordinate change creates new vector, complex-derivative, or numerical
capabilities:

1. [`PHASE_5_COMPREHENSIVE_ONE_PHASE_EULER_RESEARCH_PLAN.md`](PHASE_5_COMPREHENSIVE_ONE_PHASE_EULER_RESEARCH_PLAN.md)
   — approved comprehensive plan and acceptance gates.
2. [`PHASE_5_CANDIDATE_AUDIT.md`](PHASE_5_CANDIDATE_AUDIT.md) — detailed
   audit of the secant, Cayley, wrapped, spiral, arbitrary-curve, and
   moving-line candidates.
3. [`PHASE_5_LITERATURE_REVIEW.md`](PHASE_5_LITERATURE_REVIEW.md) —
   primary-source review and conservative novelty boundary.
4. [`PHASE_5_MATHEMATICAL_FOUNDATIONS.md`](PHASE_5_MATHEMATICAL_FOUNDATIONS.md)
   — measurable factorization, exact existence/impossibility theorem, phase
   dynamics, transition law, and natural boundaries.
5. [`PHASE_5_RIGIDITY_AND_GROUP_STRUCTURE.md`](PHASE_5_RIGIDITY_AND_GROUP_STRUCTURE.md)
   — additive rigidity, transported addition, Cayley compactification, and
   the compatible multiplicative logarithmic spiral.
6. [`PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md`](PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md)
   — what one phase preserves and why it does not create a second stochastic
   dimension or holomorphic derivative theory.
7. [`PHASE_5_NUMERICAL_IMPLICATIONS.md`](PHASE_5_NUMERICAL_IMPLICATIONS.md) —
   matched SDE, PDE, Monte Carlo, QMC, rare-event, and derivative benchmarks.
8. [`phase5_model.py`](phase5_model.py) and
   [`tests/test_phase5_model.py`](tests/test_phase5_model.py) — tested
   implementation of the exact maps and dynamics.
9. [`notebooks/phase5_one_phase_euler.ipynb`](notebooks/phase5_one_phase_euler.ipynb)
   — executed 19-section computational verification with 18 figures.
10. [`PHASE_5_SIMULATION_RESULTS.md`](PHASE_5_SIMULATION_RESULTS.md) —
    reproducibility record and measured results.
11. [`PHASE_5_SYNTHESIS.md`](PHASE_5_SYNTHESIS.md) — concise final theorem,
    formulas, implications, and limitations.
12. [`.agent/reviews/TASK-007-opencode-glm52-review.md`](.agent/reviews/TASK-007-opencode-glm52-review.md)
    — independent GLM 5.2 mathematical and evidence review.

## Main formula

If

$$
dA_t=a_tdt+u_t\cdot dW_t,\qquad
d\Theta_t=\omega_tdt+v_t\cdot dW_t,
\qquad
Z_t=e^{A_t+i\Theta_t},
$$

then

$$
\frac{dZ_t}{Z_t}
=\left[
a_t+\frac12(\|u_t\|^2-\|v_t\|^2)
+i(\omega_t+u_t\cdot v_t)
\right]dt
+(u_t+i v_t)\cdot dW_t.
$$

Pure stochastic rotation is the special case

$$
Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)},
$$

$$
dZ_t
=\left(i\omega-\frac12\beta^2\right)Z_tdt
+i\beta Z_tdW_t.
$$

For the native Phase 4 complex geometric Brownian motion, define

$$
\boxed{
\mathcal Z_t =
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
}
$$

Then its modulus is exactly the real GBM

$$
\frac{d|\mathcal Z_t|}{|\mathcal Z_t|} =
\mu\,dt+\sigma\,dW_t,
$$

its continuous phase is

$$
\Theta_t=\Theta_0+\omega t+\beta W_t,
$$

and its native complex Itô SDE is

$$
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t} =
\left[
\mu-\frac12\beta^2+i(\omega+\sigma\beta)
\right]dt
+(\sigma+i\beta)dW_t.
}
$$

This is a one-driver, rank-one complex GBM. Independent radial and angular
noise requires a second Brownian motion.

For a faithful one-driver representation with stochastic radius, let

$$
X_t=X_0+\mu t+\sigma W_t,
\qquad
c=\alpha+i\beta,
\qquad
\alpha\ne0.
$$

Then

$$
\boxed{
Z_t=Z_0e^{c(X_t-X_0)},}
$$

$$
\boxed{
\frac{dZ_t}{Z_t} =
\left(c\mu+\frac12c^2\sigma^2\right)dt
+c\sigma dW_t.}
$$

Its radius recovers the original scalar state:

$$
X_t=X_0+\frac1\alpha\log\frac{|Z_t|}{|Z_0|}.
$$

This is a rank-one logarithmic-spiral diffusion, not planar Brownian motion.

For the Phase 5 additive process

$$
Z_t=Z_0+a t+bW_t,\qquad Z_0b\ne0,
$$

a genuine, lossless, time-independent one-phase representation exists if and
only if

$$
\frac ab\in\mathbb R,
\qquad
\frac b{Z_0}\notin\mathbb R.
$$

Writing $a=\lambda b$, $b/Z_0=\rho e^{i\phi}$, and
$x_t=\lambda t+W_t$, define

$$
\theta_t=\arg(1+\rho e^{i\phi}x_t)\in I_\phi.
$$

Then the exact Euler form is

$$
\boxed{
Z_t =
Z_0
\frac{\sin\phi}{\sin(\phi-\theta_t)}
e^{i\theta_t}.
}
$$

The phase is the only stochastic state variable in this formula; its radial
factor is a deterministic function of that phase. It is a bounded chart on
the original affine support line, not Brownian motion on a circle and not a
new stochastic dimension.

For full isotropic planar Brownian motion,

$$
dZ_t=\sigma(dW_t^1+i\,dW_t^2),
$$

the stochastic radius and angle satisfy

$$
dR_t=\frac{\sigma^2}{2R_t}dt+\sigma dB_t^R,
\qquad
d\Theta_t=\frac{\sigma}{R_t}dB_t^\Theta,
$$

and the complete nonconstant-radius exponential representation is

$$
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{\sigma}{R_s}dB_s^R
+i\int_0^t\frac{\sigma}{R_s}dB_s^\Theta
\right].
$$

---

## Phases 7–13 (completed 2026-08-21)

Extension of the exact bounded-factor framework per
`PHASE_7_13_PROGRAM_PLAN.md`. Full suite: **192/192 tests**; every notebook
executed from a clean kernel with seed `20260821`.

| Phase | Deliverable | Headline result |
|---|---|---|
| 7 | `phase7_term_structure.py` | Static inheritance + proportional-drift barrier class; **forward-FK discovery** (backward equation fails off constant coefficients — counterexample in-module); exact quantile term structure \(q_\alpha(t)\); bootstrap of \((c,\lambda^{\mathbb Q})\) |
| 8 | `phase8_cos.py` | Exact 1-D characteristic function of spread/basket returns via real-potential resolvent \(L_A\); COS pricing vs MC ≤4 SE; **opposite-curvature implied-correlation smiles** |
| 9 | `phase9_estimation.py` | **Scale observational equivalence theorem**; closed-form ratio MLE; empirical study on 4 S&P pairs (local store); attenuation ~4× at 60-day windows |
| 10 | `phase10_matrix.py` | Phase-Gram: Gaussian-driven triangular angles → correlation-matrix processes with exact finite-time law, PSD by construction, GH pricing |
| 11 | `phase11_levy.py` | VG/NIG drivers: marginals stay exact, clock survives via FK-PIDE; jump asymmetry flips clock drift sign |
| 12 | `phase12_peg.py` | Pegged assets: defended bands + bounded-factor de-peg clock; closed-form de-peg digitals, pay-at-hit Laplace, shortfall swaps |
| 13 | `PHASE_13_FLAGSHIP_MANUSCRIPT.md` | Consolidated manuscript: five headline claims, master verification table |

Key documents: `PHASE_7_13_PROGRAM_PLAN.md` (approved plan),
`PHASE_{7..13}_LITERATURE_REVIEW.md` (web-audited novelty boundaries),
`PHASE_{7..13}_SIMULATION_RESULTS.md`, `PHASE_{7..13}_SYNTHESIS.md`,
flagship `PHASE_13_FLAGSHIP_MANUSCRIPT.md`.
