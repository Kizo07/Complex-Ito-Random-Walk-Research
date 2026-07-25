# Phase 4 Technical Paper Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:executing-plans` to implement this plan task-by-task. The user
> prohibited implementation delegation, so do not use
> `superpowers:subagent-driven-development`. Steps use checkbox (`- [ ]`)
> syntax for tracking.

**Goal:** Reorganize the existing Phase 3 Quarto manuscript into
`paper/phase3/` and produce an independently renderable, research-grounded
Phase 4 technical paper under `paper/phase4/`.

**Architecture:** Preserve Phase 3 as a self-contained Quarto project while
creating a second self-contained project for Phase 4. Generate all Phase 4
notebook outputs, figures, and tables from a deterministic Python builder that
imports the tested root `phase4_model.py`; use those outputs in a canonical QMD
manuscript and render matching PDF/HTML artifacts.

**Tech Stack:** Python 3.12 in conda environment `phase3-paper`, NumPy, SciPy,
Matplotlib, pandas, SymPy, nbformat/Jupyter, Quarto 1.9.38, Pandoc 3.8,
LuaLaTeX/TinyTeX, Git, and OpenCode `zai-coding-plan/glm-5.2` for review only.

## Global Constraints

- All writes remain under
  `/home/fire/Documents/Complex-Ito-Random-Walk-Research`, except temporary
  execution/render comparisons under `/tmp`.
- Preserve untracked `critique2.md`; never stage, move, rewrite, or delete it.
- Do not install packages or mutate the `phase3-paper` environment.
- Do not delegate implementation to `agy`, Copilot, Grok, a subagent, or any
  other worker.
- Use OpenCode `zai-coding-plan/glm-5.2` only after Codex implementation and
  verification, as an independent reviewer and second opinion.
- Do not push, merge, release, or publish unless the user separately asks.
- Do not claim that complex GBM or stochastic exponentials are newly invented.
- Distinguish \(d[W,W]_t=dt\), finite-increment convergence, and \(i^2=-1\).
- Do not call the one-driver model planar Brownian motion.
- Use deterministic seeds in the `20260724` family.
- Keep Phase 3 mathematically unchanged while relocating it.

## File Structure

**Move without content redesign:**

- `paper/_quarto.yml` → `paper/phase3/_quarto.yml`
- `paper/index.qmd` → `paper/phase3/index.qmd`
- `paper/references.bib` → `paper/phase3/references.bib`
- `paper/environment.yml` → `paper/phase3/environment.yml`
- `paper/notebooks/` → `paper/phase3/notebooks/`
- `paper/figures/` → `paper/phase3/figures/`
- `paper/tables/` → `paper/phase3/tables/`
- `paper/filters/` → `paper/phase3/filters/`
- `paper/styles/` → `paper/phase3/styles/`
- `paper/output/` → `paper/phase3/output/`
- existing `paper/README.md` → `paper/phase3/README.md`

**Create:**

- `paper/README.md` — two-paper index and render commands
- `paper/phase4/_quarto.yml` — independent manuscript project
- `paper/phase4/index.qmd` — canonical Phase 4 manuscript
- `paper/phase4/references.bib` — verified Phase 4 bibliography
- `paper/phase4/environment.yml` — reproducibility environment record
- `paper/phase4/README.md` — Phase 4 artifact map and commands
- `paper/phase4/RESEARCH_NOTES.md` — source and claim audit
- `paper/phase4/notebooks/build_phase4_discovery.py` — notebook/artifact builder
- `paper/phase4/notebooks/phase4_discovery.ipynb` — executed notebook
- `paper/phase4/filters/format-figures.lua` — format-specific figure resolver
- `paper/phase4/styles/paper.scss` — HTML paper styling
- `paper/phase4/figures/vector/*.pdf` — publication figures
- `paper/phase4/figures/raster/*.png` — HTML companions
- `paper/phase4/tables/*.{csv,json}` — generated evidence tables
- `paper/phase4/output/*` — PDF, HTML, TeX, and notebook outputs
- `.agent/tasks/TASK-006.md` — task contract
- `.agent/reviews/TASK-006-opencode-glm52-review.md` — final independent review

**Modify:**

- `README.md` — repair Phase 3 paths and add Phase 4 paper reading order
- `.agent/status.md`, `.agent/state.json`, `.agent/handoff.md` — TASK-006 state
- `docs/superpowers/plans/2026-07-24-phase4-technical-paper.md` — checkboxes

