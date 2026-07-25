# Phase 5 numerical implications

## 1. Verdict

The one-phase representation is numerically exact as a coordinate change,
but it is not uniformly faster, more accurate, or more solvable than the
original scalar diffusion. The experiments establish three narrower
benefits:

1. exact transformed-Gaussian steps preserve the phase domain and transformed
   invariants;
2. arctangent compactification can improve resolution on a chosen central
   region of an unbounded-domain PDE; and
3. the coordinate gives a useful test problem for nonlinear SDE integrators.

They also establish three negative results:

1. a lossless phase round trip cannot reduce ordinary Monte Carlo variance;
2. direct phase simulation is harder than direct arithmetic Brownian
   simulation unless the exact inverse transform is exploited; and
3. compactification can worsen matrix conditioning and depends materially on
   its scale parameter.

All reported values come from the executed notebook
[notebooks/phase5_one_phase_euler.ipynb](notebooks/phase5_one_phase_euler.ipynb)
and the structured files under
[phase5_evidence](phase5_evidence).

## 2. Exact simulation versus numerical integration

For the canonical phase,

\[
\theta_t=\arctan(Y_t/c),\qquad
dY_t=\mu\,dt+\sigma\,dW_t,
\]

the exact step is

\[
\theta_{n+1}
=
\arctan\left(
\tan\theta_n+\frac{\mu h}{c}
+\frac{\sigma\sqrt h}{c}\xi_n
\right),
\qquad \xi_n\sim N(0,1).
\]

This is not a new exact-simulation method for arithmetic Brownian motion. It
is the known Gaussian update conjugated by a diffeomorphism. Nevertheless, it
is the correct numerical reference for the nonlinear phase SDE.

### 2.1 Direct phase-SDE convergence

Euler--Maruyama, Milstein, and Stratonovich--Heun were advanced directly from
the nonlinear phase coefficients on shared Brownian increments. The exact
arctangent appeared only in the endpoint reference. With 4,000 paths,
\(T=1\), and step counts \(32,\ldots,512\), the fitted strong slopes were:

| Method | Base seed slope | Second seed slope | Finest-step RMSE, base | Finest-step RMSE, second |
|---|---:|---:|---:|---:|
| Euler--Maruyama | 0.495 | 0.511 | \(5.55\times10^{-3}\) | \(5.47\times10^{-3}\) |
| Milstein | 1.008 | 1.013 | \(3.49\times10^{-4}\) | \(3.44\times10^{-4}\) |
| Stratonovich--Heun | 1.004 | 1.004 | \(2.66\times10^{-4}\) | \(2.62\times10^{-4}\) |

These are the expected strong orders \(1/2\) and \(1\). The independent seed
family reproduces the conclusion. Full errors and RMSE standard errors are in
[phase_sde_convergence.csv](phase5_evidence/phase_sde_convergence.csv) and
[second_seed_replication.csv](phase5_evidence/second_seed_replication.csv).

The experiment validates the independently derived SDE coefficients. It does
not prove them; the proof is the two-way Itô calculation in
[PHASE_5_MATHEMATICAL_FOUNDATIONS.md](PHASE_5_MATHEMATICAL_FOUNDATIONS.md).

### 2.2 Boundary stress

The exact phase lives on
\((-\pi/2,\pi/2)\), whose endpoints are natural and inaccessible. A single
unconstrained Euler step can leave that interval. For \(c=0.25\),
\(\sigma=1\), and 120,000 samples, its observed violation rates were:

| \(h\) | Exact transformed step | Euler step |
|---:|---:|---:|
| 0.25 | 0 | 0.431 |
| 0.125 | 0 | 0.266 |
| 0.0625 | 0 | 0.116 |
| 0.03125 | 0 | 0.0255 |

The zeros in the exact-step column hold by construction, not by favorable
sampling: the principal \(\arctan\) maps every finite transformed state into
\((-\pi/2,\pi/2)\). The experiment measures how often the unconstrained Euler
control loses that invariant.

See [boundary_stress.csv](phase5_evidence/boundary_stress.csv). This is a
real numerical advantage of exact transformed steps or a domain-preserving
scheme. It is also a warning: bounded coordinates do not make a naive
discretization automatically safe.

## 3. Distribution, generator, and semigroup checks

The exact density is a Gaussian change of variables. Independent numerical
checks found:

- density mass \(0.9999999999999999\);
- Chapman--Kolmogorov absolute error \(1.11\times10^{-16}\);
- probability-integral-transform KS statistic \(0.00235\) with
  \(p=0.337\);
- signed diffusion parameter \(\sigma=-0.9\), confirming orientation does not
  change the law; and
