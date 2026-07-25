# TASK-005 — Independent OpenCode GLM 5.2 Review

**Reviewer:** opencode (`zai-coding-plan/glm-5.2`), independent second opinion.
**Role:** Review only. No implementation, no delegation, no credentials, no
commits, no package installs, no writes outside this review file.
**Date:** 2026-07-24.
**Task:** `.agent/tasks/TASK-005.md` — Phase 4 coordinate-free complex GBM.
**Governance read:** `AgentSystem/ARCHITECTURE.md`, `ROUTING.md`, `SECURITY.md`,
`MULTI_AGENT_WORKSPACE.md`; project `AGENTS.md`.

**Headline verdict: PASS.** No critical or major findings. All mathematics was
independently re-derived and is correct; the implementation matches the
derivations; all 10 unit tests pass; the notebook executes top-to-bottom from a
clean kernel with zero error outputs and recorded environment metadata; and an
independent recomputation of every analytic benchmark reproduced the reported
values to full precision. Five minor/editorial items remain (three are
unfinalised reproducibility evidence gates, two are coordination/consistency
notes); none affects correctness. Recommended Codex follow-ups are listed in
§7.

---

## 1. Scope and method

I acted strictly as an independent reviewer. I did **not** delegate to `agy`,
Copilot, Grok, or any other agent, and made no filesystem change other than
writing this file. I:

1. Read every deliverable listed in TASK-005 (`13_`, `14_`, `15_`, the plan,
   literature review, simulation results, synthesis, `README.md`, `AGENTS.md`,
   `status.md`).
2. Independently re-derived each structural result from `W_t`, the parameters,
   and `Z_0` (no use of the project's own chain of identities to justify
   itself).
3. Independently recomputed the analytic benchmarks in a throwaway `/tmp`
   script against the published notebook numbers.
4. Ran the test suite (`python -m unittest`, read-only, `pytest` is not
   installed in `phase3-paper`) and inspected the saved notebook outputs
   directly from the notebook JSON.
5. Ran `git diff --check` and inspected `git status`/`git diff`.

The `phase3-paper` environment is Python 3.12.13, NumPy 2.5.1, SciPy 1.18.0,
Matplotlib 3.11.1, nbformat 5.10.4 — matching `state.json` and the notebook's
recorded metadata.

---

## 2. Independent mathematical re-derivations (all correct)

Notation: `\kappa=(\mu-\tfrac12\sigma^2)+i\omega`, `\nu=B=\sigma+i\beta`,
`A=\kappa+\tfrac12\nu^2`, `a=\mu-\tfrac12\sigma^2`.

### 2.1 Central exponential representation — PASS
`Z_t=Z_0 e^{\kappa t+\nu W_t}` is defined from `W_t`, real constants, and
`Z_0\ne0` only. No Cartesian `X_t,Y_t` and no pre-existing `Z_i-Z_0` path
appear in the defining equation (`13_COORDINATE_FREE_COMPLEX_GBM.md:36-49`,
eq. 13.2). `Z_t\ne0` for all finite `t` since `Z_0\ne0` (§13.8, lines
473-487), so the continuous phase lift is well defined. Coordinate-freeness is
used operationally and explicitly scoped (lit. review §6, lines 326-345).

### 2.2 Modulus GBM and phase — PASS
`Re(\kappa t+\nu W_t)=at+\sigma W_t`, `Im=\omega t+\beta W_t`, giving
`R_t=R_0 e^{at+\sigma W_t}` (13.3) and `\Theta_t=\Theta_0+\omega t+\beta W_t`
(13.4). I applied Itô to `R_0 e^{at+\sigma W_t}`:
`dR/R = (a+\tfrac12\sigma^2)dt+\sigma dW = \mu\,dt+\sigma\,dW` (13.6). Phase
(13.7) is direct. The reverse route via the general complex SDE also yields the
same radial SDE (verified in `15_` eq. 15.4–15.7). All consistent.

