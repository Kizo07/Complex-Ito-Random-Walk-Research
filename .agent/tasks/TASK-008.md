# TASK-008 — One-phase Euler coordinates mathematical-finance paper

## Status

Complete on 2026-07-25.

## Risk tier

Tier 4 research and publication implementation. The task includes a
classification theorem, stochastic-calculus and financial-pricing
derivations, primary-source research, reproducible simulations, numerical PDE
benchmarks, and publication rendering.

## Authorization

The user approved the theorem-led integrated paper design and explicitly
instructed Codex to save the plan and begin building the paper. The standing
Codex-direct implementation exception applies. Implementation must not be
delegated. OpenCode `zai-coding-plan/glm-5.2` is reserved for independent
review and second opinion after Codex completes implementation and local
verification.

## Objective

Produce a self-contained academic paper provisionally titled **One-Phase Euler
Coordinates for Affine Brownian Factors: Exact Classification, Pricing
Conjugacy, and Numerical Consequences**. The paper must prove the exact
existence criterion for a lossless time-independent one-phase representation,
derive its stochastic theory, establish the risk-neutral pricing conjugacy for
normal/Bachelier factors, audit its geometric and analytic implications, and
test its numerical consequences.

## Approved specifications

- Design:
  `docs/superpowers/specs/2026-07-25-one-phase-euler-financial-paper-design.md`
- Implementation plan:
  `docs/superpowers/plans/2026-07-25-one-phase-euler-financial-paper.md`

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

Temporary validation artifacts may be written under `/tmp`.

## Required deliverables

- self-contained Quarto project under `paper/one-phase-euler/`;
- comprehensive `RESEARCH_NOTES.md` and verified `references.bib`;
- canonical `index.qmd`;
- deterministic notebook builder and executed discovery notebook;
- finance-specific figures and evidence tables;
- rendered PDF, HTML, and retained TeX;
- publication README and updated paper index;
- `.agent/evidence/TASK-008-verification.md`; and
- `.agent/reviews/TASK-008-opencode-glm52-review.md`.

## Mathematical acceptance gates

- State every probabilistic, regularity, branch, nondegeneracy, and financial
  assumption.
- Give gap-free necessity and sufficiency proofs for the affine
  classification.
- Separate measurable factorization from smooth Itô coordinates.
- Verify the exact phase inverse, SDE, generator, transition kernel,
  semigroup, forward equation, and endpoint behavior.
- Derive additive and multiplicative rigidity and the transported group law.
- Derive pricing-PDE conjugacy and Greek transformations in both directions.
- Distinguish driver count, covariance rank, terminal support, and state
  dimension.
- State explicitly what the representation does not imply.

## Research acceptance gates

- Use primary papers or authoritative monographs for central claims.
- Search and audit literature section by section.
- Record verified DOI or stable publisher/repository links.
- Keep the novelty claim narrower than the prior literature.
- Do not cite internal candidate, critique, planning, or phase documents in the
  academic paper.

## Computational acceptance gates

- Use the existing `phase3-paper` conda environment without mutation.
- Execute the notebook top to bottom twice from clean kernels.
- Use deterministic seeds and report Monte Carlo uncertainty.
- Generate vector and raster figure companions with accessible alt text.
- Reconcile every reported numerical value with saved evidence.
- Pass all focused and full-project tests.

## Publication acceptance gates

- Render PDF and HTML successfully with Quarto.
- Embed PDF fonts and use letter paper with one-inch margins.
- Resolve all citations and cross-references.
- Inspect every PDF page and validate HTML links, images, and alt text.
- Retain TeX and preserve a reproducibility manifest.
- Obtain and resolve an independent OpenCode GLM 5.2 review.

## Prohibited actions

- Do not edit, move, stage, or delete untracked `critique2.md`.
- Do not change completed prior-paper mathematics.
- Do not delegate implementation.
- Do not use Grok.
- Do not install or update packages.
- Do not inspect or expose credentials or secrets.
- Do not commit, push, publish, release, or open a pull request unless the user
  separately requests it.
- Do not claim that Euler notation creates stochastic dimension, variance
  reduction, holomorphic structure, or a general analytic solution.

## Completion

All required deliverables and acceptance gates are complete.

- The plan and design were saved before implementation.
- The self-contained paper project contains the source audit, 52 cited
  references, canonical QMD, executed notebook, 22 vector/raster figure pairs,
  44 evidence tables, and PDF/HTML/TeX outputs.
- The full suite passes 39/39 tests.
- Two clean-kernel notebook executions produced byte-identical structured
  evidence and zero errors.
- The final PDF has 47 letter-size pages with embedded fonts; the HTML has no
  missing image, empty alt text, or broken internal fragment.
- OpenCode GLM 5.2 found no critical or major defect. Both minor findings were
  resolved.
- Verification:
  `.agent/evidence/TASK-008-verification.md`.
- Independent review:
  `.agent/reviews/TASK-008-opencode-glm52-review.md`.
