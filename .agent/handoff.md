# Handoff

## Active work

`TASK-005` is complete under the user's Codex-direct exception. No
implementation was delegated. The Phase 4 branch is preserved locally;
commit, push, pull request, merge, release, and publication were not authorized
for this task.

## TASK-005 outcome

Phase 4 now defines a native complex geometric Brownian motion directly from
one real Brownian motion:

\[
\mathcal Z_t=\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
\]

Its modulus is exactly GBM, its phase contains deterministic and stochastic
rotation, and its exact transition combines the time and Brownian increments
inside one complex exponential. The derivations also reconcile the ordinary
and Doléans exponentials, recover Phase 3 as a constrained subfamily, and make
the one-driver rank-one limitation explicit.

Primary deliverables:

- `13_COORDINATE_FREE_COMPLEX_GBM.md`;
- `14_COMPLEX_LOG_DRIVER_AND_STOCHASTIC_EXPONENTIAL.md`;
- `15_PHASE_4_EQUIVALENCE_RANK_AND_LIMITS.md`;
- `phase4_model.py` and `tests/test_phase4_model.py`;
- `notebooks/build_phase4_coordinate_free_complex_gbm.py`;
- `notebooks/phase4_coordinate_free_complex_gbm.ipynb`;
- `PHASE_4_SIMULATION_RESULTS.md`;
- `PHASE_4_SYNTHESIS.md`;
- `.agent/reviews/TASK-005-opencode-glm52-review.md`.

## TASK-005 verification

The final notebook executed twice from clean kernels: once in place and once
to `/tmp/phase4_coordinate_free_complex_gbm_recheck.ipynb`. Both runs had 12
sequentially numbered code cells, zero error outputs, and matching
code-source and deterministic text-output hashes. All notebook assertions
passed. Ten unit tests pass in the unmodified `phase3-paper` conda
environment.

Pandoc 3.8 rendered the Phase 4 plan, literature review, three derivation
chapters, simulation record, and synthesis to temporary HTML without fatal
errors. The Python sources compile, project JSON parses, and
`git diff --check` passes.

## TASK-005 independent review

OpenCode with `zai-coding-plan/glm-5.2` returned **PASS**, with no critical or
major findings. It independently re-derived the exponential construction,
modulus and phase, full complex Itô drift, moment formulas, both complex
brackets, covariance-rank result, Phase 3 mapping, and two-driver comparator.
It also reran the ten tests and independently reproduced the numerical
benchmarks.

The review's three minor evidence notes were closed by recording the second
clean notebook run, Pandoc render, and test-first red/green history. Its
editorial consistency note was closed by explaining that the constant-radius
counterexample retains \(i\omega\) solely to isolate the omitted Itô drift.

Review usage ID: `c18c03a7-4f5a-4a1b-96c7-c767987d7bc4`. Scorecard evaluation
ID: `98e03e34-ccf7-42cf-bf44-745aad55f866`.

## TASK-005 remaining risks

The model is deliberately one-driver and therefore has rank-one instantaneous
log-polar covariance; independently randomized radial and angular noise
requires a second Brownian motion. Monte Carlo values remain seed- and
sample-size-dependent within their reported standard errors. The relation
\(d[W,W]_t=dt\) is a quadratic-variation statement, not the algebraic identity
\(i^2=-1\).

## TASK-004 outcome

The completed Phase 3 mathematics is now presented as a self-contained
technical paper, an executed computational-discovery notebook, 18
publication-quality vector figures with PNG companions, generated numerical
tables, and reproducible PDF/HTML outputs.

The canonical sources and outputs are:

- `PHASE_3_TECHNICAL_PAPER_PLAN.md`;
- `paper/index.qmd`;
- `paper/notebooks/build_phase3_discovery.py`;
- `paper/notebooks/phase3_discovery.ipynb`;
- `paper/figures/`;
- `paper/tables/`;
- `paper/output/phase3-one-driver-complex-embedding.pdf`;
- `paper/output/phase3-one-driver-complex-embedding.html`;
- `.agent/reviews/TASK-004-opencode-glm52-review.md`.

## TASK-004 verification

The notebook executed twice from clean kernels through the approved external
boundary necessitated by the workspace's Jupyter socket restriction. All 15
code-cell sources, outputs, and execution counts matched exactly; counts were
sequential from 1 through 15, and there were zero error outputs.

Quarto rendered the project successfully with Quarto 1.9.38, TinyTeX 2026,
and the `phase3-paper` Python 3.12.13 environment. The final PDF has 23
letter-size pages with all fonts embedded. It uses vector PDF figures; the
HTML uses all 18 PNG companions and has no missing figure alt text. Extracted
PDF text and HTML contain no unresolved cross-reference markers. The final
affected PDF pages were inspected visually after the editorial corrections.

## TASK-004 independent review

opencode with `zai-coding-plan/glm-5.2` returned **PASS**, with no critical or
major findings. It independently re-derived the central Itô SDE, inverse map,
moments, complex brackets, covariance-rank theorem, exact step, and
Tanaka/local-time formulas, and independently recomputed the reported
numerical targets.

