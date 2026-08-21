# The Exact-Kernel Bounded-Factor Framework for Stochastic Correlation

## Flagship consolidation — Phases 1–13

**Date:** 2026-08-21 · **Status:** full suite 192/192 tests, all notebooks
executed clean (seed `20260821` throughout), every claim web-audited.

---

## Abstract

We develop an exact-law framework for stochastic correlation built on a
single primitive: a Gaussian (or Lévy) driver pushed through the bounded map
\(\rho_t=x_t/\sqrt{x_t^2+c^2}\). Unlike Jacobi-type or hyperbolic-OU
correlation processes — where the audited literature stops at stationary
densities, spectral expansions, or Monte Carlo — every law a derivatives
desk needs is available in closed form or as a deterministic quadrature:
first-passage and band-exit laws (reflection principle), occupation-clock
characteristic functions (Feynman–Kac), vanilla spread/basket prices by
one-dimensional Fourier inversion, correlation-matrix laws by
Gaussian-driven triangular angles, exact closed-form estimation, and a
fully deterministic de-peg derivative stack. Four structural discoveries
emerged from forcing *exactness*: (i) the backward Feynman–Kac equation —
exact for constant coefficients and the workhorse of the field — fails for
deterministic coefficient curves (drift-only counterexample), and the
correct primitive is the forward Fokker–Planck-with-potential equation;
(ii) the model is scale-observationally-equivalent: only \((\mu/c,\sigma/c)\)
are identifiable, from correlation observations *and* derivative prices
alike; (iii) barrier-law exactness under time-varying coefficients survives
on precisely the proportional-drift class \(\mu(t)=\lambda\sigma^2(t)\),
where volatility curves collapse to a clock; (iv) jump-driven correlation
flips the sign of the correlation-clock drift while leaving marginals
calibrated. We validate every object against independent benchmarks
(closed forms, exact samplers, bridge-corrected Monte Carlo within ~1 SE)
and demonstrate the framework empirically on four S&P 500 pairs.

---

## Part I — The exact-kernel core (Phases 1–6, recap)

Driver \(dX=\mu\,dt+\sigma\,dW\); bounded coordinate
\(\rho=f(X)=x/\sqrt{x^2+c^2}\). Exact objects:

| law | form |
|---|---|
| transition density | Jacobian × Gaussian pdf in conjugate coordinate |
| hitting CDF / IG density / perpetual | reflection principle |
| first-exit through upper edge | scale function |
| corridor/residence-time laws | FK resolvent + spectral decomposition |
| DDS clock \(v=\beta T+\alpha A_T\) | spread/basket variance is affine in \(A_T=\int\rho\) |
| clock characteristic function | forward-FK PDE (Phase 7 correction below) |

Sign corollary: credibility deterioration (\(\lambda<0\)) raises
spread-barrier prices and lowers basket-barrier prices — falsifiable, and
confirmed ex post by Phase 8's smile geometry.

## Part II — Time-inhomogeneous exactness (Phase 7)

**Theorem (static inheritance).** For deterministic curves
\(\mu(\cdot),\sigma(\cdot)\), every finite-marginal/transition law of
\(\rho\) is the constant-coefficient formula with
\(m(t)=x_0+\int\mu,\ v(t)=\int\sigma^2\). Includes the exact quantile term
structure \(q_\alpha(t)=f(m(t)+\sqrt{v(t)}\Phi^{-1}(\alpha))\) — not
published anywhere audited.

**Theorem (proportional-drift barrier class).** If
\(\mu(t)=\lambda\sigma^2(t)\), operational time \(u=v(t)\) makes the driver
exactly \(x_0+\lambda u+B_u\): every reflection law survives with
\(t\to v(T)\), depending on \(\sigma(\cdot)\) only through \(u=v(T)\)
(parsimony). Off this class the known catalog has no closed forms (Durbin;
Wang–Pötzelberger; Kahale audits).

