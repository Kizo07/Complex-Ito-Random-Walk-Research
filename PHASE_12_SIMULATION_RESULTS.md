# Phase 12 — Simulation results record

**Date:** 2026-08-21
**Notebook:** `notebooks/phase12_peg.ipynb` (builder
`notebooks/build_phase12_peg.py`), executed clean in ~2.5 s,
seed `20260821`, zero errors.
**Module:** `phase12_peg.py` · **Tests:** `tests/test_phase12_peg.py`
(7/7 pass).
**Reference model:** band \([-2\%,+3\%]\) log-mispricing; credibility
\(\lambda=-0.25,\sigma_z=0.9,c=1.1,\rho_0=0.3\to\rho_*=0.85\); \(r=5\%\);
free float \(\mu_f=-15\%,\sigma_f=35\%\).

---

## 1. Defended-band stationary law

Zero-drift case recovers the uniform law: sd matches
\((hi-lo)/\sqrt{12}\) to \(3\cdot10^{-9}\) (quadrature resolution);
±drift cases shift the mean in the correct direction with exponential-
trapezoid shapes (figure `phase12_band_stationary.png`).

## 2. De-peg clock

| horizon | P(\(\tau\leq T\)) | de-peg digital |
|---|---|---|
| 0.5 | 0.01714 | 0.01671 |
| 1.0 | 0.07726 | 0.07349 |
| 2.0 | 0.17785 | 0.16093 |
| 5.0 | 0.31713 | 0.24698 |

Pay-at-hit transform \(E[e^{-r\tau}]=0.37777\) — verified against exact
IG-density quadrature to \(10^{-6}\) (unit suite). Perpetual mass
\(e^{2\lambda\Delta}=0.4894\).

## 3. Shortfall swap (deterministic pricing)

Pays \((K-P_T)^+\), strike as fraction of parity, only if de-pegged by
\(T=2\):

| K | price |
|---|---|
| 0.70 | 0.004430 |
| 0.80 | 0.008631 |
| 0.90 | 0.014859 |
| 0.95 | 0.018850 |
| 0.98 | 0.021529 |

## 4. Simulation benchmark (200k paths, 250 steps)

De-peg frequency 0.17800 vs exact 0.17785 (SE 0.00086, within 1 SE).
Fraction of terminal log-prices below parity: 42.6%. The sampler uses the
perpetual-mass-corrected inverse transform — the earlier normalization bug
(which rescaled uniforms and doubled frequencies) is documented and fixed.

## 5. Figures

`phase12_figures/`: `phase12_band_stationary.png`, `phase12_hazard.png`,
`phase12_shortfall.png`.
