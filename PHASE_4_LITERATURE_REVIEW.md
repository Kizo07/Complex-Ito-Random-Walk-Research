# Phase 4 Literature Review: Complex Geometric Brownian Motion and Stochastic Exponentials

## Scope and conclusion

Phase 4 asks whether geometric Brownian motion can be represented directly by
one complex exponential whose real exponent controls the modulus and whose
imaginary exponent controls rotation, without first constructing a Cartesian
pair or mapping an already-defined state process into the complex plane.

The literature supports all standard ingredients of this construction:

1. a scalar linear multiplicative Itô SDE has an exact exponential solution;
2. the drift and diffusion coefficients of that SDE may be complex;
3. this complex solution is already called a **complex geometric Brownian
   motion** in the numerical-SDE literature;
4. stochastic exponentials and stochastic logarithms are standard
   semimartingale transformations; and
5. modern semimartingale frameworks explicitly treat complex-valued
   processes.

The proposed Phase 4 contribution is therefore not a claim to have invented
complex GBM. It is a transparent, modulus-preserving parameterization of the
standard complex linear SDE, organized around the project's geometric
question:

\[
\text{How must the complex coefficients be chosen so that }
|\mathcal Z_t|
\text{ is exactly a prescribed real GBM?}
\]

## 1. Standard real GBM is already an exponential

For real constants \(\mu,\sigma\), real Brownian motion \(W_t\), and
\(R_0>0\), the SDE

\[
\frac{dR_t}{R_t}=\mu\,dt+\sigma\,dW_t
\]

has the exact solution

\[
R_t
=
R_0
\exp\!\left[
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right].
\tag{1.1}
\]

Higham presents the scalar linear test equation

\[
dX_t=\lambda X_t\,dt+\eta X_t\,dW_t
\]

and its exact solution

\[
X_t=X_0\exp\!\left[
\left(\lambda-\frac12\eta^2\right)t+\eta W_t
\right].
\tag{1.2}
\]

The same article later explicitly allows the parameters of this linear test
equation to be complex. This supplies both the exact-solution benchmark and
the numerical basis for the Phase 4 Euler--Maruyama comparison.

**Primary source**

- Desmond J. Higham, “An Algorithmic Introduction to Numerical Simulation of
  Stochastic Differential Equations,” *SIAM Review* 43(3) (2001), 525–546.
  <https://doi.org/10.1137/S0036144500378302>

## 2. Complex GBM is an established linear SDE

Buckwar, Horváth-Bokor, and Winkler study

\[
dX_t=\lambda X_t\,dt+\eta X_t\,dW_t,
\qquad
\lambda,\eta,X_0\in\mathbb C,
\tag{2.1}
\]

with one **real** Brownian motion. They explicitly describe its exact solution
as complex geometric Brownian motion. Their use is numerical stability, but
the model is the same general constant-coefficient complex multiplicative SDE
needed here.

For (2.1), the exact solution is

\[
X_t
=
X_0
\exp\!\left[
\left(\lambda-\frac12\eta^2\right)t+\eta W_t
\right].
\tag{2.2}
\]

This establishes two points relevant to Phase 4:

- no Cartesian state variables are required in the defining equation; and
- a real Brownian driver may be multiplied by a complex diffusion
  coefficient.

It does **not** imply that the resulting real and imaginary components have
independent noise. Both components are driven by the same scalar \(W_t\).

**Primary source**

- Evelyn Buckwar, Rózsa Horváth-Bokor, and Renate Winkler, “Asymptotic
  Mean-Square Stability of Two-Step Methods for Stochastic Ordinary
  Differential Equations,” *BIT Numerical Mathematics* 46 (2006), 261–282.
  <https://doi.org/10.1007/s10543-006-0060-5>

## 3. Itô's formula supplies the complex drift correction

Let

\[
\Xi_t=\kappa t+\nu W_t,
\qquad \kappa,\nu\in\mathbb C,
\]

and set

\[
\mathcal Z_t=\mathcal Z_0e^{\Xi_t}.
\]

The complex exponential is entire, so applying Itô's formula componentwise,
or applying the holomorphic version after complexification, gives

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(\kappa+\frac12\nu^2\right)dt+\nu\,dW_t.
\tag{3.1}
\]

The square in \(\nu^2\) is the complex bilinear square, not the modulus
\(|\nu|^2\). If \(\nu=\sigma+i\beta\), then

\[
\nu^2=\sigma^2-\beta^2+2i\sigma\beta.
\tag{3.2}
\]

