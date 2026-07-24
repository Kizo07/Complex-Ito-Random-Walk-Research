# Phase 3 Technical Paper Plan

## Status

**Proposed on 2026-07-23. Paper implementation has not started.**

This plan covers only the Phase 3 work. Earlier phases may appear in one
sentence of motivation or as the two-driver comparison needed to explain the
rank obstruction, but their derivations and simulations are outside the
paper's scope.

## 1. Publication objective

Turn Phase 3 into a self-contained computational mathematics paper that
answers the following question:

> How can a scalar arithmetic Brownian motion be represented by a complex
> exponential with both stochastic radius and stochastic angle, without
> introducing a second Brownian driver or falsely identifying the result with
> planar Brownian motion?

The paper will combine:

1. a rigorous mathematical narrative;
2. a new discovery notebook showing how the construction was found;
3. reproducible symbolic and Monte Carlo checks;
4. publication-quality explanatory figures;
5. a Quarto manuscript in `.qmd` format; and
6. a rendered PDF suitable for technical review.

The initial publication category should be **technical paper** or
**expository research note**, not a claim of a new theorem. The logarithmic
spiral and rank results must be positioned against a broader literature search
before any originality claim is made.

### Proposed working title

**A Faithful One-Driver Complex Embedding of Arithmetic Brownian Motion:
Itô Dynamics, Covariance Rank, and Zero Crossings**

### Intended audience

- stochastic-analysis readers;
- applied mathematicians;
- mathematical-finance readers familiar with Itô calculus;
- researchers interested in complex stochastic processes;
- advanced students seeking a geometrically visual explanation of quadratic
  variation and noise dimension.

## 2. Central mathematical content

Let

\[
dX_t=\mu\,dt+\sigma\,dW_t,
\qquad
c=\alpha+i\beta,
\qquad
Z_t=Z_0\exp\!\left(c(X_t-X_0)\right).
\]

The paper will organize its claims around six results.

### Result 1: stochastic radius and angle with one driver

\[
\log R_t=\log R_0+\alpha(X_t-X_0),
\qquad
\Theta_t=\Theta_0+\beta(X_t-X_0).
\]

Both coordinates are stochastic when \(\alpha\beta\ne0\), but they share one
Brownian direction.

### Result 2: exact state recovery

For \(\alpha\ne0\),

\[
X_t
=X_0+\frac{1}{\alpha}
\log\frac{|Z_t|}{|Z_0|}.
\]

This makes the logarithmic-spiral map a state-injective and
filtration-preserving representation of the scalar process.

### Result 3: Itô dynamics

\[
\frac{dZ_t}{Z_t}
=
\left(c\mu+\frac12c^2\sigma^2\right)dt
+c\sigma\,dW_t.
\]

The paper will derive this twice: directly from the scalar map and from the
polar reconstruction \(Z=e^{A+i\Theta}\).

### Result 4: rank-one obstruction

\[
d
\begin{pmatrix}
[A,A]_t&[A,\Theta]_t\\
[\Theta,A]_t&[\Theta,\Theta]_t
\end{pmatrix}
=
\sigma^2
\begin{pmatrix}
\alpha^2&\alpha\beta\\
\alpha\beta&\beta^2
\end{pmatrix}dt,
\qquad A_t=\log R_t.
\]

The matrix is an outer product and has rank one. More generally, for every
\(C^2\) map \(F:\mathbb R\to\mathbb C\), the instantaneous Cartesian
covariance of \(F(X_t)\) has rank at most one.

### Result 5: complex quadratic variations

\[
d[Z,Z]_t=c^2\sigma^2Z_t^2\,dt,
\qquad
d[Z,\overline Z]_t
=|c|^2\sigma^2|Z_t|^2\,dt.
\]

These quantities will be distinguished carefully from each other and from
the mnemonic \(dW\,dW=dt\).

### Result 6: exact finite-step walk and zero-crossing treatment

\[
Z_{n+1}
=Z_n\exp\!\left(c\,\Delta X_n\right).
\]

The literal real-axis polar form will be treated separately. Before the first
zero it uses \(\log|X_t|\); globally the nonsmooth radius \(|X_t|\) requires
Tanaka's formula and symmetric local time.

## 3. Research-paper structure

The final `index.qmd` will use the following conventional structure.

### Front matter

- title;
- author and affiliation placeholders;
- date and version;
- abstract;
- keywords;
- optional Mathematics Subject Classification codes after subject review;
- repository and reproducibility statement.

