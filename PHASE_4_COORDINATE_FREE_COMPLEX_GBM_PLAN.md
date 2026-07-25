# Phase 4 Plan: A Coordinate-Free Complex Euler Form for Geometric Brownian Motion

**Status:** Approved
**Implementation status:** Complete under `TASK-005`
**Scope:** Phase 4 only
**Primary objective:** Define a complex geometric Brownian motion directly in exponential form, without first constructing an \(x\)-\(y\) path or mapping an already-defined state process into the complex plane.

## 1. Research question

Can geometric Brownian motion (GBM) be lifted into a genuinely complex Euler-form process in which:

1. the modulus is exactly a real GBM;
2. the imaginary part of the exponent generates rotation;
3. \(dt\) and \(dW_t\) appear together inside one complex stochastic exponent;
4. the central definition contains no Cartesian coordinate processes \(X_t\) and \(Y_t\);
5. the construction does not depend circularly on a pre-existing complex path \(Z_i-Z_0\); and
6. all Itô correction terms and dimensional constraints are explicit?

The preliminary answer is **yes**.

Phase 3 used

\[
\mathcal Z_t=\mathcal Z_0\exp\!\left(c(X_t-X_0)\right),
\]

where the complex process was the image of an external scalar diffusion \(X_t\). Although \(X_t\) was not itself an \(x\)-\(y\) coordinate pair, the concern is valid: the complex object was defined by transforming another state process.

Phase 4 will instead define the complex process natively from one complex log-increment.

## 2. Recommended construction

Let

\[
\mu,\omega\in\mathbb R,\qquad
\sigma,\beta\in\mathbb R,\qquad
\mathcal Z_0\in\mathbb C\setminus\{0\},
\]

and let \(W_t\) be one real Brownian motion. Define the complex log-driver

\[
d\Xi_t
=
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]dt
+(\sigma+i\beta)dW_t,
\qquad \Xi_0=0.
\]

The proposed coordinate-free complex GBM is

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0 e^{\Xi_t}
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
}
\tag{P4.1}
\]

Equivalently, the definition can be written as one stochastic integral inside one exponent:

\[
\boxed{
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left\{
\int_0^t
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]ds
+
\int_0^t(\sigma+i\beta)\,dW_s
\right\}.
}
\tag{P4.2}
\]

There are no \(x\)- and \(y\)-coordinate processes in either definition. The only stochastic primitive is \(W_t\); \(\mathcal Z_0\) supplies the unavoidable initial scale and phase.

### 2.1 Why the modulus is exactly GBM

Writing \(\mathcal Z_t=R_t e^{i\Theta_t}\) only after the definition gives

\[
R_t
=
|\mathcal Z_0|
\exp\!\left[
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t
\right],
\tag{P4.3}
\]

and a continuous, unwrapped phase

\[
\Theta_t
=
\Theta_0+\omega t+\beta W_t.
\tag{P4.4}
\]

Therefore

\[
\boxed{\frac{dR_t}{R_t}=\mu\,dt+\sigma\,dW_t,}
\tag{P4.5}
\]

so the modulus is not merely “GBM-like”: it is exactly a GBM with drift \(\mu\), volatility \(\sigma\), and initial value \(R_0=|\mathcal Z_0|\).

The parameters have distinct roles:

- \(\mu\): GBM drift;
- \(\sigma\): radial/log-amplitude volatility;
- \(\omega\): deterministic angular velocity;
- \(\beta\): stochastic angular volatility.

### 2.2 The corresponding complex Itô SDE

For

\[
\kappa=\left(\mu-\frac12\sigma^2\right)+i\omega,
\qquad
\nu=\sigma+i\beta,
\]

complex Itô calculus gives

\[
d\mathcal Z_t
=
\mathcal Z_t
\left[
\left(\kappa+\frac12\nu^2\right)dt+\nu\,dW_t
\right].
\]

After expansion,

\[
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left[
\mu-\frac12\beta^2+i(\omega+\sigma\beta)
\right]dt
+(\sigma+i\beta)dW_t.
}
\tag{P4.6}
\]

This is the complex multiplicative SDE whose exact solution is (P4.1). The \(\tfrac12\nu^2\) term must be retained; it is the complex Itô correction.

