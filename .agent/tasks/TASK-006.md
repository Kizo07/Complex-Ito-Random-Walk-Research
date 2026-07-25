# TASK-006 — Phase 4 technical paper

## Status

Completed on 2026-07-24.

## Risk tier

Tier 3: research-grounded mathematical publication with a repository
reorganization, executable notebook, generated figures and tables, and
PDF/HTML outputs.

## Authorization

The user approved
`docs/superpowers/specs/2026-07-24-phase4-technical-paper-design.md` and
directed Codex to implement it. The standing Codex-direct exception applies:
no implementation may be delegated. OpenCode
`zai-coding-plan/glm-5.2` is reserved for independent review and a second
opinion after Codex completes implementation and verification.

## Objective

Reorganize the publication directory into independent Phase 3 and Phase 4
Quarto projects, preserve the Phase 3 paper, and produce a self-contained Phase
4 technical paper centered on

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
\]

The manuscript must prove the exact GBM modulus, derive phase and complex Itô
dynamics, reconcile ordinary and stochastic exponentials, establish the
one-driver rank-one limitation, recover Phase 3 as a constrained subfamily,
and document the two-driver boundary.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

Temporary notebook and render comparisons may be written under `/tmp`.

## Required deliverables

- two-paper hierarchy under `paper/phase3/` and `paper/phase4/`;
- `paper/README.md`;
- `paper/phase4/RESEARCH_NOTES.md`;
- `paper/phase4/references.bib`;
- `paper/phase4/index.qmd`;
- independent Phase 4 Quarto configuration, style, filter, environment record,
  and README;
- deterministic notebook builder and executed discovery notebook;
- 18 vector figures with raster companions;
- generated exactness, coefficient, transition, covariance, moment, Phase 3,
  convergence, bracket, software, numerical-summary, and manifest tables;
- rendered Phase 4 PDF and HTML;
- updated root navigation and coordination records; and
- `.agent/reviews/TASK-006-opencode-glm52-review.md`.

## Research acceptance criteria

- Research primary literature before drafting manuscript prose.
- Verify bibliographic metadata, DOI or stable URL, and publication role.
- Maintain a claim-to-source matrix.
- Establish that complex GBM and scalar complex linear SDEs already exist.
- Position the paper as a modulus-preserving parameterization and reproducible
  synthesis, not as invention of complex GBM.
- Distinguish the one-driver model from planar Brownian motion and winding
  theory.

## Mathematical acceptance criteria

- Define the process without Cartesian primitives or a pre-existing state
  path.
- Prove \(d|\mathcal Z_t|/|\mathcal Z_t|=\mu\,dt+\sigma\,dW_t\).
- Derive \(\Theta_t=\Theta_0+\omega t+\beta W_t\).
- Derive the complete complex Itô drift
  \(\mu-\beta^2/2+i(\omega+\sigma\beta)\).
- Reconcile ordinary exponential, exact transition, stochastic logarithm, and
  Doléans exponential.
- Derive transition laws, selected exact moments, and both complex brackets.
- Prove the rank-one log-polar covariance result.
- Recover Phase 3 through
  \(\beta=\gamma\sigma\) and
  \(\omega=\gamma(\mu-\sigma^2/2)\).
- Derive the independent two-driver comparator and explain the missing cross
  drift.
- Keep quadratic variation, finite increments, and complex algebra distinct.

## Computational acceptance criteria

- Use the unmodified `phase3-paper` conda environment.
- Import the tested root `phase4_model.py`; do not duplicate core formulas.
- Use deterministic seeds and record package versions.
- Generate all figures and tables through the notebook builder.
- Execute the notebook twice from clean kernels with zero error outputs and
  matching deterministic outputs.
- Validate exact identities at floating-point tolerance.
- Report Monte Carlo standard errors and standardized residuals.
- Demonstrate rank one versus rank two numerically.
- Estimate Euler--Maruyama strong convergence on shared Brownian paths.
- Validate bilinear and Hermitian quadratic-variation formulas.

## Publication acceptance criteria

- Render Phase 3 successfully after relocation.
- Render Phase 4 to PDF and HTML through Quarto.
- Use vector figures in PDF and raster companions in HTML.
- Provide nonempty figure alt text.
- Resolve every citation and cross-reference.
- Use letter-size PDF pages with embedded fonts.
- Inspect all PDF pages for clipping, overlap, blank pages, and unreadable
  labels.
- Validate local HTML links and image sources.
- Preserve reproducibility manifests and retained TeX output.

## Review acceptance criteria

- Obtain an independent OpenCode GLM 5.2 mathematical, numerical, literature,
  and editorial review.
- Record the `agent-usage` usage ID and `llm-scorecard` evaluation ID.
- Resolve every critical or major finding and all in-scope reproducibility,
  accessibility, and broken-link findings.

## Prohibited actions

- Do not mutate the conda environment or install packages.
- Do not inspect or expose credentials or secrets.
- Do not delegate implementation to another agent.
- Do not use Copilot, `agy`, or Grok.
- Do not alter `critique2.md`.
- Do not claim unsupported novelty.
- Do not push, merge, release, or publish unless the user separately asks.
