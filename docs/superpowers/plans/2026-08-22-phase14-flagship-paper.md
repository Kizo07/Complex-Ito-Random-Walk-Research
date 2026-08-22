# Phase 14 Flagship Paper Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and render a polished, self-contained Phase 14 Quarto research paper by Kanav Mehta that develops the variance-mixture smile theorem, leverage closure, Phase-Gram stationarity, and four corrected exactness frontiers in full technical detail.

**Architecture:** Create an isolated `paper/phase14/` manuscript project patterned after `paper/phase6/` but with a richer professional PDF/HTML visual system. A deterministic Python builder owns all numerical tables and scientific figures; the QMD owns the mathematical exposition and proofs; the bibliography and research notes own source provenance and novelty boundaries. Rendering and validation remain isolated from every prior phase.

**Tech Stack:** Quarto 1.10.18; Pandoc manuscript format; LuaLaTeX through Quarto; Python 3 in conda environment `phase3-paper`; NumPy, SciPy, Matplotlib; BibTeX; Poppler PDF utilities; HTML parsing with Python standard library or BeautifulSoup if already installed.

**Spec:** `docs/superpowers/specs/2026-08-22-phase14-flagship-paper-design.md`

## Global Constraints

- Author metadata is exactly `Kanav Mehta`.
- Working title is `Hidden Exactness in Bounded-Factor Stochastic Models` with subtitle `Variance-Mixture Smiles, Leverage Closure, and Phase-Gram Stationarity`.
- Target PDF length is 40–55 letter-size pages, but mathematical relevance takes precedence over padding.
- All writes stay under `/home/fire/Documents/Complex-Ito-Random-Walk-Research`; temporary render checks may use `/tmp`.
- Do not modify completed Phase 1–13 mathematics or outputs.
- Do not edit, move, stage, or delete untracked `critique2.md`.
- Do not install or mutate a Python environment unless the existing `phase3-paper` environment is proven insufficient and the user separately approves the mutation.
- Do not commit, push, publish, release, or open a pull request unless the user separately requests it.
- Central references must be primary papers or authoritative monographs; snippets are discovery aids only.
- Every bibliography entry must be cited; every citation key must resolve.
- Preserve every mathematical hypothesis and scope limitation recorded in the approved specification.
- Use seed `20260822` for all stochastic illustrations.
- Numerical evidence may support but never replace a derivation.

---

## File Structure

### New source files

- `paper/phase14/_quarto.yml` — render configuration and output metadata.
- `paper/phase14/index.qmd` — canonical manuscript.
- `paper/phase14/references.bib` — cited bibliography only.
- `paper/phase14/RESEARCH_NOTES.md` — source-by-source audit and novelty ledger.
- `paper/phase14/README.md` — local artifact and render guide.
- `paper/phase14/styles/paper.scss` — HTML presentation.
- `paper/phase14/tex/header-includes.tex` — PDF typography, headers, theorem colors, and table rules.
- `paper/phase14/filters/format-figures.lua` — figure format routing based on Phase 6.
- `paper/phase14/scripts/build_phase14_figures.py` — deterministic figures and evidence tables.
- `paper/phase14/figures/*.png` and `paper/phase14/figures/*.pdf` — eight paper figures.
- `paper/phase14/tables/*.csv` and `paper/phase14/tables/*.json` — numerical anchors and metadata.

### Generated files

- `paper/phase14/output/hidden-exactness-bounded-factor-models.pdf`
- `paper/phase14/output/hidden-exactness-bounded-factor-models.html`
- `paper/phase14/output/_tex/index.tex`
- generated output figures and bibliography copied by Quarto.

### Modified file

- `paper/README.md` — append the Phase 14 title, sources, outputs, and render command.

## Script interfaces

`paper/phase14/scripts/build_phase14_figures.py` must expose:

