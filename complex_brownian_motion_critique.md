# Critique of the Proposed Complex Brownian Motion Representation

The proposed formula is mathematically meaningful, but it is important to distinguish between a scalar arithmetic Brownian motion and a genuinely planar Brownian motion.

## 1. Scalar Arithmetic Brownian Motion

Start with

\[
X_t = X_0 + \mu t + \sigma W_t,
\qquad
dX_t = \mu\,dt + \sigma\,dW_t.
\]

This process has only one Brownian driver. Its exact localized stochastic-exponential representation is

\[
X_t
=
X_0
\exp\left[
\int_0^t \frac{\mu}{X_s}\,ds
+
\int_0^t \frac{\sigma}{X_s}\,dW_s
-
\frac12
\int_0^t \frac{\sigma^2}{X_s^2}\,ds
\right],
\]

valid up to the first hitting time of zero,

\[
\tau_0=\inf\{t\ge 0:X_t=0\}.
\]

This follows from Itô's formula:

\[
d\log X_t
=
\frac{dX_t}{X_t}
-
\frac12\frac{d[X,X]_t}{X_t^2},
\]

with

\[
d[X,X]_t=\sigma^2dt.
\]

This representation is exact, but it is still one-dimensional. A real-valued process does not acquire a continuously evolving stochastic angle merely by being written in polar form.

Before crossing zero,

\[
X_t=R_te^{i\Theta_t},
\]

where

\[
R_t=|X_t|,
\qquad
\Theta_t=
\begin{cases}
0,&X_t>0,\\
\pi,&X_t<0.
\end{cases}
\]

The angle changes only when the process crosses zero, precisely where the logarithmic representation becomes singular.

## 2. Fixed-Radius Complex Embedding of the Scalar Process

A natural complex embedding of the scalar process is

\[
Z_t=r_0e^{iX_t}.
\]

Then

\[
R_t=r_0,
\qquad
\Theta_t=X_t \pmod{2\pi}.
\]

Applying Itô's formula gives

\[
dZ_t
=
\left(i\mu-\frac{\sigma^2}{2}\right)Z_t\,dt
+
i\sigma Z_t\,dW_t.
\]

The exact solution is

\[
Z_t=Z_0e^{i\mu t+i\sigma W_t}.
\]

The apparent damping term

\[
-\frac{\sigma^2}{2}Z_t\,dt
\]

is the Itô correction. It does not shrink the path radius because the quadratic variation of the stochastic exponential cancels it exactly:

\[
|Z_t|=r_0.
\]

This is the appropriate complex representation when one wants to preserve the single stochastic degree of freedom in

\[
X_t=X_0+\mu t+\sigma W_t.
\]

## 3. The Proposed Stochastic-Radius Formula

The proposed formula is

\[
Z_t
=
Z_0
\exp\left[
\int_0^t\frac{\sigma}{R_s}\,dB_s^R
+
i\int_0^t\frac{\sigma}{R_s}\,dB_s^\Theta
\right],
\]

together with

\[
dR_t
=
\frac{\sigma^2}{2R_t}\,dt
+
\sigma\,dB_t^R.
\]

This formula is correct for a different process:

\[
dZ_t
=
\sigma\,dW_t^1
+
i\sigma\,dW_t^2,
\]

where \(W^1\) and \(W^2\) are independent Brownian motions.

This is an isotropic two-dimensional Brownian motion. It has two independent stochastic degrees of freedom rather than one.

Writing

\[
Z_t=R_te^{i\Theta_t},
\]

define rotated Brownian motions by

\[
dB_t^R
=
\cos\Theta_t\,dW_t^1
+
\sin\Theta_t\,dW_t^2,
\]

and

\[
dB_t^\Theta
=
-\sin\Theta_t\,dW_t^1
+
\cos\Theta_t\,dW_t^2.
\]

Because this transformation is orthogonal, \(B^R\) and \(B^\Theta\) are independent Brownian motions.

The polar equations are then

\[
dR_t
=
\frac{\sigma^2}{2R_t}\,dt
+
\sigma\,dB_t^R,
\]

and

\[
d\Theta_t
=
\frac{\sigma}{R_t}\,dB_t^\Theta.
\]

The radius is a two-dimensional Bessel process.

Applying Itô's formula to \(\log R_t\),

\[
d\log R_t
=
\frac{1}{R_t}dR_t
-
\frac{1}{2R_t^2}d[R]_t.
\]

Since

\[
d[R]_t=\sigma^2dt,
\]

the radial drift cancels:

\[
d\log R_t
=
\frac{\sigma}{R_t}\,dB_t^R.
\]

Therefore,

\[
R_t
=
R_0
\exp\left[
\int_0^t\frac{\sigma}{R_s}\,dB_s^R
\right].
\]

Also,

\[
\Theta_t
=
\Theta_0
+
\int_0^t\frac{\sigma}{R_s}\,dB_s^\Theta.
\]

Combining the two equations gives

\[
Z_t
=
Z_0
\exp\left[
\int_0^t\frac{\sigma}{R_s}\,dB_s^R
+
i\int_0^t\frac{\sigma}{R_s}\,dB_s^\Theta
\right].
\]

Thus, the proposed expression is mathematically valid for isotropic planar Brownian motion.

## 4. Adding Drift

A planar analogue of arithmetic Brownian motion is

