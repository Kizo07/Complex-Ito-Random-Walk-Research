# TASK-006 — Independent review (OpenCode `zai-coding-plan/glm-5.2`)

**Role:** Independent reviewer / second-opinion mathematician (review-only).
**Date:** 2026-07-24
**Scope:** Phase 4 technical paper and the Phase 3 / Phase 4 two-paper
reorganization.
**Constraint honored:** No delegation, no other agents, no implementation
changes. The only file written by this review is this one.

---

## 1. Summary verdict

**Final verdict: PASS WITH MINOR FINDINGS.**

I independently re-derived every central identity from elementary definitions
(without importing `phase4_model.py`) and reproduced every numerical value
reported in the manuscript to the precision printed. All 10 root unit tests
pass, the executed notebook is clean and deterministic, the PDF (29 letter
pages) and HTML meet the publication/accessibility criteria, and Phase 3 is
preserved byte-for-byte and remains independently renderable.

There are **no critical findings** and **no major findings**. Two minor items
(a PDF-margin deviation from the approved spec, and one attribution phrase I
could not confirm from the public record) and two editorial items are listed
below. None block publication; the minor items are verification/precision
refinements.

**Publication verdict:** Mathematically and computationally sound, honestly
positioned, and reproducible. Suitable for release as a technical report /
self-contained manuscript once the two minor items are checked.

---

## 2. Commands and calculations actually performed

Environment: conda env `phase3-paper` (Python 3.12.13, NumPy 2.5.1, SciPy
1.18.0, pandas 3.0.3) — matches `tables/software_versions.csv` and the
manuscript `tbl-software` (index.qmd:900).

1. `python -m unittest tests.test_phase4_model -v` → **10/10 pass**, 0.019 s.
2. `python -m py_compile phase4_model.py
   paper/phase4/notebooks/build_phase4_discovery.py
   tests/test_phase4_model.py` → all compile.
3. Wrote `/tmp/opencode/independent_verify.py` rebuilding all identities from
   scratch (parameters μ=0.18, σ=0.42, ω=0.90, β=0.65, R₀=1.25, Θ₀=0.35,
   T=1.50; seeds 20260724+k). Reproduced, to printed precision:
   - coefficients κ, B, A, A−B²/2;
   - pathwise modulus/phase/reconstruction errors (4.44e-16, 6.66e-16);
   - constant-modulus stress error (4.44e-16);
   - analytic moments E[R^p], E[Z^n], mixed (p,q);
   - empirical one-driver covariance and eigenvalue ratio 5.538e-16;
   - Phase 3 restriction (β=0.483, ω=0.10557, path error 2.734e-16);
   - two-driver drift μ−β²/2+iω (cross drift σβ=0.273 absent);
   - EM strong-convergence errors [0.21371,…,0.04450], slope 0.562511466542004;
   - bilinear/Hermitian bracket relative errors 0.001860 / 0.001872.
4. `pdfinfo` / `pdffonts` on the Phase 4 PDF: 29 pages, 612×792 pt (letter),
   **all fonts embedded**.
5. `pdftotext` → grep: zero `??`/`???` cross-reference or citation markers;
   bibliography section present.
6. BeautifulSoup scan of the HTML: 18 `<img>`, **18 nonempty alt texts**, 18
   unique sources, **0 missing local targets**.
7. Notebook JSON scan: 18 cells (9 code / 9 markdown), execution counts
   1–9 (sequential), **0 error outputs**, 18 inline figures, stream contains
   both `PHASE4_DETERMINISTIC_SUMMARY` and `ALL_PHASE4_ASSERTIONS_PASSED`.
8. `git show HEAD:paper/index.qmd` vs `paper/phase3/index.qmd`: **zero diff**
   (both 852 lines) — Phase 3 content preserved exactly by the move.
9. `git diff --check` → clean.
10. Springer page read for `10.1007/s10543-006-0060-5` to audit the Buckwar
    et al. 2006 attribution (metadata confirmed; see §6/§9).

---

## 3. Independent derivation verdict

All identities below were re-derived independently and agreed with the
manuscript (`paper/phase4/index.qmd`) and the model
(`phase4_model.py`).

**Central exponential** (eq-central-process, index.qmd:73-83). With
κ=(μ−σ²/2)+iω and B=σ+iβ, Z_t=Z_0 exp(κt+BW_t). **Correct.** The four-parameter
separation (Re exponent = log GBM, Im exponent = phase lift) is exact.

