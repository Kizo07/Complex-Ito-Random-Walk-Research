# Phase 2 Plan: Stochastic Radius and Full Complex Brownian Motion

## Status

**Approved by the user and completed on 2026-07-23.**

This plan extends the completed circle-valued model into a genuinely
two-dimensional complex diffusion with both stochastic radius and stochastic
angle.

## 1. Why Phase 2 is necessary

The Phase 1 process

\[
Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)}
\]

has a random angle but a fixed radius. It is Brownian-type motion on the
circle \(S^1\), not Brownian motion throughout the complex plane.

A full planar Brownian motion has two independent Cartesian noise directions:

\[
Z_t=X_t+iY_t,
\qquad
dZ_t=\sigma(dW_t^1+i\,dW_t^2),
\]

under the convention that \(W^1\) and \(W^2\) are independent standard
Brownian motions. Consequently,

\[
[Z,\overline Z]_t=2\sigma^2t,
\qquad
[Z,Z]_t=0.
\]

Its radius and angle are both stochastic, and their local noise intensity
depends on the current radius. This state dependence is the main feature
missing from the fixed-circle construction.

## 2. What the deep-research file contributes

`deep-research-complex-ito.md` supports four directions that are directly
useful for the next phase:

1. planar Brownian motion is the natural setting for a genuine stochastic
   polar decomposition;
2. the radius is a two-dimensional Bessel process;
3. the winding angle is a Brownian motion evaluated on a random clock
   involving \(1/R_t^2\);
4. stochastic logarithms and exponentials can join the radial and angular
   descriptions into one complex formula.

The file also discusses Lie groups, manifold-valued SDEs, heat semigroups,
Schrödinger evolution, and quantum Itô calculus. Those are valuable later
extensions, but including them now would obscure the immediate problem of
constructing a nonconstant-radius complex Brownian representation.

Some citations in the deep-research file are interface citation tokens rather
than durable bibliographic references. Phase 2 will treat the file as a
conceptual roadmap and independently verify every source used in a final
research note.

## 3. Central Phase 2 objective

Construct and test a stochastic polar-exponential representation of planar
Brownian motion and more general complex diffusions:

\[
\boxed{Z_t=R_te^{i\Theta_t},}
\]

where both \(R_t\) and \(\Theta_t\) are stochastic and their SDEs reconstruct
the original Cartesian process exactly.

The primary target is the drift-free isotropic process, started from
\(Z_0\ne0\):

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2).
\]

Define the adapted radial and angular Brownian motions

\[
\begin{aligned}
dB_t^R
&=\cos\Theta_t\,dW_t^1+\sin\Theta_t\,dW_t^2,\\
dB_t^\Theta
&=-\sin\Theta_t\,dW_t^1+\cos\Theta_t\,dW_t^2.
\end{aligned}
\]

The target polar system is

\[
\boxed{
\begin{aligned}
dR_t&=\frac{\sigma^2}{2R_t}\,dt+\sigma\,dB_t^R,\\
d\Theta_t&=\frac{\sigma}{R_t}\,dB_t^\Theta.
\end{aligned}}
\]

For log-radius \(A_t=\log R_t\), the Bessel drift cancels under Itô's
formula:

\[
\boxed{
\begin{aligned}
dA_t&=\frac{\sigma}{R_t}\,dB_t^R,\\
d\Theta_t&=\frac{\sigma}{R_t}\,dB_t^\Theta.
\end{aligned}}
\]

This suggests the nonconstant-radius exponential representation

\[
\boxed{
Z_t
=Z_0\exp\!\left[
\int_0^t\frac{\sigma}{R_s}\,dB_s^R
+i\int_0^t\frac{\sigma}{R_s}\,dB_s^\Theta
\right],}
\]

understood with a continuous lifted angle and localization away from the
origin.

This formula is the proposed Phase 2 successor to
\(r_0e^{i(\theta_0+\beta W_t)}\). Its real stochastic integral changes the
radius, while its imaginary stochastic integral changes the angle.

## 4. Main mathematical questions

Phase 2 will answer the following questions precisely.

1. Why does full planar Brownian motion require two independent noise
   directions rather than one real Brownian driver?
2. How do the Bessel drift in \(R_t\) and the angular Itô correction cancel
   when reconstructing \(Z_t\)?