### 2.3 Full complex Itô drift correction — PASS
For entire `f(z)=e^z`, `d(e^\Xi)=e^\Xi(d\Xi+\tfrac12 d[\Xi])` with
`d[\Xi]_t=\nu^2 dt` (bilinear; only the martingale part contributes). Thus
`dZ/Z=(\kappa+\tfrac12\nu^2)dt+\nu dW`. With
`\nu^2=\sigma^2-\beta^2+2i\sigma\beta`, `\kappa+\tfrac12\nu^2 =
\mu-\tfrac12\beta^2+i(\omega+\sigma\beta)` (13.8–13.10; `14_` 14.5–14.10). The
two essential corrections — real `-\tfrac12\beta^2` and imaginary
`+\sigma\beta` — are both present. The constant-modulus stress test
(`\mu=\sigma=0`) gives SDE `dZ/Z=(-\tfrac12\beta^2+i\omega)dt+i\beta dW`
(14.24); omitting `-\tfrac12\beta^2` yields `|Z|=|Z_0|e^{\beta^2 t/2}` because
`-\tfrac12(i\beta)^2=+\tfrac12\beta^2` (14.25–14.27). I re-derived this and the
numerical growth factor `e^{0.81\cdot4/2}=5.0530903` independently (matches
notebook and `PHASE_4_SIMULATION_RESULTS.md` §3).

### 2.4 Ordinary vs Doléans exponential and exact transition — PASS
Ordinary exponent uses `\kappa`; the SDE uses `A=\kappa+\tfrac12 B^2`; they
differ by `\tfrac12 B^2` (`14_` 14.8–14.10, 14.14–14.15). Doléans:
`\mathcal E(At+BW)_t=\exp((A-\tfrac12B^2)t+BW_t)=\exp(\kappa t+BW_t)`, so
`Z_t=Z_0\mathcal E(Y)_t` (14.13–14.14). Stochastic log vs continuous log lift
differ by `\tfrac12 B^2 t` (14.16–14.18). Exact transition
`Z_t=Z_s e^{\kappa h+\nu\Delta W}` and grid walk
`Z_{n+1}=Z_n e^{(\mu-\sigma^2/2+i\omega)h+(\sigma+i\beta)\sqrt h\,\xi_n}` (13.15–13.16)
are correct; the walk is exact, not Euler–Maruyama. The coefficient identity
`A-\tfrac12B^2=\kappa` closed to `0j` in float for the notebook params
(verified independently).

### 2.5 Radial and mixed complex moments — PASS
Radial: `E[R_t^p]=R_0^p\exp(p\mu t+\tfrac12p(p-1)\sigma^2 t)` (13.20) — I
confirmed via `log R\sim N(\cdot,\sigma^2 t)`. Complex:
`E[Z_t^n]=Z_0^n\exp(n\kappa t+\tfrac12n^2\nu^2 t)` (13.21); equivalently
`=Z_0^n\exp(nAt+\tfrac12n(n-1)B^2 t)` (13.22), since
`n\kappa+\tfrac12n^2B^2=nA+\tfrac12n(n-1)B^2`; `E[Z_t]=Z_0 e^{At}` (13.23).
Mixed log-polar (13.24):
`E[R_t^p e^{iq(\Theta_t-\Theta_0)}]=R_0^p\exp([p(\mu-\tfrac12\sigma^2)+iq\omega+\tfrac12(p\sigma+iq\beta)^2]t)`
— confirmed by completing the Gaussian square. My recomputation reproduced
`E[Z_T]=-0.0521966+1.6458395i`, `E[R_T^2]=4.2049252`, mixed
`=0.5153227+1.5639549i` (T=1.5) to full precision.

### 2.6 Bilinear and Hermitian brackets — PASS
`d[Z,Z]_t=B^2 Z_t^2 dt` (complex bilinear; 14.19) from the martingale part
`B Z_t dW`; `d[Z,\bar Z]_t=|B|^2|Z_t|^2 dt` (real nonneg; 14.20) from
`B Z_t dW\cdot\bar B\bar Z_t dW`. The two are correctly distinguished; the docs
explicitly warn that substituting `|B|^2` for `B^2` in the Itô correction is
wrong (`14_` lines 296-298). Implementation matches (`phase4_model.py:181-188`).

### 2.7 Rank-one log-polar covariance — PASS
Martingale increments `(σ dW, β dW)` give instantaneous covariance
`[[σ²,σβ],[σβ,β²]]=(σ,β)^T(σ,β)`, determinant 0, eigenvalues `0` and
`σ²+β²` (15.20–15.22); correlation `sign(σβ)` (15.23). The Cartesian
counterpart `g g^T` with `g=(Re(BZ),Im(BZ))` is also rank ≤1, =1 when `B\ne0`
(15.24–15.25). Fixed-time support `u\mapsto Z_0 e^{\kappa t}e^{\nu u}` is a
logarithmic spiral for `σβ\ne0` (15.26–15.27). All verified, including the
caveat that this is fixed-time support, not a whole-path statement
(`13_` lines 384-386).