### Abstract

The abstract will contain:

1. the scalar-process problem;
2. the one-driver logarithmic-spiral construction;
3. the Itô and rank-one results;
4. the distinction from planar Brownian motion;
5. the zero-crossing/local-time result; and
6. one sentence about numerical verification.

It will avoid the literal claim \(dt=(dW)^2\).

### 1. Introduction

- motivate the desire for a complex exponential form;
- explain why a fixed radius is too restrictive;
- identify the hidden issue of increasing the noise dimension;
- state the research question;
- list the paper's contributions;
- summarize the paper organization.

### 2. Related work and positioning

- multidimensional Itô calculus and covariance;
- complex semimartingales and stochastic logarithms;
- Brownian local time, occupation density, and Tanaka's formula;
- planar Brownian motion and polar decompositions;
- numerical SDE verification.

This section will cite primary or authoritative sources. It will distinguish
standard tools from the particular synthesis developed in the paper.

### 3. Preliminaries and notation

- scalar arithmetic Brownian motion;
- complex numbers as \(\mathbb R^2\);
- complex self-variation and conjugate variation;
- unwrapped angle versus angle modulo \(2\pi\);
- state dimension versus Brownian noise dimension;
- exact identities versus Itô differential identities versus heuristics;
- localization and stopping-time notation.

### 4. Problem formulation

- define the desired meaning of a “complex representation”;
- separate deterministic image, state-injective embedding, pathwise
  recoverability, and equality as a planar stochastic model;
- formulate the one-driver constraint;
- show why stochastic radius alone does not imply two-dimensional noise.

### 5. The logarithmic-spiral construction

- introduce \(c=\alpha+i\beta\);
- define \(Z_t=Z_0e^{c(X_t-X_0)}\);
- derive its radius and unwrapped angle;
- prove injectivity for \(\alpha\ne0\);
- establish equality of the generated filtrations;
- classify the circle, ray, and spiral parameter cases.

### 6. Itô dynamics and stochastic logarithm

- direct Itô derivation;
- independent polar-coordinate derivation;
- stochastic-logarithm consistency check;
- exact finite-step multiplicative walk;
- exact Gaussian and lognormal distributions;
- exact complex moments.

### 7. Noise dimension and covariance rank

- derive all polar brackets;
- state and prove the \(C^2\) rank-one theorem;
- state the stronger one-driver Itô-process version;
- derive both complex quadratic variations;
- compare with an explicitly labelled two-driver rank-two benchmark;
- explain why long-time support and instantaneous covariance rank are
  different questions.

The two-driver benchmark is included only as the control experiment needed to
interpret the Phase 3 rank result.

### 8. Scalar polar coordinates and zero crossings

- derive the localized \(\log|X_t|\) formula;
- stop at the first zero;
- explain the angular jump on the real axis;
- apply Tanaka's formula to \(|X_t|\);
- introduce symmetric local time and occupation density;
- separate the real-axis representation from the smooth spiral embedding.

### 9. Numerical methods

- parameter choices and units;
- fixed master seed and per-experiment seeds;
- exact simulation of arithmetic Brownian increments;
- Monte Carlo estimators and standard errors;
- covariance and eigenspectrum estimators;
- coupled Euler–Maruyama strong-error experiment;
- discrete Tanaka and occupation-density estimators;
- software environment and numerical tolerances.

### 10. Numerical results

- pathwise reconstruction;
- exact-product identity;
- moment agreement with uncertainty;
- rank-one versus rank-two covariance;
- strong convergence;
- nonlinear-image covariance;
- local-time checks.

Every numerical table will distinguish an exact target, an estimate, its
uncertainty, and the comparison statistic.

### 11. Discussion

- what the complex representation preserves;
- what it does not preserve;
- geometry of the logarithmic spiral;
- why the angle and radius are perfectly locally correlated;
- why a second independent driver is necessary for full-rank planar noise;
- how \(i^2=-1\) differs from quadratic variation;
- implications for complex-valued random-walk notation.

### 12. Limitations

- the construction is a deterministic embedding, not a universal planar
  stochastic model;
- \(\alpha=0\) loses pointwise injectivity unless a lifted angle is retained;
- the real-axis polar map is singular at zero;
- the local-time occupation estimator converges slowly;
- Monte Carlo evidence supports but does not prove the analytic results;
- novelty claims remain conditional on the expanded literature review.

