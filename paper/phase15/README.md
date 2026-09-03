# Phase 15 paper reproducibility guide

This directory contains the independent technical paper **American Calls
and Puts under Black–Scholes–Merton from One-Driver Complex Geometric
Brownian Motion: phase-barrier geometry, a reference boundary solver, and
the collocated logarithmic-spiral pricing formula**.

## Canonical sources

- `index.qmd` is the manuscript source.
- `references.bib` contains the bibliography.
- `notebooks/phase15_discovery.ipynb` is the executed computational
  record (copy of the repository-root executed notebook).
- `tables/benchmark_reduced.csv`, `tables/phase15_summary.json`,
  `tables/benchmark_extended.csv` are the machine-readable results.
- `environment.yml` records the existing conda environment; the build
  does not install or update packages.

Generated figures are under `figures/`; the PDF and retained TeX are
under `output/`.

## Rebuild

From the repository root:

```bash
conda run -n phase3-paper \
  python notebooks/build_phase15_american_spiral.py

conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=540 \
  notebooks/phase15_american_spiral.ipynb

cp notebooks/phase15_american_spiral.ipynb \
   paper/phase15/notebooks/phase15_discovery.ipynb
cp phase15_figures/*.png paper/phase15/figures/

quarto render paper/phase15
```

The notebook must be executed before rendering because the manuscript
quotes its numbers.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 conda run -n phase3-paper \
  python -m unittest tests.test_phase15_american -v
```

The 14 tests cover: dividend put–call parity, perpetual value matching
and smooth pasting, maturity anchors, the q = 0 call limit, boundary
monotonicity and value-matching residuals, published Ju-exhibit benchmark
values, McDonald–Schroder symmetry against independently solved
boundaries, CRR–Richardson cross-check, spiral limits and
short-maturity asymptotics, collocation residuals, spiral-beats-BAW at
ATM, and formula price bounds.
