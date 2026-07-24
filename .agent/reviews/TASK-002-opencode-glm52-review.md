# TASK-002 Independent Mathematical Review (opencode GLM 5.2)

Reviewer: opencode running `zai-coding-plan/glm-5.2` (second opinion only).
Role: independent read-only mathematical reviewer. No implementation, no
delegation, no secret access, no edits to derivation files.
Date: 2026-07-23.
Files reviewed: `06_COMPLEX_QUADRATIC_VARIATION.md`,
`07_STOCHASTIC_RADIUS_AND_PLANAR_EXPONENTIAL.md`,
`08_GENERAL_COMPLEX_DIFFUSIONS.md`, `09_DISCRETE_COMPLEX_RANDOM_WALK.md`,
`PHASE_2_PLAN.md`, `PHASE_2_LITERATURE_REVIEW.md`,
`PHASE_2_SIMULATION_RESULTS.md`, `PHASE_2_SYNTHESIS.md`, and the saved
source + outputs of `notebooks/phase2_stochastic_radius.ipynb`
(via `notebooks/build_phase2_notebook.py`).

## Verdict

**PASS.** No critical, major, or minor mathematical errors were found. Every
central formula was independently re-derived, every origin/localization
assumption is stated, the two quadratic-variation conventions are kept
distinct, the discrete-to-continuous bridge is rigorous, the general-covariance
polar SDEs are correct, and every numerical conclusion in
`PHASE_2_SIMULATION_RESULTS.md` / `PHASE_2_SYNTHESIS.md` matches the notebook's
saved outputs to the precision reported. The items below are optional
clarifications / process observations only; none affect any mathematical claim
or any embedded notebook assertion.

## Findings (findings-first)

### Errors: none

No errors of any severity were identified in 06–09, the three Phase 2 reports,
or the notebook.

### Optional clarifications (informational, not required for correctness)

**C1 — One angular-variance bin shows a large-sample z-score (informational).**
`notebooks/phase2_stochastic_radius.ipynb` cell 11, radius bin `[0.65,0.90)`:
observed angular variance rate `0.399457` vs predicted `σ²/R² = 0.400483`,
`z = -3.093`. This is a large-sample standard-error artifact, not a model
failure: the bin holds ~3.0M retained increments so the standard error is
~3.3e-4, and the actual relative deviation is only 0.26%. All other bins sit
within |z| < 1.1, and no assertion depends on this z-score. `PHASE_2_SIMULATION_RESULTS.md`
does not quote this single z, which is fine; a one-line footnote would prevent
a future reader from misreading -3.093 as a contradiction.

**C2 — Itô-compensator convergence rate is expected to be O(√h), not a defect.**
In the anisotropic experiment the continuous Itô compensator converges with
slope `0.5036` against `h` (cell 15), i.e. O(h^{1/2}), while the realized
Taylor-2 correction achieves `0.9864`, i.e. O(h). Both are exactly what theory
predicts: the deterministic compensator is a left-Riemann approximation of
`∫dt/Z²` dominated by martingale fluctuation (strong O(√h)), whereas the
realized `Σ q_n²` tracks the pathwise quadratic variation (O(h)). The reports
state both rates correctly and do not overclaim; this note only records why the
two slopes legitimately differ.

### Process observations (non-mathematical, for Codex's coordination only)

**P1 — "Execute twice from clean kernels" is only evidenced by one saved run.**
`TASK-002.md` (Numerical acceptance criteria) and `PHASE_2_PLAN.md` (§14, gate 4)
require a second clean-kernel execution. The saved notebook shows exactly one
clean top-to-bottom execution (code cells carry execution counts 1–8 with no
error outputs), and `PHASE_2_SIMULATION_RESULTS.md` documents only the primary
`nbconvert --execute --inplace` command. `.agent/state.json` still records
`last_test_result: "not_run"` and no Phase-2 recheck artifact (e.g. a
`/tmp/..._recheck.ipynb`, which the Phase-1 handoff used) is present. Recommend
documenting the second execution to close the gate. The single saved execution
is itself fully consistent.

**P2 — Coordination deliverables not yet finalized for TASK-002.**
`.agent/handoff.md` and `.agent/status.md` still contain TASK-001 (Phase 1)
content ("ito_complex_bridge.ipynb", TASK-001 outcome). `README.md` and
`.agent/state.json` have been updated for Phase 2. The task contract lists
status/handoff updates as deliverables; this is a bookkeeping item, not a
mathematical defect.

## What was independently verified (evidence)

### Central formulas (independently re-derived)