**Exact GBM modulus** (eq-radius / eq-radius-sde, index.qmd:305-320).
|Z_t|=R_0 exp((μ−σ²/2)t+σW_t); applying real Itô gives dR_t/R_t=μdt+σdW_t.
**Correct and pathwise**, not merely distributional — exactly as claimed
(index.qmd:322-323).

**Unwrapped phase** (eq-phase, index.qmd:329-333). Θ_t=Θ_0+ωt+βW_t. Im(κt+BW_t)
= ωt+βW_t. **Correct.** The discontinuity of the principal argument vs the
continuous lift is stated (index.qmd:341-345), satisfying the polar/logarithm
singularity standard.

**A = κ + B²/2** (eq-drift-A, index.qmd:399-405). B²=σ²−β²+2iσβ, hence
A=(μ−σ²/2+iω)+(σ²−β²)/2+iσβ = μ−β²/2+i(ω+σβ). **Correct.** Numerically
A=−0.03125+1.173i, A−B²/2=κ=0.0918+0.9i exactly. The uniqueness statement
"starting from B and demanding A−B²/2=κ determines A" (index.qmd:425-427) is
correct.

**Ordinary vs Doléans exponential / stochastic logarithm**
(index.qmd:453-508). For Y_t=At+BW_t, [Y,Y]_t=B²t, so
ℰ(Y)_t=exp(Y_t−Y_0−[Y,Y]_t/2)=exp((A−B²/2)t+BW_t)=exp(κt+BW_t), giving
Z_t=Z_0ℰ(Y)_t (eq-doleans-form). The continuous log lift log_cont=κt+BW_t and
the stochastic logarithm 𝓛=∫dZ/Z=At+BW_t differ by B²t/2 (eq at index.qmd:492-
504). **Correct.** The stochastic logarithm is well-defined because the
exponential never hits zero (limitation 5, index.qmd:1110-1111).

**Transition laws** (eq-log-polar-law / eq-support-line, index.qmd:551-589).
(log(R_t/R_0), Θ_t−Θ_0) is jointly Gaussian with mean ((μ−σ²/2)t, ωt) and
covariance t·[[σ²,σβ],[σβ,β²]], determinant 0. The support line follows from
the rank-one outer product. **Correct.** Fixed-time complex support
{Z_0 e^{κt+Bw}} is a logarithmic spiral for σβ≠0; ray for β=0; circle for
σ=0,β≠0 (index.qmd:604-606). **Correct.**

**Radial / complex / mixed moments** (eq-radial-moment, eq-complex-moment,
eq-mixed-moment, index.qmd:617-668). Via E[e^{cW_t}]=e^{c²t/2} (analytic
continuation, App. B, index.qmd:1239-1241):
- E[R_t^p]=R_0^p exp((pμ+½p(p−1)σ²)t). **Correct.**
- E[Z_t^n]=Z_0^n exp((nκ+½n²B²)t). **Correct.**
- E[R_t^p e^{iq(Θ_t−Θ_0)}]=R_0^p exp([p(μ−σ²/2)+iqω+½(pσ+iqβ)²]t). **Correct.**
Numerically reproduced: E[R]=1.637456, E[Z]=−0.611913+1.023833i,
E[Z²]=0.314617−0.931845i, matching `moment_validation.csv`.

**Bilinear vs Hermitian brackets** (eq-bilinear-bracket, eq-hermitian-bracket,
index.qmd:756-777). Diffusion coefficient is BZ_t, so d[Z,Z]_t=B²Z_t²dt
(bilinear, complex) and d[Z,Z̄]_t=|B|²|Z_t|²dt (Hermitian, nonnegative).
**Correct.** The paper's central anti-conflation point (B² vs |B|²) is
enforced by a dedicated test (`test_complex_brackets_keep_bilinear_and_hermitian_squares_distinct`).

**Rank-one log-polar and Cartesian covariance** (index.qmd:685-744).
Σ₁=(σ,β)ᵀ(σ,β), eigenvalues σ²+β² and 0 (verified numerically: ratio
5.54e-16). Cartesian g(z)=(Re(Bz),Im(Bz))ᵀ gives g gᵀ of rank ≤ 1. **Correct.**
The rank-invariance-under-coordinate-change remark (index.qmd:742-744) is
right.

**Phase 3 restriction** (eq-phase3-restrictions, index.qmd:799-811). Expanding
Z_0 e^{(1+iγ)L_t} with L_t=(μ−σ²/2)t+σW_t and matching gives β=γσ,
ω=γ(μ−σ²/2). **Correct** (independently reproduced: β=0.483, ω=0.10557,
pathwise error 2.73e-16 vs `phase3_equivalence.json`).

