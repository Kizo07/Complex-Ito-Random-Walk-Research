# Phase 6 — Milestone 4: the full law of the variance clock by Feynman–Kac resolvent

**Date:** 2026-07-27
**Status:** derived and verified (unit tests + Monte Carlo in
`notebooks/phase6_fk_clock_law.ipynb`)
**Builds on:** Milestone 3 (`PHASE_6_MILESTONE_3_JOINT_BARRIER.md`)
**Module:** `phase6_fk.py` · **Tests:** `tests/test_phase6_fk.py`

Milestone 3 reduced joint barrier pricing to \(V=e^{-rT}\mathbb E[g(v(T;\rho))]\)
with \(v(T;\rho)=\beta T+\alpha A_T\), \(A_T=\int_0^T\rho_s\,ds\), and priced by
matching a Gamma law to the first two moments of \(A_T\). This milestone
replaces the moment match with a **deterministic computation of the full law
of \(A_T\)**, with error controlled at two independent levels (PDE
discretization/localization, Fourier truncation) and checked against exact
simulation. The Gamma approximation remains as a fast screening tool; the
claim of exactness now rests on the resolvent computation.

---

## 1. Feynman–Kac for the occupation functional

For \(\xi\in\mathbb R\) define

\[
u(t,x)=\mathbb E_x\!\left[e^{\,i\xi\int_0^{t}f(X_s)\,ds}\right],
\qquad
f(x)=\frac{x}{\sqrt{x^{2}+c^{2}}},
\]

the characteristic function of \(A_t\) with \(X_0=x\). Feynman–Kac (the
potential \(i\xi f\) is bounded, so no integrability issue arises):

\[
\partial_t u
=
\frac{\sigma^{2}}{2}\,\partial_{xx}u+\mu\,\partial_x u+i\xi f(x)\,u,
\qquad
u(0,x)=1 .
\]

The characteristic function of the clock's random part is
\(\phi(\xi)=u(T,x_0)\).

## 2. Bounded support \(\Rightarrow\) Fourier-series density

Since \(|f|<1\), the support of \(A_T\) lies in the **bounded** interval
\((-T,T)\) — a structural feature of the bounded correlation coordinate that
mean-reverting competitors on \((-1,1)\) share, but that makes inversion
particularly simple here: on \([-T,T]\) the density admits the Fourier
representation

\[
\boxed{
p(a)=\frac{1}{2T}\sum_{k=-\infty}^{\infty}
\phi\!\left(\frac{k\pi}{T}\right)e^{-ik\pi a/T},
\qquad a\in(-T,T),
}
\]

requiring \(\phi\) only at the equispaced nodes \(\xi_k=k\pi/T\). No Talbot
contour, no damping parameter: one PDE solve per Fourier mode. By
conjugation symmetry (\(A_T\) real, \(\phi(-\xi)=\overline{\phi(\xi)}\)) only
\(k\ge0\) are computed. Truncation at \(K\) modes gives

\[
p_K(a)=\frac{1}{2T}\Big[1+2\operatorname{Re}\sum_{k=1}^{K}
\phi(\xi_k)e^{-ik\pi a/T}\Big],
\]

with the truncation error controlled by the decay of \(|\phi(\xi_k)|\)
(verified numerically; smooth densities of additive functionals have rapidly
decaying transforms). Negativity of the truncated series is monitored as a
diagnostic, not assumed away.

