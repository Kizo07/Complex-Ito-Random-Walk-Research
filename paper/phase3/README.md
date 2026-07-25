# Phase 3 paper reproducibility guide

This directory contains the paper
**A Faithful One-Driver Complex Embedding of Arithmetic Brownian Motion:
Itô Dynamics, Covariance Rank, and Zero Crossings**.

## Canonical sources

- `index.qmd` is the edited paper source.
- `notebooks/phase3_discovery.ipynb` records the computational discovery path.
- `notebooks/build_phase3_discovery.py` regenerates the notebook structure.
- `references.bib` contains the checked bibliography.
- `environment.yml` records direct Python dependencies.

Generated figures and tables are written under `figures/` and `tables/`.
The final PDF and HTML companion are written under `output/`.

## Rebuild

From the repository root:

```bash
conda run -n phase3-paper \
  python paper/phase3/notebooks/build_phase3_discovery.py
conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=900 \
  paper/phase3/notebooks/phase3_discovery.ipynb
quarto render paper/phase3
```

The notebook must be executed before rendering because the paper consumes its
generated figures and CSV/JSON summaries. The notebook uses deterministic
seeds, relative paths, and assertions for exact identities and numerical
tolerances. A second clean execution reproduces the same 15 code-cell outputs
exactly.

## Scope

The article covers Phase 3 only. The two-driver planar process appears solely
as a control for interpreting covariance rank; it is not presented as an
equivalent representation of the scalar process.
