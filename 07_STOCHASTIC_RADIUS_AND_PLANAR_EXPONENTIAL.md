# Stochastic Radius and the Planar Exponential

## 1. Why a second Brownian direction is necessary

Suppose

\[
dA_t=a_tdt+u_t\cdot dW_t,\qquad
d\Theta_t=\omega_tdt+v_t\cdot dW_t,
\]

where \(A=\log R\). The instantaneous covariance of
\((A,\Theta)\) is

\[
K_t=
\begin{pmatrix}
\lVert u_t\rVert^2 & u_t\cdot v_t\\
u_t\cdot v_t & \lVert v_t\rVert^2
\end{pmatrix}.
\]

With one real Brownian driver, \(u_t,v_t\) are scalars and

\[
\det K_t=u_t^2v_t^2-(u_tv_t)^2=0.
\]

The diffusion has rank at most one. It may have both a random radius and a
random angle, but their instantaneous noise is constrained to one direction.
It cannot reproduce the full-rank covariance of planar Brownian motion.

Two independent Brownian drivers allow

\[
\det K_t>0.
\]

This is the precise reason a complete planar Brownian representation requires
more stochastic structure than the original one-dimensional random walk.

## 2. Cartesian model and normalization

Let

\[
Z_t=X_t+iY_t
\]

solve

\[
dX_t=\sigma dW_t^1,\qquad
dY_t=\sigma dW_t^2,
\]

with \(W^1,W^2\) independent and \(Z_0\ne0\). Thus

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2).
\]

This project does not divide the complex Brownian motion by \(\sqrt2\).
Consequently,

\[
\mathbb E|Z_t-Z_0|^2=2\sigma^2t.
\]

Define

\[
R_t=|Z_t|,\qquad Z_t=R_te^{i\Theta_t},
\]

where \(\Theta\) is a continuous lift of the argument.

## 3. Radial equation

For

\[
r(x,y)=\sqrt{x^2+y^2},
\]

\[
\nabla r=e_r,\qquad
\Delta r=\frac1r,
\qquad
e_r=(\cos\Theta,\sin\Theta).
\]

The two-dimensional Itô formula gives

\[
dR_t
=\frac{\sigma^2}{2R_t}dt
+\sigma\left(
\cos\Theta_t\,dW_t^1+\sin\Theta_t\,dW_t^2
\right).
\]

Define

\[
dB_t^R
=\cos\Theta_t\,dW_t^1+\sin\Theta_t\,dW_t^2.
\]

Then

\[
d[B^R,B^R]_t=dt.
\]

Hence

\[
\boxed{
dR_t=\frac{\sigma^2}{2R_t}dt+\sigma dB_t^R.}
\]

The radius is a scaled two-dimensional Bessel process. The outward
\(\sigma^2/(2R)\) term is an Itô/geometric drift, not an independent physical
force.

## 4. Angular equation

For a local branch of

\[
\theta(x,y)=\operatorname{atan2}(y,x),
\]

\[
\nabla\theta=\frac1r e_\theta,\qquad
\Delta\theta=0,
\qquad
e_\theta=(-\sin\Theta,\cos\Theta).
\]

Therefore

\[
d\Theta_t
=\frac{\sigma}{R_t}
\left(
-\sin\Theta_t\,dW_t^1+\cos\Theta_t\,dW_t^2
\right).
\]

Define

\[
dB_t^\Theta
=-\sin\Theta_t\,dW_t^1+\cos\Theta_t\,dW_t^2.
\]

Then

\[
\boxed{
d\Theta_t=\frac{\sigma}{R_t}dB_t^\Theta.}
\]

The adapted rotation from \((W^1,W^2)\) to
\((B^R,B^\Theta)\) is orthogonal. Consequently,

\[
d[B^R,B^R]_t=d[B^\Theta,B^\Theta]_t=dt,
\qquad
d[B^R,B^\Theta]_t=0.
\]

Lévy's characterization implies that the pair
\((B^R,B^\Theta)\) is a two-dimensional Brownian motion.

The angular variance rate is

\[
\frac{d[\Theta,\Theta]_t}{dt}=\frac{\sigma^2}{R_t^2}.
\]

Winding therefore accelerates when the path is close to the origin.

## 5. Log-radius

Let

\[
A_t=\log R_t.
\]

Applying the one-dimensional Itô formula to the Bessel equation,

\[
dA_t
=\frac1{R_t}dR_t-\frac1{2R_t^2}d[R,R]_t.
\]

Since \(d[R,R]_t=\sigma^2dt\),

\[
\begin{aligned}
dA_t
&=\frac{\sigma^2}{2R_t^2}dt
+\frac{\sigma}{R_t}dB_t^R
-\frac{\sigma^2}{2R_t^2}dt\\
&=\frac{\sigma}{R_t}dB_t^R.
\end{aligned}
\]

Thus

\[
\boxed{
d\log R_t=\frac{\sigma}{R_t}dB_t^R.}
\]

This is a local-martingale statement under localization. It should not be
promoted to a global true-martingale claim without an integrability argument.

## 6. Full stochastic polar exponential

The log-radius and angle equations are

