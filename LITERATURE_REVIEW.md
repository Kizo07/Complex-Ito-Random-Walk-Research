# Literature Review and Research Positioning

## Scope

The ingredients of this project are classical. The intended contribution is
not a new stochastic-calculus theorem; it is a careful synthesis that
separates two bridges:

1. the **algebraic bridge** from quadratic variation to stochastic
   exponentials;
2. the **geometric bridge** from Brownian phase to complex rotation.

The numerical work tests these consequences and common failure modes.

## 1. Random-walk scaling and Brownian motion

[Davár Khoshnevisan's *Lecture Notes on Donsker's
Theorem*](https://www.math.utah.edu/~davar/ps-pdf-files/donsker.pdf) develops
the normalized, interpolated random walk and its weak convergence to Brownian
motion in \(C[0,1]\). It supplies the rigorous random-walk-to-Brownian scaling
context for increments of size \(\sqrt{\Delta t}\).

Donsker convergence alone should not be cited as a proof of convergence of
quadratic variation, because quadratic variation is not continuous under
uniform path convergence. This project therefore proves the Brownian
quadratic-variation statement directly using independent Gaussian increments.

## 2. Quadratic variation and Itô's formula

[John K. Hunter's Brownian-motion
notes](https://www.math.ucdavis.edu/~hunter/m280_09/ch.pdf) compute the mean
and variance of sums of squared Brownian increments and explain the formal
rule \((dB)^2=dt\) through nonzero quadratic variation.

[Jonathan Goodman's *Stochastic Calculus*, Week
4](https://math.nyu.edu/~goodman/teaching/StochCalc2021/week4/Week4.pdf)
defines quadratic variation for Itô processes and states the operational rule
that \((dX_t)^2\) is replaced by \(d[X]_t\) in Itô's formula.

Together these references support the central distinction used here:

\[
\mathbb E[(\Delta W)^2]=\Delta t
\]

is a finite-step expectation identity, while

\[
[W]_t=t
\]

is the limiting pathwise/quadratic-variation structure represented
differentially by \((dW)^2=dt\).

## 3. Stochastic exponentials

Catherine Doléans-Dade's 1970 paper,
“Quelques applications de la formule de changement de variables pour les
semimartingales,” established the stochastic exponential in general
semimartingale form.

[Paul-André Meyer's 1976
exposition](https://www.numdam.org/article/SPS_1976__10__432_0.pdf) defines
the exponential of a semimartingale through the linear equation

\[
Z_t=1+\int_0^t Z_{s-}\,dX_s
\]

and records the exponential formula, including continuous quadratic
variation and jump factors.

[Martin Larsson and Johannes Ruf's modern
survey](https://arxiv.org/abs/1702.03573) treats stochastic exponentials and
logarithms on stochastic intervals, including behavior near zeros.

For a continuous local martingale \(M\), the special case used in this project
is

\[
\mathcal E(M)_t
=\exp\!\left(M_t-\frac12[M]_t\right).
\]

This is the established object closest to “exponential form” for a
multiplicative stochastic differential.

## 4. Planar Brownian motion and polar coordinates

[Jim Pitman and Marc Yor's *A Guide to Brownian Motion and Related Stochastic
Processes*](https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf)
describes the Brownian skew-product representation: the radius is a Bessel
process and the angular component is Brownian motion on the sphere evaluated
at the random clock \(\int ds/R_s^2\).

[Daniel Revuz and Marc Yor, *Continuous Martingales and Brownian
Motion*](https://link.springer.com/book/10.1007/978-3-662-06400-9) is a
standard monograph reference for continuous martingales, Bessel processes,
and planar Brownian motion.

These results show that “Brownian motion in a plane” and “Brownian phase on a
fixed circle” are distinct:

- planar Brownian angle has volatility proportional to \(1/R_t\);
- Brownian motion on a fixed circle has prescribed phase volatility and
  requires tangential noise.

## 5. Itô versus Stratonovich geometry

[John Armstrong and Damiano Brigo, “Projections of SDEs onto
submanifolds”](https://link.springer.com/article/10.1007/s41884-022-00093-7)
explain why Stratonovich SDEs transform as first-order geometric equations:
tangent Stratonovich vector fields preserve an embedded submanifold, while an
Itô representation carries second-order information.

Classical book treatments include
[K. D. Elworthy, *Stochastic Differential Equations on
Manifolds*](https://www.cambridge.org/core/books/stochastic-differential-equations-on-manifolds/stochastic-differential-equations-on-manifolds/45932142D05C0E14D49FF1D7247172D7)
and
[Michel Émery, *Stochastic Calculus in
Manifolds*](https://link.springer.com/book/10.1007/978-3-642-75051-9).

This geometric perspective explains the two equivalent pure-rotation forms:

\[
dZ=i\omega Z\,dt+i\beta Z\circ dW
\]

and

\[
dZ=\left(i\omega-\frac12\beta^2\right)Z\,dt+i\beta Z\,dW.
\]

The first displays tangent vector fields; the second displays the inward Itô
correction that preserves the circle after quadratic variation is included.

## 6. Numerical verification

[Desmond J. Higham, “An Algorithmic Introduction to Numerical Simulation of
Stochastic Differential
Equations”](https://epubs.siam.org/doi/10.1137/S0036144500378302), *SIAM
Review* 43(3), 2001, develops Euler–Maruyama, strong and weak error, and Monte
Carlo simulation. The coupled-error experiment in this project follows its
central strong-error principle: exact and numerical solutions are compared on
the same Brownian path.

## 7. Position of the present formula

The project's unified formula

\[
Z_t=e^{A_t+i\Theta_t}
\]

with stochastic log-amplitude \(A\) and phase \(\Theta\) is a direct
application of multidimensional Itô calculus, not a claim of a newly
discovered stochastic exponential. Its value is that it places, in one
coordinate system:

- geometric Brownian motion;
- Brownian motion on a circle;
- correlated amplitude–phase noise;
- and the polar equations of planar Brownian motion.

The accompanying simulations are diagnostic examples designed to make the
different correction terms empirically visible.
