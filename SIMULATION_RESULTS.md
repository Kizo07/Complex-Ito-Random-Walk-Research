# Reproducible Numerical Results

## Execution record

The notebook
[`notebooks/ito_complex_bridge.ipynb`](notebooks/ito_complex_bridge.ipynb)
was executed from top to bottom on 2026-07-23 in the existing `base` conda
environment:

- Python 3.13.9
- NumPy 2.3.5
- Matplotlib 3.10.6
- IPython 9.7.0
- ipykernel 6.31.0

All simulations use section-specific deterministic seeds. A second execution
to a temporary notebook reproduced every numerical output exactly. The only
difference was a one-time, nonnumerical Fontconfig warning.

The execution command was

```bash
conda run -n base jupyter nbconvert \
  --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=300 \
  notebooks/ito_complex_bridge.ipynb
```

## 1. Quadratic variation

For \(T=1\), 12,000 paths, and \(N\) equal increments:

| \(N\) | empirical mean | empirical variance | exact mean | exact variance \(2/N\) |
|---:|---:|---:|---:|---:|
| 16 | 0.995695 | 0.125839 | 1 | 0.125000 |
| 64 | 1.003809 | 0.031230 | 1 | 0.031250 |
| 256 | 0.999453 | 0.007599 | 1 | 0.007812 |
| 1024 | 1.000604 | 0.001972 | 1 | 0.001953 |

This checks the precise content of \((dW)^2=dt\): an individual normalized
square remains random, while the accumulated squared increments concentrate.

## 2. Arithmetic diffusion

For \(X_0=0.3\), \(\mu=0.5\), \(\sigma=0.8\), \(T=1\), and 200,000 terminal
samples:

| quantity | empirical | theory | standardized error |
|---|---:|---:|---:|
| mean | 0.801534 | 0.800000 | 0.858 |
| variance | 0.640235 | 0.640000 | 0.116 |

The standardized errors use the exact Monte Carlo standard errors for normal
data.

## 3. Stochastic exponential

For geometric Brownian motion with \(S_0=1.3\), \(\mu=0.2\),
\(\sigma=0.7\), and \(T=1\), 200,000 exact terminal samples gave

\[
\widehat{\mathbb E[S_T]}=1.587666,
\qquad
\mathbb E[S_T]=1.587824.
\]

Coupled Euler–Maruyama and exact solutions, driven by the same Brownian
increments, produced:

| \(N\) | \(\Delta t\) | mean absolute error | root mean square error |
|---:|---:|---:|---:|
| 16 | 0.0625000 | 0.1101493 | 0.1767281 |
| 64 | 0.0156250 | 0.0545096 | 0.0860046 |
| 256 | 0.0039062 | 0.0272612 | 0.0436000 |
| 1024 | 0.0009766 | 0.0138720 | 0.0223796 |

The fitted log-log slopes were 0.498 for mean absolute error and 0.496 for
root mean square error, matching Euler–Maruyama's strong order \(1/2\).

## 4. Stochastic rotation

For \(r_0=1\), \(\beta=1.1\), \(T=1\), 30,000 paths, and 400 steps:

- the exact phase update preserved radius to \(4.8\times10^{-15}\);
- correct Itô Euler–Maruyama gave terminal
  \(\widehat{\mathbb E|Z_T|^2}=1.000402\), versus its finite-grid value
  \(1.000915\);
- omitting the drift \(-\beta^2Z/2\) gave
  \(\widehat{\mathbb E|Z_T|^2}=3.345654\), versus its finite-grid value
  \(3.347365\);
- the wrong SDE's predicted exact radius is
  \(e^{\beta^2T/2}=1.831252\), while the simulated terminal mean radius was
  \(1.827472\).

This is the most visually decisive experiment: the Itô correction is what
keeps the limiting phase process on the circle.

## 5. Planar Brownian polar rates

For Cartesian volatility \(\sigma=0.6\), step \(10^{-3}\), and 600,000 local
samples per starting radius:

| \(r_0\) | radial drift: empirical / theory | radial variance rate: empirical / theory | angular variance rate: empirical / theory |
|---:|---:|---:|---:|
| 0.5 | 0.4127 / 0.3600 | 0.3599 / 0.3600 | 1.4405 / 1.4400 |
| 1.0 | 0.2069 / 0.1800 | 0.3596 / 0.3600 | 0.3603 / 0.3600 |
| 2.0 | 0.0942 / 0.0900 | 0.3587 / 0.3600 | 0.0899 / 0.0900 |

The drift is estimated from a mean increment of order \(dt\) in the presence
of noise of order \(\sqrt{dt}\), so it is statistically much harder to
estimate than the two variance rates. The drift discrepancies are at most
about 2.2 Monte Carlo standard errors; the variance rates closely match
\(\sigma^2\) and \(\sigma^2/r_0^2\).

## Verification boundary

These simulations test analytical consequences and implementation failure
modes. They do not prove the formulas. The proofs are in the numbered notes,
and every deterministic sanity assertion at the end of the notebook passed
on both executions.
