# General Complex Diffusions in Polar Coordinates

## 1. Cartesian model

Let

\[
\mathbf X_t=
\begin{pmatrix}X_t\\Y_t\end{pmatrix}
\]

solve

\[
d\mathbf X_t
=b(t,\mathbf X_t)dt+\Sigma(t,\mathbf X_t)d\mathbf W_t,
\]

where \(\mathbf W\) is \(m\)-dimensional Brownian motion and

\[
C=\Sigma\Sigma^\mathsf T
\]

is the \(2\times2\) instantaneous Cartesian covariance matrix. Define

\[
Z=X+iY,\qquad
R=|Z|,\qquad
\Theta=\arg Z,
\]

on a stopped region \(R>\varepsilon\).

Write

\[
e_r=
\begin{pmatrix}\cos\Theta\\\sin\Theta\end{pmatrix},
\qquad
e_\theta=
\begin{pmatrix}-\sin\Theta\\\cos\Theta\end{pmatrix}.
\]

## 2. Radial SDE

The Hessian of \(R\) is

\[
\nabla^2R=\frac1R(I-e_re_r^\mathsf T).
\]

The two-dimensional Itô formula gives

\[
\boxed{
dR
=
\left[
e_r\cdot b
+\frac{\operatorname{tr}C-e_r^\mathsf TCe_r}{2R}
\right]dt
+e_r^\mathsf T\Sigma\,dW.}
\]

The covariance correction is the variance in the tangential direction:

\[
\operatorname{tr}C-e_r^\mathsf TCe_r
=e_\theta^\mathsf TCe_\theta.
\]

Tangential noise creates an outward radial Itô drift because a locally
straight tangential step lies outside the original circle to second order.

## 3. Angular SDE

The gradient and Hessian of the local angle are

\[
\nabla\Theta=\frac1R e_\theta,
\]

\[
\nabla^2\Theta
=-\frac1{R^2}
\left(e_re_\theta^\mathsf T+e_\theta e_r^\mathsf T\right).
\]

Therefore

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

Anisotropic covariance can induce angular drift even when the Cartesian drift
\(b\) is zero.

## 4. Log-radius SDE

For \(A=\log R\),

\[
\nabla A=\frac1R e_r,
\qquad
\nabla^2A=\frac1{R^2}(I-2e_re_r^\mathsf T).
\]

Itô's formula yields

\[
\boxed{
dA
=
\left[
\frac{e_r\cdot b}{R}
+\frac{\operatorname{tr}C-2e_r^\mathsf TCe_r}{2R^2}
\right]dt
+\frac{e_r^\mathsf T\Sigma}{R}\,dW.}
\]

Set

\[
\begin{aligned}
a&=\frac{e_r\cdot b}{R}
+\frac{\operatorname{tr}C-2e_r^\mathsf TCe_r}{2R^2},\\
\omega&=\frac{e_\theta\cdot b}{R}
-\frac{e_r^\mathsf TCe_\theta}{R^2},\\
u&=\frac{\Sigma^\mathsf Te_r}{R},\\
v&=\frac{\Sigma^\mathsf Te_\theta}{R}.
\end{aligned}
\]

Then

\[
dA=a\,dt+u\cdot dW,\qquad
d\Theta=\omega\,dt+v\cdot dW.
\]

## 5. Covariance in polar coordinates

The instantaneous covariance of \((A,\Theta)\) is

\[
K=
\begin{pmatrix}
\lVert u\rVert^2 & u\cdot v\\
u\cdot v & \lVert v\rVert^2
\end{pmatrix}
=\frac1{R^2}
\begin{pmatrix}
e_r^\mathsf TCe_r & e_r^\mathsf TCe_\theta\\
e_r^\mathsf TCe_\theta & e_\theta^\mathsf TCe_\theta
\end{pmatrix}.
\]

Since \((e_r,e_\theta)\) is an orthonormal basis,

\[
\boxed{\det K=\frac{\det C}{R^4}.}
\]

Consequences:

- if \(C\) has rank one, the polar noise also has rank one;
- if \(C\) is positive definite, both polar directions are genuinely noisy;
- changing coordinates cannot manufacture a second independent Brownian
  direction.

## 6. Reconstruction with the unified amplitude-phase formula

Phase 1 established

\[
\frac{dZ}{Z}
=
\left[
a+\frac12(\lVert u\rVert^2-\lVert v\rVert^2)
+i(\omega+u\cdot v)
\right]dt
+(u+i v)\cdot dW.
\]

For the coefficients above,

\[
\lVert u\rVert^2
=\frac{e_r^\mathsf TCe_r}{R^2},
\qquad
\lVert v\rVert^2
=\frac{e_\theta^\mathsf TCe_\theta}{R^2},
\]

and

\[
u\cdot v=\frac{e_r^\mathsf TCe_\theta}{R^2}.
\]

The covariance terms cancel:

\[
a+\frac12(\lVert u\rVert^2-\lVert v\rVert^2)
=\frac{e_r\cdot b}{R},
\]