---

### Task 1: Establish TASK-006 and the two-paper hierarchy

**Files:**

- Create: `.agent/tasks/TASK-006.md`
- Modify: `.agent/status.md`
- Modify: `.agent/state.json`
- Move: existing `paper/` Phase 3 files to `paper/phase3/`
- Create: `paper/README.md`

**Interfaces:**

- Consumes: merged Phase 4 repository and approved design specification.
- Produces: stable Phase 3/Phase 4 directory boundary used by every later task.

- [x] **Step 1: Write the TASK-006 contract**

Create a Tier 3 research/publication contract that lists the exact deliverables,
allowed paths, central model, research requirements, notebook requirements,
render requirements, review model, and prohibited actions.

- [x] **Step 2: Mark TASK-006 active**

Set `.agent/status.md` and `.agent/state.json` to:

```json
{
  "active_task": "TASK-006",
  "owner": "Codex",
  "status": "in_progress",
  "scope": "Phase 4 technical paper and two-paper reorganization",
  "blocked": false
}
```

Retain additional environment, branch, and model fields used by the repository.

- [x] **Step 3: Move Phase 3 atomically**

Use explicit `mv` operations, not globs that could capture `critique2.md`.
After moving, verify:

```bash
test -f paper/phase3/index.qmd
test -f paper/phase3/_quarto.yml
test -f paper/phase3/output/phase3-one-driver-complex-embedding.pdf
```

- [x] **Step 4: Create the paper index**

`paper/README.md` must list both projects, canonical source, discovery notebook,
PDF, HTML, and exact render command for each.

- [x] **Step 5: Verify Phase 3 relocation**

Run:

```bash
quarto render paper/phase3
```

Expected: exit 0 and regenerated PDF/HTML under `paper/phase3/output/`.

---

### Task 2: Complete and record the primary-source research

**Files:**

- Create: `paper/phase4/RESEARCH_NOTES.md`
- Create: `paper/phase4/references.bib`

**Interfaces:**

- Consumes: Phase 4 literature review, verified publisher/repository metadata,
  and primary papers.
- Produces: citation keys and novelty boundaries consumed by `index.qmd`.

- [x] **Step 1: Build the bibliography audit table**

Record author, title, year, venue, DOI/stable URL, source type, primary/secondary
classification, and the exact manuscript claim supported.

- [x] **Step 2: Verify the core references**

At minimum verify entries for:

```text
ito1951
doleansdade1970
spitzer1958
pitmanyor1986
higham2001
buckwar2006
perret2010
larssonruf2019
cernyruf2022
cernyruf2023
```

- [x] **Step 3: Write the novelty-boundary matrix**

Include explicit rows for:

```text
complex scalar linear SDE exists
complex GBM terminology exists
stochastic exponential/logarithm exists
modulus-preserving four-parameter reparameterization is the paper focus
one-driver process is not planar Brownian motion
no claim equates quadratic variation with complex algebra
```

- [x] **Step 4: Validate BibTeX**

Run:

```bash
pandoc paper/phase4/RESEARCH_NOTES.md \
  --bibliography paper/phase4/references.bib \
  --citeproc -t html -o /tmp/phase4-research-notes.html
```

Expected: exit 0 and no missing citation warnings.

---

### Task 3: Scaffold the independent Phase 4 Quarto project

**Files:**

- Create: `paper/phase4/_quarto.yml`
- Create: `paper/phase4/environment.yml`
- Create: `paper/phase4/README.md`
- Create: `paper/phase4/filters/format-figures.lua`
- Create: `paper/phase4/styles/paper.scss`

**Interfaces:**

- Consumes: the proven Phase 3 publication configuration.
- Produces: independent PDF/HTML rendering contract for Phase 4.

- [x] **Step 1: Copy and retarget the figure filter**

Keep the PDF-to-raster HTML mapping logic, but resolve paths relative to
`paper/phase4/`.

- [x] **Step 2: Define the Quarto project**

Set:

```yaml
project:
  type: manuscript
  output-dir: output
  render:
    - index.qmd

manuscript:
  article: index.qmd
  notebooks:
    - notebook: notebooks/phase4_discovery.ipynb
      title: Phase 4 discovery notebook

bibliography: references.bib
```

