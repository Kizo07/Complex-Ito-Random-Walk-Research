# TASK-005 — Phase 4 coordinate-free complex GBM

## Status

Complete.

## Risk tier

Tier 2: substantive stochastic-calculus research with executable simulations
and cross-document mathematical claims.

## Authorization

The user approved `PHASE_4_COORDINATE_FREE_COMPLEX_GBM_PLAN.md` by directing
Codex to start implementation. The repository records a user-authorized
Codex-direct implementation exception. No implementation work may be
delegated. OpenCode with `zai-coding-plan/glm-5.2` is reserved for an
independent review after Codex completes the derivations and verification.

## Objective

Construct and validate a native complex exponential process

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right)
\]

whose modulus is exactly a geometric Brownian motion and whose imaginary
exponent produces deterministic and stochastic rotation, without defining the
model through Cartesian coordinate processes or a pre-existing state path.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

## Expected deliverables

- `PHASE_4_COORDINATE_FREE_COMPLEX_GBM_PLAN.md`
- `PHASE_4_LITERATURE_REVIEW.md`
- `13_COORDINATE_FREE_COMPLEX_GBM.md`
- `14_COMPLEX_LOG_DRIVER_AND_STOCHASTIC_EXPONENTIAL.md`
- `15_PHASE_4_EQUIVALENCE_RANK_AND_LIMITS.md`
- `phase4_model.py`
- `tests/test_phase4_model.py`
- `notebooks/build_phase4_coordinate_free_complex_gbm.py`
- `notebooks/phase4_coordinate_free_complex_gbm.ipynb`
- `PHASE_4_SIMULATION_RESULTS.md`
- `PHASE_4_SYNTHESIS.md`
- `.agent/reviews/TASK-005-opencode-glm52-review.md`
- updates to `README.md`, `.agent/status.md`, `.agent/handoff.md`, and
  `.agent/state.json`

## Mathematical acceptance criteria

- Define the complex process directly from \(W_t\), parameters, and
  \(\mathcal Z_0\), with no defining Cartesian coordinate processes.
- Prove that \(R_t=|\mathcal Z_t|\) satisfies
  \(dR_t/R_t=\mu\,dt+\sigma\,dW_t\).
- Derive the unwrapped phase
  \(\Theta_t=\Theta_0+\omega t+\beta W_t\).
- Derive the complex Itô SDE, including its full complex drift correction.
- Reconcile the ordinary exponential, exact-step, and Doléans stochastic
  exponential forms.
- Derive log-polar covariance, both complex brackets, transition laws, and
  selected exact moments.
- Recover the Phase 3 fixed logarithmic spiral as a constrained parameter
  subfamily.
- State and demonstrate the one-driver rank-one limitation and the
  independent two-driver boundary.
- Keep \(d[W,W]_t=dt\) distinct from an ordinary finite-increment identity and
  from \(i^2=-1\).
- Make no unsupported novelty claim.

## Computational acceptance criteria

- Use the existing `phase3-paper` conda environment without mutation.
- Develop the computational core test-first and retain the red/green evidence.
- Use deterministic random seeds and record package versions.
- Execute the notebook top-to-bottom from a clean kernel with saved outputs.
- Verify exact pathwise modulus, phase, transition, and Phase 3 equivalence
  identities at strict floating-point tolerances.
- Verify constant-modulus stochastic rotation with the required Itô drift and
  demonstrate failure when that drift is omitted.
- Compare analytic moments with Monte Carlo estimates and standard errors.
- Verify log-polar rank one numerically and contrast it with a rank-two,
  two-driver control.
- Estimate Euler--Maruyama strong convergence across at least four step sizes
  on shared Brownian paths.
- Execute a second clean notebook run to `/tmp`, check for zero error outputs,
  and compare deterministic text outputs.
- Render the authoritative Markdown files with Pandoc and run
  `git diff --check`.
- Obtain an independent OpenCode GLM 5.2 review and resolve every critical or
  major finding.

## Prohibited actions

- No package installation or conda-environment mutation.
- No credential or secret access.
- No writes outside the project.
- No implementation delegation, Copilot calls, `agy` calls, or Grok calls.
- No commit, push, pull request, merge, release, or publication unless the
  user separately requests it.
