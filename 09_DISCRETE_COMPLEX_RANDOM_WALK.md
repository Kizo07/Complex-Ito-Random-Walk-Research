# The Discrete Complex Random Walk and Its Logarithmic Limit

## 1. Additive Cartesian walk

Let \(h=T/N\) and consider

\[
Z_{n+1}=Z_n+\Delta Z_n,
\]

with

\[
\Delta Z_n=\mu_nh
+\sigma\sqrt h\,(\xi_n+i\eta_n),
\]

where \(\xi_n,\eta_n\) are independent standard normal variables.

For zero drift and constant \(\sigma\), this is an exact sample of planar
Brownian motion on the grid:

\[
Z_n=Z_0+\sigma(W_{nh}^1+iW_{nh}^2).
\]

The walk is additive in Cartesian coordinates. The goal is to expose its
exact multiplicative polar form without pretending its radius is fixed.

## 2. Exact finite-step polar update

If \(Z_n\ne0\) and \(Z_{n+1}\ne0\), define

\[
R_{n+1}=|Z_{n+1}|,
\]

and choose the angular increment by continuous unwrapping:

\[
\Delta\Theta_n
=\operatorname{Arg}_{\mathrm{cont}}
\left(\frac{Z_{n+1}}{Z_n}\right).
\]

Then

\[
\Delta A_n
=\log R_{n+1}-\log R_n
=\log\left|\frac{Z_{n+1}}{Z_n}\right|.
\]

Consequently,

\[
\boxed{
Z_{n+1}
=Z_n\exp(\Delta A_n+i\Delta\Theta_n).}
\]

Equivalently,

\[
\boxed{
Z_{n+1}
=Z_n\exp\!\left[
\operatorname{Log}_{\mathrm{cont}}
\left(1+\frac{\Delta Z_n}{Z_n}\right)
\right].}
\]

This is an exact finite-grid identity. Unlike the circle walk, its
multiplicative factor depends on the current state through \(1/Z_n\).

## 3. Exact path product

Multiplying the one-step ratios gives

\[
\frac{Z_N}{Z_0}
=\prod_{n=0}^{N-1}
\left(1+\frac{\Delta Z_n}{Z_n}\right).
\]

With consistent logarithmic branches,

\[
\boxed{
\frac{Z_N}{Z_0}
=\exp\!\left[
\sum_{n=0}^{N-1}
\operatorname{Log}_{\mathrm{cont}}
\left(1+\frac{\Delta Z_n}{Z_n}\right)
\right].}
\]

The real part of the summed logarithm is exactly

\[
\log\frac{R_N}{R_0}.
\]

Its imaginary part is the total unwrapped winding angle.

## 4. Local logarithmic expansion

Let

\[
q_n=\frac{\Delta Z_n}{Z_n}.
\]

On stopped paths for which \(|q_n|\) is small,

\[
\operatorname{Log}(1+q_n)
=q_n-\frac12q_n^2+\frac13q_n^3-\cdots.
\]

Thus

\[
\boxed{
\Delta\log Z_n
=
\frac{\Delta Z_n}{Z_n}
-\frac12\left(\frac{\Delta Z_n}{Z_n}\right)^2
+O_p(h^{3/2}).}
\]

Over \(N=T/h\) steps, the accumulated third-order remainder tends to zero
under localization. The first sum converges to an Itô integral and the second
to complex quadratic variation:

\[
\sum_n\frac{\Delta Z_n}{Z_n}
\longrightarrow
\int_0^T\frac{dZ_t}{Z_t},
\]

\[
\sum_n\left(\frac{\Delta Z_n}{Z_n}\right)^2
\longrightarrow
\int_0^T\frac{d[Z,Z]_t}{Z_t^2}.
\]

Therefore

\[
\boxed{
\log\frac{Z_T}{Z_0}
=
\int_0^T\frac{dZ_t}{Z_t}
-\frac12\int_0^T\frac{d[Z,Z]_t}{Z_t^2}.}
\]

This derives the complex stochastic-logarithm formula directly from the
finite random walk.

## 5. Isotropic cancellation

For isotropic increments,

\[
\Delta Z_n
=\sigma\sqrt h(\xi_n+i\eta_n).
\]

Although each finite square \((\Delta Z_n)^2\) is random and nonzero,

\[
\sum_n(\Delta Z_n)^2\longrightarrow[Z,Z]_T=0.
\]

Hence

\[
\sum_n\left(\frac{\Delta Z_n}{Z_n}\right)^2
\longrightarrow0
\]

on localized paths. The limiting logarithm becomes

\[
\log\frac{Z_T}{Z_0}
=\int_0^T\frac{dZ_t}{Z_t},
\]

and

\[
Z_T
=Z_0\exp\!\left(\int_0^T\frac{dZ_t}{Z_t}\right).
\]

