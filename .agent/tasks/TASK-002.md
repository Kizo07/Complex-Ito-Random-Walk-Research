# TASK-002 — Stochastic radius and full complex Brownian motion

## Risk tier

Tier 2: substantive mathematical implementation with executable simulations.

## Authorization

The user approved `PHASE_2_PLAN.md` and retained the Codex-direct exception for
this session. Codex performs all implementation. No work is delegated.
opencode with GLM 5.2 is reserved for independent review after implementation.

## Objective

Extend the Phase 1 circle-valued stochastic phase into a genuinely
two-dimensional complex diffusion with stochastic radius and angle.

The implementation must:

1. distinguish \([Z,Z]\) from \([Z,\overline Z]\);
2. derive the stochastic logarithm and exponential reconstruction of planar
   Brownian motion;
3. prove that one real Brownian driver cannot generate a full-rank planar
   diffusion;
4. derive the polar SDE for a general planar covariance matrix;
5. connect exact discrete complex random-walk steps to the continuous
   stochastic logarithm;
6. verify the main claims in a reproducible Jupyter notebook.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

## Expected deliverables

- `06_COMPLEX_QUADRATIC_VARIATION.md`
- `07_STOCHASTIC_RADIUS_AND_PLANAR_EXPONENTIAL.md`
- `08_GENERAL_COMPLEX_DIFFUSIONS.md`
- `09_DISCRETE_COMPLEX_RANDOM_WALK.md`
- `notebooks/phase2_stochastic_radius.ipynb`
- `PHASE_2_SIMULATION_RESULTS.md`
- `PHASE_2_LITERATURE_REVIEW.md`
- `PHASE_2_SYNTHESIS.md`
- `.agent/reviews/TASK-002-opencode-glm52-review.md`
- updates to `README.md`, `.agent/status.md`, `.agent/handoff.md`, and
  `.agent/state.json`

## Mathematical acceptance criteria

- Use the convention
  \(dZ=\sigma(dW^1+i\,dW^2)\) and state its normalization.
- Derive
  \[
  dR=\frac{\sigma^2}{2R}dt+\sigma dB^R,\qquad
  d\Theta=\frac{\sigma}{R}dB^\Theta.
  \]
- Derive \(d\log R=(\sigma/R)dB^R\) under localization.
- Verify that \(B^R,B^\Theta\) form a two-dimensional Brownian motion.
- Derive
  \[
  d\log Z=\frac{dZ}{Z}-\frac12\frac{d[Z,Z]}{Z^2}.
  \]
- For isotropic planar Brownian motion, verify
  \([Z,Z]=0\), \([Z,\overline Z]=2\sigma^2t\), and
  \[
  Z_t=Z_0\exp\!\left(\int_0^t\frac{dZ_s}{Z_s}\right).
  \]
- Derive the general covariance polar formulas in `PHASE_2_PLAN.md`.
- Explain rank-one versus rank-two noise without conflating state dimension
  with Brownian-driver dimension.
- Localize all logarithmic and polar arguments away from the origin.
- Distinguish exact finite-step identities from Itô limits.

## Numerical acceptance criteria

- Use deterministic seeds and the existing conda `base` environment.
- Compare Cartesian and polar reconstruction on shared paths.
- Verify radial second moments and the Rice/noncentral-chi law.
- Compare angular quadratic variation with the random clock.
- Demonstrate convergence of stochastic-logarithm reconstruction.
- Verify \(\sum(\Delta Z)^2\to0\) while
  \(\sum|\Delta Z|^2\to2\sigma^2T\).
- Use anisotropic volatility to show a nonzero complex self-quadratic
  variation and the necessity of its logarithmic correction.
- Report Monte Carlo uncertainty or pathwise error metrics as appropriate.
- Execute twice from clean kernels without cell errors.

## Prohibited actions

- No package installation or conda-environment mutation.
- No credential or secret access.
- No writes outside the project.
- No publishing, cloud upload, or Git history changes.
- No implementation delegation and no Grok calls.
