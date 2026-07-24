# Complex Quadratic Variation

## 1. Two quadratic variations, not one

Let

\[
Z_t=X_t+iY_t
\]

be a continuous complex-valued semimartingale. Extend quadratic covariation
complex-bilinearly. Then

\[
\boxed{
d[Z,Z]_t
=d[X,X]_t-d[Y,Y]_t+2i\,d[X,Y]_t,}
\]

whereas conjugation gives

\[
\boxed{
d[Z,\overline Z]_t
=d[X,X]_t+d[Y,Y]_t.}
\]

These objects answer different questions:

- \([Z,Z]\) is the **complex self-quadratic variation**. It is the term that
  appears in a holomorphic Itô formula.
- \([Z,\overline Z]\) is the **total Euclidean quadratic variation**. It is
  nonnegative and measures accumulated planar noise.

The first is bilinear, not positive definite. The second behaves like a
squared Euclidean norm.

## 2. Isotropic planar Brownian motion

Use the project convention

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2),
\]

where \(W^1,W^2\) are independent standard Brownian motions. Each Cartesian
coordinate therefore has variance rate \(\sigma^2\). The complex increment
has

\[
\begin{aligned}
d[Z,Z]_t
&=\sigma^2\left(d[W^1,W^1]_t-d[W^2,W^2]_t
+2i\,d[W^1,W^2]_t\right)\\
&=\sigma^2(dt-dt+0)=0,
\end{aligned}
\]

but

\[
d[Z,\overline Z]_t
=\sigma^2(dt+dt)=2\sigma^2dt.
\]

Thus

\[
\boxed{[Z,Z]_t=0,\qquad [Z,\overline Z]_t=2\sigma^2t.}
\]

The statement \([Z,Z]=0\) does **not** say that \(Z\) has zero quadratic
variation in the Euclidean sense. It says that the two equal Cartesian
quadratic variations cancel in the complex-bilinear square because
\(i^2=-1\).

This is a genuine meeting point of complex algebra and Itô calculus:

\[
(dW^1+i\,dW^2)^2
=(dW^1)^2-(dW^2)^2+2i\,dW^1dW^2=0.
\]

It requires two independent, equally scaled Brownian directions. It is not
the one-dimensional mnemonic \((dW)^2=dt\).

## 3. General complex diffusion coefficients

Write a two-dimensional diffusion as

\[
dZ_t=b_tdt+\sum_{k=1}^m\gamma_{k,t}\,dW_t^k,
\]

where

\[
b_t=b_{x,t}+ib_{y,t},
\qquad
\gamma_{k,t}=\Sigma_{1k,t}+i\Sigma_{2k,t}.
\]

If

\[
C_t=\Sigma_t\Sigma_t^\mathsf T,
\]

then

\[
\boxed{
\frac{d[Z,Z]_t}{dt}
=\sum_k\gamma_{k,t}^2
=C_{11,t}-C_{22,t}+2iC_{12,t},}
\]

and

\[
\boxed{
\frac{d[Z,\overline Z]_t}{dt}
=\sum_k|\gamma_{k,t}|^2
=\operatorname{tr}C_t.}
\]

In two dimensions, \(d[Z,Z]=0\) precisely when

\[
C_{11}=C_{22},\qquad C_{12}=0,
\]

so the instantaneous covariance is a scalar multiple of the identity. This
is the isotropic, or conformal, case.

For unequal independent volatilities,

\[
dX=\sigma_xdW^1,\qquad dY=\sigma_ydW^2,
\]

\[
d[Z,Z]=(\sigma_x^2-\sigma_y^2)dt.
\]

For Brownian drivers with instantaneous correlation \(\rho\),

\[
d[Z,Z]
=\left(\sigma_x^2-\sigma_y^2
+2i\rho\sigma_x\sigma_y\right)dt.
\]

Anisotropy and correlation are therefore visible directly in the complex
self-quadratic variation.

## 4. Holomorphic Itô formula

Let \(f\) be holomorphic on a neighborhood of the stopped path of \(Z\). The
ordinary two-dimensional Itô formula, together with the Cauchy–Riemann
equations, reduces to

