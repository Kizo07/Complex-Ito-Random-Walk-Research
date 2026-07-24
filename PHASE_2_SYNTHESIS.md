# Phase 2 Synthesis: Beyond Brownian Motion on a Circle

## 1. The fixed-radius limitation

The Phase 1 model

\[
Z_t=r_0e^{i(\theta_0+\beta W_t)}
\]

is an exact stochastic rotation, but it is constrained to a circle. It has
one random degree of freedom and cannot represent unconstrained Brownian
motion in the complex plane.

The correct planar starting point is

\[
\boxed{
Z_t=Z_0+\sigma(W_t^1+i\,W_t^2),}
\]

where \(W^1,W^2\) are independent standard Brownian motions.

Its real and imaginary coordinates each have variance \(\sigma^2t\), so

\[
\mathbb E|Z_t-Z_0|^2=2\sigma^2t.
\]

## 2. The stochastic radius and angle

For \(Z_0\ne0\), write

\[
Z_t=R_te^{i\Theta_t}
\]

with a continuously unwrapped angle. Define the adapted Brownian motions

\[
\begin{aligned}
dB_t^R
&=\cos\Theta_t\,dW_t^1+\sin\Theta_t\,dW_t^2,\\
dB_t^\Theta
&=-\sin\Theta_t\,dW_t^1+\cos\Theta_t\,dW_t^2.
\end{aligned}
\]

Then

\[
\boxed{
\begin{aligned}
dR_t&=\frac{\sigma^2}{2R_t}dt+\sigma dB_t^R,\\
d\Theta_t&=\frac{\sigma}{R_t}dB_t^\Theta.
\end{aligned}}
\]

The radius is a two-dimensional Bessel process. The phase is not a
constant-speed Brownian motion: its variance rate is \(\sigma^2/R_t^2\).

This is the structural change that takes the project beyond the circle.

## 3. The full planar polar-exponential formula

Let

\[
A_t=\log R_t.
\]

The Bessel drift cancels in the log-radius equation:

\[
dA_t=\frac{\sigma}{R_t}dB_t^R.
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

This is the sought stochastic counterpart of

\[
z=re^{i\theta}
\]

for full planar Brownian motion:

- the real part of the exponent is the stochastic log-radius;
- the imaginary part is the stochastic winding angle;
- both use the same endogenous clock;
- neither radius nor phase is fixed.

The formula is exact but state dependent: \(R_s\) appears inside its own
stochastic exponent. It is a stochastic-logarithm representation, not an
independent-increments closed form like geometric Brownian motion.

## 4. Why no Itô correction remains in the isotropic exponent

There are two different complex quadratic variations:

\[
[Z,Z]
\quad\text{and}\quad
[Z,\overline Z].
\]

For isotropic planar Brownian motion,

\[
\boxed{[Z,Z]_t=0,}
\]

because

\[
(dW^1+i\,dW^2)^2
=dt-dt+0=0.
\]

But

\[
\boxed{[Z,\overline Z]_t=2\sigma^2t,}
\]

so the process still has positive Euclidean quadratic variation.

The complex logarithm obeys

\[
d\log Z_t
=\frac{dZ_t}{Z_t}
-\frac12\frac{d[Z,Z]_t}{Z_t^2}.
\]

Isotropy makes the second term vanish, giving

\[
\boxed{
\log\frac{Z_t}{Z_0}
=\int_0^t\frac{dZ_s}{Z_s},}
\]

and therefore

\[
\boxed{
Z_t
=Z_0\exp\!\left(\int_0^t\frac{dZ_s}{Z_s}\right).}
\]

This is the deepest bridge found so far. The \(i^2=-1\) cancellation occurs
between the quadratic variations of two independent Brownian coordinates,
not by identifying one \(dW\) with \(i\).

## 5. Why two Brownian drivers matter

For

\[
dA=u\cdot dW,\qquad d\Theta=v\cdot dW,
\]

the polar covariance is

\[
\begin{pmatrix}
\lVert u\rVert^2&u\cdot v\\
u\cdot v&\lVert v\rVert^2
\end{pmatrix}.
\]

With one real Brownian driver its determinant is zero. Radius and angle may
both fluctuate, but the instantaneous diffusion remains rank one.

Full planar Brownian motion requires rank two. In the adapted polar basis,

\[
u=\left(\frac{\sigma}{R},0\right),
\qquad
v=\left(0,\frac{\sigma}{R}\right).
\]

The two independent directions are radial and angular.

## 6. The random clock

Both stochastic logarithmic coordinates have quadratic variation

\[
H_t=\int_0^t\frac{\sigma^2}{R_s^2}ds:
\]

\[
[A-A_0]_t=[\Theta-\Theta_0]_t=H_t,
\qquad
[A,\Theta]_t=0.
\]

The classical skew-product theorem represents the angle as a Brownian motion
run on this clock, with the angular Brownian motion independent of the radial
Bessel process.

This explains the winding geometry:

- far from the origin, the angular clock runs slowly;
- near the origin, it accelerates sharply;
- the radius determines the speed at which phase randomness accumulates.

## 7. General complex diffusion

For

\[
d\mathbf X=b\,dt+\Sigma\,dW,
\qquad
C=\Sigma\Sigma^\mathsf T,
\]

the polar equations are

\[
\boxed{
dR
=
\left[
e_r\cdot b+
\frac{\operatorname{tr}C-e_r^\mathsf TCe_r}{2R}
\right]dt
+e_r^\mathsf T\Sigma\,dW,}
\]

\[
\boxed{
d\Theta
=
\left[
\frac{e_\theta\cdot b}{R}
-\frac{e_r^\mathsf TCe_\theta}{R^2}
\right]dt
+\frac{e_\theta^\mathsf T\Sigma}{R}\,dW.}
\]

The complex self-QV rate is

\[
q=C_{11}-C_{22}+2iC_{12}.
\]

The general exponential reconstruction becomes

\[
\boxed{
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{dZ_s}{Z_s}
-\frac12\int_0^t\frac{q_s}{Z_s^2}ds
\right].}
\]

