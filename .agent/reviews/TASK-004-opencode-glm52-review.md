# Independent Review: TASK-004 — Phase 3 technical paper

**Reviewer:** opencode `zai-coding-plan/glm-5.2`
**Date:** 2026-07-24
**Mode:** Review-only under the user's explicit Codex-direct exception. No
implementation, delegation, package installation, environment mutation, commit,
push, secret access, or network writes were performed. The only write performed
in this session was this review file.
**Scope inspected:** `paper/index.qmd`, `paper/references.bib`,
`paper/_quarto.yml`, `paper/README.md`, `paper/environment.yml`,
`paper/notebooks/build_phase3_discovery.py`,
`paper/notebooks/phase3_discovery.ipynb`, `paper/tables/*` (CSV/JSON),
`paper/figures/` (vector PDF + raster PNG), and the rendered
`paper/output/phase3-one-driver-complex-embedding.pdf` (+HTML, +executed
output notebooks).

---

## Verdict: **PASS**

No critical or major findings. All central mathematics is correct, every
published numerical value was cross-checked and independently re-derived, the
manuscript renders cleanly with no broken cross-references, claim discipline is
excellent, and all TASK-004 acceptance criteria are met. The items listed under
"Minor / editorial" do not affect any result, proof, or figure and do not block
acceptance.

---

## 1. Independent mathematical re-derivations (all correct)

I re-derived every requested object from first principles using Itô's lemma.
All are correct.

### 1.1 Central Itô SDE — `paper/index.qmd` eq-complex-sde (lines 285–291)
For `F(x)=Z_0 e^{c(x-X_0)}`, `F'=cF`, `F''=c^2 F`. Scalar Itô gives
`dZ = cZ dX + ½c²Z d[X,X] = (cμ+½c²σ²)Z dt + cσZ dW`, hence
`dZ/Z = (cμ+½c²σ²)dt + cσ dW`. **Correct.** The manuscript derives this two
independent ways (direct Itô, lines 282–291; polar reconstruction,
eq-polar-reconstruction lines 309–325; expanded in Appendix A lines 770–788),
and a SymPy cell asserts the two drifts coincide (build script lines 526–541).
The polar route correctly includes the mixed covariation `i d[A,Θ]`; the
manuscript explicitly warns that omitting it loses the imaginary Itô correction
(line 325). **Correct.**

### 1.2 Inverse map — eq-inverse-radius (lines 238–242)
`|Z_t| = R_0 e^{α(X_t-X_0)}` ⟹ `X_t = X_0 + (1/α) log(|Z_t|/|Z_0|)`, valid for
`α≠0`. **Correct**, including the natural filtration-equality consequence
(line 244–245).

### 1.3 Log-polar covariance — eq-polar-covariance (lines 384–394)
`dA=αμ dt+ασ dW`, `dΘ=βμ dt+βσ dW` (affine maps, no Itô correction). The
covariance density is `σ²(α,β)^T(α,β)`, eigenvalues `{0, σ²(α²+β²)}`.
**Correct.** I verified `σ²(α²+β²)=0.59678125` analytically; the empirical
eigenvalue `0.595978` is a consistent Monte Carlo estimate.

### 1.4 General rank-one theorem — thm-rank (lines 400–434)
For `dX=b dt+s dW` and `F:R→R²` of class `C²`, componentwise Itô gives a single
diffusion column `s_t F'(X_t)`, so `C_t=s_t² F'(X_t)F'(X_t)^T` has rank ≤1.
The proof is sound. The strengthened statement eq-stronger-rank (lines 439–443)
for adapted one-driver 2D Itô processes is also correct. The manuscript is
appropriately careful that this concerns *instantaneous continuous-martingale*
rank, not long-time support (lines 463–467, limitation 4 at lines 718–721).
**Correct.**

