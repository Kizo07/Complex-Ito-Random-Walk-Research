# TASK-007 — Comprehensive Phase 5 one-phase Euler research

## Status

Completed on 2026-07-24.

## Risk tier

Tier 4 research and mathematical implementation. The task includes
measure-theoretic proofs, stochastic-calculus derivations, primary-source
research, a tested numerical model, a reproducible notebook, numerical PDE and
SDE benchmarks, and an implications assessment.

## Authorization

The user approved
`PHASE_5_COMPREHENSIVE_ONE_PHASE_EULER_RESEARCH_PLAN.md` and instructed Codex
to continue until the implementation is complete. The standing Codex-direct
exception applies. Implementation must not be delegated. OpenCode
`zai-coding-plan/glm-5.2` is reserved for independent review and second opinion
after Codex completes its own implementation and verification.

## Objective

Determine rigorously when

\[
Z_t=Z_0+a t+bW_t
\]

admits a lossless time-independent representation

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t}
\]

with one stochastic phase, reconcile the supplied secant, Cayley, wrapped,
spiral, arbitrary-curve, and moving-line candidates, and establish what the
representation does and does not contribute to vector stochastic calculus,
complex differentiation, analytic solvability, and numerical methods.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

Temporary validation artifacts may be written under `/tmp`.

## Required deliverables

- `PHASE_5_CANDIDATE_AUDIT.md`
- `PHASE_5_LITERATURE_REVIEW.md`
- `PHASE_5_MATHEMATICAL_FOUNDATIONS.md`
- `PHASE_5_RIGIDITY_AND_GROUP_STRUCTURE.md`
- `PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md`
- `PHASE_5_NUMERICAL_IMPLICATIONS.md`
- `phase5_model.py`
- `tests/test_phase5_model.py`
- `notebooks/build_phase5_one_phase_euler.py`
- `notebooks/phase5_one_phase_euler.ipynb`
- generated Phase 5 figures and evidence tables
- `PHASE_5_SIMULATION_RESULTS.md`
- `PHASE_5_SYNTHESIS.md`
- `.agent/reviews/TASK-007-opencode-glm52-review.md`

## Core acceptance gates

- Audit every substantive claim in the three supplied candidate documents.
- Establish the correct measurable factorization criterion.
- Give a gap-free additive affine existence and impossibility theorem.
- Verify the exact angular domain, inverse, phase dynamics, generator,
  transition kernel, semigroup, and boundary behavior.
- Complete the Cayley, group, logarithmic-spiral, and corrected rigidity
  analyses.
- Distinguish Borel state maps from maps regular enough for Itô calculus.
- Use primary sources and a claim-to-source matrix.
- Implement the model test-first and preserve the red/green evidence.
- Execute the notebook twice from clean kernels with deterministic evidence.
- Benchmark vector, complex-derivative, PDE, SDE, and Monte Carlo implications
  against matched scalar baselines and negative controls.
- Do not call a coordinate change a new stochastic dimension, analytical
  solution, or numerical improvement without proof or measured evidence.
- Obtain and resolve an independent OpenCode GLM 5.2 review.

## Prohibited actions

- Do not modify the supplied candidate or critique documents.
- Do not alter completed Phase 3 or Phase 4 mathematical artifacts.
- Do not mutate or install into a conda environment.
- Do not delegate implementation to `agy`, Copilot, Grok, a subagent, or any
  other worker.
- Do not inspect or expose credentials or secrets.
- Do not commit, push, open a pull request, merge, publish, or release unless
  separately requested.

## Outcome

All required deliverables and acceptance gates are complete. The exact
time-independent genuine one-phase representation for
\(Z_t=Z_0+a t+bW_t\), with \(Z_0b\ne0\), exists if and only if
\(a/b\in\mathbb R\) and \(b/Z_0\notin\mathbb R\). The phase SDE, generator,
transition kernel, natural boundaries, inverse, group law, Cayley alternative,
moving-line fallback, and compatible multiplicative spiral are derived and
implemented. The vector, complex-calculus, and numerical claims were tested
against matched controls and conservatively classified.

## Final verification

- 23/23 focused Phase 5 tests pass.
- 33/33 tests pass in the full project suite.
- `phase5_model.py` and the deterministic notebook builder compile.
- Three post-review clean-kernel notebook executions had 18 sequential code
  cells, zero errors, and byte-identical 33-file evidence bundles.
- Two consecutive unexecuted notebook builds were byte-identical.
- The final artifact set contains 18 raster and 18 vector figures.
- Ordered relative-name evidence SHA-256:
  `fa8fd5f517c9f321f3426cfdbd5fe2e9f8bea4e213ad945a8207a87a9736619e`.
- Verification details are preserved in
  `.agent/evidence/TASK-007-verification.md`.

## Independent review

OpenCode `zai-coding-plan/glm-5.2` found no critical or major defect. Six
minor rigor/provenance refinements were corrected, and the focused final
re-review returned `PASS` with no residuals.

- Usage ID: `02b1ddc2-d429-4f87-be6d-a3cf873b8c32`
- Scorecard evaluation ID: `ca7b1eca-19a4-41e1-92e5-565ccc78c595`
- Review: `.agent/reviews/TASK-007-opencode-glm52-review.md`
