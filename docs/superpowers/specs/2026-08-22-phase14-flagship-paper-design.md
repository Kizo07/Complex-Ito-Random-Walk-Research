# Phase 14 Flagship Paper Design

**Date:** 2026-08-22

**Approved direction:** theorem-led flagship paper

**Working title:** *Hidden Exactness in Bounded-Factor Stochastic Models:
Variance-Mixture Smiles, Leverage Closure, and Phase-Gram Stationarity*

**Author:** Kanav Mehta

## 1. Purpose

Create a standalone, professionally typeset Phase 14 research paper that
turns `PHASE_14_HIDDEN_EXACTNESS_AND_CORRECTED_FRONTIERS.md` into a coherent
academic manuscript. The new paper must retain the mathematical substance of
all seven surviving Phase 14 results while presenting the three major
discoveries as one unified thesis:

1. exact Bachelier variance-mixture level and curvature identities;
2. one-dimensional transform closure under Brownian leverage; and
3. stationary and boundary laws for Phase-Gram correlation matrices.

The remaining results—correct scale symmetry, nonautonomous Feynman–Kac
operator ordering, the joint endpoint–clock density, and spectrally one-sided
Lévy barrier transforms—serve as mathematically consequential extensions and
corrections rather than competing headline claims.

The manuscript is not a lightly restyled copy of the Phase 14 Markdown draft.
It must be rewritten as a self-contained research article with a clear thesis,
formal assumptions, detailed proofs, related-work positioning, explanatory
transitions, figures, tables, appendices, and a restrained novelty boundary.

## 2. Deliverables

Create an isolated Quarto manuscript project under `paper/phase14/` containing:

- `_quarto.yml` for manuscript, PDF, and HTML output;
- `index.qmd` as the canonical paper source;
- `references.bib` containing verified, cited references;
- `RESEARCH_NOTES.md` recording the source audit and claim boundaries;
- `README.md` with render instructions and artifact map;
- `styles/paper.scss` for the HTML visual system;
- `tex/header-includes.tex` for robust professional PDF typography;
- `filters/format-figures.lua`, adapted from the established project pattern;
- `figures/` containing publication-quality raster figures and, where useful,
  vector PDF companions;
- `tables/` containing the numerical values used in the paper;
- `scripts/build_phase14_figures.py`, a deterministic figure/table generator;
- rendered HTML, PDF, retained TeX, figures, and copied bibliography under
  `paper/phase14/output/`.

Update `paper/README.md` only to add the finished Phase 14 paper to the paper
index. Do not modify prior phase manuscripts or outputs.

## 3. Manuscript scale and voice

Target 40–55 letter-size PDF pages, excluding any long automatically generated
bibliography spillover. The paper should be detailed enough that a stochastic-
calculus researcher can verify every central derivation without consulting the
phase notes.

The voice is formal, precise, and skeptical. It must distinguish:

- exact identities;
- equalities in conditional law;
- local asymptotic expansions;
- sufficient conditions;
- corrections to earlier project statements;
- classical ingredients newly combined here; and
- claims for which no priority is asserted.

Avoid promotional adjectives in theorem statements. “Breakthrough,” “first,”
and “unique” may appear only if directly supported by a completed literature
audit; the default wording is “we derive,” “we prove,” or “within the model
class considered here.”

## 4. Narrative architecture

### Front matter

- Title, subtitle, author, date, keywords, MSC 2020, and JEL classifications.
- A 350–500 word structured abstract describing the three main results, the
  four supporting results, and the precise limitation that world-priority is
  not claimed.
- A one-page contribution map separating discoveries, corrections, exact
  extensions, and rejected claims.

### Part I — Problem and framework

1. **Introduction.** Motivate bounded stochastic correlation, exact path laws,
   variance mixtures, leverage, and matrix admissibility. State the paper’s
   single thesis: several apparent losses of exactness are losses of a special
   representation, not losses of one-dimensional transform closure.
