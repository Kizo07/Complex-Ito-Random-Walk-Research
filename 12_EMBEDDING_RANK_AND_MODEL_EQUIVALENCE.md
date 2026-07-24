# Embedding Rank and Model Equivalence

## 1. General deterministic complex image

Let

\[
dX_t=b(t,X_t)dt+a(t,X_t)dW_t
\]

be a scalar Itô diffusion, and let

\[
F:\mathbb R\to\mathbb C,
\qquad
F=F_1+iF_2,
\]

be \(C^2\). Define

\[
Z_t=F(X_t).
\]

Componentwise Itô calculus gives

\[
\boxed{
dZ_t
=
\left[
bF'(X_t)+\frac12a^2F''(X_t)
\right]dt
+aF'(X_t)dW_t.}
\]

The image can curve, rotate, and change radius, but its martingale part still
uses only the original scalar Brownian motion.

## 2. Rank-one theorem

Write

\[
\mathbf F(x)
=
\begin{pmatrix}F_1(x)\\F_2(x)\end{pmatrix}.
\]

The Cartesian martingale coefficient is the \(2\times1\) vector

\[
g_t
=a(t,X_t)\mathbf F'(X_t).
\]

Therefore the instantaneous Cartesian covariance is

\[
\boxed{
C_t
=g_tg_t^{\mathsf T}
=a(t,X_t)^2
\mathbf F'(X_t)\mathbf F'(X_t)^{\mathsf T}.}
\]

An outer product of one vector has rank at most one:

\[
\boxed{
\operatorname{rank}C_t\le1,
\qquad
\det C_t=0.}
\]

This proves:

> A deterministic \(C^2\) transformation of a scalar Itô diffusion cannot
> produce a nondegenerate planar diffusion.

The result is local and instantaneous. It does not depend on whether the
image curve crosses itself or becomes dense in some region over long times.

## 3. Stronger one-driver statement

The obstruction is not limited to Markov transformations \(F(X_t)\).
Suppose a general adapted complex Itô process is driven by one Brownian
motion:

\[
dZ_t
=b_tdt+g_t\,dW_t,
\qquad
g_t=g_t^1+ig_t^2.
\]

Its Cartesian covariance is

\[
\begin{pmatrix}g_t^1\\g_t^2\end{pmatrix}
\begin{pmatrix}g_t^1&g_t^2\end{pmatrix}dt,
\]

again of rank at most one. Path dependence and state dependence can rotate
the noisy direction over time, but at each instant there is still only one
independent Gaussian increment.

Full-rank planar Brownian covariance requires at least two independent
instantaneous directions.

## 4. Polar version of the rank theorem

Assume \(Z_t\ne0\) and write

\[
Z_t=e^{A_t+i\Theta_t}.
\]

If one Brownian motion drives both polar coordinates,

\[
\begin{aligned}
dA_t&=a_tdt+u_t\,dW_t,\\
d\Theta_t&=\omega_tdt+v_t\,dW_t,
\end{aligned}
\]

then

\[
\boxed{
K_t
=
\begin{pmatrix}
u_t^2&u_tv_t\\
u_tv_t&v_t^2
\end{pmatrix}
=
\begin{pmatrix}u_t\\v_t\end{pmatrix}
\begin{pmatrix}u_t&v_t\end{pmatrix}.}
\]

Hence

\[
\det K_t=0.
\]

Radius and angle can both be random, but their instantaneous correlation has
absolute value one whenever \(u_tv_t\ne0\).

For the Phase 3 logarithmic spiral,

\[
u_t=\alpha\sigma,
\qquad
v_t=\beta\sigma.
\]

For isotropic Phase 2 planar Brownian motion in its adapted polar basis,

\[
K_t
=\frac{\sigma^2}{R_t^2}
\begin{pmatrix}1&0\\0&1\end{pmatrix},
\]

which has rank two.

## 5. Four meanings of “representation”

### Deterministic image

\[
Z_t=F(X_t).
\]

This always produces a complex-valued process from \(X_t\), but it may lose
information.

### State-injective embedding

There is an inverse \(F^{-1}\) on the image curve, so \(X_t\) is recoverable
from \(Z_t\) at each fixed time.

The logarithmic spiral with \(\alpha\ne0\) has this property because its
radius is strictly monotone in \(X_t\).

### Pathwise recoverability

The current complex state may be insufficient, but the continuous path and
initial value may determine the scalar process. The fixed-radius phase map
has this property through angle unwrapping.

### Equality as a planar stochastic model

The complex process has the same law, generator, and covariance as a target
planar diffusion. A rank-one image of one Brownian driver cannot satisfy this
criterion for nondegenerate planar Brownian motion.

These meanings should never be interchanged.

## 6. State dimension is not noise dimension

A process can take values in \(\mathbb R^2\) while using one Brownian driver.
For example,

\[
\begin{pmatrix}
A_t\\\Theta_t
\end{pmatrix}
=
\begin{pmatrix}
A_0\\\Theta_0
\end{pmatrix}
+
\begin{pmatrix}
\alpha\\\beta
\end{pmatrix}
(\mu t+\sigma W_t).
\]

Its state has two coordinates, but all random increments lie along the vector
\((\alpha,\beta)\).

Conversely, planar Brownian motion

\[
\begin{pmatrix}X_t\\Y_t\end{pmatrix}
=
\begin{pmatrix}X_0\\Y_0\end{pmatrix}
+
\sigma
\begin{pmatrix}W_t^1\\W_t^2\end{pmatrix}
\]

has two independent stochastic directions.

The difference appears in the covariance rank, not merely in the number of
symbols used to write the state.

## 7. Geometry and generators

For \(Z_t=F(X_t)\), the state remains on the deterministic curve

\[
\Gamma=F(\mathbb R).
\]

The scalar generator

\[
\mathcal L_X
=b(t,x)\frac{\partial}{\partial x}
+\frac12a(t,x)^2\frac{\partial^2}{\partial x^2}
\]

pushes forward to a second-order operator tangent to \(\Gamma\). The Itô drift
contains the curvature term

\[
\frac12a^2F''(x).
\]

For planar Brownian motion, the generator is

\[
\mathcal L_{\mathrm{plane}}
=\frac{\sigma^2}{2}
\left(
\frac{\partial^2}{\partial x^2}
+\frac{\partial^2}{\partial y^2}
\right),
\]

which diffuses in every planar direction. No one-dimensional coordinate
change turns the curve generator into the planar Laplacian.

## 8. Model comparison

| Model | Brownian drivers | Radius | Angle | Covariance rank | Scalar-state recovery |
|---|---:|---|---|---:|---|
| \(X_t+i0\) | 1 | \(|X_t|\) | \(0/\pi\) | 1 away from degenerate points | direct |
| \(r_0e^{i\beta(X_t-X_0)}\) | 1 | fixed | stochastic | 1 | from lifted path, not current state |
| \(Z_0e^{(\alpha+i\beta)(X_t-X_0)}\), \(\alpha\ne0\) | 1 | stochastic | stochastic | 1 | from radius |
| \(Z_0+\sigma(W_t^1+iW_t^2)\) | 2 | Bessel | stochastic winding | 2 | different process |

## 9. How the critique changes the interpretation

The dimensional criticism is correct:

\[
dX_t=\mu dt+\sigma dW_t
\]

and

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2)
\]

