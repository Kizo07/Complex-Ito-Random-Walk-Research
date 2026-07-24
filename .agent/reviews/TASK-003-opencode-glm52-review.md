# TASK-003 Independent Mathematical Review (opencode GLM 5.2)

Reviewer: opencode running `zai-coding-plan/glm-5.2` (second opinion only).
Role: independent read-only mathematical and numerical reviewer. No
implementation, no delegation, no secret access, no edits to any derivation
or state file.
Date: 2026-07-23.
Files reviewed: `AGENTS.md`, `.agent/tasks/TASK-003.md`, `.agent/status.md`,
`PHASE_3_PLAN.md`, `complex_brownian_motion_critique.md`,
`10_SCALAR_POLAR_FORM_AND_ZERO_CROSSINGS.md`,
`11_ONE_DRIVER_LOGARITHMIC_SPIRAL.md`,
`12_EMBEDDING_RANK_AND_MODEL_EQUIVALENCE.md`,
`PHASE_3_LITERATURE_REVIEW.md`, `PHASE_3_SIMULATION_RESULTS.md`,
`PHASE_3_SYNTHESIS.md`, `README.md`, `notebooks/build_phase3_notebook.py`,
and the saved source + outputs of
`notebooks/phase3_one_driver_complex_embedding.ipynb`.

Method: every central formula was re-derived from scratch (Itô's lemma,
two-dimensional Itô on `e^{A+iΘ}`, stochastic logarithm, Gaussian MGF, the
rank-one outer-product argument, Tanaka/occupation density). All exact
benchmarks were recomputed independently in a read-only script outside the
project; the recomputed values are reported below and agree with the notebook
to the precision displayed. All reported numbers in
`PHASE_3_SIMULATION_RESULTS.md` and `PHASE_3_SYNTHESIS.md` were cross-checked
against the notebook's saved outputs.

## Verdict

**PASS.** No critical, major, or minor mathematical or numerical error was
found. The one-driver logarithmic-spiral model, its Itô equation, both
complex quadratic variations, the rank-one polar covariance, the general
`rank ≤ 1` no-go theorem, the exact finite-step walk, the exact moments, and
the Tanaka/local-time treatment are all correct and internally consistent.
Every reported notebook value matches an independent recomputation of the
exact formulas and matches the saved outputs. The items below are
clarifications / observations only; none affects any mathematical claim or
any embedded assertion, and none blocks acceptance.

## Findings (findings-first)

### Errors: none

No errors of any severity were identified in `10_…`, `11_…`, `12_…`, the
three Phase 3 reports, the README Phase 3 sections, or the notebook
(source and saved outputs).

### Optional clarifications / observations (informational, not required)

**O1 — Independent confirmation of every central identity.**
Re-derivation results:

- Itô drift `cμ + ½c²σ² = (αμ + ½(α²−β²)σ²) + i(βα·… )`: with
  `μ=0.20, σ=0.65, α=0.45, β=1.10`, the split is
  `Re = −0.122834375`, `Im = +0.429137500`, matching `11` §4 and `12` §1.
- `c² = −1.0075 + 0.9900i ≠ 0`, so a nontrivial one-driver embedding cannot
  have `[Z,Z]=0` (the `c²=0 ⇒ c=0` argument is valid; ℂ has no nilpotents).
  `|c|² = 1.4125`, so `d[Z,Z̄] = |c|²σ²|Z_t|²dt` and
  `d[Z,Z] = c²σ²Z_t²dt` are both correct.
- Polar covariance `K = σ²[[α²,αβ],[αβ,β²]]` recomputed as
  `[0.08555625, 0.2091375, 0.2091375, 0.511225]`, eigenvalues
  `[0, 0.59678125]`, correlation `+1 = sgn(αβ)`. The notebook's empirical
  nonzero eigenvalue `0.5963867` differs from theory by `~3.9e-4`, exactly
  the reported relative error `6.6111e-4`. ✓
- Stochastic-logarithm self-consistency:
  `dlog Z = dZ/Z − ½ d[Z,Z]/Z² = cμdt + cσdW = c dX`, hence
  `log(Z_t/Z_0) = c(X_t−X_0)`, recovering the definition. This is a
  non-trivial internal check and it passes.

**O2 — Exact moments recomputed; all match to displayed precision.**