### 13. Conclusion

- restate the one-driver representation;
- summarize the Itô and rank results;
- state the exact random-walk form;
- close with the correct relationship between algebraic complex structure and
  stochastic quadratic variation.

### Appendices

- full algebra for the two Itô derivations;
- proof of the general covariance-rank theorem;
- moment derivations;
- local-time convention and Tanaka details;
- numerical parameters and assertion tolerances;
- software and environment manifest;
- optional supplementary figure gallery.

## 4. New discovery notebook

### Purpose

Create a new notebook that records **how the representation was found**, not
just a cleaned-up rerun of the existing verification notebook.

Proposed file:

`paper/notebooks/phase3_discovery.ipynb`

The existing
`notebooks/phase3_one_driver_complex_embedding.ipynb` remains the validation
record. The discovery notebook will be more explanatory, visual, and
step-by-step.

### Notebook narrative

1. Start from the scalar arithmetic Brownian motion.
2. State the design requirements:
   one driver, stochastic radius, stochastic angle, and recoverable state.
3. Introduce general log-polar coordinates
   \(A_t=a(X_t)\), \(\Theta_t=b(X_t)\).
4. Choose the simplest globally smooth linear functions
   \(a(x)=\alpha(x-X_0)\) and \(b(x)=\beta(x-X_0)\).
5. Reconstruct \(Z_t=Z_0e^{A_t+i\Theta_t}\).
6. Discover the logarithmic-spiral relation
   \(\Theta-\Theta_0=(\beta/\alpha)\log(R/R_0)\).
7. Recover \(X_t\) from \(R_t\).
8. Apply Itô's lemma directly.
9. Re-derive the SDE from polar coordinates.
10. Compute covariance as an outer product and formulate the rank theorem.
11. Derive the exact finite-step update.
12. Explore the failure of the literal real-axis log at zero.
13. Introduce stopping, Tanaka local time, and occupation density.
14. Verify all claims numerically.
15. End with the precise hierarchy of representations.

### Notebook standards

- execute from a clean kernel without hidden state;
- record the conda environment and package versions;
- use relative paths only;
- use deterministic seeds;
- place reusable figure code in functions;
- preserve executed outputs;
- report Monte Carlo standard errors;
- include assertions for every claimed exact or asymptotic relation;
- export publication figures from the same code used in the notebook;
- separate exploratory cells from final reproducible cells;
- keep the full runtime moderate enough for a clean rerun.

## 5. Visualization program

All final figures will have captions that state the mathematical message, not
merely describe the marks on the page.

| ID | Figure | Mathematical purpose |
|---|---|---|
| F1 | Discovery map | Flow from scalar process to log-radius, angle, and complex spiral |
| F2 | Linked sample path | Show \(X_t\), \(\log R_t\), \(R_t\), and unwrapped \(\Theta_t\) on a shared time axis |
| F3 | Complex-plane spiral | Plot \(Z_t\) with time coloring and the deterministic supporting spiral |
| F4 | Three-dimensional trajectory | Plot \((\Re Z_t,\Im Z_t,t)\) to show time evolution without implying planar noise |
| F5 | Parameter gallery | Compare circle, positive ray, expanding spiral, and contracting spiral cases |
| F6 | Local tangent/noise direction | Show that one Brownian increment moves only along one instantaneous direction |
| F7 | Covariance eigenspectrum | Compare rank-one polar covariance with the two-driver rank-two control |
| F8 | Covariance ellipses | Visualize a collapsed line ellipse versus a genuine planar ellipse |
| F9 | Exact multiplicative step | Decompose one update into radial scaling and angular rotation |
| F10 | Distribution checks | Overlay empirical radial densities and exact lognormal densities |
| F11 | Complex moment plane | Plot empirical complex moments with uncertainty against exact targets |
| F12 | Strong convergence | Log-log Euler–Maruyama error plot with fitted and \(1/2\) reference slopes |
| F13 | Zero-crossing anatomy | Show \(X_t\), \(|X_t|\), sign changes, and the origin |
| F14 | Tanaka decomposition | Compare reflected path, stochastic integral term, and accumulated local time |
| F15 | Occupation-density bands | Show how shrinking neighborhoods approximate local time |
| F16 | Representation taxonomy | Separate deterministic image, injective embedding, pathwise recovery, and planar-model equality |
| F17 | Claim hierarchy | Mark which statements are exact, localized, asymptotic, numerical, or heuristic |