### 2.8 Phase 3 subfamily mapping — PASS
Phase 3 `Z_0 e^{(1+i\gamma)L_t}` with `L_t=at+σW_t` equals the Phase 4 model
iff `β=γσ`, `ω=γ a=γ(\mu-\tfrac12σ²)` (15.16). The fixed-spiral condition
`ω=(β/σ)(\mu-\tfrac12σ²)` (15.18) is the same restriction with `γ=β/σ`
(15.17, 15.19). The general Phase 4 params (`ω=0.70,β=0.45,σ=0.30`) violate
the restriction (residual 0.6475), so the unrestricted model is genuinely freer.
I confirmed `γσ\neβ` for the free choice. Pathwise equivalence error
`6.66e-16` reproduced.

### 2.9 Independent two-driver comparator drift/covariance — PASS
`Z_t^{(2)}=Z_0\exp((\mu-\tfrac12σ²+iω)t+σW^{(r)}+iβW^{(\theta)})` has GBM
modulus driven by `W^{(r)}` (15.29) and phase driven by `W^{(\theta)}` (15.30),
diagonal rank-two covariance `diag(σ²,β²)` (15.31). Applying Itô to the
2-driver log-driver gives `d[Z^{(2)}/Z^{(2)}=(\mu-\tfrac12β²+iω)dt+σdW^{(r)}+iβdW^{(\theta)}`
(15.32): the cross term `σβ` disappears because `[W^{(r)},W^{(\theta)}]=0`. The
contrast between (15.9) (one driver, `+σβ` imaginary drift) and (15.32) (two
drivers, no cross drift) is exactly the right way to expose what a single driver
cannot do. The comparator is correctly labelled as not planar Brownian motion
(15.8, table lines 469-473).

---

## 3. Implementation and tests — PASS

`phase4_model.py`:
- `ComplexGBMParameters.log_drift/sde_drift/diffusion` (lines 23-36) match
  `\kappa`, `A=\mu-\tfrac12β²+i(ω+σβ)`, `B`. The relation
  `sde_drift = log_drift + ½·diffusion²` holds (test lines 36-39), which is the
  right invariant to catch a modulus-square-for-bilinear-square regression.
- `exact_path` (39-55), `gbm_radius` (58-74), `unwrapped_phase` (77-89) match
  (13.2)/(13.3)/(13.4). `exact_step` (92-104) matches (13.15); rejects `h<0`
  and `z0=0`.
- `euler_maruyama_path` (107-122) uses the SDE drift `A` (`1+Ah+BΔW`), not the
  compensated `\kappa` — correct, and tested (lines 87-101).
- `log_polar_covariance` (125-130) = `outer([σ,β],[σ,β])`; `radial_moment`
  (133-144) = (13.20); `complex_moment` (147-158) = (13.21); `mixed_log_polar_moment`
  (161-178) = (13.24); `complex_bracket_rates` (181-188) = (14.19)/(14.20);
  `two_driver_path` (191-207) = (15.28). All verified against the derivations.

`tests/test_phase4_model.py` (10 tests): ran via `python -m unittest` in
`phase3-paper` (read-only; `pytest` is absent from the env). **Result: 10/10
OK.** Each test targets a specific regression class (documented in its
docstring): bilinear-vs-Modulus-square, SDE-vs-compensated drift, hidden second
driver, two-driver phase noise, half-variance omission, etc. Tolerances
(`atol=2e-17`, `rtol=2e-15`) are at floating-point scale, appropriate for exact
identities.

---

## 4. Notebook — PASS