| Quantity | Recomputed exact | Notebook/report exact | Match |
|---|---:|---:|:--:|
| `E[R_T]` | `1.4166490` | `1.4166490` | ✓ |
| `E[R_T²]` | `2.2334193` | `2.2334193` | ✓ |
| `E|Z_T|²` | `2.2334193` (= `E[R_T²]`) | `2.2334…` (`11` §9) | ✓ |
| `E[(Z_T/Z_0)¹]` | `0.7371989+0.4383209i` | `0.7371989+0.4383209i` | ✓ |
| `E[(Z_T/Z_0)²]` | `−0.0107536+0.4319343i` | `−0.0107536+0.4319343i` | ✓ |
| Nonlinear-image `det C` | `7.058e-18` | `7.058e-18` | ✓ |
| `E[L_T^0]` (std BM) | `0.8920621` | `0.8920621` | ✓ |
| EM fitted slope (from reported errors) | `0.5028773` | `0.5029` | ✓ |
| Successive EM error ratios | `≈1.413–1.427` | `2^(1/2)=1.4142` | ✓ |

The radial/complex moment z-scores (`−0.465, −0.575, 0.484/−0.295,
0.309/−0.318`) all reproduce from the reported estimates/SEs and lie far
inside the `|z|<4.5` tolerance. Strong-order `1/2` is confirmed both by the
fitted slope and by the per-halving ratios clustering at `1/0.7071`.

**O3 — Planar contrast is correctly rank two.**
Recomputed two-driver covariance at `r=1.30` is `σ²/r²·I₂ = 0.25·I₂`
(eigenvalues `0.25, 0.25`). The notebook's empirical eigenvalues
`0.2492954, 0.2499687` bracket `0.25` within the reported relative error
`1.9950e-3`. Both components use two independent standard normals, so this is
a genuine rank-two benchmark, cleanly separated from the rank-one spiral.

**O4 — Local-time / Tanaka conventions are consistent and correctly stated.**
`10` §4–§5 fixes the symmetric local-time convention
`∫₀ᵗ g(X_s)d[X,X]_s = ∫_ℝ g(a)L_t^a da`, gives
`L_t^0 = lim_{ε↓0} (σ²/2ε)∫₀ᵗ 1_{|X_s|<ε}ds`, and explicitly names it the
"symmetric semimartingale local time." The notebook's occupation estimator
`L̂ = (1/2ε)Σ1_{|W_n|<ε}h` drops the `σ²` factor only because that experiment
uses standard Brownian motion (`σ=1`, `μ=0`), which is consistent.
`E[L_T^0]=√(2T/π)=0.8920621` recomputes exactly for standard BM. The discrete
Tanaka residual `ℓ_n = |W_{n+1}|−|W_n|−sgn(W_n)ΔW_n` gives a pathwise exact
identity at machine precision (`≤3.02e-14`), correctly distinguished from the
biased, slowly-converging occupation estimator (`0.0678→0.0206`).

A useful additional observation (not used by the notebook, included as a
reviewer cross-check): the discrete estimator `Σℓ_n` is *unbiased* for
`E[L_T^0]` at every grid size, because
`E[sgn(W_{t_n})·(W_{t_{n+1}}−W_{t_n})]=0` by independence of increments, so
`E[Σℓ_n]=E|W_T|=√(2T/π)` exactly. This is why the reported z-scores
(`−0.151,…,+1.298`) are centered at zero at all four resolutions. The
notebook's use of the z-score test is therefore sound.

**O5 — `log|X|` vs `log X` handled correctly.**
`10` §2 derives the localized exponential from `dlog|x|`, obtains
`|X_t|=|X_0|exp[…]`, and then explicitly upgrades the prefactor to `X_0`
using the constant sign on `[0,τ₀)` — fixing the unqualified `log X_t` that
appears in the motivating `complex_brownian_motion_critique.md` §1. This is
exactly the correction the acceptance criteria required.

**O6 — Filtration/injectivity claims are sound.**
For `α≠0`, `X_t = X_0 + (1/α)log(|Z_t|/|Z_0|)` is a continuous function of
`Z_t`, so `σ(Z_s:s≤t) ⊇ σ(X_s:s≤t)`; combined with `Z_t=F(X_t)` this gives
`σ(Z_s)=σ(X_s)`. State-injectivity (inverse at fixed time, via radius) is
correctly distinguished from pathwise recoverability of the fixed-radius map
(via lifted angle). `12` §5 and §6 state the four meanings of
"representation" without conflation.

**O7 — Rank-one theorem generality.**
The `rank C_t ≤ 1` result is proved for `C²` maps `F:ℝ→ℂ` (`12` §2) and
strengthened to any one-driver adapted complex Itô process (`12` §3, via the
outer product `g gᵀ`). `C² ⊃ C^∞`, so it covers "every smooth map" as the
task requires. The caveat that the obstruction is *instantaneous/local*
(`12` §2) is correctly stated and prevents over-claiming about long-time
support.