### 1.5 Complex brackets — eq-complex-brackets (lines 349–354); definitions
eq-bilinear-bracket (136–137) and eq-hermitian-bracket (141–143)
From `(ΔZ)²=(ΔU)²−(ΔV)²+2iΔUΔV` and `(ΔZ)(ΔZ̄)=(ΔU)²+(ΔV)²` the definitions
follow. With diffusion `cσZ`: `d[Z,Z]=c²σ²Z² dt` (bilinear, complex) and
`d[Z,Z̄]=|c|²σ²|Z|² dt` (Hermitian, real, nonnegative). **Correct.**

### 1.6 Exact step — eq-exact-step (lines 329–334)
`Z_{n+1}=Z_n exp(c ΔX_n)` by telescoping the pathwise exponential. **Correct**,
and correctly distinguished from Euler–Maruyama (line 338).

### 1.7 Moment formulas — eq-radial-moments (365–369), eq-complex-moments
(373–378); Appendix B (793–806)
Using the entire Gaussian MGF `E[e^{qY_t}]=exp(qμt+½q²σ²t)` (valid for complex
`q`) with `q=pα` and `q=nc`. **Correct.** I independently recomputed the
published exact values to machine precision (see §2).

### 1.8 Localized log|X| — eq-local-log (lines 487–490)
`f(x)=log|x|`: `f'=1/x`, `f''=−1/x²`, restricted to `t<τ_0`. **Correct**, and
correctly flagged as local-only with the Larsson–Ruf stopping rationale
(lines 492–494).

### 1.9 Tanaka / local-time — eq-tanaka (499–505), eq-occupation-density
(510–518)
`|X_t|=|X_0|+∫sgn(X_s)dX_s+L_t^0(X)` with symmetric local time, and the
occupation-density representation with the `σ²/(2ε)` factor for constant
volatility. **Correct.** The discrete Tanaka increment
eq-discrete-tanaka-increment (567–569) and the occupation estimator
eq-occupation-estimator (575–579) match the notebook code exactly. Note: the
experiments use standard Brownian motion (σ=1, μ=0), and the manuscript states
this explicitly ("For standard Brownian motion over T=1.25", line 657); the
exact mean `√(2T/π)` is the correct standard-BM value. **Correct.**

### 1.10 Rank-two control — eq-planar-control (lines 451–457)
`dẼ=σ(dW¹+i dW²)` has Cartesian covariance `σ²I₂` and, at fixed radius `r`,
log-polar covariance `(σ²/r²)I₂`, both rank two. **Correct.** It is labelled
"For comparison only" and "a distinct stochastic model" (lines 448, 457),
satisfying the requirement that the planar process never be presented as an
equivalent representation.

---

## 2. Numerical cross-checks (all match)

### 2.1 Manuscript tables vs generated CSV/JSON — all consistent
- `tbl-exactness` (index.qmd 590–596) vs `tables/exactness.json`: product
  `6.273e-15`, inverse `1.110e-15`, spiral `5.274e-16` — match.
- `tbl-moments` (611–620) vs `tables/moment_validation.csv`: all six rows
  (estimate/exact/se/z) match to displayed precision; max `|z|=0.700`.
- `tbl-covariance-results` (626–631) vs `tables/covariance_rank.csv`: one-driver
  `{−1.39e-16, 0.595978}`, two-driver `{0.249766, 0.250352}`, matrix errors
  `0.00135/0.00120` — match.
- `tbl-convergence` (639–648) vs `tables/strong_convergence.csv`: all six rows
  match; slope `0.5015`.
- `tbl-local-time` (663–670) vs `tables/local_time.csv`: all four rows match;
  identity errors `2.82e-15 … 2.00e-14`.
- `tbl-software` (812–825) vs `tables/software_versions.csv`: match.

