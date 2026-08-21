# Phase 10 — Simulation results record

**Date:** 2026-08-21
**Notebook:** `notebooks/phase10_matrix.ipynb` (builder
`notebooks/build_phase10_matrix.py`), executed clean in ~8 s,
seed `20260821`, zero errors.
**Module:** `phase10_matrix.py` · **Tests:** `tests/test_phase10_matrix.py`
(11/11 pass).
**Reference system:** \(n=3\), angles \((\alpha_0,\beta_0,\gamma_0)=
(0.3,-0.2,0.5)\), volatilities \((0.8,0.6,0.7)\), \(T=1\).

---

## 1. Structural checks

- PSD: minimum eigenvalue over 2,000 random angle draws: \(4\cdot10^{-10}\)
  (machine zero); unit diagonal to \(10^{-12}\); symmetry exact.
- Deterministic limit (\(\sigma=0\)): simulated matrices equal the static
  RBM map exactly.
- Free-entry identity \(R_{23}=\cos\alpha\cos\beta+\sin\alpha\sin\beta
  \cos\gamma\) verified against the general map on 50 random states.

## 2. Exact marginals vs Monte Carlo (300k paths, 200 steps)

| quantity | exact / GH | MC |
|---|---|---|
| \(\mathbb E[R_{12}(T)]\) (closed form) | 0.69372 | 0.69374 (SE 0.00067) |
| sd\((R_{12}(T))\) (closed form) | 0.36537 | 0.36537 |
| \(\mathbb E[R_{23}(T)]\) (GH, 30 pts/dim) | 0.54343 | 0.54432 (SE 0.00082) |
| sd\((R_{23}(T))\) (GH) | 0.45116 | 0.45059 |

## 3. Itô drift verification (dt = 1e-3, 400k paths per start)

| start \((\alpha,\beta,\gamma)\) | empirical drift | analytic |
|---|---|---|
| (0.3, −0.2, 0.5) | −0.4316 | −0.4298 |
| (1.0, 0.8, −0.6) | −0.5589 | −0.5594 |
| (−0.9, 0.4, 1.2) | −0.2212 | −0.2039 |

The endogenous mean reversion (curvature term) is present and quantitatively
correct at all three states.

## 4. European correlation derivatives (GH 40 pts/dim vs MC)

Calls on \(R_{23}(T)\):

| strike | GH | MC (SE) |
|---|---|---|
| −0.2 | 0.77088 | 0.77159 (0.00070) |
| 0.0 | 0.59329 | 0.59381 (0.00063) |
| +0.2 | 0.42673 | 0.42727 (0.00053) |
| +0.4 | 0.27566 | 0.27601 (0.00041) |
| +0.6 | 0.14564 | 0.14598 (0.00028) |

Digital \(R_{23}(T)\ge0.4\): GH 0.71248 vs MC 0.70950 (SE ≈ 0.00083).
All within ~1–3.5 SE; kinked payoffs converge polynomially in node count
(20→40 nodes differ by 2.4e-4, documented in the suite).

Exact term structure of \(\mathbb E[R_{23}(t)]\) over \(t\in[0.05,2]\)
computed by GH (figure `phase10_term_structure.png`).

## 5. Figures

`phase10_figures/`: `phase10_map.png`, `phase10_term_structure.png`.