```python
SEED: int = 20260822

def bachelier_call(total_std: float, signed_moneyness: float) -> float: ...
def implied_total_std(price: float, signed_moneyness: float) -> float: ...
def centered_mixture_identities(scales: np.ndarray, weights: np.ndarray) -> dict[str, float]: ...
def phase8_clock_density() -> tuple[np.ndarray, np.ndarray]: ...
def leveraged_characteristic_check() -> dict[str, float]: ...
def phasegram_finite_moment(m: int, time: float, theta0: np.ndarray, sigmas: np.ndarray) -> float: ...
def phasegram_stationary_logdet(n_assets: int, n_paths: int, rng: np.random.Generator) -> np.ndarray: ...
def nonautonomous_linear_transform(time: float, lam: float) -> dict[str, float]: ...
def build_all() -> None: ...
```

`build_all()` writes exactly these structured outputs:

```text
tables/phase14_identity_checks.json
tables/phase14_atm_wedge.csv
tables/phase14_curvature.csv
tables/phase14_leverage_cf.csv
tables/phase14_phasegram_moments.csv
tables/phase14_phasegram_logdet.json
tables/phase14_nonautonomous_check.csv
tables/phase14_software_versions.json
```

and exactly these figure basenames in both PNG and PDF where the format is supported:

```text
f01_contribution_map
f02_atm_jensen_wedge
f03_local_curvature
f04_leverage_geometry
f05_leverage_cf
f06_phasegram_moments
f07_phasegram_logdet
f08_operator_ordering
```

---

### Task 1: Scaffold the isolated Quarto manuscript and structural checks

**Files:**
- Create: `paper/phase14/_quarto.yml`
- Create: `paper/phase14/index.qmd`
- Create: `paper/phase14/README.md`
- Create: `paper/phase14/styles/paper.scss`
- Create: `paper/phase14/tex/header-includes.tex`
- Create: `paper/phase14/filters/format-figures.lua`
- Create directories: `paper/phase14/scripts`, `paper/phase14/figures`, `paper/phase14/tables`

**Interfaces:**
- Consumes: Phase 6 configuration and style conventions; approved design spec.
- Produces: a minimal renderable Phase 14 project with final filenames and author metadata.

- [ ] **Step 1: Create a failing structural check**

Run:

```bash
python - <<'PY'
from pathlib import Path
root = Path('paper/phase14')
required = [
    root / '_quarto.yml', root / 'index.qmd', root / 'README.md',
    root / 'styles/paper.scss', root / 'tex/header-includes.tex',
    root / 'filters/format-figures.lua', root / 'scripts',
    root / 'figures', root / 'tables',
]
missing = [str(path) for path in required if not path.exists()]
assert not missing, missing
PY
```

Expected before creation: assertion failure listing the missing Phase 14 paths.

- [ ] **Step 2: Create the directory and configuration skeleton with `apply_patch`**

The QMD front matter must include:

```yaml
title: "Hidden Exactness in Bounded-Factor Stochastic Models"
subtitle: "Variance-Mixture Smiles, Leverage Closure, and Phase-Gram Stationarity"
author:
  - name: "Kanav Mehta"
date: 2026-08-22
output-file: hidden-exactness-bounded-factor-models
```

The QMD body initially contains every final level-one section heading from the spec so cross-reference identifiers are stable from the start.

- [ ] **Step 3: Configure PDF and HTML formats**

Copy Phase 6’s manuscript isolation, bibliography, Lua filter, freeze, cross-reference prefixes, and letter-paper defaults. Add the Phase 14 SCSS and TeX header. Use numbered sections and a three-level HTML TOC, two-level PDF TOC, retained TeX, color links, and `fig-pos: tbp`.

- [ ] **Step 4: Run the structural check again**

Expected: exit 0 and no missing paths.

- [ ] **Step 5: Run an initial minimal render**

Run:

```bash
quarto render paper/phase14
```

Expected: PDF and HTML named `hidden-exactness-bounded-factor-models.*`. Record any missing TeX package before adding optional styling.

---

### Task 2: Build the literature audit and bibliography

**Files:**
- Create: `paper/phase14/references.bib`
- Create: `paper/phase14/RESEARCH_NOTES.md`
- Modify: `paper/phase14/index.qmd`

**Interfaces:**
- Consumes: the seven theorem families and novelty boundaries in the spec.
- Produces: verified BibTeX keys and a claim-to-source map used by every manuscript section.

- [ ] **Step 1: Create the source-audit headings**

`RESEARCH_NOTES.md` contains these exact clusters:

```text
1. Bachelier and normal implied volatility
2. Variance mixtures and ATM curvature
3. Stochastic correlation and multi-asset transforms
4. Brownian leverage and conditional Gaussianity
5. Nonautonomous Feynman–Kac and evolution families
6. Hyperspherical and random correlation matrices
7. Hörmander and integrated diffusions
8. Spectrally negative Lévy fluctuation theory
9. Novelty and correction ledger
```

- [ ] **Step 2: Search and verify primary sources cluster by cluster**

For each source record authors, title, venue, year, DOI or stable URL, exact theorem/claim used, access level, and the manuscript sections it supports. Include at minimum the original or authoritative sources for Bachelier pricing; DDS; Feynman–Kac; Hörmander; Rebonato–Jäckel/Rapisarda–Brigo–Mercurio angles; Joe/Lewandowski–Kurowicka–Joe and Pourahmadi–Wang random correlation matrices; and Kyprianou/Kuznetsov–Kyprianou–Rivero scale functions.

- [ ] **Step 3: Add the recent Bachelier-curvature boundary explicitly**

Verify Alòs and García-Lorite, “On the Curvature of the Bachelier Implied Volatility” (2025), and distinguish its correlated stochastic-volatility/Malliavin setting from the exact centered finite-mixture identity proved here.

- [ ] **Step 4: Add BibTeX entries only after verification**

Use stable lowercase keys such as `bachelier1900`, `alosgarcialorite2025`, `rebonatojackel1999`, `pourahmadiwang2015`, `kuznetsovkyprianourivero2013`. Include DOI where verified; do not invent DOI fields.

- [ ] **Step 5: Run bibliography integrity checks**

Run a Python check that parses citation keys from `index.qmd`, entry keys from `references.bib`, and asserts both set differences are empty after the manuscript is complete. At this task, require only that the BibTeX file parses and contains no duplicate keys.

Expected: 55–85 relevant entries after the manuscript is complete; no quota-driven filler.

---

### Task 3: Implement the deterministic figure and evidence builder

**Files:**
- Create: `paper/phase14/scripts/build_phase14_figures.py`
- Create: `paper/phase14/tables/*`
- Create: `paper/phase14/figures/*`

**Interfaces:**
- Consumes: functions from `phase6_fk.py`, `phase6_joint.py`, `phase8_cos.py`, and `phase10_matrix.py` where mathematically identical; re-derives independent checks where circular reuse would weaken validation.
- Produces: the exact script API, eight tables, and eight figure pairs listed in File Structure.

- [ ] **Step 1: Write failing smoke assertions at the bottom of the builder**

The builder must assert:

```python
assert abs(implied_spread - formula_spread) < 2e-10
assert abs(implied_basket - formula_basket) < 2e-10
assert curvature_spread < 0.0 < curvature_basket
assert direct_conditional_cf_max_gap < 4.0 * direct_mc_se_max
assert conditional_gauge_cf_max_gap < 1e-4
assert abs(logdet_mean_mc - logdet_mean_exact) < 4.0 * logdet_mean_se
assert abs(true_nonautonomous - misordered_nonautonomous) > 0.5
```

- [ ] **Step 2: Implement pure mathematical helpers**

Implement every declared interface with type hints, docstrings specifying whether a value is exact or simulated, and input validation. `implied_total_std` uses Brent’s method with strict bracketing; `phasegram_finite_moment` uses the finite cosine series; no paper value is hard-coded except the declared reference parameters.

- [ ] **Step 3: Implement deterministic evidence generation**

Use seed `20260822`, batching for Monte Carlo memory control, and report standard errors. Reproduce these anchors:

```text
E[A_T] = 0.10662872... for the Phase 8 reference parameters
spread ATM implied correlation ≈ 0.13453
basket ATM implied correlation ≈ 0.08198
correct curvature signs: spread negative, basket positive
```

- [ ] **Step 4: Implement the eight figures**

Use Matplotlib’s object-oriented API, the common navy/teal/rust palette, 300-DPI PNG, PDF vector companions, tight bounding boxes, readable 9–11 pt labels, and no embedded titles that duplicate manuscript captions.

- [ ] **Step 5: Record environment versions**