**Discovery (the FK pitfall).** The backward equation
\(\partial_tu=L_tu+q(x)u\) is violated by
\(u(t,x)=E_x[e^{q\int_0^tf(X_s)ds}]\) when coefficients depend on calendar
time. Counterexample: \(\sigma=0,\mu(t)=t\) gives true solution
\(e^{q(xt+t^3/6)}\neq\) PDE solution. Root cause: semigroup time-translation
invariance fails. Correct primitive: **forward** Feynman–Kac
(Fokker–Planck with potential) started from a delta bump; implemented with
Crank–Nicolson, verified against closed-form Gaussian cases, clean
second-order convergence, and MC within 4 SE. The failure mode is invisible
to marginal checks — only path-functional validation catches it.

**Term-structure bootstrap:** two-parameter least squares on correlation
digitals recovers \((c,\lambda^{\mathbb Q})\) to \(10^{-8}\) on synthetic
markets (identification holds here because \(\sigma(\cdot)\) is exogenous).

## Part III — Vanilla spread/basket options (Phase 8)

**Theorem (exact one-dimensional transform).**
\[
\phi_Z(u)=e^{-rT}e^{iuz_0-\frac12u^2\beta T}\,
L_A\!\Big(\frac{\alpha u^2}{2}\Big),\qquad
L_A(s)=E[e^{-sA_T}],
\]
with \(L_A\) a real-potential FK resolvent. Boundedness confines
\(A_T\in(-T,T)\): the transform exists for **all** real \(s\). COS inversion
(Fang–Oosterlee) plus a robust clock-density-quadrature route give
deterministic European prices (MC-verified within ~1 SE across strikes),
semi-analytic Greeks from the clock density, and the model's falsifiable
signature: implied-correlation smiles that are exactly symmetric in
moneyness with **opposite curvature** for spreads (−2.4e-3) vs baskets
(+1.8e-3); ATM implied correlation equals \(E[A_T]\) exactly. Audited
multi-asset Fourier methods (2-D COS, tensor-train) require the joint CF
and contain no stochastic-correlation models.

## Part IV — Estimation and identifiability (Phase 9)

**Theorem (scale observational equivalence).** \((c,\mu,\sigma)\sim
(\lambda c,\mu/\lambda,\sigma/\lambda)\) induce identical laws for every
observable correlation functional — and for every derivative price, since
the clock depends only on the \(\rho\)-path. Identified parameters:
\((\mu/c,\sigma/c)\), estimated in **closed form** (OLS in the normalized
coordinate) — vs stationary-density least squares (Teng et al.) and ad-hoc
back-transformed OLS (Kumar et al.) in the audited literature.

Empirics (four S&P pairs, 2015–2026, local store): vol ratios 0.84–1.55;
drift ratios statistically zero; window-smoothing attenuates measured
dynamics ~4× at the standard 60-day window; marginal KS rejects *all*
iid-increment models on smoothed proxies while the PIT-state-correlation
diagnostic separates them — marginal calibration tests alone mislead.

## Part V — Correlation matrices: Phase-Gram (Phase 10)

Driving Rebonato–Jäckel/Rapisarda–Brigo–Mercurio triangular angles with
independent Brownian motions yields matrix-valued correlation processes
that are PSD/unit-diagonal **by construction**, have **exact**
finite-dimensional laws (every European functional = \(d=n(n-1)/2\)-dim
Gauss–Hermite product), closed-form pairwise marginals, analytic entry
drifts with endogenous curvature mean-reversion
\(\mu_{R_{23}}=-\tfrac12(\sigma_\alpha^2+\sigma_\beta^2)R_{23}-\ldots\),
verified against MC to third decimals. Audited angle parameterizations are
static calibration tools; no stochastic-Gaussian-angle exact-law competitor
exists.

## Part VI — Lévy-powered drivers (Phase 11)

