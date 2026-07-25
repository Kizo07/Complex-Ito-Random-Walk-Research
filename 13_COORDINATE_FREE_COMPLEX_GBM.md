# 13. Coordinate-Free Complex Geometric Brownian Motion

## 13.1 Objective and assumptions

Let \((\Omega,\mathcal F,(\mathcal F_t)_{t\ge0},\mathbb P)\) support one
standard real Brownian motion \(W\). Fix

\[
\mu,\omega,\sigma,\beta\in\mathbb R,
\qquad
\mathcal Z_0\in\mathbb C\setminus\{0\}.
\]

All coefficients are constant. The units are

\[
[\mu]=[\omega]=T^{-1},
\qquad
[\sigma]=[\beta]=T^{-1/2},
\qquad
[W_t]=T^{1/2}.
\]

Define

\[
a=\mu-\frac12\sigma^2,
\qquad
\kappa=a+i\omega,
\qquad
\nu=\sigma+i\beta.
\tag{13.1}
\]

The Phase 4 process is defined directly by

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(\kappa t+\nu W_t\right).
}
\tag{13.2}
\]

No real and imaginary coordinate processes are used to define
\(\mathcal Z\). They can be recovered later for visualization, but they are
not stochastic primitives of the model.

## 13.2 The radial and angular theorem

Choose an initial phase \(\Theta_0\) such that

\[
\mathcal Z_0=R_0e^{i\Theta_0},
\qquad R_0=|\mathcal Z_0|>0.
\]

Since

\[
\operatorname{Re}(\kappa t+\nu W_t)=at+\sigma W_t
\]

and

\[
\operatorname{Im}(\kappa t+\nu W_t)=\omega t+\beta W_t,
\]

(13.2) gives the pathwise factorization

\[
\boxed{
R_t:=|\mathcal Z_t|
=
R_0\exp\!\left[
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right],
}
\tag{13.3}
\]

\[
\boxed{
\Theta_t
=
\Theta_0+\omega t+\beta W_t,
}
\tag{13.4}
\]

\[
\boxed{\mathcal Z_t=R_te^{i\Theta_t}.}
\tag{13.5}
\]

Equation (13.4) is a continuous, unwrapped phase. The principal argument
\(\operatorname{Arg}\mathcal Z_t\in(-\pi,\pi]\) is (13.4) reduced modulo
\(2\pi\) and may have artificial branch jumps.

### Theorem 13.1

The modulus \(R_t=|\mathcal Z_t|\) is exactly a geometric Brownian motion:

\[
\boxed{
dR_t=\mu R_t\,dt+\sigma R_t\,dW_t,
\qquad R_0=|\mathcal Z_0|.
}
\tag{13.6}
\]

The unwrapped phase satisfies

\[
\boxed{
d\Theta_t=\omega\,dt+\beta\,dW_t.
}
\tag{13.7}
\]

### Proof

Apply the real Itô formula to

\[
R_t=R_0e^{at+\sigma W_t}.
\]

Then

\[
\frac{dR_t}{R_t}
=
a\,dt+\sigma\,dW_t+\frac12\sigma^2dt
=
\mu\,dt+\sigma\,dW_t.
\]

Equation (13.7) follows directly from (13.4). These identities are exact
Itô SDEs, not finite-increment algebra. \(\square\)

## 13.3 Direct complex SDE

For the entire function \(f(z)=e^z\), Itô's formula gives

\[
d(e^{\Xi_t})
=
e^{\Xi_t}
\left(d\Xi_t+\frac12d[\Xi,\Xi]_t\right),
\]

where

\[
d\Xi_t=\kappa\,dt+\nu\,dW_t
\]

and the complex bilinear quadratic variation is

\[
d[\Xi,\Xi]_t=\nu^2dt.
\]

Therefore

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(\kappa+\frac12\nu^2\right)dt+\nu\,dW_t.
\tag{13.8}
\]

Now

