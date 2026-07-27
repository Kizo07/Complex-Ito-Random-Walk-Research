# Phase 6 — Milestone 3: joint two-asset barrier options under stochastic correlation

**Date:** 2026-07-27
**Status:** derived and verified (unit tests + Monte Carlo in
`notebooks/phase6_joint_barrier.ipynb`)
**Builds on:** Milestones 1–2 (`PHASE_6_MILESTONE_1_FIRST_PASSAGE.md`,
`PHASE_6_MILESTONE_2_CORRELATION_DERIVATIVES.md`)
**Module:** `phase6_joint.py` · **Tests:** `tests/test_phase6_joint.py`

This is the O1 target of the Phase 6 problem list: barrier-type payoffs whose
price *genuinely depends* on stochastic correlation, treated exactly.

---

## 1. Model

Two traded forward prices (martingales under the forward measure — drifts are
removed by the choice of numéraire, so no drift terms appear):

\[
dF_1=\sigma_1\,dW_1,\qquad
dF_2=\sigma_2\big(\rho_t\,dW_1+\sqrt{1-\rho_t^{2}}\,dW_2\big),
\]

with normal volatilities \(\sigma_1,\sigma_2>0\) (Bachelier convention,
consistent with the additive framework of the project), and the bounded
correlation coordinate of Milestones 1–2:

\[
\rho_t=\frac{X_t}{\sqrt{X_t^{2}+c^{2}}},\qquad
X_t=x_0+\mu t+\sigma W_t .
\]

**Structural assumption (stated, not hidden):** the correlation driver \(W\) is
*independent* of the asset drivers \((W_1,W_2)\). This is the van
Emmerich/Teng–Ehrhardt–Günther construction, and it is what buys conditional
Gaussianity below. The cost is real: the model has no leverage effect between
returns and correlation (correlation does not respond to asset moves). Where
this assumption fails, the clean reduction of §3 fails with it; see §7.

## 2. Lemma — conditional Gaussianity

*Conditional on the whole correlation path \(\rho_{[0,T]}\), the pair
\((F_1,F_2)\) is a Gaussian process with zero mean and deterministic
covariance function determined by \(\rho_{[0,T]}\).*

*Proof.* \(F_1\) and the two stochastic integrals defining \(F_2\) are Itô
integrals against \((W_1,W_2)\) with integrands that are deterministic once
\(\rho_{[0,T]}\) is fixed (bounded, hence square-integrable). Itô integrals
with deterministic integrands are Gaussian; independence of \(W\) from
\((W_1,W_2)\) makes the conditioning free. \(\square\)

## 3. Theorem — deterministic variance clock for linear combinations

Let \(Z=\alpha_1F_1+\alpha_2F_2\) for constants \(\alpha_1,\alpha_2\)
(spread: \((1,-1)\); basket: \((1,1)\)). Then \(Z\) is a continuous local
martingale with quadratic variation

\[
\langle Z\rangle_t
=\int_0^{t}\Big[\big(\alpha_1\sigma_1+\alpha_2\sigma_2\rho_s\big)^{2}
+\alpha_2^{2}\sigma_2^{2}\big(1-\rho_s^{2}\big)\Big]ds
=\int_0^{t}q(\rho_s)\,ds,
\]

\[
\boxed{
q(\rho)=\alpha_1^{2}\sigma_1^{2}+\alpha_2^{2}\sigma_2^{2}
+2\alpha_1\alpha_2\sigma_1\sigma_2\,\rho .
}
\]

Conditional on \(\rho_{[0,T]}\), this quadratic variation is *deterministic*,
so by the Dambis–Dubins–Schwarz theorem, conditionally on \(\rho\),

\[
Z_t\ \stackrel{\mathrm{law}}{=}\ z_0+B_{v(t)},
\qquad
v(t;\rho)=\int_0^{t}q(\rho_s)\,ds ,
\]