**Moment identities (used as verification):**
\(\phi(0)=1\); \(\phi'(0)=i\,\mathbb E[A_T]\); and
\(\int_{-T}^{T}a^{n}p(a)\,da\) must reproduce the quadrature moments of
Milestone 3 for \(n=1,2\).

## 3. Localized discretization of the PDE

The PDE is solved on a truncated domain \([x_{\min},x_{\max}]\) centered on
\(x_0+\mu T\) with half-width \(L=M\sigma\sqrt T\) (margin factor \(M\), two
values compared for the localization check), second-order central
differences on a uniform grid of \(N\) nodes, homogeneous Dirichlet
conditions, and Krylov time integration (`expm_multiply`, no time-stepping
error beyond the Krylov tolerance). The Dirichlet values are *wrong* in
principle — the true boundary behavior is \(u\to e^{\pm i\xi t}\) as
\(x\to\pm\infty\) — but the induced error at \(x_0\) is bounded by the
probability of the driver reaching the boundary by \(T\)
(Cont–Voltchkova-style localization, cf. the Phase 5 audit), which is
\(\mathcal O(\exp(-M^{2}/2))\) and verified directly by doubling \(M\).

Cost: \(K+1\) complex sparse matrix exponentials of size \(N\). Everything is
deterministic; there is no Monte Carlo anywhere in the pricing path.

## 4. Pricing through the full law

With \(v=\beta T+\alpha a\), \(\beta=\alpha_1^{2}\sigma_1^{2}+\alpha_2^{2}\sigma_2^{2}\),
\(\alpha=2\alpha_1\alpha_2\sigma_1\sigma_2\),

\[
\boxed{
V_{\mathrm{FK}}
=
e^{-rT}
\int_{-T}^{T}
g\!\left(\beta T+\alpha a\right)p_K(a)\,da ,
\qquad
g(v)=2\Big(1-\Phi\Big(\frac{d-z_0}{\sqrt v}\Big)\Big),
}
\]

evaluated by trapezoid on the density grid. Note the clock can in principle
go negative for the spread when \(\alpha<0\) and \(A_T>\beta T/|\alpha|\)
(extreme persistent high correlation): the integrand is then 0 (a crossed
spread is already through any upper barrier — \(g(0^{+})=1\) at \(v=0\);
negative \(v\) is truncated at 0 with the convention \(g\equiv1\)). This edge
case is handled explicitly in code and occurs only when
\(\beta T/|\alpha|<T\), i.e. \(\sigma_1^{2}+\sigma_2^{2}<2\sigma_1\sigma_2\),
equivalently \((\sigma_1-\sigma_2)^{2}<0\) — never. So for the spread the
clock is always positive; the guard is defensive only.

*Check:* \(q(\rho)=(\alpha_1\sigma_1+\alpha_2\sigma_2\rho)^{2}+\alpha_2^{2}\sigma_2^{2}(1-\rho^{2})\ge0\)
always, since it is a sum of squares — the integrand itself is a variance.
The affine form \(\beta+\alpha\rho\) can indeed go negative for \(\alpha<0\),
but the true clock \(v=\int q(\rho_s)ds\) cannot; the affine reduction
\(\beta T+\alpha A_T\) equals \(\int q\,ds\) only because
\(q(\rho)=\beta+\alpha\rho\) identically — both forms are equal, so
\(\beta T+\alpha A_T\ge0\) automatically. The guard remains as a numerical
safety net. \(\square\)

## 5. What this buys

1. **Exactness of the Milestone 3 pricing path**, up to two monitored
   discretization errors — replacing an approximation whose error could only
   be measured, not bounded a priori.
2. **The full density of the clock**, from which *any* clock-measurable
   claim prices by one quadrature: lookbacks on the spread, barrier digitals,
   clock options.
3. **A reusable resolvent primitive**: the same PDE with potential
   \(-\lambda f\) instead of \(i\xi f\) gives Laplace transforms (resolvent
   approach to occupation-time laws — the deferred corridor problem of
   Milestone 2).

## 6. Explicitly deferred

- Resolvent (\(\lambda\)-domain) inversion for continuous corridor/range
  occupation prices.
- Higher-accuracy potential treatment near the truncated boundaries
  (transparent/absorbing conditions).
- Leverage extension (still the main structural open problem).

## 7. Verification summary

| Claim | Check | Result |
|---|---|---|
| \(\phi(0)=1\) | direct | unit test |
| \(|\phi(\xi)|\le1\) | several \(\xi\) | unit test |
| \(\phi'(0)=i\mathbb E[A_T]\) | numerical derivative vs Milestone 3 quadrature | unit test |
| PDE vs MC | \(|\phi(\xi)-\widehat\phi_{\mathrm{MC}}(\xi)|\) at several \(\xi\) | notebook, ~2 SE |
| localization | \(M\) vs \(2M\) agreement | unit test + notebook |
| density normalization & nonnegativity | trapezoid, min value | notebook diagnostic |
| density moments \(n=1,2\) | vs quadrature moments | notebook |
| Fourier convergence | \(K\) vs \(2K\) price agreement | unit test + notebook |
| deterministic limit | \(\sigma\to0^{+}\): FK price \(\to\) deterministic-clock price | unit test |
| FK vs Gamma vs MC benchmark | price table, three driver vols | notebook |
