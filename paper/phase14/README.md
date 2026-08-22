# Phase 14 — Hidden Exactness in Bounded-Factor Stochastic Models

This isolated Quarto project contains the Phase 14 flagship paper by Kanav
Mehta. The manuscript has 81 cited references, eight scientific figures, and
technical appendices supporting every principal derivation.

## Sources

- canonical manuscript: `index.qmd`
- bibliography: `references.bib`
- source and novelty audit: `RESEARCH_NOTES.md`
- visual styles: `styles/paper.scss` and `tex/header-includes.tex`
- deterministic evidence builder: `scripts/build_phase14_figures.py`
- structured values: `tables/`
- vector/raster figures: `figures/vector/` and `figures/raster/`

## Build

From the repository root:

```bash
conda run -n phase3-paper python paper/phase14/scripts/build_phase14_figures.py
quarto render paper/phase14
```

The existing `phase3-paper` conda environment is used without mutation. All
stochastic illustrations use seed `20260822`.

## Outputs

- `output/hidden-exactness-bounded-factor-models.pdf`
- `output/hidden-exactness-bounded-factor-models.html`
- `output/_tex/index.tex`

The project remains local and unpublished.
