# Technical Papers

This directory contains two independent Quarto manuscript projects. Each
project owns its notebook, figures, tables, bibliography, styles, filters, and
rendered outputs.

## Phase 3

**A Faithful One-Driver Complex Embedding of Arithmetic Brownian Motion**

- canonical manuscript: [`phase3/index.qmd`](phase3/index.qmd)
- discovery notebook:
  [`phase3/notebooks/phase3_discovery.ipynb`](phase3/notebooks/phase3_discovery.ipynb)
- PDF:
  [`phase3/output/phase3-one-driver-complex-embedding.pdf`](phase3/output/phase3-one-driver-complex-embedding.pdf)
- HTML:
  [`phase3/output/phase3-one-driver-complex-embedding.html`](phase3/output/phase3-one-driver-complex-embedding.html)

Render from the repository root:

```bash
quarto render paper/phase3
```

## Phase 4

**Native Complex Geometric Brownian Motion**

- canonical manuscript: [`phase4/index.qmd`](phase4/index.qmd)
- research record: [`phase4/RESEARCH_NOTES.md`](phase4/RESEARCH_NOTES.md)
- discovery notebook:
  [`phase4/notebooks/phase4_discovery.ipynb`](phase4/notebooks/phase4_discovery.ipynb)
- PDF:
  [`phase4/output/phase4-native-complex-geometric-brownian-motion.pdf`](phase4/output/phase4-native-complex-geometric-brownian-motion.pdf)
- HTML:
  [`phase4/output/phase4-native-complex-geometric-brownian-motion.html`](phase4/output/phase4-native-complex-geometric-brownian-motion.html)

Render from the repository root:

```bash
quarto render paper/phase4
```

The two projects are deliberately self-contained. Rendering one does not
modify the source, cache, figures, tables, or output directory of the other.