- **Two quadratic variations** (`06` §1–2): `d[Z,Z] = d[X,X] - d[Y,Y] + 2i d[X,Y]`
  and `d[Z,\bar Z] = d[X,X] + d[Y,Y]` follow from complex-bilinear extension.
  For `dZ = σ(dW¹ + i dW²)`: `d[Z,Z] = σ²(dt - dt + 0) = 0`,
  `d[Z,\bar Z] = 2σ²dt`. Confirmed.
- **Complex self-QV rate** (`06` §3): `q = Σ_k γ_k² = C₁₁ - C₂₂ + 2i C₁₂`,
  with `γ_k = Σ₁ₖ + iΣ₂ₖ`, and `d[Z,\bar Z]/dt = tr C = Σ|γ_k|²`. Confirmed
  term-by-term. `d[Z,Z]=0 ⇔ C₁₁=C₂₂, C₁₂=0` (conformal/isotropic case).
- **Holomorphic Itô / complex log** (`06` §4–5): `df = f'dZ + ½ f'' d[Z,Z]`;
  with `f=log`, `d log Z = dZ/Z - ½ d[Z,Z]/Z²`, on `[0,τ_ε]`. Confirmed.
- **Radial SDE** (`07` §3): `∇r = e_r`, `Δr = 1/r` ⇒ `dR = σ²/(2R) dt + σ dB^R`.
  Confirmed via 2D Itô.
- **Angular SDE** (`07` §4): `∇θ = e_θ/r`, `Δθ = 0` ⇒ `dΘ = (σ/R) dB^Θ`.
  Orthogonal adapted rotation ⇒ `d[B^R,B^R]=d[B^Θ,B^Θ]=dt`, `d[B^R,B^Θ]=0`;
  Lévy characterization ⇒ `(B^R,B^Θ)` is 2D Brownian. Confirmed.
- **Log-radius** (`07` §5): `d log R = (σ/R) dB^R` (Bessel drift cancels with
  the Itô term). Confirmed, correctly flagged as a local-martingale statement.
- **Cartesian reconstruction** (`07` §8): Itô on `Z = R e^{iΘ}` gives
  `dZ = e^{iΘ}dR + iR e^{iΘ}dΘ + i e^{iΘ}d[R,Θ] - ½ R e^{iΘ}d[Θ,Θ]`; with
  `d[R,Θ]=0`, `d[Θ,Θ]=σ²/R² dt` the drifts cancel and
  `e^{iΘ}(dB^R + i dB^Θ) = dW¹ + i dW²`. Confirmed algebraically.
- **General covariance polar SDEs** (`08` §2–4): Hessians
  `∇²R = (1/R)(I - e_r e_rᵀ)`, `∇²Θ = -(1/R²)(e_r e_θᵀ + e_θ e_rᵀ)`,
  `∇²(log R) = (1/R²)(I - 2 e_r e_rᵀ)` all verified by direct
  second-derivative computation. Resulting
  `dR = [e_r·b + (tr C - e_rᵀCe_r)/(2R)]dt + e_rᵀΣ dW`,
  `dΘ = [(e_θ·b)/R - (e_rᵀCe_θ)/R²]dt + (e_θᵀΣ/R)dW`,
  `dA = [(e_r·b)/R + (tr C - 2e_rᵀCe_r)/(2R²)]dt + (e_rᵀΣ/R)dW`. Confirmed.
- **Polar covariance rank** (`08` §5): `det K = det C / R⁴`. Confirmed
  (determinant is basis-invariant in `{e_r,e_θ}`). Rank-one Cartesian noise
  ⇒ rank-one polar noise; coordinates cannot manufacture a second driver.
- **Amplitude-phase cross-check** (`08` §6): the Phase-1 identity
  `dZ/Z = [a+½(‖u‖²-‖v‖²)+i(ω+u·v)]dt + (u+iv)·dW` collapses to
  `(e_r·b + i e_θ·b)/R dt + (u+iv)·dW` because
  `(tr C - 2e_rᵀCe_r)/(2R²) + (e_rᵀCe_r - e_θᵀCe_θ)/(2R²) = 0`. Confirmed.
- **Discrete-to-continuous** (`09` §2–5): exact finite step
  `Z_{n+1} = Z_n exp(Log_cont(1 + ΔZ_n/Z_n))`; local expansion
  `Δlog Z_n = q_n - ½ q_n² + O_p(h^{3/2})`; `Σq_n → ∫dZ/Z`,
  `Σq_n² → ∫d[Z,Z]/Z²` (predictable-integrand quadratic-variation convergence,
  valid since `1/Z²` is bounded on localized paths); accumulated cubic
  remainder is `O_p(√h) → 0`. Confirmed. The isotropic cancellation
  `Σ(ΔZ)² → 0` and the explicit "a single finite square is not zero" caveat
  are both correct.

