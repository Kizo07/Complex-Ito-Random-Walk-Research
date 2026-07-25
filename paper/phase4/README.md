# Phase 4 paper reproducibility guide

This directory contains the independent technical paper **Native Complex
Geometric Brownian Motion: Itô correction, stochastic rotation, and
noise-dimension geometry**.

## Canonical sources

- `index.qmd` is the edited manuscript source.
- `RESEARCH_NOTES.md` records the primary-source and claim audit.
- `references.bib` contains the verified bibliography.
- `notebooks/build_phase4_discovery.py` generates the notebook structure.
- `notebooks/phase4_discovery.ipynb` preserves the executed computational
  investigation.
- `environment.yml` records the existing conda environment; the build does not
  install or update packages.

Generated publication figures and evidence tables are under `figures/` and
`tables/`. The final PDF, HTML companion, retained TeX, and notebook preview
are under `output/`.

## Rebuild

From the repository root:

```bash
conda run -n phase3-paper \
  python paper/phase4/notebooks/build_phase4_discovery.py

conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=900 \
  paper/phase4/notebooks/phase4_discovery.ipynb

quarto render paper/phase4
```

The notebook must be executed before rendering because the manuscript consumes
its deterministic figures, CSV files, and JSON summaries.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 conda run -n phase3-paper \
  python -m unittest discover -s tests -v

pandoc paper/phase4/RESEARCH_NOTES.md \
  --bibliography paper/phase4/references.bib \
  --citeproc -t html -o /tmp/phase4-research-notes.html

quarto inspect paper/phase4
```

The numerical notebook performs its own exact-identity, moment, covariance,
convergence, bracket, and artifact-manifest assertions. Reproducibility hashes
are recorded here after the final two clean notebook executions.

## Reproducibility hashes

The final two clean executions had identical code-cell sources and
deterministic stream text. SHA-256:

| Artifact | SHA-256 |
|:--|:--|
| executed notebook file | `453f3976e3a3baec8a9e26a20b37c415ee7ff5f6c357f4b448f64cf2555d7961` |
| canonical code-cell sources | `4673d786f7cd65ce28937856d21cbeef2e39a440c8e951af64826dc2aa8bb02a` |
| deterministic stream outputs | `07a1c0bd52c0fa08594358e43d89f24728a7d960425f95ba0464393d3ee8965b` |
| aggregate generated tables | `250dcd06f2003940d2a460c9fa4a0d3699f4f56fa41fd5f87a5e31c1cfc754a1` |
| canonical QMD manuscript | `f363776655bcf62ff89c1dc13f3d638327818da0cde61187f9d43a890bfab591` |

The aggregate table hash is computed over lexically sorted filenames, each
followed by a null byte and its exact file bytes.

## Scope

The article covers Phase 4 only. Complex geometric Brownian motion and
stochastic exponentials are treated as established theory. The paper's focus
is a modulus-preserving four-parameter synthesis, its rank-one one-driver
geometry, the Phase 3 subfamily, and the exact two-driver boundary.
