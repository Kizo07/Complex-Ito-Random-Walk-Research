# Phase 2 Simulation Results

## Reproducibility

Notebook:

`notebooks/phase2_stochastic_radius.ipynb`

Builder:

`notebooks/build_phase2_notebook.py`

Environment:

- conda environment: `base`
- Python: 3.13.9
- NumPy: 2.3.5
- SciPy: 1.16.3
- Matplotlib: 3.10.6
- nbformat: 5.10.4

Primary execution command:

```text
conda run -n base jupyter nbconvert --to notebook --execute --inplace \
  --ExecutePreprocessor.timeout=300 \
  notebooks/phase2_stochastic_radius.ipynb
```

Independent clean-kernel recheck:

```text
conda run -n base jupyter nbconvert --to notebook --execute \
  --ExecutePreprocessor.timeout=300 \
  --output phase2_stochastic_radius_recheck.ipynb \
  --output-dir /tmp \
  notebooks/phase2_stochastic_radius.ipynb
```

All random-number generators use deterministic seeds derived from
`20260723`. The notebook passed both clean executions with no cell errors; all
embedded assertions passed, and the eight saved text-output streams were
identical between executions.

## 1. Complex self-QV versus Euclidean QV

The experiment used

\[
\Delta Z=\sigma\sqrt h(\xi+i\eta),
\qquad
\sigma=0.7,\quad T=1.
\]

The Euclidean quadratic-variation target was

\[
2\sigma^2T=0.98.
\]

| \(N\) | paths | mean \(\operatorname{Re}\sum(\Delta Z)^2\) | mean \(\operatorname{Im}\sum(\Delta Z)^2\) | mean \(\sum|\Delta Z|^2\) |
|---:|---:|---:|---:|---:|
| 64 | 30,000 | 0.000955 | 0.000671 | 0.979869 |
| 256 | 20,000 | -0.000096 | 0.000065 | 0.979682 |
| 1,024 | 10,000 | 0.000211 | -0.000377 | 0.979403 |
| 4,096 | 5,000 | 0.000331 | -0.000348 | 0.979940 |

The observed log-log slope of the RMS complex self-QV against \(N\) was

\[
-0.5010,
\]

matching the exact finite-grid prediction \(-1/2\).

The sample variance ratios to their analytic finite-grid values stayed
between approximately \(0.978\) and \(1.011\).

Conclusion:

\[
\sum(\Delta Z)^2\to0
\]

while

\[
\sum|\Delta Z|^2\to0.98.
\]

The isotropic cancellation is numerically clear.

## 2. Terminal stochastic radius

Parameters:

\[
Z_0=1+0.4i,\qquad
\sigma=0.65,\qquad
T=1.2,
\]

with 150,000 terminal samples.

The Rice parameters were

\[
b=1.512603,\qquad
\text{scale}=0.712039.
\]

Results:

| Quantity | Monte Carlo | Theory | standardized discrepancy |
|---|---:|---:|---:|
| \(\mathbb E R_T\) | 1.341791 | 1.341644 | 0.093 |
| \(\operatorname{Var}(R_T)\) | 0.376195 | 0.373992 | — |
| \(\mathbb E R_T^2\) | 2.176596 | 2.174000 | 0.544 |

The Kolmogorov–Smirnov statistic against the Rice distribution was

\[
0.001589,
\]

with \(p=0.8428\). The standard reference scale
\(1.36/\sqrt M\) was \(0.003512\).

This confirms that the Phase 2 radius is genuinely stochastic and has the
correct planar-Brownian terminal distribution.

## 3. Pathwise Cartesian-polar reconstruction

For a 20,000-step planar Brownian path:

- minimum displayed radius: \(1.609401\);
- maximum error in
  \(R_te^{i\Theta_t}-Z_t\): \(4.578\times10^{-16}\);
- adapted Brownian grid quadratic variations:
  \[
  \sum(\Delta B^R)^2=0.986288,
  \]
  \[
  \sum(\Delta B^\Theta)^2=1.015184,
  \]
  \[
  \sum\Delta B^R\Delta B^\Theta=-0.008828.
  \]

The last three values are consistent with two orthogonal Brownian drivers
over a unit horizon.

## 4. Random angular and log-radial clock

Stopped simulations compared the discrete quadratic variations of
\(\Theta\) and \(\log R\) with

\[
H_T=\int_0^T\frac{\sigma^2}{R_t^2}dt.
\]

| \(N\) | retained paths | mean \(\mathrm{QV}(\Theta)/H\) | mean \(\mathrm{QV}(\log R)/H\) | mean cross-QV/\(H\) |
|---:|---:|---:|---:|---:|
| 250 | 11,987 | 0.998829 | 0.999173 | -0.000476 |
| 1,000 | 7,989 | 0.998888 | 1.000073 | -0.000222 |
| 4,000 | 3,992 | 0.999991 | 0.999818 | -0.000467 |