### Assumptions at the origin / localization

- `Z₀ ≠ 0` assumed; `τ_ε = inf{t: |Z_t| ≤ ε}` defined; identities stated on
  `[0,τ_ε]`; starting exactly at the origin treated as a separate boundary case
  (`07` §11, `08` §1, `09` §9). 2D Brownian started away from 0 a.s. does not
  hit 0 (points are polar) — correctly stated and cited (Pitman–Yor guide).
- `log R` correctly described as a local martingale only; no global
  true-martingale claim made without integrability (`07` §5).

### Quadratic-variation conventions

- `[Z,Z]` (complex-bilinear, not positive) is never conflated with
  `[Z,\bar Z]` (Euclidean, nonnegative). The `(dW¹ + i dW²)² = 0` identity is
  attributed to the `i² = -1` cancellation between two independent equally-scaled
  coordinates, explicitly distinguished from the 1D mnemonic `(dW)² = dt`
  (`06` §2, `PHASE_2_SYNTHESIS.md` §4, §10 "Not claimed").

### Discrete-to-continuous claims

- Exact finite-step multiplicative identity vs. Itô limit cleanly separated
  (`09` §11 classification table). Branch/unwrapping handling and grid stopping
  `ν_ε` described (`09` §8–9).

### Numerical conclusions vs. saved notebook outputs

Extracted every `stream` output from `phase2_stochastic_radius.ipynb` (8 code
cells, execution counts 1–8, zero error outputs) and cross-checked each number
in `PHASE_2_SIMULATION_RESULTS.md`:

- QV table (`06`/sim §1): N=64/256/1024/4096 rows for Re/Im self-QV means and
  energy means match the notebook exactly (e.g. `0.979869, 0.979682, 0.979403,
  0.979940` vs target `2σ²T = 0.98`). Self-QV RMS log-log slope `-0.5010`
  matches theory `-0.5`. Variance ratios span `0.9779–1.0111` (report says
  `≈0.978–1.011`). Independently confirmed `Var(Re Σ(ΔZ)²) = 4σ⁴T²/N`.
- Rice law (sim §2): `b = |Z₀|/(σ√T) = 1.512603`, `scale = 0.712039`,
  `E[R²] = |Z₀|² + 2σ²T = 2.174` all re-derived independently; MC/theory/KS
  (`0.001589`, `1.36/√150000 = 0.003512`, `p = 0.8428`) match.
- Pathwise reconstruction (sim §3): max error `4.578e-16`, adapted grid QVs
  `[0.986288, 1.015184, -0.008828]` (≈ unit horizon, orthogonal) match.
- Random clock (sim §4): QV(Θ)/H, QV(log R)/H ≈ 1.000, cross/H ≈ 0 across
  N=250/1000/4000 match; radius-binned angular rates `0.822970 … 0.076857`
  vs predicted `σ²/R²` match (ratio `10.7×`, "more than ten times").
- Bessel drift (sim §5): z-scores `-0.924 … 1.131` over 14,155,754 retained
  increments (report: "more than 14 million") match.
- Isotropic log reconstruction (sim §6): first-order errors and Taylor-2 errors
  match; slopes `0.5007` / `0.9949`; exact-log product error ≤ `9.03e-15`
  (≈ `10⁻¹⁴`). Match.
- Anisotropic counterexample (sim §7): `[Z,Z]_T = (σ_x²-σ_y²)T = 0.288`,
  finest mean `0.288231` (`z = 1.707`); uncorrected error flat ≈ `0.0366`
  (does not decrease); corrected errors match; slopes Taylor-2 `0.9864`,
  Itô `0.5036`. All re-derived and confirmed.

### Literature review

`PHASE_2_LITERATURE_REVIEW.md` correctly separates project derivations
(`06`/`08` formulas) from cited authorities (Pitman–Yor 1986 skew-product,
Pitman–Yor guide for polarity/continuous winding/complex-log identity,
Larsson–Ruf and Černý–Ruf for stochastic exponentials near zeros, SciPy Rice,
Higham 2001 for SDE numerics). The subtle point that zero cross-variation does
not by itself imply independence (the skew-product independence is a separate
theorem) is stated correctly in both `07` §9 and the literature review.

## Independence and scope notes

This review is a second opinion only. Codex owns mathematical acceptance and
performed all implementation. No implementation, file edits, delegation
(`agy`/Copilot/Grok), credential access, or network writes occurred. Only this
review file was written, under the allowed project path. Monte Carlo values
support but do not replace the derivations, per project standards.
