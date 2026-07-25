# 15. Phase 4 Equivalence, Rank, and Limits

## 15.1 General one-driver complex GBM in log-polar form

Consider the established complex linear SDE

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
A\,dt+B\,dW_t,
\qquad
A,B\in\mathbb C,
\qquad
\mathcal Z_0\ne0,
\tag{15.1}
\]

driven by one real Brownian motion. Write

\[
A=A_r+iA_i,
\qquad
B=\sigma+i\beta.
\tag{15.2}
\]

Its exact solution is

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\tag{15.3}
\]

Taking the real and imaginary parts of the continuous log lift gives

\[
\log\frac{R_t}{R_0}
=
\left(
A_r-\frac12\sigma^2+\frac12\beta^2
\right)t+\sigma W_t,
\tag{15.4}
\]

\[
\Theta_t-\Theta_0
=
(A_i-\sigma\beta)t+\beta W_t.
\tag{15.5}
\]

It follows that every one-driver complex GBM has the log-polar SDE

\[
\boxed{
\frac{dR_t}{R_t}
=
\left(A_r+\frac12\beta^2\right)dt+\sigma\,dW_t,
}
\tag{15.6}
\]

\[
\boxed{
d\Theta_t
=
(A_i-\sigma\beta)dt+\beta\,dW_t.
}
\tag{15.7}
\]

Conversely, prescribing

\[
\frac{dR_t}{R_t}=\mu\,dt+\sigma\,dW_t,
\qquad
d\Theta_t=\omega\,dt+\beta\,dW_t
\tag{15.8}
\]

forces

\[
\boxed{
A=\mu-\frac12\beta^2+i(\omega+\sigma\beta),
\qquad
B=\sigma+i\beta.
}
\tag{15.9}
\]

This is the Phase 4 normal form.

## 15.2 Phase 3 as the fixed-spiral subfamily

Let

\[
L_t
=
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\tag{15.10}
\]

be the log-return of a real GBM. The Phase 3 construction applied to \(L_t\)
is

\[
\mathcal Z_t
=
\mathcal Z_0e^{cL_t},
\qquad c=\alpha+i\gamma.
\tag{15.11}
\]

Its modulus is

\[
|\mathcal Z_t|=|\mathcal Z_0|e^{\alpha L_t}.
\tag{15.12}
\]

To reproduce the original GBM modulus rather than a power of it, one must set

\[
\alpha=1.
\tag{15.13}
\]

Then

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
+i\gamma
\left(
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right)
\right].
\tag{15.14}
\]

Comparing with the Phase 4 model,

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)t
+(\sigma+i\beta)W_t
\right],
\tag{15.15}
\]

shows exact equivalence if and only if

\[
\boxed{
\beta=\gamma\sigma,
\qquad
\omega=\gamma\left(\mu-\frac12\sigma^2\right).
}
\tag{15.16}
\]

Thus Phase 3 is embedded in Phase 4 as a parameter-constrained family.

## 15.3 When is the path on one fixed logarithmic spiral?

Assume \(\sigma\ne0\) and write

\[
a=\mu-\frac12\sigma^2.
\]

From

\[
\log(R_t/R_0)=at+\sigma W_t
\]

we obtain

\[
W_t=\frac{\log(R_t/R_0)-at}{\sigma}.
\]

Substitution into the phase gives

\[
\boxed{
\Theta_t-\Theta_0
=
\frac{\beta}{\sigma}\log\frac{R_t}{R_0}
+
\left(
\omega-\frac{\beta}{\sigma}a
\right)t.
}
\tag{15.17}
\]

The spatial relation between angle and log-radius is time-independent exactly
when

\[
\boxed{
\omega=\frac{\beta}{\sigma}
\left(\mu-\frac12\sigma^2\right).
}
\tag{15.18}
\]

This is the same restriction as (15.16), with
\(\gamma=\beta/\sigma\). Under (15.18),

\[
\Theta_t-\Theta_0
=
\frac{\beta}{\sigma}\log\frac{R_t}{R_0},
\tag{15.19}
\]