Write Python, NumPy, SciPy, Matplotlib, platform, seed, and script-relative paths to `phase14_software_versions.json`. Do not record environment variables or secrets.

- [ ] **Step 6: Execute the builder**

Run:

```bash
conda run -n phase3-paper python paper/phase14/scripts/build_phase14_figures.py
```

Expected: eight figure basenames, eight structured tables, all assertions passing, moderate runtime.

- [ ] **Step 7: Visually inspect the eight PNG figures**

Create a contact sheet under `/tmp`, inspect it, then inspect any dense diagram or small-label figure individually. Reject clipped labels, illegible legends, color ambiguity, or excess whitespace.

---

### Task 4: Write the front matter and Part I

**Files:**
- Modify: `paper/phase14/index.qmd`

**Interfaces:**
- Consumes: verified references, contribution map, approved narrative architecture.
- Produces: front matter, abstract, introduction, relationship-to-prior-phases section, and consolidated assumptions.

- [ ] **Step 1: Write final metadata and a 350–500 word abstract**

The abstract states three major results, four supporting results, and the no-priority boundary. It does not mention repository filenames or internal agent work.

- [ ] **Step 2: Write the introduction as a problem–gap–result narrative**

Use citations for bounded correlation models, spread/basket pricing, Bachelier curvature, stochastic leverage, and matrix-valued correlation. End with a numbered contribution list and a paper roadmap.

- [ ] **Step 3: Write the self-contained framework section**

Define `f_c`, its inverse/Jacobian, the Gaussian driver, two Bachelier forwards, linear combination, clock, and Phase-Gram map. Explicitly state what is inherited from prior phases and what is newly proved here.

- [ ] **Step 4: Add notation and assumptions table**

The table covers probability measure, filtrations, Brownian covariance order, positivity/nondegeneracy, conditional-law notation, total standard deviation, angle initialization, and Lévy killing-rate notation.

- [ ] **Step 5: Run a prose and cross-reference check**

Expected: all citations resolve, all referenced section IDs exist, and no internal path or “Phase 14 draft” wording appears in the academic prose.

---

### Task 5: Write Part II — variance-mixture smile geometry

**Files:**
- Modify: `paper/phase14/index.qmd`
- Consume figures: `f02_atm_jensen_wedge`, `f03_local_curvature`
- Consume tables: `phase14_atm_wedge.csv`, `phase14_curvature.csv`

**Interfaces:**
- Consumes: Theorem 3.1 and Corollary 3.2 from the Phase 14 mathematical draft.
- Produces: publication-level theorem statements, complete proofs, interpretation, literature comparison, and numerical reconciliation.

- [ ] **Step 1: Define the Bachelier mixture and implied map**

State strict vega monotonicity, existence/uniqueness, signed-moneyness parity, and the conditions under which the algebraic inversion is an admissible implied correlation.

- [ ] **Step 2: Prove the exact level-and-curvature theorem**

Show every derivative, dominated-convergence bound, implicit differentiation step, and equality condition. State `E[S^{-1}] < ∞` exactly where used.

- [ ] **Step 3: Prove the Jensen-wedge corollary**

Derive

```text
rho_imp(0) = E[A_T]/T - Var(sqrt(V_T))/(alpha T)
rho_imp''(0) = 2(E[sqrt(V_T)]E[V_T^{-1/2}] - 1)/(alpha T)
```

and the strict spread/basket sign conclusions.

- [ ] **Step 4: Add a small-dispersion expansion**

For `V = v_bar + epsilon` with zero-mean epsilon and sufficient moments, derive the leading correction `I(0)^2 = v_bar - Var(V)/(4 v_bar) + higher-order terms` and translate it into correlation units with an explicit remainder qualification.

- [ ] **Step 5: Reconcile Phase 8 numerically**

Use the generated values, not copied prose, to show the mean clock and the two ATM inversions. Make clear why the earlier equality was false and why the opposite-curvature observation remains valid in stronger exact form.

- [ ] **Step 6: Position against related literature**

Explain that general Bachelier curvature under stochastic volatility is established research; the present contribution is the finite-horizon exact centered-scale-mixture identity and its correlation-clock interpretation.

---

### Task 6: Write Part III — leverage closure