### 2.2 Independent recomputation of "exact" values (run in `/tmp`, project
read-only)
I recomputed the analytic targets independently with a separate script:
```
E[R^1]   = 1.4166489850426411   (paper 1.4166489850426411)  match
E[R^2]   = 2.2334193202405945   (paper 2.2334193202405945)  match
E[(Z/Z0)^1] = 0.7371988646808149 + 0.4383209070572161i      match
E[(Z/Z0)^2] = -0.010753573435980407 + 0.4319343403388583i   match
E[L_T^0] = sqrt(2T/pi) = 0.8920620580763856                  match
rank-one nonzero eigenvalue (theory) = 0.59678125            (empirical 0.595978, consistent)
strong-convergence slope re-fit      = 0.5015310910600802    match (monotone decreasing)
```
An independent Monte Carlo (different seed, 2e6 draws) gave `E[R]≈1.41641` and
`E[(Z/Z0)]≈0.73726+0.43781i`, both within sampling error of the exact values,
confirming the published estimates are statistically sound.

### 2.3 Notebook execution integrity
`paper/notebooks/phase3_discovery.ipynb`: 15 code cells, execution counts 1–15
sequential, **zero errors**, no absolute paths in code cells. The preserved
output copies `paper/output/notebooks/phase3_discovery.ipynb` and
`phase3_discovery.out.ipynb` are likewise clean (counts 1–15, no errors). All
embedded assertions are satisfied by the published outputs (verified by
re-checking each tolerance against the CSV/JSON).

---

## 3. Manuscript, citations, cross-references, reproducibility

- **Cross-references:** `pdftotext` extraction of the rendered 23-page PDF
  contains **no `??` markers** — every `@eq-*`, `@fig-*`, `@thm-*` resolves.
  All 31 equation labels, 2 theorem labels, and figure/table labels are defined
  and referenced consistently.
- **Citations:** all 7 bib keys (`goodman2007ito`, `mortersperes2010`,
  `biskup2025localtime`, `larssonruf2019`, `pitmanyor2018guide`,
  `pitmanyor1986`, `higham2001`) are used; every in-text `@key` resolves to a
  defined entry. No orphan citations.
- **Figures:** all 18 referenced `figures/vector/fNN_*.pdf` exist and are
  non-trivial (21 KB–159 KB); 18 PNG companions exist. All 18 embeds carry
  `fig-alt` accessibility text. Requirement "≥12 substantive panels" is
  exceeded (18).
- **Render:** PDF (LuaTeX, letter, 1in margins, 23 pp) and HTML both produced
  with correct title/author/keywords metadata.
- **Reproducibility:** deterministic master seed `20260723`; package versions
  recorded in-notebook (`software_versions.csv` + displayed DataFrame) and in
  Appendix C; `paper/README.md` and Appendix C give the exact rebuild commands;
  the discovery notebook is distinct from the Phase 3 verification notebook.
- **Scope:** the article stays within Phase 3; the two-driver planar process
  appears only as the covariance-rank control (stated in `paper/README.md`
  §Scope and throughout the manuscript). Earlier phases appear only as brief
  motivation.
- **Claim discipline:** explicit, repeated non-novelty disclaimers
  (lines 89–91, 126–128, 727); the mnemonic `(dW)²=dt` is consistently treated
  as a quadratic-variation limit and explicitly called "false pathwise"
  (lines 48–53, 703–706); `fig-claim-hierarchy` separates exact / localized /
  asymptotic / numerical / heuristic statements; the rank-one *experiment* is
  honestly labelled "a check of implementation, not an independent proof"
  (lines 633–635), matching the analytic proof.

---

## 4. Minor / editorial findings (do not block PASS)

These are presentation/housekeeping items only. None is a mathematical or
numerical error.

### M1 — Notebook markdown: three equations missing a `+` sign
`paper/notebooks/build_phase3_discovery.py` (rendered into notebook markdown
cells 10 and 25). The manuscript `index.qmd` has all three **correct**, so this
affects only the notebook display, not the paper.
- Lines 508–509: `=\left(c\mu+\tfrac12 c^2\sigma^2\right)dt` immediately
  followed by `c\sigma\,dW_t.` — **missing `+`** before `c\sigma\,dW_t`
  (cf. correct eq-complex-sde, index.qmd line 289).
- Lines 517–519: the polar-drift assembly
  `\alpha\mu+i\beta\mu` / `\frac12(\alpha^2-\beta^2)\sigma^2` /
  `i\alpha\beta\sigma^2` — **missing `+`** between the three terms.