### 2.3 Exact one-step random-walk formula

For \(t_{n+1}-t_n=h\) and independent \(\xi_n\sim N(0,1)\),

\[
\boxed{
\mathcal Z_{n+1}
=
\mathcal Z_n
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]h
+(\sigma+i\beta)\sqrt h\,\xi_n
\right).
}
\tag{P4.7}
\]

This is the discrete formula closest to the requested “one term”: one complex exponential combines the deterministic \(h\) contribution and stochastic \(\sqrt h\,\xi_n\) contribution. No Cartesian update is required.

## 3. Three candidate formulations

### Candidate A: Complex power of a pre-existing real GBM

\[
\mathcal Z_t
=
\mathcal Z_0\left(\frac{S_t}{S_0}\right)^c
=
\mathcal Z_0
\exp\!\left[c\log\!\left(\frac{S_t}{S_0}\right)\right],
\qquad c=\alpha+i\gamma.
\]

**Advantage:** Immediate connection to Phase 3 and to complex powers.
**Limitation:** It still defines \(\mathcal Z_t\) through an already-constructed process \(S_t\), and its radius is \(S_t^\alpha\), not \(S_t\), unless \(\alpha=1\).

### Candidate B: General constant-coefficient complex multiplicative SDE

\[
\frac{d\mathcal Z_t}{\mathcal Z_t}=A\,dt+B\,dW_t,
\qquad A,B\in\mathbb C,
\]

with exact solution

\[
\mathcal Z_t
=
\mathcal Z_0
\exp\!\left[\left(A-\frac12B^2\right)t+BW_t\right].
\]

**Advantage:** Native, coordinate-free, and maximally general for one real driver and constant coefficients.
**Limitation:** Arbitrary \(A\) and \(B\) do not make the modulus a prescribed GBM; the necessary parameter relations are hidden.

### Candidate C: Modulus-preserving complex GBM lift

Use (P4.1), with \(\mu,\sigma\) controlling the GBM modulus and \(\omega,\beta\) controlling rotation.

**Advantage:** Native complex definition, exact GBM modulus, explicit rotation, exact transition formula, and transparent parameter meanings.
**Limitation:** With only one Brownian driver, random radial and angular increments are perfectly coupled.

**Decision:** Candidate C is the recommended Phase 4 model. Candidate B will provide the general theorem, and Candidate A will be retained as a restricted special case connecting Phase 4 to Phase 3.

## 4. Stochastic-exponential interpretation

Phase 4 must distinguish Euler's complex exponential from the Euler--Maruyama numerical method.

For the single complex semimartingale

\[
dY_t=A\,dt+B\,dW_t,
\]

the Doléans stochastic exponential satisfies

\[
\mathcal E(Y)_t
=
\exp\!\left(Y_t-\frac12[Y]_t\right)
=
\exp\!\left[\left(A-\frac12B^2\right)t+BW_t\right].
\]

Thus the proposed process can also be written

\[
\boxed{\mathcal Z_t=\mathcal Z_0\mathcal E(Y)_t,}
\tag{P4.8}
\]

where

\[
A=\mu-\frac12\beta^2+i(\omega+\sigma\beta),
\qquad
B=\sigma+i\beta.
\]

This is the mathematically standard way to package drift and Brownian noise into one multiplicative stochastic object. It does **not** assert that \(dt\) and \(dW_t\) are ordinary algebraic numbers.

## 5. Structural facts to prove

### 5.1 Native construction and non-circularity

- Begin with \(W_t\), the parameters, and \(\mathcal Z_0\), not a pre-existing \(X_t+iY_t\).
- Define \(\mathcal Z_t\) directly by (P4.1).
- Derive real and imaginary coordinates only as optional consequences for plotting.
- Show that \(\mathcal Z_t\neq0\) for all finite \(t\) whenever \(\mathcal Z_0\neq0\).

### 5.2 Exact radial theorem

- Prove (P4.3) directly from the modulus of a complex exponential.
- Apply Itô's lemma to prove (P4.5).
- Independently derive the same radial SDE from the complex SDE (P4.6).
- Verify pathwise reconstruction:

