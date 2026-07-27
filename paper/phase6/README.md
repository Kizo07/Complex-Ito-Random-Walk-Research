# Exact Bounded Correlation paper

This directory is the independent publication project for **Exact Bounded
Correlation: One-Phase Euler Coordinates for Stochastic Correlation,
Derivative Pricing, and Joint Barriers** (Phase 6 of the research program).

## Canonical sources

- `index.qmd` — edited academic manuscript;
- `RESEARCH_NOTES.md` — primary-source, claim, and novelty audit;
- `references.bib` — bibliography;
- `notebooks/build_phase6_correlation_paper.py` — deterministic notebook source;
- `notebooks/phase6_correlation_paper.ipynb` — executed research notebook;
- `figures/` and `tables/` — generated publication evidence; and
- `output/` — rendered PDF, HTML, TeX, and notebook companion.

The notebook imports the tested repository modules `phase6_correlation.py`,
`phase6_joint.py`, `phase6_fk.py`, `phase6_corridor.py`, and `phase6_ou.py`.
No package installation or environment mutation is part of the build.

## Rebuild

From the repository root:

```bash
conda run -n phase3-paper \
  python paper/phase6/notebooks/build_phase6_correlation_paper.py

conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=1200 \
  paper/phase6/notebooks/phase6_correlation_paper.ipynb

quarto render paper/phase6
```

## Verification

```bash
PYTHONDONTWRITEBYTECODE=1 conda run -n phase3-paper \
  python -m unittest discover -s tests -v

pandoc paper/phase6/RESEARCH_NOTES.md \
  --bibliography paper/phase6/references.bib \
  --citeproc -t html -o /tmp/phase6-research-notes.html

quarto inspect paper/phase6
```

The supporting milestone documents at the repository root
(`PHASE_6_FINANCE_APPLICATION_PROBLEM_LIST.md`, `PHASE_6_LITERATURE_REVIEW.md`,
`PHASE_6_MILESTONE_1_..._6_*.md`) contain the full derivations, the economic
selection record, and the honest bias/cost analyses summarized in the
manuscript.