**Files:**
- Modify: `paper/phase14/index.qmd`
- Consume figures: `f04_leverage_geometry`, `f05_leverage_cf`
- Consume table: `phase14_leverage_cf.csv`

**Interfaces:**
- Consumes: Brownian covariance, conditional law, gauge, PDE, skew, and barrier results from Phase 14.
- Produces: the central leverage theorem package and its exact tractability boundary.

- [ ] **Step 1: Derive the PSD condition and orthogonal decomposition**

State Brownian coordinate order `(W1,W2,W0)`, list every principal minor, define `g`, `C`, `r`, `h`, `Q`, and `Gamma`, and prove the covariance-rate determinant.

- [ ] **Step 2: Prove conditional Gaussianity with random mean**

Use equality in conditional law, state the role of invertibility of `X`, and derive the full conditional covariance function.

- [ ] **Step 3: Derive the Itô gauge**

Differentiate the explicit primitive and show each drift term. State the generalized-inverse convention for degenerate residual clocks.

- [ ] **Step 4: Derive both one-dimensional transform equations**

Give the joint generator and Fourier-reduced complex-drift PDE, then gauge it into the complex-potential Feynman–Kac equation. State initial/terminal conditions, boundedness, uniqueness class, and zero-leverage reduction.

- [ ] **Step 5: Prove the exponential-moment bound**

Use bounded quadratic variation and the exponential martingale; distinguish a bound from an equality.

- [ ] **Step 6: Prove the short-time skew expansion**

Show `L(y^3)`, `L^2(y^3)` at the initial state, the semigroup expansion, generic nonzero conditions, and why nonzero third moment breaks global evenness but does not alone force nonzero ATM slope.

- [ ] **Step 7: Derive the barrier obstruction**

Write the conditional moving-boundary formulation with `J^←`, state strict versus generalized inverse conditions, and explain the remaining two-state problem.

---

### Task 7: Write Part IV — Phase-Gram quotient theory

**Files:**
- Modify: `paper/phase14/index.qmd`
- Consume figures: `f06_phasegram_moments`, `f07_phasegram_logdet`
- Consume tables: `phase14_phasegram_moments.csv`, `phase14_phasegram_logdet.json`

**Interfaces:**
- Consumes: triangular-angle process and Phase 14 determinant/stationarity/boundary theorems.
- Produces: a rigorous matrix-valued section separating lifted and quotient behavior.

- [ ] **Step 1: Define the triangular map and initialization conventions**

State deterministic initial angles for finite-time product moments; state independent Haar initialization independent of future Brownian increments for stationarity.

- [ ] **Step 2: Prove determinant factorization and finite-time moments**

Derive the lower-triangular determinant, the finite Fourier series for `sin^(2m)`, and the conditional formula for random initial angles.

- [ ] **Step 3: Prove quotient stationarity**

Use Brownian motion modulo `2π`, product Haar convergence, continuous pushforward, and a direct proof that the stationary mean matrix is identity.

- [ ] **Step 4: Derive the stationary determinant law**

Prove `sin²(U) ~ Beta(1/2,1/2)`, the Mellin transform domain, polygamma log moments, mean/geometric mean gap, LLN, and CLT.

- [ ] **Step 5: Prove the boundary-hitting distribution**

Use the killed heat equation on `(0,π)`, odd sine expansion, product survival under deterministic starts, the general expectation formula for random starts, and recurrent boundary contact.

- [ ] **Step 6: Interpret high-dimensional near-singularity carefully**

Use determinant statements only; do not silently convert them into an unproved smallest-eigenvalue theorem. State the latter as open.

---

### Task 8: Write Part V and the technical appendices

**Files:**
- Modify: `paper/phase14/index.qmd`
- Consume figures: `f01_contribution_map`, `f08_operator_ordering`
- Consume table: `phase14_nonautonomous_check.csv`

**Interfaces:**
- Consumes: supporting Phase 14 theorems and all literature clusters.
- Produces: corrected frontier sections, unified exactness table, limitations, conclusion, and detailed appendices.

- [ ] **Step 1: Write nonautonomous Feynman–Kac section**

Derive the two-time evolution equations, right action, commutator integral, exact Gaussian true/misordered transforms, and constant-coefficient iff calculation. Assert no converse beyond what is proved.