3. Why do \(\log R_t\) and \(\Theta_t\) have the same stochastic clock?
4. In what sense can planar Brownian motion be written as a stochastic
   exponential even though its Cartesian dynamics are additive?
5. What roles are played by the two different quadratic variations
   \([Z,Z]\) and \([Z,\overline Z]\)?
6. How does the representation change under drift, anisotropic volatility,
   or correlated Cartesian noise?
7. How should the origin, angular branches, and numerical near-origin
   instability be handled?
8. What is the correct exact finite-step complex random-walk formula, and
   what only emerges in the continuous-time limit?

## 5. Work package A — Noise dimension and nondegeneracy

Begin with the general amplitude-phase system

\[
dA_t=a_tdt+u_t\cdot dW_t,
\qquad
d\Theta_t=\omega_tdt+v_t\cdot dW_t.
\]

Its instantaneous covariance in \((A,\Theta)\) coordinates is

\[
\begin{pmatrix}
\lVert u_t\rVert^2 & u_t\cdot v_t\\
u_t\cdot v_t & \lVert v_t\rVert^2
\end{pmatrix}.
\]

The work will show:

- with only one real Brownian driver, this matrix has rank at most one;
- a rank-one diffusion cannot reproduce nondegenerate planar Brownian
  motion;
- two independent drivers permit separate radial and angular noise and a
  full-rank planar covariance;
- for isotropic planar Brownian motion, the adapted choice is
  \[
  u_t=\left(\frac{\sigma}{R_t},0\right),
  \qquad
  v_t=\left(0,\frac{\sigma}{R_t}\right)
  \]
  in the \((B^R,B^\Theta)\) Brownian basis.

This establishes exactly what additional stochastic structure is needed
beyond the original one-dimensional random walk.

## 6. Work package B — Polar derivation by two independent methods

Derive the radial and angular equations twice.

### Method 1: two-dimensional Itô formula

Apply Itô's formula to

\[
R(x,y)=\sqrt{x^2+y^2},
\qquad
\Theta(x,y)=\operatorname{atan2}(y,x).
\]

Track their gradients, Hessians, quadratic variations, and cross-variation.

### Method 2: reconstruction from \(Z=Re^{i\Theta}\)

Starting from the proposed polar SDEs, calculate

\[
d(Re^{i\Theta})
\]

including:

- the Bessel drift in \(dR\);
- the angular term \(d[\Theta]\);
- the cross-variation \(d[R,\Theta]\).

Verify that every drift correction cancels and that the result is exactly

\[
dZ_t=\sigma(dW_t^1+i\,dW_t^2).
\]

## 7. Work package C — Complex quadratic variation and stochastic logarithm

For a nonvanishing continuous complex semimartingale, derive the local
complex Itô identity

\[
\boxed{
d\log Z_t
=\frac{dZ_t}{Z_t}
-\frac12\frac{d[Z,Z]_t}{Z_t^2}.}
\]

This requires distinguishing:

\[
[Z,Z]
\quad\text{from}\quad
[Z,\overline Z].
\]

For isotropic planar Brownian motion,

\[
d[Z,Z]_t=0
\]

because the two equal Cartesian quadratic variations cancel through
\(i^2=-1\), while

\[
d[Z,\overline Z]_t=2\sigma^2dt
\]

remains positive and measures total planar noise.

The resulting stochastic logarithm should satisfy

\[
\log\frac{Z_t}{Z_0}
=
\int_0^t\frac{dZ_s}{Z_s}
=
\log\frac{R_t}{R_0}
+i(\Theta_t-\Theta_0),
\]

using a continuously lifted angle. Exponentiating this identity should
produce the full stochastic-radius representation in Section 3.

This is expected to be the strongest mathematical bridge between:

- additive complex Brownian motion;
- stochastic polar form;
- stochastic logarithms;
- and ordinary complex exponentiation.

## 8. Work package D — General planar complex diffusion

Extend the isotropic result to

\[
d\mathbf X_t=b(t,\mathbf X_t)dt+\Sigma(t,\mathbf X_t)d\mathbf W_t,
\qquad
\mathbf X_t=(X_t,Y_t),
\]

with covariance matrix

\[
C=\Sigma\Sigma^\mathsf T.
\]

Using

\[
e_r=(\cos\Theta,\sin\Theta),
\qquad
e_\theta=(-\sin\Theta,\cos\Theta),
\]

derive

