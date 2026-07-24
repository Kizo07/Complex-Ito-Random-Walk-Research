# Complex–Itô Random-Walk Research

This folder develops and numerically checks a rigorous bridge between complex
polar form, Brownian quadratic variation, Itô's lemma, and random walks.

## Phase 1 reading order

1. [`RESEARCH_PLAN.md`](RESEARCH_PLAN.md) — objectives and research phases.
2. [`01_ITO_ALGEBRA.md`](01_ITO_ALGEBRA.md) — why \((dW)^2=dt\).
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
   — why \([Z,Z]\) and \([Z,\overline Z]\) are different.
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
2. [`paper/index.qmd`](paper/index.qmd) — canonical Quarto manuscript.
3. [`paper/notebooks/phase3_discovery.ipynb`](paper/notebooks/phase3_discovery.ipynb)
   — executed computational narrative showing how the construction was found
   and tested.
4. [`paper/output/phase3-one-driver-complex-embedding.pdf`](paper/output/phase3-one-driver-complex-embedding.pdf)
   — final 23-page PDF.
5. [`paper/output/phase3-one-driver-complex-embedding.html`](paper/output/phase3-one-driver-complex-embedding.html)
   — browser-readable companion.
6. [`.agent/reviews/TASK-004-opencode-glm52-review.md`](.agent/reviews/TASK-004-opencode-glm52-review.md)
   — independent GLM 5.2 mathematical and numerical review.

## Main formula

If

\[
dA_t=a_tdt+u_t\cdot dW_t,\qquad
d\Theta_t=\omega_tdt+v_t\cdot dW_t,
\qquad
Z_t=e^{A_t+i\Theta_t},
\]

then

\[
\frac{dZ_t}{Z_t}
=\left[
a_t+\frac12(\|u_t\|^2-\|v_t\|^2)
+i(\omega_t+u_t\cdot v_t)
\right]dt
+(u_t+i v_t)\cdot dW_t.
\]

Pure stochastic rotation is the special case

\[
Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)},
\]

\[
dZ_t
=\left(i\omega-\frac12\beta^2\right)Z_tdt
+i\beta Z_tdW_t.
\]

For a faithful one-driver representation with stochastic radius, let

\[
X_t=X_0+\mu t+\sigma W_t,
\qquad
c=\alpha+i\beta,
\qquad
\alpha\ne0.
\]

Then

\[
\boxed{
Z_t=Z_0e^{c(X_t-X_0)},}
\]

\[
\boxed{
\frac{dZ_t}{Z_t}
=
\left(c\mu+\frac12c^2\sigma^2\right)dt
+c\sigma dW_t.}
\]

Its radius recovers the original scalar state:

\[
X_t=X_0+\frac1\alpha\log\frac{|Z_t|}{|Z_0|}.
\]

This is a rank-one logarithmic-spiral diffusion, not planar Brownian motion.

For full isotropic planar Brownian motion,

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2),
\]

the stochastic radius and angle satisfy

\[
dR_t=\frac{\sigma^2}{2R_t}dt+\sigma dB_t^R,
\qquad
d\Theta_t=\frac{\sigma}{R_t}dB_t^\Theta,
\]

and the complete nonconstant-radius exponential representation is

\[
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{\sigma}{R_s}dB_s^R
+i\int_0^t\frac{\sigma}{R_s}dB_s^\Theta
\right].
\]
