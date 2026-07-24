# Stochastic Polar Form: Amplitude and Phase

## 1. Pure stochastic rotation

Let a drifted Brownian motion drive the angle:

\[
\Theta_t=\theta_0+\omega t+\beta W_t,
\qquad
Z_t=r_0e^{i\Theta_t}.
\]

This is already an exact stochastic polar form:

\[
\boxed{
Z_t=r_0
\exp\!\left(i[\theta_0+\omega t+\beta W_t]\right).}
\]

It has constant radius \(r_0\) and a continuously varying random phase.

Apply the one-dimensional Itô formula to
\(f(\theta)=r_0e^{i\theta}\):

\[
f'(\theta)=if(\theta),\qquad f''(\theta)=-f(\theta).
\]

Since \(d\Theta=\omega dt+\beta dW\) and
\((d\Theta)^2=\beta^2dt\),

\[
\begin{aligned}
dZ_t
&=iZ_t\,d\Theta_t-\frac12Z_t(d\Theta_t)^2\\
&=\left(i\omega-\frac{\beta^2}{2}\right)Z_tdt
  +i\beta Z_tdW_t.
\end{aligned}
\]

Therefore

\[
\boxed{
Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)}
\quad\Longleftrightarrow\quad
dZ_t=\left(i\omega-\frac{\beta^2}{2}\right)Z_tdt
     +i\beta Z_tdW_t.}
\]

The term \(-\beta^2Z_tdt/2\) is an inward radial drift in Cartesian
coordinates. It compensates exactly for the outward second-order effect of
tangential Brownian increments.

## 2. Independent constant-modulus check

Write \(\overline Z\) for the complex conjugate. From the SDE,

\[
d\overline Z_t
=\left(-i\omega-\frac{\beta^2}{2}\right)\overline Z_tdt
-i\beta\overline Z_tdW_t.
\]

The Itô product rule gives

\[
d|Z_t|^2
=\overline Z_t\,dZ_t+Z_t\,d\overline Z_t
+d[Z,\overline Z]_t.
\]

The first two terms contribute

\[
-\beta^2|Z_t|^2dt
\]

after the imaginary drift and noise cancel. The covariation is

\[
d[Z,\overline Z]_t
=(i\beta Z_t)(-i\beta\overline Z_t)dt
=\beta^2|Z_t|^2dt.
\]

Hence

\[
\boxed{d|Z_t|^2=0.}
\]

This checks constant modulus without using the explicit exponential solution.

## 3. What happens if the correction is omitted?

Consider the incorrect Itô equation

\[
d\widetilde Z_t=i\omega\widetilde Z_tdt
+i\beta\widetilde Z_tdW_t.
\]

The complex stochastic-exponential formula gives

\[
\widetilde Z_t
=Z_0\exp\!\left[
\left(i\omega+\frac{\beta^2}{2}\right)t+i\beta W_t
\right].
\]

Therefore

\[
|\widetilde Z_t|=|Z_0|e^{\beta^2t/2},
\qquad
|\widetilde Z_t|^2=|Z_0|^2e^{\beta^2t}.
\]

The omitted correction creates deterministic radial growth in the exact
solution of the wrong Itô SDE.

Euler–Maruyama also reveals the difference. With the correct drift and
\(\omega=0\),

\[
Z_{n+1}=Z_n
\left(1-\frac12\beta^2h+i\beta\Delta W_n\right).
\]

It does not preserve the radius exactly at finite \(h\). Conditionally,

\[
\mathbb E\!\left[
\frac{|Z_{n+1}|^2}{|Z_n|^2}\,\middle|\,Z_n
\right]
=1+\frac14\beta^4h^2.
\]

The per-step radial bias is second order and vanishes in the continuous-time
limit. Without the drift,

\[
\mathbb E\!\left[
\frac{|\widetilde Z_{n+1}|^2}{|\widetilde Z_n|^2}
\right]
=1+\beta^2h,
\]

which accumulates to \(e^{\beta^2T}\). A structure-preserving phase update
\(Z_{n+1}=Z_ne^{i(\omega h+\beta\Delta W_n)}\) preserves the radius exactly.

## 4. Itô versus Stratonovich

The same constant-radius motion has Stratonovich form

\[
\boxed{
dZ_t=i\omega Z_tdt+i\beta Z_t\circ dW_t.}
\]