\[
\boxed{
dR
=
\left[
e_r\cdot b+
\frac{\operatorname{tr}C-e_r^\mathsf TC e_r}{2R}
\right]dt
+e_r^\mathsf T\Sigma\,dW,}
\]

and

\[
\boxed{
d\Theta
=
\left[
\frac{e_\theta\cdot b}{R}
-\frac{e_r^\mathsf TC e_\theta}{R^2}
\right]dt
+\frac{e_\theta^\mathsf T\Sigma}{R}\,dW.}
\]

Then derive the corresponding equation for \(A=\log R\) and insert its
coefficients into the Phase 1 general amplitude-phase formula.

Special cases will include:

- complex Brownian motion with a constant complex drift;
- unequal Cartesian volatilities;
- correlated Cartesian Brownian drivers;
- radial-only noise;
- angular-only noise;
- shared versus independent amplitude-phase noise.

This comparison will identify exactly when the elegant isotropic
cancellations survive.

## 9. Work package E — Exact discrete complex random walk

Start from a two-dimensional Gaussian random walk:

\[
Z_{n+1}
=Z_n+\mu_nh+G_n\sqrt h\,\xi_n,
\qquad
\xi_n\sim N(0,I_2).
\]

Whenever \(Z_n\) and \(Z_{n+1}\) are nonzero, write the exact multiplicative
step

\[
\boxed{
Z_{n+1}
=Z_n\exp\!\left[
\operatorname{Log}_{\mathrm{cont}}
\left(1+\frac{\Delta Z_n}{Z_n}\right)
\right].}
\]

Here \(\operatorname{Log}_{\mathrm{cont}}\) denotes a consistently unwrapped
logarithm along the sampled path. Its real part is the log-radius increment
and its imaginary part is the unwrapped angular increment.

Expand the logarithm locally:

\[
\Delta\log Z_n
=
\frac{\Delta Z_n}{Z_n}
-\frac12\left(\frac{\Delta Z_n}{Z_n}\right)^2
+\text{higher-order terms}.
\]

The plan will distinguish:

- the exact finite-grid multiplicative identity;
- the branch choice needed to unwrap angles;
- convergence of the squared-increment sum to complex quadratic variation;
- and the limiting stochastic-logarithm formula.

This is the discrete-to-continuous bridge most directly connected to the
original random-walk question.

## 10. Work package F — Origin and localization

Polar coordinates and \(\log Z\) are singular at \(Z=0\). The core analysis
will therefore:

1. assume \(Z_0\ne0\);
2. define
   \[
   \tau_\varepsilon
   =\inf\{t:R_t\le\varepsilon\};
   \]
3. prove identities first on \(t\le\tau_\varepsilon\);
4. state carefully when \(\varepsilon\downarrow0\) is legitimate;
5. distinguish exact non-hitting of the origin from arbitrarily close
   approaches to it;
6. avoid claiming that a local martingale such as \(\log R_t\) is globally a
   true martingale without checking integrability.

Starting exactly at the origin will be treated as a separate boundary case,
not hidden inside formulas where the angle is undefined.

## 11. Numerical program

Create a new notebook rather than modifying the Phase 1 notebook.

### Experiment 1: Cartesian and polar pathwise reconstruction

- Generate planar Brownian paths from shared Cartesian increments.
- Compute \(R_t\) and a continuously unwrapped \(\Theta_t\).
- Reconstruct \(R_te^{i\Theta_t}\).
- Verify pathwise agreement with the Cartesian complex process.

### Experiment 2: stochastic radius

- Confirm
  \[
  \mathbb E|Z_t-Z_0|^2=2\sigma^2t.
  \]
- Compare the terminal radial distribution with the corresponding
  noncentral chi/Rice law.
- Verify the Bessel radial drift using conditional increment bins.

### Experiment 3: state-dependent angular clock

- Estimate angular quadratic variation.
- Compare it with
  \[
  H_t=\int_0^t\frac{\sigma^2}{R_s^2}\,ds.
  \]
- Demonstrate accelerated winding near the origin.

### Experiment 4: stochastic-logarithm reconstruction

- Approximate
  \[
  \sum_n\left[
  \frac{\Delta Z_n}{Z_n}
  -\frac12\left(\frac{\Delta Z_n}{Z_n}\right)^2
  \right].
  \]
- Compare its exponential with \(Z_T/Z_0\).
- Measure convergence over several grid sizes.