\[
\omega+u\cdot v=\frac{e_\theta\cdot b}{R}.
\]

Hence

\[
\frac{dZ}{Z}
=
\frac{e_r\cdot b+i\,e_\theta\cdot b}{R}dt
+(u+i v)\cdot dW.
\]

Multiplying by \(Z=Re^{i\Theta}\) reconstructs exactly

\[
dZ=(b_x+ib_y)dt
+\sum_k(\Sigma_{1k}+i\Sigma_{2k})dW^k.
\]

This independent cancellation check verifies the general polar equations.

## 7. Complex logarithm form

Define

\[
b_\mathbb C=b_x+ib_y,
\qquad
\gamma_k=\Sigma_{1k}+i\Sigma_{2k}.
\]

Then

\[
dZ=b_\mathbb Cdt+\sum_k\gamma_kdW^k,
\]

and

\[
d[Z,Z]=q\,dt,
\qquad
q=\sum_k\gamma_k^2
=C_{11}-C_{22}+2iC_{12}.
\]

The localized logarithm equation is

\[
\boxed{
d\log Z
=
\left(
\frac{b_\mathbb C}{Z}
-\frac{q}{2Z^2}
\right)dt
+\sum_k\frac{\gamma_k}{Z}dW^k.}
\]

Taking real and imaginary parts reproduces the log-radius and angle equations.

The exponential reconstruction is

\[
\boxed{
Z_t=Z_0\exp\!\left[
\int_0^t\frac{dZ_s}{Z_s}
-\frac12\int_0^t\frac{q_s}{Z_s^2}ds
\right].}
\]

For isotropic covariance \(C=\sigma^2I\), \(q=0\), recovering the simpler
planar Brownian formula.

## 8. Constant complex drift

Consider

\[
dZ_t=\mu_\mathbb Cdt+\sigma(dW_t^1+i\,dW_t^2).
\]

The polar equations become

\[
dR
=
\left(
e_r\cdot\mu+\frac{\sigma^2}{2R}
\right)dt+\sigma dB^R,
\]

\[
d\Theta
=\frac{e_\theta\cdot\mu}{R}dt
+\frac{\sigma}{R}dB^\Theta,
\]

and

\[
d\log R
=\frac{e_r\cdot\mu}{R}dt
+\frac{\sigma}{R}dB^R.
\]

Since isotropy still gives \([Z,Z]=0\),

\[
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{\mu_\mathbb C}{Z_s}ds
+\int_0^t\frac{\sigma(dW_s^1+i\,dW_s^2)}{Z_s}
\right].
\]

This representation is exact but implicit because the exponent's
coefficients depend on \(Z_s\).

## 9. Anisotropic independent noise

Let

\[
dX=\sigma_xdW^1,\qquad dY=\sigma_ydW^2.
\]

Then

\[
C=
\begin{pmatrix}
\sigma_x^2&0\\0&\sigma_y^2
\end{pmatrix},
\qquad
q=\sigma_x^2-\sigma_y^2.
\]

If \(\sigma_x\ne\sigma_y\), the holomorphic Itô correction does not cancel:

\[
d\log Z
=\frac{dZ}{Z}
-\frac{\sigma_x^2-\sigma_y^2}{2Z^2}dt.
\]

This will be the notebook's controlled counterexample. It demonstrates that
the correction-free exponential is special to conformal planar noise.

## 10. Correlated Cartesian noise

If

\[
d[X,Y]_t=\rho\sigma_x\sigma_y\,dt,
\]

then

\[
q=\sigma_x^2-\sigma_y^2
+2i\rho\sigma_x\sigma_y.
\]

The real part of \(q/Z^2\) affects log-radius drift; the imaginary part affects
angular drift. Cartesian correlation and polar amplitude-phase correlation
are two coordinate descriptions of the same quadratic-covariation structure.

## 11. Rank-one special cases

### Radial-only noise

If

\[
dZ=e^{i\Theta}\sigma_RdW,
\]

the stochastic motion is instantaneously radial. The covariance has rank one.

### Tangential-only noise

If

\[
dZ=i e^{i\Theta}\sigma_\Theta dW
\]

without the necessary Itô drift, the radius grows. A constant-radius Itô
model must add

\[
-\frac{\sigma_\Theta^2}{2R}e^{i\Theta}dt
\]

in Cartesian form, equivalently the inward
\(-\beta^2Z/2\) correction from Phase 1.

### Shared amplitude-phase noise

If both \(A\) and \(\Theta\) use the same real Brownian driver, their
covariance matrix is singular even when both coordinates fluctuate. This is a
random curve-like diffusion in the plane, not planar Brownian motion.

## 12. Interpretation

The general result separates three phenomena:

1. **drift projection:** \(e_r\cdot b\) and \(e_\theta\cdot b\);
2. **coordinate curvature:** the \(C/R\) and \(C/R^2\) Itô terms;
3. **noise rank and conformality:** encoded by \(\det C\) and
   \(q=C_{11}-C_{22}+2iC_{12}\).

The simple stochastic polar exponential survives without a quadratic
correction precisely in the conformal isotropic case.
