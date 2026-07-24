# From a Scaled Random Walk to the Itô Table

## 1. The discrete starting point

Fix a horizon \(T\), divide it into \(N\) intervals of length
\(h=T/N\), and set

\[
\Delta W_k=\sqrt{h}\,\xi_k,
\qquad
\xi_k\stackrel{\mathrm{iid}}{\sim}N(0,1).
\]

Then

\[
\mathbb E[\Delta W_k]=0,\qquad
\mathbb E[(\Delta W_k)^2]=h,\qquad
\operatorname{Var}((\Delta W_k)^2)=2h^2.
\]

The equality \(\mathbb E[(\Delta W_k)^2]=h\) is an equality of
expectations. It is not the pointwise statement
\((\Delta W_k)^2=h\): in fact,
\((\Delta W_k)^2/h=\xi_k^2\) has a \(\chi^2_1\) distribution at every
resolution.

The accumulated squared increments are

\[
Q_N=\sum_{k=0}^{N-1}(\Delta W_k)^2
    =h\sum_{k=0}^{N-1}\xi_k^2.
\]

Independence gives

\[
\mathbb E[Q_N]=Nh=T,\qquad
\operatorname{Var}(Q_N)=2Nh^2=\frac{2T^2}{N}.
\]

Thus \(Q_N\to T\) in \(L^2\), hence in probability. The random square of
one increment does not become deterministic after division by \(h\);
the *sum* of many squares concentrates because its relative fluctuations
are of order \(N^{-1/2}\).

The same Brownian scaling arises from a normalized finite-variance random
walk. Donsker's theorem connects its interpolated path to Brownian motion.
Quadratic variation itself is not a continuous functional under uniform
path convergence, so this scaling argument is motivation rather than a
standalone proof of Brownian quadratic variation.

## 2. Brownian quadratic variation

Let \(W\) be Brownian motion and let
\(\pi=\{0=t_0<\cdots<t_n=T\}\) be a deterministic partition. Define

\[
Q_\pi(W)=\sum_{k=0}^{n-1}
  (W_{t_{k+1}}-W_{t_k})^2.
\]

Since the increments are independent Gaussians with variances
\(\Delta t_k=t_{k+1}-t_k\),

\[
\mathbb E[Q_\pi(W)]=T,\qquad
\operatorname{Var}(Q_\pi(W))
 =2\sum_k(\Delta t_k)^2
 \le 2T\,|\pi|,
\]

where \(|\pi|=\max_k\Delta t_k\). Consequently,

\[
Q_\pi(W)\longrightarrow T
\quad\text{in }L^2
\quad\text{as }|\pi|\to0.
\]

For the partial interval \([0,t]\), the limit is \(t\), written

\[
[W]_t=t.
\]

This is the precise source of the mnemonic

\[
(dW_t)^2=dt.
\]

It means that the second-order increment that survives when stochastic
Taylor expansions are accumulated is Brownian quadratic variation. It does
not mean that \(dW_t\) is an ordinary infinitesimal number.

## 3. Order bookkeeping

On a step of size \(h\),

\[
\Delta t=O(h),\qquad \Delta W=O_{\mathbb P}(h^{1/2}).
\]

The relevant products have orders

\[
(\Delta W)^2=O_{\mathbb P}(h),\quad
\Delta t\,\Delta W=O_{\mathbb P}(h^{3/2}),\quad
(\Delta t)^2=O(h^2).
\]

Across \(T/h\) time steps, the quadratic Brownian term has a nonzero
accumulated limit. The other two terms vanish under the hypotheses used in
Itô calculus. This produces the first-order Itô table

\[
\begin{array}{c|cc}
 &dt&dW\\ \hline
dt&0&0\\
dW&0&dt
\end{array},
\]

or

\[
(dt)^2=0,\qquad dt\,dW=0,\qquad(dW)^2=dt.
\]

The zeros mean “discarded at Itô order,” not literal real-number zeros.
For two Brownian motions \(W^1,W^2\) with instantaneous correlation
\(\rho_t\),

\[
dW^1_t\,dW^2_t=\rho_t\,dt.
\]

In particular, independent Brownian drivers have zero cross-variation.

## 4. Itô's lemma from Taylor expansion

For \(dX_t=a_tdt+b_tdW_t\), formally expand a smooth function:

\[
df(t,X_t)
=f_tdt+f_xdX_t+\frac12f_{xx}(dX_t)^2.
\]

Using the Itô table,

\[
(dX_t)^2
=(a_tdt+b_tdW_t)^2=b_t^2dt,
\]

so

\[
df
=\left(f_t+a_tf_x+\frac12b_t^2f_{xx}\right)dt
+b_tf_xdW_t.
\]

The term involving \(f_{xx}\) is the operational effect of quadratic
variation. It is the mechanism behind every Itô drift correction used later
in this project.

## 5. Comparison with \(i^2=-1\)

There is a useful resemblance: both \(i^2=-1\) and \((dW)^2=dt\) are
multiplication rules that change what survives in an expansion. Their
meanings are fundamentally different.

| Feature | Complex unit \(i\) | Itô symbols \(dt,dW\) |
|---|---|---|
| Exact status | Algebraic identity \(i^2=-1\) | Differential-calculus rule induced by quadratic variation |
| Repeated powers | Periodic: \(i^4=1\) | Truncated at retained order: \((dW)^3=0\) formally |
| Geometry | Multiplication by \(i\) rotates by \(\pi/2\) | \(dW\) has no inherent planar rotation |
| Sign | The square is negative | The quadratic variation is nonnegative |
| Randomness | \(i\) is deterministic | Brownian increments are random |

A compact mnemonic algebra is

\[
\mathbb R[\varepsilon]/(\varepsilon^3),
\qquad
dW\leftrightarrow\varepsilon,\quad
dt\leftrightarrow\varepsilon^2.
\]

Then \((dW)^2=dt\), \(dt\,dW=0\), and \((dt)^2=0\) follow from
\(\varepsilon^3=0\). This quotient algebra is a bookkeeping model only. It
does not encode adaptedness, probability, stochastic integration, or limits
of quadratic variation, and therefore is not a definition of Itô calculus.

By contrast,

\[
\mathbb C\cong\mathbb R[x]/(x^2+1)
\]

has no truncation and supports genuine rotation. The right bridge between the
two subjects is therefore not \(dW=i\). The bridges are:

1. **algebraic:** quadratic variation modifies exponential calculus;
2. **geometric:** Brownian motion can drive a genuine complex phase.

## 6. Status of the statements

- \(\mathbb E[(\Delta W)^2]=\Delta t\): exact expectation identity.
- \(\sum(\Delta W)^2\to T\): limiting statement, here proved in \(L^2\).
- \([W]_t=t\): quadratic-variation identity.
- \((dW)^2=dt\): equality inside Itô differential bookkeeping.
- \(dW=i\): false.
