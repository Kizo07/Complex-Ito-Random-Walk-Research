# Scalar Polar Form and Zero Crossings

## 1. The process that must be preserved

Let

\[
X_t=X_0+\mu t+\sigma W_t,
\qquad
dX_t=\mu\,dt+\sigma\,dW_t,
\]

with \(\sigma>0\). This is a real-valued diffusion with one Brownian driver.
Embedding it in \(\mathbb C\) does not by itself add another stochastic
direction.

The literal complex embedding is

\[
Z_t=X_t+i0.
\]

Away from zero it has polar coordinates

\[
R_t=|X_t|,
\qquad
\Theta_t=
\begin{cases}
0,&X_t>0,\\
\pi,&X_t<0.
\end{cases}
\]

Thus the radius is stochastic, but the angle only records the sign. A
continuously rotating phase is not hidden inside a scalar arithmetic Brownian
motion.

## 2. Localized logarithmic representation

Assume \(X_0\ne0\) and define

\[
\tau_0=\inf\{t\ge0:X_t=0\}.
\]

For \(t<\tau_0\), the sign of \(X_t\) agrees with the sign of \(X_0\).
Apply Itô's formula to

\[
f(x)=\log|x|,
\qquad x\ne0.
\]

Since

\[
f'(x)=\frac1x,
\qquad
f''(x)=-\frac1{x^2},
\]

we obtain

\[
d\log|X_t|
=
\frac{\mu}{X_t}dt
+\frac{\sigma}{X_t}dW_t
-\frac12\frac{\sigma^2}{X_t^2}dt.
\]

Integrating and exponentiating gives

\[
\boxed{
X_t
=X_0
\exp\!\left[
\int_0^t\frac{\mu}{X_s}ds
+\int_0^t\frac{\sigma}{X_s}dW_s
-\frac12\int_0^t\frac{\sigma^2}{X_s^2}ds
\right],
\qquad t<\tau_0.}
\]

The factor \(X_0\), rather than \(|X_0|\), restores the constant sign on the
localized interval.

This is an exact stochastic-logarithm representation, but it is singular at
zero. Writing \(d\log X_t\) without qualification is incorrect when
\(X_0<0\); the real formula is \(d\log|X_t|\).

## 3. Localization before zero

For rigorous bounded-coefficient calculations, use

\[
\tau_\varepsilon
=\inf\{t\ge0:|X_t|\le\varepsilon\},
\qquad
0<\varepsilon<|X_0|.
\]

On \([0,\tau_\varepsilon]\), the functions \(1/X_t\) and \(1/X_t^2\) are
bounded. The identity above is first established on every such stopped
interval. Letting \(\varepsilon\downarrow0\) recovers the statement on
\([0,\tau_0)\).

This distinction matters:

- the differential identity is exact under localization;
- it does not extend through \(\tau_0\) as a single real logarithm;
- the Cartesian process \(X_t\) itself remains perfectly well defined at and
  after \(\tau_0\).

## 4. Why the global radius needs local time

The function \(x\mapsto|x|\) is not twice differentiable at zero. Ordinary
Itô's formula therefore cannot give a global equation for \(R_t=|X_t|\).

Tanaka's formula gives the correct replacement:

\[
\boxed{
|X_t|
=|X_0|
+\int_0^t\operatorname{sgn}(X_s)\,dX_s
+L_t^0(X),}
\]

where \(L_t^0(X)\) is the symmetric semimartingale local time of \(X\) at
zero. In differential notation,

\[
\boxed{
dR_t
=
\mu\operatorname{sgn}(X_t)dt
+\sigma\operatorname{sgn}(X_t)dW_t
+dL_t^0(X).}
\]

The convention at \(X_t=0\) does not affect the stochastic integral because
the zero set has zero Lebesgue measure almost surely.

The local-time term is not an optional modeling force. It is the
second-order correction created by the corner of \(|x|\) at zero. It keeps
the radius nonnegative while the underlying real process changes sign.

## 5. Occupation-density interpretation

Under the local-time normalization above,

\[
\int_0^t g(X_s)\,d[X,X]_s
=\int_{\mathbb R}g(a)L_t^a(X)\,da.
\]

For constant volatility,

\[
d[X,X]_s=\sigma^2ds.
\]

Consequently,

\[
\boxed{
L_t^0(X)
=
\lim_{\varepsilon\downarrow0}
\frac{\sigma^2}{2\varepsilon}
\int_0^t
\mathbf1_{\{|X_s|<\varepsilon\}}ds}
\]

in the standard senses supplied by the occupation-density theory.

This explains why a time-grid approximation near zero must be refined in
both \(h\) and \(\varepsilon\). Counting exact grid hits would fail because a
continuous random variable equals zero at a fixed grid time with probability
zero.

## 6. The angular obstruction at zero

On each connected interval where \(X_t\ne0\), \(\Theta_t\) is constant:

\[
d\Theta_t=0.
\]

A sign change forces the real-axis path through the complex origin. Polar
coordinates are undefined at that instant, and the phase changes between
\(0\) and \(\pi\).

Therefore no single continuous polar angle represents the literal real-axis
embedding across all zero crossings. The obstruction is geometric, not a
failure of Itô calculus.

## 7. Three scalar embeddings

The original scalar process admits several complex images with different
properties.

### Real-axis image

\[
Z_t=X_t.
\]

- state-injective;
- stochastic radius \(|X_t|\);
- phase only \(0\) or \(\pi\);
- singular polar coordinates at zero.

### Fixed-radius phase image

\[
Z_t=r_0e^{i\beta(X_t-X_0)}.
\]

- nonvanishing and continuously liftable along a path;
- stochastic angle;
- fixed radius;
- not state-injective from \(Z_t\) alone because of phase periodicity.

### Logarithmic-spiral image

\[
Z_t
=Z_0e^{(\alpha+i\beta)(X_t-X_0)},
\qquad \alpha\ne0.
\]

- nonvanishing;
- stochastic radius and angle;
- globally state-injective because the radius recovers \(X_t\);
- driven by exactly the original Brownian motion;
- constrained to a one-dimensional curve in \(\mathbb C\).

The third construction is the central Phase 3 representation.

## 8. Exact, local, and heuristic statements

| Statement | Classification |
|---|---|
| \(Z_t=X_t+i0\) | exact deterministic embedding |
| \(R_t=|X_t|\) | exact pathwise identity |
| \(\Theta_t\in\{0,\pi\}\) away from zero | exact local polar description |
| localized exponential for \(X_t\) | exact on \(t<\tau_0\) |
| Tanaka equation for \(|X_t|\) | exact global semimartingale identity |
| occupation-density approximation | limiting statement |
| scalar Brownian motion contains a hidden continuous angle | false |

## 9. Conclusion

The critique is correct that the original scalar diffusion cannot acquire an
independent angular Brownian motion through a change of coordinates. It is
also incomplete if interpreted as saying that a one-driver process cannot
have both stochastic radius and angle.

The real-axis form gives a stochastic radius with singular sign angle. The
logarithmic-spiral form developed next gives a smooth, nonvanishing, and
information-preserving complex exponential with both polar coordinates
stochastic.