- Lines 1354–1355: boxed summary `\right]dt` followed by
  `(\alpha+i\beta)\sigma\,dW_t.` — **missing `+`** before the diffusion term
  (cf. correct Conclusion, index.qmd lines 741–747).
Suggested fix: insert the `+` operators in the three `build_phase3_discovery.py`
strings and regenerate the notebook. (Editorial.)

### M2 — Leftover draft file
`paper/index-draft.qmd` (1345 lines, untracked, older title
"Discovering a faithful one-driver complex embedding") is not in the
`_quarto.yml` render list and is superseded by `index.qmd` (847 lines). It is
harmless cruft; removing it would avoid confusion. (Editorial / housekeeping.)

### M3 — Covariance table does not state the planar control radius
`tbl-covariance-results` reports two-driver eigenvalues ≈0.25, which are the
**log-polar** covariances at the code's `local_radius=1.30`
(`σ²/r²=0.4225/1.69=0.25`), not the Cartesian `σ²I₂=0.4225`. The surrounding
text (lines 453–457) does explain the `(σ²/r²)I₂` log-polar form, and the
rank-1-vs-rank-2 conclusion is robust, so this is only a minor clarity note:
the manuscript could state `r=1.30` once, or label the rows "log-polar", so a
reader does not momentarily expect `0.4225`. (Editorial / clarity.)

### M4 — "Stochastic logarithm" naming (informational, no action required)
The task acceptance list names a "stochastic logarithm". The paper derives the
`dZ/Z` dynamics two independent ways (which *is* the stochastic logarithm) and
cites Larsson–Ruf for the concept, but does not use that exact label. The
mathematics is fully present; this note only records coverage for the
acceptance checklist.

---

## 5. Commands and evidence used

```bash
# structure / git state
git status; git log --oneline -10; find . -type f -not -path './.git/*'

# cross-reference / citation / figure audit
rg -o '\{#(eq|fig|tbl|thm|sec)-[a-z0-9-]+\}' paper/index.qmd | sort
rg -o '@(eq|fig|tbl|thm|sec)-[a-z0-9-]+|@[a-z]+' paper/index.qmd | sort | uniq -c
rg -o 'figures/[a-z]+/f[0-9]+_[a-z_]+\.pdf' paper/index.qmd | sort -u
rg -o '@\w+\{[^,]+,' paper/references.bib
rg -c 'fig-alt=' paper/index.qmd            # 18 / 18

# PDF integrity
pdfinfo paper/output/phase3-one-driver-complex-embedding.pdf    # 23 pp, letter
pdftotext .../....pdf /tmp/opencode/task004_pdf.txt
rg -n '\?\?' /tmp/opencode/task004_pdf.txt                       # none -> refs resolve
rg -n '0\.5015|0\.892062|0\.595978|6\.273|1\.416649' ...          # values present

# notebook integrity (counts, errors, abs paths)
python3 -c "import json; ..."   # counts 1..15, 0 errors, no /home/ in code

# independent recomputation (project read-only; ran under /tmp/opencode)
python3 -c "... Erad/Ezc/slope/sqrt(2T/pi) ..."   # all match to machine precision
python3 -c "... np.polyfit(log h, log err) ..."    # slope 0.5015310910600802

# assertion re-check against published CSV/JSON -> ALL PASS
```

No project files were modified, executed, or committed. All Python recomputation
ran in `/tmp/opencode` against the *published* table values (read-only).

---

## 6. Conclusion

The TASK-004 deliverables are mathematically correct, numerically
self-consistent, fully cross-referenced, reproducible, and within the approved
Phase 3 scope with disciplined, non-overclaiming language. Every acceptance
criterion in `.agent/tasks/TASK-004.md` is satisfied. The only findings are four
minor/editorial items (three missing `+` signs in notebook-only markdown, one
leftover draft file, one optional clarity label, one informational naming note),
none of which affects any theorem, formula, figure, or numerical result.

**Result: PASS** — no unresolved critical or major findings.