\[
\nu^2
=
(\sigma+i\beta)^2
=
\sigma^2-\beta^2+2i\sigma\beta.
\]

Using \(\kappa=\mu-\tfrac12\sigma^2+i\omega\),

\[
\kappa+\frac12\nu^2
=
\mu-\frac12\beta^2+i(\omega+\sigma\beta).
\]

Hence the native complex Itô SDE is

\[
\boxed{
d\mathcal Z_t
=
A\mathcal Z_t\,dt+B\mathcal Z_t\,dW_t,
}
\tag{13.9}
\]

where

\[
\boxed{
A=\mu-\frac12\beta^2+i(\omega+\sigma\beta),
\qquad
B=\sigma+i\beta.
}
\tag{13.10}
\]

The diffusion coefficient \(B\) controls both radial and angular Brownian
motion. The imaginary drift term \(\sigma\beta\) is the shared-driver cross
correction.

## 13.4 Reverse derivation and uniqueness of the coefficients

Consider the general constant-coefficient one-driver complex SDE

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}=A\,dt+B\,dW_t,
\qquad A,B\in\mathbb C.
\tag{13.11}
\]

Its exact solution is

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\tag{13.12}
\]

Suppose its desired log-radius and phase are

\[
\log\frac{R_t}{R_0}
=
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t,
\tag{13.13}
\]

\[
\Theta_t-\Theta_0=\omega t+\beta W_t.
\tag{13.14}
\]

Matching the Brownian coefficients in (13.12) first forces

\[
B=\sigma+i\beta.
\]

Matching the drift coefficients then forces

\[
A-\frac12B^2
=
\left(\mu-\frac12\sigma^2\right)+i\omega,
\]

and therefore

\[
A=\mu-\frac12\beta^2+i(\omega+\sigma\beta).
\]

Thus (13.10) is the unique constant-coefficient choice realizing
(13.13)–(13.14) with the same real Brownian driver.

## 13.5 Exact transition and discrete random walk

For \(0\le s<t\), let \(h=t-s\) and

\[
\Delta W_{s,t}=W_t-W_s\sim N(0,h),
\]

independently of \(\mathcal F_s\). Dividing (13.2) at times \(t\) and \(s\)
gives

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_s
\exp\!\left(\kappa h+\nu\Delta W_{s,t}\right).
}
\tag{13.15}
\]

On a uniform grid, write

\[
\Delta W_n=\sqrt h\,\xi_n,
\qquad
\xi_n\overset{\mathrm{iid}}{\sim}N(0,1).
\]

The exact multiplicative random walk is

\[
\boxed{
\mathcal Z_{n+1}
=
\mathcal Z_n
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)h
+(\sigma+i\beta)\sqrt h\,\xi_n
\right].
}
\tag{13.16}
\]

This is an exact transition, not an Euler--Maruyama approximation.

Its log-polar increments are

\[
\log\frac{R_{n+1}}{R_n}
=
\left(\mu-\frac12\sigma^2\right)h+\sigma\sqrt h\,\xi_n,
\tag{13.17}
\]

\[
\Theta_{n+1}-\Theta_n
=
\omega h+\beta\sqrt h\,\xi_n.
\tag{13.18}
\]

Equations (13.17) and (13.18) use the same Gaussian increment. This is the
source of their rank-one covariance.

## 13.6 Distribution at a fixed time

The vector

\[
\begin{pmatrix}
\log(R_t/R_0)\\
\Theta_t-\Theta_0
\end{pmatrix}
\]

is Gaussian, possibly degenerate, with mean

\[
\begin{pmatrix}
\left(\mu-\tfrac12\sigma^2\right)t\\
\omega t
\end{pmatrix}
\]

and covariance

\[
t
\begin{pmatrix}
\sigma^2&\sigma\beta\\
\sigma\beta&\beta^2
\end{pmatrix}.
\tag{13.19}
\]

Consequently:

- \(R_t\) is lognormal;
- the unwrapped phase is normal;
- the principal phase is wrapped normal; and
- the joint log-polar law is supported on an affine line at each fixed
  \(t>0\) whenever \((\sigma,\beta)\ne(0,0)\).

The last statement concerns fixed-time support in log-polar coordinates. It
does not say that an entire sample path lies on one fixed spatial curve for
arbitrary \(\omega\) and \(\beta\).

## 13.7 Exact moments

For every real \(p\) for which the expression is requested,

\[
\boxed{
\mathbb E[R_t^p]
=
R_0^p
\exp\!\left[
p\mu t+\frac12p(p-1)\sigma^2t
\right].
}
\tag{13.20}
\]

All real moments exist because \(R_t\) is lognormal.

For an integer \(n\),

\[
\mathcal Z_t^n
=
\mathcal Z_0^n
\exp\!\left(n\kappa t+n\nu W_t\right),
\]

so the Gaussian moment-generating formula gives

\[
\boxed{
\mathbb E[\mathcal Z_t^n]
=
\mathcal Z_0^n
\exp\!\left[
n\kappa t+\frac12n^2\nu^2t
\right].
}
\tag{13.21}
\]

Equivalently, using \(A=\kappa+\tfrac12\nu^2\) and \(B=\nu\),

\[
\boxed{
\mathbb E[\mathcal Z_t^n]
=
\mathcal Z_0^n
\exp\!\left[
nA t+\frac12n(n-1)B^2t
\right].
}
\tag{13.22}
\]

In particular,

\[
\mathbb E[\mathcal Z_t]=\mathcal Z_0e^{At}.
\tag{13.23}
\]

For real \(p,q\), the mixed log-polar transform is

\[
\boxed{
\mathbb E\!\left[
R_t^p e^{iq(\Theta_t-\Theta_0)}
\right]
=
R_0^p
\exp\!\left\{
\left[
p\left(\mu-\frac12\sigma^2\right)
+iq\omega
+\frac12(p\sigma+iq\beta)^2
\right]t
\right\}.
}
\tag{13.24}
\]

This one identity contains the radial moments, circular phase moments, and
their dependence.

## 13.8 Nonvanishing and pathwise phase

For every finite \(t\),

\[
\mathcal Z_t=\mathcal Z_0e^{\kappa t+\nu W_t}\ne0
\]

whenever \(\mathcal Z_0\ne0\). Thus:

- \(R_t>0\) pathwise;
- no stopping at the origin is needed;
- a continuous phase lift is available explicitly from (13.4); and
- the model avoids the zero-crossing singularities of literal polar
  coordinates for a real arithmetic diffusion.

## 13.9 Parameter regimes

### No rotation

\[
\omega=\beta=0
\quad\Longrightarrow\quad
\mathcal Z_t=e^{i\Theta_0}R_t.
\]

The path remains on a fixed ray.

### Deterministic rotation

\[
\beta=0,\quad\omega\ne0
\]

gives a GBM radius and phase \(\Theta_0+\omega t\).

### Stochastic rotation

\[
\omega=0,\quad\beta\ne0
\]

gives phase \(\Theta_0+\beta W_t\), driven by the same Brownian motion as the
radius when \(\sigma\ne0\).

### Constant modulus

\[
\mu=\sigma=0
\]

gives

\[
\mathcal Z_t
=
\mathcal Z_0e^{i(\omega t+\beta W_t)},
\qquad
|\mathcal Z_t|=|\mathcal Z_0|.
\tag{13.25}
\]

The corresponding SDE is

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(-\frac12\beta^2+i\omega\right)dt+i\beta\,dW_t.
\tag{13.26}
\]

The real drift \(-\tfrac12\beta^2\) is required to preserve the modulus.

## 13.10 Main conclusion

Equation (13.2) is a native complex exponential representation of geometric
Brownian motion:

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
\]

Its modulus is exactly GBM, its phase rotates, its exact random-walk
transition contains drift and Brownian noise in one complex exponent, and its
defining equation contains no Cartesian state process.