- [ ] **Step 2: Write maximal scale symmetry section**

State homeomorphism and path-space hypotheses, nonnegative-volatility convention, Gaussian mean/covariance proof, simultaneous scale orbit, signed-volatility gauge, and the explicit inverse-scaling counterexample.

- [ ] **Step 3: Write endpoint–clock density section**

State smooth bounded coefficients and nonexplosion, derive the tilted forward kernel, retain distributional Fourier inversion unless an `L1` condition is proved, show the Hörmander bracket, and explain corridor atoms pathwise.

- [ ] **Step 4: Write one-sided Lévy barrier section**

Define `δ`, `Φ(δ)`, passage times, scale-function Laplace normalization, upper-passage transform, and both two-sided exit transforms. State that this is classical fluctuation theory transferred by monotonicity and does not cover two-sided VG/NIG directly.

- [ ] **Step 5: Write the unified exactness map**

Tabulate independence/leverage, Gaussian/one-sided Lévy/two-sided Lévy, scalar/matrix factors, and autonomous/nonautonomous coefficients across static law, terminal transform, smile symmetry, stationarity, and barriers.

- [ ] **Step 6: Write limitations, open problems, and conclusion**

Retain all seven open questions from the design. End with the precise closure principle “bounded factor + Brownian leverage + linear asset combination with terminal European payoff ⇒ one-dimensional complex Feynman–Kac transform.”

- [ ] **Step 7: Write appendices A–I**

Move algebra that interrupts the main narrative into the named appendices without omitting steps needed to verify the central theorems.

---

### Task 9: Apply the professional visual system and integrate figures/tables

**Files:**
- Modify: `paper/phase14/styles/paper.scss`
- Modify: `paper/phase14/tex/header-includes.tex`
- Modify: `paper/phase14/index.qmd`

**Interfaces:**
- Consumes: complete manuscript, eight figures, eight evidence tables.
- Produces: consistent PDF/HTML theorem styling, accessible figures, and publication-grade tables.

- [ ] **Step 1: Implement HTML styling**

Use Phase 6 navy/teal lineage with a deep navy banner, maximum readable line width, sticky TOC, tabular numerals, restrained theorem/proof/correction/limitation panels, responsive figures, and print-safe colors.

- [ ] **Step 2: Implement PDF typography**

Use KOMA-Script, title page, running headers, page numbers, microtype if available, `booktabs`, controlled paragraph spacing, theorem spacing, and restrained colored section rules. Add only TeX packages confirmed available through the Quarto TeX distribution.

- [ ] **Step 3: Integrate all figures**

Each figure has a stable cross-reference ID, a substantive caption, an HTML `fig-alt`, and a PDF vector source selected by the Lua filter where supported.

- [ ] **Step 4: Integrate all tables**

Use booktabs-compatible Markdown tables or raw LaTeX only where necessary. Keep tables within text width and repeat header rows for multipage tables where the renderer supports it.

- [ ] **Step 5: Run a heading/float audit**

Reject a heading immediately followed by a page break, figures separated far from their first citation, or more than two consecutive float-only pages.

---

### Task 10: Render and repair PDF/HTML outputs

**Files:**
- Generate: `paper/phase14/output/*`
- Modify as needed: Phase 14 source/style files only.

**Interfaces:**
- Consumes: complete source project.
- Produces: final PDF, HTML, and retained TeX with zero unresolved render issues.

- [ ] **Step 1: Perform a clean render**

Run:

```bash
quarto render paper/phase14
```

Expected: exit 0; output PDF, HTML, `_tex/index.tex`; no unresolved citation or cross-reference warnings.

- [ ] **Step 2: Inspect render logs and generated TeX**

Search for `Undefined`, `LaTeX Warning`, `Overfull`, `Underfull`, `Missing character`, `citation`, and `reference`. Resolve substantive issues; tolerate only documented negligible underfull boxes.

- [ ] **Step 3: Validate PDF metadata and fonts**

Run:

```bash
pdfinfo paper/phase14/output/hidden-exactness-bounded-factor-models.pdf
pdffonts paper/phase14/output/hidden-exactness-bounded-factor-models.pdf
```

Expected: author `Kanav Mehta`, letter pages, 40–55 pages unless justified by content, all fonts embedded.

