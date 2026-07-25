# 14. The Complex Log-Driver and Stochastic Exponential

## 14.1 Three related but different objects

For Phase 4 define

\[
\kappa
=
\left(\mu-\frac12\sigma^2\right)+i\omega,
\qquad
\nu=\sigma+i\beta,
\]

and

\[
\Xi_t=\kappa t+\nu W_t.
\tag{14.1}
\]

There are three related objects that must not be conflated:

1. the **complex log-driver** \(\Xi_t\);
2. the ordinary complex exponential
   \(\mathcal Z_t=\mathcal Z_0e^{\Xi_t}\); and
3. the Doléans **stochastic exponential** of the stochastic logarithm of
   \(\mathcal Z\).

The distinction is exactly where the Itô correction lives.

## 14.2 One semimartingale increment combines drift and noise

The differential

\[
\boxed{
d\Xi_t
=
\left[
\left(\mu-\frac12\sigma^2\right)+i\omega
\right]dt
+(\sigma+i\beta)dW_t
}
\tag{14.2}
\]

packages the deterministic and Brownian contributions into one complex
semimartingale.

Integrated from \(0\) to \(t\),

\[
\Xi_t
=
\int_0^t
\left[
\left(\mu-\frac12\sigma^2\right)+i\omega
\right]ds
+
\int_0^t(\sigma+i\beta)\,dW_s.
\tag{14.3}
\]

The model can therefore be written as the single exponential

\[
\boxed{
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
}
\tag{14.4}
\]

This is the rigorous interpretation of a “single term combining \(dt\) and
\(dW_t\).” The integrators remain mathematically different.

## 14.3 Ordinary exponential and Itô correction

For

\[
\mathcal Z_t=\mathcal Z_0e^{\Xi_t},
\]

Itô's formula gives

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
d\Xi_t+\frac12d[\Xi,\Xi]_t.
\tag{14.5}
\]

Since only the local-martingale part contributes to quadratic variation,

\[
d[\Xi,\Xi]_t=\nu^2dt.
\tag{14.6}
\]

Therefore

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(\kappa+\frac12\nu^2\right)dt+\nu\,dW_t.
\tag{14.7}
\]

Define

\[
A=\kappa+\frac12\nu^2,
\qquad B=\nu.
\tag{14.8}
\]

Then

\[
A
=
\mu-\frac12\beta^2+i(\omega+\sigma\beta),
\qquad
B=\sigma+i\beta,
\tag{14.9}
\]

and

\[
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}=A\,dt+B\,dW_t.
}
\tag{14.10}
\]

The ordinary exponential uses the drift \(\kappa\) in its exponent, whereas
the multiplicative Itô SDE uses the drift \(A\). They differ by
\(\tfrac12B^2\).

## 14.4 Doléans stochastic exponential

Let

\[
Y_t=A t+B W_t.
\tag{14.11}
\]

For a continuous complex semimartingale, the Doléans stochastic exponential
is

\[
\mathcal E(Y)_t
=
\exp\!\left(
Y_t-Y_0-\frac12[Y,Y]_t
\right).
\tag{14.12}
\]

Here \(Y_0=0\) and

\[
[Y,Y]_t=B^2t.
\]

Consequently,

\[
\mathcal E(Y)_t
=
\exp\!\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\tag{14.13}
\]

Because

\[
A-\frac12B^2=\kappa,
\]

we obtain

\[
\boxed{
\mathcal Z_t=\mathcal Z_0\mathcal E(Y)_t.
}
\tag{14.14}
\]

Thus the ordinary exponential of the compensated log-driver and the
stochastic exponential of the SDE driver are the same process:

\[
\boxed{
e^{\kappa t+BW_t}
=
\mathcal E(At+BW)_t.
}
\tag{14.15}
\]

## 14.5 Ordinary log lift versus stochastic logarithm

Because \(\mathcal Z_t\ne0\), choose the continuous ordinary logarithm along
the path, normalized at time zero:

\[
\operatorname{Log}_{\mathrm c}
\left(\frac{\mathcal Z_t}{\mathcal Z_0}\right)
=
\kappa t+BW_t.
\tag{14.16}
\]

The stochastic logarithm is instead

\[
\mathcal L\left(\frac{\mathcal Z}{\mathcal Z_0}\right)_t
:=
\int_0^t\frac{d\mathcal Z_s}{\mathcal Z_s}
=
A t+BW_t.
\tag{14.17}
\]

Their difference is

\[
\boxed{
\mathcal L\left(\frac{\mathcal Z}{\mathcal Z_0}\right)_t
-
\operatorname{Log}_{\mathrm c}
\left(\frac{\mathcal Z_t}{\mathcal Z_0}\right)
=
\frac12B^2t.
}
\tag{14.18}
\]

This is the stochastic analogue of the distinction between an ordinary
logarithm and the inverse of a stochastic exponential.