\[
R_t=|\mathcal Z_t|,
\qquad
\mathcal Z_t/R_t=e^{i\Theta_t}.
\]

### 5.3 Angular theorem

- Establish the continuous phase lift (P4.4).
- Separate deterministic rotation \(\omega t\) from stochastic rotation \(\beta W_t\).
- Explain why the principal argument has artificial \(2\pi\) jumps while the unwrapped phase does not.

### 5.4 Quadratic variations and rank

For \(L_t=\log(R_t/R_0)\),

\[
dL_t=\left(\mu-\frac12\sigma^2\right)dt+\sigma dW_t,
\qquad
d\Theta_t=\omega dt+\beta dW_t.
\]

The local covariance is

\[
d
\begin{bmatrix}
[L]_t & [L,\Theta]_t\\
[L,\Theta]_t & [\Theta]_t
\end{bmatrix}
=
\begin{bmatrix}
\sigma^2 & \sigma\beta\\
\sigma\beta & \beta^2
\end{bmatrix}dt.
\tag{P4.9}
\]

Its determinant is zero, so the one-driver process has rank-one local noise. When \(\sigma\beta\neq0\), log-radius and stochastic phase increments have correlation \(+1\) or \(-1\).

This is a feature that must be stated, not hidden: one real Brownian driver cannot supply two independent local noise directions.

### 5.5 Complex quadratic variation

Prove

\[
d[\Xi]_t=(\sigma+i\beta)^2dt
=
(\sigma^2-\beta^2+2i\sigma\beta)dt,
\tag{P4.10}
\]

and show exactly how it produces the drift correction in (P4.6).

### 5.6 Moments and transition law

Derive and test:

- the lognormal law of \(R_t\);
- the wrapped-normal law of the phase modulo \(2\pi\);
- integer complex moments \(\mathbb E[\mathcal Z_t^n]\);
- mixed radial-angular moments;
- the joint Gaussian law of \((\log R_t,\Theta_t)\) before wrapping;
- the exact conditional transition from \(\mathcal Z_s\) to \(\mathcal Z_t\).

## 6. Relation to Phase 3

The Phase 3 model becomes a special case rather than the definition.

Let the GBM log-return be

\[
L_t
=
\left(\mu-\frac12\sigma^2\right)t+\sigma W_t.
\]

With \(c=1+i\gamma\),

\[
\mathcal Z_t=\mathcal Z_0e^{cL_t}
\]

has GBM modulus and corresponds to

\[
\beta=\gamma\sigma,
\qquad
\omega=\gamma\left(\mu-\frac12\sigma^2\right).
\tag{P4.11}
\]

Under these restrictions, phase is an affine function of log-radius and the path lies on a fixed logarithmic spiral.

The Phase 4 construction removes these restrictions: \(\omega\) and \(\beta\) may be selected independently of \(\mu\) and \(\sigma\), while the modulus remains exactly GBM. The fixed logarithmic spiral is therefore one parameter subfamily, not the whole model.

## 7. What “combining \(dt\) and \(dW_t\)” can and cannot mean

The project will make the following distinction precise:

\[
d\Xi_t=\kappa\,dt+\nu\,dW_t
\]

is one complex semimartingale increment, and

\[
\mathcal Z_t=\mathcal Z_0e^{\Xi_t}
\]

is one exponential representation. This legitimately packages drift and diffusion into one stochastic object.

However:

- \(dt\) and \(dW_t\) remain different stochastic orders;
- \(dW_t^2=dt\) is a quadratic-variation rule, not an ordinary equality of numbers;
- \(dW_t^2=dt\) is not the same algebraic phenomenon as \(i^2=-1\);
- exponentiation introduces the Itô correction \(\tfrac12\nu^2dt\);
- a single Brownian driver cannot create independent radial and angular noise.

These boundaries are essential to the mathematical validity of the result.

## 8. Dimensional analysis

The exponent must be dimensionless. Therefore:

\[
[\mu]=[\omega]=T^{-1},
\qquad
[\sigma]=[\beta]=T^{-1/2},
\qquad
[W_t]=T^{1/2}.
\]