The correction disappears exactly when \(C\) is isotropic.

## 8. Exact discrete random-walk form

For a Cartesian random walk

\[
Z_{n+1}=Z_n+\Delta Z_n,
\]

the exact multiplicative update is

\[
\boxed{
Z_{n+1}
=Z_n\exp\!\left[
\operatorname{Log}_{\mathrm{cont}}
\left(1+\frac{\Delta Z_n}{Z_n}\right)
\right].}
\]

Its exponent has two stochastic components:

\[
\operatorname{Re}\operatorname{Log}_{\mathrm{cont}}
\left(1+\frac{\Delta Z_n}{Z_n}\right)
=\log\frac{R_{n+1}}{R_n},
\]

\[
\operatorname{Im}\operatorname{Log}_{\mathrm{cont}}
\left(1+\frac{\Delta Z_n}{Z_n}\right)
=\Delta\Theta_n.
\]

The local expansion

\[
\operatorname{Log}(1+q_n)
=q_n-\frac12q_n^2+O(q_n^3)
\]

converges to the continuous stochastic logarithm. Thus the additive random
walk and the multiplicative polar form are two exact finite-grid
descriptions connected by a complex logarithm.

## 9. Numerical evidence

The Phase 2 notebook verified:

- \(\sum(\Delta Z)^2\to0\) with RMS slope \(-0.5010\);
- \(\sum|\Delta Z|^2\to2\sigma^2T\);
- the Rice terminal-radius law with KS statistic \(0.001589\);
- Cartesian-polar path reconstruction to \(4.578\times10^{-16}\);
- angular and log-radial quadratic variation equal to the random clock;
- radius-binned angular variance falling from \(0.822970\) to \(0.076857\)
  as mean radius increased from \(0.56349\) to \(1.81369\);
- conditional Bessel drift discrepancies within \(1.131\) Monte Carlo
  standard errors;
- isotropic stochastic-log reconstruction with first-order slope \(0.5007\);
- anisotropic failure of the uncorrected exponential;
- convergence of the anisotropic Itô-corrected formula with slope \(0.5036\).

## 10. What has and has not been achieved

### Achieved

- a stochastic radius rather than fixed \(r_0\);
- full-rank planar Brownian covariance;
- an exact stochastic polar decomposition;
- an exact complex stochastic-logarithm/exponential representation;
- a finite-step multiplicative random-walk formula;
- a generalization to drift, anisotropy, and correlation.

### Not claimed

- that \(dW\) is an imaginary number;
- that a finite Brownian increment literally squares to \(dt\);
- that the stochastic exponent is independent of the process it represents;
- that polar coordinates are valid at the origin;
- that zero cross-variation alone proves independence;
- that all general planar diffusions avoid zero.

## 11. Final Phase 2 answer

The fixed-circle model was not the end of the analogy. For a full planar
Brownian motion, the correct stochastic polar form is

\[
\boxed{
Z_t=R_te^{i\Theta_t},
\qquad
dR_t=\frac{\sigma^2}{2R_t}dt+\sigma dB_t^R,
\qquad
d\Theta_t=\frac{\sigma}{R_t}dB_t^\Theta.}
\]

Equivalently,

\[
\boxed{
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{\sigma}{R_s}dB_s^R
+i\int_0^t\frac{\sigma}{R_s}dB_s^\Theta
\right].}
\]

This formula represents Brownian motion throughout the complex plane, not
merely on a circle. The radius is random, the phase is random, and their
coupling through \(1/R_t\) is the essential geometry.
