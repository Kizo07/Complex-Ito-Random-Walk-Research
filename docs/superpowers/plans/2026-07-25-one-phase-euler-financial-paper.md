# One-Phase Euler Financial Paper Implementation Plan

> **Execution rule:** Use `superpowers:executing-plans` task by task. The user
> explicitly prohibited implementation delegation. Codex implements directly;
> OpenCode `zai-coding-plan/glm-5.2` is reserved for the final independent
> review.

**Goal:** Produce a research-grade, self-contained mathematical-finance paper
on exact one-phase Euler coordinates for affine Brownian factors, with a
reproducible notebook, comprehensive primary-source record, publication
figures, evidence tables, PDF, and HTML companion.

**Architecture:** Add a third independent Quarto manuscript project at
`paper/one-phase-euler/`. Preserve all prior mathematical and publication
artifacts. Generate the new paper's computational evidence with a
deterministic notebook builder that imports the tested `phase5_model.py` and
adds finance-specific pricing, Greek, and PDE experiments.

**Environment:** Existing conda environment `phase3-paper`; Python 3.12,
NumPy, SciPy, pandas, Matplotlib, Seaborn, SymPy, Jupyter/nbformat, Quarto,
Pandoc, and LuaLaTeX. Do not install or upgrade packages.

## Global constraints

- Write only under the project directory, with temporary validation files
  under `/tmp`.
- Preserve untracked `critique2.md`; never stage, edit, move, or remove it.
- Do not alter the completed mathematical content of `paper/phase3/`,
  `paper/phase4/`, or the validated root research artifacts.
- Do not delegate implementation to agy, Copilot, Grok, subagents, or other
  workers.
- Use OpenCode GLM 5.2 only after Codex completes implementation and local
  verification.
- Use `agent-usage` and `llm-scorecard` for the external review.
- Do not mutate the conda environment.
- Do not commit, push, publish, or open a pull request unless separately
  authorized.
- State exact, almost-sure, distributional, asymptotic, and empirical claims
  distinctly.
- Treat numerical experiments as validation, not proof.

## Deliverable tree

```text
docs/superpowers/specs/
  2026-07-25-one-phase-euler-financial-paper-design.md
docs/superpowers/plans/
  2026-07-25-one-phase-euler-financial-paper.md
.agent/tasks/
  TASK-008.md
.agent/reviews/
  TASK-008-opencode-glm52-review.md
.agent/evidence/
  TASK-008-verification.md
paper/
  README.md
  one-phase-euler/
    _quarto.yml
    index.qmd
    references.bib
    RESEARCH_NOTES.md
    README.md
    environment.yml
    filters/format-figures.lua
    styles/paper.scss
    notebooks/
      build_one_phase_euler_finance.py
      one_phase_euler_finance.ipynb
    figures/
      vector/*.pdf
      raster/*.png
    tables/*.{csv,json}
    output/
      one-phase-euler-affine-brownian-factors.pdf
      one-phase-euler-affine-brownian-factors.html
      one-phase-euler-affine-brownian-factors.tex
```

---

## Task 1: Establish TASK-008 and publication boundaries

**Files:**

- Create `.agent/tasks/TASK-008.md`
- Modify `.agent/status.md`
- Modify `.agent/state.json`
- Modify `.agent/handoff.md`

- [ ] Record the user-approved objective, direct-implementation exception,
  allowed paths, deliverables, acceptance gates, reviewer, and prohibitions.
- [ ] Mark TASK-008 active without erasing the completed TASK-007 record.
- [ ] Confirm the branch and dirty-worktree state.
- [ ] Record `critique2.md` as protected and out of scope.

## Task 2: Complete the section-by-section literature audit

**Files:**

- Create `paper/one-phase-euler/RESEARCH_NOTES.md`
- Create `paper/one-phase-euler/references.bib`

