# Technical Papers

This directory contains three independent Quarto manuscript projects. Each
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

## One-Phase Euler Coordinates

**One-Phase Euler Coordinates for Affine Brownian Factors: Exact
Classification, Pricing Conjugacy, and Numerical Consequences**

- canonical manuscript:
  [`one-phase-euler/index.qmd`](one-phase-euler/index.qmd)
- research record:
  [`one-phase-euler/RESEARCH_NOTES.md`](one-phase-euler/RESEARCH_NOTES.md)
- reproducible notebook:
  [`one-phase-euler/notebooks/one_phase_euler_finance.ipynb`](one-phase-euler/notebooks/one_phase_euler_finance.ipynb)
- PDF:
  [`one-phase-euler/output/one-phase-euler-affine-brownian-factors.pdf`](one-phase-euler/output/one-phase-euler-affine-brownian-factors.pdf)
- HTML:
  [`one-phase-euler/output/one-phase-euler-affine-brownian-factors.html`](one-phase-euler/output/one-phase-euler-affine-brownian-factors.html)

Render from the repository root:

```bash
quarto render paper/one-phase-euler
```

All three projects are deliberately isolated: rendering one does not modify
the sources, caches, figures, tables, or outputs of either other project.

## Phase 7

**Exact Term Structure of Stochastic Correlation: Static Inheritance, the
Proportional-Drift Class, and a Feynman–Kac Pitfall**

- manuscript: [`phase7/index.qmd`](phase7/index.qmd)
- outputs: [`phase7/output/`](phase7/output/) (HTML + PDF)

## Phase 8

**Fourier Pricing of Spread and Basket Options under Stochastic
Correlation**

- manuscript: [`phase8/index.qmd`](phase8/index.qmd)
- outputs: [`phase8/output/`](phase8/output/) (HTML + PDF)

## Phase 9

**What Can Be Estimated? Scale Observational Equivalence and Exact Maximum
Likelihood for Bounded-Factor Correlation Models**

- manuscript: [`phase9/index.qmd`](phase9/index.qmd)
- outputs: [`phase9/output/`](phase9/output/) (HTML + PDF)

## Phase 10

**Phase-Gram: Correlation-Matrix Processes with Exact Finite-Time Law from
Gaussian-Driven Triangular Angles**

- manuscript: [`phase10/index.qmd`](phase10/index.qmd)
- outputs: [`phase10/output/`](phase10/output/) (HTML + PDF)

## Phase 11

**Lévy-Powered Bounded Factors: What Survives of Exact Correlation Laws
under Jump Drivers**

- manuscript: [`phase11/index.qmd`](phase11/index.qmd)
- outputs: [`phase11/output/`](phase11/output/) (HTML + PDF)

## Phase 12

**The Economics of De-Peg: Defended Bands, Credibility Clocks, and
Closed-Form De-Peg Derivatives**

- manuscript: [`phase12/index.qmd`](phase12/index.qmd)
- outputs: [`phase12/output/`](phase12/output/) (HTML + PDF)

All six follow the same isolated-project layout as phases 3/4/6. Render:

```bash
quarto render paper/phaseN   # N in {7,...,12}
```