\[
dA_t=\frac{\sigma}{R_t}dB_t^R,\qquad
d\Theta_t=\frac{\sigma}{R_t}dB_t^\Theta.
\]

Integrating gives

\[
\begin{aligned}
A_t-A_0
&=\int_0^t\frac{\sigma}{R_s}dB_s^R,\\
\Theta_t-\Theta_0
&=\int_0^t\frac{\sigma}{R_s}dB_s^\Theta.
\end{aligned}
\]

Therefore

\[
\boxed{
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{\sigma}{R_s}dB_s^R
+i\int_0^t\frac{\sigma}{R_s}dB_s^\Theta
\right].}
\]

This is the requested nonconstant-radius counterpart of

\[
r_0e^{i(\theta_0+\beta W_t)}.
\]

Its real stochastic integral changes log-radius. Its imaginary stochastic
integral changes the unwrapped angle. Both have the same state-dependent
variance clock.

## 7. Why the exponential adds no drift

Set

\[
M_t
=\int_0^t\frac{\sigma}{R_s}dB_s^R
+i\int_0^t\frac{\sigma}{R_s}dB_s^\Theta.
\]

Because the two real martingale parts have equal quadratic variations and
zero cross-variation,

\[
\begin{aligned}
d[M,M]_t
&=\frac{\sigma^2}{R_t^2}dt
-\frac{\sigma^2}{R_t^2}dt+0\\
&=0.
\end{aligned}
\]

Complex Itô's formula then gives

\[
d(e^{M_t})=e^{M_t}dM_t
\]

with no remaining \(\tfrac12d[M,M]\) term. This cancellation is exactly the
complex self-quadratic-variation identity from
`06_COMPLEX_QUADRATIC_VARIATION.md`.

## 8. Independent reconstruction of the Cartesian SDE

Apply Itô's formula directly to

\[
Z=Re^{i\Theta}.
\]

The complete differential is

\[
\begin{aligned}
dZ
={}&e^{i\Theta}dR
+iRe^{i\Theta}d\Theta
+i e^{i\Theta}d[R,\Theta]\\
&-\frac12Re^{i\Theta}d[\Theta,\Theta].
\end{aligned}
\]

Here

\[
d[R,\Theta]=0,\qquad
d[\Theta,\Theta]=\frac{\sigma^2}{R^2}dt.
\]

The radial Bessel drift and angular Itô drift cancel:

\[
e^{i\Theta}\frac{\sigma^2}{2R}dt
-\frac12Re^{i\Theta}\frac{\sigma^2}{R^2}dt=0.
\]

The remaining martingale part is

\[
\sigma e^{i\Theta}dB^R
+i\sigma e^{i\Theta}dB^\Theta.
\]

Using the adapted rotation,

\[
e^{i\Theta}(dB^R+i\,dB^\Theta)
=dW^1+i\,dW^2.
\]

Hence

\[
\boxed{dZ=\sigma(dW^1+i\,dW^2).}
\]

The polar system and the Cartesian system are therefore two exact coordinate
descriptions of the same diffusion.

## 9. Common random clock and skew product

Define

\[
H_t=\int_0^t\frac{\sigma^2}{R_s^2}ds.
\]

Then

\[
[A-A_0,A-A_0]_t
=[\Theta-\Theta_0,\Theta-\Theta_0]_t
=H_t,
\]

and

\[
[A,\Theta]_t=0.
\]

The two-dimensional Dambis–Dubins–Schwarz representation therefore converts
\((A-A_0,\Theta-\Theta_0)\) into a planar Brownian motion evaluated at the
clock \(H_t\).

The classical planar Brownian skew-product theorem makes a stronger
statement: the Brownian motion generating the angle can be chosen independent
of the entire radial Bessel process. That independence is a theorem; it does
not follow merely from zero cross-variation of two arbitrary martingales.

## 10. Circle motion versus planar motion

| Feature | Brownian phase on \(S^1\) | Planar Brownian motion |
|---|---|---|
| State | \(r_0e^{i\Theta_t}\) | \(R_te^{i\Theta_t}\) |
| Radius | fixed | Bessel, stochastic |
| Noise rank | one | two |
| Phase variance rate | constant \(\beta^2\) | \(\sigma^2/R_t^2\) |
| Complex self-QV | generally nonzero for \(dZ=i\beta Z\,dW+\cdots\) | zero in the isotropic Cartesian model |
| Generator | circle Laplacian plus drift | planar Laplacian |
| Geometry | constrained rotation | unconstrained two-dimensional diffusion |

The fixed-circle process was a correct model of stochastic rotation. The
present process is the full complex Brownian random walk.

## 11. Origin and branch conditions

Planar Brownian motion started from a nonzero point almost surely does not hit
the origin, so a continuous winding angle exists along the entire path.
Nevertheless, it visits arbitrarily small neighborhoods over long horizons,
and the factor \(1/R_t\) creates large angular increments there.

All differential derivations should first be read on

\[
[0,\tau_\varepsilon],
\qquad
\tau_\varepsilon=\inf\{t:R_t\le\varepsilon\}.
\]

Starting at \(Z_0=0\) is a separate case: the Cartesian process is perfectly
well defined, but \(\Theta_0\), \(\log R_0\), and the polar exponential are
not.