- [ ] Verify primary or authoritative references for Brownian motion,
  Bachelier, Itô calculus, Girsanov, Feynman--Kac, support, boundary
  classification, stochastic transformations, angular distributions,
  stochastic exponentials, complex SDEs, financial PDE compactification,
  Monte Carlo/QMC, geometric integration, and complex differentiation.
- [ ] Record authors, title, year, venue, volume/pages, DOI/stable URL,
  primary/secondary status, and exact supported claim.
- [ ] Add page, theorem, or equation pointers when available.
- [ ] Build a novelty-boundary matrix distinguishing established tools from
  this paper's classification and synthesis.
- [ ] Record rejected or weak sources so they are not accidentally cited.
- [ ] Validate every BibTeX entry with Pandoc/citeproc.
- [ ] Audit that every substantive historical statement has a source and that
  central claims rely on primary sources.

## Task 3: Scaffold the independent Quarto project

**Files:**

- Create `paper/one-phase-euler/_quarto.yml`
- Create `paper/one-phase-euler/environment.yml`
- Create `paper/one-phase-euler/README.md`
- Create `paper/one-phase-euler/filters/format-figures.lua`
- Create `paper/one-phase-euler/styles/paper.scss`
- Modify `paper/README.md`

- [ ] Copy the proven format-specific figure filter and publication style.
- [ ] Configure independent PDF and HTML output.
- [ ] Set the manuscript title slug, bibliography, notebook, cross-reference
  prefixes, and output directory.
- [ ] Record the existing environment without installation.
- [ ] Document exact notebook, render, and verification commands.
- [ ] Add the new paper to the publication index without changing earlier
  entries.

## Task 4: Add finance-specific mathematical functions and tests

**Files:**

- Create `paper/one-phase-euler/notebooks/build_one_phase_euler_finance.py`
- If reusable functions are needed, modify `phase5_model.py`
- If the model changes, modify `tests/test_phase5_model.py`

- [ ] Reuse the tested secant and general-affine maps.
- [ ] Implement pure functions for the canonical phase drift and diffusion,
  Gaussian-to-phase density, Bachelier call value, scalar Greeks, transformed
  Greeks, pricing-operator conjugacy, and exact phase transition.
- [ ] Write tests before any reusable model change.
- [ ] Verify limiting and degenerate parameter cases.
- [ ] Check density normalization, inverse reconstruction, Greek chain rules,
  and PDE residuals.
- [ ] Keep backward compatibility with all 33 existing tests.

## Task 5: Build the deterministic research notebook

**Files:**

- Create `paper/one-phase-euler/notebooks/build_one_phase_euler_finance.py`
- Generate `paper/one-phase-euler/notebooks/one_phase_euler_finance.ipynb`
- Generate `paper/one-phase-euler/figures/vector/*.pdf`
- Generate `paper/one-phase-euler/figures/raster/*.png`
- Generate `paper/one-phase-euler/tables/*.{csv,json}`

- [ ] Record Python, OS, conda environment, and numerical package versions.
- [ ] Explain the discovery chain from support geometry to the secant chart.
- [ ] Derive and symbolically/numerically verify the classification formulas.
- [ ] Generate the 22 planned publication figures with accessible alt text.
- [ ] Generate deterministic evidence tables and an artifact manifest.
- [ ] Use seeds in the `20260725` family and report Monte Carlo uncertainty.
- [ ] Validate exact reconstruction, density, semigroup, generator,
  Fokker--Planck, boundary, group, covariance-rank, pricing, Greek, PDE,
  Monte Carlo, QMC, and negative-control claims.
- [ ] Execute twice from clean kernels and compare deterministic artifacts.
- [ ] Leave the canonical notebook in an executed, sequential, error-free
  state.

## Task 6: Write the manuscript

**Files:**

- Create `paper/one-phase-euler/index.qmd`

- [ ] Write a concise abstract that states the exact theorem, financial
  conjugacy, and numerical conclusion without overstating novelty.