For \(b(z)=i\beta z\), the Itô correction is

\[
\frac12b'(z)b(z)
=\frac12(i\beta)(i\beta z)
=-\frac12\beta^2z.
\]

Thus the Stratonovich equation converts to the Itô equation already derived.
The Stratonovich form exposes the geometry: its noise vector field is tangent
to every circle. The Itô form exposes the quadratic-variation compensation.

## 5. General stochastic amplitude–phase formula

Let \(W_t=(W^1_t,\ldots,W^m_t)\) be an \(m\)-dimensional standard Brownian
motion. Model log-amplitude \(A_t=\log R_t\) and an unwrapped phase
\(\Theta_t\) by

\[
dA_t=a_tdt+u_t\cdot dW_t,
\qquad
d\Theta_t=\omega_tdt+v_t\cdot dW_t,
\]

where \(u_t,v_t\in\mathbb R^m\). Define

\[
\boxed{Z_t=e^{A_t+i\Theta_t}=R_te^{i\Theta_t}.}
\]

For \(Y=A+i\Theta\),

\[
d[Y]_t
=\sum_{j=1}^m(u_t^j+iv_t^j)^2dt
=\left(\|u_t\|^2-\|v_t\|^2
+2i\,u_t\cdot v_t\right)dt.
\]

Applying Itô's lemma to \(e^Y\) gives the unified SDE

\[
\boxed{
\begin{aligned}
\frac{dZ_t}{Z_t}
={}&\left[
a_t+\frac12(\|u_t\|^2-\|v_t\|^2)
+i(\omega_t+u_t\cdot v_t)
\right]dt\\
&+(u_t+i v_t)\cdot dW_t.
\end{aligned}}
\]

This is the stochastic counterpart of \(z=re^{i\theta}\). It contains two
quadratic-variation corrections:

- \(-\|v\|^2/2\) is the radial compensation for phase noise;
- \(i\,u\cdot v\) is a phase drift induced by correlated amplitude and phase
  noise.

The radius itself obeys

\[
\frac{dR_t}{R_t}
=\left(a_t+\frac12\|u_t\|^2\right)dt+u_t\cdot dW_t.
\]

If one prefers to prescribe

\[
\frac{dR_t}{R_t}=\alpha_tdt+u_t\cdot dW_t,
\]

then \(a_t=\alpha_t-\|u_t\|^2/2\), and the unified formula becomes

\[
\boxed{
\frac{dZ_t}{Z_t}
=\left[
\alpha_t-\frac12\|v_t\|^2
+i(\omega_t+u_t\cdot v_t)
\right]dt
+(u_t+i v_t)\cdot dW_t.}
\]

For constant coefficients this integrates exactly:

\[
Z_t
=Z_0\exp\!\left[
(a+i\omega)t+(u+i v)\cdot W_t
\right].
\]

This is the requested form most directly analogous to \(re^{i\theta}\):
the real part of the exponent controls log-radius and the imaginary part
controls phase.

## 6. Important special cases

### Arithmetic diffusion

\[
dX=\mu dt+\sigma dW
\]

is additive and real; it is not naturally a polar model.

### Geometric Brownian motion

Set \(v=0\). Then the exponent has random real part only, producing stochastic
amplitude and fixed phase.

### Pure stochastic rotation

Set \(u=0\), \(a=0\). Then \(R_t\) is constant and the exponent has random
imaginary part only.

### Independent amplitude and phase

Use separate Brownian drivers, for example

\[
dA=a\,dt+\sigma_R\,dB,\qquad
d\Theta=\omega\,dt+\beta\,dW,\qquad d[B,W]=0.
\]

Then \(u\cdot v=0\).

### Correlated amplitude and phase

If \(d[B,W]_t=\rho\,dt\), the corresponding term is
\(\rho\sigma_R\beta\). Correlation therefore adds the phase drift
\(i\rho\sigma_R\beta Z_tdt\) to the complex SDE.

## 7. Branch and origin issues

- \(R_t=|Z_t|\ge0\) is single-valued.
- \(\arg Z_t\) is defined only modulo \(2\pi\). A continuous unwrapped phase
  can be chosen along a path that does not hit the origin.
- At \(Z_t=0\), both \(\log R_t\) and the phase are singular.
- The formula based on \(A_t=\log R_t\) therefore applies up to the first
  hitting time of zero unless nonvanishing is known.