\[
\boxed{
df(Z_t)
=f'(Z_t)dZ_t+\frac12f''(Z_t)d[Z,Z]_t.}
\]

For isotropic planar Brownian motion, \(d[Z,Z]=0\), so

\[
df(Z_t)=f'(Z_t)dZ_t.
\]

There is no Itô drift for a holomorphic function because its real and
imaginary parts are harmonic and the planar Brownian generator is
\((\sigma^2/2)\Delta\).

This does not mean second-order effects have disappeared. They have canceled
specifically in the holomorphic direction. Nonholomorphic functions such as
\(|z|\), \(|z|^2\), and \(\overline z\) still see
\([Z,\overline Z]\).

## 5. Complex logarithm

Assume \(Z_0\ne0\), and localize before the path approaches the origin:

\[
\tau_\varepsilon
=\inf\{t\ge0:|Z_t|\le\varepsilon\}.
\]

On a continuously chosen logarithmic branch along
\([0,\tau_\varepsilon]\), use

\[
f(z)=\log z,\qquad f'(z)=\frac1z,\qquad
f''(z)=-\frac1{z^2}.
\]

The holomorphic Itô formula gives

\[
\boxed{
d\log Z_t
=\frac{dZ_t}{Z_t}
-\frac12\frac{d[Z,Z]_t}{Z_t^2}.}
\]

Equivalently,

\[
\boxed{
\log\frac{Z_t}{Z_0}
=
\int_0^t\frac{dZ_s}{Z_s}
-\frac12\int_0^t\frac{d[Z,Z]_s}{Z_s^2},}
\qquad t\le\tau_\varepsilon.
\]

Writing a continuous logarithm as

\[
\log Z_t=\log R_t+i\Theta_t
\]

shows that its real part is log-radius and its imaginary part is the
continuously unwrapped winding angle.

## 6. Stochastic logarithm and exponential reconstruction

Define the relative stochastic integral

\[
L_t=\int_0^t\frac{dZ_s}{Z_s}.
\]

Since

\[
d[L,L]_t=\frac{d[Z,Z]_t}{Z_t^2},
\]

the logarithm identity becomes

\[
\log\frac{Z_t}{Z_0}=L_t-\frac12[L,L]_t.
\]

Therefore

\[
\boxed{
Z_t
=Z_0\exp\!\left(
\int_0^t\frac{dZ_s}{Z_s}
-\frac12\int_0^t\frac{d[Z,Z]_s}{Z_s^2}
\right).}
\]

This is the continuous complex stochastic-exponential reconstruction of a
nonvanishing process.

For isotropic planar Brownian motion, \([Z,Z]=0\), so it simplifies to

\[
\boxed{
Z_t
=Z_0\exp\!\left(\int_0^t\frac{dZ_s}{Z_s}\right).}
\]

The exponent is not a Brownian motion at deterministic speed. Its real and
imaginary parts share the state-dependent clock

\[
H_t=\int_0^t\frac{\sigma^2}{R_s^2}\,ds.
\]

## 7. Finite-grid diagnostics

For a uniform grid with \(N\) steps over \([0,T]\),

\[
\Delta Z_k=\sigma\sqrt{\frac TN}(\xi_k+i\eta_k),
\]

where \(\xi_k,\eta_k\) are independent standard normal variables. Then

\[
Q_N^{\mathrm{self}}=\sum_k(\Delta Z_k)^2
\]

has zero mean and converges to \(0\). Its real and imaginary parts each have

\[
\operatorname{Var}(\operatorname{Re}Q_N^{\mathrm{self}})
=\operatorname{Var}(\operatorname{Im}Q_N^{\mathrm{self}})
=\frac{4\sigma^4T^2}{N}.
\]

In contrast,

\[
Q_N^{\mathrm{energy}}=\sum_k|\Delta Z_k|^2
\]

satisfies

\[
\mathbb E Q_N^{\mathrm{energy}}=2\sigma^2T,
\qquad
\operatorname{Var}(Q_N^{\mathrm{energy}})
=\frac{4\sigma^4T^2}{N}.
\]

These two limits will be checked independently in the Phase 2 notebook.

## 8. Classification

| Statement | Meaning |
|---|---|
| \(d[Z,Z]=0\) for isotropic planar Brownian motion | exact complex-bilinear quadratic-variation identity |
| \(d[Z,\overline Z]=2\sigma^2dt\) | exact Euclidean quadratic-variation identity under this normalization |
| \(\sum(\Delta Z)^2\to0\) | quadratic-variation convergence |
| \(\sum|\Delta Z|^2\to2\sigma^2T\) | Euclidean quadratic-variation convergence |
| \(d\log Z=dZ/Z\) | localized Itô identity in the isotropic nonvanishing case |
| \(Z=Z_0\exp(\int dZ/Z)\) | localized pathwise stochastic-exponential identity |
