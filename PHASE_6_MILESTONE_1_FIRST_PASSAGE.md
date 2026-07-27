# Phase 6 — Milestone 1: exact first-passage and transition laws for the bounded correlation coordinate

**Date:** 2026-07-27
**Status:** derived and verified (15/15 unit tests; Monte Carlo cross-checks in
`notebooks/phase6_correlation_first_passage.ipynb`)
**Module:** `phase6_correlation.py` · **Tests:** `tests/test_phase6_correlation.py`

---

## 1. Setup

Let

\[
X_t=x_0+\mu t+\sigma W_t,\qquad \sigma>0,\ c>0,
\]

be an arithmetic (drifted) Brownian factor. The one-phase Euler coordinate and
the bounded correlation coordinate are

\[
\theta_t=\arctan\!\left(\frac{X_t}{c}\right)\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
\qquad
\rho_t=\sin\theta_t=\frac{X_t}{\sqrt{X_t^{2}+c^{2}}}\in(-1,1).
\]

The map \(f(x)=x/\sqrt{x^{2}+c^{2}}\) is smooth and strictly increasing, with
smooth inverse

\[
x(\rho)=\frac{c\,\rho}{\sqrt{1-\rho^{2}}}.
\]

**Interpretation.** \(\rho_t\) is a stochastic-correlation state variable: it
lives in \((-1,1)\), its endpoints are unattainable in finite time (they
correspond to \(|X_t|=\infty\)), and it is an invertible reparameterization of
the Gaussian factor, so the filtrations coincide. This is the
correlation-domain image of the Phase 5 canonical secant chart: the phase map
\(\theta=\arctan(X/c)\) composed with \(\rho=\sin\theta\). The radial function
is the secant law \(r(\theta)=\sec\theta\) of the additive family; nothing here
requires new existence theory — but all exactness statements below are
*inherited* from the Brownian driver, which is precisely the asset the Phase 6
literature audit (`PHASE_6_LITERATURE_REVIEW.md`, §3) identified as
unavailable in the mean-reverting competition.

**Honest costs (stated, not hidden).** \(\rho_t\) is *not* mean-reverting: it
is conjugate to a non-stationary factor. If \(\mu\neq0\), \(\rho_t\to\operatorname{sgn}(\mu)\)
a.s.; if \(\mu=0\), \(\limsup\rho_t=1\) and \(\liminf\rho_t=-1\) a.s. Its
diffusion coefficient vanishes like \((1-\rho^{2})^{3/2}\) at the boundaries —
faster than the Jacobi/van Emmerich \(\sqrt{1-\rho^{2}}\) — so correlation
spends more time near \(\pm1\) than in those models, and density mass near the
boundaries decays only polynomially in the conjugate coordinate. Whether these
are defects or features is an empirical question, deferred to the estimation
stage.

## 2. The autonomous correlation SDE