All four editorial notes were resolved: missing plus signs in notebook
markdown were corrected and regenerated; the obsolete draft QMD was removed;
the planar control radius and log-polar basis were stated explicitly; and the
stochastic logarithm was named in the manuscript.

Review usage ID: `0afa46c6-6b46-4dd2-a026-7b43209ae569`. Scorecard evaluation
ID: `c2c88e0f-1bcd-4ed3-a4d1-e2b0bbd72663`.

# TASK-003 historical record

## Outcome

Success. Codex completed the user-authorized direct implementation of
`TASK-003`; no implementation work was delegated. Phase 3 now gives an exact
one-driver complex representation of the original scalar arithmetic Brownian
motion in which radius and angle are both stochastic, while preserving the
distinct two-driver planar theory from Phase 2.

## Deliverables

- `10_SCALAR_POLAR_FORM_AND_ZERO_CROSSINGS.md`;
- `11_ONE_DRIVER_LOGARITHMIC_SPIRAL.md`;
- `12_EMBEDDING_RANK_AND_MODEL_EQUIVALENCE.md`;
- `PHASE_3_LITERATURE_REVIEW.md`;
- `notebooks/build_phase3_notebook.py`;
- `notebooks/phase3_one_driver_complex_embedding.ipynb`;
- `PHASE_3_SIMULATION_RESULTS.md`;
- `PHASE_3_SYNTHESIS.md`;
- `.agent/reviews/TASK-003-opencode-glm52-review.md`.

The authoritative index is `README.md`.

## Verification

The notebook executed successfully in the conda `base` environment, in place,
and again from a clean kernel to
`/tmp/phase3_one_driver_complex_embedding_recheck.ipynb`. There were no cell
errors, all embedded assertions passed, and all seven text-output streams were
identical between the two executions. Notebook JSON is valid, execution
counts are sequential from 1 through 7, and the Python builder compiles.
Authoritative Markdown files render with Pandoc.

The exact-product, inverse-radius, and spiral-constraint pathwise errors were
at most \(6.273\times10^{-15}\). Radial and complex moment estimates agreed
with their exact Gaussian formulas within \(0.6\) Monte Carlo standard errors.
The Euler–Maruyama strong-error fit had slope \(0.5029\). The discrete Tanaka
identity closed to \(3.02\times10^{-14}\), while the occupation-density
approximation showed the expected slower convergence.

## Mathematical checks

- With \(c=\alpha+i\beta\),
  \[
  Z_t=Z_0e^{c(X_t-X_0)},\qquad
  \frac{dZ_t}{Z_t}
  =\left(c\mu+\frac12c^2\sigma^2\right)dt+c\sigma\,dW_t.
  \]
- For \(\alpha\ne0\), radius gives the pointwise inverse
  \[
  X_t=X_0+\frac1\alpha\log\frac{|Z_t|}{|Z_0|},
  \]
  so the embedding is information- and filtration-preserving.
- The polar covariance is
  \[
  \sigma^2
  \begin{pmatrix}
  \alpha^2&\alpha\beta\\
  \alpha\beta&\beta^2
  \end{pmatrix},
  \]
  an outer product of rank one.
- More generally, every deterministic \(C^2\) map
  \(F:\mathbb R\to\mathbb C\) and every complex Itô process driven by one
  scalar Brownian motion have instantaneous Cartesian covariance rank at
  most one.
- The exact discrete walk is
  \(Z_{n+1}=Z_n\exp(c\,\Delta X_n)\).
- Both complex brackets are explicit:
  \(d[Z,Z]_t=c^2\sigma^2Z_t^2dt\) and
  \(d[Z,\overline Z]_t=|c|^2\sigma^2|Z_t|^2dt\).
- The literal real-axis polar representation uses localized
  \(\log|X_t|\) before the first zero and Tanaka's formula plus symmetric
  local time globally.
- Phase 2 planar Brownian motion remains a distinct rank-two, two-driver
  model; Phase 3 does not relabel it as the original scalar process.

## Independent review

opencode with `zai-coding-plan/glm-5.2` returned **PASS**, with no critical,
major, or minor mathematical or numerical errors. It independently re-derived
the Itô equations, stochastic logarithm, moments, complex quadratic
variations, covariance-rank theorem, and Tanaka/occupation-density formulas,
then independently recomputed every exact numerical benchmark. Review usage
ID: `676ca875-893f-40a7-af9e-4afd763c516e`. Scorecard evaluation ID:
`1ac43d08-8859-45a4-b620-32aaf2d9a91e`.

## Remaining risks

Monte Carlo values fluctuate if seeds or sample counts are changed, as
expected. The rank-one covariance experiment constructs both polar increments
from the same scalar increment, so its zero eigenvalue checks the implemented
formula rather than serving as an independent proof of the rank theorem; the
proof is analytic. The occupation-density estimator converges slowly, while
the discrete Tanaka identity is exact on its grid. The analogy between
\(i^2=-1\) and \(d[W,W]_t=dt\) remains a mnemonic: the former is algebraic,
whereas the latter is a quadratic-variation limit.
