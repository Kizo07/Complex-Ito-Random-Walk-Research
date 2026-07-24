# Phase 3 Literature Review

## Scope

Phase 3 needs sources for four established tools:

1. one- and multidimensional Itô formulas;
2. Brownian local time, occupation density, and Tanaka's formula;
3. stochastic logarithms before a process reaches zero;
4. shared-path numerical verification of SDE approximations.

The logarithmic-spiral representation, its moment formulas, and the
covariance-rank theorem are derived in this project rather than attributed to
external sources.

## 1. Itô calculus and covariance

### Jonathan Goodman, Courant Institute

Jonathan Goodman, *Stochastic Calculus Notes, Lecture 8*, New York
University:

https://math.nyu.edu/~goodman/teaching/StochCalc2004/notes/l8_1.pdf

The notes formulate a multidimensional diffusion with an \(n\times m\)
volatility matrix, identify its short-time covariance as
\(\Sigma\Sigma^{\mathsf T}\), state the multidimensional Itô formula, and
describe the forward Euler approximation.

Phase 3 use:

- componentwise Itô derivation of \(F(X_t)\);
- interpreting the number of Brownian drivers as the number of volatility
  columns;
- the covariance outer-product calculation for a one-driver complex image;
- Euler–Maruyama verification.

The rank-one no-go theorem itself is a direct project consequence:

\[
C_t
=\sigma^2
F'(X_t)F'(X_t)^{\mathsf T}.
\]

## 2. Brownian local time and occupation density

### Mörters and Peres

Peter Mörters and Yuval Peres, *Brownian Motion*, Cambridge University Press;
author-hosted PDF:

https://www.stat.berkeley.edu/users/aldous/205B/bmbook.pdf

Chapter 6 develops one-dimensional Brownian local time through downcrossings
and occupation times, including the occupation-time representation.

Phase 3 use:

- interpreting local time as the density of occupation near a level;
- supporting the near-zero numerical experiment;
- explaining why exact grid hits are not a valid local-time estimator.

### Marek Biskup, UCLA

Marek Biskup, *MATH 275D Notes, Chapter 29: Brownian Local Time*:

https://www.math.ucla.edu/~biskup/275d.1.25f/PDFs/ch29.pdf

These lecture notes connect occupation-time measure, Brownian local time,
Tanaka's formula, and reflected Brownian motion.

Phase 3 use:

- the Tanaka decomposition of \(|X_t|\);
- the local-time correction at the nonsmooth point of the absolute value;
- the occupation-density normalization.

The notes are marked preliminary, so the project will use them as an
accessible derivational source while treating the established theorem in its
standard semimartingale form.

## 3. Stochastic logarithms and zeros

### Larsson and Ruf

Martin Larsson and Johannes Ruf, “Stochastic Exponentials and Logarithms on
Stochastic Intervals — A Survey,” *Journal of Mathematical Analysis and
Applications* 476 (2019), 186–206:

https://arxiv.org/abs/1702.03573

The paper treats stochastic logarithms on stochastic intervals and makes
explicit the role of continuous hitting of zero.

Phase 3 use:

- stopping the scalar representation before \(\tau_0\);
- separating the ordinary complex logarithm along a nonvanishing path from
  a global real logarithm through sign changes;
- keeping the stochastic logarithm distinct from informal exponentiation.

The project specializes the general theory to the continuous scalar process:

\[
d\log|X_t|
=\frac{dX_t}{X_t}
-\frac12\frac{d[X,X]_t}{X_t^2},
\qquad t<\tau_0.
\]

## 4. Planar Brownian comparison

### Pitman and Yor

Jim Pitman and Marc Yor, *A Guide to Brownian Motion and Related Stochastic
Processes*:

https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf

The guide establishes the relevant distinction on the planar side:

- the radial part of planar Brownian motion is a two-dimensional Bessel
  process;
- points are polar for planar Brownian motion started elsewhere;
- a continuous winding and complex logarithm exist along the nonvanishing
  path;
- the angular Brownian motion can be separated from the radial process under
  the skew-product representation.

Primary paper:

Jim Pitman and Marc Yor, “Asymptotic Laws of Planar Brownian Motion,”
*The Annals of Probability* 14(3), 733–779 (1986):

https://www.stat.berkeley.edu/users/pitman/asym.pdf

Phase 3 use:

- comparison only;
- confirmation that the Phase 2 Bessel/winding model is genuine planar
  Brownian motion;
- preventing the one-driver logarithmic spiral from being mislabeled as
  planar Brownian motion.

## 5. Numerical SDE verification

### Desmond Higham

Desmond J. Higham, “An Algorithmic Introduction to Numerical Simulation of
Stochastic Differential Equations,” *SIAM Review* 43(3), 525–546 (2001):

https://epubs.siam.org/doi/10.1137/S0036144500378302

Phase 3 use:

- Euler–Maruyama on Brownian paths shared with the exact solution;
- empirical strong convergence;
- clear separation between analytic identities and numerical evidence.

## 6. Claims derived within Phase 3

The following are project derivations:

\[
Z_t
=Z_0e^{(\alpha+i\beta)(X_t-X_0)},
\]

\[
\frac{dZ_t}{Z_t}
=
\left[
(\alpha+i\beta)\mu
+\frac12(\alpha+i\beta)^2\sigma^2
\right]dt
+(\alpha+i\beta)\sigma dW_t,
\]

\[
\operatorname{Cov}(d\log R_t,d\Theta_t)
=
\sigma^2
\begin{pmatrix}
\alpha^2&\alpha\beta\\
\alpha\beta&\beta^2
\end{pmatrix}dt,
\]

and, for any \(C^2\) map \(F:\mathbb R\to\mathbb C\),

\[
\operatorname{rank}
\left(
\sigma^2F'(X_t)F'(X_t)^{\mathsf T}
\right)
\le1.
\]

These identities follow directly from Itô's formula and elementary linear
algebra. The external literature supplies the general calculus, local-time
framework, and planar comparison rather than the specific Phase 3 theorem.

## 7. Source discipline

Phase 3 will:

- cite sources only for claims they directly support;
- label the logarithmic-spiral construction as a project derivation;
- use \(\log|X|\) for negative scalar states;
- state the local-time normalization explicitly;
- keep rank-one scalar embeddings separate from rank-two planar Brownian
  motion;
- treat simulation as verification, not proof.
