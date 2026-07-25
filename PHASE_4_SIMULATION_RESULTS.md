# Phase 4 Simulation Results

## 1. Reproducible setup

The executed notebook is:

`notebooks/phase4_coordinate_free_complex_gbm.ipynb`

It was generated from:

`notebooks/build_phase4_coordinate_free_complex_gbm.py`

The reusable formulas are implemented in:

`phase4_model.py`

All simulations used deterministic seeds beginning with `20260724`. The
notebook recorded:

- conda environment: `phase3-paper`;
- Python 3.12.13;
- NumPy 2.5.1;
- SciPy 1.18.0;
- Matplotlib 3.11.1; and
- nbformat 5.10.4.

The main numerical parameters were

\[
\mu=0.08,\qquad
\sigma=0.30,\qquad
\omega=0.70,\qquad
\beta=0.45,
\]

with

\[
\mathcal Z_0=1.7e^{0.35i}.
\]

The complex log and SDE coefficients were

\[
\kappa=0.035+0.70i,
\]

\[
B=0.30+0.45i,
\]

\[
A=-0.02125+0.835i.
\]

The coefficient identity

\[
A-\frac12B^2=\kappa
\]

closed exactly in floating-point arithmetic for these decimal parameters.

## 2. Exact pathwise identities

On one Brownian path over \(T=4\) with 4,000 time steps, the notebook
compared

\[
\mathcal Z_t
=
\mathcal Z_0e^{\kappa t+BW_t}
\]

with independent evaluations of the GBM modulus, unwrapped phase, and exact
multiplicative step.

| Quantity | Maximum absolute error |
|---|---:|
| \(||\mathcal Z_t|-R_t|\) | \(8.882\times10^{-16}\) |
| unwrapped phase | \(4.441\times10^{-16}\) |
| cumulative exact steps versus closed form | \(8.750\times10^{-15}\) |

These errors are at floating-point scale. They support the exact identities

\[
|\mathcal Z_t|
=
|\mathcal Z_0|
e^{(\mu-\sigma^2/2)t+\sigma W_t},
\]

\[
\Theta_t=\Theta_0+\omega t+\beta W_t,
\]

and

\[
\mathcal Z_{n+1}
=
\mathcal Z_n
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)h
+(\sigma+i\beta)\Delta W_n
\right].
\]

## 3. Constant-modulus Itô correction

The stress test set

\[
\mu=\sigma=0,\qquad
\omega=0.8,\qquad
\beta=0.9.
\]

The correct process

\[
\mathcal Z_t
=
\mathcal Z_0e^{i(\omega t+\beta W_t)}
\]

had maximum modulus error

\[
4.441\times10^{-16}.
\]

Its SDE is

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(-\frac12\beta^2+i\omega\right)dt
+i\beta\,dW_t.
\]

For comparison, omitting the real drift
\(-\tfrac12\beta^2\) gives

\[
\widetilde{\mathcal Z}_t
=
\mathcal Z_0
e^{\beta^2t/2+i(\omega t+\beta W_t)}.
\]

The simulated modulus matched its incorrect growth law to
\(3.553\times10^{-15}\). At \(T=4\), the radial growth factor was

\[
5.053090,
\]

equal to \(e^{\beta^2T/2}\). This directly demonstrates that the complex Itô
correction is required for pure stochastic rotation.

## 4. One-driver versus two-driver covariance

Using 250,000 increments of length \(h=0.01\), the theoretical one-driver
log-polar covariance per unit time was

\[
\Sigma_1
=
\begin{pmatrix}
0.09&0.135\\
0.135&0.2025
\end{pmatrix}.
\]

The empirical estimate was

\[
\widehat\Sigma_1
=
\begin{pmatrix}
0.0898792&0.1348188\\
0.1348188&0.2022282
\end{pmatrix},
\]

with eigenvalues

\[
(-1.25\times10^{-16},\,0.2921074).
\]

The numerically negligible negative first eigenvalue is floating-point
roundoff around the exact value zero.

For independent radial and angular Brownian increments, the empirical
covariance was

\[
\widehat\Sigma_2
=
\begin{pmatrix}
0.0898792&-0.0004942\\
-0.0004942&0.2024680
\end{pmatrix},
\]

with eigenvalues

\[
(0.0898770,\,0.2024701).
\]

The experiment confirms:

- one shared driver gives rank one; and
- two independent drivers give rank two when
  \(\sigma\beta\ne0\).

## 5. Monte Carlo moment validation

At \(T=1.5\), 300,000 independent terminal samples were used. Uncertainty was
reported through Monte Carlo standard errors and standardized residuals.

### Second radial moment

\[
\mathbb E[R_T^2]_{\rm MC}=4.1984821,
\]

\[
\mathbb E[R_T^2]_{\rm exact}=4.2049252,
\]

with standard error \(6.479\times10^{-3}\) and standardized residual

\[
z=-0.994.
\]

### Complex mean

\[
\mathbb E[\mathcal Z_T]_{\rm MC}
=
-0.0503968+1.6437556i,
\]

\[
\mathbb E[\mathcal Z_T]_{\rm exact}
=
-0.0521966+1.6458395i.
\]

The real and imaginary standardized residuals were

\[
(0.949,\,-1.770).
\]

### Mixed radial-angular moment

For

\[
\mathbb E\!\left[
R_Te^{i(\Theta_T-\Theta_0)}
\right],
\]

