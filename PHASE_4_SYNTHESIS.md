# Phase 4 Synthesis: Native Complex Euler Form for GBM

## 1. Final answer

Yes. Geometric Brownian motion can be represented natively by one complex
Euler-form exponential without first defining an \(x\)-\(y\) process or
mapping an external state variable into the complex plane.

Let

\[
\mu,\sigma,\omega,\beta\in\mathbb R,
\qquad
\mathcal Z_0\in\mathbb C\setminus\{0\},
\]

and let \(W_t\) be one real Brownian motion. Define

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
}
\tag{S4.1}
\]

This is the central Phase 4 equation. It contains:

- no defining Cartesian processes;
- no pre-existing \(Z_i-Z_0\) path;
- one initial complex scale and phase;
- one Brownian primitive;
- one complex exponent combining time and Brownian noise.

## 2. GBM is the modulus

Taking the modulus of (S4.1) gives

\[
\boxed{
R_t:=|\mathcal Z_t|
=
|\mathcal Z_0|
\exp\!\left[
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right].
}
\tag{S4.2}
\]

Therefore

\[
\boxed{
\frac{dR_t}{R_t}
=
\mu\,dt+\sigma\,dW_t.
}
\tag{S4.3}
\]

The modulus is exactly geometric Brownian motion, not merely a process with
similar qualitative behavior.

## 3. Rotation is the phase

Choose a continuous initial phase \(\Theta_0\) for \(\mathcal Z_0\). The
unwrapped phase is

\[
\boxed{
\Theta_t
=
\Theta_0+\omega t+\beta W_t.
}
\tag{S4.4}
\]

Thus:

- \(\omega\) supplies deterministic rotation;
- \(\beta\) supplies stochastic rotation;
- \(\sigma\) supplies radial Brownian noise; and
- the same \(W_t\) drives both random effects.

The principal argument is (S4.4) modulo \(2\pi\). Its branch jumps are not
jumps of the underlying complex path.

## 4. One complex log-increment

Define the native complex log-driver

\[
\boxed{
d\Xi_t
=
\left[
\left(\mu-\frac12\sigma^2\right)+i\omega
\right]dt
+(\sigma+i\beta)dW_t.
}
\tag{S4.5}
\]

Then

\[
\boxed{\mathcal Z_t=\mathcal Z_0e^{\Xi_t}.}
\tag{S4.6}
\]

Equivalently,

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left\{
\int_0^t
\left[
\left(\mu-\frac12\sigma^2\right)+i\omega
\right]ds
+
\int_0^t(\sigma+i\beta)\,dW_s
\right\}.
\tag{S4.7}
\]

This is the rigorous sense in which \(dt\) and \(dW_t\) are combined into one
complex stochastic object. They are not turned into ordinary algebraic
numbers.

## 5. The exact complex Itô SDE

Set

\[
\kappa
=
\left(\mu-\frac12\sigma^2\right)+i\omega,
\qquad
B=\sigma+i\beta.
\]

Itô's formula gives

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(\kappa+\frac12B^2\right)dt+B\,dW_t.
\]

Since

\[
B^2=\sigma^2-\beta^2+2i\sigma\beta,
\]

the SDE is

\[
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left[
\mu-\frac12\beta^2+i(\omega+\sigma\beta)
\right]dt
+(\sigma+i\beta)dW_t.
}
\tag{S4.8}
\]

Two corrections are essential:

- \(-\tfrac12\beta^2\) in the real SDE drift; and
- \(+\sigma\beta\) in the imaginary SDE drift.

The second appears because radial and angular noise use the same Brownian
driver.

## 6. Stochastic-exponential form

Define

\[
A
=
\mu-\frac12\beta^2+i(\omega+\sigma\beta),
\qquad
Y_t=At+BW_t.
\]

The Doléans stochastic exponential satisfies

\[
\mathcal E(Y)_t
=
\exp\!\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\]

Because

\[
A-\frac12B^2=\kappa,
\]

the model also has the canonical multiplicative form

\[
\boxed{
\mathcal Z_t=\mathcal Z_0\mathcal E(Y)_t.
}
\tag{S4.9}
\]

The ordinary continuous log lift and stochastic logarithm are

\[
\operatorname{Log}_{\mathrm c}
\left(\frac{\mathcal Z_t}{\mathcal Z_0}\right)
=
\kappa t+BW_t,
\]

\[
\mathcal L
\left(\frac{\mathcal Z}{\mathcal Z_0}\right)_t
=
\int_0^t\frac{d\mathcal Z_s}{\mathcal Z_s}
=
At+BW_t.
\]

They differ by \(\tfrac12B^2t\).

## 7. Exact random-walk formula

For a step of length \(h\), let

\[
\Delta W_n=\sqrt h\,\xi_n,
\qquad
\xi_n\overset{\mathrm{iid}}{\sim}N(0,1).
\]

Then

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
\tag{S4.10}
\]

This is exact at grid points. It is not Euler--Maruyama.

The same Gaussian variable determines

\[
\log\frac{R_{n+1}}{R_n}
=
\left(\mu-\frac12\sigma^2\right)h
+\sigma\sqrt h\,\xi_n,
\]

\[
\Theta_{n+1}-\Theta_n
=
\omega h+\beta\sqrt h\,\xi_n.
\]

## 8. Why Phase 3 was a special case