### Experiment 5: two quadratic variations

- Verify numerically that
  \[
  \sum_n(\Delta Z_n)^2\longrightarrow0
  \]
  for isotropic planar Brownian motion.
- Simultaneously verify that
  \[
  \sum_n|\Delta Z_n|^2\longrightarrow2\sigma^2T.
  \]
- Use this to demonstrate why \([Z,Z]\) and
  \([Z,\overline Z]\) encode different information.

### Experiment 6: anisotropy as a controlled counterexample

- Choose unequal or correlated Cartesian volatilities.
- Show that \([Z,Z]\) no longer vanishes.
- Demonstrate that omitting the
  \(-\tfrac12\,d[Z,Z]/Z^2\) stochastic-log correction produces a measurable
  reconstruction error.

### Numerical safeguards

- deterministic seeds;
- at least two grid refinements for every convergence claim;
- Monte Carlo standard errors or confidence intervals;
- stopped-path analysis near \(R=\varepsilon\);
- explicit tracking of angle unwrapping failures;
- no claim based only on a visually plausible plot.

## 12. Planned deliverables

If approved, Phase 2 will create:

1. `06_COMPLEX_QUADRATIC_VARIATION.md`
2. `07_STOCHASTIC_RADIUS_AND_PLANAR_EXPONENTIAL.md`
3. `08_GENERAL_COMPLEX_DIFFUSIONS.md`
4. `09_DISCRETE_COMPLEX_RANDOM_WALK.md`
5. `notebooks/phase2_stochastic_radius.ipynb`
6. `PHASE_2_SIMULATION_RESULTS.md`
7. `PHASE_2_LITERATURE_REVIEW.md`
8. `PHASE_2_SYNTHESIS.md`

The existing Phase 1 files will remain intact except for index links or
clearly identified corrections if a contradiction is discovered.

## 13. Literature verification targets

Before making historical or theorem-attribution claims, verify authoritative
sources for:

- the two-dimensional Bessel radial process;
- the planar Brownian skew-product theorem;
- Brownian winding and continuous argument processes;
- complex semimartingale quadratic variation;
- stochastic logarithms and stochastic exponentials;
- conformal invariance and holomorphic Itô formulas;
- numerical simulation of Bessel and near-singular polar SDEs.

The literature review will distinguish directly verified sources from
informal explanatory material.

## 14. Verification and review gates

Implementation will not be considered complete until:

1. every polar formula is derived independently in Cartesian and
   amplitude-phase coordinates;
2. the complex logarithm formula is checked using complex and real
   two-dimensional Itô calculations;
3. all notebook cells execute from a clean conda kernel;
4. the notebook is executed a second time to a temporary output;
5. all numerical claims have explicit tolerances and uncertainty estimates;
6. Markdown and notebook files pass syntax and consistency checks;
7. opencode with GLM 5.2 is used only for an independent mathematical review
   and second opinion, consistent with the user's instruction;
8. Codex verifies every reviewer finding before changing the research.

No implementation work will be delegated.

## 15. Acceptance criteria

Phase 2 succeeds only if it establishes all of the following:

- \(R_t\) is genuinely stochastic rather than fixed by construction;
- the resulting process has full two-dimensional Brownian covariance;
- the need for two independent noise directions is proved, not merely
  asserted;
- the Bessel radial drift and angular correction are both derived;
- the state-dependent angular clock \(\sigma^2/R_t^2\) is verified;
- the proposed stochastic exponential reconstructs planar Brownian motion;
- \([Z,Z]\) is never confused with \([Z,\overline Z]\);
- finite-step logarithms are separated from continuous Itô limits;
- origin and branch issues are handled explicitly;
- isotropic, anisotropic, and rank-one diffusions are clearly distinguished;
- Monte Carlo results support, but do not replace, the proofs.

## 16. Recommended scope decision

The recommended Phase 2 scope is:

- start from \(Z_0\ne0\);
- solve isotropic drift-free planar Brownian motion first;
- add constant drift and general covariance only after the core identity is
  established;
- include the exact discrete multiplicative random-walk representation;
- defer Lie groups, quantum stochastic calculus, and heat/Schrödinger
  extensions to a possible Phase 3.

This scope directly addresses the fixed-radius limitation while remaining
small enough for rigorous derivation and reproducible simulation.

## Approval record

The user approved this plan and instructed Codex to start implementation.