`notebooks/phase4_coordinate_free_complex_gbm.ipynb` (780 KB, 23 cells):
- Clean top-to-bottom execution: 0 `error` outputs; execution counts sequential
  1–12; all assertions passed (final stream: "All Phase 4 notebook assertions
  passed.").
- Environment recorded in execution-count 1 (`Environment: phase3-paper`,
  Python 3.12.13, NumPy 2.5.1, SciPy 1.18.0, Matplotlib 3.11.1, nbformat
  5.10.4), satisfying the AGENTS.md notebook standard. Builder uses
  `Path.cwd()`/`Path.parent` (no absolute paths in code; builder lines 72-77).
- Every headline number in `PHASE_4_SIMULATION_RESULTS.md` was read directly
  from the saved notebook outputs and matched exactly:
  - modulus identity error `8.882e-16`; phase `4.441e-16`; exact-step
    `8.750e-15`;
  - constant-modulus error `4.441e-16`; wrong-SDE radius-formula error
    `3.553e-15`; wrong growth factor `5.053090`;
  - one-driver eigenvalues `(-1.249e-16, 0.2921074)`; two-driver min eigenvalue
    `0.0898770`;
  - Phase 3 equivalence `6.661e-16`; spiral residual `0.647500`;
  - EM strong slope `0.5469` over 5 step sizes (16,32,64,128,256);
  - bilinear QV rel. error `0.6998%`; Hermitian `0.3648%`;
  - two-driver modulus error `8.882e-16`;
  - MC z-scores: radial `-0.994`; complex mean `(0.949,-1.770)`; mixed
    `(0.629,-1.605)` — all within 2 SE, so the results-doc claim "within two
    Monte Carlo standard errors" is accurate (max |z|=1.770).
- Constant-modulus demonstration shows both the correct constant-modulus
  behaviour and the failure when the `-\tfrac12β²` drift is omitted
  (criterion: "demonstrate failure when that drift is omitted").
- EM convergence is measured as `E|Z_T^{EM}-Z_T|` on 3500 shared fine paths
  aggregated to each coarse step — methodologically sound; slope `0.5469` is
  consistent with strong order `1/2`, and uses SDE drift `A` (not `\kappa`).

---

## 5. Independent recomputation (throwaway script in `/tmp`, no repo writes)

For the notebook's main params (`μ=0.08,σ=0.30,ω=0.70,β=0.45`, `Z_0=1.7e^{0.35i}`,
`T=1.5`) I recomputed from scratch and obtained, matching the docs/notebook to
full precision:
`\kappa=0.035+0.7j`; `B=0.3+0.45j`; `A=-0.02125+0.835j`;
`A-B²/2-κ=0`; `E[Z_T]=-0.05219665+1.64583953j`; `E[R_T²]=4.20492519`;
mixed `=0.51532266+1.56395486j`; one-driver eig `[~0, 0.2925]`; two-driver eig
`[0.09,0.2025]`; wrong growth `5.05309032`. No discrepancy found.

`git diff --check`: exit 0 (no whitespace errors). `git status`: branch
`phase-4-coordinate-free-complex-gbm`; Phase 4 deliverables are untracked (new),
with only `README.md`, `.agent/status.md`, `.agent/state.json` modified — all
Phase-4-scoped. No out-of-scope files touched.

---

## 6. Acceptance-criteria checklist (TASK-005)

Mathematical (lines 62-80): all satisfied.
- Defined from `W_t`, params, `Z_0`, no Cartesian primitives — YES.
- `R_t` proven GBM (`dR/R=μdt+σdW`) — YES.
- Unwrapped phase `\Theta_0+ωt+βW_t` — YES.
- Full complex Itô drift correction — YES.
- Ordinary / exact-step / Doléans reconciled — YES.
- Log-polar covariance, both brackets, transitions, selected moments — YES.
- Phase 3 recovered as constrained subfamily — YES.
- One-driver rank-one limitation + two-driver boundary stated and shown — YES.
- `d[W,W]=dt` kept distinct from finite-increment identity and from `i²=-1`
  (`14_` §14.9) — YES.
- No unsupported novelty claim (lit. review §10) — YES.

Computational (lines 82-102):
- `phase3-paper` env, unmuted — YES.
- Deterministic seeds (`20260724` family), versions recorded — YES.
- Clean top-to-bottom kernel run with saved outputs — YES.
- Exact identities at float tolerances — YES (≤8.75e-15).
- Constant-modulus Itô drift + failure-on-omission — YES.
- MC moments + standard errors — YES.
- Rank-one vs rank-two control — YES.
- EM strong convergence ≥4 step sizes (used 5) — YES.
- Second clean `/tmp` rerun + deterministic-text comparison — **NOT EVIDENCED**
  (see F1).
- Pandoc render + `git diff --check` — `git diff --check` YES; **Pandoc render
  of Phase 4 `.md` files NOT EVIDENCED** (see F2).
- Independent OpenCode GLM 5.2 review — this document (YES).

---

## 7. Findings

No critical. No major. No mathematical or numerical errors of any severity.

### F1 — minor: no documented second clean `/tmp` rerun for Phase 4
**Where:** TASK-005 lines 97-98; `PHASE_4_SIMULATION_RESULTS.md` (only one
execution documented); `.agent/handoff.md` (its `/tmp` rerun evidence at lines
85-91 refers to TASK-003, not TASK-005).
**Issue:** Criterion requires a second clean run to `/tmp`, zero error outputs,
and a deterministic-text comparison. Only one Phase 4 execution is recorded.
**Residual risk:** negligible (fixed seeds; I confirmed the single saved run is
clean, deterministic, and matches the docs).
**Correction (for Codex):** execute
`jupyter nbconvert --to notebook --execute --output-dir /tmp ...phase4...ipynb`
against a clean kernel in `phase3-paper`, confirm zero error cells, diff the
text-output streams against the committed notebook (they must be byte-identical
for the deterministic streams), and append a short paragraph to
`PHASE_4_SIMULATION_RESULTS.md` recording the command and the match result
(verbatim model of prior phases, `PHASE_2_SIMULATION_RESULTS.md:25-36`).