which is a fixed logarithmic spiral.

When (15.18) fails, the process remains a native one-driver complex GBM with
an exact GBM modulus, but it is not confined to one fixed logarithmic spiral.
Equation (15.17) contains a time-dependent angular offset.

## 15.4 Rank-one covariance in log-polar coordinates

The martingale parts of log-radius and phase are

\[
dM_t^{(r)}=\sigma\,dW_t,
\qquad
dM_t^{(\theta)}=\beta\,dW_t.
\]

Their instantaneous covariance is

\[
\boxed{
\Sigma_{\log R,\Theta}
=
\begin{pmatrix}
\sigma^2&\sigma\beta\\
\sigma\beta&\beta^2
\end{pmatrix}
=
\begin{pmatrix}\sigma\\\beta\end{pmatrix}
\begin{pmatrix}\sigma&\beta\end{pmatrix}.
}
\tag{15.20}
\]

Therefore

\[
\det\Sigma_{\log R,\Theta}=0.
\tag{15.21}
\]

Its eigenvalues are

\[
\lambda_1=0,
\qquad
\lambda_2=\sigma^2+\beta^2.
\tag{15.22}
\]

The rank is:

- zero if \(\sigma=\beta=0\);
- one otherwise.

When \(\sigma\beta\ne0\), centered infinitesimal log-radius and phase
increments have correlation

\[
\operatorname{Corr}(dM^{(r)},dM^{(\theta)})
=
\operatorname{sign}(\sigma\beta).
\tag{15.23}
\]

## 15.5 Rank-one covariance in Cartesian coordinates

Although Cartesian coordinates are not used in the model definition, they can
be used to verify that complex notation has not hidden a second noise source.

Let

\[
\mathcal Z_t=X_t+iY_t.
\]

The diffusion coefficient in

\[
d\mathcal Z_t=A\mathcal Z_t\,dt+B\mathcal Z_t\,dW_t
\]

is the single complex number \(B\mathcal Z_t\). The corresponding real
diffusion vector is

\[
g(\mathcal Z_t)
=
\begin{pmatrix}
\operatorname{Re}(B\mathcal Z_t)\\
\operatorname{Im}(B\mathcal Z_t)
\end{pmatrix}.
\tag{15.24}
\]

Hence the Cartesian local covariance is

\[
\boxed{
\Sigma_{X,Y}(\mathcal Z_t)
=
g(\mathcal Z_t)g(\mathcal Z_t)^\mathsf T.
}
\tag{15.25}
\]

This outer product has rank at most one. It has rank exactly one whenever
\(B\ne0\), because \(\mathcal Z_t\ne0\).

Complex multiplication rotates and scales the one available noise direction;
it does not create a second independent direction.

## 15.6 Fixed-time support

At a fixed time \(t>0\),

\[
\mathcal Z_t
=
\mathcal Z_0e^{\kappa t}e^{\nu W_t}.
\tag{15.26}
\]

Since \(W_t\) is one real random variable, the fixed-time distribution is the
pushforward of a one-dimensional Gaussian under

\[
u\longmapsto \mathcal Z_0e^{\kappa t}e^{\nu u}.
\tag{15.27}
\]

For \(\sigma\beta\ne0\), this support is a logarithmic spiral. Special cases
are:

- a ray when \(\beta=0\);
- a circle when \(\sigma=0\);
- a point when \(\sigma=\beta=0\).

This fixed-time one-dimensional support is another expression of the
rank-one structure.

## 15.7 Two-driver independent radial and angular noise

To obtain independent radial and angular Brownian increments while preserving
the same GBM modulus, introduce independent real Brownian motions
\(W^{(r)}\) and \(W^{(\theta)}\):

\[
\boxed{
\mathcal Z_t^{(2)}
=
\mathcal Z_0
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)t
+\sigma W_t^{(r)}
+i\beta W_t^{(\theta)}
\right].
}
\tag{15.28}
\]

Then