With VG/NIG drivers: marginals stay exact (Gil–Pelaez pushforward); the
clock transform survives via the **backward** FK-PIDE (time-homogeneous ⇒
translation-invariant semigroup — the pitfall does not bite);
reflection-principle barrier laws die honestly. Findings: variance-matched
VG halves \(E[A_T]\) (0.073→0.035); NIG \(\beta<0\) flips its sign — a
jump signature invisible to any marginal-only analysis. Solver validated
against the integrated-exponent closed form and the tiny-jump Gaussian
limit.

## Part VII — Pegged assets (Phase 12)

De-peg = first passage of a bounded credibility factor. Full deterministic
derivative stack: defended-band stationarity (exponential trapezoid),
de-peg CDF/density/perpetual, pay-at-hit Laplace
\(E[e^{-r\tau}]=\exp((\lambda-\sqrt{\lambda^2+2r/\sigma_z^2})\Delta)\),
hazard-contingent shortfall swaps as one quadrature over the exact IG
density. Simulation (perpetual-mass-corrected inverse transform) matches
exact frequencies within 1 SE. De-peg probabilities are strongly concave in
horizon — capped by perpetual mass — a feature exponential-hazard models
miss.

## Master verification table

| phase | module | tests | notebook | headline anchor |
|---|---|---|---|---|
| 7 | phase7_term_structure | 21/21 | ~21 s | linear-potential closed form; second-order convergence |
| 8 | phase8_cos | 14/14 | ~173 s | COS vs MC ≤4 SE all strikes; parity 1e-8 |
| 9 | phase9_estimation | 14/14 | ~6 s | ratio recovery; likelihood invariance theorem |
| 10 | phase10_matrix | 11/11 | ~8 s | PSD machine-zero; GH vs MC ≤~3 SE |
| 11 | phase11_levy | 9/9 | ~321 s | integrated-exponent closed form; tiny-jump limit |
| 12 | phase12_peg | 7/7 | ~3 s | Laplace vs quadrature 1e-6; freq vs CDF ~1 SE |
| all | **192/192** | | | full suite green 2026-08-21 |

## The five headline claims (all web-audited)

1. **Forward-FK primality**: the correct occupation-transform engine for
   non-autonomous drivers, with an explicit counterexample against the
   naive backward extension (new).
2. **Scale observational equivalence** of bounded-factor correlation
   models, covering derivative prices (new).
3. **Exact one-dimensional CF of spreads/baskets under stochastic
   correlation** with global real-potential resolvents (new), delivering
   deterministic multi-asset pricing where the field uses MC.
4. **Opposite-curvature implied-correlation smiles** with ATM level
   \(=E[A_T]\) — a direct empirical test of stochastic correlation (new).
5. **Phase-Gram processes**: Gaussian-driven triangular angles give
   constraint-free correlation-matrix dynamics with exact finite-time laws
   (new).

## Limitations (honest register)

- Pay-at-hit discounting loses closed form off constant \(\sigma\) (maps
  through \(v^{-1}\)).
- Product-rule Gauss–Hermite caps Phase-Gram dimension at \(n\approx4\);
  larger n needs sparse grids.
- Realized-correlation proxies are smoothed observations: attenuation ~4×
  at 60-day windows; state-space filtering of proxy noise is future work.
- Lévy barrier laws need absorbing-type PIDEs (reflection formulas dead).
- Lévy FK solver is first-order in time (one LU amortizes all steps).

## Repository map (phases 7–13)

`PHASE_{7..13}_{LITERATURE_REVIEW, SIMULATION_RESULTS, SYNTHESIS}.md`,
modules `phase7_term_structure.py … phase12_peg.py`,
tests `tests/test_phase{7..12}_*.py`, builders + executed notebooks
`notebooks/`, figures `phase{7..12}_figures/`, program plan
`PHASE_7_13_PROGRAM_PLAN.md`.