\[
dZ_t
=
\mu_c\,dt
+
\sigma(dW_t^1+i\,dW_t^2),
\]

where

\[
\mu_c=\mu_x+i\mu_y.
\]

The exact polar equations become

\[
dR_t
=
\left[
\operatorname{Re}\left(\mu_c e^{-i\Theta_t}\right)
+
\frac{\sigma^2}{2R_t}
\right]dt
+
\sigma\,dB_t^R,
\]

and

\[
d\Theta_t
=
\frac{
\operatorname{Im}\left(\mu_c e^{-i\Theta_t}\right)
}{R_t}\,dt
+
\frac{\sigma}{R_t}\,dB_t^\Theta.
\]

For a purely horizontal real drift \(\mu_c=\mu\),

\[
dR_t
=
\left(
\mu\cos\Theta_t
+
\frac{\sigma^2}{2R_t}
\right)dt
+
\sigma\,dB_t^R,
\]

and

\[
d\Theta_t
=
-\frac{\mu\sin\Theta_t}{R_t}\,dt
+
\frac{\sigma}{R_t}\,dB_t^\Theta.
\]

The corresponding multiplicative representation is

\[
Z_t
=
Z_0
\exp\left[
\int_0^t\frac{\mu_c}{Z_s}\,ds
+
\int_0^t\frac{\sigma}{R_s}\,dB_s^R
+
i\int_0^t\frac{\sigma}{R_s}\,dB_s^\Theta
\right].
\]

The proposed formula is the special case \(\mu_c=0\).

## 5. The General Complex Stochastic-Exponential Identity

For a continuous complex semimartingale \(Z_t\), localized away from zero,

\[
Z_t
=
Z_0
\exp\left[
\int_0^t\frac{dZ_s}{Z_s}
-
\frac12
\int_0^t\frac{d[Z,Z]_s}{Z_s^2}
\right].
\]

The complex quadratic variation is

\[
[Z,Z]_t
=
[X,X]_t-[Y,Y]_t+2i[X,Y]_t,
\]

where

\[
Z_t=X_t+iY_t.
\]

For isotropic planar Brownian motion,

\[
dZ_t
=
\sigma\,dW_t^1+i\sigma\,dW_t^2,
\]

we obtain

\[
d[Z,Z]_t
=
\sigma^2dt+i^2\sigma^2dt
=
\sigma^2dt-\sigma^2dt
=
0.
\]

Therefore, the general formula reduces to

\[
Z_t
=
Z_0
\exp\left(
\int_0^t\frac{dZ_s}{Z_s}
\right).
\]

In polar coordinates,

\[
\frac{dZ_t}{Z_t}
=
\frac{\sigma}{R_t}\,dB_t^R
+
i\frac{\sigma}{R_t}\,dB_t^\Theta.
\]

This reproduces the proposed representation.

The cancellation

\[
(dB^R)^2+i^2(dB^\Theta)^2
=
dt-dt
=
0
\]

is a precise mathematical instance in which \(i^2=-1\) cancels two equal quadratic-variation contributions.

However,

\[
d[Z,\overline Z]_t
=
2\sigma^2dt
\]

does not vanish. This nonzero Hermitian quadratic variation is why the Euclidean radius is stochastic.

## 6. The Main Dimensional Obstruction

The scalar arithmetic Brownian motion

\[
dX_t=\mu\,dt+\sigma\,dW_t
\]

has one instantaneous random increment.

The planar polar formula contains two independent increments:

\[
dB_t^R,
\qquad
dB_t^\Theta.
\]

A coordinate transformation cannot create an additional independent Brownian driver. Therefore, the stochastic-radius formula cannot be an equivalent polar rewriting of the original scalar process.

The three relevant constructions are:

### Scalar arithmetic Brownian motion

\[
X_t=X_0+\mu t+\sigma W_t.
\]

This is a one-dimensional process.

### Fixed-radius phase embedding

\[
Z_t=r_0e^{iX_t}.
\]

This preserves the same single stochastic degree of freedom and turns it into a stochastic angle.

### Genuine planar arithmetic Brownian motion

\[
Z_t
=
Z_0+\mu_ct+\sigma(W_t^1+iW_t^2).
\]

This has a stochastic radius and stochastic angle because it has two independent Brownian coordinates.

## 7. Final Assessment

The proposed formula is mathematically sound as a polar representation of isotropic planar Brownian motion.

It should not be described as a polar rewriting of the scalar process

\[
X_t=X_0+\mu t+\sigma W_t
\]

unless a second independent Brownian coordinate is explicitly introduced.

For the original scalar process, the natural complex representation is

\[
Z_t=r_0e^{iX_t},
\]

which has a fixed radius and a stochastic angle.

For a genuinely planar process with stochastic radius and stochastic angle, the correct underlying model is

\[
dZ_t
=
\mu_c\,dt
+
\sigma(dW_t^1+i\,dW_t^2).
\]

One final convention must be stated explicitly. The radial drift

\[
\frac{\sigma^2}{2R_t}
\]

assumes that each Cartesian component has volatility \(\sigma\). If complex Brownian motion is normalized as

\[
B_t^{\mathbb C}
=
\frac{W_t^1+iW_t^2}{\sqrt 2},
\]

the diffusion coefficients and radial drift differ by a factor of two.