Configure HTML and LuaLaTeX PDF formats to match Phase 3.

- [x] **Step 3: Record the environment**

Copy the package floors from the detected `phase3-paper` environment without
installing or updating anything.

- [x] **Step 4: Write project instructions**

Document notebook generation, clean execution, Quarto render, expected output
filenames, and validation commands.

- [x] **Step 5: Smoke-test configuration**

Run `quarto check` and inspect `_quarto.yml` with `quarto inspect` after
`index.qmd` is created in Task 6. At this stage, confirm that every configured
filter, style, bibliography, and notebook path is a valid Phase 4-relative
path.

---

### Task 4: Build the deterministic Phase 4 discovery notebook

**Files:**

- Create: `paper/phase4/notebooks/build_phase4_discovery.py`
- Create: `paper/phase4/notebooks/phase4_discovery.ipynb`
- Create: `paper/phase4/figures/vector/*.pdf`
- Create: `paper/phase4/figures/raster/*.png`
- Create: `paper/phase4/tables/*.{csv,json}`

**Interfaces:**

- Consumes:
  `phase4_model.ComplexGBMParameters`, `exact_path`, `exact_step`,
  `gbm_radius`, `unwrapped_phase`, `euler_maruyama_path`,
  `log_polar_covariance`, moment functions, bracket functions, and
  `two_driver_path`.
- Produces: an executed notebook source plus 18 named figure pairs and nine
  evidence tables.

- [x] **Step 1: Define deterministic publication helpers**

The builder must include:

```python
def save_figure(fig, stem: str, alt_text: str) -> None:
    """Save vector PDF and raster PNG companions under paper/phase4."""

def write_csv(name: str, frame: pandas.DataFrame) -> None:
    """Write a deterministic CSV with stable column order."""

def write_json(name: str, payload: dict[str, object]) -> None:
    """Write sorted, indented JSON without nonfinite values."""

def assert_inside_phase4(path: pathlib.Path) -> pathlib.Path:
    """Reject output paths escaping the Phase 4 paper root."""
```

- [x] **Step 2: Create the environment and derivation cells**

The first code cell records versions. Early cells derive
\(\kappa\), \(A\), and \(B\), assert \(A-B^2/2=\kappa\), and generate the
log-plane/exponential-plane explanation.

- [x] **Step 3: Create exactness and rotation experiments**

Generate Figures 2--7 and tables:

```text
coefficient_reconciliation.csv
exactness.json
```

Assertions must cover modulus, phase, exact transition, and constant-modulus
errors below \(2\times10^{-13}\).

- [x] **Step 4: Create distribution and covariance experiments**

Generate Figures 8--12 and:

```text
covariance_rank.csv
transition_summary.csv
```

Use at least 200,000 seeded increments for empirical covariance. Assert
one-driver numerical rank one and two-driver numerical rank two.

- [x] **Step 5: Create moment and Phase 3 experiments**

Generate Figures 13--15 and:

```text
moment_validation.csv
phase3_equivalence.json
```

Report componentwise Monte Carlo standard errors and require every standardized
residual to have absolute value below 3.

- [x] **Step 6: Create convergence and bracket experiments**

Generate Figures 16--17 and:

```text
strong_convergence.csv
quadratic_variation.csv
```

Use at least five shared-path step sizes and require fitted strong slope in
\([0.42,0.65]\). Require both bracket relative errors below 2%.

- [x] **Step 7: Create synthesis figure and manifests**

Generate Figure 18 and:

```text
software_versions.csv
numerical_summary.json
figure_manifest.csv
table_manifest.csv
```

The final cell asserts that exactly 18 vector and 18 raster figures exist and
that every planned table exists.

- [x] **Step 8: Generate the notebook**

Run:

```bash
conda run -n phase3-paper \
  python paper/phase4/notebooks/build_phase4_discovery.py
```

Expected: notebook created with no absolute project paths embedded in code.

---

### Task 5: Execute and verify the notebook twice

**Files:**

- Modify: `paper/phase4/notebooks/phase4_discovery.ipynb`
- Generate temporarily:
  `/tmp/phase4_discovery_recheck.ipynb`

**Interfaces:**

- Consumes: generated notebook from Task 4.
- Produces: clean executed notebook and reproducibility evidence.

- [x] **Step 1: Execute in place from a clean kernel**

