# TASK-004 — Phase 3 technical paper

## Status

Complete.

## Risk tier

Tier 2: substantive mathematical publication work with executable simulations
and a PDF build pipeline.

## Authorization

The user approved `PHASE_3_TECHNICAL_PAPER_PLAN.md`, installed the requested
publication packages, and explicitly authorized Codex to implement the work
directly. No implementation work may be delegated. opencode with
`zai-coding-plan/glm-5.2` is reserved for an independent review after the
paper and reproducibility checks are complete.

On 2026-07-24, after accepting the completed artifacts, the user separately
authorized committing them, pushing the current feature branch, and opening a
GitHub pull request.

## Objective

Turn the completed Phase 3 results into a self-contained technical paper that
explains how the one-driver logarithmic-spiral representation was discovered,
derives its stochastic calculus rigorously, distinguishes it from rank-two
planar Brownian motion, and supports the analysis with publication-quality
figures and reproducible simulations.

The paper must remain within Phase 3. Earlier phases may appear only as brief
motivation or as the two-driver control required for the covariance-rank
comparison.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

## Expected deliverables

- `paper/_quarto.yml`
- `paper/index.qmd`
- `paper/references.bib`
- `paper/README.md`
- `paper/environment.yml`
- `paper/notebooks/build_phase3_discovery.py`
- `paper/notebooks/phase3_discovery.ipynb`
- publication figures under `paper/figures/`
- generated tables under `paper/tables/`
- rendered PDF under `paper/output/`
- `.agent/reviews/TASK-004-opencode-glm52-review.md`
- updates to `README.md`, `.agent/status.md`, `.agent/handoff.md`, and
  `.agent/state.json`

## Mathematical acceptance criteria

- State the central model
  \[
  Z_t=Z_0\exp((\alpha+i\beta)(X_t-X_0))
  \]
  with exactly one Brownian driver.
- Derive its radius, unwrapped angle, inverse-radius map, Itô SDE, stochastic
  logarithm, exact step rule, moments, and both complex brackets.
- Prove and visualize the rank-one covariance obstruction for one scalar
  Brownian driver.
- Keep the rank-two planar process explicitly labelled as a comparator, never
  as an equivalent representation.
- Treat the literal scalar polar form at zero using localization, Tanaka's
  formula, and local time.
- Separate exact theorems, numerical evidence, intuition, and heuristic
  notation.
- Make no unsupported novelty claim.

## Computational acceptance criteria

- Use the conda environment `phase3-paper`.
- Use deterministic seeds and record package versions.
- Build a new discovery notebook rather than repackaging the Phase 3
  verification notebook.
- Execute the notebook twice from clean kernels without cell errors and verify
  stable numerical summaries.
- Produce at least twelve substantive, publication-quality figure panels or
  composite figures spanning geometry, state recovery, exact stepping,
  covariance rank, quadratic variation, convergence, and local time.
- Export canonical figures as vector PDF, with PNG companions for notebook and
  HTML display.
- Render the canonical Quarto manuscript successfully to PDF.
- Check cross-references, citations, equations, extracted text, page geometry,
  and representative rendered pages.
- Obtain an independent opencode GLM 5.2 mathematical and editorial review and
  resolve all critical or major findings.

## Prohibited actions

- No package installation or conda-environment mutation.
- No credential or secret access.
- No writes outside the project.
- No implementation delegation, Copilot calls, agy calls, or Grok calls.
- No merge, release, or publication beyond the separately authorized branch
  push and pull-request creation.