with \(B\) a standard Brownian motion and \(z_0=\alpha_1F_{1,0}+\alpha_2F_{2,0}\).

**Corollary (scalar reduction of joint barrier laws).** For an upper barrier
\(d>z_0\),

\[
\boxed{
\mathbb P\!\left(\sup_{t\le T}Z_t\ge d\ \Big|\ \rho_{[0,T]}\right)
=
2\Big(1-\Phi\!\Big(\frac{d-z_0}{\sqrt{v(T;\rho)}}\Big)\Big),
}
\]

and analogously for lower barriers and for the joint law of \((\sup Z,Z_T)\).
*Every* claim measurable with respect to the running extrema of \(Z\) —
one-touches, barrier digitals, lookbacks on the spread/basket — prices as

\[
V=e^{-rT}\,\mathbb E_{\rho}\big[\,g\big(v(T;\rho)\big)\big]
\]

with \(g\) a closed form of the scalar \(v(T;\rho)\). The three-dimensional
pricing problem \((F_1,F_2,\rho)\) collapses to the law of **one scalar
functional** of the correlation path.

**Sign corollary (spread vs. basket).** The \(q\)-coefficient of \(\rho\) is
\(2\alpha_1\alpha_2\sigma_1\sigma_2\): *negative* for the spread, *positive*
for the basket. Correlation risk therefore moves spread-barrier and
basket-barrier prices in **opposite directions**, and a model with constant
correlation misprices the two in opposite senses. This is a qualitative,
testable prediction of the framework.

**Why the driftless (forward) form matters.** With nonzero drift, the running
supremum of \(Z\) depends on the whole path \(v(\cdot)\), not only on
\(v(T)\), and the scalar collapse fails. Working with forward prices under the
forward measure removes drifts exactly; barrier options on futures/forwards
are the natural habitat of the theorem.

## 4. The law of the clock: exact moments

Since \(q\) is affine in \(\rho\), with \(A_T=\int_0^{T}\rho_s\,ds\),

\[
v(T;\rho)=\big(\alpha_1^{2}\sigma_1^{2}+\alpha_2^{2}\sigma_2^{2}\big)T
+2\alpha_1\alpha_2\sigma_1\sigma_2\,A_T ,
\]

so all moments of the clock reduce to moments of the occupation integral
\(A_T\) of the correlation coordinate:

\[
\mathbb E[A_T]=\int_0^{T}\mathbb E[\rho_s]\,ds,
\qquad
\operatorname{Var}(A_T)=2\int\!\!\!\int_{0\le s<t\le T}
\operatorname{Cov}(\rho_s,\rho_t)\,ds\,dt .
\]

Both \(\mathbb E[\rho_s]\) and
\(\mathbb E[\rho_s\rho_t]=\mathbb E[f(X_s)f(X_t)]\) are expectations of smooth
functions of (bi)variate Gaussians — \(\rho_s=f(X_s)\) with
\(X_s\sim N(x_0+\mu s,\sigma^{2}s)\) — computed here by Gauss–Hermite
quadrature in 1D and tensor Gauss–Hermite in 2D (using
\(X_t=X_s+\mu(t-s)+\sigma(W_t-W_s)\) for \(s<t\)). These are *deterministic*
evaluations, converged to the reported digits across two quadrature orders —
not Monte Carlo estimates.

Higher moments of \(A_T\) are available by the same route (ordered-simplex
integrals of \(\mathbb E[\rho_{s_1}\cdots\rho_{s_n}]\)); cost grows
factorially with \(n\). \(n\le2\) suffices for the approximation below.

## 5. From moments to prices: controlled approximation

The exact price is \(V=e^{-rT}\mathbb E[g(v(T;\rho))]\); the law of
\(v(T;\rho)\) has no elementary closed form (it is an additive functional of
Brownian motion — the same obstruction as for arithmetic Asian options, cf.
the Phase 5 audit). Two routes, used against each other:

