# Phase 5 simulation and verification results

## 1. Purpose

The Phase 5 computation was designed to answer four different questions
without conflating them:

1. Do the algebraic phase formulas reconstruct the intended process?
2. Do independently integrated nonlinear phase SDEs converge to the exact
   transformed process?
3. Do the derived density, generator, semigroup, and boundary statements agree
   with independent numerical checks?
4. Do the coordinates provide measurable vector, derivative, PDE, or Monte
   Carlo benefits against matched controls?

Proofs remain primary. Simulation is used for reconstruction, error detection,
stress testing, and quantitative comparison.

## 2. Reproducible implementation

The implementation consists of:

- [phase5_model.py](phase5_model.py), the focused mathematical model;
- [tests/test_phase5_model.py](tests/test_phase5_model.py), the Phase 5 unit
  tests;
- [notebooks/build_phase5_one_phase_euler.py](notebooks/build_phase5_one_phase_euler.py),
  the deterministic notebook builder;
- [notebooks/phase5_one_phase_euler.ipynb](notebooks/phase5_one_phase_euler.ipynb),
  the executed 19-section notebook;
- [phase5_evidence](phase5_evidence), structured CSV and JSON evidence; and
- [phase5_figures](phase5_figures), 18 raster and 18 vector figures.

The preserved environment used Python 3.12.13, NumPy 2.5.1, SciPy 1.18.0,
pandas 3.0.3, Matplotlib 3.11.1, and nbformat 5.10.4. No package was installed
or upgraded during Phase 5.

### 2.1 Test-first record

Before `phase5_model.py` existed, the new Phase 5 suite failed with:

```text
ModuleNotFoundError: No module named 'phase5_model'
```

After implementation:

- all 23 Phase 5 tests passed; and
- all 33 project tests passed.

The final verification commands and outputs are recorded in
[the TASK-007 verification ledger](.agent/evidence/TASK-007-verification.md)
and the independent-review record.

### 2.2 Seed design

The primary seed family is \(20260724\); a disjoint replication family uses
\(20360724\). Each experiment uses a documented offset and an independent
NumPy generator. Comparisons between numerical methods use shared streams.
SciPy's sparse matrix-exponential estimator uses NumPy's legacy RNG
internally, so that generator is explicitly seeded as well.

The complete parameter manifest is
[experiment_parameters.json](phase5_evidence/experiment_parameters.json).

## 3. Exact representation results

### 3.1 Canonical secant representation

For

\[
\mathcal Z=Z_0(1+iY/c),\qquad
\theta=\arctan(Y/c),
\]

the experiment checked

\[
\mathcal Z=Z_0\sec\theta\,e^{i\theta},
\qquad
Y=c\tan\theta
\]

over a wide deterministic state grid. Both the Euler-form reconstruction and
the inverse reconstruction had maximum absolute error
\(1.07\times10^{-14}\). The observed finite grid covered a phase span
\(2.909\), approaching the theoretical limiting span \(\pi\). See
[secant_reconstruction.csv](phase5_evidence/secant_reconstruction.csv).

### 3.2 General eligible affine lines

Six randomly generated eligible oblique lines were tested. Every line
satisfied the proved criterion

\[
a/b\in\mathbb R,\qquad b/Z_0\notin\mathbb R.
\]

Maximum scalar inverse errors ranged from \(2.49\times10^{-14}\) to
\(3.27\times10^{-13}\), and maximum complex reconstruction errors ranged from
\(2.16\times10^{-14}\) to \(5.94\times10^{-13}\). Every exact phase interval
had limiting length \(\pi\). See
[general_affine_reconstruction.csv](phase5_evidence/general_affine_reconstruction.csv).

### 3.3 Support-level obstructions

Randomizing time separates a fixed affine support line from a family of
moving support lines:

| Case | Small covariance eigenvalue | Determinant | Empirical rank |
|---|---:|---:|---:|
| radial line | 0 | 0 | 1 |
| eligible oblique line | 0 | 0 | 1 |
| noncollinear drift/diffusion with random time | 0.0532 | 0.0377 | 2 |

See [support_dimension.csv](phase5_evidence/support_dimension.csv).

