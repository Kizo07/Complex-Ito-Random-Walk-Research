# TASK-001 — Foundations, stochastic exponential, and simulation baseline

## Risk tier

Tier 2: substantive mathematical implementation with executable simulations.

## Objective

Implement the first reproducible research unit from `RESEARCH_PLAN.md`:

1. derive the Itô table from scaled random-walk/quadratic-variation limits;
2. compare arithmetic diffusion, geometric Brownian motion, and stochastic
   complex rotation;
3. preserve analytical and Monte Carlo checks in an executed Jupyter notebook;
4. prepare a bounded literature-review scaffold using only verifiable sources.

## Required orchestration

Superseded on 2026-07-23 by the user's explicit Codex-direct exception. Codex
performs the implementation and verification. opencode with GLM 5.2 is used
only after implementation as an independent reviewer/second opinion. No
implementation worker is to be started.

## Allowed writes

Only under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

## Expected files

- `01_ITO_ALGEBRA.md`
- `02_ARITHMETIC_DIFFUSION.md`
- `03_STOCHASTIC_EXPONENTIAL.md`
- `04_STOCHASTIC_POLAR_FORM.md`
- `LITERATURE_REVIEW.md`
- `notebooks/ito_complex_bridge.ipynb`
- generated figures only under `figures/`, if the notebook needs external files
- `.agent/status.md`
- `.agent/handoff.md`
- `.agent/reviews/TASK-001-opencode-review.md`

Do not overwrite `RESEARCH_PLAN.md` except to correct a demonstrable
mathematical error, and document any such correction.

## Mathematical requirements

### Itô algebra

- Begin with `Delta W_k = sqrt(Delta t) xi_k`.
- Separate the facts
  `E[(Delta W)^2] = Delta t`,
  concentration of accumulated squared increments, and Brownian quadratic
  variation.
- Explain the order bookkeeping behind
  `(dt)^2 = dt dW = 0` and `(dW)^2 = dt`.
- Compare the Itô table with `i^2 = -1` without identifying `dW` with `i`.
- Discuss the formal truncated/nilpotent algebra carefully and label it as a
  mnemonic model rather than the definition of stochastic calculus.

### Arithmetic and multiplicative diffusions

- Derive
  `X_t = X_0 + mu t + sigma W_t`.
- Derive its transition distribution and first two moments.
- Derive geometric Brownian motion with Itô's lemma:
  `S_t = S_0 exp((mu - sigma^2/2)t + sigma W_t)`.
- Derive the local Itô exponential expansion.
- State the continuous stochastic-exponential formula and its assumptions.

### Stochastic rotation

- Derive
  `Z_t = r_0 exp(i(theta_0 + omega t + beta W_t))`.
- Derive its Itô SDE:
  `dZ_t = (i omega - beta^2/2) Z_t dt + i beta Z_t dW_t`.
- Independently verify `d|Z_t|^2 = 0`, including the quadratic covariation
  term.
- Explain why dropping `-beta^2 Z_t dt / 2` from an Itô discretization causes
  radial growth.
- Clearly distinguish Itô and Stratonovich forms.

## Notebook experiments

Use an existing conda environment, selected after inspecting available
environments. Record Python, NumPy, Matplotlib, and Jupyter versions.

The executed notebook must include:

1. **Quadratic variation**
   - simulate Brownian paths at multiple partition sizes;
   - estimate `sum (Delta W)^2`;
   - compare mean and variance with exact finite-grid values;
   - demonstrate convergence toward the horizon `T`.

2. **Arithmetic diffusion**
   - compare empirical terminal mean and variance with
     `X_0 + mu T` and `sigma^2 T`;
   - report Monte Carlo standard errors or confidence intervals.

3. **Geometric Brownian motion**
   - compare exact sampling with Euler-Maruyama;
   - compare empirical moments with analytic moments;
   - estimate strong or coupled terminal error for at least two step sizes.

4. **Stochastic rotation**
   - compare the exact phase solution, Euler-Maruyama for the correct Itô SDE,
     and Euler-Maruyama after incorrectly omitting the Itô drift;
   - measure modulus error and show radial growth in the incorrect scheme;
   - explain finite-step Euler error in the correct scheme.

Use deterministic seeds. Keep the total Monte Carlo size and grid sizes
reasonable for local execution.

## Literature-review scaffold

Create a concise `LITERATURE_REVIEW.md` organized around:

- Brownian quadratic variation and Itô's formula;
- Doléans-Dade/stochastic exponentials;
- complex or planar Brownian motion in polar coordinates;
- Brownian motion on the circle / stochastic phase;
- Itô versus Stratonovich geometry.

Do not invent titles, authors, dates, DOIs, or URLs. It is acceptable to leave
clearly marked source slots for Codex to fill after independent web
verification. Prefer primary papers, books, or authoritative lecture notes.

## Acceptance criteria

- All expected derivation files exist and agree with each other.
- The notebook executes from a clean kernel with no errors.
- Saved notebook outputs contain the reported numerical evidence.
- No claim equates pointwise `(dW)^2` with `dt`.
- The stochastic-rotation drift sign is correct and its constant modulus is
  verified twice.
- opencode records review findings with file references and identifies any
  remaining uncertainty.
- `.agent/status.md` records the conda environment, execution command, result,
  and changed files.

## Verification commands

The worker should determine the available conda environment and use an
equivalent of:

`conda run -n ENV jupyter nbconvert --to notebook --execute --inplace notebooks/ito_complex_bridge.ipynb`

Then perform a second clean execution to a temporary output path or use
`nbclient` to confirm reproducibility.

## Prohibited actions

- No package installation or conda-environment mutation.
- No credential or secret access.
- No writes outside the project.
- No Git history changes, pushes, publishing, or cloud uploads.
- No Grok calls.
