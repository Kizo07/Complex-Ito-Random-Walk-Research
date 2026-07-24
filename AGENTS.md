# Project Agent Rules

## Roles

- Codex owns scope, source selection, mathematical acceptance, and final review.
- The user authorized a Codex-direct implementation exception on 2026-07-23.
- opencode with GLM 5.2 is used only for independent review/second opinions.
- Do not delegate implementation to `agy` or any other worker in this session.
- External-agent claims are provisional until Codex verifies them.

## Allowed scope

All writes must stay under:

`/home/fire/Documents/Complex-Ito-Random-Walk-Research`

Do not modify files elsewhere. Do not use or inspect credentials, tokens,
authentication files, browser cookies, SSH keys, certificates, or secrets.
Do not make network writes or publish artifacts.

## Mathematical standards

- Distinguish exact identities, Itô differential rules, convergence statements,
  distributional identities, and heuristics.
- Never state that an individual Brownian increment literally satisfies
  `(Delta W)^2 = Delta t`.
- State assumptions, stopping conditions, and singularities, especially for
  logarithms and polar coordinates.
- Independently check stochastic differential formulas by applying Itô's lemma.
- Use fixed random seeds for simulations and report uncertainty or Monte Carlo
  standard errors where applicable.
- Numerical experiments support but do not replace derivations.

## Notebook standards

- Use an existing conda environment; do not create or mutate environments.
- Record the selected environment and package versions in the notebook.
- The notebook must execute from top to bottom without hidden state.
- Keep runtimes moderate and make all figures reproducible.
- Save executed outputs in the notebook.
- Avoid absolute paths inside notebook code.

## Verification

- Execute the notebook from a clean kernel.
- Check analytic moments against Monte Carlo estimates.
- Check constant-modulus stochastic rotation with and without the Itô drift.
- Check numerical convergence across at least two time-step sizes.
- Review Markdown equations and generated files for internal consistency.

## Coordination

Read the active task named in `.agent/status.md` before work. The user's
direct-exception instruction supersedes any original delegation requirement.
Keep `.agent/status.md` concise. opencode writes review findings only to the
matching `.agent/reviews/TASK-NNN-opencode-glm52-review.md` file.
