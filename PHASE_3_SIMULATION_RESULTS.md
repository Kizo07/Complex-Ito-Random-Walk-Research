# Phase 3 Simulation Results

## 1. Reproducibility

Notebook:

`notebooks/phase3_one_driver_complex_embedding.ipynb`

Builder:

`notebooks/build_phase3_notebook.py`

Environment:

- conda environment: `base`;
- Python: 3.13.9;
- NumPy: 2.3.5;
- SciPy: 1.16.3;
- Matplotlib: 3.10.6;
- nbformat: 5.10.4;
- master seed: `20260723`.

Build command:

```bash
conda run -n base python notebooks/build_phase3_notebook.py
```

Execution command:

```bash
conda run -n base jupyter nbconvert \
  --to notebook \
  --execute \
  --inplace \
  --ExecutePreprocessor.timeout=300 \
  notebooks/phase3_one_driver_complex_embedding.ipynb
```

The executed notebook completed without cell errors, and every embedded
assertion passed.

## 2. Parameters

The main logarithmic-spiral experiment used

\[
\mu=0.20,\quad
\sigma=0.65,\quad
\alpha=0.45,\quad
\beta=1.10,\quad
T=1.25,
\]

with

\[
X_0=-0.30,
\qquad
Z_0=1.20e^{0.40i}.
\]

The central map was

\[
Z_t=Z_0e^{(\alpha+i\beta)(X_t-X_0)}.
\]

## 3. Pathwise exactness

A path with \(4096\) time steps was evaluated in three ways:

1. direct evaluation of the complex exponential;
2. cumulative multiplication of the exact finite-step factors;
3. reconstruction of \(X_t\) from the radius.

The maximum errors were:

| Check | Maximum error |
|---|---:|
| exact product versus direct \(Z_t\) | \(6.273\times10^{-15}\) |
| \(X_t\) reconstructed from radius | \(1.110\times10^{-15}\) |
| logarithmic-spiral relation | \(9.437\times10^{-16}\) |

These are floating-point roundoff errors. They numerically confirm exact
algebraic identities rather than a convergence approximation.

## 4. Analytic moment checks

The terminal experiment used \(250{,}000\) independent samples.

### Radial moments

| Moment | Estimate | Exact | Monte Carlo SE | Standardized difference |
|---|---:|---:|---:|---:|
| \(\mathbb E[R_T]\) | 1.4162073 | 1.4166490 | \(9.51\times10^{-4}\) | \(-0.465\) |
| \(\mathbb E[R_T^2]\) | 2.2315513 | 2.2334193 | \(3.25\times10^{-3}\) | \(-0.575\) |

### Complex moments of \(Z_T/Z_0\)

| Power | Estimate | Exact | \(z_{\mathrm{Re}}\) | \(z_{\mathrm{Im}}\) |
|---|---|---|---:|---:|
| \(n=1\) | \(0.7376586+0.4378687i\) | \(0.7371989+0.4383209i\) | 0.484 | -0.295 |
| \(n=2\) | \(-0.0099133+0.4311182i\) | \(-0.0107536+0.4319343i\) | 0.309 | -0.318 |

All discrepancies are well within one Monte Carlo standard error.

## 5. Covariance rank

The empirical covariance of

\[
\left(\Delta\log R,\Delta\Theta\right)
\]

was divided by \(h=0.005\) and compared with

\[
\sigma^2
\begin{pmatrix}
\alpha^2&\alpha\beta\\
\alpha\beta&\beta^2
\end{pmatrix}.
\]

Using \(400{,}000\) increments, the empirical matrix was

\[
\begin{pmatrix}
0.0854997&0.2089992\\
0.2089992&0.5108870
\end{pmatrix}.
\]

Its eigenvalues were

\[
\boxed{0,\qquad0.5963867}
\]

to displayed precision. The relative covariance error was

\[
6.6111\times10^{-4}.
\]

For the two-driver planar comparison at local radius \(1.30\), the empirical
matrix was

\[
\begin{pmatrix}
0.2499651&-0.0000490\\
-0.0000490&0.2492990
\end{pmatrix},
\]