### Figure production standards

- use Matplotlib/Seaborn for the canonical PDF figures;
- use Plotly only for exploratory notebook views or export it through Kaleido;
- prefer PDF or SVG vector output for curves, diagrams, and text;
- use PNG at 300 DPI or higher only when raster output is necessary;
- use a color-blind-safe palette that remains distinguishable in grayscale;
- use the same symbols, colors, and parameter values throughout;
- set single-column and full-width target sizes explicitly;
- avoid 3D figures unless the third dimension communicates time;
- add alternative text to every Quarto figure;
- confirm equations and labels remain legible in the final PDF;
- do not use a covariance ellipse to conceal an exactly zero eigenvalue:
  explicitly annotate the rank-one collapse.

## 6. Planned tables

| ID | Table | Contents |
|---|---|---|
| T1 | Notation | \(X,Z,R,\Theta,A,c,\alpha,\beta,\mu,\sigma\), brackets, and stopping times |
| T2 | Meaning of representation | Four representation notions and what each preserves |
| T3 | Parameter cases | Circle, ray, logarithmic spiral, and degenerate map |
| T4 | Formula summary | Itô drift/diffusion, brackets, inverse, moments, and exact step |
| T5 | Covariance rank | One-driver theorem versus two-driver control |
| T6 | Monte Carlo validation | Exact values, estimates, standard errors, and \(z\)-scores |
| T7 | Convergence | Step sizes, strong errors, ratios, and fitted slope |
| T8 | Local time | Grid size, discrete estimate, occupation estimate, error, and residual |
| T9 | Reproducibility | Seed, environment, package versions, and render commands |

## 7. Quarto manuscript architecture

Proposed directory:

```text
paper/
├── _quarto.yml
├── index.qmd
├── references.bib
├── README.md
├── environment.yml
├── notebooks/
│   └── phase3_discovery.ipynb
├── figures/
│   ├── vector/
│   └── raster/
├── tables/
├── styles/
│   ├── paper.scss
│   └── header.tex
└── output/
    └── phase3-one-driver-complex-embedding.pdf
```

The initial project should use Quarto's manuscript project type:

```yaml
project:
  type: manuscript

manuscript:
  article: index.qmd
```

The primary deliverable is PDF. An HTML manuscript preview is useful for
checking cross-references, notebook links, and accessibility, but publication
of a website is not part of this plan.

### Notebook-to-QMD workflow

1. Build and execute `phase3_discovery.ipynb`.
2. Save a clean executed copy as the derivation record.
3. Convert it explicitly:

   ```bash
   quarto convert paper/notebooks/phase3_discovery.ipynb \
     --output paper/index-draft.qmd
   ```

4. Editorially restructure `index-draft.qmd` into `paper/index.qmd`.
5. Make `index.qmd` the canonical paper source.
6. Keep the discovery notebook as supplementary computational provenance.
7. Do not round-trip repeatedly between `.ipynb` and `.qmd`, because repeated
   conversion can degrade carefully edited cross-references and layout.

The final `.qmd` will use Quarto equation, theorem, figure, table, and section
labels. Citations will use a checked `references.bib` file and Pandoc citation
syntax.

## 8. Reproducibility design

### Recommended environment choice

Create a new `phase3-paper` conda environment. This isolates publication
dependencies from the already-tested Phase 3 numerical environment and makes
the paper easier to reproduce.

Python 3.12 is recommended for the publication environment because it has
broad package compatibility. The existing `base` environment on this machine
also works for the mathematics and may be used if environment creation is
undesirable.

### Reproducibility artifacts

- `paper/environment.yml` with direct dependencies;
- an exact package/version table generated at render time;
- fixed seeds in both notebook and paper;
- one command that executes the notebook;
- one command that renders the PDF;
- a clean-kernel recheck;
- saved output hashes for the final PDF and principal figures;
- a short record of Quarto and TinyTeX versions;
- no absolute paths or machine-specific cache paths.

### Render workflow

After activating the selected environment:

```bash
quarto check
quarto render paper --to pdf
```

The render must be repeated from a clean state. The second PDF should have the
same substantive text, tables, and numerical output. Byte-for-byte PDF
identity is not required because PDF metadata can contain timestamps.

## 9. Toolchain audit on this machine

Audit date: 2026-07-23.

### Already installed