The angle-bin diagnostic is only an illustration of the proof. As the number
of angle bins increased from 90 to 1,440, the median conditional radial spread
for the eligible line fell from \(0.0436\) to \(0.00226\). For the
noncollinear process it remained near \(0.403\). See
[angle_bin_spread.csv](phase5_evidence/angle_bin_spread.csv). This empirical
contrast is consistent with radius being a function of phase on one fixed
line and not on the randomized-time planar law.

## 4. Independent phase-SDE integration

The canonical Itô phase SDE was integrated without using the arctangent
closed form inside the numerical update:

\[
d\theta
=
\left[
\frac{\mu}{c}\cos^2\theta
-\frac{\sigma^2}{c^2}\sin\theta\cos^3\theta
\right]dt
+\frac{\sigma}{c}\cos^2\theta\,dW.
\]

With \(T=1\), \(\mu=0.3\), \(\sigma=0.8\), \(c=1.25\), 4,000 paths, and
step counts \(32\) through \(512\):

- Euler--Maruyama had fitted strong slope \(0.495\);
- Milstein had fitted strong slope \(1.008\); and
- Stratonovich--Heun had fitted strong slope \(1.004\).

At 512 steps the RMSE values were \(5.55\times10^{-3}\),
\(3.49\times10^{-4}\), and \(2.66\times10^{-4}\), respectively. Every
RMSE has a recorded sampling standard error. The second seed family produced
slopes \(0.511\), \(1.013\), and \(1.004\), with nearly identical finest-step
RMSE values. See
[phase_sde_convergence.csv](phase5_evidence/phase_sde_convergence.csv) and
[second_seed_replication.csv](phase5_evidence/second_seed_replication.csv).

These orders provide a non-circular check of the nonlinear coefficients and
the Itô/Stratonovich conversion.

### 4.1 Natural-boundary stress

For \(c=0.25,\sigma=1\), exact transformed steps produced zero phase-domain
violations in 120,000 trials at every tested \(h\). A naive one-step Euler
update violated the interval in \(43.1\%\) of trials at \(h=0.25\), falling to
\(2.55\%\) at \(h=0.03125\). See
[boundary_stress.csv](phase5_evidence/boundary_stress.csv).

Exact-step domain preservation holds by construction: the principal
\(\arctan\) maps every finite transformed state into the open phase interval.
Its recorded zeros are therefore an invariant check, while the Euler rates
are empirical discretization failures.

This does not estimate a boundary-hitting probability for the exact
diffusion—the proved probability is zero. It quantifies discretization error
in an unconstrained numerical method.

## 5. Transition law and generator

The signed-\(\sigma\) experiment used \(\sigma=-0.9\). Results were:

- density normalization: \(0.9999999999999999\);
- quadrature error estimate: \(6.57\times10^{-10}\);
- semigroup composition error: \(1.11\times10^{-16}\);
- probability-integral-transform KS statistic: \(0.002354\);
- PIT \(p\)-value: \(0.337\); and
- Fokker--Planck relative RMS residual: \(6.90\times10^{-5}\).

See
[distribution_summary.json](phase5_evidence/distribution_summary.json) and
[fokker_planck_residual.json](phase5_evidence/fokker_planck_residual.json).
The empirical quantile curve is preserved in
[phase_quantiles.csv](phase5_evidence/phase_quantiles.csv).

Small-time conditional means and variances were divided by \(h\) and compared
with the exact local drift and squared diffusion. The finest-\(h\) mean
estimate is noisy at the expected \(h^{-1/2}\) Monte Carlo scale; standard
errors are reported explicitly rather than hiding this effect. The variance
estimates approach the theoretical value \(1.28718\). See
[small_time_generator_checks.csv](phase5_evidence/small_time_generator_checks.csv).

### 5.1 Endpoint tails

The endpoint \(\pi/2\) represents \(+\infty\) in the original coordinate.
At distance \(\epsilon=0.25\), the exact upper-tail probability was
\(3.8947\times10^{-4}\), and 69 of 160,000 samples were observed. At smaller
\(\epsilon\), exact probabilities rapidly became too small for ordinary Monte
Carlo. Zero counts are accompanied by a \(95\%\) Clopper--Pearson upper bound
of \(2.31\times10^{-5}\), not misreported as a zero probability. See
[endpoint_tails.csv](phase5_evidence/endpoint_tails.csv).

