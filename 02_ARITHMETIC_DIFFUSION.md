# Arithmetic Diffusion: The Additive Random Walk

## 1. SDE and solution

Consider the real Itô SDE with constants \(\mu,\sigma\):

\[
dX_t=\mu\,dt+\sigma\,dW_t,\qquad X_0=x_0.
\]

Integrating from \(0\) to \(t\) gives the exact pathwise representation

\[
\boxed{X_t=x_0+\mu t+\sigma W_t.}
\]

No Itô correction appears because the map from \(W_t\) to \(X_t\) is linear.

For \(s<t\),

\[
X_t-X_s=\mu(t-s)+\sigma(W_t-W_s).
\]

Since \(W_t-W_s\sim N(0,t-s)\) and is independent of the past,

\[
\boxed{X_t\mid X_s=x
\sim N\!\left(x+\mu(t-s),\,\sigma^2(t-s)\right).}
\]

In particular,

\[
\mathbb E[X_t]=x_0+\mu t,\qquad
\operatorname{Var}(X_t)=\sigma^2t.
\]

## 2. Euler steps are exact on a grid

For a step \(h\),

\[
X_{n+1}=X_n+\mu h+\sigma\sqrt h\,\xi_n,
\qquad \xi_n\stackrel{\mathrm{iid}}{\sim}N(0,1).
\]

This is usually called an Euler–Maruyama step, but for constant additive
coefficients it is also the exact transition law at the grid points.
Summing the steps gives

\[
X_N=x_0+\mu Nh+\sigma\sqrt h\sum_{n=0}^{N-1}\xi_n,
\]

which has exactly the continuous-time terminal distribution at \(T=Nh\).

## 3. Why there is no useful complex polar form

A single real increment is

\[
\Delta X=\mu h+\sigma\sqrt h\,\xi.
\]

If it is embedded into \(\mathbb C\), its polar representation is only

\[
\Delta X=|\Delta X|e^{i\Theta},
\qquad
\Theta=
\begin{cases}
0,&\Delta X\ge0,\\
\pi,&\Delta X<0.
\end{cases}
\]

Thus the “angle” contains only the sign. It is not a continuously varying
phase and it does not turn the additive solution into a stochastic analogue
of \(re^{i\theta}\).

There is a second obstruction: \(dX_t\) is local increment notation, whereas
\(re^{i\theta}\) is a coordinate representation of a state. Seeking a polar
form for \(dX_t\) conflates a tangent increment with a point in a plane.

Two meaningful replacements are:

1. change from additive to multiplicative dynamics, producing a stochastic
   exponential;
2. enlarge the state space to two real dimensions, producing a genuine
   complex amplitude and phase.

## 4. The role of \(\mu\,dt+\sigma\,dW\)

The two terms have different small-time orders:

\[
\mu h=O(h),\qquad \sigma\Delta W=O_{\mathbb P}(\sqrt h).
\]

Noise dominates the size of a sufficiently short increment, even though the
drift controls the mean. Squaring gives

\[
(dX_t)^2=\sigma^2dt
\]

inside the Itô table. This does not create rotation; it records the local
quadratic variation

\[
[X]_t=\sigma^2t.
\]

The additive diffusion is therefore the random-walk benchmark, not the
desired exponential or polar object.