The project will reject expressions that add an unscaled \(dt\) directly to an unscaled \(dW_t\), because their units differ.

## 9. Literature research track

The implementation will begin with a focused literature note covering:

1. exact exponential solutions of scalar linear SDEs and GBM;
2. stochastic exponentials and stochastic logarithms;
3. complex-valued semimartingales and complex stochastic exponentials;
4. complex coefficients in linear SDEs;
5. complex powers of positive GBM and branch selection;
6. phase wrapping, unwrapped phase, and wrapped-normal distributions;
7. the difference between a one-driver rank-one lift and planar Brownian motion.

Initial primary sources:

- Desmond J. Higham, “An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations,” *SIAM Review* 43 (2001), 525–546. The article gives the exact exponential solution of a linear multiplicative SDE and later explicitly allows complex drift and diffusion parameters.
  <https://doi.org/10.1137/S0036144500378302>
- Martin Larsson and Johannes Ruf, “Stochastic Exponentials and Logarithms on
  Stochastic Intervals—A Survey,” *Journal of Mathematical Analysis and
  Applications* 476 (2019), 2–12.
  <https://doi.org/10.1016/j.jmaa.2018.11.040>
- Aleš Černý and Johannes Ruf, “Simplified Calculus for Semimartingales: Multiplicative Compensators and Changes of Measure,” *Stochastic Processes and their Applications* 161 (2023), 572–602. This work explicitly treats stochastic exponentials of complex-valued semimartingales.
  <https://doi.org/10.1016/j.spa.2023.04.010>
- Kiyosi Itô, “On a Formula Concerning Stochastic Differentials,” *Nagoya Mathematical Journal* 3 (1951), 55–65.
  <https://www.mathnet.ru/eng/mat116>

The literature review will distinguish standard theory from the project's expository parameterization. No novelty claim will be made without a separate, exhaustive search.

## 10. Computational validation plan

Create:

- `notebooks/build_phase4_coordinate_free_complex_gbm.py`
- `notebooks/phase4_coordinate_free_complex_gbm.ipynb`
- `PHASE_4_SIMULATION_RESULTS.md`

Use the existing project conda environment unless a dependency audit finds a genuine gap.

### Experiment 1: Pathwise modulus identity

- Generate \(W_t\).
- Compute \(\mathcal Z_t\) from (P4.1).
- Compute the reference GBM directly from (P4.3).
- Verify \(\max_t ||\mathcal Z_t|-R_t|\) is at floating-point scale.

### Experiment 2: Rotation

- Plot \(\mathcal Z_t\) in the complex plane for:
  - \(\omega=\beta=0\);
  - deterministic rotation only;
  - stochastic rotation only;
  - mixed deterministic and stochastic rotation.
- Plot radius, unwrapped phase, and principal phase separately.

### Experiment 3: Exact step versus continuous formula

- Use the same Gaussian increments in (P4.7) and the cumulative closed form.
- Verify pathwise equality to floating-point precision.

### Experiment 4: Complex SDE verification

- Simulate Euler--Maruyama for (P4.6).
- Couple it to the exact solution with the same Brownian path.
- Estimate strong convergence as the step size decreases.
- Keep “Euler form” and “Euler--Maruyama” terminologically separate.

### Experiment 5: Covariance rank

- Estimate the covariance of increments of \((\log R,\Theta)\).
- Compare with (P4.9).
- Verify one eigenvalue tends to zero and the other tends to \((\sigma^2+\beta^2)h\).

### Experiment 6: Distribution and moment checks

- Compare empirical log-radius and phase distributions with their Gaussian laws.
- Compare the radius with its lognormal moments.
- Validate selected complex and mixed moments with Monte Carlo confidence intervals.

### Experiment 7: Phase 3 equivalence

- Impose the restrictions (P4.11).
- Simulate both Phase 3 and Phase 4 expressions with the same Brownian path.
- Verify pathwise equality.
- Then violate (P4.11) to demonstrate the additional Phase 4 freedom.

### Experiment 8: One-driver versus two-driver boundary

As a contrast only, simulate

\[
\mathcal Z_t^{(2)}
=
\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+\sigma W_t^{(r)}+i\beta W_t^{(\theta)}
\right),
\]

