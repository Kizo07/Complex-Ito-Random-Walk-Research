# TASK-003 — One-driver stochastic radius and model equivalence

## Status

Complete. All mathematical and numerical acceptance criteria passed; the
independent opencode GLM 5.2 review found no unresolved error.

## Risk tier

Tier 2: substantive mathematical implementation with executable simulations.

## Authorization

The user approved `PHASE_3_PLAN.md` and retained the Codex-direct exception
recorded in `AGENTS.md`. Codex performs all implementation. No work is
delegated. opencode with GLM 5.2 is reserved for independent review after
implementation.

## Objective

Resolve the dimensional concern raised in
`complex_brownian_motion_critique.md` without discarding the valid Phase 2
planar theory.

The implementation must:

1. distinguish a deterministic complex image of scalar arithmetic Brownian
   motion from genuine planar Brownian motion;
2. construct an injective one-driver logarithmic-spiral representation with
   stochastic radius and angle;
3. derive its Itô equation, quadratic variations, exact moments, and exact
   finite-step random-walk formula;
4. prove the rank-one obstruction for every smooth map
   \(F:\mathbb R\to\mathbb C\);
5. treat the literal real-axis polar form at zero using stopping and Tanaka
   local time;
6. verify the claims in a reproducible Jupyter notebook.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

## Expected deliverables

- `10_SCALAR_POLAR_FORM_AND_ZERO_CROSSINGS.md`
- `11_ONE_DRIVER_LOGARITHMIC_SPIRAL.md`
- `12_EMBEDDING_RANK_AND_MODEL_EQUIVALENCE.md`
- `PHASE_3_LITERATURE_REVIEW.md`
- `notebooks/build_phase3_notebook.py`
- `notebooks/phase3_one_driver_complex_embedding.ipynb`
- `PHASE_3_SIMULATION_RESULTS.md`
- `PHASE_3_SYNTHESIS.md`
- `.agent/reviews/TASK-003-opencode-glm52-review.md`
- updates to `README.md`, `.agent/status.md`, `.agent/handoff.md`, and
  `.agent/state.json`

## Mathematical acceptance criteria

- Use one and only one Brownian driver for the Phase 3 central model.
- For \(c=\alpha+i\beta\), derive
  \[
  Z_t=Z_0e^{c(X_t-X_0)}
  \]
  and
  \[
  \frac{dZ_t}{Z_t}
  =
  \left(c\mu+\frac12c^2\sigma^2\right)dt+c\sigma dW_t.
  \]
- Derive the rank-one covariance of \((\log R,\Theta)\), including its
  cross-variation.
- Prove that a deterministic \(C^2\) image of a scalar diffusion has
  Cartesian covariance rank at most one.
- Distinguish state injectivity from recovery through an unwrapped phase.
- Use \(\log|X|\) rather than \(\log X\) for negative scalar states.
- Treat scalar zero crossings with Tanaka's formula and local time.
- Derive both \([Z,Z]\) and \([Z,\overline Z]\).
- Preserve the Phase 2 rank-two planar result as a distinct model.

## Numerical acceptance criteria

- Use deterministic seeds and the existing conda `base` environment.
- Verify direct-map, inverse-radius, and exact-product identities pathwise.
- Check analytic radial and complex moments with Monte Carlo standard errors.
- Demonstrate rank-one polar covariance against rank-two planar covariance.
- Estimate Euler–Maruyama strong convergence over at least four step sizes.
- Verify a discrete Tanaka formula with exact grid local-time residual and
  show convergence of an occupation-density approximation.
- Execute the notebook twice from clean kernels without errors.

## Prohibited actions

- No package installation or conda-environment mutation.
- No credential or secret access.
- No writes outside the project.
- No implementation delegation and no Grok calls.
- No Git commit, push, or publication without a separate user request.