With \(f'(x)=c^{2}(x^{2}+c^{2})^{-3/2}\) and
\(f''(x)=-3c^{2}x(x^{2}+c^{2})^{-5/2}\), Itô's formula and the substitution
\(x^{2}+c^{2}=c^{2}/(1-\rho^{2})\) give the closed autonomous form

\[
\boxed{
d\rho_t=
\left[
\frac{\mu}{c}\,(1-\rho_t^{2})^{3/2}
-\frac{3\sigma^{2}}{2c^{2}}\,\rho_t(1-\rho_t^{2})^{2}
\right]dt
+\frac{\sigma}{c}\,(1-\rho_t^{2})^{3/2}\,dW_t .
}
\]

Checked two ways in `tests/test_phase6_correlation.py`: against an independent
\(x\)-coordinate transcription of the Itô derivatives (12 decimal places), and
through the module's own \(\rho\)-coordinate formulas.

## 3. Exact finite-time transition density

By monotone change of variables with Jacobian
\(dx/d\rho=c/(1-\rho^{2})^{3/2}\),

\[
\boxed{
p_t(\rho\mid\rho_0)
=
\frac{c}{(1-\rho^{2})^{3/2}}\,
\frac{1}{\sigma\sqrt{2\pi t}}
\exp\!\left[
-\frac{\big(x(\rho)-x(\rho_0)-\mu t\big)^{2}}{2\sigma^{2}t}
\right],
\qquad \rho\in(-1,1).
}
\]

This is an exact *finite-time* law in a single closed form. Contrast: the
closed-form density in Teng–Ehrhardt–Günther (2016) is the *stationary* density
of their modified-OU tanh model; their finite-time transition density is not
closed form because their driver (OU with \(\tanh\) inside the drift) has no
closed-form transition law. Verified: integrates to 1 to \(10^{-9}\) over
\((-1,1)\) for maturities \(0.05\), \(0.5\), \(3.0\) (unit test, adaptive
quadrature), and matches exact-skeleton Monte Carlo in the notebook.

## 4. Milestone-1 theorem: first passage of correlation to a level

Fix \(\rho^{*}\in(\rho_0,1)\) and set

\[
\tau_\rho(\rho^{*})=\inf\{t\ge0:\rho_t\ge\rho^{*}\}.
\]

Because \(f\) is strictly increasing, \(\rho_t\ge\rho^{*}\iff X_t\ge x^{*}\)
with

\[
x^{*}=\frac{c\,\rho^{*}}{\sqrt{1-\rho^{*2}}},
\qquad
b:=x^{*}-x_0>0.
\]

Therefore \(\tau_\rho(\rho^{*})=\tau_X(x^{*})\) almost surely, and the
reflection principle for drifted Brownian motion transfers verbatim:

### 4.1 Hitting probability over a finite horizon

\[
\boxed{
\mathbb P\!\left(\tau_\rho(\rho^{*})\le T\right)
=
\Phi\!\left(\frac{\mu T-b}{\sigma\sqrt T}\right)
+
e^{2\mu b/\sigma^{2}}\,
\Phi\!\left(-\frac{\mu T+b}{\sigma\sqrt T}\right).
}
\]

### 4.2 Hitting-time density (possibly defective)

\[
\boxed{
f_{\tau}(t)
=
\frac{b}{\sigma\sqrt{2\pi t^{3}}}
\exp\!\left[-\frac{(b-\mu t)^{2}}{2\sigma^{2}t}\right],
\qquad t>0,
}
\]

the inverse-Gaussian law; it integrates to
\(\min\!\left(1,e^{2\mu b/\sigma^{2}}\right)\).

### 4.3 Perpetual hitting probability

\[
\boxed{
\mathbb P\!\left(\tau_\rho(\rho^{*})<\infty\right)
=
\begin{cases}
1, & \mu\ge0,\\[4pt]
e^{2\mu b/\sigma^{2}}, & \mu<0.
\end{cases}
}
\]

In correlation terms,
\(b=c\!\left(\rho^{*}/\sqrt{1-\rho^{*2}}-\rho_0/\sqrt{1-\rho_0^{2}}\right)\).
Note the structural consequence: for a non-positive correlation trend
(\(\mu<0\)), *every* upper correlation level has a strictly positive
probability of never being reached, with an explicit exponential decay in the
conjugate distance \(b\).

### 4.4 Conditional moments (when \(\mu>0\))

\[
\mathbb E[\tau_\rho\mid\tau_\rho<\infty]=\frac{b}{\mu},
\qquad
\operatorname{Var}(\tau_\rho\mid\tau_\rho<\infty)=\frac{b\sigma^{2}}{\mu^{3}}.
\]

### 4.5 Two-sided correlation bands

For \(-1<\rho_\ell<\rho_0<\rho_h<1\), conjugate levels
\(x_\ell=x(\rho_\ell)\), \(x_h=x(\rho_h)\), and scale function
\(s(x)=e^{-2\mu x/\sigma^{2}}\) (\(s(x)=x\) when \(\mu=0\)):

\[
\boxed{
\mathbb P\!\left(\rho\text{ exits the band at }\rho_h\text{ first}\right)
=
\frac{s(x_0)-s(x_\ell)}{s(x_h)-s(x_\ell)}.
}
\]

Band exit itself happens in finite time almost surely (two finite Brownian
barriers), so this is a genuine Bernoulli law, not a perpetual limit.

## 5. Verification summary

| Claim | Check | Result |
|---|---|---|
| \(\rho=\sin\theta\) identity | algebraic, 5 points | \(10^{-15}\) |
| conjugate inverse | 5 points | \(10^{-12}\) |
| \(\rho\)-SDE coefficients | independent \(x\)-coordinate Itô transcription | \(10^{-12}\) |
| transition density normalized | adaptive quadrature, 3 maturities | \(|I-1|<10^{-9}\) |
| hitting CDF = integrated density | quadrature vs §4.1, 3 horizons | \(10^{-8}\) |
| CDF → perpetual law | limits incl. driftless slow tail | \(10^{-3}\)–\(10^{-2}\) |
| driftless CDF = reflection principle | hand formula | \(10^{-12}\) |
| exit probability | limits, monotonicity, driftless linear case | \(10^{-15}\) |
| all of §4 against Monte Carlo | exact skeleton + Brownian-bridge crossing correction, fixed seed `20260727`, two step sizes | see notebook |

Monte Carlo methodology note (per project standards): paths are sampled as
*exact Gaussian skeletons* — no Euler–Maruyama bias anywhere — and intra-step
crossings are resolved by the Brownian-bridge crossing probability
\(\exp\!\big(-2(b-x_t)(b-x_{t+1})/(\sigma^{2}\Delta t)\big)\), which is
drift-free (conditioning on endpoints removes the drift). The estimator is
therefore unbiased up to bridge-resolution error, reported at two step sizes
with Monte Carlo standard errors.

## 6. What Milestone 1 buys for the P1 program

1. **O3 deliverable.** §4 is, to our knowledge after the Phase 6 audit, the
   first closed-form first-passage law for a bounded stochastic-correlation
   state: Jacobi, tanh-of-OU, and von Mises correlation models admit none
   (their drivers' first-passage problems are unsolved or series-only).
2. **Pricable objects.** One-touch and barrier payoffs on correlation-dependent
   underlyings reduce to expectations against §4.1–§4.2 — a one-dimensional
   integral at worst — where today only approximations exist
   (`PHASE_6_LITERATURE_REVIEW.md` §3, O1).
3. **Calibration boundary.** §3 gives exact maximum-likelihood for discretely
   observed correlation (no spectral expansion, no simulation), the estimation
   counterpart to the pricing results.

## 7. Explicitly deferred

- Occupation-time laws for correlation ranges (needed for range accruals):
  resolvent/Laplace-transform route through the conjugate Brownian coordinate;
  the arc-sine law applies only at \(\mu=0\) and is not the product.
- Mean-reverting variant (OU driver): exact transition density survives, exact
  first-passage does not (OU hitting is series-only) — the
  stationarity–tractability trade-off to be made precise as a classification
  result.
- Embedding \(\rho_t\) into a two-asset pricing SDE with no-arbitrage
  conditions on the joint \((S_1,S_2,\rho)\) system.
