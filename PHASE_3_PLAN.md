# Phase 3 Plan: One-Driver Stochastic Radius Without Dimensional Inflation

## Status

**Approved by the user on 2026-07-23; implementation completed and
independently reviewed on 2026-07-23.**

## 1. The concern Phase 3 must resolve

The original arithmetic Brownian motion is the scalar process

\[
dX_t=\mu\,dt+\sigma\,dW_t,
\qquad
X_t=X_0+\mu t+\sigma W_t.
\]

It has one Brownian driver and therefore one instantaneous stochastic degree
of freedom.

Phase 1 embedded \(X_t\) as a stochastic phase,

\[
Z_t=r_0e^{iX_t},
\]

which preserved the one-driver structure but fixed the radius.

Phase 2 correctly replaced that circle-valued process with planar Brownian
motion,

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2),
\]

whose Bessel radius and winding angle are both stochastic. That construction
is mathematically sound, but it introduces a second independent Brownian
driver. It is therefore a new two-dimensional process, not a coordinate
rewriting of the original scalar arithmetic Brownian motion.

Phase 3 will fill the missing middle ground:

> Find exact complex exponential embeddings of the original one-driver
> process in which both radius and angle can be stochastic, while stating
> precisely what is preserved, what is lost, and why the resulting motion
> cannot be full planar Brownian motion.

## 2. Central Phase 3 model

Let

\[
c=\alpha+i\beta,
\qquad
Z_0\ne0,
\]

where \(\alpha\) and \(\beta\) have the reciprocal units needed to make
\(c(X_t-X_0)\) dimensionless. Define

\[
\boxed{
Z_t
=Z_0\exp\!\left[c(X_t-X_0)\right].}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
A_t:=\log R_t
&=\log R_0+\alpha(X_t-X_0),\\
\Theta_t
&=\Theta_0+\beta(X_t-X_0),
\end{aligned}}
\]

where \(\Theta_t\) is an unwrapped angle.

This construction has the required properties:

- it uses the same single Brownian motion \(W_t\) as \(X_t\);
- the radius is stochastic whenever \(\alpha\ne0\);
- the angle is stochastic whenever \(\beta\ne0\);
- if \(\alpha\ne0\), the scalar state can be recovered from the radius:
  \[
  X_t=X_0+\frac1\alpha\log\frac{R_t}{R_0};
  \]
- its image is a logarithmic spiral when \(\alpha\beta\ne0\);
- it remains a rank-one diffusion rather than planar Brownian motion.

The special cases organize the earlier work:

| Parameters | Geometry | Information |
|---|---|---|
| \(\alpha=0,\ \beta\ne0\) | fixed-radius circle | state is periodic unless the angle is unwrapped |
| \(\alpha\ne0,\ \beta=0\) | stochastic positive ray | scalar state is recoverable from radius |
| \(\alpha\ne0,\ \beta\ne0\) | stochastic logarithmic spiral | injective scalar-to-complex embedding |
| two independent drivers | full planar diffusion | not equivalent to the scalar process |

## 3. Target Itô equation

Applying Itô's formula to

\[
F(x)=Z_0e^{c(x-X_0)}
\]

should give

\[
\boxed{
\frac{dZ_t}{Z_t}
=
\left[
c\mu+\frac12c^2\sigma^2
\right]dt
+c\sigma\,dW_t.}
\]

Writing \(c=\alpha+i\beta\), the drift becomes

\[
c\mu+\frac12c^2\sigma^2
=
\left[
\alpha\mu+\frac12(\alpha^2-\beta^2)\sigma^2
\right]
+i\left[
\beta\mu+\alpha\beta\sigma^2
\right].
\]

This formula exposes two distinct Itô corrections:

- the real correction
  \[
  \frac12(\alpha^2-\beta^2)\sigma^2
  \]
  balances radial amplification against angular rotation;
- the imaginary correction
  \[
  \alpha\beta\sigma^2
  \]
  comes from the cross-variation of log-radius and phase.

The log-radius and angle themselves satisfy the simpler equations

\[
\boxed{
\begin{aligned}
dA_t&=\alpha\mu\,dt+\alpha\sigma\,dW_t,\\
d\Theta_t&=\beta\mu\,dt+\beta\sigma\,dW_t.
\end{aligned}}
\]

Their quadratic variations are

\[
\boxed{
\begin{aligned}
d[A,A]_t&=\alpha^2\sigma^2dt,\\
d[\Theta,\Theta]_t&=\beta^2\sigma^2dt,\\
d[A,\Theta]_t&=\alpha\beta\sigma^2dt.
\end{aligned}}
\]

Consequently,