This is the source of both the real correction
\(-\tfrac12\beta^2\) and the imaginary cross term \(\sigma\beta\) in the
Phase 4 SDE.

**Foundational source**

- Kiyosi Itô, “On a Formula Concerning Stochastic Differentials,” *Nagoya
  Mathematical Journal* 3 (1951), 55–65.
  <https://www.mathnet.ru/eng/mat116>

## 4. Stochastic exponentials are the canonical multiplicative form

For a continuous semimartingale \(Y\), its Doléans stochastic exponential is

\[
\mathcal E(Y)_t
=
\exp\!\left(Y_t-Y_0-\frac12[Y,Y]_t\right).
\tag{4.1}
\]

It is the solution of

\[
d\mathcal E(Y)_t=\mathcal E(Y)_t\,dY_t,
\qquad \mathcal E(Y)_0=1.
\tag{4.2}
\]

For

\[
Y_t=A t+B W_t,
\qquad A,B\in\mathbb C,
\]

the complex bilinear quadratic variation is

\[
[Y,Y]_t=B^2t,
\]

so

\[
\mathcal E(Y)_t
=
\exp\!\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\tag{4.3}
\]

Larsson and Ruf review stochastic exponentials and logarithms on stochastic
intervals. Černý and Ruf subsequently give unified semimartingale calculi that
explicitly include complex-valued processes, transformations, and
multiplicative compensation.

**Primary sources**

- Martin Larsson and Johannes Ruf, “Stochastic Exponentials and Logarithms on
  Stochastic Intervals—A Survey,” *Journal of Mathematical Analysis and
  Applications* 476(1) (2019), 2–12.
  <https://doi.org/10.1016/j.jmaa.2018.11.040>
- Aleš Černý and Johannes Ruf, “Simplified Stochastic Calculus via
  Semimartingale Representations,” *Electronic Journal of Probability* 27
  (2022), article 3, 1–32.
  <https://doi.org/10.1214/21-EJP729>
- Aleš Černý and Johannes Ruf, “Simplified Calculus for Semimartingales:
  Multiplicative Compensators and Changes of Measure,” *Stochastic Processes
  and their Applications* 161 (2023), 572–602.
  <https://doi.org/10.1016/j.spa.2023.04.010>

## 5. Deriving the modulus-preserving parameterization

Start from the established general complex GBM

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=A\,dt+B\,dW_t,
\qquad A,B\in\mathbb C.
\tag{5.1}
\]

Its exact solution is

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\tag{5.2}
\]

Write

\[
B=\sigma+i\beta.
\]

Then

\[
\log\frac{|\mathcal Z_t|}{|\mathcal Z_0|}
=
\operatorname{Re}\!\left(A-\frac12B^2\right)t+\sigma W_t,
\tag{5.3}
\]

while a continuous phase lift satisfies

\[
\Theta_t-\Theta_0
=
\operatorname{Im}\!\left(A-\frac12B^2\right)t+\beta W_t.
\tag{5.4}
\]

Demanding a GBM modulus with drift \(\mu\) and an unwrapped phase with angular
drift \(\omega\) imposes

\[
\operatorname{Re}\!\left(A-\frac12B^2\right)
=\mu-\frac12\sigma^2,
\tag{5.5}
\]

\[
\operatorname{Im}\!\left(A-\frac12B^2\right)=\omega.
\tag{5.6}
\]

Since

\[
B^2=\sigma^2-\beta^2+2i\sigma\beta,
\]

these constraints determine \(A\) uniquely:

\[
\boxed{
A
=
\mu-\frac12\beta^2+i(\omega+\sigma\beta).
}
\tag{5.7}
\]

Substitution into (5.2) yields

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
}
\tag{5.8}
\]

Equation (5.8) is therefore not an ad hoc analogy. It is the uniquely
parameterized member of the standard one-driver complex linear SDE family
having the requested radial and angular drifts and diffusions.

## 6. The meaning of “coordinate-free” in this project

In differential geometry, “coordinate-free” can carry a stronger
manifold-invariance meaning. Phase 4 uses the term operationally:

- the defining formula contains no separately evolved Cartesian processes
  \(X_t\) and \(Y_t\);
- it does not first build a path \(X_t+iY_t\);
- it does not transform an already-defined scalar state \(S_t\);
- it begins with \(\mathcal Z_0\), one Brownian primitive \(W_t\), and a
  complex log-increment.

Cartesian components may still be derived later for plotting:

\[
\operatorname{Re}\mathcal Z_t=R_t\cos\Theta_t,
\qquad
\operatorname{Im}\mathcal Z_t=R_t\sin\Theta_t.
\]