2. **Relationship to Phases 6–13.** Give a self-contained account of the
   bounded coordinate, variance clock, Phase-Gram construction, and the four
   statements corrected in Phase 14. Do not require the reader to know the
   repository history.
3. **Notation and assumptions.** Consolidate probability-space, Brownian
   covariance, integrability, regularity, transform, and implied-correlation
   conventions in one reference section.

### Part II — Exact variance-mixture smile geometry

4. **Centered Gaussian scale mixtures.** Define the Bachelier call, total
   implied standard deviation, and constant-correlation inversion.
5. **Level-and-curvature theorem.** Prove evenness, the ATM level
   `E[sqrt(V)]`, the inverse-moment curvature formula, strictness conditions,
   and the admissible-correlation inversion.
6. **The ATM Jensen wedge.** Derive the exact correction to the mean clock,
   prove the spread/basket sign split, develop a small-clock-dispersion
   expansion, and reconcile the Phase 8 numerical values.
7. **Interpretation and limitations.** Explain what the local theorem does and
   does not prove about global wings. Relate the formula to modern work on
   Bachelier implied curvature without claiming the general subject as new.

### Part III — Leverage closure

8. **Admissible leveraged Brownian geometry.** Derive the three-driver PSD
   condition, orthogonal decomposition, covariance-rate determinant, and the
   state-dependent leverage seen by the second asset.
9. **Conditional Gaussian law with random mean.** Give the process-level
   conditional law and clarify exactly why the earlier “conditional
   Gaussianity is destroyed” statement was false.
10. **Itô gauge transform.** Derive the explicit primitive, endpoint-plus-
    additive-functional representation, and regularity conditions.
11. **One-dimensional transform theorem.** Derive the joint generator,
    Fourier-reduced PDE, equivalent complex-potential Feynman–Kac equation,
    zero-leverage degeneration, uniqueness conditions, and exponential-moment
    bound.
12. **Skewness and broken symmetry.** Prove the short-time third-moment
    expansion and connect it carefully to loss of global implied-smile
    evenness without overclaiming a nonzero ATM slope.
13. **True barrier frontier.** Show that leverage produces a conditional
    moving boundary, classify the zero-mean recovery case, and state the open
    exceptional-solvability problem.

### Part IV — Phase-Gram quotient theory

14. **Triangular-angle construction.** Restate the Gram map and distinguish
    the unwrapped lift from the observable matrix.
15. **Determinant theorem.** Prove the product-of-squared-sines identity and
    finite-time integer moment formula.
16. **Stationary quotient law.** Prove convergence of wrapped angles to Haar
    measure and the stationary matrix pushforward, including `E[R]=I`.
17. **Product-Beta determinant law.** Derive the Mellin transform,
    log-determinant mean and variance, arithmetic/geometric determinant gap,
    and high-dimensional CLT.
18. **Boundary hitting.** Derive the exact first-singularity survival product,
    explain deterministic versus random initial states, and prove recurrent
    boundary contact.
19. **Structural implications.** Explain how identity mean coexists with
    typical near-singularity and identify the open smallest-eigenvalue problem.

### Part V — Corrected and extended frontiers

20. **Nonautonomous Feynman–Kac.** Present the two-time evolution family,
    right-versus-left operator ordering, exact commutator defect, linear-
    potential Gaussian calculation, and the constant-coefficient iff result.
21. **Maximal scale symmetry.** Prove the normalized Gaussian path-law
    criterion, correct the simultaneous scaling orbit, and discuss the signed-
    volatility gauge and exogenous scale breaking.
22. **Joint endpoint–clock law.** Derive the tilted endpoint kernel,
    distributional Fourier inversion, Hörmander bracket condition, and the
    corridor-atom boundary.
23. **Spectrally one-sided Lévy barriers.** State and prove the monotone
    transfer to one-sided fluctuation identities, define scale-function
    normalization, and separate this classical extension from the two-sided
    VG/NIG setting.