the Monte Carlo estimate was

\[
0.5162989+1.5613801i,
\]

and the exact value was

\[
0.5153227+1.5639549i.
\]

The componentwise standardized residuals were

\[
(0.629,\,-1.605).
\]

All tested moments were within two Monte Carlo standard errors of their exact
values.

## 6. Phase 3 equivalence

The Phase 3 subfamily was imposed with

\[
c=1+i\gamma,\qquad\gamma=0.85,
\]

\[
\beta=\gamma\sigma,
\qquad
\omega=\gamma\left(\mu-\frac12\sigma^2\right).
\]

On the same Brownian path, the maximum difference between

\[
\mathcal Z_t^{(3)}
=
\mathcal Z_0
\exp\!\left[
(1+i\gamma)
\left(
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right)
\right]
\]

and the restricted Phase 4 formula was

\[
6.661\times10^{-16}.
\]

For the general Phase 4 parameter choice, the time-dependent spiral residual

\[
\omega
-
\frac{\beta}{\sigma}
\left(\mu-\frac12\sigma^2\right)
\]

was \(0.647500\), confirming that the unrestricted model is not confined to
the fixed Phase 3 logarithmic spiral.

## 7. Euler--Maruyama strong convergence

Euler--Maruyama was coupled to the exact solution on 3,500 shared fine
Brownian paths. Coarse Brownian increments were obtained by summing the same
fine increments.

| Step size \(h\) | Mean strong terminal error |
|---:|---:|
| \(0.0625\) | \(0.0890496\) |
| \(0.03125\) | \(0.0572328\) |
| \(0.015625\) | \(0.0397036\) |
| \(0.0078125\) | \(0.0274716\) |
| \(0.00390625\) | \(0.0193116\) |

The fitted log-log slope was

\[
0.5469,
\]

consistent with the expected Euler--Maruyama strong order \(1/2\).

The numerical update used the SDE drift

\[
A=\mu-\frac12\beta^2+i(\omega+\sigma\beta),
\]

not the compensated exponent drift \(\kappa\).

## 8. Complex quadratic variation

On a fine grid of 65,536 steps over \(T=1.5\), the realized brackets were
compared with

\[
\int_0^T B^2\mathcal Z_t^2\,dt
\]

and

\[
\int_0^T |B|^2|\mathcal Z_t|^2\,dt.
\]

The relative discrepancies were:

| Bracket | Relative error |
|---|---:|
| bilinear \([\mathcal Z,\mathcal Z]\) | \(0.6998\%\) |
| Hermitian \([\mathcal Z,\overline{\mathcal Z}]\) | \(0.3648\%\) |

The results distinguish the complex square \(B^2\) from the nonnegative
quantity \(|B|^2\).

## 9. Independent two-driver modulus

The comparator

\[
\mathcal Z_t^{(2)}
=
\mathcal Z_0
\exp\!\left[
\left(\mu-\frac12\sigma^2+i\omega\right)t
+\sigma W_t^{(r)}
+i\beta W_t^{(\theta)}
\right]
\]

used independent Brownian paths. Its modulus agreed with the same direct GBM
reference to

\[
8.882\times10^{-16}.
\]

This confirms that an independent angular driver can be added without
changing the radius, but it is a different, rank-two model.

## 10. Reproducibility and test evidence

The computational core was developed test-first. The initial test run failed
because `phase4_model` did not yet exist; the next red runs exposed the
unimplemented coefficient, exact-path, covariance, moment, bracket, and
two-driver behaviors before each implementation slice was added. The retained
test docstrings name the regression guarded by every test. The final command

```bash
conda run -n phase3-paper \
  python -m unittest discover -s tests -v
```

ran 10 tests successfully.

The notebook was executed twice from clean kernels through the approved
external execution boundary required by the managed workspace:

```bash
conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute --inplace \
  notebooks/phase4_coordinate_free_complex_gbm.ipynb

conda run -n phase3-paper jupyter nbconvert \
  --to notebook --execute \
  --output phase4_coordinate_free_complex_gbm_recheck.ipynb \
  --output-dir /tmp \
  notebooks/phase4_coordinate_free_complex_gbm.ipynb
```

Both runs had 12 code cells, sequential execution counts from 1 through 12,
zero error outputs, and identical deterministic text outputs. The SHA-256
hash over the concatenated code-cell source text was

`472c9b098777eaafda1bee99fa5b9869fb69809f0753b86fbecc81f3ec6c312f`

and the SHA-256 hash over the concatenated stream-output text was

`2db5cedc09452515912716602a2b8d79266760d8b7cfebe7573cf7da103e1ebf`.

Pandoc 3.8 rendered the Phase 4 plan, literature review, three derivation
chapters, simulation record, and synthesis to temporary HTML files without a
fatal parse error. `git diff --check` also completed successfully.

## 11. Computational conclusion

The executed notebook verified every primary Phase 4 claim:

- exact GBM modulus;
- exact unwrapped phase;
- exact multiplicative step;
- required complex Itô corrections;
- constant-modulus stochastic rotation;
- rank-one shared-driver covariance;
- rank-two independent-driver boundary;
- analytic moments within Monte Carlo uncertainty;
- Phase 3 as a constrained special case;
- Euler--Maruyama strong order near \(1/2\); and
- both complex quadratic-variation formulas.

The numerical experiments support the derivations; they do not replace the
proofs in `13_`–`15_`.
