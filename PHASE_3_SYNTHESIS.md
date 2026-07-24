# Phase 3 Synthesis: A Faithful One-Driver Complex Representation

## 1. The concern

The original process is

\[
dX_t=\mu\,dt+\sigma\,dW_t.
\]

It has one Brownian driver. Phase 2 correctly studied the different process

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2),
\]

which has two independent Brownian drivers and full planar covariance.

The critique is therefore correct about dimensionality:

> Planar Brownian motion is not a polar coordinate change of scalar
> arithmetic Brownian motion.

This does not invalidate Phase 2. It means a separate construction is needed
when the goal is to preserve the original scalar process while making the
complex radius stochastic.

## 2. The Phase 3 answer

Let

\[
c=\alpha+i\beta,
\qquad
\alpha\ne0,
\qquad
Z_0\ne0.
\]

Define

\[
\boxed{
Z_t
=Z_0e^{c(X_t-X_0)}.}
\]

Then

\[
\boxed{
\begin{aligned}
\log\frac{R_t}{R_0}
&=\alpha(X_t-X_0),\\
\Theta_t-\Theta_0
&=\beta(X_t-X_0).
\end{aligned}}
\]

Both radius and angle are stochastic when \(\alpha\beta\ne0\), but both are
driven by the same \(W_t\).

The radius recovers the scalar state:

\[
\boxed{
X_t
=X_0+\frac1\alpha\log\frac{R_t}{R_0}.}
\]

Thus the logarithmic-spiral process and \(X_t\) contain exactly the same
stochastic information.

## 3. Exact Itô equation

Itô's formula gives

\[
\boxed{
\frac{dZ_t}{Z_t}
=
\left[
c\mu+\frac12c^2\sigma^2
\right]dt
+c\sigma\,dW_t.}
\]

In real and imaginary parts, the relative drift is

\[
\boxed{
\begin{aligned}
\text{real drift}
&=\alpha\mu
+\frac12(\alpha^2-\beta^2)\sigma^2,\\
\text{imaginary drift}
&=\beta\mu+\alpha\beta\sigma^2.
\end{aligned}}
\]

The \(-\beta^2\sigma^2/2\) term is the inward correction already present in
the circle model. The \(+\alpha^2\sigma^2/2\) term is the radial exponential
correction. The imaginary \(\alpha\beta\sigma^2\) term is created by the
cross-variation of log-radius and angle.

## 4. Polar covariance and the missing dimension

The polar equations are

\[
\begin{aligned}
d\log R_t&=\alpha\mu\,dt+\alpha\sigma\,dW_t,\\
d\Theta_t&=\beta\mu\,dt+\beta\sigma\,dW_t.
\end{aligned}
\]

Their covariance rate is

\[
\boxed{
K
=\sigma^2
\begin{pmatrix}
\alpha^2&\alpha\beta\\
\alpha\beta&\beta^2
\end{pmatrix}.}
\]

Its eigenvalues are

\[
\boxed{
\sigma^2(\alpha^2+\beta^2),\qquad0.}
\]

The zero eigenvalue is the mathematical record of the missing second
Brownian driver. The process has two coordinates but one stochastic
direction.

## 5. The general no-go theorem

For any \(C^2\) map

\[
F:\mathbb R\to\mathbb C
\]

and scalar diffusion

\[
dX_t=b(t,X_t)dt+a(t,X_t)dW_t,
\]

the image \(Z_t=F(X_t)\) satisfies

\[
dZ_t
=
\left[
bF'(X_t)+\frac12a^2F''(X_t)
\right]dt
+aF'(X_t)dW_t.
\]

Writing \(F\) as a two-component real vector, its covariance is

\[
\boxed{
C_t
=a(t,X_t)^2
F'(X_t)F'(X_t)^{\mathsf T}.}
\]

This is an outer product, so

\[
\boxed{\operatorname{rank}C_t\le1.}
\]

No smooth coordinate map from one scalar Brownian diffusion can produce
nondegenerate planar Brownian covariance.

The theorem does not prohibit stochastic radius and angle. It prohibits
their instantaneous noises from being independent.

## 6. Complex quadratic variation

For the logarithmic spiral,

\[
dZ_t^M=c\sigma Z_t\,dW_t.
\]

Therefore,

\[
\boxed{
d[Z,Z]_t=c^2\sigma^2Z_t^2dt}
\]

and

\[
\boxed{
d[Z,\overline Z]_t
=|c|^2\sigma^2|Z_t|^2dt.}
\]

A nonzero complex number cannot satisfy \(c^2=0\). Hence a nontrivial
one-driver embedding cannot reproduce the Phase 2 cancellation
\([Z,Z]=0\).

The stochastic logarithm makes the Itô correction explicit:

\[
\begin{aligned}
d\log Z_t
&=\frac{dZ_t}{Z_t}
-\frac12\frac{d[Z,Z]_t}{Z_t^2}\\
&=c\,dX_t.
\end{aligned}
\]

Thus

\[
\boxed{
\log\frac{Z_t}{Z_0}
=c(X_t-X_0).}
\]

## 7. Exact random-walk form

For

