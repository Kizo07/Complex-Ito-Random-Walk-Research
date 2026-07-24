# Independently verified source context

These sources were located and checked by Codex on 2026-07-23. The worker may
use them in `LITERATURE_REVIEW.md`, but should not claim more than each source
supports.

## Random walks and Brownian motion

Davár Khoshnevisan, *Lecture Notes on Donsker's Theorem*, University of Utah:

https://www.math.utah.edu/~davar/ps-pdf-files/donsker.pdf

- Defines the linearly interpolated, normalized random walk.
- Theorem 1.4 states convergence to Brownian motion in `C[0,1]` under i.i.d.
  mean-zero, variance-one increments.

## Quadratic variation and the Itô rule

John K. Hunter, *Lecture Notes on Applied Mathematics*, UC Davis, chapter on
Brownian motion:

https://www.math.ucdavis.edu/~hunter/m280_09/ch.pdf

- Pages 148–149 define Brownian quadratic variation.
- For a uniform partition, the squared increments have total mean `b-a` and
  variance tending to zero.
- Explicitly describes `(dB)^2 = dt` as a formal rule arising from nonzero
  quadratic variation.

Jonathan Goodman, *Stochastic Calculus*, Courant Institute, Fall 2021, Week 4:

https://math.nyu.edu/~goodman/teaching/StochCalc2021/week4/Week4.pdf

- Defines quadratic variation of an Itô process.
- States the rule to replace `(dX_t)^2` by `d[X]_t`.
- Gives Itô's formula for `dX_t = a_t dt + b_t dW_t`.

## Stochastic exponentials

Paul-André Meyer, *Décomposition des martingales locales et formules
exponentielles*, Séminaire de Probabilités X (1976), Numdam:

https://www.numdam.org/article/SPS_1976__10__432_0.pdf

- Section 2 defines the exponential of a semimartingale as the unique solution
  of `Z_t = 1 + integral_0^t Z_{s-} dX_s`.
- Gives the general exponential formula including the continuous quadratic
  variation and jump product.
- Attributes the theorem to Catherine Doléans-Dade.

Historical citation:

Catherine Doléans-Dade, “Quelques applications de la formule de changement de
variables pour les semimartingales,” *Zeitschrift für
Wahrscheinlichkeitstheorie und Verwandte Gebiete* 16 (1970), 181–194.

The original bibliographic details are corroborated by later journal
references. Do not attach a DOI unless separately verified.

Martin Larsson and Johannes Ruf, *Stochastic Exponentials and Logarithms on
Stochastic Intervals — A Survey*:

https://arxiv.org/abs/1702.03573

- Modern survey of stochastic exponentials and logarithms, including behavior
  up to zeros and stochastic intervals.

## Planar Brownian motion and angular time change

Jim Pitman and Marc Yor, *A Guide to Brownian Motion and Related Stochastic
Processes*:

https://www.stat.berkeley.edu/users/aldous/205B/pitman_yor_guide_bm.pdf

- Section 9.1 gives the skew-product representation
  `B_t = |B_t| theta(integral_0^t ds/|B_s|^2)`.
- Identifies the radius as a Bessel process and the angular component as
  Brownian motion on the sphere, independent of the radius.
- Gives a Stratonovich SDE representation for angular Brownian motion.

Daniel Revuz and Marc Yor, *Continuous Martingales and Brownian Motion*,
Springer:

https://link.springer.com/book/10.1007/978-3-662-06400-9

- Authoritative book reference for continuous martingales, Bessel processes,
  and planar Brownian motion. Cite chapter/section only after checking the
  relevant edition.

## Itô versus Stratonovich geometry

John Armstrong and Damiano Brigo, “Projections of SDEs onto submanifolds,”
*Information Geometry*:

https://link.springer.com/article/10.1007/s41884-022-00093-7

- Explains that Stratonovich SDEs behave as first-order calculus on manifolds.
- Notes that tangent Stratonovich vector fields preserve an embedded
  submanifold, while Itô calculus requires second-order structure.

K. D. Elworthy, *Stochastic Differential Equations on Manifolds*, Cambridge
University Press:

https://www.cambridge.org/core/books/stochastic-differential-equations-on-manifolds/stochastic-differential-equations-on-manifolds/45932142D05C0E14D49FF1D7247172D7

- Classical monograph on manifold-valued SDEs and Brownian motion.

Michel Émery, *Stochastic Calculus in Manifolds*, Springer:

https://link.springer.com/book/10.1007/978-3-642-75051-9

- Covers manifold-valued semimartingales, quadratic variation, Brownian motion
  on Riemannian manifolds, and Stratonovich/Itô integration.

## Numerical SDE verification

Desmond J. Higham, “An Algorithmic Introduction to Numerical Simulation of
Stochastic Differential Equations,” *SIAM Review* 43(3) (2001), 525–546:

https://epubs.siam.org/doi/10.1137/S0036144500378302

- Peer-reviewed, reproducible introduction to Euler–Maruyama, Milstein,
  stochastic integration, strong/weak convergence, and Monte Carlo simulation.
- DOI and bibliographic data are displayed on the SIAM publication page.
- The project's coupled geometric-Brownian-motion experiment should follow the
  strong-error principle: exact and numerical solutions must use the same
  Brownian path.

## Direct project consequence

For `Theta_t = theta_0 + omega t + beta W_t` and
`Z_t = r_0 exp(i Theta_t)`, applying Itô's formula gives

`dZ_t = (i omega - beta^2/2) Z_t dt + i beta Z_t dW_t`.

Equivalently, the same motion has the Stratonovich form

`dZ_t = i omega Z_t dt + i beta Z_t o dW_t`.

This consequence should be presented as a derivation made in this project, not
as a verbatim result from one of the sources above.

## Phase 2 additions verified on 2026-07-23

Jim Pitman and Marc Yor, “Asymptotic Laws of Planar Brownian Motion,”
*The Annals of Probability* 14(3), 733–779 (1986):

https://www.stat.berkeley.edu/users/pitman/asym.pdf

- Develops the skew-product representation of planar Brownian motion.
- Represents the continuous complex logarithm through log-radial and angular
  Brownian motions on a common clock.
- Establishes the stronger independence structure between angular Brownian
  motion and the radial process.

The Pitman–Yor guide already listed above was rechecked at Section 8:

- states point polarity for planar Brownian motion;
- defines the continuous winding process;
- gives
  `log|Z_t-z| + i Theta_t = integral dZ/(Z-z)`;
- exponentiates this stochastic logarithm to reconstruct the process;
- identifies the radius as a two-dimensional Bessel process.

SciPy official documentation for the Rice distribution:

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rice.html

- Gives the density and the interpretation as the length of a two-dimensional
  Gaussian vector with a nonzero mean.
- Supports the Phase 2 terminal-radius distribution check.

Aleš Černý and Johannes Ruf, “Simplified Calculus for Semimartingales:
Multiplicative Compensators and Changes of Measure”:

https://arxiv.org/abs/2006.12765

- Explicitly includes complex-valued semimartingales in a multiplicative
  compensation framework.
- Used only for context; the project's continuous complex-logarithm formula
  is independently derived with Itô's formula.
