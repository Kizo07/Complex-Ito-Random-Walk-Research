# The One-Driver Logarithmic-Spiral Representation

## 1. Definition

Let

\[
dX_t=\mu\,dt+\sigma\,dW_t,
\qquad
X_t=X_0+\mu t+\sigma W_t,
\]

and choose

\[
c=\alpha+i\beta,
\qquad
Z_0=R_0e^{i\Theta_0}\ne0.
\]

The Phase 3 process is

\[
\boxed{
Z_t
=Z_0\exp\!\left[c(X_t-X_0)\right].}
\]

The exponent must be dimensionless. Thus \(\alpha\) and \(\beta\) have units
reciprocal to the units of \(X\), unless \(X\) is already dimensionless.

## 2. Polar coordinates

Writing \(Z_t=R_te^{i\Theta_t}\) with an unwrapped phase,

\[
\boxed{
\begin{aligned}
\log\frac{R_t}{R_0}
&=\alpha(X_t-X_0),\\
\Theta_t-\Theta_0
&=\beta(X_t-X_0).
\end{aligned}}
\]

Hence

\[
\boxed{
\begin{aligned}
d\log R_t&=\alpha\mu\,dt+\alpha\sigma\,dW_t,\\
d\Theta_t&=\beta\mu\,dt+\beta\sigma\,dW_t.
\end{aligned}}
\]

If \(\alpha\beta\ne0\), the path lies on the logarithmic spiral

\[
\Theta_t-\Theta_0
=\frac{\beta}{\alpha}\log\frac{R_t}{R_0}.
\]

Both coordinates fluctuate, but the relation between them is exact.

## 3. Information preservation

When \(\alpha\ne0\),

\[
\boxed{
X_t
=X_0+\frac1\alpha\log\frac{|Z_t|}{|Z_0|}.}
\]

Thus the map from \(X_t\) to \(Z_t\) is injective, even though its angular
coordinate winds modulo \(2\pi\). For every \(t\),

\[
\sigma(X_s:0\le s\le t)
=
\sigma(Z_s:0\le s\le t).
\]

The logarithmic-spiral representation is not merely a visualization. It
contains exactly the same stochastic information as the scalar process.

When \(\alpha=0\), the radius no longer distinguishes phase windings. The
fixed-radius process can recover \(X_t\) only from a continuously lifted angle
and its initial value, not from the current complex state alone.

## 4. Itô derivation from the scalar map

Let

\[
F(x)=Z_0e^{c(x-X_0)}.
\]

Then

\[
F'(x)=cF(x),
\qquad
F''(x)=c^2F(x).
\]

Itô's formula yields

\[
\begin{aligned}
dZ_t
&=F'(X_t)dX_t+\frac12F''(X_t)d[X,X]_t\\
&=cZ_t(\mu\,dt+\sigma\,dW_t)
  +\frac12c^2Z_t\sigma^2dt.
\end{aligned}
\]

Therefore,

\[
\boxed{
\frac{dZ_t}{Z_t}
=
\left(c\mu+\frac12c^2\sigma^2\right)dt
+c\sigma\,dW_t.}
\]

With \(c=\alpha+i\beta\),

\[
\boxed{
\begin{aligned}
\operatorname{Re}\left(
c\mu+\frac12c^2\sigma^2
\right)
&=
\alpha\mu+\frac12(\alpha^2-\beta^2)\sigma^2,\\
\operatorname{Im}\left(
c\mu+\frac12c^2\sigma^2
\right)
&=
\beta\mu+\alpha\beta\sigma^2.
\end{aligned}}
\]

The real Itô drift contains the competition between radial amplification and
angular curvature. The imaginary Itô drift is the amplitude-phase
cross-variation.

## 5. Independent derivation from polar reconstruction

Set

\[
A_t=\log R_t.
\]

For \(Z_t=e^{A_t+i\Theta_t}\), the two-dimensional Itô formula gives

\[
\frac{dZ_t}{Z_t}
=dA_t+i\,d\Theta_t
+\frac12\left(d[A,A]_t-d[\Theta,\Theta]_t\right)
+i\,d[A,\Theta]_t.
\]

Here

\[
\begin{aligned}
d[A,A]_t&=\alpha^2\sigma^2dt,\\
d[\Theta,\Theta]_t&=\beta^2\sigma^2dt,\\
d[A,\Theta]_t&=\alpha\beta\sigma^2dt.
\end{aligned}
\]

Substitution gives

\[
\frac{dZ_t}{Z_t}
=
\left[
(\alpha+i\beta)\mu
+\frac12(\alpha+i\beta)^2\sigma^2
\right]dt
+(\alpha+i\beta)\sigma\,dW_t,
\]

which agrees exactly with the direct scalar derivation.

## 6. Rank-one polar covariance

The instantaneous covariance of \((A_t,\Theta_t)\) is

\[
\boxed{
K
=\sigma^2
\begin{pmatrix}
\alpha^2&\alpha\beta\\
\alpha\beta&\beta^2
\end{pmatrix}
=
\sigma^2
\begin{pmatrix}\alpha\\\beta\end{pmatrix}
\begin{pmatrix}\alpha&\beta\end{pmatrix}.}
\]