## 14.6 Complex bilinear and Hermitian brackets

The martingale part of \(\mathcal Z\) is

\[
dM_t=B\mathcal Z_t\,dW_t.
\]

The complex bilinear self-bracket is

\[
\boxed{
d[\mathcal Z,\mathcal Z]_t
=
B^2\mathcal Z_t^2\,dt
=
(\sigma+i\beta)^2\mathcal Z_t^2\,dt.
}
\tag{14.19}
\]

The bracket with the complex conjugate is

\[
\boxed{
d[\mathcal Z,\overline{\mathcal Z}]_t
=
|B|^2|\mathcal Z_t|^2\,dt
=
(\sigma^2+\beta^2)|\mathcal Z_t|^2\,dt.
}
\tag{14.20}
\]

These are different objects:

- \([\mathcal Z,\mathcal Z]\) is complex bilinear and can be complex;
- \([\mathcal Z,\overline{\mathcal Z}]\) is real and nonnegative.

Replacing \(B^2\) by \(|B|^2\) in the Itô correction would therefore be
incorrect.

For the log-driver,

\[
\boxed{
[\Xi,\Xi]_t
=
(\sigma+i\beta)^2t,
}
\tag{14.21}
\]

\[
\boxed{
[\Xi,\overline\Xi]_t
=
(\sigma^2+\beta^2)t.
}
\tag{14.22}
\]

## 14.7 The constant-modulus stress test

Set

\[
\mu=0,\qquad\sigma=0.
\]

Then

\[
\mathcal Z_t
=
\mathcal Z_0e^{i(\omega t+\beta W_t)}
\tag{14.23}
\]

has exactly constant modulus. Applying Itô's formula,

\[
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(-\frac12\beta^2+i\omega\right)dt
+i\beta\,dW_t.
}
\tag{14.24}
\]

The real drift \(-\tfrac12\beta^2\) is indispensable.

To see what fails without it, consider the incorrect SDE

\[
\frac{d\widetilde{\mathcal Z}_t}
{\widetilde{\mathcal Z}_t}
=
i\beta\,dW_t.
\tag{14.25}
\]

Its exact solution is

\[
\widetilde{\mathcal Z}_t
=
\mathcal Z_0
\exp\!\left(
\frac12\beta^2t+i\beta W_t
\right),
\tag{14.26}
\]

because \((i\beta)^2=-\beta^2\). Hence

\[
\left|\widetilde{\mathcal Z}_t\right|
=
|\mathcal Z_0|e^{\beta^2t/2},
\tag{14.27}
\]

which grows deterministically rather than remaining constant.

This stress test isolates the precise role of the complex Itô correction.

## 14.8 Euler form versus Euler--Maruyama

The phrase **Euler form** in this project refers to the complex exponential

\[
e^{x+iy}=e^x(\cos y+i\sin y).
\]

The Euler--Maruyama method is a numerical approximation. Applied to

\[
d\mathcal Z_t=A\mathcal Z_t\,dt+B\mathcal Z_t\,dW_t,
\]

it gives

\[
\mathcal Z_{n+1}^{\mathrm{EM}}
=
\mathcal Z_n^{\mathrm{EM}}
\left(1+Ah+B\Delta W_n\right).
\tag{14.28}
\]

The exact update is instead

\[
\mathcal Z_{n+1}
=
\mathcal Z_n
\exp\!\left[
\left(A-\frac12B^2\right)h+B\Delta W_n
\right].
\tag{14.29}
\]

The exact exponential step preserves all analytic identities at grid points.
Euler--Maruyama converges as \(h\to0\), but it does not preserve them exactly
at finite step size.

## 14.9 Why \(dt\) and \(dW_t\) are not ordinary algebra

The Itô multiplication table

\[
(dW_t)^2=dt,\qquad dt\,dW_t=0,\qquad(dt)^2=0
\]

is shorthand for quadratic-variation limits. It does not state that an
individual finite Brownian increment obeys

\[
(\Delta W)^2=\Delta t.
\]

In fact, if \(\Delta W\sim N(0,\Delta t)\), then

\[
\frac{(\Delta W)^2}{\Delta t}\sim\chi_1^2,
\]

which is random. The convergence occurs after summing squared increments over
increasingly fine partitions.

Likewise,

\[
i^2=-1
\]

is an exact algebraic identity in \(\mathbb C\), not a limiting stochastic
rule. The analogy is useful only as a mnemonic that second-order terms matter.

## 14.10 Main conclusion

The requested single exponential can be written in either of two rigorously
equivalent ways:

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left(\kappa t+BW_t\right)
}
\]

or

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0\mathcal E(At+BW)_t,
\qquad
A=\kappa+\frac12B^2.
}
\]

The first emphasizes Euler's complex exponential; the second emphasizes the
canonical multiplicative object of stochastic calculus.
