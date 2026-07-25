# One-Phase Euler Coordinates paper

This directory is the independent publication project for **One-Phase Euler
Coordinates for Affine Brownian Factors: Exact Classification, Pricing
Conjugacy, and Numerical Consequences**.

## Canonical sources

- `index.qmd` — edited academic manuscript;
- `RESEARCH_NOTES.md` — primary-source, claim, and novelty audit;
- `references.bib` — verified bibliography;
- `notebooks/build_one_phase_euler_finance.py` — deterministic notebook source;
- `notebooks/one_phase_euler_finance.ipynb` — executed research notebook;
- `figures/` and `tables/` — generated publication evidence; and
- `output/` — rendered PDF, HTML, TeX, and notebook companion.

The notebook imports the tested repository modules `phase5_model.py` and
`phase5_finance.py`. No package installation or environment mutation is part
of the build.

## Rebuild

From the repository root:

```bash
conda run -n phase3-paper \
  python paper/one-phase-euler/notebooks/build_one_phase_euler_finance.py

conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=1200 \
  paper/one-phase-euler/notebooks/one_phase_euler_finance.ipynb

quarto render paper/one-phase-euler
```

## Verification

```bash
PYTHONDONTWRITEBYTECODE=1 conda run -n phase3-paper \
  python -m unittest discover -s tests -v

pandoc paper/one-phase-euler/RESEARCH_NOTES.md \
  --bibliography paper/one-phase-euler/references.bib \
  --citeproc -t html -o /tmp/one-phase-euler-research-notes.html

quarto inspect paper/one-phase-euler
```

Final verification:

- 39/39 full-project tests pass;
- the notebook has 46 cells, 22 sequentially executed code cells, and zero
  error outputs;
- two clean-kernel runs produced byte-identical 44-file structured-evidence
  bundles;
- the artifact set contains 22 raster and 22 vector figures;
- the PDF has 47 letter-size pages and all fonts are embedded;
- the HTML contains all 22 figures with nonempty alt text, 52 bibliography
  entries, and no broken internal links; and
- OpenCode `zai-coding-plan/glm-5.2` returned **PASS WITH MINOR FINDINGS**,
  with both findings resolved and no critical or major defect.

Reproducibility identifiers:

```text
structured-evidence ledger
3c3d0625edc69175bd9bbac792d581fb7b5ee0c42f07cada9df6f406a4fa2df3

executed notebook
5f673a88f5bb15cc4c1c2790b876dae70f93cdda19d4e3337ebf84032bc4156e

canonical QMD
117a2799bca58e7afd0d089bce176c01dccdd3c203c93b36a1509bc1d49d203c

PDF
7f64602ef98b40df096a8b108eaa686bc0e46b701d838549340b9a41480bc988

HTML
f9a83b59968d106c2efda7993d742c247575b722d27a76b2dfffb0c9af119647

OpenCode review usage ID
61d151d7-1472-4571-a4dc-ed1089a0ecb0

scorecard evaluation ID
92e9a611-3108-40b5-b12d-5488204e79a8
```

The complete command record and acceptance evidence are in
`../../.agent/evidence/TASK-008-verification.md`.