- CachyOS/Arch-compatible Linux;
- conda 25.11.1;
- Python 3.13.9 in `base`;
- Jupyter and JupyterLab;
- NumPy 2.3.5;
- SciPy 1.16.3;
- Matplotlib 3.10.6;
- Pandas 2.3.3;
- Seaborn 0.13.2;
- SymPy 1.14.0;
- Plotly 6.3.0;
- Altair 5.5.0;
- Statsmodels 0.14.5;
- nbformat, nbclient, and nbconvert;
- Pandoc 3.8;
- Chromium;
- `rsvg-convert`;
- Poppler PDF inspection tools (`pdfinfo`, `pdftotext`, `pdftoppm`).

### Missing core publishing tools

- Quarto CLI;
- TinyTeX or another TeX distribution;
- a LaTeX PDF engine supplied by TinyTeX.

### Missing recommended notebook/publication additions

- `jupyter-cache`;
- `jupyterlab-quarto`;
- Kaleido (`python-kaleido`) if Plotly figures are exported to PDF/SVG.

## 10. Installation plan

No installation should occur until this plan is approved.

### A. Required system-level installation

On this CachyOS machine, the available package is currently
`quarto-cli-bin` 1.9.38:

```bash
sudo pacman -S quarto-cli-bin
```

Then install Quarto's recommended compact TeX distribution:

```bash
quarto install tinytex
```

Verify it with:

```bash
quarto --version
quarto check
quarto list tools
```

TinyTeX supplies the LaTeX engine and packages needed for PDF rendering.
Quarto's PDF engine can automatically install missing TeX packages when using
TinyTeX or TeX Live.

Do not separately install `pdflatex`, `xelatex`, `lualatex`, `latexmk`, and a
full TeX Live distribution unless TinyTeX fails a specific requirement.

### B. Recommended new conda environment

```bash
conda create -n phase3-paper -c conda-forge \
  python=3.12 \
  numpy scipy pandas \
  matplotlib seaborn sympy \
  plotly python-kaleido \
  jupyter jupyterlab ipykernel \
  nbformat nbclient nbconvert jupyter-cache
```

Then:

```bash
conda activate phase3-paper
python -m pip install jupyterlab-quarto
python -m ipykernel install --user \
  --name phase3-paper \
  --display-name "Python (phase3-paper)"
```

`jupyterlab-quarto` is an editing convenience rather than a render-time
requirement. It makes Quarto front matter, callouts, citations, and other
Quarto markdown easier to inspect inside JupyterLab.

### C. Minimal additions if reusing `base`

The mathematical stack is already present. Only these additions are
recommended:

```bash
conda install -n base -c conda-forge jupyter-cache python-kaleido
conda run -n base python -m pip install jupyterlab-quarto
```

Quarto and TinyTeX are still required at the system/user tool level.

### D. Optional tools

- Zotero plus Better BibTeX for managing a larger bibliography;
- Graphviz only if DOT diagrams are preferred over Mermaid or Python figures;
- Inkscape only for manual figure editing;
- `scienceplots` only if a journal-specific Matplotlib style is desired;
- `conda-lock` only if cross-platform dependency locks become necessary.

These are not required for the initial paper. Quarto already supports Mermaid
and Graphviz syntax, Chromium is installed for diagram rendering, and
`rsvg-convert` is available for SVG conversion.

### E. Tools not required

- R or Julia;
- Typst;
- a separate standalone Pandoc installation;
- a full TeX Live installation;
- Microsoft Word;
- a LaTeX IDE;
- Plotly for the canonical figures.

## 11. Implementation phases and gates

### Stage 1: paper preflight

- approve title, audience, and paper scope;
- install or select the toolchain;
- create the paper directory;
- write and test a minimal `.qmd` to PDF;
- freeze notation and parameter conventions.

**Gate:** a one-page test PDF renders with equations, one figure, one table,
one citation, and one cross-reference.

### Stage 2: source and novelty audit

- expand the Phase 3 literature review;
- obtain stable bibliographic metadata;
- classify every claim as standard, derived here, computational, or
  interpretive;
- avoid novelty language unless the search supports it.

**Gate:** every externally sourced claim has a citation and every central
paper claim has a provenance classification.

### Stage 3: discovery notebook

- build the new narrative notebook;
- derive the construction step by step;
- add the visualization suite;
- execute from a clean kernel;
- cross-check against the original Phase 3 notebook.

**Gate:** all mathematical assertions pass and all final figure files are
generated reproducibly.

### Stage 4: paper draft