\[
\det
\begin{pmatrix}
d[A,A]_t/dt & d[A,\Theta]_t/dt\\
d[A,\Theta]_t/dt & d[\Theta,\Theta]_t/dt
\end{pmatrix}
=0.
\]

Both polar coordinates may be random, but their instantaneous noises are
perfectly dependent.

## 4. Exact finite-step random-walk formula

For a time step \(h\), let

\[
\Delta X_n=\mu h+\sigma\sqrt h\,\xi_n,
\qquad
\xi_n\sim N(0,1).
\]

The exact induced complex step is

\[
\boxed{
Z_{n+1}
=Z_n\exp\!\left[
(\alpha+i\beta)
(\mu h+\sigma\sqrt h\,\xi_n)
\right].}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
R_{n+1}
&=R_n
\exp\!\left[
\alpha(\mu h+\sigma\sqrt h\,\xi_n)
\right],\\
\Theta_{n+1}
&=\Theta_n+
\beta(\mu h+\sigma\sqrt h\,\xi_n).
\end{aligned}}
\]

The same Gaussian increment changes radius and angle. This is the
one-driver counterpart of the two-driver planar polar walk from Phase 2.

## 5. Work package A — Define “representation” precisely

Phase 3 will distinguish four notions that were previously easy to conflate:

1. **deterministic image:** \(Z_t=F(X_t)\);
2. **state-injective embedding:** \(F\) has an inverse on its image;
3. **pathwise recoverability:** \(X\) can be recovered using a continuous
   lifted angle even if \(F\) is periodic at a fixed time;
4. **equality with planar Brownian motion:** the complex process has
   full-rank isotropic planar covariance.

The work will prove that the first three are possible with one driver, while
the fourth is not.

For \(\alpha\ne0\), the logarithmic-spiral map is state-injective and
filtration preserving:

\[
\sigma(X_s:0\le s\le t)
=
\sigma(Z_s:0\le s\le t).
\]

For the fixed-radius map \(\alpha=0\), \(Z_t\) alone only records phase modulo
\(2\pi\). Recovering \(X_t\) requires the initial value and the continuously
unwrapped phase history.

## 6. Work package B — Direct scalar polar form and zero crossings

The literal complex embedding

\[
Z_t=X_t+i0
\]

has

\[
R_t=|X_t|,
\qquad
\Theta_t\in\{0,\pi\}
\]

away from zero. Phase 3 will treat this exact representation honestly rather
than forcing a smooth rotating angle onto it.

Before the first zero

\[
\tau_0=\inf\{t\ge0:X_t=0\},
\]

Itô's formula applied to \(\log|X_t|\) gives

\[
X_t
=X_0\exp\!\left[
\int_0^t\frac{\mu}{X_s}\,ds
+\int_0^t\frac{\sigma}{X_s}\,dW_s
-\frac12\int_0^t\frac{\sigma^2}{X_s^2}\,ds
\right],
\qquad t<\tau_0.
\]

The absolute value, not \(\log X_t\), is required when \(X_0<0\).

Across zero, the smooth Itô formula is no longer sufficient. The global
radial equation must be analyzed with Tanaka's formula:

\[
d|X_t|
=\operatorname{sgn}(X_t)\,dX_t+dL_t^0(X),
\]

where \(L_t^0(X)\) is the local time at zero. This work package will explain:

- why the scalar polar angle is singular at every sign change;
- why local time appears in the global radius;
- why the localized stochastic logarithm stops at zero;
- how the nonvanishing logarithmic-spiral embedding avoids this singularity.

## 7. Work package C — General one-driver complex embeddings

Let

\[
Z_t=F(X_t),
\qquad
F:\mathbb R\longrightarrow\mathbb C,
\]

with \(F\in C^2\). Itô's formula gives