are not the same process in different coordinates. The latter adds an
independent stochastic degree of freedom.

The criticism does not invalidate the Phase 2 formulas. Those formulas were
explicitly derived for planar Brownian motion. It instead clarifies that
Phase 2 answered a different question:

> What is the stochastic polar exponential of genuine Brownian motion in the
> complex plane?

Phase 3 answers the question left open:

> What is an information-preserving complex exponential of the original
> scalar Brownian diffusion when the radius must also be stochastic?

The logarithmic-spiral embedding supplies that answer without dimensional
inflation.

## 10. No contradiction between the phases

The three phases form a hierarchy:

1. **Phase 1:** use scalar Brownian motion as phase on a circle;
2. **Phase 2:** introduce two independent directions for full planar Brownian
   motion;
3. **Phase 3:** return to the scalar process and construct an injective
   rank-one amplitude-phase embedding.

Phase 2 is the correct full-plane model. Phase 3 is the correct faithful
one-driver representation. They are complementary rather than competing
answers.

## 11. Final theorem

Let \(X\) be a scalar Itô diffusion and \(F:\mathbb R\to\mathbb C\) be \(C^2\).
Then:

1. \(F(X)\) is an exact complex image of \(X\);
2. its instantaneous Cartesian covariance has rank at most one;
3. both radius and angle may be stochastic;
4. if \(F\) is injective, the scalar state is exactly recoverable;
5. if a target planar diffusion has rank-two covariance, \(F(X)\) cannot have
   the same law as that target.

This theorem is the precise boundary between complex representation and the
creation of genuinely new stochastic structure.
