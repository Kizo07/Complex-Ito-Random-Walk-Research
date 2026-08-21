# Phase 11 — Simulation results record

**Date:** 2026-08-21
**Notebook:** `notebooks/phase11_levy.ipynb` (builder
`notebooks/build_phase11_levy.py`), executed clean in ~321 s,
seed `20260821`, zero errors.
**Module:** `phase11_levy.py` · **Tests:** `tests/test_phase11_levy.py`
(9/9 pass).
**Drivers:** VG(\(\sigma=0.35,\nu=0.8,\theta=-0.12\));
NIG(\(\alpha=8,\beta=-2,\delta=1.1,\mu=0.03\)); \(T=1,x_0=0,c=1,b=0.15\).

---

## 1. Marginal laws (Gil–Pelaez vs exact samplers, 300k paths)

Digital \(1\{\rho_T\ge0.5\}\):

| driver | exact | MC (SE) |
|---|---|---|
| VG | 0.02018 | 0.01989 (0.00025) |
| NIG | 0.01257 | 0.01222 (0.00020) |

Driver densities and bounded-factor marginals plotted against sampler
histograms (`phase11_driver_laws.png`, `phase11_rho_marginals.png`).

## 2. Clock characteristic function across drivers

Variance-matched Gaussian baseline (\(\sigma^2=\sigma_{VG}^2+\nu\theta^2\)):

| \(\xi\) | Gaussian | VG PIDE (MC) | NIG PIDE (MC) |
|---|---|---|---|
| 0.5 | +0.9949+0.0334j | +0.9960+0.0092j (+0.9960+0.0087j) | +0.9948−0.0243j (+0.9949−0.0220j) |
| 1.0 | +0.9796+0.0660j | +0.9841+0.0187j (+0.9840+0.0177j) | +0.9793−0.0478j (+0.9798−0.0432j) |
| 2.0 | +0.9204+0.1255j | +0.9384+0.0388j (+0.9383+0.0369j) | +0.9196−0.0895j (+0.9214−0.0807j) |
| 3.0 | +0.8284+0.1729j | +0.8685+0.0612j (+0.8685+0.0586j) | +0.8275−0.1201j (+0.8313−0.1081j) |

PIDE vs MC agree to ~1–2 SE everywhere; largest-\(\xi\) VG real-part check
passes at 5 SE.

## 3. Scientific findings

1. **Jump asymmetry halves the clock mean**: \(\mathbb E[A_T]\) is 0.0730
   under the variance-matched Gaussian but 0.0350 under VG
   (\(\theta<0\) pushes the driver down; the concave-then-saturating map
   converts that into a materially lower time-average correlation).
2. **NIG with \(\beta<0\) flips the sign of the clock drift**
   (Im \(\phi_A(\xi)<0\)): the time-average correlation becomes negative
   despite identical marginal calibration of the driver variance — a
   falsifiable jump signature invisible to any marginal-only analysis.
3. The clock *distribution* (Fourier-inverted PIDE transform) shows the VG
   density shifted and left-skewed relative to the Gaussian
   (`phase11_clock_densities.png`), with the MC histogram confirming.

## 4. Verification anchors (unit suite)

Sampler cumulants match closed forms (VG/NIG); exponent-vs-sampler
characteristic-function check; Gil–Pelaez CDF vs empirical quartiles
(<0.01); digital monotonicity/bounds; FK-PIDE: \(\phi(0)=1\); **linear-
potential closed form** via integrated characteristic exponent; **tiny-jump
NIG limit reproduces the Phase-7 forward-FK Gaussian solver** (<0.02).

## 5. Numerical caveats

- Jump localization requires generous margins (jump tails are heavy);
  margin-doubling verified in-notebook.
- Implicit-Euler time error is first-order but cheap here because one LU
  factorization serves all steps; second-order schemes are a straightforward
  upgrade if needed.
- Runtime ~320 s dominated by the 900-point CF grid for Fourier inversion.

## 6. Figures

`phase11_figures/`: `phase11_driver_laws.png`, `phase11_rho_marginals.png`,
`phase11_clock_densities.png`.
