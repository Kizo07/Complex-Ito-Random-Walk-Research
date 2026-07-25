# TASK-008 verification ledger

## Completion state

TASK-008 is complete as of 2026-07-25. Work remained local on branch
`phase-4-technical-paper`; no commit, push, pull request, publication, or
release action was performed.

The protected untracked file `critique2.md` was not edited, moved, staged, or
deleted.

## Deliverables

The completed publication project is `paper/one-phase-euler/` and contains:

- the canonical Quarto manuscript and project configuration;
- a 52-entry cited bibliography and section-by-section source audit;
- a deterministic notebook builder and executed notebook;
- 22 raster figures and 22 vector companions;
- 44 CSV/JSON evidence files;
- PDF, HTML, retained TeX, and notebook-companion outputs;
- a reproducible finance module and focused tests; and
- publication and repository-level READMEs.

The paper proves the exact criterion

\[
\exists\,r,\theta_t:\quad
Z_t=Z_0r(\theta_t)e^{i\theta_t}
\text{ losslessly in one genuine phase}
\quad\Longleftrightarrow\quad
\frac{a}{b}\in\mathbb R
\ \text{and}\
\frac{b}{Z_0}\notin\mathbb R
\]

for \(Z_t=Z_0+a t+bW_t\) with \(Z_0b\ne0\). With
\(a=\lambda b\) and \(b/Z_0=\rho e^{i\phi}\), the exact reconstruction is
\(Z_t=Z_0\sin\phi\,e^{i\theta_t}/\sin(\phi-\theta_t)\), with the stated phase
interval and inverse. The manuscript separately proves the phase diffusion
theory, rigidity results, group transport, and financial-pricing conjugacy,
and it states the limits of those results.

## Test gate

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 conda run -n phase3-paper \
  python -m unittest discover -s tests -v
```

Result:

```text
Ran 39 tests in 0.012s
OK
```

This includes the six finance-specific tests in
`tests/test_phase5_finance.py` and the complete pre-existing project suite.

## Notebook and numerical gate

- Environment: unchanged `phase3-paper` conda environment.
- Notebook cells: 46 total, including 22 code cells.
- Saved execution counts: the consecutive sequence 1 through 22.
- Error outputs: zero.
- Clean-kernel executions: two.
- Run-to-run result: byte-identical structured evidence bundles.
- Deterministic seeds and Monte Carlo uncertainty: recorded in the notebook
  and evidence tables.
- Current structured-evidence ledger: 44 files.
- Current path-independent ledger SHA-256:

  `3c3d0625edc69175bd9bbac792d581fb7b5ee0c42f07cada9df6f406a4fa2df3`.

The ledger digest is the SHA-256 of lexicographically ordered standard
`sha256sum` records over the 44 table basenames. It can be reproduced from
`paper/one-phase-euler/tables` with:

```bash
sha256sum $(find . -maxdepth 1 -type f \
  \( -name '*.csv' -o -name '*.json' \) -printf '%f\n' | sort) \
  | sha256sum
```

Selected saved numerical checks:

| Check | Result |
|:--|--:|
| Maximum direct-versus-phase price error | \(2.7755575615628914\times10^{-17}\) |
| Maximum delta reconstruction error | \(1.7563087206795558\times10^{-8}\) |
| Maximum gamma reconstruction error | \(5.806385084961008\times10^{-7}\) |
| Maximum pricing-PDE residual | \(8.122450385894542\times10^{-10}\) |
| Brownian-bridge path-average standard deviation | \(0.004267495185143631\) |
| Two-factor covariance rank | \(2\) |

All notebook terminal assertions passed.

## Publication gate

Final Quarto render:

```text
Output created:
paper/one-phase-euler/output/
  one-phase-euler-affine-brownian-factors.pdf
  one-phase-euler-affine-brownian-factors.html
```

PDF checks:

- 47 pages;
- letter size, \(612\times792\) points;
- one-inch margins specified in the rendered configuration;
- every listed font reports `emb=yes`;
- no unresolved citation or cross-reference marker was found;
- all 47 page thumbnails were inspected on a contact sheet; pages 1, 7, 15,
  31, 40, and 47 were additionally inspected at full size; and
- no clipping, overlap, missing figure, or malformed equation was observed.

HTML checks:

```text
images: 22
empty alt attributes: 0
missing local image sources: 0
internal IDs: 355
broken internal fragments: 0
bibliography entries: 52
```

Every bibliography entry is cited. The research-notes citeproc audit also
completed successfully. `git diff --check` passes.

## Final artifact hashes

```text
index.qmd
117a2799bca58e7afd0d089bce176c01dccdd3c203c93b36a1509bc1d49d203c

references.bib
4f0b56b199a1420264425679748bef9c7bb3d0e085a8db68bbc0542d8325ecca

notebooks/build_one_phase_euler_finance.py
848a0e0a6ed3f313f3d3873c8ce54c885eefe94d472f3b0974ebb7912caae4b8

notebooks/one_phase_euler_finance.ipynb
5f673a88f5bb15cc4c1c2790b876dae70f93cdda19d4e3337ebf84032bc4156e

one-phase-euler-affine-brownian-factors.pdf
7f64602ef98b40df096a8b108eaa686bc0e46b701d838549340b9a41480bc988

one-phase-euler-affine-brownian-factors.html
f9a83b59968d106c2efda7993d742c247575b722d27a76b2dfffb0c9af119647

phase5_finance.py
7d618773b8661e5ae2c1c669a09712c746cfd79e9963419e8bf3dac6dcf83509

tests/test_phase5_finance.py
6cae63d779b61dfdb45f53b58d82a34b9175fd7c5ddc07962c76dc4d45a4e0af
```

## Independent review

OpenCode `zai-coding-plan/glm-5.2` returned **PASS WITH MINOR FINDINGS** and
found no critical or major defect. Both minor findings were valid and
resolved before the final render.

- Usage ID: `61d151d7-1472-4571-a4dc-ed1089a0ecb0`
- Scorecard evaluation ID: `92e9a611-3108-40b5-b12d-5488204e79a8`
- Review record:
  `.agent/reviews/TASK-008-opencode-glm52-review.md`