Run outside the managed socket sandbox:

```bash
conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  paper/phase4/notebooks/phase4_discovery.ipynb
```

- [x] **Step 2: Execute a second clean copy**

```bash
conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute \
  --output phase4_discovery_recheck.ipynb \
  --output-dir /tmp \
  paper/phase4/notebooks/phase4_discovery.ipynb
```

- [x] **Step 3: Compare executions**

Parse notebook JSON and assert:

```text
no error outputs
sequential execution counts
identical code-cell sources
identical deterministic stream text
identical generated CSV/JSON hashes
all final assertions passed
```

- [x] **Step 4: Record evidence**

Write the final source/output/table hashes to
`paper/phase4/README.md` and `.agent/status.md`.

---

### Task 6: Write the canonical Phase 4 manuscript

**Files:**

- Create: `paper/phase4/index.qmd`

**Interfaces:**

- Consumes: research notes, references, generated figures/tables, and Phase 4
  derivation documents.
- Produces: complete research manuscript with no placeholders.

- [x] **Step 1: Write front matter and abstract**

Use the approved title and include author metadata consistent with Phase 3.
State the model, exact modulus, phase, Itô correction, rank limitation, and
computational evidence in the abstract.

- [x] **Step 2: Write introduction through problem formulation**

Use primary citations for precedent and explicitly state the novelty boundary.
Include the coordinate-free operational definition and the one-driver target.

- [x] **Step 3: Write analytical sections**

Derive:

```text
native exponential
GBM modulus
unwrapped phase
complex Itô SDE
ordinary/Doléans exponential identity
stochastic logarithm
exact transition
radial, complex, and mixed moments
bilinear and Hermitian brackets
rank-one covariance
```

- [x] **Step 4: Write structural comparisons**

Prove the Phase 3 restrictions
\(\beta=\gamma\sigma\) and
\(\omega=\gamma(\mu-\sigma^2/2)\). Derive the independent two-driver drift and
rank-two covariance.

- [x] **Step 5: Write methods and results**

Every reported number must come from a generated CSV/JSON table or saved
notebook output. Add cross-referenced figures and tables with descriptive alt
text.

- [x] **Step 6: Write discussion, limitations, and conclusion**

End with boxed direct-exponential, exact-step, and Itô-SDE forms. State that the
model is rank one, not planar Brownian motion, and not a novelty claim for
complex GBM.

- [x] **Step 7: Write appendices**

Include expanded Itô algebra, moment derivation, and a complete reproducibility
manifest.

- [x] **Step 8: Audit manuscript structure**

Run:

```bash
rg -n '^#|^##|^###' paper/phase4/index.qmd
rg -n 'T[O]DO|T[B]D|PLACE[H]OLDER|FIXME|citation needed' \
  paper/phase4/index.qmd
```

Expected: all required sections present and no placeholder matches.

---

### Task 7: Render PDF and HTML

**Files:**

- Generate: `paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf`
- Generate: `paper/phase4/output/phase4-native-complex-geometric-brownian-motion.html`
- Generate: `paper/phase4/output/_tex/index.tex`
- Generate: Phase 4 notebook preview/output files

**Interfaces:**

- Consumes: complete Quarto project.
- Produces: final publication artifacts.

- [x] **Step 1: Render Phase 4**

Run outside the sandbox if Jupyter sockets are required:

```bash
quarto render paper/phase4
```

Expected: exit 0 for both PDF and HTML.

- [x] **Step 2: Verify filenames**

If Quarto emits `index.pdf` or `index.html`, set the manuscript output filename
in configuration and rerender. Do not rename only one format manually.

- [x] **Step 3: Verify Phase 3 remains renderable**

Run:

```bash
quarto render paper/phase3
```

Expected: Phase 3 output regenerates without content drift.

- [x] **Step 4: Check unresolved references**

Run text extraction and search:

```bash
pdftotext \
  paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf \
  /tmp/phase4-paper.txt
rg -n '\?\?|undefined|citation needed' /tmp/phase4-paper.txt
```

Expected: no unresolved markers.

---

### Task 8: Perform publication-quality validation

**Files:**

- Modify as needed: Phase 4 QMD, builder, figures, styles, filter, and config.

**Interfaces:**

- Consumes: rendered PDF/HTML and manifests.
- Produces: validated accessible publication.