## 6. Candidate comparisons

### 6.1 Cayley transform

The exact Cayley transform preserved unit modulus to
\(3.33\times10^{-16}\) and inverted the scalar state to
\(4.44\times10^{-16}\). Direct complex Euler integration of its nonlinear
complex SDE accumulated a maximum modulus error \(0.718\). See
[cayley_invariants.csv](phase5_evidence/cayley_invariants.csv).

This supports exact-transform or geometric integration for the transformed
state. It does not identify the process with ordinary circular Brownian
motion.

### 6.2 Transported addition

The secant transported group law satisfied:

- tangent-addition maximum error \(3.11\times10^{-15}\);
- associativity maximum error \(1.53\times10^{-15}\); and
- inverse maximum error \(0\).

Its RMS difference from ordinary angle addition was \(0.288\), confirming
that it is a transported real group rather than usual rotation. See
[transported_group_checks.csv](phase5_evidence/transported_group_checks.csv).

### 6.3 Additive half-turn and multiplicative winding

The compatible logarithmic-spiral path reconstructed the multiplicative
process to \(2.38\times10^{-15}\). On the tested horizon its unwrapped phase
spanned \(10.23\) radians, or \(1.63\) turns. The additive secant phase spanned
\(2.54\) radians and is theoretically bounded by \(\pi\). See
[spiral_winding.csv](phase5_evidence/spiral_winding.csv).

The experiment illustrates, but does not blur, the model distinction:
unbounded lossless winding is available for a compatible multiplicative
process, not for the original additive affine state.

### 6.4 Rigidity controls

The centered noise-coefficient residuals were:

| Curve | Additive residual | Multiplicative residual |
|---|---:|---:|
| line | \(4.90\times10^{-17}\) | 0.434 |
| logarithmic spiral | 0.510 | \(1.09\times10^{-16}\) |
| arbitrary quadratic-radius curve | 0.325 | 0.144 |

See [rigidity_residuals.csv](phase5_evidence/rigidity_residuals.csv). These
controls agree with the proved line/additive and spiral/multiplicative
classification. They are not substitutes for the drift-complete rigidity
proof.

### 6.5 Moving-line fallback

For a noncollinear process, the explicit time-dependent radius reconstructed
four nonsingular fixed-time support lines with errors between
\(1.04\times10^{-14}\) and \(1.76\times10^{-13}\). At \(t=1\), the line
crossed the origin and the implementation rejected the chart. See
[moving_line_fallback.csv](phase5_evidence/moving_line_fallback.csv).

## 7. Vector and complex-calculus controls

The one-phase tangent covariance had rank one. Planar Brownian terminal
covariance and the one-driver hypoelliptic terminal covariance both had rank
two. The empirical hypoelliptic covariance was within
\(4.18\times10^{-3}\) of its exact matrix. See
[vector_rank_controls.csv](phase5_evidence/vector_rank_controls.csv).

Two real-differentiable extensions agreed exactly on the canonical state line
but had normal derivatives \(0\) and \(1\). The Wirtinger pullback identity
was accurate to \(3.55\times10^{-15}\). See
[complex_derivative_summary.json](phase5_evidence/complex_derivative_summary.json).

These controls refute claims that complex notation creates a second
stochastic dimension or a unique holomorphic derivative.

## 8. Numerical-implication benchmarks

### 8.1 Heat-equation compactification

At 161 matched grid points on the same physical comparison region
\(|x|\le4\):

- direct-\(x\) maximum error was \(4.65\times10^{-4}\);
- phase \(c=2\) maximum error was \(4.07\times10^{-5}\);
- direct condition proxy was \(1.70\); and
- phase \(c=2\) condition proxy was \(7.30\).

Compactification improved central-region accuracy by a factor of about 11.4
in this benchmark but worsened conditioning. At \(c=0.5\), the condition
proxy grew to \(78.8\). See
[pde_compactification.csv](phase5_evidence/pde_compactification.csv).

### 8.2 Monte Carlo equivalence

