# Phase 6 — Milestone 2: exact prices for derivatives on the bounded correlation coordinate

**Date:** 2026-07-27
**Status:** derived and verified (unit tests + Monte Carlo in
`notebooks/phase6_correlation_derivatives.ipynb`)
**Builds on:** `PHASE_6_MILESTONE_1_FIRST_PASSAGE.md` (all notation as there)

---

## 1. Market setup and the risk-neutral drift question

The correlation state \(\rho_t=f(X_t)\), \(f(x)=x/\sqrt{x^{2}+c^{2}}\), is
driven by \(X_t=x_0+\mu t+\sigma W_t\). Correlation is **not a traded asset**,
so the market is incomplete in the correlation factor: equivalent martingale
measures are parameterized by the market price of correlation risk. For a
constant market price \(\lambda\), Girsanov's theorem changes only the drift:

\[
\mu^{\mathbb Q}=\mu^{\mathbb P}+\sigma\lambda,
\qquad
dX_t=\mu^{\mathbb Q}dt+\sigma dW_t^{\mathbb Q}.
\]

**Proposition (invariance of the exact class under measure change).**
*Every exact law of Milestones 1–2 — the transition density, the first-passage
CDF and density, the perpetual hitting probability, the band-exit probability,
and every price below — holds verbatim under any equivalent martingale measure
with constant correlation risk premium, with \(\mu\) replaced by
\(\mu^{\mathbb Q}\). The diffusion coefficient, the conjugate map, and the
bounded state space are unchanged.*

*Proof.* Girsanov with constant \(\lambda\) maps drifted Brownian motion to
drifted Brownian motion; the reflection-principle and scale-function
constructions depend on the path space only through the drift. \(\square\)

This is the P7 item of the problem list, resolved: the exact-kernel class is
*closed* under the measure changes that pricing requires. The economic content
of \(\lambda\) (the correlation risk premium) is a separate estimation
question and is explicitly out of scope here.

**Convention.** All prices below are at time 0, with constant risk-free rate
\(r\ge0\), under a chosen pricing measure with drift \(\mu=\mu^{\mathbb Q}\).
Write \(b=x(\rho^{*})-x_0>0\) for the conjugate barrier distance and
\(x(\rho)=c\rho/\sqrt{1-\rho^{2}}\).

## 2. Product 1 — correlation digital at expiry

Pays \(\mathbf 1_{\{\rho_T\ge\rho^{*}\}}\) at \(T\) (\(\rho^{*}\in(-1,1)\) arbitrary):

\[
\boxed{
V_{\mathrm{dig}}
=
e^{-rT}\,
\Phi\!\left(\frac{\mu T-b}{\sigma\sqrt T}\right)
}
\]

because \(\{\rho_T\ge\rho^{*}\}=\{X_T\ge x(\rho^{*})\}\) and \(X_T\) is Gaussian.
(For \(\rho^{*}\le\rho_0\) the same formula holds with \(b<0\); no barrier
crossing is required.)

## 3. Product 2 — one-touch, paid at expiry

Pays \(\mathbf 1_{\{\tau_\rho\le T\}}\) at \(T\), i.e. 1 if the correlation
level was touched at any time before expiry (\(\rho^{*}>\rho_0\)):

\[
\boxed{
V_{\mathrm{touch}}^{T}
=
e^{-rT}
\left[
\Phi\!\left(\frac{\mu T-b}{\sigma\sqrt T}\right)
+
e^{2\mu b/\sigma^{2}}\,
\Phi\!\left(-\frac{\mu T+b}{\sigma\sqrt T}\right)
\right].
}
\]

Immediate bounds used as tests:
\(V_{\mathrm{touch}}^{T}\ge V_{\mathrm{dig}}\) (the touch event contains the
expiry event), and \(V_{\mathrm{touch}}^{T}\to e^{-rT}\min(1,e^{2\mu b/\sigma^{2}})\)
as \(T\to\infty\) — for \(\mu<0\) the perpetual touch is *not* certain, so the
price stays strictly below \(e^{-rT}\) even at infinite horizon.

## 4. Product 3 — one-touch, paid at hit

Pays 1 *at the hitting time* \(\tau_\rho\) if \(\tau_\rho\le T\). The price is
\(E[e^{-r\tau}\mathbf 1_{\{\tau\le T\}}]\). Completing the square in the
inverse-Gaussian density with

\[
\gamma=\sqrt{\mu^{2}+2r\sigma^{2}}
\]

gives the key identity
\(e^{-rt}f^{(\mu)}_\tau(t)=e^{-b(\gamma-\mu)/\sigma^{2}}f^{(\gamma)}_\tau(t)\),
hence the closed form