The correction vanishes only after summing in the quadratic-variation limit.
It is not correct to set an individual finite square to zero.

## 6. Anisotropic correction

For

\[
\Delta Z_n
=\sqrt h(\sigma_x\xi_n+i\sigma_y\eta_n),
\]

\[
\sum_n(\Delta Z_n)^2
\longrightarrow
(\sigma_x^2-\sigma_y^2)T.
\]

Therefore

\[
\log\frac{Z_T}{Z_0}
=
\int_0^T\frac{dZ_t}{Z_t}
-\frac12(\sigma_x^2-\sigma_y^2)
\int_0^T\frac{dt}{Z_t^2}.
\]

An exponential based only on the first integral is then systematically
wrong. The notebook will show that the corrected reconstruction converges
while the uncorrected one does not.

## 7. Polar increment expansion

Since

\[
\Delta A_n+i\Delta\Theta_n
=q_n-\frac12q_n^2+O_p(h^{3/2}),
\]

the real and imaginary parts give

\[
\Delta A_n
=\operatorname{Re}q_n
-\frac12\operatorname{Re}(q_n^2)
+O_p(h^{3/2}),
\]

\[
\Delta\Theta_n
=\operatorname{Im}q_n
-\frac12\operatorname{Im}(q_n^2)
+O_p(h^{3/2}).
\]

For the isotropic process, write

\[
\Delta W_n^R
=\cos\Theta_n\Delta W_n^1
+\sin\Theta_n\Delta W_n^2,
\]

\[
\Delta W_n^\Theta
=-\sin\Theta_n\Delta W_n^1
+\cos\Theta_n\Delta W_n^2.
\]

The first-order terms are

\[
\Delta A_n
\approx\frac{\sigma}{R_n}\Delta W_n^R,
\qquad
\Delta\Theta_n
\approx\frac{\sigma}{R_n}\Delta W_n^\Theta.
\]

These converge to the stochastic log-radius and angle equations. The
state-dependent coefficient \(1/R_n\) is exactly what was absent from the
fixed-circle model.

## 8. Branch handling

The principal value of `atan2` lies in a bounded interval and jumps by
\(2\pi\). It cannot represent winding by itself.

A numerical implementation must:

1. compute successive principal angles;
2. shift each difference by an integer multiple of \(2\pi\) into a locally
   continuous range;
3. accumulate the adjusted differences;
4. flag steps that pass too close to the origin, where coarse sampling makes
   the winding ambiguous.

The exact endpoint ratio remains correct even if an integer winding is missed,
because \(e^{2\pi i k}=1\). The unwrapped angle and stochastic-logarithm path,
however, require adequate temporal resolution.

## 9. Stopping near the origin

Define the grid stopping index

\[
\nu_\varepsilon
=\min\{n:R_n\le\varepsilon\}.
\]

Convergence tests for \(1/Z_n\), \(1/Z_n^2\), and angle increments should be
performed only through \(\nu_\varepsilon\). This mirrors the continuous
stopping time

\[
\tau_\varepsilon=\inf\{t:R_t\le\varepsilon\}.
\]

The stopping is a numerical and analytical localization device. It does not
assert that planar Brownian motion started away from the origin hits the
origin.

## 10. Comparison with the circle step

The Phase 1 circle walk had the exact update

\[
Z_{n+1}
=Z_n\exp\!\left(
i[\omega h+\beta\sqrt h\,\xi_n]
\right).
\]

The radius was fixed because every multiplier had unit modulus.

The planar walk has

\[
Z_{n+1}
=Z_n\exp\!\left[
\operatorname{Log}_{\mathrm{cont}}
\left(
1+\frac{\sigma\sqrt h(\xi_n+i\eta_n)}{Z_n}
\right)
\right].
\]

Now both parts of the exponent are stochastic:

- the real part changes radius;
- the imaginary part changes angle;
- both depend on the current state;
- two independent Gaussian directions produce full planar noise.

This is the finite-step formula that moves the project beyond Brownian motion
on a circle.

## 11. Classification of formulas

| Formula | Status |
|---|---|
| \(Z_{n+1}=Z_n+\Delta Z_n\) | exact discrete additive update |
| \(Z_{n+1}=Z_n\exp(\operatorname{Log}_{\mathrm{cont}}(1+\Delta Z_n/Z_n))\) | exact discrete multiplicative identity |
| \(\log(1+q)=q-q^2/2+O(q^3)\) | local analytic expansion |
| sums of \(q_n\) converge to \(\int dZ/Z\) | stochastic-integral limit under localization |
| sums of \(q_n^2\) converge to \(\int d[Z,Z]/Z^2\) | quadratic-variation limit under localization |
| correction vanishes for isotropic planar Brownian motion | exact consequence of \([Z,Z]=0\) |
| one finite \((\Delta Z)^2\) equals zero | false |
