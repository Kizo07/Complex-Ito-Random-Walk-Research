# Phase 6 — Milestone 5: continuous corridor occupation prices by Feynman–Kac resolvent

**Date:** 2026-07-27
**Status:** derived and verified (unit tests + Monte Carlo in
`notebooks/phase6_corridor_occupation.ipynb`)
**Builds on:** Milestones 2 (deferred corridor item) and 4 (resolvent machinery)
**Module:** `phase6_corridor.py` · **Tests:** `tests/test_phase6_corridor.py`

---

## 1. The deferred problem

Milestone 2 priced *discretely* monitored correlation range accruals exactly
(sum of Gaussian tail differences) and explicitly deferred the *continuously*
monitored corridor: payoff a function of the occupation time

\[
\mathcal O_T=\int_0^{T}\mathbf 1_{\{x_\ell\le X_t\le x_h\}}\,dt
\]

of the conjugate factor \(X_t=x_0+\mu t+\sigma W_t\), which is exactly the
occupation time of the correlation band
\(\{\rho_\ell\le\rho_t\le\rho_h\}\) under the monotone map
\(x(\rho)=c\rho/\sqrt{1-\rho^{2}}\).

Two clarifications on what is hard and what is not:

- **The plain corridor bond** (coupon \(\propto\mathcal O_T\)) is *linear* in
  \(\mathcal O_T\), so its price is \(e^{-rT}\mathbb E[\mathcal O_T]\), and
  \(\mathbb E[\mathcal O_T]=\int_0^T\mathbb P(X_t\in[x_\ell,x_h])\,dt\) is a
  one-dimensional quadrature of Gaussian probabilities — exact, no resolvent
  needed. This is recorded as the anchor product, not as a contribution.
- **Anything nonlinear in \(\mathcal O_T\)** — a corridor digital
  \(\mathbf 1_{\{\mathcal O_T\ge\kappa T\}}\), a corridor call
  \((\mathcal O_T/T-\kappa)^{+}\), a range note with a participation cap —
  needs the *law* of \(\mathcal O_T\). Outside the driftless half-line case
  (Lévy's arcsine law) no elementary form exists. That law is the product of
  this milestone.

## 2. Resolvent with an indicator potential

The Milestone 4 pipeline applies verbatim with the potential replaced by the
corridor indicator \(g(x)=\mathbf 1_{[x_\ell,x_h]}(x)\) (bounded, measurable —
the PDE requires no smoothness of \(g\)):

\[
\partial_t u=\frac{\sigma^{2}}{2}u_{xx}+\mu u_x+i\xi\,\mathbf 1_{[x_\ell,x_h]}(x)\,u,
\qquad u(0,x)=1,
\]

and \(\phi_{\mathcal O}(\xi)=u(T,x_0)\) is the characteristic function of
\(\mathcal O_T\).

**Support and Fourier representation.** \(\mathcal O_T\in[0,T]\), so on
\([0,T]\) the density is

\[
\boxed{
p_{\mathcal O}(o)=\frac1T\Big[1+2\operatorname{Re}\sum_{k=1}^{\infty}
\phi_{\mathcal O}\Big(\frac{2\pi k}{T}\Big)e^{-i2\pi k o/T}\Big],
}
\]

truncated at \(K\) modes in computation.

**Atoms (handled explicitly).** A bounded corridor *always* has an atom at
\(\mathcal O_T=T\): the event of never exiting has positive probability.
Starting outside gives a second atom at \(0\) (never entering) with mass
equal to the Milestone 1 survival probability; an unbounded corridor with
drift can also carry an atom at \(T\) in closed form (Milestone 1 perpetual
hitting). The pipeline therefore **separates the atom before the Fourier
inversion**: the atom at \(T\) is computed deterministically — by an
absorbing-boundary PDE on the corridor itself (bounded corridor) or by the
Milestone 1 perpetual formula (unbounded corridor) — and subtracted from
every Fourier mode (since \(e^{i\xi_kT}=1\) at the nodes \(\xi_k=2\pi k/T\),
the atom contributes its mass as a constant to all modes). The Fourier
series then represents only the continuous part, with mass \(1-\)atom, and
converges orders of magnitude faster. Prices reassemble atom and continuous
parts in closed form. Starting outside the corridor (atom at \(0\)) is
rejected explicitly and deferred.

## 3. The arcsine anchor

For \(\mu=0\), corridor \([0,\infty)\), \(x_0=0\), the occupation *fraction*
\(\mathcal O_T/T\) has Lévy's arcsine law

\[
\mathbb P(\mathcal O_T\le sT)=\frac{2}{\pi}\arcsin\sqrt s,
\qquad s\in[0,1],
\]

a parameter-free, exact, non-Gaussian benchmark. The resolvent pipeline
reproduces it (unit test: tail probabilities at several fractions; notebook:
density overlay). This is the strongest available anchor for the corridor
machinery — it validates the PDE, the truncation, and the Fourier inversion
against a law that is *not* built from Gaussian integrals at all.

## 4. Priced products

All at time 0, rate \(r\), band \((\rho_\ell,\rho_h)\) with conjugate
\((x_\ell,x_h)\):

1. **Corridor digital** — pays \(\mathbf 1_{\{\mathcal O_T\ge\kappa T\}}\):
   \[
   V=e^{-rT}\int_{\kappa T}^{T}p_{\mathcal O}(o)\,do .
   \]
2. **Corridor call** — pays \((\mathcal O_T/T-\kappa)^{+}\):
   \[
   V=\frac{e^{-rT}}{T}\int_{\kappa T}^{T}(o-\kappa T)\,p_{\mathcal O}(o)\,do .
   \]
3. **Corridor bond (anchor)** — pays \(\mathcal O_T/T\):
   \(V=e^{-rT}\mathbb E[\mathcal O_T]/T\) by the quadrature formula of §1;
   used to validate the density's first moment, not claimed as new.

## 5. Verification summary

| Claim | Check | Result |
|---|---|---|
| \(\phi_{\mathcal O}(0)=1\); conjugate symmetry | direct | unit tests |
| arcsine law (driftless half-line) | FK density vs \((2/\pi)\arcsin\sqrt s\) | unit test + notebook overlay |
| \(\mathbb E[\mathcal O_T]\) anchor | continuous part + atom vs Gaussian quadrature | unit test, residual truncation bias \(<5\times10^{-3}\) abutting a large atom, shrinking in \(K\) and grid |
| deterministic limit | near-deterministic driver concentrates \(\mathcal O_T\) | unit test |
| mass normalization / nonnegativity | trapezoid; min value diagnostic | unit test + notebook |
| atom at \(T\) (bounded corridor) | absorbing-PDE vs MC; closed form for unbounded corridors | unit test + notebook |
| digital and call prices | FK vs exact-skeleton MC, two step sizes | notebook: uniform gap \(\sim7\times10^{-3}\) with two identified opposite-sign biases — MC overstates occupation (bridge misses brief exits; gap shrinks with finer steps) and FK truncation biases prices slightly downward; \(K\)-convergence continuing at \(K=128\), grid stable |
| convergence | \(K\) and grid sweeps | notebook |

## 6. Explicitly deferred

- Atom treatment for outside starts and drifted unbounded corridors (the
  Milestone 1 first-passage formulas supply the masses; assembly deferred).
- Occupation *joint* law with terminal value (needed for corridor + terminal
  condition hybrids) — two-dimensional resolvent, open.
- Double barriers on the *corridor excursion* (Parisian-style occupation
  derivatives) — related resolvent, open.