\[
\boxed{
V_{\mathrm{touch}}^{\mathrm{hit}}
=
e^{-b(\gamma-\mu)/\sigma^{2}}
\left[
\Phi\!\left(\frac{\gamma T-b}{\sigma\sqrt T}\right)
+
e^{2\gamma b/\sigma^{2}}\,
\Phi\!\left(-\frac{\gamma T+b}{\sigma\sqrt T}\right)
\right].
}
\]

Consistency limits (all used as tests):

- \(r\to0^{+}\): \(\gamma\to|\mu|\) and the formula collapses to Product 2's
  undiscounted hitting probability, for both drift signs.
- \(T\to\infty\): \(V_{\mathrm{touch}}^{\mathrm{hit}}\to e^{-b(\gamma-\mu)/\sigma^{2}}\),
  the classical Laplace transform of the first-passage time.
- \(V_{\mathrm{touch}}^{\mathrm{hit}}\ge V_{\mathrm{touch}}^{T}\) for \(r>0\)
  (payment arrives no later).

## 5. Product 4 — discretely monitored correlation range accrual

Pays a fixed amount at each monitoring date \(0<t_1<\dots<t_n=T\) if the
correlation is inside a band: payoff \(\sum_i \mathbf 1_{\{\rho_\ell\le\rho_{t_i}\le\rho_h\}}\).
Most real range accruals monitor daily, so the discrete version is the
practically relevant one — and it is exact:

\[
\boxed{
V_{\mathrm{range}}
=
\sum_{i=1}^{n}
e^{-rt_i}
\left[
\Phi\!\left(\frac{x_h-x_0-\mu t_i}{\sigma\sqrt{t_i}}\right)
-
\Phi\!\left(\frac{x_\ell-x_0-\mu t_i}{\sigma\sqrt{t_i}}\right)
\right]
}
\]

with \(x_\ell=x(\rho_\ell)\), \(x_h=x(\rho_h)\) (either level may be
\(\mp1\), giving \(\pm\infty\) and recovering one-sided digitals).

Test anchors: the full band \((-1,1)\) prices to \(\sum_i e^{-rt_i}\); the
price is monotone in band width; a zero-width band prices to 0.

**Continuously monitored corridor** (payoff proportional to the occupation
time \(\int_0^T\mathbf 1_{\{\rho_\ell\le\rho_t\le\rho_h\}}dt\)) is *not* covered
by these formulas: it needs the occupation-time law of drifted Brownian
motion, known only through Laplace transforms that do not invert in
elementary functions. Deferred — see §7.

## 6. What this buys against the audit baseline

The Phase 6 audit (`PHASE_6_LITERATURE_REVIEW.md` §3, O1/O3) found that
barrier/touch structures under stochastic correlation admit only
approximations in every tractable competitor, because the underlying
first-passage problems are unsolved (Jacobi, OU-driven) or approximate
(von Mises). Products 2–4 above are, within the audited scope, the first
closed-form prices for correlation-barrier and correlation-range payoffs:

- Products 2–3 are exact up to the Gaussian CDF — no series, no transform
  inversion, no simulation;
- Product 4 is exact per monitoring date with daily monitoring, which is how
  range accruals are actually written;
- all of them inherit the risk-neutral extension for free (§1), with the
  correlation risk premium entering as the single free drift parameter.

## 7. Explicitly deferred

1. **Continuously monitored corridor** — occupation-time law required
   (resolvent route through the conjugate coordinate; the arc-sine law covers
   only \(\mu=0\)).
2. **Barrier options on traded assets under stochastic asset–asset
   correlation** — the genuine O1 target; needs the joint law of
   \((S_T,\sup S,\int\rho)\) or a two-dimensional extension. The correlation
   products here are the building blocks and the benchmark.
3. **Greeks in \(\rho_0\)** — the formulas are smooth in all parameters;
   sensitivities follow by differentiation (chain rule through \(b(\rho_0)\)).
   Verified numerically by bumping in the notebook rather than tabulated here.
4. **Calibration of \((\mu^{\mathbb Q},\sigma,c,\lambda)\)** — estimation stage.

## 8. Verification summary

| Claim | Check | Result |
|---|---|---|
| digital = Gaussian tail | hand formula, limits | unit tests |
| one-touch expiry = discounted §4.1 CDF | construction | unit tests |
| pay-at-hit identity \(e^{-rt}f^{(\mu)}=e^{-b(\gamma-\mu)/\sigma^2}f^{(\gamma)}\) | completing the square | derivation + limits tests |
| \(r\to0\) limit of Product 3 = Product 2 undiscounted | both drift signs | unit tests, \(10^{-10}\) |
| \(T\to\infty\) = classical Laplace transform | direct evaluation | unit tests, \(10^{-12}\) |
| ordering touch-hit \(\ge\) touch-expiry \(\ge\) digital | parameter sweep | unit tests |
| range accrual anchors (full band, monotonicity) | evaluation | unit tests |
| all prices vs Monte Carlo | exact skeleton + bridge correction, seed `20260727` | notebook, within ~2 SE |