- Fokker--Planck relative RMS residual \(6.90\times10^{-5}\) on the interior
  finite-difference grid.

See
[distribution_summary.json](phase5_evidence/distribution_summary.json) and
[fokker_planck_residual.json](phase5_evidence/fokker_planck_residual.json).

Small-time empirical drift and variance approach the generator coefficients
within finite-\(h\) bias and the reported Monte Carlo standard errors. Those
uncertainties are preserved in
[small_time_generator_checks.csv](phase5_evidence/small_time_generator_checks.csv).

The endpoint-tail experiment also records exact binomial upper confidence
bounds. Zero observed events at extremely small probabilities is not treated
as evidence that the true probability is zero; see
[endpoint_tails.csv](phase5_evidence/endpoint_tails.csv).

## 4. Cayley invariant preservation

For

\[
U=\frac{1+iY/c}{1-iY/c},
\]

the exact map stays on the unit circle to machine precision. On the tested
path:

- exact maximum modulus error:
  \(3.33\times10^{-16}\);
- inverse reconstruction error:
  \(4.44\times10^{-16}\);
- unconstrained complex Euler maximum modulus error:
  \(0.718\).

See [cayley_invariants.csv](phase5_evidence/cayley_invariants.csv).

This supports using the exact transform or a geometric integrator when unit
modulus of the transformed state matters. It does not imply that the Cayley
phase is ordinary circular Brownian motion; its diffusion coefficient is
state dependent and tends to zero at the missing point.

## 5. Compactified heat-equation benchmark

The transformation

\[
x=c\tan\theta
\]

conjugates the heat generator on an unbounded coordinate to a
variable-coefficient generator on a bounded interval. The notebook solved

\[
\partial_tu=\frac12\partial_{xx}u,\qquad
u(0,x)=e^{-x^2},
\]

at \(T=0.35\), truncating the physical domain at \([-8,8]\). Direct-\(x\) and
phase grids used the same total number of points. Errors were compared on the
same physical region \(|x|\le4\).

At 161 grid points:

| Coordinate | Map scale | Maximum error | RMS error | Condition proxy |
|---|---:|---:|---:|---:|
| direct \(x\) | — | \(4.65\times10^{-4}\) | \(1.78\times10^{-4}\) | 1.70 |
| phase | 0.5 | \(1.99\times10^{-4}\) | \(6.04\times10^{-5}\) | 78.8 |
| phase | 1 | \(5.98\times10^{-5}\) | \(2.28\times10^{-5}\) | 22.1 |
| phase | 2 | \(4.07\times10^{-5}\) | \(2.55\times10^{-5}\) | 7.30 |

The best mapped maximum error was about 11.4 times smaller than the direct
grid error at this fixed degree of freedom. The price was a condition proxy
about 4.3 times larger even for the best-conditioned mapped case; smaller
\(c\) became much worse conditioned. The same qualitative pattern occurred
at 41 and 81 points. Full results are in
[pde_compactification.csv](phase5_evidence/pde_compactification.csv).

The correct conclusion is conditional:

> Arctangent compactification can allocate more points to a region of
> interest and improve a particular discretization, but its scale must be
> tuned and bounded coordinates do not guarantee better conditioning.

This benchmark does not produce a new analytic heat solution. The
transformed solution is the original solution composed with
\(x=c\tan\theta\).

## 6. Monte Carlo, quasi-Monte Carlo, and rare events

Let \(X_T\) be sampled and set

\[
\theta_T=\arctan(X_T/c),\qquad
X_T=c\tan\theta_T.
\]

For any payoff \(g\),

\[
g(X_T)=g(c\tan\theta_T)
\]

sample by sample. Therefore, under the same random numbers:

\[
\widehat V_X=\widehat V_\theta,\qquad
\operatorname{Var}(\widehat V_X)
=\operatorname{Var}(\widehat V_\theta).
\]

The notebook confirms this identity to machine precision for:

- ordinary Monte Carlo of a Bachelier call;
- scrambled Sobol quasi-Monte Carlo;
- importance sampling of a rare event; and
- two independent Monte Carlo seed families.

The direct and phase ordinary-Monte-Carlo estimates were both
\(0.365562577394\), with sample variance \(0.32424455365\) and standard error
\(0.00111216\). The phase reconstruction and payoff differences were at most
\(2.66\times10^{-15}\). See
[monte_carlo_equivalence.csv](phase5_evidence/monte_carlo_equivalence.csv),
[qmc_equivalence.csv](phase5_evidence/qmc_equivalence.csv),
[rare_event_equivalence.csv](phase5_evidence/rare_event_equivalence.csv), and
[monte_carlo_seed_replication.csv](phase5_evidence/monte_carlo_seed_replication.csv).

### 6.1 Work proxy