**O8 — Provenance note on the heuristic `(dB)²=dt` (input only, not a Phase 3 defect).**
The motivating `complex_brownian_motion_critique.md` §5 uses the informal
differential-square heuristic `(dB^R)²+i²(dB^Θ)²=dt−dt=0`. This is the
standard Itô heuristic and is acceptable in a motivating input, but it is
precisely the usage the project's mathematical standards advise against. The
Phase 3 deliverables themselves (`10`–`12`, synthesis) avoid it throughout:
they state quadratic variations as `d[A,A]_t=α²σ²dt` etc. using the
`[·,·]`-bracket notation, never as a literal finite-increment square. No
action required for Phase 3; flagged only for completeness.

**O9 — Covariance experiment is a valid check, with a minor caveat worth recording.**
In notebook cell 4 the one-driver increments are constructed as
`ΔA=α·ΔX, ΔΘ=β·ΔX`, so the increment pair is rank-one *by construction*. The
smallest eigenvalue is therefore at floating-point roundoff (`≈−0.`, i.e.
`~1e-16`), not a finite-sample `~1e-9`. This makes the rank-one *structure*
near-tautological, but the experiment is still a legitimate verification:
the relative error `6.6111e-4` confirms the empirical matrix matches the
analytic `K` in scale and off-diagonal structure, and the visual/numerical
contrast against the genuinely rank-two planar block (two independent
drivers) is meaningful. Noting this so the result is not over-interpreted as
a Monte Carlo test of the *theorem*; it is a Monte Carlo test of the
covariance *formula* plus a clean rank-one-vs-rank-two contrast.

**O10 — Reproducibility posture.**
The notebook records environment (`base`, Python 3.13.9, NumPy 2.3.5, SciPy
1.16.3, Matplotlib 3.10.6, nbformat 5.10.4), master seed `20260723`, and
deterministic per-cell seeds. Execution counts ascend `1→7`, all cells carry
outputs, no error outputs are present, and every embedded assertion passes
with large margins. The notebook executes top-to-bottom without hidden state
(no absolute paths in code; seeds reset per experiment). I did not
re-execute the notebook (read-only review; no project mutation), but the
saved outputs are internally consistent with the source and with the
independently recomputed exact values.

## Acceptance-criteria coverage

Mathematical acceptance (TASK-003 §"Mathematical acceptance criteria"):

- One and only one Brownian driver: ✓ (`Z_t=Z_0 e^{c(X_t−X_0)}`).
- Target Itô equation derived: ✓ (`11` §4 via `F(X_t)`; `11` §5 via
  `e^{A+iΘ}`; both agree).
- Rank-one covariance of `(log R, Θ)` incl. cross-variation: ✓ (`11` §6,
  `12` §4; `d[A,Θ]=αβσ²dt`).
- `C²` Cartesian covariance rank ≤ 1: ✓ (`12` §2).
- State injectivity vs unwrapped-phase recovery distinguished: ✓
  (`12` §5, `10` §7).
- `log|X|` (not `log X`) for negative scalar states: ✓ (`10` §2).
- Scalar zero crossings via Tanaka + local time: ✓ (`10` §4–§6).
- Both `[Z,Z]` and `[Z,Z̄]`: ✓ (`11` §7, synthesis §6).
- Phase 2 rank-two planar result preserved as a distinct model: ✓
  (`12` §8–§10, synthesis §11).

Numerical acceptance (TASK-003 §"Numerical acceptance criteria"):

- Deterministic seeds, existing conda `base`: ✓.
- Direct-map / inverse-radius / exact-product identities pathwise: ✓ (errors
  `6.273e-15 / 1.110e-15 / 9.437e-16`).
- Analytic radial + complex moments with MC SE: ✓ (all `|z|<0.6`).
- Rank-one polar vs rank-two planar covariance: ✓.
- Euler–Maruyama strong convergence over ≥4 step sizes: ✓ (6 sizes, slope
  `0.5029`).
- Discrete Tanaka formula with exact grid residual + occupation-density
  convergence: ✓ (identity residual `≤3.02e-14`; occupation bias
  `0.0678→0.0206`).
- Executed twice from clean kernels without errors: reported in
  `PHASE_3_SIMULATION_RESULTS.md`; saved outputs are consistent and
  error-free (re-execution not performed by this read-only reviewer).

## Conclusion

Phase 3 resolves the dimensional critique of
`complex_brownian_motion_critique.md` correctly and completely: it supplies
a faithful, injective, one-driver logarithmic-spiral embedding with
stochastic radius and angle; proves the general `rank ≤ 1` obstruction;
treats the literal real-axis polar form at zero with stopping, Tanaka local
time, and occupation density; and verifies every claim in a reproducible
notebook whose saved outputs match independent recomputation. No
unresolved mathematical or numerical issue remains.

Verdict: **PASS.**
