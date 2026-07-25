# Phase 4 Technical Paper Design

**Date:** 2026-07-24
**Status:** Approved
**Owner:** Codex under the standing user-authorized direct implementation
exception
**Reviewer:** OpenCode `zai-coding-plan/glm-5.2`, review and second opinion only

## 1. Objective

Create a self-contained technical paper for Phase 4 that defines and analyzes
the native complex exponential process

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right),
\]

proves that its modulus is exactly geometric Brownian motion, explains the
deterministic and stochastic rotation in its phase, derives the full complex
Itô SDE, and documents the one-driver rank-one limitation. The paper must
combine rigorous derivations, primary-source positioning, reproducible
computation, and publication-quality visual explanation.

## 2. Contribution and novelty boundary

Complex geometric Brownian motion and scalar complex linear stochastic
differential equations already appear in the numerical SDE literature. The
paper must not claim to invent complex GBM or the complex stochastic
exponential.

The paper's contribution is the following synthesis:

1. a modulus-preserving four-real-parameter representation in which
   \((\mu,\sigma)\) retain their exact real-GBM meanings and
   \((\omega,\beta)\) separately control deterministic and stochastic phase;
2. a direct definition from one real Brownian motion and a nonzero complex
   initial value, with no defining Cartesian coordinate processes and no
   transformed pre-existing state path;
3. a reconciliation of the ordinary complex exponential, the exact
   multiplicative transition, the complex Itô SDE, the stochastic logarithm,
   and the Doléans exponential;
4. an explicit log-polar covariance-rank analysis and a comparison with the
   independent two-driver boundary;
5. a precise recovery of the Phase 3 logarithmic spiral as a constrained
   parameter subfamily; and
6. a fully reproducible computational demonstration of every central identity.

The result is presented as a rigorous construction and parameterization, not
as an unsupported new theorem.

## 3. Repository architecture

The existing Phase 3 Quarto project is moved intact from `paper/` to
`paper/phase3/`. A new independent Phase 4 project is created at
`paper/phase4/`.

```text
paper/
  README.md
  phase3/
    _quarto.yml
    index.qmd
    references.bib
    environment.yml
    README.md
    notebooks/
    figures/
    tables/
    filters/
    styles/
    output/
  phase4/
    _quarto.yml
    index.qmd
    references.bib
    environment.yml
    README.md
    RESEARCH_NOTES.md
    notebooks/
      build_phase4_discovery.py
      phase4_discovery.ipynb
    figures/
      vector/
      raster/
    tables/
    filters/
    styles/
    output/
```

Each paper remains independently renderable. Phase 4 may copy the proven Phase
3 filter and style, but it must not depend on files inside `paper/phase3/`.
This prevents changes to one manuscript from invalidating the other.

The root `README.md` and `paper/README.md` become the authoritative navigation
indexes. Every existing path that moves under `paper/phase3/` is updated in
project documentation and coordination records.

## 4. Research design

Research is completed before manuscript prose is drafted. The research record
is saved in `paper/phase4/RESEARCH_NOTES.md` and contains:

- a verified bibliography table with authors, year, venue, DOI or stable URL,
  publication type, and relevance;
- a claim-to-source matrix identifying which source supports which
  mathematical or historical statement;
- a distinction between sources used for theory, numerical methodology,
  complex-valued SDE precedent, and contrast with planar Brownian motion;
- a list of claims deliberately excluded because the literature does not
  support them; and
- a source-audit checklist confirming that every manuscript citation key
  exists in `references.bib`.

The primary literature set includes:

- Itô's original stochastic differential formula;
- Doléans-Dade's original change-of-variables and stochastic-exponential work;
- Higham's exact linear SDE solution and example-driven numerical methodology;
- Buckwar, Horváth-Bokor, and Winkler on complex GBM as a scalar linear test
  equation;
- Perret's treatment of complex linear SDEs and their moments;
- Larsson and Ruf on stochastic exponentials and stochastic logarithms;
- Černý and Ruf on complex-valued semimartingale calculus and multiplicative
  compensation;
- Spitzer and Pitman--Yor on planar Brownian winding, used only to distinguish
  the present one-driver process from planar Brownian motion; and
- standard Brownian-motion and SDE references for assumptions and notation.

Secondary or tertiary sources may help discover primary sources but may not
support central mathematical claims.

## 5. Manuscript architecture

The canonical manuscript is `paper/phase4/index.qmd`, with this structure:

1. **Abstract.** State the model, exact GBM modulus, phase, Itô correction,
   rank-one limitation, and reproducible validation.
2. **Introduction.** Motivate the request for one complex exponential combining
   time and Brownian increments without defining Cartesian primitives.
3. **Literature and positioning.** Establish precedent and the exact novelty
   boundary.
4. **Preliminaries and notation.** State the filtered probability space,
   Brownian assumptions, complex bracket conventions, and phase lift.
5. **Problem formulation.** List the required properties and reject circular
   or Cartesian-first constructions.
6. **Native complex exponential construction.** Define the process directly.
7. **Modulus and phase.** Prove exact GBM radius and unwrapped phase.
8. **Complex Itô dynamics.** Derive the full drift
   \(\mu-\beta^2/2+i(\omega+\sigma\beta)\).
9. **Stochastic exponential and logarithm.** Reconcile ordinary and Doléans
   exponentials.
10. **Exact transition and random walk.** Derive the one-step formula.
11. **Moments and transition laws.** Derive radial, complex, and mixed moments.
12. **Geometry and noise dimension.** Prove rank-one log-polar covariance and
    describe fixed-time support.
13. **Phase 3 and two-driver boundaries.** Identify the constrained spiral
    subfamily and independent-noise comparator.
14. **Numerical methods.** Document seeds, estimators, shared-path convergence,
    and tolerances.