\[
\Delta X_n
=\mu h+\sigma\sqrt h\,\xi_n,
\qquad
\xi_n\sim N(0,1),
\]

the exact complex step is

\[
\boxed{
Z_{n+1}
=Z_n
\exp\!\left[
(\alpha+i\beta)
(\mu h+\sigma\sqrt h\,\xi_n)
\right].}
\]

Its polar components are

\[
\boxed{
\begin{aligned}
\log\frac{R_{n+1}}{R_n}
&=\alpha\Delta X_n,\\
\Theta_{n+1}-\Theta_n
&=\beta\Delta X_n.
\end{aligned}}
\]

The same Gaussian increment changes both radius and angle. This is exact at
every grid size.

## 8. The literal real-axis polar form

The most literal complex representation is

\[
Z_t=X_t+i0.
\]

Then

\[
R_t=|X_t|,
\qquad
\Theta_t\in\{0,\pi\}
\]

away from zero.

Before the first zero \(\tau_0\),

\[
\boxed{
X_t
=X_0
\exp\!\left[
\int_0^t\frac{\mu}{X_s}ds
+\int_0^t\frac{\sigma}{X_s}dW_s
-\frac12\int_0^t\frac{\sigma^2}{X_s^2}ds
\right].}
\]

For negative \(X_0\), this comes from \(\log|X_t|\), not \(\log X_t\).

Across zero, Tanaka's formula gives

\[
\boxed{
d|X_t|
=\operatorname{sgn}(X_t)dX_t+dL_t^0(X).}
\]

The local time \(L_t^0(X)\) is the global radial correction at the nonsmooth
origin. The logarithmic-spiral embedding avoids this singularity because it
never vanishes.

## 9. Exact distributions

Since

\[
X_t-X_0\sim N(\mu t,\sigma^2t),
\]

the log-radius and unwrapped angle are a degenerate jointly Gaussian pair.
For real \(p\),

\[
\boxed{
\mathbb E[R_t^p]
=R_0^p
\exp\!\left[
p\alpha\mu t
+\frac12p^2\alpha^2\sigma^2t
\right].}
\]

For integer \(n\),

\[
\boxed{
\mathbb E\left[
\left(\frac{Z_t}{Z_0}\right)^n
\right]
=
\exp\!\left[
nc\mu t+\frac12n^2c^2\sigma^2t
\right].}
\]

## 10. Numerical verification

The executed Phase 3 notebook found:

- exact-product error:
  \(6.273\times10^{-15}\);
- inverse-radius error:
  \(1.110\times10^{-15}\);
- spiral-relation error:
  \(9.437\times10^{-16}\);
- one-driver covariance eigenvalues:
  \(0\) and \(0.5963867\);
- two-driver comparison eigenvalues:
  \(0.2492954\) and \(0.2499687\);
- Euler–Maruyama strong convergence slope:
  \(0.5029\);
- nonlinear-image covariance determinant:
  \(7.058\times10^{-18}\);
- occupation local-time bias reduced from \(0.0678\) to \(0.0206\).

Every embedded assertion passed.

## 11. Model hierarchy

| Model | Drivers | Radius | Angle | Noise rank | Meaning |
|---|---:|---|---|---:|---|
| \(X_t+i0\) | 1 | \(|X_t|\) | sign phase | 1 | literal scalar embedding |
| \(r_0e^{i\beta(X_t-X_0)}\) | 1 | fixed | stochastic | 1 | circle phase |
| \(Z_0e^{(\alpha+i\beta)(X_t-X_0)}\) | 1 | stochastic | stochastic | 1 | faithful logarithmic spiral |
| \(Z_0+\sigma(W_t^1+iW_t^2)\) | 2 | Bessel | winding | 2 | planar Brownian motion |

## 12. What Phase 3 establishes

Phase 3 establishes:

- a stochastic radius does not require a second Brownian driver;
- a stochastic radius and angle can faithfully encode the scalar diffusion;
- one-driver amplitude and phase must remain perfectly coupled;
- an injective radial coordinate can preserve the entire scalar state;
- full planar Brownian motion requires genuinely new stochastic structure;
- zero crossings of the literal real-axis model require local time.

It does not claim:

- that the logarithmic spiral is planar Brownian motion;
- that a complex coordinate transformation creates randomness;
- that \(dW\) is an imaginary unit;
- that individual finite Brownian increments square to \(dt\);
- that a fixed-radius phase is state-injective without angle unwrapping.

## 13. Final answer

The concern is resolved by keeping two formulas rather than forcing one model
to do two incompatible jobs:

\[
\boxed{
\begin{aligned}
\text{faithful scalar complex representation:}\quad
&Z_t
=Z_0e^{(\alpha+i\beta)(X_t-X_0)},
\quad \alpha\ne0,\\[1mm]
\text{genuine planar Brownian motion:}\quad
&\widetilde Z_t
=\widetilde Z_0+\sigma(W_t^1+iW_t^2).
\end{aligned}}
\]

The first has a stochastic radius and angle but remains rank one. The second
has a stochastic Bessel radius and winding angle because it is rank two.

That is the precise boundary between representing the original Brownian
motion and constructing a new Brownian motion in the complex plane.
