# Phase 9 — Simulation results record

**Date:** 2026-08-21
**Notebook:** `notebooks/phase9_estimation_empirical.ipynb` (builder
`notebooks/build_phase9_estimation.py`), executed clean in ~6 s,
seed `20260821`, zero errors.
**Module:** `phase9_estimation.py` · **Tests:** `tests/test_phase9_estimation.py`
(14/14 pass).
**Data:** local alpha-engine store (`/home/fire/Documents/alpha_engine/data`),
daily adjusted closes 2015-01-01 → 2026-08-14, four pairs, 60-day rolling
realized correlation (2,860 windows per pair).

---

## 1. Realized correlation series

| pair | mean | sd | range |
|---|---|---|---|
| XOM/CVX | +0.793 | 0.123 | [+0.338, +0.965] |
| JPM/BAC | +0.847 | 0.099 | [+0.498, +0.985] |
| KO/PEP | +0.700 | 0.120 | [+0.260, +0.947] |
| AAPL/MSFT | +0.550 | 0.223 | [−0.060, +0.953] |

## 2. Exact MLE vs Fisher-space competitors (in-sample, full series)

| pair | conj \(\mu/c\) | conj \(\sigma/c\) | conj logL | frw \(m\) | frw \(s\) | frw logL | fou \(\kappa\) | fou \(\theta\) | fou logL | AIC c/f/o |
|---|---|---|---|---|---|---|---|---|---|---|
| XOM/CVX | −0.020 | 1.169 | 8409.4 | −0.010 | 0.643 | 8447.9 | 1.90 | 1.160 | 8453.3 | −16815 / −16892 / **−16901** |
| JPM/BAC | +0.017 | 1.552 | 8857.8 | +0.009 | 0.639 | 9306.4 | 1.77 | 1.348 | 9311.4 | −17712 / −18609 / **−18617** |
| KO/PEP | −0.009 | 0.913 | 7396.4 | −0.007 | 0.548 | 7757.9 | 2.29 | 0.909 | 7764.4 | −14789 / −15512 / **−15523** |
| AAPL/MSFT | −0.032 | 0.841 | 6546.2 | −0.031 | 0.621 | 6678.0 | 1.41 | 0.661 | 6681.8 | −13088 / −13352 / **−13358** |

Reading: window-smoothed proxies are highly persistent, so the OU-in-Fisher
model wins AIC everywhere but with *weak* mean reversion
(\(\kappa\approx1.4\!-\!2.3\)/yr) — the persistence is largely an artifact of
overlapping windows (Section 4). Estimated drift ratios are small and
within their large standard errors (~0.11/yr at n≈2,900 daily increments).

## 3. Out-of-sample diagnostics (70/30 split)

All three models are formally rejected by marginal KS on every pair
(KS ≈ 0.17–0.27, p ≈ 0). This is expected and honest: overlapping-window
proxies violate the exact-skeleton observation scheme for ANY iid-increment
model. The state-correlation diagnostic adds separation: conjugate-RW and
Fisher-RW show z-state down to −2.6 (dynamic misspecification), while the
OU's z-state stays within ±1.2. Out-of-sample mean log predictive density:
OU ≥ Fisher-RW > conjugate-RW on every pair (e.g. XOM/CVX: 3.062 / 3.060 /
3.027) — the smoothed-proxy ranking, not the latent-truth ranking.

**Methodological point recorded:** marginal KS alone would have declared all
models equally bad; the state-correlation diagnostic is what identifies
*which* structure is missing.

## 4. Attenuation study (deterministic MC, 24 replications per cell)

True ratios \(\mu/c=0.2\), \(\sigma/c=0.467\); 2,500 simulated days:

| window | est. vol ratio (median) | attenuation factor | IQR |
|---|---|---|---|
| 20 | 0.564 | 1.209 | 0.219 |
| 40 | 0.177 | 0.379 | 0.072 |
| 60 | 0.118 | 0.253 | 0.043 |
| 120 | 0.036 | 0.077 | 0.015 |

Window noise damps the measured dynamics by ~4× at the empirically common
60-day choice; short windows can even inflate the ratio (heavy tails of
\(g(\hat\rho)\)). Consequence: fitted \(\sigma/c\) values from Section 2 are
attenuated lower bounds on the true latent volatility ratio.

## 5. Figures

`phase9_figures/`: `phase9_rho_series.png`, `phase9_pit_histograms.png`,
`phase9_attenuation.png`.

## 6. Verification anchors (unit suite)

Exact recovery of identified ratios from exact-skeleton data; likelihood
invariance under the scale equivalence; PIT machinery exact under true
parameters (KS p>0.05); misspecification detection via state-correlation
(|z|>4) where marginal KS has no power; OU quasi-MLE recovers
\((\kappa,\theta)\); information criteria rank the generating model.