- [ ] Add keywords, MSC classifications, and JEL classifications.
- [ ] Write the introduction and contribution list.
- [ ] Write the literature review and explicit novelty boundary.
- [ ] State all probabilistic, geometric, analytic, and financial assumptions.
- [ ] Give complete necessity and sufficiency proofs.
- [ ] Derive the canonical/general phase maps, inverse, SDE, generator,
  density, semigroup, and endpoint behavior.
- [ ] Derive additive/multiplicative rigidity and transported group laws.
- [ ] Derive risk-neutral pricing conjugacy and Greek transformations.
- [ ] Present Bachelier benchmarks and numerical methods.
- [ ] Report every numerical value from generated evidence, not memory.
- [ ] Discuss stochastic dimension, vector geometry, complex differentiation,
  and numerical implications conservatively.
- [ ] State limitations and a concrete research agenda.
- [ ] Add proof, Itô, pricing, and reproducibility appendices.
- [ ] Ensure no internal phase/task/document terminology appears in the
  academic article.

## Task 7: Render and publication-check

**Files:**

- Generate `paper/one-phase-euler/output/*`

- [ ] Run `quarto inspect` and `quarto render`.
- [ ] Reject unresolved citations, cross-references, or missing assets.
- [ ] Confirm letter-size pages, embedded fonts, one-inch margins, and retained
  TeX.
- [ ] Inspect every PDF page visually for clipping, bad floats, malformed
  equations, sparse pages, and unreadable legends.
- [ ] Validate every HTML local link, image source, figure alt text, and table.
- [ ] Confirm all manuscript numbers match generated evidence.
- [ ] Confirm all bibliography entries are cited and all citation keys resolve.

## Task 8: Full local verification

**Files:**

- Create `.agent/evidence/TASK-008-verification.md`

- [ ] Run focused and full unit tests.
- [ ] Compile Python sources.
- [ ] Rebuild and execute the notebook from clean state twice.
- [ ] Hash normalized code cells, deterministic streams, generated tables, and
  manuscript source.
- [ ] Validate figure/table manifests and counts.
- [ ] Validate PDF metadata, pages, fonts, and unresolved markers.
- [ ] Validate HTML accessibility and links.
- [ ] Run `git diff --check`.
- [ ] Preserve exact commands, outcomes, and hashes in the verification ledger.

## Task 9: Independent OpenCode GLM 5.2 review

**Files:**

- Create `.agent/reviews/TASK-008-opencode-glm52-review.md`

- [ ] Prepare a review-only prompt with explicit file scope and no
  implementation authority.
- [ ] Require independent re-derivation of the main theorem, phase SDE,
  transition density, pricing PDE, and Greeks.
- [ ] Require a source/novelty audit and checks for unsupported claims.
- [ ] Require notebook-to-manuscript numerical reconciliation.
- [ ] Require PDF/HTML presentation and accessibility inspection.
- [ ] Record the `agent-usage` call identifier.
- [ ] Evaluate the review with `llm-scorecard`.
- [ ] Resolve every valid critical, major, and minor finding.
- [ ] Rerun affected verification gates.

## Task 10: Finalize records and handoff

**Files:**

- Modify `.agent/status.md`
- Modify `.agent/state.json`
- Modify `.agent/handoff.md`
- Modify `paper/one-phase-euler/README.md`

- [ ] Mark TASK-008 complete only after all acceptance gates pass.
- [ ] Record final hashes, page count, artifact counts, test counts, review
  result, usage ID, and scorecard ID.
- [ ] Confirm `critique2.md` remains untouched and untracked.
- [ ] Deliver clickable paths to the PDF, HTML, manuscript, notebook, research
  notes, and implementation plan.

## Acceptance definition

The task is complete only when the paper is mathematically self-contained,
academically positioned, reproducible from the recorded environment, rendered
successfully as PDF and HTML, reconciled against notebook evidence, visually
inspected, independently reviewed by OpenCode GLM 5.2, and free of unresolved
critical or major findings.