This verifies:

\[
d[\log R]_t=d[\Theta]_t
=\frac{\sigma^2}{R_t^2}dt,
\qquad
d[\log R,\Theta]_t=0.
\]

The same paths were binned by current radius to test the local angular
variance rate directly:

| mean radius | observed angular variance rate | predicted mean \(\sigma^2/R^2\) |
|---:|---:|---:|
| 0.56349 | 0.822970 | 0.822799 |
| 0.79957 | 0.399457 | 0.400483 |
| 1.02230 | 0.242540 | 0.242449 |
| 1.25474 | 0.160382 | 0.160266 |
| 1.51205 | 0.110122 | 0.110259 |
| 1.81369 | 0.076857 | 0.076585 |

The observed rate near the smallest-radius bin was more than ten times the
rate in the largest-radius bin. This directly demonstrates accelerated
winding near the origin.

The second bin's observed and predicted rates differ by only \(0.26\%\). Its
nominal \(z=-3.093\) is amplified by the very large number of retained
increments and by a simple standard-error calculation that does not model
within-path dependence; it is not evidence against the \(1/R^2\) law.

## 5. Bessel radial drift

The conditional prediction

\[
\mathbb E[dR_t\mid R_t]
=\frac{\sigma^2}{2R_t}dt
\]

was tested by binning more than 14 million retained increments. Across the
six radial bins, observed-minus-predicted discrepancies ranged from
\(-0.924\) to \(1.131\) Monte Carlo standard errors.

Examples:

| mean radius | observed drift rate | predicted drift rate | standardized discrepancy |
|---:|---:|---:|---:|
| 0.56349 | 0.249659 | 0.225011 | 1.131 |
| 1.02230 | 0.123414 | 0.122822 | 0.080 |
| 1.51205 | 0.088959 | 0.082901 | 0.346 |

The conditional-increment experiment supports the Bessel drift formula.

## 6. Isotropic stochastic-logarithm convergence

The reconstruction compared:

\[
L_N^{(1)}=\sum_n\frac{\Delta Z_n}{Z_n}
\]

with

\[
L_N^{(2)}
=\sum_n\left[
\frac{\Delta Z_n}{Z_n}
-\frac12\left(\frac{\Delta Z_n}{Z_n}\right)^2
\right].
\]

| \(N\) | mean error from \(e^{L_N^{(1)}}\) | mean error from \(e^{L_N^{(2)}}\) |
|---:|---:|---:|
| 64 | 0.0062879 | 0.0002620 |
| 256 | 0.0031901 | 0.0000669 |
| 1,024 | 0.0015850 | 0.0000165 |
| 4,096 | 0.0007851 | 0.0000042 |

The slopes against \(h\) were:

\[
0.5007
\quad\text{for the first-order Itô sum,}
\]

\[
0.9949
\quad\text{for the second-order finite-grid logarithm.}
\]

The exact continuously unwrapped logarithmic product reconstructed the
endpoint to approximately \(10^{-14}\).

The first-order sum converges because the limiting complex self-QV is zero.
The realized second-order term still improves finite-grid accuracy.

## 7. Anisotropic counterexample

Parameters:

\[
\sigma_x=0.65,\qquad
\sigma_y=0.25,\qquad
T=0.8.
\]

The theoretical complex self-QV was

\[
[Z,Z]_T
=(\sigma_x^2-\sigma_y^2)T
=0.288.
\]

At \(N=4096\), its empirical mean was

\[
0.288231,
\]

a discrepancy of \(1.707\) Monte Carlo standard errors.

Reconstruction errors:

| \(N\) | uncorrected | realized Taylor correction | Itô compensator |
|---:|---:|---:|---:|
| 64 | 0.0367731 | 0.0004684 | 0.0076642 |
| 256 | 0.0366605 | 0.0001181 | 0.0038425 |
| 1,024 | 0.0365787 | 0.0000303 | 0.0019198 |
| 4,096 | 0.0365905 | 0.0000077 | 0.0009424 |

The uncorrected error does not decrease. The realized second-order
logarithm converged with slope \(0.9864\), and the continuous Itô compensator
converged with slope \(0.5036\).

This is the controlled failure case:

\[
Z_t\ne Z_0\exp\!\left(\int_0^t\frac{dZ_s}{Z_s}\right)
\]

under anisotropic noise. The correct formula is

\[
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{dZ_s}{Z_s}
-\frac12\int_0^t\frac{d[Z,Z]_s}{Z_s^2}
\right].
\]

## 8. Numerical conclusion

Every Phase 2 numerical acceptance criterion was met:

- stochastic radius verified;
- Rice law verified;
- Cartesian-polar reconstruction at floating-point precision;
- Bessel drift supported by conditional increments;
- shared angular/log-radial clock verified;
- isotropic complex self-QV cancellation verified;
- stochastic-logarithm convergence verified;
- anisotropic correction shown to be essential.