with eigenvalues

\[
\boxed{0.2492954,\qquad0.2499687}.
\]

The relative covariance error was

\[
1.9950\times10^{-3}.
\]

This directly separates one-driver stochastic radius and angle from
rank-two planar Brownian motion.

## 6. Euler–Maruyama strong convergence

The induced complex SDE

\[
dZ_t
=
\left[
c\mu+\frac12c^2\sigma^2
\right]Z_tdt
+c\sigma Z_tdW_t
\]

was integrated with Euler–Maruyama on Brownian paths shared with the exact
solution. The experiment used \(15{,}000\) paths.

| Steps | \(h\) | Mean terminal absolute error | Monte Carlo SE |
|---:|---:|---:|---:|
| 16 | 0.0781250 | \(1.4986753\times10^{-1}\) | \(1.15\times10^{-3}\) |
| 32 | 0.0390625 | \(1.0650886\times10^{-1}\) | \(7.78\times10^{-4}\) |
| 64 | 0.0195312 | \(7.5144605\times10^{-2}\) | \(5.45\times10^{-4}\) |
| 128 | 0.0097656 | \(5.2677443\times10^{-2}\) | \(3.68\times10^{-4}\) |
| 256 | 0.0048828 | \(3.7240809\times10^{-2}\) | \(2.56\times10^{-4}\) |
| 512 | 0.0024414 | \(2.6345962\times10^{-2}\) | \(1.84\times10^{-4}\) |

The fitted log-log slope was

\[
\boxed{0.5029,}
\]

matching the expected strong order \(1/2\).

## 7. General nonlinear image

For the example

\[
F(x)=x+i(0.30x^2+0.20x)
\]

at \(x=0.70\), the derivative vector is

\[
F'(x)=(1,0.62).
\]

The computed covariance was

\[
\begin{pmatrix}
0.422500&0.261950\\
0.261950&0.162409
\end{pmatrix},
\]

with eigenvalues

\[
0,\qquad0.584909
\]

and determinant

\[
7.058\times10^{-18}.
\]

The numerical result matches the exact outer-product rank theorem.

## 8. Tanaka local time

For standard Brownian motion over \(T=1.25\),

\[
\mathbb E[L_T^0]
=\sqrt{\frac{2T}{\pi}}
=0.8920621.
\]

Each resolution used \(12{,}000\) paths. The discrete crossing residual
satisfied the exact grid Tanaka identity pathwise.

| Steps | \(\varepsilon\) | Mean discrete local time | \(z\)-score | Mean occupation estimator | Occupation error |
|---:|---:|---:|---:|---:|---:|
| 128 | 0.15718 | 0.8911254 | -0.151 | 0.8242986 | -0.0678 |
| 512 | 0.11114 | 0.8943396 | 0.371 | 0.8454725 | -0.0466 |
| 2048 | 0.07859 | 0.8878201 | -0.686 | 0.8511989 | -0.0409 |
| 8192 | 0.05557 | 0.9001265 | 1.298 | 0.8714687 | -0.0206 |

The maximum discrete-identity residual at the finest resolution was

\[
3.02\times10^{-14}.
\]

The occupation-density bias decreased from \(0.0678\) to \(0.0206\) as
\(h\) and \(\varepsilon\) were reduced. This supports the limiting
occupation-density interpretation while keeping it distinct from the exact
discrete identity.

## 9. What the simulations establish

The numerical evidence confirms:

- the logarithmic-spiral map is pathwise invertible through its radius;
- its finite-step multiplicative walk is exact;
- its analytic moments follow from one Gaussian driver;
- its polar covariance is rank one even though both coordinates fluctuate;
- planar Brownian motion has rank two under the comparison normalization;
- the induced complex SDE has the predicted Itô drift;
- Euler–Maruyama displays strong order \(1/2\);
- the literal real-axis radius requires a local-time correction at zero.

The covariance-rank theorem and Itô identities are analytic results. Monte
Carlo supports their implementation but is not their proof.