**Two-driver comparator and disappearance of the imaginary cross drift**
(index.qmd:819-876). With independent W^(r),W^(θ), the log-increment bracket is
σ²dt+(iβ)²dt=(σ²−β²)dt (cross bracket vanishes by independence), so the SDE
drift is κ+(σ²−β²)/2=μ−β²/2+iω — i.e. the one-driver imaginary cross drift σβ
disappears (eq-two-driver-sde vs eq-final-sde). **Correct.** Σ₂=diag(σ²,β²)
rank two for σβ≠0, reproduced.

**Quadratic-variation / Itô-table discipline.** The paper repeatedly
distinguishes the quadratic-variation statement d[W,W]_t=dt (a partition-sum
limit in probability, index.qmd:178-184) from the algebraic identity i²=−1
(index.qmd:113-118). This satisfies the project's mathematical standard that
an individual Brownian increment is never said to literally satisfy
(ΔW)²=Δt.

**Derivation verdict: all central identities verified.** No mathematical
errors found.

---

## 4. Notebook-to-manuscript numerical consistency

Every number quoted in the manuscript was reproduced by my independent script
or matches the generated tables exactly:

| Manuscript item | Location | Independent check |
|---|---|---|
| κ=0.0918+0.9i, B=0.42+0.65i, A=−0.03125+1.173i | tbl-coefficients (index.qmd:971-975) | exact match |
| max exactness error 6.66e-16 | tbl-exactness (index.qmd:982-989) | exact (reconstruction 6.66e-16) |
| eigenvalue ratio 5.54e-16 | index.qmd:748-749 | exact (5.538e-16) |
| Phase 3 error 2.73e-16 | index.qmd:815-817 | exact (2.734e-16) |
| E[R]=1.63746, E[Z]=−0.61191+1.02383i | tbl-moments (index.qmd:1021-1026) | exact |
| covariance one-driver [[0.17713,0.27413],[…,0.42426]] | tbl-covariance (index.qmd:1005-1008) | exact |
| EM slope 0.5625; errors [0.21371…0.04450] | tbl-convergence (index.qmd:1035-1045) | exact (0.562511…) |
| bracket rel. errors 0.00186 / 0.00187 | tbl-brackets (index.qmd:1056-1059) | exact |
| two-driver off-diagonal "sampling error ~0" | index.qmd:1013-1014 | consistent (0.00025, <1 SE) |

**Consistency: complete.**

---

## 5. Reproducibility evidence

- Builder imports the tested root `phase4_model.py` (no formula duplication).
- All RNG seeds derive from 20260724 (index.qmd:884; `software_versions.csv`
  master seed).
- Notebook: 9 sequential code cells, 0 errors, 18 inline figures, terminal
  markers present; deterministic stream reproduced exactly (same EM slope,
  same covariance entries to full double precision).
- `figure_manifest.csv` and `table_manifest.csv` list all 18 figures and 12
  tables with stable relative paths; `assert_inside_phase4` guards against
  path escape.
- Environment recorded; no packages installed or mutated during review.

**Reproducibility: confirmed.**

---

## 6. Literature attribution and novelty language

The positioning is appropriately modest and accurate:
- Abstract (index.qmd:33-35): "Complex geometric Brownian motion is
  established theory; the contribution is a modulus-preserving four-parameter
  synthesis…"
- Intro (index.qmd:110-111): "We do not claim to have invented complex GBM."
- RESEARCH_NOTES novelty boundary (lines 74-84) explicitly rejects
  inventing complex GBM / stochastic exponentials and rejects the slogans
  dW²=dt≡i²=−1 and "this is planar Brownian motion."

Bibliographic metadata for all 13 keys was checked; DOIs are well-formed, and
the Doléans-Dade entry honestly omits a DOI with a stated reason
(RESEARCH_NOTES line 35, 50-51). The Buckwar et al. 2006 record (BIT 46(2),
261-282, DOI 10.1007/s10543-006-0060-5) is **verified correct** against the
Springer page. See §9 (minor 2) for one phrasing precision item.

---

## 7. PDF / HTML presentation and accessibility

- PDF: 29 pages, US letter, **all fonts embedded** (Latin Modern, DejaVu,
  STIX), no unresolved `??`/`???` markers, bibliography present. Status notes
  all 29 pages visually inspected.
