# Phase 6 — Milestone 6: the OU driver and the stationarity–tractability classification

**Date:** 2026-07-27
**Status:** derived and verified (unit tests + Monte Carlo in
`notebooks/phase6_ou_driver.ipynb`)
**Builds on:** Milestones 1–5
**Module:** `phase6_ou.py` · **Tests:** `tests/test_phase6_ou.py`

This milestone delivers item O2 of the Phase 6 audit: replacing the
arithmetic-Brownian driver by an Ornstein–Uhlenbeck driver makes the
correlation coordinate mean-reverting — the standard economic desideratum —
and the framework's job is to say *exactly* which tractability survives the
switch and which does not.

---

## 1. The two drivers

**BM driver (Milestones 1–5):**
\(X_t=x_0+\mu t+\sigma W_t\). Non-stationary; \(\rho_t\to\operatorname{sgn}(\mu)\) a.s.

**OU driver (this milestone):**
\[
dX_t=\kappa(\bar x-X_t)\,dt+\sigma\,dW_t,\qquad \kappa>0,
\]
with Gaussian transition and stationary law
\(X_\infty\sim N\!\left(\bar x,\frac{\sigma^{2}}{2\kappa}\right)\).
The correlation coordinate \(\rho_t=f(X_t)=X_t/\sqrt{X_t^{2}+c^{2}}\) inherits
mean reversion (monotone image of a mean-reverting process) and has an exact
stationary density by change of variables.

## 2. The classification theorem

*Statement.* For the bounded correlation coordinate \(\rho_t=f(X_t)\) with
\(f(x)=x/\sqrt{x^{2}+c^{2}}\), driven by a scalar Gaussian factor \(X\):

| # | Object | BM driver | OU driver |
|---|---|---|---|
| 1 | Stationarity / mean reversion | **no** | **yes** (exact stationary density) |
| 2 | Finite-time transition density | closed form (Gaussian in conjugate coordinate) | closed form (same, OU moments) |
| 3 | Digital / discrete range accrual prices | closed form | closed form |
| 4 | First-passage CDF, density, perpetual probability | closed form (reflection principle) | **no closed form** (series only, Ricciardi–Sato / Alili–Patie–Pedersen); deterministic FK/PDE computation instead |
| 5 | DDS variance clock for two-asset linear combinations | exact (driver-agnostic) | exact (driver-agnostic) |
| 6 | Clock moments \(E[A_T]\), \(\operatorname{Var}(A_T)\) | Gauss quadrature | Gauss quadrature (OU bivariate law) |
| 7 | Full clock law | FK resolvent | FK resolvent (OU generator) |
| 8 | Measure-change invariance with constant risk premium \(\lambda\) | \(\mu\to\mu^{\mathbb Q}=\mu+\sigma\lambda\) | \(\bar x\to\bar x^{\mathbb Q}=\bar x+\sigma\lambda/\kappa\) |

*Proof sketch.* Rows 1–3: OU transition is Gaussian; the conjugate map is
deterministic and monotone, so all static laws and static-payoff prices are
exact change-of-variables. Row 4: OU first passage is classical unsolved
closed-form territory; nothing in the conjugate map repairs it, because
hitting probabilities are path properties, not marginal properties — the
reflection principle is Brownian-specific. Row 5: the Dambis–Dubins–Schwarz
argument conditions on the *realized* correlation path and never sees the
driver's generator. Rows 6–7: both drivers have jointly Gaussian
finite-dimensional laws, so the same quadrature and Feynman–Kac machinery
apply with the appropriate (co)variance and drift terms. Row 8: Girsanov
with constant \(\lambda\) adds a constant to the OU drift, which is
equivalent to shifting the long-run mean. \(\square\)

**Corollary (the frontier).** *Reflection-principle first-passage laws and
stationarity are mutually exclusive in this model class*: a scalar Gaussian
factor with a Gaussian stationary law cannot be a Brownian motion, and only
Brownian motion has reflection-principle hitting laws. Mean reversion is
bought by surrendering the closed-form barrier laws to the FK resolvent;
everything static and everything clock-based survives intact.

## 3. What is delivered computationally

1. Exact transition and stationary densities of \(\rho\) under OU
   (`ou_rho_transition_density`, `ou_rho_stationary_density`).
2. Exact digital price under OU (Gaussian tail with OU moments).
3. Clock moments under OU by triangle-aware Gauss quadrature with the OU
   bivariate law: for \(s<t\),
   \(X_t=\bar x+e^{-\kappa(t-s)}(X_s-\bar x)+\) independent increment.
4. The FK resolvent generalized to state-dependent drift
   (\(\mu\to\kappa(\bar x-x)\)), giving first-passage/occupation laws under
   OU deterministically — the deterministic replacement for the lost
   closed forms.
5. The **\(\kappa\to0^{+}\) anchor**: OU degenerates to the BM driver, and
   every OU formula is checked against the Milestone 1–4 formulas in that
   limit (tests enforce agreement).

## 4. Economic reading

The OU-driver model answers the mean-reversion objection (Teng et al.'s
desiderata (i)–(iii) are all satisfied: bounded support, variation around a
mean, vanishing boundary mass *with exact finite-time and stationary
densities*, unlike the modified-OU tanh model whose finite-time density is
not closed form). The price paid vs. Milestones 1–5: correlation-barrier and
touch prices move from closed form to deterministic PDE computation. Where
the two-asset DDS reduction applies (spread/basket barriers), the pricing
cost is unchanged, because the FK clock layer was already the computational
engine of Milestones 3–4.

## 5. Explicitly deferred

- Calibration/estimation under the OU driver (exact likelihood is immediate
  from row 2; the study is statistical, not probabilistic).
- Non-constant correlation risk premium (\(\lambda_t\) state-dependent):
  leaves the Gaussian class.
- Leverage (still the main structural open problem).

## 6. Verification summary

| Claim | Check | Result |
|---|---|---|
| OU transition density | normalization; \(\kappa\to0\) matches Milestone 1 density | unit tests |
| OU stationary density | normalization; transition \(\to\) stationary as \(T\to\infty\) | unit test + notebook |
| OU digital price | Gaussian tail vs density integral | unit test |
| OU clock moments | \(\kappa\to0\) matches Milestone 3 quadrature; \(\operatorname{Var}(A_T)\) reduced vs BM | unit tests |
| FK with OU generator | \(\phi(0)=1\), symmetry, first moment vs quadrature | unit tests |
| \(\kappa\to0\) full-pricing anchor | FK clock price vs Milestone 4 value | unit test |
| OU spread one-touch price | FK vs exact-skeleton MC benchmark | notebook, ~2 SE |
| classification table | rows verified individually as above | this table |