with independent Brownian motions. Show that this preserves the same GBM modulus while producing rank-two log-polar noise. This is not the target model; it demonstrates precisely what one driver cannot do.

## 11. Mathematical deliverables

Proposed Phase 4 documents:

- `PHASE_4_LITERATURE_REVIEW.md`
- `13_COORDINATE_FREE_COMPLEX_GBM.md`
- `14_COMPLEX_LOG_DRIVER_AND_STOCHASTIC_EXPONENTIAL.md`
- `15_PHASE_4_EQUIVALENCE_RANK_AND_LIMITS.md`
- `PHASE_4_SIMULATION_RESULTS.md`
- `PHASE_4_SYNTHESIS.md`
- the Phase 4 notebook and reproducible notebook builder
- targeted updates to `README.md`

The synthesis will end with three equivalent boxed forms:

1. direct complex exponential;
2. exact multiplicative random-walk step;
3. complex Itô SDE.

## 12. Implementation sequence

### Stage 1: Literature and notation

- Complete the primary-source review.
- Freeze notation so \(\mathcal Z_t\) is never used both as input and output.
- Define “Euler-form exponential,” “ordinary exponential,” and “stochastic exponential.”
- State assumptions and dimensional units.

**Checkpoint:** The model is stated without any Cartesian coordinate process.

### Stage 2: Analytical derivation

- Prove the exact modulus and phase formulas.
- Derive (P4.6) from (P4.1).
- Derive (P4.1) from (P4.6).
- Establish the stochastic-exponential representation.
- Derive moments, transitions, and quadratic variations.

**Checkpoint:** Two independent derivations agree on every drift correction.

### Stage 3: Structural comparison

- Map Phase 3 into the Phase 4 parameter space.
- Characterize the fixed-spiral subfamily.
- Prove the rank-one covariance result.
- Document the two-driver boundary.

**Checkpoint:** The new freedom and the remaining limitation are both explicit.

### Stage 4: Reproducible computation

- Build and execute the notebook.
- Run pathwise, distributional, covariance, and convergence tests.
- Save numerical tables and explanatory figures.

**Checkpoint:** Exact identities hold at floating-point precision and Monte Carlo results agree within stated uncertainty.

### Stage 5: Synthesis and review

- Write the Phase 4 synthesis.
- Update the project map in `README.md`.
- Audit every claim against derivations, simulations, and primary sources.
- If a second opinion is useful, use OpenCode GLM 5.2 only as a reviewer; do not delegate implementation.

**Checkpoint:** No overclaiming, no hidden Cartesian construction, and no confusion between Itô algebra and complex-number algebra.

## 13. Acceptance criteria

Phase 4 is complete only if:

- the central definition and final boxed equation contain no \(X_t,Y_t\), or pre-existing \(Z_i-Z_0\) path;
- the modulus is proved to satisfy \(dR_t/R_t=\mu dt+\sigma dW_t\);
- the phase has a genuine rotational term;
- the exact step combines \(h\) and \(\sqrt h\,\xi_n\) inside one complex exponential;
- the complex Itô correction is derived correctly;
- the stochastic-exponential and ordinary-exponential forms are reconciled;
- Phase 3 is recovered as a parameter-restricted special case;
- the one-driver covariance is shown to be rank one;
- branch and phase-unwrapping issues are handled;
- dimensions are consistent;
- simulations reproduce all exact identities and theoretical moments;
- the work is presented as a rigorous construction or parameterization, not as an unsupported claim of a new theorem.

## 14. Non-goals

Phase 4 will not:

- claim that \(dW_t^2=dt\) and \(i^2=-1\) are the same algebraic identity;
- claim that one real Brownian motion creates full two-dimensional Brownian motion;
- hide a second independent stochastic degree of freedom in complex notation;
- use Cartesian coordinates in the defining formula;
- interpret the model financially beyond the mathematical definition of GBM;
- claim research novelty without a separate novelty review.

## 15. Approval gate

No Phase 4 implementation should begin until this plan is approved.

On approval, the first implementation artifact will be `PHASE_4_LITERATURE_REVIEW.md`, followed by the analytical derivation and only then the notebook simulations.