- convert the notebook to `index-draft.qmd`;
- reorganize it into the research-paper structure;
- shorten code output in the article;
- move extended derivations to appendices;
- add citations, theorems, cross-references, and captions.

**Gate:** the `.qmd` renders to both HTML preview and PDF without unresolved
references.

### Stage 5: mathematical and numerical audit

- independently re-derive every displayed SDE;
- check units and assumptions;
- verify covariance ranks and complex brackets;
- check localization and local-time conventions;
- re-run all Monte Carlo tables with fixed seeds;
- compare all paper values with notebook outputs.

**Gate:** no discrepancy remains between paper, discovery notebook, original
Phase 3 notebook, and exact formulas.

### Stage 6: PDF editorial pass

- inspect every PDF page visually;
- check figure placement and legibility;
- remove clipped equations and overfull tables;
- validate captions, numbering, citations, and bibliography;
- check grayscale and color accessibility;
- extract PDF text to detect missing glyphs;
- verify fonts and metadata.

**Gate:** the PDF is readable without the notebook and contains no rendering
defect.

### Stage 7: final reproducibility pass

- recreate or validate the conda environment;
- run the notebook twice from clean kernels;
- render the QMD twice;
- archive versions, commands, hashes, and final outputs;
- conduct the permitted GLM 5.2 second-opinion review;
- resolve all substantive findings.

**Gate:** paper, notebook, figures, tables, and environment manifest form a
self-contained reproducibility package.

## 12. Acceptance criteria

### Scope

- the paper is Phase-3-only;
- the two-driver process appears only as a clearly labelled control;
- no earlier-phase derivation is presented as part of the paper's result.

### Mathematics

- all assumptions and stopping conditions are explicit;
- \(\log|X|\), not \(\log X\), is used for signed scalar states;
- both \([Z,Z]\) and \([Z,\overline Z]\) are defined correctly;
- the rank theorem is stated as an instantaneous covariance result;
- state injectivity and phase unwrapping are not conflated;
- no finite Brownian increment is said to literally square to \(\Delta t\);
- numerical evidence is never substituted for proof.

### Computation

- deterministic seeds;
- clean top-to-bottom notebook execution;
- exact moment comparisons include Monte Carlo standard errors;
- coupled strong-error experiment uses at least four resolutions;
- local-time conventions match between derivation and code;
- every published number is generated or independently checked.

### Figures

- at least twelve substantive explanatory figures;
- vector output wherever practical;
- readable at final PDF size;
- consistent notation and color;
- captions explain the mathematical conclusion;
- alt text exists for every figure.

### Quarto and PDF

- valid `.qmd` source;
- all figures, tables, equations, theorems, and sections cross-reference
  correctly;
- bibliography resolves without missing keys;
- PDF renders from a clean environment;
- no clipped content, missing glyphs, or broken links;
- final PDF is accompanied by its discovery notebook and environment file.

## 13. Authoritative tool references

- Quarto download:
  <https://quarto.org/docs/download/>
- Quarto manuscripts:
  <https://quarto.org/docs/manuscripts/>
- Quarto manuscript components:
  <https://quarto.org/docs/manuscripts/components.html>
- Quarto with Python:
  <https://quarto.org/docs/computations/python.html>
- Notebook/QMD conversion:
  <https://quarto.org/docs/cli/convert.html>
- PDF engines and TinyTeX:
  <https://quarto.org/docs/output-formats/pdf-engine>
- Citations:
  <https://quarto.org/docs/authoring/citations.html>
- Cross-references and theorem blocks:
  <https://quarto.org/docs/authoring/cross-references>
- Diagrams:
  <https://quarto.org/docs/authoring/diagrams.html>
- JupyterLab Quarto extension:
  <https://quarto.org/docs/tools/jupyter-lab-extension.html>
- Plotly/Kaleido static export:
  <https://plotly.com/python/static-image-export/>

## 14. Recommended decision

Use a new `phase3-paper` conda environment, Quarto's manuscript project type,
TinyTeX for PDF generation, Matplotlib/Seaborn for canonical static figures,
and Plotly/Kaleido only for supplementary exploratory views.

Keep two durable sources:

1. the executed discovery notebook as the historical and computational record;
2. `index.qmd` as the edited canonical paper.

The next step, after approval and installation, is Stage 1: create the paper
directory and prove the full notebook-to-QMD-to-PDF toolchain with a one-page
smoke manuscript before drafting the paper.