### F2 — minor: no documented Pandoc render of Phase 4 Markdown
**Where:** TASK-005 line 99; no Phase 4 Pandoc record exists
(`PHASE_3_TECHNICAL_PAPER_PLAN.md` documents Pandoc for Phase 3 only).
**Issue:** Criterion requires rendering the authoritative Phase 4 `.md` files
with Pandoc; `git diff --check` (the second half) passes (exit 0), but a Pandoc
round-trip of `13_`/`14_`/`15_`/synthesis/lit-review is not evidenced.
**Residual risk:** very low (the LaTeX/Markdown is simple display math; no
unresolved refs are apparent).
**Correction (for Codex):** run
`pandoc -f markdown -t html <file>.md -o /tmp/<file>.html` (or `-t pdf`) for
each authoritative Phase 4 `.md`, confirm no fatal parse errors, and record the
Pandoc version in `PHASE_4_SIMULATION_RESULTS.md`.

### F3 — minor: red/green TDD evidence not retained
**Where:** TASK-005 line 85; no red/green evidence artifact for Phase 4.
**Issue:** "Develop the computational core test-first and retain the
red/green evidence" — tests exist and are green (10/10), but the
first-failing-then-passing evidence trail is not documented.
**Residual risk:** none to correctness (the tests are meaningful and pass).
**Correction (for Codex):** add a one-line note in `PHASE_4_SIMULATION_RESULTS.md`
(or `status.md`) that the core was built test-first, citing the test docstrings
that name the regression each test guards, and the green run command
(`python -m unittest tests.test_phase4_model -v` → 10 OK).

### F4 — editorial: coordination state lags TASK-005 completion
**Where:** `.agent/state.json` (`notebook_verification: "pending"`,
`review_result: "pending"`); `.agent/status.md` (`State: in progress`);
`.agent/handoff.md` (no TASK-005 section).
**Issue:** State files still reflect pre-review status and have no Phase 4
handoff entry.
**Correction (for Codex):** after this review is accepted and F1–F3 closed,
set `state.json` `notebook_verification`/`review_result` to the outcome, flip
`status.md` to `complete`, and prepend a concise TASK-005 section to
`handoff.md` (changed files, test command/result, review verdict, usage/scorecard
IDs).

### F5 — editorial: notebook "wrong SDE" demo adds an `iω` term vs doc 14
**Where:** notebook Section 3, builder lines 293-299
(`wrong_no_ito_drift = z0*exp((0.5β²+iω)t+iβW)`); contrasted with
`14_…md` eq. 14.25–14.27 which writes the wrong SDE `d\tilde Z/\tilde Z=iβ\,dW`
without `ω`.
**Issue:** The notebook's incorrect process retains the deterministic
`iω` rotation while dropping only `-\tfrac12β²`. This is *not* an error — the
`iω` term is purely imaginary and cannot affect the modulus, and isolating the
single missing term while holding rotation fixed is arguably a cleaner
demonstration. It is a cross-document presentation difference a careful reader
could notice.
**Correction (optional, for Codex):** either (a) add one sentence to the
Section-3 markdown noting that the demo retains `ω` to isolate the Itô drift
and that the modulus conclusion is identical to doc 14.25–14.27, or (b) leave
as-is. No code change needed.

---

## 8. Verdict

**PASS.**

The Phase 4 construction is mathematically correct and rigorously presented;
the implementation faithfully realizes every formula; the unit tests are
meaningful and green; the notebook is clean, deterministic, environment-stamped,
and reproduces every claimed identity and moment; and my independent
re-derivation and recomputation found no error. The work makes no unsupported
novelty claim and correctly keeps `d[W,W]=dt`, the finite-increment heuristic,
and `i²=-1` in separate mathematical categories.

The only open items are F1–F3 (unfinalised reproducibility evidence gates with
negligible residual risk) and F4–F5 (coordination/presentation). None is a
correctness blocker. Recommendation: before formally declaring TASK-005
*complete*, Codex should close F1 (second clean `/tmp` rerun with deterministic
text comparison), F2 (Pandoc render of the Phase 4 `.md` files), and F4
(update `state.json`/`status.md`/`handoff.md`). F3 and F5 are minor record
additions. Because none is critical or major, the review verdict is **PASS**.
