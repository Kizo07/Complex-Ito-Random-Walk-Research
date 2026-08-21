# Phase 8 — Simulation results record

**Date:** 2026-08-21
**Notebook:** `notebooks/phase8_cos_vanillas.ipynb` (builder
`notebooks/build_phase8_cos_vanillas.py`), executed clean in ~173 s,
seed `20260821`, zero errors.
**Module:** `phase8_cos.py` · **Tests:** `tests/test_phase8_cos.py`
(14/14 pass).
**Model:** Milestone-3 spread/basket, \(\sigma_1=1.5,\sigma_2=2.5\),
driver \(x_0=0,\mu=0.3,\sigma=0.8,c=1\), \(T=1\), \(r=0.05\), \(z_0=100\).

---

## 1. Real-potential resolvent \(L_A(s)\)

17 points on \(s\in[-4,4]\): forward-FK resolvent vs exact-skeleton MC
(200k paths). Max deviation 4.24 SE (at the extreme tilts where the MC
estimator of \(e^{-sA}\) is heavy-tailed; all central points within 2 SE).
Bounds \(0<L_A(s)\le e^{|s|T}\) and convexity verified in the unit suite;
deterministic-limit (\(\sigma\to0\)) agreement with
\(e^{-s\int_0^T\rho(X_t)dt}\) to \(1.5\cdot10^{-4}\) (documented FK grid
error at this discretization).

## 2. Characteristic function cross-validation

At \(u\in\{0.7,1.6,2.9\}\), spread weights: resolvent route
\(e^{iuz_0-u^2\beta T/2}L_A(\alpha u^2/2)\) vs clock-density route
(integral of \(e^{-u^2\alpha a/2}\) against the Milestone-4 Fourier density)
agree to \(10^{-5}\) — two independent deterministic constructions.

## 3. COS prices vs Monte Carlo

Spread call, strikes 88–112, COS(128 modes) vs conditional-Gaussian MC:

| K | COS | MC (SE) | |
|---|---|---|---|
| 88 | 11.414795 | 11.413487 (0.0059) | OK |
| 92 | 7.612942 | 7.611496 (0.0059) | OK |
| 96 | 3.898779 | 3.896773 (0.0055) | OK |
| 100 | 1.038546 | 1.037599 (0.0035) | OK |
| 104 | 0.093861 | 0.093752 (0.0010) | OK |
| 108 | 0.003107 | 0.002963 (0.00016) | OK |
| 112 | 0.000042 | 0.000019 (0.000007) | OK |

All within 4 SE; put–call parity to \(10^{-8}\); mode convergence
64→128 to \(10^{-5}\); deterministic-clock (\(\alpha=0\)) case reproduces
closed-form Bachelier to \(10^{-6}\); clock-quadrature and COS routes agree
to \(<2\cdot10^{-4}\) (unit suite).

## 4. Implied-correlation smiles (flagship)

Inverting constant-correlation Bachelier against stochastic-correlation
prices (clock-quadrature route), strikes 90–110:

| strike | spread implied ρ | basket implied ρ |
|---|---|---|
| 90 | −0.1068 | +0.2615 |
| 95 | −0.0450 | +0.2159 |
| 100 (ATM) | +0.1345 | +0.0820 |
| 105 | −0.0450 | +0.2159 |
| 110 | −0.1068 | +0.2615 |

Both smiles are exactly symmetric in moneyness (linear slope ≈ 0 to machine
precision — a consequence of the variance-mixture structure with no drift
in \(Z\)); the curvatures are **opposite**:
spread −2.385e-3, basket +1.770e-3.
Mechanism: variance-mixture tails raise wing implied variance; for spreads
higher variance maps to lower implied correlation, for baskets higher.
ATM implied correlations recover \(E[A_T]=0.1345\) (spread) directly.

## 5. Semi-analytic Greeks

Clock-density Greeks vs finite differences of the quadrature price:
delta, gamma, vega σ1, vega σ2 all agree to ≤ \(10^{-4}\) (unit suite);
notebook table shows analytic-vs-FD agreement at 6 decimals for delta/vegas.

## 6. Figures

`phase8_figures/`: `phase8_mgf.png`, `phase8_cos_vs_mc.png`,
`phase8_implied_corr_smiles.png`.

## 7. Numerical caveats (honest record)

- The resolvent route evaluates \(L_A(\alpha u^2/2)\) at large negative
  arguments for OTM spreads (\(|s|\) up to ~50 here): exponentially tilted
  mass concentrates near the domain boundary, so localization margins must
  grow with \(|s|\). In the tested regime both routes agree; for much larger
  \(|\alpha|T/u\)-regimes the clock-density route (oscillating frequencies
  only, \(|\phi_A(\xi)|\le1\)) is the robust default and is exposed as
  `clock_quadrature_call_price`.
- Payoff coefficients handle strikes outside the truncation band explicitly
  (three cases derived in-module); strikes above the band raise a
  configuration error instead of returning garbage.