- [ ] **Step 4: Inspect every PDF page**

Rasterize at 110–140 DPI, create contact sheets under `/tmp`, inspect every page, then inspect title, dense theorem, figure, wide table, appendix, references, and final pages individually at higher resolution.

- [ ] **Step 5: Validate HTML**

Parse the HTML and assert:

```text
missing local images = 0
empty figure alt text = 0
broken internal fragments = 0
unresolved citation markers = 0
unresolved cross-reference markers = 0
```

- [ ] **Step 6: Re-render after every source/style repair**

Do not claim a fixed output based on stale artifacts.

---

### Task 11: Run mathematical, citation, and artifact verification

**Files:**
- Modify as needed: Phase 14 files only.

**Interfaces:**
- Consumes: exact rendered artifact and all structured evidence.
- Produces: final verified manuscript with no critical or major defect.

- [ ] **Step 1: Re-run the deterministic builder**

Run it twice and compare the structured CSV/JSON outputs byte-for-byte. Figure binary hashes may vary only if the backend embeds timestamps; underlying values must not.

- [ ] **Step 2: Run focused mathematical checks**

Freshly verify:

```text
mixture evenness and ATM level
finite-difference versus exact ATM curvature
Phase 8 Jensen-wedge values
leverage direct/conditional/gauge characteristic functions
Phase-Gram finite moments and logdet cumulants
nonautonomous true versus misordered transforms
correct versus incorrect scale action
```

- [ ] **Step 3: Run bibliography closure**

Assert cited keys equal bibliography keys. Inspect every URL/DOI field for malformed values and verify that no internal planning or critique file is cited academically.

- [ ] **Step 4: Run repository integrity checks**

Run:

```bash
git diff --check
git status --short
```

Expected: only intended Phase 14 files and the `paper/README.md` addition, plus the pre-existing protected `critique2.md` and Phase 14 source draft/spec/plan.

- [ ] **Step 5: Obtain independent mathematical review**

The reviewer checks every theorem statement against its proof, with special attention to inverse moments, conditional-law notation, Brownian PSD order, Phase-Gram initial states, nonautonomous operator order, Hörmander hypotheses, and Lévy scale normalization.

- [ ] **Step 6: Obtain independent publication review**

The reviewer checks title/abstract coherence, section flow, citation support, table/figure quality, PDF/HTML visual defects, and novelty inflation.

- [ ] **Step 7: Resolve every critical and major finding**

Re-run the exact affected checks and render again. Record minor unresolved stylistic preferences only if they do not affect correctness or readability.

---

### Task 12: Finalize the paper index and handoff

**Files:**
- Modify: `paper/README.md`
- Modify: `paper/phase14/README.md`

**Interfaces:**
- Consumes: final exact artifact names and verification results.
- Produces: discoverable local paper with correct render instructions and no publication side effects.

- [ ] **Step 1: Add Phase 14 to the paper index**

Include title, canonical QMD, PDF, HTML, and exact render command.

- [ ] **Step 2: Complete the Phase 14 README**

List source files, figure builder, evidence tables, output files, environment, and clean render command. State that outputs are local and unpublished.

- [ ] **Step 3: Perform the final fresh verification gate**

Run the figure builder, Quarto render, PDF metadata/font checks, HTML validator, citation closure, and `git diff --check` in the same final verification pass.

- [ ] **Step 4: Report the handoff**

Provide clickable paths to the QMD, PDF, HTML, and bibliography; report page count, reference count, figure/table count, render status, review result, and any honest residual limitations. Do not commit or publish.

---

## Plan Self-Review

- **Spec coverage:** Tasks 1–12 cover every deliverable, narrative section, figure, table, literature cluster, visual requirement, mathematical gate, render gate, and scope boundary in the approved spec.
- **Placeholder scan:** The plan contains no placeholder markers and no deferred implementation language.
- **Interface consistency:** The figure builder API, table filenames, figure basenames, output filename, author metadata, seed, environment, and render command are consistent across all tasks.
- **Scope check:** This is one isolated manuscript subsystem. Literature research, figures, prose, style, and rendering all converge on the same independently testable paper and do not require decomposition into separate product specs.
