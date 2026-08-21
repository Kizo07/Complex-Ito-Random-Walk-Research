# Phase 7 — Literature review and novelty audit: time-inhomogeneous exactness and the correlation term structure

**Date:** 2026-08-21
**Status:** web-verified re-audit for Phase 7 scope (per `PHASE_7_13_PROGRAM_PLAN.md`).
Snippet/abstract-level unless marked ✔ (full text or abstract fetched).

---

## 1. What this phase adds

Phase 6 fixed constant driver coefficients \((\mu,\sigma)\). Phase 7 asks which
of the exact laws survive when the driver is

\[
dX_t=\mu(t)\,dt+\sigma(t)\,dW_t
\]

with *deterministic* time-dependent coefficients, and what correlation
term-structure objects become computable in closed form. The two new
mathematical claims to be audited:

1. **Static inheritance:** every law that depends on finitely many marginals
   or transitions of \(\rho_t=f(X_t)\) (transition density, expiry digitals,
   discrete range accruals, forward-start digitals, quantile curves
   \(q_\alpha(t)=f(m(t)+\sqrt{v(t)}\Phi^{-1}(\alpha))\)) remains a single
   closed form with \(m(t)=x_0+\int\mu\), \(v(t)=\int\sigma^2\).
2. **Proportional-drift barrier class:** if \(\mu(t)=\lambda\sigma^2(t)\)
   (drift proportional to instantaneous variance), then in operational time
   \(u=v(t)\) the driver is exactly drifted Brownian motion
   \(x_0+\lambda u+B_u\) (Dambis–Dubins–Schwarz), so *every*
   reflection-principle law of Phase 6 Milestones 1–2 survives verbatim with
   calendar time replaced by integrated variance; the diffusion level
   \(\sigma(\cdot)\) drops out of all barrier laws except through the clock
   \(v(t)\). Conversely, if \(\mu/\sigma^2\) is not constant, constant-level
   hitting becomes curved-boundary crossing in operational time, for which
   the literature provides no closed forms outside special families.

## 2. Prior art found (this phase's scope)

### 2.1 Boundary crossing for Brownian motion with time-dependent coefficients

- **Bachelier–Lévy reflection principle / linear boundaries**: classical;
  the only general family with elementary closed forms.
- **Daniels (1969, 1996)**, **Durbin (1992)** (*J. Appl. Prob.* 29, 291–304):
  first-passage of BM to *curved* boundaries — series of multiple integrals /
  integral-equation approximations ✔ (abstract fetched via Cambridge Core).
  No closed forms; error bounds only under concavity/convexity.
- **Wang & Pötzelberger (1997)**, **Pötzelberger & Wang (2001)**: explicit
  formulas for *piecewise-linear* boundaries, Monte Carlo evaluation,
  \(O(n^{-2})\) approximation of general boundaries ✔ (PDF fetched). They
  state explicitly: *"explicit formulas … exist only for linear boundaries
  and very few, if any, nonlinear boundaries."*
- **Kahale (2008, AAP 18)**: analytic crossing probabilities for special
  moving barriers (\(a+b\sqrt{T-t}\), logarithmic) via Schwartz-distribution
  method of images ✔ (PDF fetched). New special families, still isolated.
- Quadratic boundaries → Airy-function relations; square-root boundaries →
  hypergeometric densities (Groeneboom–Loh; Novikov et al.) — special ODE
  families, not transferable.
- **Conclusion:** the catalog of closed-form boundary crossings contains
  affine boundaries and isolated special families. A time-inhomogeneous
  driver hits a *constant* level iff, in operational time, Brownian motion
  crosses the curve \(b+m(t(u))\); this is affine in \(u\) precisely when
  \(m(t)\) is affine in \(v(t)\), i.e. \(\mu(t)=\lambda\sigma^2(t)\) a.e.
  The sufficiency direction is a one-line DDS argument (our Theorem 2); the
  necessity direction holds within the known catalog and is stated as such
  (a conjecture beyond it would require a new impossibility theorem, out of
  scope).

### 2.2 Correlation term structure

- Search for "stochastic correlation term structure", "forward correlation
  derivatives", "correlation smile term structure model" (2024–2026 window
  plus classics) returns: factor-HJM stochastic-volatility rate models
  (Sepp–Rakhmonov 2023–2025; Karbach–Khedher 2025 — vol term structures,
  not correlation), Wishart multi-curve models with stochastic spread
  (da Fonseca–Dawui–Malevergne 2023/2024 — stochastic correlation between
  curves via Wishart affinity; swaption pricing by approximation, no exact
  finite-time law of correlation entries), and pairwise/local-correlation
  smile literature (Langnau; Fengler–Herwartz–Werner; Ahdida–Alfonsi).
- **No published work found** that gives (i) an exact closed-form quantile
  term structure \(q_\alpha(t)\) of a stochastic correlation, (ii) exact
  forward-start correlation digitals, or (iii) a bootstrap of correlation
  digital quotes into model parameters. The Phase 6 audit's finding that
  bounded-correlation models stop at stationary densities or spectral
  expansions remains valid for the time-inhomogeneous extension.

### 2.3 Time-inhomogeneous bounded factors

- Time-dependent Jacobi processes: eigenfunction expansions break (non-autonomous
  generator); literature treats simulation/spectral numerics only.
- Teng–Ehrhardt–Günther-type tanh(OU) models with time-dependent parameters:
  no finite-time laws even with constant parameters; time dependence worsens.
- Nothing found combining deterministic coefficient curves with exact
  pushforward laws for bounded correlation states.

## 3. Novelty boundary for Phase 7

**Cannot be claimed:**
1. That Gaussian drivers with deterministic coefficients have closed-form
   marginals — trivial textbook material.
2. DDS/time-change arguments themselves (1930s–1960s classical).
3. Curved-boundary numerical methods (Durbin, Pötzelberger–Wang, etc.) — we
   *consume* them as the known frontier that makes our necessity remark
   meaningful.

**Can be claimed (after verification below):**
1. The *classification*: within the bounded-factor framework, static laws are
   invariant under arbitrary deterministic coefficient curves, while the full
   reflection toolkit survives exactly on the proportional-drift class
   \(\mu(t)=\lambda\sigma^2(t)\) — with all barrier laws depending on the
   coefficients only through integrated variance (parsimony corollary:
   \((c,\lambda)\) determine barrier prices; \(\sigma(\cdot)\) warps time).
2. Exact closed-form correlation quantile term structure
   \(q_\alpha(t)\), forward-start digitals, and a discrete bootstrap of
   \((c,\lambda^{\mathbb Q})\) from correlation-digital quotes — no published
   counterpart found.
3. Calendar-time discounting cost: pay-at-hit Laplace transforms lose closed
   form off constant \(\sigma\) (since \(\tau\) maps through \(v^{-1}\));
   stated as an honest limitation.

## 4. Verification tasks

1. ✔ Pötzelberger–Wang quote confirming linear-boundary exclusivity (PDF).
2. ✔ Durbin abstract confirming series/integral-equation status of curved
   boundaries (Cambridge Core).
3. ✔ Kahale abstract confirming isolated special families (Project Euclid).
4. Searches for exact correlation term structure returned none; recorded as
   negative evidence with query strings in the notebook record.