Phase 3 applied a complex coefficient \(c=1+i\gamma\) to the real GBM
log-return

\[
L_t
=
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t.
\]

It produced

\[
\mathcal Z_t=\mathcal Z_0e^{(1+i\gamma)L_t}.
\]

This equals (S4.1) only when

\[
\boxed{
\beta=\gamma\sigma,
\qquad
\omega=\gamma\left(\mu-\frac12\sigma^2\right).
}
\tag{S4.11}
\]

Under these restrictions,

\[
\Theta_t-\Theta_0
=
\gamma\log\frac{R_t}{R_0},
\]

so the path lies on one fixed logarithmic spiral.

Phase 4 frees \(\omega\) and \(\beta\) from those restrictions while preserving
the exact GBM modulus. In general,

\[
\Theta_t-\Theta_0
=
\frac{\beta}{\sigma}\log\frac{R_t}{R_0}
+
\left[
\omega
-
\frac{\beta}{\sigma}
\left(\mu-\frac12\sigma^2\right)
\right]t,
\]

for \(\sigma\ne0\). The final term is the additional rotational freedom.

## 9. The unavoidable one-driver limitation

The log-radius and phase noise vector is

\[
\begin{pmatrix}\sigma\\\beta\end{pmatrix}dW_t.
\]

Its local covariance is

\[
\boxed{
\begin{pmatrix}
\sigma^2&\sigma\beta\\
\sigma\beta&\beta^2
\end{pmatrix}dt.
}
\tag{S4.12}
\]

This matrix is an outer product and has determinant zero. Except in the
deterministic case, its rank is one.

Complex multiplication provides scaling and rotation, but it cannot turn one
real Brownian driver into two independent stochastic directions.

If independent radial and angular noise is required, a different model is

\[
\mathcal Z_t^{(2)}
=
\mathcal Z_0
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)t
+\sigma W_t^{(r)}
+i\beta W_t^{(\theta)}
\right],
\]

with independent Brownian motions. This has rank-two log-polar noise when
\(\sigma\beta\ne0\), but it is not an equivalent one-driver representation
and is not ordinary planar Brownian motion.

## 10. Constant-modulus rotation

With \(\mu=\sigma=0\),

\[
\mathcal Z_t
=
\mathcal Z_0e^{i(\omega t+\beta W_t)}
\]

has constant modulus. Its SDE is

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(-\frac12\beta^2+i\omega\right)dt
+i\beta\,dW_t.
\]

If the drift \(-\tfrac12\beta^2\) is omitted, the modulus becomes

\[
|\mathcal Z_0|e^{\beta^2t/2}.
\]

The notebook reproduced both behaviors to floating-point precision.

## 11. Complex quadratic variations

The bilinear and Hermitian brackets are

\[
\boxed{
d[\mathcal Z,\mathcal Z]_t
=
(\sigma+i\beta)^2\mathcal Z_t^2\,dt,
}
\tag{S4.13}
\]

\[
\boxed{
d[\mathcal Z,\overline{\mathcal Z}]_t
=
(\sigma^2+\beta^2)|\mathcal Z_t|^2\,dt.
}
\tag{S4.14}
\]

The first uses a complex square. The second uses an absolute square. They
cannot be interchanged.

## 12. Computational evidence

The cleanly executed Phase 4 notebook reported:

- modulus identity error: \(8.882\times10^{-16}\);
- unwrapped-phase error: \(4.441\times10^{-16}\);
- exact-step error: \(8.750\times10^{-15}\);
- constant-modulus error: \(4.441\times10^{-16}\);
- one-driver minimum covariance eigenvalue:
  \(-1.249\times10^{-16}\), numerically zero;
- two-driver minimum covariance eigenvalue: \(0.0898770\);
- Phase 3 equivalence error: \(6.661\times10^{-16}\);
- Euler--Maruyama fitted strong slope: \(0.5469\);
- bilinear quadratic-variation relative error: \(0.6998\%\); and
- Hermitian quadratic-variation relative error: \(0.3648\%\).

All Monte Carlo moment residuals were within two estimated standard errors of
their exact values.

## 13. Relationship to existing research

The literature already contains:

- exact exponential solutions of scalar linear SDEs;
- complex coefficients in the scalar linear SDE;
- the term **complex geometric Brownian motion** for that process;
- stochastic exponentials and logarithms; and
- unified calculus for complex-valued semimartingales.

Phase 4 does not claim to invent complex GBM. Its contribution to this
research project is the explicit modulus-preserving parameterization,
geometric interpretation, Phase 3 equivalence map, and rank analysis.

The source audit is recorded in `PHASE_4_LITERATURE_REVIEW.md`.

## 14. What the \(dW^2=dt\) analogy does not mean

\[
d[W,W]_t=dt
\]

is a quadratic-variation statement. It does not mean that each finite
increment satisfies

\[
(\Delta W)^2=\Delta t.
\]

Likewise,

\[
i^2=-1
\]

is an exact algebraic identity. The two facts belong to different
mathematical structures.

The useful bridge is narrower: both make second-order terms consequential,
and the complex Itô correction \(B^2/2\) directly changes radial and angular
drift.

## 15. Final equation

The requested coordinate-free, rotational geometric Brownian motion is

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
}
\]

It is one native complex process whose modulus is GBM, whose phase rotates,
and whose drift and diffusion appear together inside one exact exponential.