### Closing material

24. **Unified exactness map.** A table showing which structures retain static
    laws, terminal transforms, smile symmetry, barrier reduction, stationarity,
    and exact boundary transforms.
25. **Limitations and open problems.** Preserve all seven mathematically
    specific research questions from the Phase 14 draft.
26. **Conclusion.** State the corrected closure principle and the three major
    results without novelty inflation.

### Appendices

- A. Bachelier derivative calculations and implicit-function details.
- B. Brownian covariance decomposition and Itô-gauge algebra.
- C. Generator calculation for the short-time third moment.
- D. Fourier expansion and Beta-polygamma identities for Phase-Gram.
- E. Killed-heat-kernel derivation of the first-singularity law.
- F. Nonautonomous evolution-family and commutator derivation.
- G. Gaussian path-law identifiability proof.
- H. Hypoellipticity and Lévy scale-function conventions.
- I. Numerical values and figure-generation definitions.

## 5. Figure and table program

Create publication-quality figures that explain mathematics rather than merely
decorate it:

1. **Contribution and correction map:** phases 6–13 inputs flowing into the
   three Phase 14 theorem families.
2. **ATM Jensen wedge:** mean clock versus spread and basket ATM implied
   correlation, with exact decomposition annotations.
3. **Local curvature identity:** exact curvature versus clock-dispersion
   parameter for positive and negative `alpha`.
4. **Leverage geometry:** orthogonal Brownian decomposition, common-factor
   mean, residual clock, and one-dimensional transform closure.
5. **Characteristic-function validation:** direct leveraged simulation versus
   conditional and gauge-transformed characteristic functions.
6. **Phase-Gram determinant law:** finite-time determinant moments converging
   to stationary values.
7. **Stationary log determinant:** standardized histogram against the exact
   CLT normal reference for increasing matrix dimension.
8. **Operator-ordering diagram:** two-time evolution versus the invalid
   one-parameter left action, annotated by the commutator defect.

Required tables:

- notation and assumptions;
- main theorem map;
- correction ledger for Phases 7–10;
- independence versus leverage tractability;
- Phase-Gram stationary determinant formulas;
- unified exactness frontier;
- numerical identity checks;
- literature comparison and novelty boundary.

Figures use a restrained navy/teal/rust palette, colorblind-safe distinctions,
vector output for line art, 300-DPI raster companions, readable labels at
single-column width, and descriptive alt text in HTML.

## 6. Literature and references

Build a verified bibliography centered on primary papers and authoritative
monographs. The source program covers:

- Bachelier pricing and normal implied volatility;
- variance mixtures and stochastic-volatility smile geometry;
- modern ATM Bachelier curvature results;
- stochastic correlation, spread/basket pricing, Jacobi and Wishart models;
- conditional Gaussianity, stochastic time changes, and leverage;
- Feynman–Kac formulas, nonautonomous evolution families, and time-ordered
  semigroups;
- hyperspherical parameterizations, LKJ/random correlation matrices, Brownian
  motion on compact groups, and product-Beta laws;
- Hörmander hypoellipticity and integrated diffusions;
- spectrally negative Lévy processes and scale functions; and
- foundational Itô, DDS, and stochastic-calculus references.

Every cited entry must be used in the manuscript. Central mathematical
attributions use primary sources or standard monographs. Search-result snippets
are discovery aids only. The paper must explicitly identify results that are
classical ingredients, project corrections, or potentially new combinations.

Target 55–85 references, determined by relevance rather than quota.

## 7. Visual and typographic design

The paper retains the clean Phase 6 lineage but is more polished.

### PDF

- Letter paper, 10.5–11 pt body, approximately one-inch margins.
- KOMA-Script article class with a dedicated title page.
- Embedded fonts and high-quality mathematical typography.
- Running headers, restrained colored rules, page numbers, and a detailed TOC.
- Numbered sections, equations, theorems, propositions, lemmas, corollaries,
  definitions, remarks, and examples.