\[
|\mathcal Z_t^{(2)}|
=
|\mathcal Z_0|
\exp\!\left[
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t^{(r)}
\right],
\tag{15.29}
\]

\[
\Theta_t^{(2)}
=
\Theta_0+\omega t+\beta W_t^{(\theta)}.
\tag{15.30}
\]

The log-polar covariance becomes

\[
\boxed{
\Sigma_{\log R,\Theta}^{(2)}
=
\begin{pmatrix}
\sigma^2&0\\
0&\beta^2
\end{pmatrix}.
}
\tag{15.31}
\]

It has rank two when \(\sigma\beta\ne0\).

Applying Itô's formula to (15.28) gives

\[
\boxed{
\frac{d\mathcal Z_t^{(2)}}{\mathcal Z_t^{(2)}}
=
\left(
\mu-\frac12\beta^2+i\omega
\right)dt
+\sigma\,dW_t^{(r)}
+i\beta\,dW_t^{(\theta)}.
}
\tag{15.32}
\]

There is no imaginary cross correction \(\sigma\beta\), because

\[
d[W^{(r)},W^{(\theta)}]_t=0.
\]

Equations (15.9) and (15.32) display exactly how shared versus independent
drivers change the Itô drift.

## 15.8 This two-driver comparator is not planar Brownian motion

The process (15.28) has independent radial and angular log-noise, but it is
still a multiplicative complex diffusion. It should not be called ordinary
planar Brownian motion.

Ordinary planar Brownian motion has additive dynamics

\[
dB_t^{\mathbb C}=dW_t^{(1)}+i\,dW_t^{(2)}
\]

and a Bessel radial process. By contrast, (15.28) has a GBM radius and
multiplicative dynamics.

The distinctions are:

| Model | Drivers | Noise form | Radius |
|---|---:|---|---|
| Phase 4 complex GBM | one real Brownian motion | multiplicative | GBM |
| Independent log-polar comparator | two real Brownian motions | multiplicative | GBM |
| Planar Brownian motion | two real Brownian motions | additive | Bessel |

## 15.9 Information recovery

### If \(\sigma\ne0\)

The Brownian state can be recovered from the modulus at time \(t\):

\[
\boxed{
W_t
=
\frac{
\log(|\mathcal Z_t|/|\mathcal Z_0|)
-
\left(\mu-\frac12\sigma^2\right)t
}{\sigma}.
}
\tag{15.33}
\]

Thus the modulus alone determines the current Brownian value.

### If \(\sigma=0\) and \(\beta\ne0\)

The endpoint \(\mathcal Z_t\) determines phase only modulo \(2\pi\), so it
does not determine \(W_t\) globally. The continuous sample path and its
unwrapped phase do recover

\[
W_t=\frac{\Theta_t-\Theta_0-\omega t}{\beta}.
\tag{15.34}
\]

### If \(\sigma=\beta=0\)

The model is deterministic and contains no Brownian information.

These cases distinguish pointwise injectivity from pathwise recovery.

## 15.10 What has been eliminated

Phase 4 eliminates the earlier pattern

\[
\text{external state process}
\ \longrightarrow\
\text{complex transformation}.
\]

The defining data are only:

\[
\mathcal Z_0,\quad
\mu,\sigma,\omega,\beta,\quad
W_t.
\]

The native definition is

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)t
+(\sigma+i\beta)W_t
\right].
\]

Real and imaginary coordinates, radius, phase, and any comparison with real
GBM are derived from this equation afterward.

## 15.11 Limits of the construction

The model does not:

- turn one Brownian driver into two independent noise sources;
- give rank-two local covariance;
- make \(dt\) and \(dW_t\) algebraically interchangeable;
- identify \(d[W,W]_t=dt\) with \(i^2=-1\);
- become planar Brownian motion merely because it is complex-valued; or
- remove the need for an initial complex scale and phase.

What it does provide is one exact, non-circular complex exponential that
combines GBM scaling and rotation while retaining the original one-driver
stochastic dimension.