- HTML: 18 figures, **18 nonempty descriptive alt texts**, 18 valid local
  sources, `code-fold` and external-link-new-window enabled per spec.
- Vector figures in PDF; raster companions in HTML, per design.

**Presentation/accessibility: meet criteria.** (One spec-deviation on margins
— see §9 minor 1.)

---

## 8. Phase 3 independence (reorganization integrity)

- Phase 3 owns its own `_quarto.yml`, `references.bib`, `environment.yml`,
  `README.md`, notebook, figures, tables, filter, and styles; renders to a
  23-page letter PDF.
- Phase 3 contains **zero** references to phase4; Phase 4 references "phase3"
  only conceptually (the constrained-subfamily comparison) and via the shared
  conda env name — **no file-path dependency** on `paper/phase3/`.
- `git show HEAD:paper/index.qmd` vs `paper/phase3/index.qmd`: **byte-for-byte
  identical** (852 lines, empty diff). The design non-goal "do not alter the
  mathematical content of the completed Phase 3 paper while moving it" is
  satisfied exactly.

**Phase 3 remains fully independent and unaltered.**

---

## 9. Findings by severity

### Critical
None.

### Major
None.

### Minor

**M1 — PDF margin deviates from the approved spec.**
`paper/phase4/_quarto.yml:35-36` sets `geometry: margin=0.75in`, whereas the
approved design (section 7 of
`docs/superpowers/specs/2026-07-24-phase4-technical-paper-design.md`) specifies
"one-inch margins" (Phase 3 correctly uses `margin=1in`,
`paper/phase3/_quarto.yml:36`). Impact is purely cosmetic (the 29-page letter
PDF renders cleanly with all pages inspected) and the acceptance criteria
(§12) only require letter size + embedded fonts, which are met. Genuine but
non-blocking spec-compliance deviation. Fix: set `margin=1in`, or amend the
spec if 0.75in is the intended choice.

**M2 — Buckwar et al. 2006 "complex geometric Brownian motion" attribution
phrasing.**
`paper/phase4/index.qmd:138-141` states that Buckwar, Horváth-Bokor, and
Winkler "allow the state and coefficients to be complex, keep W real, and
explicitly refer to the exact solution as complex geometric Brownian motion";
`RESEARCH_NOTES.md:37,61` lists the term as established terminology supported
by `buckwar2006`. The bibliographic metadata and the "complex scalar linear
test equation with a real Brownian driver" precedent are verified and solid
(also independently supported by `perret2010` and `abdulle2013`). However, the
public abstract of the 2006 paper describes only a "linear time-invariant test
equation"; I could not confirm from the accessible record that the exact phrase
"complex geometric Brownian motion" appears in that paper's full text. This is
a verification/precision item, **not** an asserted error and **not** a novelty
violation (the manuscript never claims the term is new). Recommendation:
confirm the exact phrase against the 2006 full text; if absent, soften
index.qmd:138-141 to "treat the complex scalar linear test equation" and
attribute the "complex GBM" terminology to wherever it is verifiably stated
(e.g., Perret's thesis).

### Editorial

**E1 — `tbl-software` omits Seaborn.** `paper/phase4/index.qmd:900-910`
summarizes `tables/software_versions.csv` but omits Seaborn 0.13.2, which is
imported and used for plot theming (`sns.set_theme` in
`build_phase4_discovery.py:132`) and is present in the CSV. No numerical impact
(theming only); include for completeness or note it is theming-only.

**E2 — Appendix A Itô shorthand could re-state its meaning.**
`paper/phase4/index.qmd:1194-1198` writes the Itô multiplication table as
(dU_t)²=σ²dt, (dV_t)²=β²dt, dU_t dV_t=σβdt. This is standard and used
correctly inside Itô's formula, but a brief "(quadratic covariation)"
parenthetical would reinforce the careful distinction the paper itself makes
in `sec-preliminaries` (index.qmd:113-118, 178-184). Optional; not an error.

---

## 10. Publication verdict

The manuscript is mathematically rigorous, computationally reproducible,
honestly positioned relative to prior work, and cleanly presented. The central
claim (a modulus-preserving four-parameter native complex exponential whose
modulus is exactly GBM, with the Itô cross drift and rank-one covariance as
honest records of a single shared driver) is fully substantiated by both
derivation and seeded experiment. The two minor items are precision/spec
refinements that do not affect any result. **Recommended for release** after
M1/M2 are checked.

---

## 11. Final verdict

**PASS WITH MINOR FINDINGS.**
