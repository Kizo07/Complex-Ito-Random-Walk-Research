# Final Synthesis: Complex Exponentials, Itô Calculus, and Random Walks

## The central answer

Start with the arithmetic diffusion

\[
dX_t=\mu\,dt+\sigma\,dW_t,
\qquad
X_t=X_0+\mu t+\sigma W_t.
\]

The process \(X_t\) itself is real and additive, so it has no nontrivial
polar form. But it can be used as a stochastic angle. Define

\[
Z_t=r_0e^{iX_t}.
\]

Then

\[
\boxed{
Z_t=r_0
\exp\!\left(i[X_0+\mu t+\sigma W_t]\right)}
\]

and Itô's lemma gives

\[
\boxed{
dZ_t
=\left(i\mu-\frac{\sigma^2}{2}\right)Z_tdt
+i\sigma Z_tdW_t.}
\]

This is the most direct rigorous realization of the proposed analogy. The
\(i\) creates rotation; the Brownian quadratic variation creates the
additional real drift \(-\sigma^2/2\) required to keep the radius constant.

The rule \((dW)^2=dt\) does not *act like* \(i^2=-1\). Rather, the full
stochastic increment has the Itô square

\[
(i\sigma Z\,dW)^2=-\sigma^2Z^2dt.
\]

After factoring out \(Z\), the corresponding relative square is

\[
(i\sigma dW)^2=i^2\sigma^2(dW)^2=-\sigma^2dt.
\]

Equivalently, for \(f(x)=r_0e^{ix}\), \(f''=-f\), so half of the
second-order term in Itô's lemma is \(-\sigma^2Zdt/2\).

## A finite-step polar random-walk formula

For \(h>0\) and
\(\Delta W_n=\sqrt h\,\xi_n\), the exact phase step is

\[
\boxed{
Z_{n+1}
=Z_n\exp\!\left(i[\mu h+\sigma\sqrt h\,\xi_n]\right).}
\]

Equivalently,

\[
R_{n+1}=R_n,\qquad
\Theta_{n+1}=\Theta_n+\mu h+\sigma\sqrt h\,\xi_n.
\]

This is an exact discrete random walk on the circle. Its continuous-time
limit is the stochastic-rotation SDE above.

For stochastic amplitude as well as phase, let

\[
\Delta A_n=a h+u\cdot\Delta W_n,\qquad
\Delta\Theta_n=\omega h+v\cdot\Delta W_n.
\]

Then

\[
\boxed{
Z_{n+1}
=Z_n\exp\!\left[
(a+i\omega)h+(u+i v)\cdot\Delta W_n
\right].}
\]

The real part of the exponent changes log-radius; the imaginary part changes
angle.

## The unified continuous formula

Let

\[
dA_t=a_tdt+u_t\cdot dW_t,\qquad
d\Theta_t=\omega_tdt+v_t\cdot dW_t,
\]

and set \(Z_t=e^{A_t+i\Theta_t}\). Then

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

This is the sought stochastic analogue of

\[
z=re^{i\theta}.
\]

It unites random log-amplitude and random phase while displaying every Itô
correction.

## Six questions answered

### 1. In what sense is \((dW_t)^2=dt\) true?

It is an equality in the Itô differential calculus representing

\[
[W]_t=t,
\]

the quadratic-variation limit

\[
\sum_k(W_{t_{k+1}}-W_{t_k})^2\to t.
\]

For a finite increment, only
\(\mathbb E[(\Delta W)^2]=\Delta t\) is exact; its square is still random.

### 2. Why does this not make \(dW_t\) an imaginary unit?

\(i^2=-1\) is an exact identity in a nontruncated algebra and multiplication
by \(i\) rotates the complex plane. The Itô rule is asymptotic
quadratic-variation bookkeeping. Formally, \((dW)^3=0\) at retained order,
whereas powers of \(i\) cycle forever. Brownian noise has no intrinsic
orientation.

### 3. What is the exponential form associated with an SDE?

For a continuous local martingale \(M\),

\[
\mathcal E(M)_t
=\exp\!\left(M_t-\frac12[M]_t\right)
\]

solves \(dZ_t=Z_t\,dM_t\). For geometric Brownian motion,

\[
dS_t=\mu S_tdt+\sigma S_tdW_t,
\]

\[
S_t=S_0e^{(\mu-\sigma^2/2)t+\sigma W_t}.
\]

This is the algebraic exponential bridge.

### 4. When is \(Z_t=R_te^{i\Theta_t}\) useful?

It is useful when the state is genuinely two-dimensional and remains away
from zero. It separates radial and angular noise, exposes their correlation,
and reveals Itô corrections. It is not informative for a one-dimensional
real increment, whose angle is only \(0\) or \(\pi\).

### 5. What SDE represents pure stochastic rotation?

\[
\boxed{
dZ_t
=\left(i\omega-\frac12\beta^2\right)Z_tdt
+i\beta Z_tdW_t}
\]

in Itô form, or

\[
\boxed{
dZ_t=i\omega Z_tdt+i\beta Z_t\circ dW_t}
\]

in Stratonovich form.

### 6. How do the main processes fit together?

| Process | Exact state form | Geometry |
|---|---|---|
| Arithmetic diffusion | \(X_0+\mu t+\sigma W_t\) | additive line |
| Geometric Brownian motion | \(S_0e^{(\mu-\sigma^2/2)t+\sigma W_t}\) | random amplitude |
| Brownian phase | \(r_0e^{i(\theta_0+\omega t+\beta W_t)}\) | random angle, fixed radius |
| General amplitude–phase | \(e^{A_t+i\Theta_t}\) | random radius and angle |
| Planar Brownian motion | \(Z_0+\sigma(W^1_t+iW^2_t)\) | Cartesian noise; Bessel radius and time-changed angle |

## Classification of the analogies

| Statement | Classification |
|---|---|
| \(i^2=-1\) | exact algebraic identity |
| \(\mathbb E[(\Delta W)^2]=\Delta t\) | exact expectation identity |
| \(\sum(\Delta W)^2\to t\) | limiting statement |
| \([W]_t=t\) | quadratic-variation identity |
| \((dW)^2=dt\) | equality in Itô differential calculus |
| \(X_t-X_s\sim N(\mu\Delta t,\sigma^2\Delta t)\) | equality in distribution |
| \(dW\) is like \(i\) | heuristic analogy that fails algebraically and geometrically |
| \(r_0e^{i(X_0+\mu t+\sigma W_t)}\) is stochastic rotation | exact process representation |

## Bottom line

There are two different exponentials:

\[
\underbrace{\mathcal E(M)_t}_{\text{quadratic-variation-corrected
algebraic exponential}}
\qquad\text{and}\qquad
\underbrace{e^{i\Theta_t}}_{\text{geometric phase rotation}}.
\]

Their intersection,

\[
Z_t=e^{A_t+i\Theta_t},
\]

is the precise bridge. Quadratic variation supplies deterministic correction
terms; the imaginary unit supplies rotation. Neither replaces the other.