- [x] **Step 1: Inspect PDF metadata**

Run:

```bash
pdfinfo paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf
pdffonts paper/phase4/output/phase4-native-complex-geometric-brownian-motion.pdf
```

Require letter-size pages and all fonts embedded.

- [x] **Step 2: Rasterize and inspect every PDF page**

Render pages to `/tmp/phase4-paper-pages/` and inspect contact sheets plus every
page changed after any correction. Reject clipped equations, overlapping
captions, unreadable labels, blank pages, and orphaned headings.

- [x] **Step 3: Validate HTML**

Parse the HTML and assert:

```text
all local href targets exist
all image src targets exist
all figures have nonempty alt text
all 18 raster figures are referenced
no unresolved cross-reference text appears
```

- [x] **Step 4: Validate manifests and citations**

Compare filesystem figures/tables with manifests. Extract citation keys from
QMD and confirm every key exists in `references.bib`; confirm no unused key is
accidentally presented as supporting a central claim.

- [x] **Step 5: Run source checks**

```bash
PYTHONDONTWRITEBYTECODE=1 conda run -n phase3-paper \
  python -m unittest discover -s tests -v
conda run -n phase3-paper python -m py_compile \
  phase4_model.py \
  tests/test_phase4_model.py \
  paper/phase4/notebooks/build_phase4_discovery.py
python -m json.tool .agent/state.json
git diff --check
```

Expected: all commands exit 0.

---

### Task 9: Repair navigation and finalize coordination

**Files:**

- Modify: `README.md`
- Modify: `paper/README.md`
- Modify: `.agent/status.md`
- Modify: `.agent/state.json`
- Modify: `.agent/handoff.md`

**Interfaces:**

- Consumes: final verified artifacts.
- Produces: authoritative project navigation and handoff.

- [x] **Step 1: Repair Phase 3 links**

Replace old `paper/...` paths with `paper/phase3/...` only where the target
moved. Do not rewrite unrelated mathematical content.

- [x] **Step 2: Add Phase 4 paper reading order**

Link the design, plan, research notes, manuscript, discovery notebook, PDF,
HTML, and pending review.

- [x] **Step 3: Validate local Markdown links**

Parse local Markdown links in root and paper README files. Require zero missing
targets except the review file before Task 10 creates it.

- [x] **Step 4: Update handoff**

Record changed paths, exact test/render commands, notebook hashes, PDF/HTML
validation, known limitations, and pending reviewer state.

---

### Task 10: Obtain and resolve the OpenCode GLM 5.2 review

**Files:**

- Create: `.agent/reviews/TASK-006-opencode-glm52-review.md`
- Modify as needed: reviewed Phase 4 sources/artifacts
- Modify: `.agent/status.md`, `.agent/state.json`, `.agent/handoff.md`

**Interfaces:**

- Consumes: complete verified implementation.
- Produces: independent verdict, resolved findings, and final task state.

- [x] **Step 1: Run the bounded review**

Use `agent-usage run` with model `zai-coding-plan/glm-5.2`. Instruct the model
to review only, not delegate or implement, and write only the TASK-006 review
file.

- [x] **Step 2: Require review coverage**

The review must independently check:

```text
central Itô derivations
ordinary versus stochastic exponential
moments and complex brackets
rank-one and two-driver claims
Phase 3 mapping
literature positioning and novelty language
notebook-to-manuscript numeric consistency
PDF/HTML presentation evidence
```

- [x] **Step 3: Evaluate the external call**

Record the usage ID and run:

Pass the exact UUID printed by `agent-usage run` to
`llm-scorecard evaluate --usage-id`, together with the actual model, role,
outcome, and evidence-based scores.

Store only the resulting identifiers and concise evaluation notes.

- [x] **Step 4: Resolve findings**

Fix every critical or major finding. Resolve minor mathematical,
reproducibility, accessibility, or broken-link findings that are in scope.
Rerun affected notebook/render/validation gates.

- [x] **Step 5: Mark TASK-006 complete**

Set status to complete only after all gates pass. Record:

```text
review verdict
usage ID
scorecard evaluation ID
test result
notebook reproducibility result
PDF/HTML result
remaining nonblocking limitations
```

- [x] **Step 6: Final verification**

Rerun the full source, notebook, render, link, manifest, and `git diff --check`
suite on the final tree. Leave the branch local and unpushed.