15. **Numerical results.** Present exactness, moments, covariance, convergence,
    and bracket evidence.
16. **Discussion.** Explain what the representation achieves.
17. **Limitations.** State rank, branch, modeling, and novelty limitations.
18. **Conclusion.** Give the three equivalent final forms.
19. **Appendices.** Expanded Itô algebra, moment derivations, and
    reproducibility manifest.

The target length is comparable to the Phase 3 paper: approximately 20--28
letter-size PDF pages, depending on figure placement.

## 6. Computational architecture

`paper/phase4/notebooks/build_phase4_discovery.py` is the deterministic source
for the executed notebook. It imports the tested root `phase4_model.py` rather
than duplicating the model formulas.

The notebook:

- records the conda environment, Python version, operating platform, and
  numerical package versions;
- uses deterministic seeds in the `20260724` family;
- executes from the repository without absolute paths;
- exports all figures in vector PDF and raster PNG formats;
- exports all tables as CSV or JSON;
- prints a compact deterministic summary consumed by verification; and
- contains assertions for every exact identity and acceptance threshold.

Planned figures:

1. research and claim map;
2. complex log-plane to exponential-plane mapping;
3. linked modulus, phase, and complex path;
4. space-time trajectory;
5. deterministic/stochastic rotation parameter gallery;
6. constant-modulus Itô-correction stress test;
7. exact multiplicative-step geometry;
8. transition distribution in log-polar coordinates;
9. fixed-time logarithmic-spiral support;
10. one-driver local noise direction;
11. covariance eigenspectrum and rank;
12. one-driver versus two-driver increment clouds;
13. radial and mixed moment validation;
14. complex mean geometry;
15. Phase 3 constrained-subfamily comparison;
16. Euler--Maruyama strong convergence;
17. bilinear versus Hermitian quadratic variation; and
18. representation taxonomy and claim hierarchy.

Planned tables:

- software versions;
- exactness and invariant errors;
- coefficient reconciliation;
- moment validation with Monte Carlo standard errors;
- one-driver and two-driver covariance ranks;
- strong-convergence data;
- complex quadratic-variation data;
- Phase 3 equivalence data; and
- literature claim-source matrix.

## 7. Rendering design

Quarto renders:

- `paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf`;
- `paper/phase4/output/phase4-native-complex-geometric-brownian-motion.html`;
- the executed discovery notebook and its HTML preview.

PDF uses LuaLaTeX, letter paper, one-inch margins, numbered sections,
cross-references, embedded fonts, vector figures, and a retained TeX source.
HTML uses raster companions, a table of contents, code folding, accessible
figure alt text, and external links opening separately.

## 8. Error handling and reproducibility

The builder fails explicitly when:

- the root model module cannot be imported;
- required package versions cannot be recorded;
- a generated figure or table is missing;
- an exact identity exceeds its tolerance;
- a Monte Carlo result exceeds its documented uncertainty threshold;
- the one-driver covariance has numerical rank other than one beyond
  tolerance;
- the two-driver control fails to have rank two for nonzero
  \(\sigma,\beta\); or
- an output path would escape `paper/phase4/`.

The render is rejected if:

- citations or cross-references are unresolved;
- the PDF has missing or substituted fonts;
- expected vector figures are absent;
- HTML figure sources or alt text are missing;
- the notebook has error outputs or nonsequential execution counts; or
- two clean executions differ in deterministic code/output hashes.

## 9. Verification

Verification includes:

1. the root Phase 4 unit suite;
2. Python compilation of the model, tests, and notebook builder;
3. two clean notebook executions with saved outputs;
4. equality of deterministic code sources, output streams, and generated
   tables across runs;
5. Quarto PDF and HTML rendering;
6. PDF page count, page-size, font-embedding, unresolved-reference, and visual
   checks;
7. HTML link, image-source, and figure-alt validation;
8. bibliography key and DOI/stable-URL validation;
9. figure/table manifest validation;
10. `git diff --check`; and
11. independent OpenCode GLM 5.2 review.

## 10. Independent review

After Codex completes the implementation and local verification, OpenCode
`zai-coding-plan/glm-5.2` receives a review-only task. It must:

- independently re-derive the central formulas;
- inspect literature positioning and novelty language;
- verify manuscript-to-notebook numerical consistency;
- inspect PDF/HTML presentation and accessibility evidence;
- report findings with severity and file/line references; and
- write only `.agent/reviews/TASK-006-opencode-glm52-review.md`.

Codex resolves every critical or major finding, evaluates the external call
with `llm-scorecard`, and records the review and scorecard identifiers.

## 11. Non-goals

The project will not:

- claim that complex GBM is newly invented;
- identify \(d[W,W]_t=dt\) with the algebraic identity \(i^2=-1\);
- call the one-driver process planar Brownian motion;
- introduce financial interpretation beyond standard GBM terminology;
- add package dependencies or mutate the conda environment;
- delegate implementation to another agent;
- alter the mathematical content of the completed Phase 3 paper while moving
  it; or
- commit, push, merge, or publish the final implementation unless separately
  authorized.

## 12. Acceptance criteria

The task is complete when:

- the two-paper hierarchy renders both Phase 3 and Phase 4 independently;
- all moved Phase 3 links are repaired;
- Phase 4 has a verified primary-source research record;
- the manuscript contains the full research-paper structure;
- all 18 planned visual explanations and all planned tables are generated;
- the notebook executes twice without errors and reproducibly regenerates
  outputs;
- exact and Monte Carlo checks meet their stated thresholds;
- PDF and HTML pass technical and visual inspection;
- the root tests remain green;
- OpenCode GLM 5.2 returns a reviewed verdict and all critical or major
  findings are resolved; and
- project coordination records identify the final artifacts and evidence.