They are consequences, not the model definition.

## 7. Branches, zeros, and logarithms

Because a complex exponential never vanishes,

\[
\mathcal Z_0\ne0
\quad\Longrightarrow\quad
\mathcal Z_t\ne0
\quad\text{for every finite }t.
\]

Consequently:

- the modulus is strictly positive;
- a continuous unwrapped phase exists along each sample path once the initial
  phase is chosen;
- the principal argument may jump by \(2\pi\), but those jumps are a branch
  convention rather than physical jumps of the path; and
- the stochastic logarithm
  \(\int_0^t d\mathcal Z_s/\mathcal Z_s\) is well-defined without localization
  at zero.

The ordinary complex logarithm remains multivalued globally. Phase 4 will use
the explicit continuous lift, not silently identify it with the principal
branch.

## 8. The one-driver restriction

The log-radius and unwrapped angle have martingale increments

\[
dM_t^{(r)}=\sigma\,dW_t,
\qquad
dM_t^{(\theta)}=\beta\,dW_t.
\]

Their local covariance matrix is

\[
\begin{pmatrix}
\sigma^2&\sigma\beta\\
\sigma\beta&\beta^2
\end{pmatrix}dt
=
\begin{pmatrix}\sigma\\\beta\end{pmatrix}
\begin{pmatrix}\sigma&\beta\end{pmatrix}dt.
\tag{8.1}
\]

It has rank at most one. This follows directly from the single-driver
structure and agrees with the general rank theorem already established in
Phase 3.

Independent radial and angular Brownian noise requires two drivers, for
example

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+\sigma W_t^{(r)}+i\beta W_t^{(\theta)}
\right),
\]

with independent \(W^{(r)}\) and \(W^{(\theta)}\). That comparator is a
different model, not an equivalent rewriting of (5.8).

## 9. Relation to the Phase 3 logarithmic spiral

Phase 3 used

\[
\mathcal Z_t
=
\mathcal Z_0e^{cL_t},
\qquad c=\alpha+i\gamma,
\]

for a real scalar driver \(L_t\). If \(L_t\) is the log-return of a GBM and
\(\alpha=1\), then

\[
L_t=\left(\mu-\frac12\sigma^2\right)t+\sigma W_t,
\]

and

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
(1+i\gamma)
\left(
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right)
\right].
\]

This is the Phase 4 model only under

\[
\beta=\gamma\sigma,
\qquad
\omega=\gamma\left(\mu-\frac12\sigma^2\right).
\tag{9.1}
\]

Thus the Phase 3 fixed logarithmic spiral is a constrained subfamily. Phase 4
allows \(\omega\) and \(\beta\) to be specified independently while preserving
the GBM modulus.

## 10. Terminology and novelty audit

The source review leads to the following claim hierarchy:

### Established theory

- real GBM is an exponential of Brownian motion with an Itô drift correction;
- scalar linear SDEs admit exact exponential solutions;
- drift and diffusion coefficients may be complex;
- such a solution is called complex geometric Brownian motion in published
  numerical-SDE research;
- stochastic exponentials and logarithms are standard semimartingale
  transformations; and
- complex-valued semimartingales are covered by modern stochastic-calculus
  frameworks.

### Phase 4 derivation

- parameterize the general complex GBM so that its modulus is a prescribed
  real GBM;
- interpret the imaginary log-drift and log-diffusion as deterministic and
  stochastic rotation;
- show that the required complex SDE drift is uniquely fixed by
  \((\mu,\sigma,\omega,\beta)\);
- connect the model to Phase 3 and isolate the fixed-spiral subfamily; and
- expose the rank-one limitation and the exact two-driver boundary.

### Claims not made

- that complex GBM is new;
- that (5.8) is a new existence theorem;
- that \(dW_t^2=dt\) is an ordinary algebraic equality;
- that \(dW_t^2=dt\) is the same fact as \(i^2=-1\); or
- that one Brownian driver produces full planar Brownian motion.

## 11. Research verdict

The proposed model is mathematically supported:

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
}
\]

It eliminates the external state variable used in Phase 3, combines drift and
Brownian noise inside one complex exponent, retains an exact GBM as its
modulus, and supplies rotation through the imaginary exponent. Its exact
complex Itô SDE is

\[
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left[
\mu-\frac12\beta^2+i(\omega+\sigma\beta)
\right]dt
+(\sigma+i\beta)dW_t.
}
\]

The construction is a rigorous specialization of established complex linear
SDE theory. Its one-driver radial and angular noise is necessarily rank one.