1. **Exact simulation benchmark.** Simulate exact skeletons of \(X\),
   integrate \(q(\rho_s)\) by trapezoid, evaluate the closed form \(g\).
   Unbiased up to trapezoid error; Monte Carlo standard error reported; two
   step sizes. *No asset simulation is ever needed* — the reduction theorem
   removes \((W_1,W_2)\) from the computation, a genuine effective-dimension
   reduction from 3 drivers to 1.
2. **Moment-matched one-dimensional pricing.** Match a Gamma law to
   \((\mathbb E v,\operatorname{Var}v)\) and compute
   \(V_{\Gamma}=e^{-rT}\mathbb E_{v\sim\Gamma}[g(v)]\) by one-dimensional
   quadrature. Fully deterministic and instant; its error against the exact
   benchmark is *measured*, not assumed (and reported per parameter set —
   per project standards, no blanket accuracy claim).

## 6. Worked product: the spread one-touch

Pays 1 at \(T\) if the forward spread \(F_1-F_2\) ever reaches \(d>z_0\):

\[
\boxed{
V_{\mathrm{spread\ touch}}
=
e^{-rT}\,
\mathbb E_{\rho}\!\left[
2\Big(1-\Phi\Big(\frac{d-z_0}{\sqrt{v(T;\rho)}}\Big)\right)
],
\qquad
v(T;\rho)=\big(\sigma_1^{2}+\sigma_2^{2}\big)T-2\sigma_1\sigma_2A_T .
}
\]

Benchmarks in the notebook: the constant-correlation price
\(e^{-rT}\,2\big(1-\Phi\big((d-z_0)/\sqrt{q(\bar\rho)T}\big)\big)\) at
\(\bar\rho=\rho_0\), whose error against the stochastic-correlation price is
the *correlation-convexity mispricing* — signed, and opposite for spread and
basket (§3). Because \(2(1-\Phi(d/\sqrt v))\) is concave in \(v\) for small
\(v\) and convex for large \(v\), the sign of the Jensen gap is
parameter-dependent and is exhibited numerically rather than asserted.

## 7. Explicitly deferred

1. **Leverage** (\(W\) correlated with \((W_1,W_2)\)): destroys conditional
   Gaussianity; needs a different construction (e.g., \(\rho\) driven
   endogenously) and is the main open extension.
2. **Joint barriers on each asset separately** ("out if either asset breaches")
   and **min/max barriers**: not linear combinations; even with constant
   correlation these need wedge-domain image series. Stochastic-\(\rho\)
   versions are open.
3. **Pay-at-hit and American variants** of joint barriers.
4. **Full law of \(A_T\)** via Feynman–Kac resolvent inversion (numerical
   Laplace inversion route) as an alternative to moment matching.
5. **Lognormal families** for the assets (geometric rather than arithmetic):
   the time-change argument survives for \(\log F\) with deterministic vol
   ratios only; in general the clock picks up asset-level dependence. Open.

## 8. Verification summary

| Claim | Check | Result |
|---|---|---|
| conditional Gaussianity + DDS clock | derivation | Lemma/Theorem §2–3 |
| clock limits | constant-\(\rho\) recovers deterministic-clock formula; \(\sigma\to0\) collapses \(A_T\) | unit tests |
| moment quadrature | symmetry anchors (\(x_0=\mu=0\Rightarrow \mathbb E\rho_s=0\)); two GH orders agree | unit tests |
| Gamma-matched price anchors | \(d\to z_0^{+}\) gives \(e^{-rT}\); monotone in \(d\) | unit tests |
| reduction theorem, numerically | full 3-process MC (assets + correlation, bridge-corrected) vs scalar reduction MC | notebook, within ~2 SE |
| moment quadrature vs MC | \(\mathbb E[A_T]\), \(\operatorname{Var}(A_T)\) | notebook |
| Gamma price vs exact benchmark | error measured per parameter set, two step sizes | notebook |
| constant-\(\rho\) mispricing sign | spread vs basket, opposite directions | notebook figure |
