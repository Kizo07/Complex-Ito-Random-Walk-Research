# Phase 2 Literature Review

## Scope

Phase 2 needs sources for four precise claims:

1. planar Brownian motion has a Bessel radius and a time-changed angular
   Brownian motion;
2. a continuous complex logarithm exists along a planar Brownian path started
   away from the point about which it winds;
3. stochastic exponentials and logarithms require care near zeros;
4. numerical stochastic-integral claims must be checked through refinement
   and shared-path comparisons.

The formulas for general covariance, complex self-quadratic variation, and
the discrete logarithmic expansion are derived independently in this project.

## 1. Planar Brownian motion, logarithms, and winding

### Pitman and Yor, 1986

Jim Pitman and Marc Yor, “Asymptotic Laws of Planar Brownian Motion,”
*The Annals of Probability* 14(3), 733–779 (1986):

https://www.stat.berkeley.edu/users/pitman/asym.pdf

This primary paper develops the skew-product representation of planar
Brownian motion. In particular, it represents

\[
\log Z_t=\log R_t+i\Theta_t
\]

as a time-changed complex Brownian motion. The log-radial and angular
Brownian motions can be taken independent, while the random clock is
determined by the radial process.

Project use:

- justification of the planar skew-product interpretation;
- historical and mathematical support for the shared random clock;
- support for distinguishing zero cross-variation from the stronger
  independence statement.

### Pitman and Yor guide

Jim Pitman and Marc Yor, *A Guide to Brownian Motion and Related Stochastic
Processes*:

https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf

Section 8 treats planar Brownian motion. It states:

- conformal invariance under holomorphic maps, up to a time change;
- polarity of points for planar Brownian motion;
- existence of a continuous winding process around a point not hit by the
  path;
- the complex logarithm identity
  \[
  \log|Z_t-z_1|+i\Theta_t^{(z_1)}
  =\int_0^t\frac{dZ_s}{Z_s-z_1};
  \]
- the exponential reconstruction of \(Z_t-z_1\);
- the skew-product in which the radius is a two-dimensional Bessel process
  and the angular Brownian motion is independent of the radius.

Project use:

- direct authoritative support for the central Phase 2 formula;
- origin and branch conditions;
- the relation between holomorphic Itô calculus and the winding process.

## 2. Stochastic exponentials and logarithms

### Larsson and Ruf

Martin Larsson and Johannes Ruf, “Stochastic Exponentials and Logarithms on
Stochastic Intervals — A Survey”:

https://arxiv.org/abs/1702.03573

The survey develops stochastic exponentials and logarithms up to times at
which a process may reach zero. It is useful for separating:

- ordinary complex exponentiation;
- the Doléans–Dade stochastic exponential;
- the stochastic logarithm \(\int dZ/Z\);
- and the stopping/localization needed near zeros.

Project use:

- terminology and zero-boundary cautions;
- comparison of the Phase 2 complex logarithm with the standard
  semimartingale stochastic logarithm.

### Černý and Ruf

Aleš Černý and Johannes Ruf, “Simplified Calculus for Semimartingales:
Multiplicative Compensators and Changes of Measure”:

https://arxiv.org/abs/2006.12765

This paper explicitly considers signed and complex-valued semimartingales in
a multiplicative-compensation framework.

Project use:

- confirmation that complex-valued stochastic exponentials are part of the
  modern semimartingale literature;
- context only—the concrete continuous formulas in this project are derived
  directly with Itô's formula.

## 3. Rice distribution for the terminal radius

The SciPy reference for `scipy.stats.rice` gives both the density and its
geometric interpretation:

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rice.html

If

\[
X=U+s\xi,\qquad Y=V+s\eta,
\]

with independent standard normal \(\xi,\eta\), then

\[
\sqrt{X^2+Y^2}
\]

has a Rice distribution with shape

\[
b=\frac{\sqrt{U^2+V^2}}s
\]

and scale \(s\).

For

\[
Z_T=Z_0+\sigma(W_T^1+iW_T^2),
\]

the terminal radius therefore has

\[
b=\frac{|Z_0|}{\sigma\sqrt T},
\qquad
\text{scale}=\sigma\sqrt T.
\]

Project use:

- independent distributional check of the stochastic radius;
- Kolmogorov–Smirnov and moment comparisons in the notebook.

## 4. Numerical SDE methodology

Desmond J. Higham, “An Algorithmic Introduction to Numerical Simulation of
Stochastic Differential Equations,” *SIAM Review* 43(3), 525–546 (2001):

https://epubs.siam.org/doi/10.1137/S0036144500378302

The paper covers Brownian path simulation, stochastic integrals,
Euler–Maruyama, strong and weak convergence, and the stochastic chain rule.

Project use:

- grid-refinement design;
- shared-path comparisons;
- keeping Monte Carlo evidence separate from proof;
- interpreting convergence rates rather than relying on a single plot.

## 5. Relationship to the deep-research note

`deep-research-complex-ito.md` correctly identifies planar Brownian motion,
Bessel radius, winding, and stochastic logarithms as the path beyond the
fixed circle. It also contains interface-specific citation tokens that are
not reusable references. The sources above replace those tokens for the
Phase 2 scope.

The deep-research note's Lie-group, manifold, heat-equation, Schrödinger, and
quantum-Itô directions are intentionally deferred. They are not needed to
establish the full stochastic-radius representation.

## 6. Claims derived within this project

The following should be cited as project derivations, not quotations from the
sources:

\[
d[Z,Z]
=(C_{11}-C_{22}+2iC_{12})dt,
\]

\[
d[Z,\overline Z]=\operatorname{tr}(C)dt,
\]

\[
d\log Z
=\frac{dZ}{Z}-\frac12\frac{d[Z,Z]}{Z^2},
\]

and the general covariance polar formulas

\[
dR
=
\left[
e_r\cdot b+
\frac{\operatorname{tr}C-e_r^\mathsf TCe_r}{2R}
\right]dt
+e_r^\mathsf T\Sigma\,dW,
\]

\[
d\Theta
=
\left[
\frac{e_\theta\cdot b}{R}
-\frac{e_r^\mathsf TCe_\theta}{R^2}
\right]dt
+\frac{e_\theta^\mathsf T\Sigma}{R}\,dW.
\]

They agree with the cited planar and conformal theory but are worked out here
from the two-dimensional Itô formula.