For a Bachelier call, direct and phase-round-trip estimators had exactly the
same estimate, sample variance, and standard error under shared samples:

\[
\widehat V=0.365562577394,\qquad
s^2=0.32424455365,\qquad
\operatorname{SE}=0.00111216.
\]

The second seed family again produced identical direct and phase estimates.
Scrambled Sobol and importance-sampling estimators also agreed. See
[monte_carlo_equivalence.csv](phase5_evidence/monte_carlo_equivalence.csv),
[monte_carlo_seed_replication.csv](phase5_evidence/monte_carlo_seed_replication.csv),
[qmc_equivalence.csv](phase5_evidence/qmc_equivalence.csv), and
[rare_event_equivalence.csv](phase5_evidence/rare_event_equivalence.csv).

The phase route uses the same random dimension and stored stochastic scalar,
plus an arctangent/tangent round trip. See
[computational_work_proxy.csv](phase5_evidence/computational_work_proxy.csv).

### 8.3 Path dependence

Terminal phase exactly reconstructs terminal state, but not path history. The
mean conditional variance of a barrier payoff within terminal-phase bins was
\(0.0561\). A full phase path is equivalent to a full scalar path; a terminal
phase is not a sufficient statistic for a generic path-dependent payoff. See
[monte_carlo_summary.json](phase5_evidence/monte_carlo_summary.json).

## 9. Explicit negative controls

The notebook includes a standalone register covering:

- radial-line failure;
- randomized-time noncollinear support;
- a one-driver full-rank hypoelliptic law;
- nonunique off-curve derivatives;
- transported versus ordinary angle addition;
- Monte Carlo variance equivalence;
- scale-dependent PDE conditioning;
- state-dependent Cayley angular diffusion; and
- moving-line origin crossing.

See [negative_controls.csv](phase5_evidence/negative_controls.csv). These
controls are essential: they prevent an exact coordinate identity from being
mistaken for a new dimension, topology, derivative theory, or universal
numerical algorithm.

## 10. Reproducibility result

The final notebook has 38 cells, including 18 code cells. After the review
corrections it executed three times from clean kernels with:

- execution counts \(1,2,\ldots,18\);
- zero error outputs;
- byte-identical structured evidence files; and
- aggregate ordered-evidence hash

```text
fa8fd5f517c9f321f3426cfdbd5fe2e9f8bea4e213ad945a8207a87a9736619e
```

The aggregate uses lexicographically ordered basenames and standard
`sha256sum` records, so it is independent of the evidence directory's
absolute path. Two consecutive unexecuted builds were byte-identical with
hash
`105201af9508a908f3466cb4e2ed73ede08a476baa60420c70bd137ce0580576`;
the final executed notebook's normalized cell-source hash is
`5dd4f3ddb420c8e69e8f2ad4c344b15cbe837c2b63c402a5aa1082cefeefe61d`.

The PDF figures are retained for publication-quality inspection but are not
part of the byte-level gate because PDF metadata can be renderer-dependent.
The CSV and JSON evidence is the deterministic comparison target.

## 11. Limitations

1. Reconstruction checks cannot prove identities from which their samples are
   generated; the proofs are separate.
2. Convergence slopes are empirical finite-resolution estimates with recorded
   sampling uncertainty.
3. The heat benchmark is one PDE, one discretization family, and three map
   scales; it supports no universal compactification claim.
4. Timing results are deliberately excluded from deterministic evidence.
   Operation counts and matched degrees of freedom are used instead.
5. Extremely small endpoint probabilities are below ordinary Monte Carlo
   resolution; exact tails and binomial detection limits are both reported.
6. The complex-step demonstration assumes an analytic test function and does
   not transfer automatically to stochastic payoffs.
7. No experiment establishes novelty. The novelty boundary comes from the
   primary-source review.

## 12. Computational conclusion

The simulations support the exact one-phase classification, nonlinear phase
SDE, transition kernel, boundary behavior, Cayley invariant, transported
group law, spiral comparison, and line/spiral rigidity results. They refute
the stronger claims that the coordinate supplies repeated additive rotation,
new stochastic dimension, automatic holomorphic calculus, generic variance
reduction, or universal numerical improvement.