\[
\boxed{
dZ_t
=
\left[
\mu F'(X_t)+\frac12\sigma^2F''(X_t)
\right]dt
+\sigma F'(X_t)dW_t.}
\]

Writing \(F=(F_1,F_2)\), the Cartesian instantaneous covariance is

\[
\boxed{
C_t
=\sigma^2
\begin{pmatrix}
F_1'(X_t)\\
F_2'(X_t)
\end{pmatrix}
\begin{pmatrix}
F_1'(X_t)&F_2'(X_t)
\end{pmatrix}.}
\]

Therefore,

\[
\operatorname{rank}C_t\le1,
\qquad
\det C_t=0.
\]

This will become the Phase 3 no-go theorem:

> No deterministic \(C^2\) transformation of one scalar Brownian driver can
> produce nondegenerate planar Brownian covariance.

The theorem does **not** say that radius and angle cannot both be stochastic.
It says that their randomness must be constrained to one instantaneous
direction.

The work will identify conditions on \(F\) for:

- local immersion: \(F'(x)\ne0\);
- global state injectivity;
- nonvanishing images that admit a global pathwise logarithm;
- stochastic radius and stochastic angle;
- preservation or loss of information about \(X_t\).

## 8. Work package D — Complex quadratic variation

For the logarithmic-spiral model,

\[
dZ_t^{\mathrm{noise}}=c\sigma Z_t\,dW_t.
\]

Its complex quadratic variations are

\[
\boxed{
\begin{aligned}
d[Z,Z]_t&=c^2\sigma^2Z_t^2dt,\\
d[Z,\overline Z]_t&=|c|^2\sigma^2|Z_t|^2dt.
\end{aligned}}
\]

Unlike isotropic planar Brownian motion, a nontrivial one-driver complex
embedding cannot have

\[
d[Z,Z]_t=0.
\]

Indeed, \(c^2=0\) over the complex numbers implies \(c=0\). Thus the Phase 2
cancellation between two independent Cartesian quadratic variations cannot
occur here.

Phase 3 will verify that

\[
d\log Z_t
=\frac{dZ_t}{Z_t}
-\frac12\frac{d[Z,Z]_t}{Z_t^2}
=c\,dX_t.
\]

This is the exact one-driver version of the stochastic-logarithm bridge.

## 9. Work package E — Analytic distributions and moments

Because \(X_t-X_0\) is Gaussian, the logarithmic-spiral model has closed-form
benchmarks.

The log-radius and unwrapped angle are jointly Gaussian with rank-one
covariance:

\[
\begin{pmatrix}
A_t-A_0\\
\Theta_t-\Theta_0
\end{pmatrix}
=
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
(\mu t+\sigma W_t).
\]

For real \(p\),

\[
\boxed{
\mathbb E[R_t^p]
=R_0^p
\exp\!\left[
p\alpha\mu t+\frac12p^2\alpha^2\sigma^2t
\right].}
\]

Complex moments satisfy

\[
\boxed{
\mathbb E\!\left[\left(\frac{Z_t}{Z_0}\right)^n\right]
=
\exp\!\left[
nc\mu t+\frac12n^2c^2\sigma^2t
\right]}
\]

for integer \(n\), with the same Gaussian-transform formula available for
appropriate complex exponents.

These identities will provide exact Monte Carlo checks rather than relying
only on visual agreement.

## 10. Work package F — Numerical experiments

Create an executed notebook:

`notebooks/phase3_one_driver_complex_embedding.ipynb`

using an existing conda environment, fixed seeds, recorded package versions,
and moderate runtimes.

The notebook will contain:

1. **Shared-path reconstruction**
   - simulate \(X_t\);
   - compute \(Z_t\) directly from the exponential map;
   - reconstruct \(X_t\) from \(R_t\) when \(\alpha\ne0\);
   - confirm pathwise errors at floating-point precision.

2. **Exact multiplicative walk**
   - compare the direct terminal map with the product of exact complex steps;
   - verify agreement on every shared path.

3. **Euler–Maruyama convergence**
   - integrate the derived complex SDE using the same Brownian paths;
   - compare against the exact logarithmic-spiral solution;
   - estimate the strong convergence rate over at least four step sizes.

4. **Rank-one covariance test**
   - estimate the covariance of \((\Delta A,\Delta\Theta)\);
   - compare both eigenvalues with the rank-one analytic prediction;
   - contrast it with the two positive eigenvalues of Phase 2 planar Brownian
     motion.

5. **Moment checks**
   - compare empirical radial and complex moments with the exact formulas;
   - report Monte Carlo standard errors and standardized discrepancies.

6. **Geometry comparison**
   - plot the same scalar Brownian path under the real-axis, circle,
     radial-ray, and logarithmic-spiral embeddings;
   - separately plot a genuine two-driver planar Brownian path;
   - label the number of drivers and covariance rank on every figure.

7. **Zero-crossing and local-time experiment**
   - demonstrate the failure of the localized \(\log|X|\) representation at
     the first zero;
   - approximate the Tanaka local-time residual under grid refinement;
   - contrast this with the globally nonvanishing spiral embedding.

## 11. Work package G — Comparison theorem and model hierarchy

The final synthesis will present the following hierarchy.

### Level 1: scalar arithmetic Brownian motion

\[
X_t=X_0+\mu t+\sigma W_t.
\]

It is additive motion on a line.

### Level 2: one-driver complex image

\[
Z_t=F(X_t).
\]

It may have stochastic radius and stochastic angle, but its covariance rank
is at most one and its path remains on the deterministic image curve
\(F(\mathbb R)\).

### Level 3: injective logarithmic-spiral representation

\[
Z_t=Z_0e^{(\alpha+i\beta)(X_t-X_0)},
\qquad \alpha\ne0.
\]

It preserves the complete scalar state, has nonconstant radius, and has an
exact exponential random-walk formula.

### Level 4: genuine planar Brownian motion

\[
Z_t=Z_0+\sigma(W_t^1+iW_t^2).
\]

It has two independent drivers, full-rank covariance, a Bessel radius, and a
time-changed winding angle. It is a different stochastic model, not a
reparameterization of Level 1.

## 12. Planned research artifacts

Subject to approval, Phase 3 will produce:

1. `10_SCALAR_POLAR_FORM_AND_ZERO_CROSSINGS.md`
2. `11_ONE_DRIVER_LOGARITHMIC_SPIRAL.md`
3. `12_EMBEDDING_RANK_AND_MODEL_EQUIVALENCE.md`
4. `PHASE_3_LITERATURE_REVIEW.md`
5. `notebooks/phase3_one_driver_complex_embedding.ipynb`
6. `PHASE_3_SIMULATION_RESULTS.md`
7. `PHASE_3_SYNTHESIS.md`
8. updates to `README.md`, `.agent/status.md`, and `.agent/handoff.md`
9. an independent opencode GLM 5.2 review after Codex completes and verifies
   the implementation

No implementation will be delegated to another agent.

## 13. Source-verification plan

The literature review will verify authoritative or primary sources for:

- Itô's formula under smooth maps from \(\mathbb R\) to \(\mathbb R^2\);
- Tanaka's formula and Brownian local time;
- diffusion covariance rank under deterministic transformations;
- curve-valued or manifold-valued diffusions;
- stochastic logarithms up to zero;
- numerical approximation of local time and strong SDE convergence.

Existing Phase 1 and Phase 2 sources may be reused only for claims they
directly support. Any new claim about zero crossings, local time, or
information-preserving embeddings will receive a separately verified source
or a complete project derivation.

## 14. Acceptance criteria

Phase 3 is complete only if all of the following hold:

1. The scalar and planar models are never described as equivalent.
2. The logarithmic-spiral model uses exactly the original Brownian driver.
3. The complex SDE is derived independently:
   - by Itô's formula applied to \(F(X_t)\);
   - by reconstructing \(Z_t=e^{A_t+i\Theta_t}\).
4. The rank-one covariance obstruction is proved for general \(C^2\)
   embeddings \(F:\mathbb R\to\mathbb C\).
5. State injectivity and pathwise recoverability are distinguished.
6. The scalar zero-crossing case uses \(\log|X|\), stopping, and Tanaka local
   time correctly.
7. Exact finite-step formulas are separated from continuous-time Itô
   identities and numerical approximations.
8. Analytic moments agree with Monte Carlo estimates within reported
   uncertainty.
9. The covariance experiment distinguishes rank one from rank two.
10. The notebook executes from a clean kernel with all assertions passing.
11. At least four time-step sizes are used for every convergence claim.
12. Exact identities, distributional identities, convergence statements, and
    heuristics are labeled separately.
13. An independent GLM 5.2 review finds no unresolved major mathematical
    issue.

## 15. Scope limits

Phase 3 will not claim:

- that complex notation creates an additional source of randomness;
- that stochastic radius requires two Brownian drivers;
- that a rank-one spiral diffusion is planar Brownian motion;
- that \(dW\) is an imaginary unit;
- that an individual finite increment satisfies \((\Delta W)^2=\Delta t\);
- that polar coordinates remain regular when the scalar real-axis embedding
  crosses zero;
- that a periodic phase embedding preserves the scalar state without an
  unwrapped path.

Quantum Itô calculus, Lie-group Brownian motion, Schrödinger evolution, and
higher-dimensional Clifford-algebra analogies remain outside Phase 3.

## 16. Expected final answer

Phase 3 should culminate in a layered answer rather than forcing one formula
to serve incompatible models:

\[
\boxed{
\begin{aligned}
\text{scalar Brownian motion:}\quad
&X_t=X_0+\mu t+\sigma W_t,\\[1mm]
\text{faithful one-driver complex embedding:}\quad
&Z_t=Z_0e^{(\alpha+i\beta)(X_t-X_0)},\quad \alpha\ne0,\\[1mm]
\text{genuine planar Brownian motion:}\quad
&\widetilde Z_t
=\widetilde Z_0+\sigma(W_t^1+iW_t^2).
\end{aligned}}
\]

The first and second lines contain the same stochastic information. The third
line does not: it deliberately introduces a second independent stochastic
degree of freedom.

That distinction directly resolves the concern raised by
`complex_brownian_motion_critique.md` while preserving the valid results of
both earlier phases.