Its eigenvalues are

\[
\boxed{
\lambda_1=\sigma^2(\alpha^2+\beta^2),
\qquad
\lambda_2=0.}
\]

For \(\alpha\beta\ne0\), the instantaneous correlation between \(dA_t\) and
\(d\Theta_t\) is

\[
\operatorname{Corr}(dA_t,d\Theta_t)
=\operatorname{sgn}(\alpha\beta).
\]

There are two random-looking coordinates but only one random direction.

## 7. Complex quadratic variations

The martingale part of \(Z_t\) is

\[
dZ_t^{M}=c\sigma Z_t\,dW_t.
\]

The complex bilinear quadratic variation is

\[
\boxed{
d[Z,Z]_t=c^2\sigma^2Z_t^2dt.}
\]

The Hermitian quadratic variation is

\[
\boxed{
d[Z,\overline Z]_t
=|c|^2\sigma^2|Z_t|^2dt.}
\]

For a nontrivial one-driver embedding, \(c^2\ne0\). The Phase 2 cancellation
\([Z,Z]=0\) depended on two independent, equally scaled Cartesian Brownian
directions and cannot occur here.

Apply the complex logarithm identity:

\[
\begin{aligned}
d\log Z_t
&=\frac{dZ_t}{Z_t}
-\frac12\frac{d[Z,Z]_t}{Z_t^2}\\
&=c\mu\,dt+c\sigma\,dW_t\\
&=c\,dX_t.
\end{aligned}
\]

Consequently,

\[
\boxed{
\log\frac{Z_t}{Z_0}
=c(X_t-X_0)}
\]

using the continuous logarithm along the nonvanishing path. This is global on
each finite time interval because the exponential image never reaches zero.

## 8. Exact finite-step random walk

For grid size \(h\), let

\[
\Delta X_n=\mu h+\sigma\sqrt h\,\xi_n,
\qquad
\xi_n\overset{\mathrm{iid}}{\sim}N(0,1).
\]

Then

\[
\boxed{
Z_{n+1}
=Z_n\exp(c\Delta X_n).}
\]

This formula is exact at the grid points:

\[
\prod_{n=0}^{N-1}e^{c\Delta X_n}
=e^{c\sum_{n=0}^{N-1}\Delta X_n}
=e^{c(X_T-X_0)}.
\]

The polar step is

\[
\boxed{
\begin{aligned}
\log\frac{R_{n+1}}{R_n}&=\alpha\Delta X_n,\\
\Theta_{n+1}-\Theta_n&=\beta\Delta X_n.
\end{aligned}}
\]

The same increment changes amplitude and phase. No second Gaussian variable
is introduced.

## 9. Exact distributions and moments

At time \(t\),

\[
X_t-X_0\sim N(\mu t,\sigma^2t).
\]

Therefore,

\[
\log R_t
\sim
N\left(
\log R_0+\alpha\mu t,\,
\alpha^2\sigma^2t
\right),
\]

and the unwrapped angle is normal:

\[
\Theta_t
\sim
N\left(
\Theta_0+\beta\mu t,\,
\beta^2\sigma^2t
\right).
\]

The two variables are jointly Gaussian but degenerate because they are affine
functions of the same normal variable.

For real \(p\),

\[
\boxed{
\mathbb E[R_t^p]
=
R_0^p
\exp\!\left(
p\alpha\mu t
+\frac12p^2\alpha^2\sigma^2t
\right).}
\]

For integer \(n\),

\[
\boxed{
\mathbb E\left[
\left(\frac{Z_t}{Z_0}\right)^n
\right]
=
\exp\!\left(
nc\mu t+\frac12n^2c^2\sigma^2t
\right).}
\]

In particular,

\[
\mathbb E|Z_t|^2
=R_0^2
\exp\!\left(
2\alpha\mu t+2\alpha^2\sigma^2t
\right).
\]

## 10. Special cases

### Pure stochastic rotation

If \(\alpha=0\),

\[
Z_t=Z_0e^{i\beta(X_t-X_0)}
\]

and

\[
\frac{dZ_t}{Z_t}
=
\left(i\beta\mu-\frac12\beta^2\sigma^2\right)dt
+i\beta\sigma dW_t.
\]

This is the Phase 1 circle model.

### Pure stochastic radius

If \(\beta=0\),

\[
Z_t=Z_0e^{\alpha(X_t-X_0)}
\]

stays on the ray through \(Z_0\). It is a geometric image of the arithmetic
diffusion.

### Logarithmic spiral

If \(\alpha\beta\ne0\), both radius and angle vary. The process never fills an
area because its state lies on a deterministic spiral.

## 11. Conclusion

The logarithmic-spiral construction is a complete, injective, one-driver
complex representation of scalar arithmetic Brownian motion. It remedies the
fixed-radius limitation without changing the Brownian noise dimension.

Its limitation is equally precise: stochastic radius and angle are perfectly
coupled. Full planar Brownian motion remains the distinct rank-two model from
Phase 2.
