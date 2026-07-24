# Planar Brownian Motion in Polar Coordinates

## 1. Cartesian model

Let

\[
Z_t=X_t+iY_t,
\]

where, away from any stopping issue,

\[
dX_t=b_x(t,X_t,Y_t)dt+\sigma dW^1_t,
\qquad
dY_t=b_y(t,X_t,Y_t)dt+\sigma dW^2_t,
\]

and \(W^1,W^2\) are independent Brownian motions. Define

\[
R_t=\sqrt{X_t^2+Y_t^2},\qquad
\Theta_t=\operatorname{atan2}(Y_t,X_t)
\]

on a continuous angular branch while \(R_t>0\).

Write

\[
e_r=(\cos\Theta,\sin\Theta),\qquad
e_\theta=(-\sin\Theta,\cos\Theta).
\]

## 2. Radial SDE

For \(r(x,y)=\sqrt{x^2+y^2}\),

\[
\nabla r=e_r,\qquad
\Delta r=\frac1r
\quad (r>0).
\]

The two-dimensional Itô formula gives

\[
dR_t
=\left(e_r\cdot b+\frac{\sigma^2}{2R_t}\right)dt
+\sigma\left(\cos\Theta_t\,dW^1_t
+\sin\Theta_t\,dW^2_t\right).
\]

Define

\[
dB^R_t
=\cos\Theta_t\,dW^1_t+\sin\Theta_t\,dW^2_t.
\]

Its quadratic variation is \(dt\), so it is a Brownian motion by Lévy's
characterization. Hence

\[
\boxed{
dR_t
=\left(e_r\cdot b+\frac{\sigma^2}{2R_t}\right)dt
+\sigma dB^R_t.}
\]

With \(b=0\), the radius is a two-dimensional Bessel process (scaled by
\(\sigma\)). The positive drift \(\sigma^2/(2R)\) is a geometric Itô
correction.

## 3. Angular SDE

For a local branch of
\(\theta(x,y)=\operatorname{atan2}(y,x)\),

\[
\nabla\theta=\frac1r e_\theta,\qquad
\Delta\theta=0
\quad (r>0).
\]

Therefore

\[
d\Theta_t
=\frac{e_\theta\cdot b}{R_t}dt
+\frac{\sigma}{R_t}
\left(-\sin\Theta_t\,dW^1_t
+\cos\Theta_t\,dW^2_t\right).
\]

Define

\[
dB^\Theta_t
=-\sin\Theta_t\,dW^1_t+\cos\Theta_t\,dW^2_t.
\]

Then

\[
\boxed{
d\Theta_t
=\frac{e_\theta\cdot b}{R_t}dt
+\frac{\sigma}{R_t}dB^\Theta_t.}
\]

Moreover,

\[
d[B^R,B^\Theta]_t=0.
\]

The pair \((B^R,B^\Theta)\) is a two-dimensional Brownian motion. In the
drift-free isotropic case,

\[
dR_t=\frac{\sigma^2}{2R_t}dt+\sigma dB^R_t,
\qquad
d\Theta_t=\frac{\sigma}{R_t}dB^\Theta_t.
\]

The angular clock runs faster near the origin.

## 4. Reconstructing the Cartesian equation

Apply the two-dimensional Itô formula to
\(Z=Re^{i\Theta}\):

\[
\begin{aligned}
dZ
={}&e^{i\Theta}dR
+iRe^{i\Theta}d\Theta
+i e^{i\Theta}d[R,\Theta]\\
&-\frac12Re^{i\Theta}d[\Theta].
\end{aligned}
\]

For isotropic planar Brownian motion,

\[
d[R,\Theta]=0,\qquad
d[\Theta]=\frac{\sigma^2}{R^2}dt.
\]

The radial Bessel drift and angular Itô correction cancel:

\[
e^{i\Theta}\frac{\sigma^2}{2R}dt
-\frac12Re^{i\Theta}\frac{\sigma^2}{R^2}dt=0.
\]

What remains is

\[
\boxed{
dZ_t
=\sigma e^{i\Theta_t}dB^R_t
+i\sigma e^{i\Theta_t}dB^\Theta_t
=\sigma(dW^1_t+i\,dW^2_t).}
\]

This cancellation is the planar analogue of the inward correction in pure
stochastic rotation.

## 5. Skew-product interpretation

In the drift-free case, define the random clock

\[
H_t=\int_0^t\frac{\sigma^2}{R_s^2}\,ds.
\]

The angular local martingale has quadratic variation \(H_t\), so the
Dambis–Dubins–Schwarz theorem represents the unwrapped angle as a
one-dimensional Brownian motion evaluated at this clock:

\[
\Theta_t-\Theta_0=\widehat W_{H_t}.
\]

The classical planar Brownian skew-product theorem strengthens this to a
representation with an angular Brownian motion independent of the radial
Bessel process. The essential point for this project is that planar Brownian
motion does not have a constant-speed Brownian phase: its phase volatility is
\(\sigma/R_t\).

## 6. Which process is the “polar random walk”?

There are two legitimate but different answers.

### Brownian phase on a circle

\[
Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)}.
\]

- radius fixed;
- phase has constant volatility;
- noise is tangent to the circle;
- best model of stochastic rotation.

### Planar Brownian motion

\[
Z_t=Z_0+\sigma(W^1_t+iW^2_t).
\]

- noise is additive in Cartesian coordinates;
- radius is Bessel;
- phase volatility is state dependent, \(\sigma/R_t\);
- best model of an unconstrained two-dimensional random walk.

Neither is a polar rewriting of the one-dimensional increment
\(\mu dt+\sigma dW\). Each adds genuinely two-dimensional state structure.

## 7. Singularity at the origin

The derivatives of \(R\) and \(\Theta\) used above are singular at \(R=0\).
The SDEs are therefore understood on intervals where \(R_t>0\), or after
stopping before \(R_t\) becomes too small. Planar Brownian motion started at a
nonzero point almost surely does not hit that exact point \(0\), but it visits
arbitrarily small neighborhoods, so numerical angle estimates still become
unstable near the origin. General planar diffusions may hit zero and require
separate boundary analysis.