For a terminal estimator driven by one normal draw, both formulations store
one stochastic scalar. The direct estimator needs no trigonometric
round-trip; the phase route adds one arctangent and one tangent evaluation.
This deterministic work proxy is recorded in
[computational_work_proxy.csv](phase5_evidence/computational_work_proxy.csv).

Wall-clock microbenchmarks were intentionally not used as primary evidence
because they are hardware-, load-, and implementation-dependent and would
break byte-level evidence reproducibility. For this elementary terminal
payoff, the operation count already proves there is no direct-work advantage.

Variance reduction remains possible only if the transformation enables a
different proposal, control variate, smoothing, stratification, or numerical
solver. It does not follow from lossless reparameterization alone.

### 6.2 Terminal phase does not summarize path history

A terminal phase exactly determines the terminal scalar state, not the
intermediate path. In the barrier-payoff control, the mean conditional
variance of the path payoff within terminal-phase bins was \(0.0561\).
The full phase path and full scalar path are equivalent, but
\(\theta_T\) alone cannot replace a path-dependent statistic. See
[monte_carlo_summary.json](phase5_evidence/monte_carlo_summary.json).

## 7. Complex derivatives and numerical differentiation

The complex-step derivative benchmark accurately reproduces the known
small-\(h\) stability of complex-step differentiation for an analytic
function. It is not a numerical consequence of the Brownian phase embedding.
A payoff restricted to a curve does not automatically possess the analytic
extension required by the method.

Accordingly:

- complex-step differentiation is useful when its own analyticity assumptions
  hold;
- Wirtinger derivatives are useful for nonholomorphic functions of
  \((z,\bar z)\);
- neither method turns an arbitrary stochastic payoff into a complex-analytic
  one.

See
[PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md](PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md)
for the derivative obstruction.

## 8. Did a numerical-only problem become analytic?

No benchmark crossed that threshold.

The exact phase transition, density, generator, semigroup, and transformed
heat solution are inherited from the exactly solvable arithmetic Brownian
model. The phase coordinate exposes and repackages those solutions; it does
not solve a previously unsolved diffusion.

The most defensible numerical contribution is instead:

\[
\boxed{
\text{a tunable compactification and invariant-aware coordinate, whose
benefit must be measured problem by problem.}
}
\]

## 9. Reproducibility statement

The notebook uses:

- base seed \(20260724\);
- disjoint second seed \(20360724\);
- explicit independent generators for Monte Carlo experiments;
- an explicit seed for SciPy routines that use NumPy's legacy RNG;
- shared streams within method comparisons; and
- fixed software versions and experiment parameters.

After the final review corrections, it executed three times from clean
kernels with 18 sequential code-cell counts and zero error outputs. Every
structured evidence file was byte-identical across all three executions. The
aggregate digest below is reproducible by sorting the 33 evidence basenames
lexicographically, writing each standard
`<SHA-256><two spaces><basename><newline>` record, and hashing that record
stream:

```text
fa8fd5f517c9f321f3426cfdbd5fe2e9f8bea4e213ad945a8207a87a9736619e
```

Two consecutive unexecuted notebook builds were also byte-identical, with
SHA-256
`105201af9508a908f3466cb4e2ed73ede08a476baa60420c70bd137ce0580576`.
The executed notebook's normalized cell-source hash was
`5dd4f3ddb420c8e69e8f2ad4c344b15cbe837c2b63c402a5aa1082cefeefe61d`.

The environment and parameter manifests are
[software_versions.csv](phase5_evidence/software_versions.csv) and
[experiment_parameters.json](phase5_evidence/experiment_parameters.json).

## 10. Numerical decision table

| Claim | Decision |
|---|---|
| The nonlinear phase SDE is numerically consistent with the exact transform. | Supported. |
| Exact phase steps preserve the natural interval. | Supported. |
| Naive Euler automatically respects the bounded phase domain. | Refuted. |
| Cayley coordinates can preserve unit modulus exactly. | Supported for the transformed state. |
| The phase route lowers ordinary Monte Carlo variance by itself. | Refuted. |
| The phase route lowers direct terminal-estimator work. | Refuted. |
| Compactification can improve fixed-grid accuracy in a chosen physical region. | Supported in the benchmark. |
| Compactification always improves conditioning or accuracy. | Refuted. |
| The coordinate solves a previously numerical-only stochastic problem analytically. | Not supported. |

## 11. Final numerical implication

The phase coordinate is a mathematically controlled change of variables, not
a universal solver. Its strongest uses are exact transformed sampling,
constraint-preserving state representation, and tunable treatment of
unbounded domains. Any broader claim must be attached to a specified model,
algorithm, error metric, conditioning metric, and computational budget.
