# The Stochastic Exponential: The Algebraic Bridge

## 1. Why ordinary exponentiation changes

For ordinary differentiable \(x_t\),

\[
d(e^{x_t})=e^{x_t}dx_t.
\]

If \(Y_t\) has Brownian variation, the second derivative of the exponential
survives:

\[
d(e^{Y_t})=e^{Y_t}\left(dY_t+\frac12d[Y]_t\right).
\]

Locally, for \(dY=a\,dt+b\,dW\),

\[
\begin{aligned}
e^{dY}
&=1+dY+\frac12(dY)^2+\cdots\\
&=1+b\,dW+\left(a+\frac12b^2\right)dt.
\end{aligned}
\]

The \(b^2/2\) term is the algebraic bridge from the Itô multiplication rule
to exponential calculus.

## 2. Geometric Brownian motion

Let

\[
dS_t=\mu S_t\,dt+\sigma S_t\,dW_t,\qquad S_0>0.
\]

Apply Itô's lemma to \(f(s)=\log s\):

\[
f'(s)=\frac1s,\qquad f''(s)=-\frac1{s^2}.
\]

Therefore

\[
\begin{aligned}
d\log S_t
&=\frac{1}{S_t}dS_t
 -\frac{1}{2S_t^2}(dS_t)^2\\
&=\left(\mu-\frac{\sigma^2}{2}\right)dt+\sigma dW_t.
\end{aligned}
\]

Integration and exponentiation give

\[
\boxed{
S_t=S_0\exp\!\left[
\left(\mu-\frac{\sigma^2}{2}\right)t+\sigma W_t
\right].}
\]

The correction \(-\sigma^2/2\) ensures that applying Itô's lemma back to the
exponential produces drift \(\mu\), not \(\mu+\sigma^2/2\).

The moments are

\[
\mathbb E[S_t]=S_0e^{\mu t},
\]

\[
\mathbb E[S_t^2]
=S_0^2e^{(2\mu+\sigma^2)t},
\]

and

\[
\operatorname{Var}(S_t)
=S_0^2e^{2\mu t}\left(e^{\sigma^2t}-1\right).
\]

## 3. Continuous stochastic exponentials

Let \(M\) be a continuous local martingale with \(M_0=0\). Its
Doléans–Dade stochastic exponential is

\[
\boxed{
\mathcal E(M)_t
=\exp\!\left(M_t-\frac12[M]_t\right).}
\]

It is the unique solution of

\[
Z_t=1+\int_0^t Z_s\,dM_s,
\qquad\text{equivalently}\qquad
dZ_t=Z_t\,dM_t.
\]

To check this, set \(Y=M-\tfrac12[M]\). Then
\([Y]=[M]\), so

\[
d(e^Y)=e^Y\left(dM-\frac12d[M]+\frac12d[M]\right)
=e^YdM.
\]

For a continuous semimartingale \(X=X_0+A+M\), with \(A\) continuous finite
variation and \(M\) a continuous local martingale, the solution of

\[
dZ_t=Z_t\,dX_t,\qquad Z_0=1,
\]

is

\[
\mathcal E(X)_t
=\exp\!\left(X_t-X_0-\frac12[M]_t\right).
\]

Finite-variation terms contribute no quadratic variation. For discontinuous
semimartingales there is an additional jump product; the displayed formula
is intentionally restricted to the continuous case.

The stochastic exponential \(\mathcal E(M)\) is a strictly positive local
martingale when \(M\) is real and continuous. Extra integrability conditions are required
for it to be a true martingale. Those conditions are not needed for the
pathwise formula used here.

## 4. Complex coefficient

The same calculation works by treating a complex process as a pair of real
processes. For constants \(c,\gamma\in\mathbb C\),

\[
dZ_t=cZ_t\,dt+\gamma Z_t\,dW_t
\]

has solution

\[
\boxed{
Z_t=Z_0
\exp\!\left[\left(c-\frac{\gamma^2}{2}\right)t+\gamma W_t\right].}
\]

The correction uses \(\gamma^2\), not \(|\gamma|^2\), because it comes from
the complex second derivative of \(e^z\) along the real Brownian driver.

Two cases reveal the geometry:

- real \(\gamma=\sigma\): \(\gamma^2=\sigma^2\), giving random log-amplitude;
- imaginary \(\gamma=i\beta\):
  \(\gamma^2=-\beta^2\), so

  \[
  Z_t=Z_0e^{(c+\beta^2/2)t+i\beta W_t}.
  \]

If we want *pure phase noise with constant modulus*, the Itô SDE coefficient
must instead use

\[
c=-\frac{\beta^2}{2}+i\omega.
\]

Then

\[
c-\frac{(i\beta)^2}{2}=i\omega
\]

and the solution becomes \(Z_t=Z_0e^{i(\omega t+\beta W_t)}\). This is the
entry point to stochastic rotation.

## 5. What is analogous to \(re^{i\theta}\)?

The additive SDE \(dX=\mu dt+\sigma dW\) has an additive solution. Its
exponential is not forced by the equation.

The multiplicative SDE \(dZ=Z\,dX\) has the stochastic exponential solution
\(\mathcal E(X)\). Thus:

\[
\boxed{\text{ordinary exponential coordinates}
\quad\longleftrightarrow\quad
\text{Doléans--Dade stochastic exponential}.}
\]

This is the algebraic analogue. A literal polar analogue needs a complex
state and is developed next.
