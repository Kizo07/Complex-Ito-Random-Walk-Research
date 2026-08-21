# Phase 7 — Simulation results record

**Date:** 2026-08-21
**Notebook:** `notebooks/phase7_term_structure.ipynb` (deterministic builder
`notebooks/build_phase7_term_structure.py`), executed clean in ~21 s,
seed `20260821`, zero errors.
**Module:** `phase7_term_structure.py` · **Tests:** `tests/test_phase7_term_structure.py`
(21/21 pass; full-suite status recorded at phase end).
**Environment:** conda `phase3-paper`, Python 3.12.13, numpy 2.5.1,
scipy 1.18.0, matplotlib 3.11.1.

---

## 1. Scenarios

| scenario | \(\sigma(t)\) | \(v(2)\) |
|---|---|---|
| constant | \(1\) | 2.000000 |
| humped | \(0.9+0.4te^{-t}\) | 2.078244 |
| oscillating | \(\sqrt{1+0.6\cos(\pi t)}\) | 2.000000 |

Driver drift for static-layer checks: \(\mu(t)=0.3(1+0.5e^{-t})\).
Proportional-class checks use \(\mu(t)=\lambda\sigma^2(t)\), \(\lambda=0.35\),
\(c=1.1\), \(\rho_0=-0.2\).

## 2. Static inheritance (Theorem 1)

| check | result |
|---|---|
| transition density vs Phase 6 (constant coefficients), 9 points | \(10^{-13}\) |
| transition density normalization (quad, 2 maturities) | \(10^{-8}\) |
| expiry digitals vs MC (200k exact-skeleton paths): 0.53280/0.53390 (SE 0.00110), 0.44901/0.44998 (0.00112), 0.31893/0.32006 (0.00106) | all within 1.6 SE |
| discrete range accrual per date vs MC, 5 dates | max gap 0.00033 (≈0.5 SE) |
| range accrual total: model 2.52752 vs MC 2.52476 | within 1.1 SE |
| forward-start digital tower property (GH in conjugate coordinate) | \(10^{-10}\) |
| quantile term structure vs MC empirical quantiles, 15 (α,t) points | max error 0.0033 |

## 3. Proportional-drift barrier class (Theorem 2)

Hitting \(\rho^*=0.55\) by \(T=2\), bridge-corrected exact-skeleton MC
(200k paths, two step sizes):

| curve | \(u(T)=v(2)\) | exact CDF | MC(100) | MC(400) |
|---|---|---|---|---|
| humped | 2.078244 | 0.67685 | 0.67608 (SE 0.00105) | 0.67628 (0.00105) |
| oscillating rescaled to same \(u(T)\) | 2.078244 | 0.67685 | 0.67766 (0.00105) | 0.67605 (0.00105) |

Parsimony corollary verified operationally: different volatility curves with
equal integrated variance give *identical* exact barrier CDFs; both MC runs
agree with the shared closed form within 1 SE.

Calendar-time hitting-time density vs MC frequency histogram (800 steps):
mean absolute bin deviation 0.0096 (histogram-scale).

Unit-test anchors: constant-\(\sigma\) member of the class reproduces
Milestone-1 CDF/density/perpetual/band formulas to \(10^{12}\); density
integrates to the CDF (\(10^{-7}\)) and to the perpetual mass (\(10^{-3}\),
slow IG tail documented).

## 4. Forward Feynman–Kac solver (the pitfall and the fix)

**Finding.** The backward equation
\(\partial_tu=L_tu+i\xi f(x)u\) — exact for constant coefficients and the
Phase-6 engine — is **violated** by
\(u(t,x)=\mathbb E_x[e^{i\xi\int_0^tf(X_s)ds}]\) under deterministic
coefficient curves. Counterexample used in the module documentation:
\(\sigma=0,\ \mu(t)=t\) gives the true solution
\(e^{i\xi(xt+t^3/6)}\), which fails the equation by \(i\xi t^2/2\cdot u\).
Root cause: the derivation requires time-translation invariance of the
propagator, which deterministic coefficient curves destroy. The correct
primitive is the **forward** Feynman–Kac (Fokker–Planck with potential)
equation for the tilted density \(p\):

\[
\partial_tp=\tfrac12\sigma^2(t)p_{xx}-\mu(t)p_x+i\xi f(x)p,\qquad
p(0,x)=\delta(x-x_0),\qquad \phi(\xi)=\textstyle\int p(T,x)\,dx .
\]

**Verification of the fixed solver.**

| check | result |
|---|---|
| constant coefficients vs Milestone-4 expm solver (\(\xi=0.7,2.1\)) | \(2\cdot10^{-4}\) (grid 2000) |
| **closed-form Gaussian case** (linear potential, variable coefficients) \(\xi=0.3,0.8\) | \(4.2\cdot10^{-4}\) (grid 3600) |
| spatial convergence, linear-potential case (\(\xi=0.3\)) | 1.69e-3 → 4.22e-4 → 1.05e-4 across grid doublings 900→1800→3600 (clean second order) |
| \(\phi(0)=1\) under variable curves | \(10^{-6}\) |
| localization margin 8 vs 16 at fixed \(h\) | \(<10^{-3}\) |
| bounded map vs MC, \(\xi=0.5,1.5,3.0\) (humped vol) | all real/imag parts within 4 SE |
| \(E[A_T]\): PDE central difference 0.13452 vs exact marginal quadrature 0.13454 vs MC 0.13648 (SE 0.0019) | PDE–quadrature \(2\cdot10^{-5}\) |

For contrast, the *incorrect* backward-equation solver (initial bug) gave
\(\phi(0.5)=0.9060+0.0428j\) against the true \(0.9094+0.0651j\) and an
implied \(E[A_T]\) of 0.0892 against the exact 0.13454 — the failure mode is
invisible on first moments of marginals and appears only in path-functional
law checks, which is why marginal-only validation would have missed it.

## 5. Term-structure bootstrap

Synthetic market of five correlation digitals generated from
\((c,\lambda)=(1.25,0.30)\), humped vol, \(\rho_0=-0.2\), \(r=0.04\):
least-squares recovery gives \((1.25000000, 0.30000000)\), max residual
\(<10^{-8}\); the SSE landscape is single-funnel in \((\log c,\lambda)\)
(figure `phase7_bootstrap.png`).

## 6. Figures

`phase7_figures/`: `phase7_vol_scenarios.png`,
`phase7_transition_density.png`, `phase7_quantile_term_structure.png`,
`phase7_proportional_hitting_density.png`, `phase7_bootstrap.png`.