- Consistent proof-ending marks and controlled theorem spacing.
- Professional table rules, repeated headers where needed, and no vertical
  table borders.
- Figures placed near first reference without clipping or float congestion.

### HTML

- Deep navy/teal title banner derived from Phase 6.
- Sticky table of contents and clear section hierarchy.
- Distinct but restrained theorem, proof, correction, and limitation panels.
- Responsive figures, accessible alt text, visible equation numbering, and
  external links opening separately.
- Tabular numerals and readable maximum line width.

The design must remain recognizably academic. It must not resemble a marketing
landing page or use ornamental imagery unrelated to the mathematics.

## 8. Mathematical quality gates

- Preserve every hypothesis added during the two independent Phase 14 reviews.
- Re-derive all central equations rather than copying unsupported statements.
- Keep `q`-type notation disambiguated between asset loadings and Lévy killing
  rates.
- Mark equalities in conditional law explicitly.
- Restrict the centered-mixture smile theorem to random conditional variance
  with zero conditional mean.
- State inverse-moment conditions for finite ATM curvature.
- State deterministic/independent initial-angle conditions for Phase-Gram
  product formulas.
- Use generalized inverses for possibly degenerate clocks.
- Do not claim a general converse to the nonautonomous commutator identity.
- State smoothness/nonexplosion assumptions for Hörmander arguments.
- State scale-function normalization and one-sided Lévy hypotheses.
- Separate local ATM curvature from global wing behavior.
- Separate world-priority claims from results newly derived within this
  project.

## 9. Publication and verification gates

The work is accepted only when:

1. `quarto render paper/phase14` exits successfully and produces PDF and HTML.
2. The PDF has letter-size pages, embedded fonts, no clipping, no malformed
   equations, no orphaned headings, and no unresolved citation or cross-
   reference markers.
3. Every PDF page is inspected via contact sheets, with title, theorem-dense,
   figure-dense, appendix, and final pages inspected at full resolution.
4. The HTML contains no missing images, empty figure alt text, broken internal
   fragments, or unresolved references.
5. All bibliography entries are cited and all citation keys resolve.
6. Numerical figure values reproduce the exact identities and previously
   verified anchors, including the Phase 8 mean-clock correction.
7. The direct, conditional, and gauge-transformed leveraged characteristic
   functions agree within the reported Monte Carlo uncertainty.
8. The Phase-Gram finite-time and stationary determinant formulas agree with
   independent simulation.
9. The manuscript receives an independent mathematical review and a separate
   publication/visual review; all critical and major findings are resolved.
10. `git diff --check` passes, prior phase sources remain unchanged, and the
    protected untracked `critique2.md` remains untouched.

## 10. Scope boundaries

- Do not alter completed Phase 1–13 mathematics.
- Do not publish, push, open a pull request, or release the paper.
- Do not claim empirical validation beyond the existing numerical examples.
- Do not add a new calibration study or large simulation campaign unless a
  mathematical claim requires it.
- Do not create a notebook merely to mimic the Phase 6 directory; the
  deterministic figure script is sufficient for this paper’s mathematics-
  first scope.
- Do not pad the paper to hit a page count. Detail must serve proof,
  interpretation, literature positioning, or reproducible figures.

## 11. Expected final artifact

The final Phase 14 paper should read as a unified research contribution, not a
repository audit. A reader should leave with three clear results:

1. clock dispersion, not the mean clock alone, determines the ATM
   implied-correlation level and curvature;
2. Brownian leverage preserves one-dimensional European transform closure but
   replaces a centered variance mixture by a random-mean Gaussian mixture; and
3. Phase-Gram matrices possess a compact stationary quotient law whose exact
   determinant distribution reveals recurrent boundary contact and severe
   high-dimensional near-singularity.

The four supporting sections should reinforce that thesis by replacing broad
“exactness is lost” statements with precise mathematical frontiers.
