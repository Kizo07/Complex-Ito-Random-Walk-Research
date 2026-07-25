# Phase 5 synthesis: exact one-phase Euler representations

A real Brownian motion on the real axis cannot store its full magnitude in its
ordinary polar angle, but an exact nonradial complex affine lift can. For
\(c>0\), define
\(\mathcal Z_t=Z_0[1+i(X_t-X_0)/c]\) and
\(\theta_t=\arctan((X_t-X_0)/c)\). Then
\[
\mathcal Z_t=Z_0\sec(\theta_t)e^{i\theta_t},
\qquad
X_t=X_0+c\tan\theta_t,
\]
so the displayed Euler form contains only the stochastic phase and the radius
is the deterministic function \(r(\theta)=\sec\theta\). A constant radius is
possible only after changing the represented state through a nonlinear
encoding such as the Cayley transform. The phase combines the drifted
Brownian state into one lossless coordinate; it does not remove time or
randomness from the process law.

## 1. The complete answer for the original affine complex process

Consider

\[
Z_t=Z_0+a t+bW_t,
\qquad
Z_0\ne0,\quad b\ne0,
\]

driven by one real Brownian motion. Require an exact, pathwise,
time-independent, genuine polar representation

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t},
\]

where:

- \(r\) is deterministic and positive;
- \(\theta_t\) is the only stochastic state coordinate;
- \(\theta_t\) losslessly determines \(Z_t\); and
- the phase is a continuous lift anchored at the initial state.

Such a representation exists if and only if

\[
\boxed{
\frac ab\in\mathbb R
\quad\text{and}\quad
\frac b{Z_0}\notin\mathbb R.
}
\]

Equivalently,

\[
\operatorname{Im}(a\overline b)=0,
\qquad
\operatorname{Im}(b\overline{Z_0})\ne0.
\]

The first condition says drift and diffusion trace one fixed affine line.
The second says that line misses the origin, allowing its argument to be
injective.

Write

\[
a=\lambda b,\qquad
\frac b{Z_0}=\rho e^{i\phi},\qquad
x_t=\lambda t+W_t.
\]

Then

\[
\theta_t=\operatorname{Arg}\!\left(1+\rho e^{i\phi}x_t\right)
\]

is a bijective phase coordinate and

\[
\boxed{
Z_t
=
Z_0
\frac{\sin\phi}{\sin(\phi-\theta_t)}
e^{i\theta_t},
}
\]

with inverse

\[
\boxed{
x_t
=
\frac{\sin\theta_t}
{\rho\sin(\phi-\theta_t)}.
}
\]

The exact phase domain is the unique positive-radius interval

\[
I_\phi=
\begin{cases}
(\phi-\pi,\phi),&\sin\phi>0,\\
(\phi,\phi+\pi),&\sin\phi<0.
\end{cases}
\]

It has length \(\pi\). Therefore an additive affine one-phase
representation never completes a full revolution and cannot wind repeatedly.

## 2. Eliminating explicit \(t\) and \(W_t\) from the state equation

The state identity itself can be written solely in terms of \(\theta_t\):

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t}.
\]

The phase law can then be specified without treating \(t\) and \(W_t\) as
separate state coordinates. In the canonical case,

\[
d\theta_t
=
\left[
\frac{\mu}{c}\cos^2\theta_t
-\frac{\sigma^2}{c^2}\sin\theta_t\cos^3\theta_t
\right]dt
+\frac{\sigma}{c}\cos^2\theta_t\,dW_t,
\]

or equivalently by the generator

\[
\mathcal L_\theta f
=
\left[
\frac{\mu}{c}\cos^2\theta
-\frac{\sigma^2}{c^2}\sin\theta\cos^3\theta
\right]f'
+\frac{\sigma^2}{2c^2}\cos^4\theta\,f'',
\]

or by its exact transition kernel

\[
p_h(v\mid u)
=
\frac{c\sec^2v}{|\sigma|\sqrt{2\pi h}}
\exp\left[
-\frac{(c\tan v-c\tan u-\mu h)^2}
{2\sigma^2h}
\right].
\]

The generator or kernel presents \(\theta\) as the only Markov state
coordinate. Time still indexes the process, and stochasticity still appears
in its law. No nontrivial stochastic process can literally eliminate both
evolution and randomness.

## 3. Why the two failure conditions are necessary

### 3.1 Radial lines

If \(b/Z_0\in\mathbb R\), the support line passes through the origin. Its
ordinary geometric phase has at most two directions, while Brownian motion
has a continuum of scalar states. A genuine phase cannot recover that
continuum. State-dependent additions of \(2\pi\) would be artificial winding,
not the ordinary continuous polar angle.

### 3.2 Noncollinear drift and diffusion

If \(a/b\notin\mathbb R\), the fixed-time support lines move in different
directions. Randomizing time over a nontrivial interval makes
\((\tau,W_\tau)\) have a two-dimensional density; the noncollinear affine map
then gives \(Z_\tau\) a planar density. A Borel polar graph

\[
\{r(\theta)e^{i\theta}:\theta\in\mathbb R\}
\]

has planar measure zero. It cannot carry that law. This randomized-time
argument avoids the invalid step of taking an uncountable union of
fixed-time null sets.

### 3.3 Time-dependent fallback

A noncollinear process can still be represented at nonsingular times as

\[
Z_t=Z_0R(t,\theta_t)e^{i\theta_t},
\]

with an explicit time-dependent line radius. This uses one random coordinate
plus deterministic time, not the requested time-independent \(r(\theta)\).
At the deterministic time when a support line crosses the origin, even that
single polar chart fails for the whole fixed-time support.

## 4. Which candidate to use

| Requirement | Appropriate candidate | Exact tradeoff |
|---|---|---|
| Preserve an eligible additive affine complex state exactly | General affine/secant phase | Radius depends on phase; phase spans one open half-turn |
| Embed a real arithmetic Brownian state losslessly in Euler form | Canonical secant lift | The complex lift is nonradial; it is not the literal real-axis process |
| Obtain constant radius and retain the scalar state | Cayley transform | Represents an invertible nonlinear transform, not the original additive complex state |
| Obtain ordinary \(e^{i\theta}\) with unrestricted winding and remain lossless | Compatible logarithmic spiral | Requires a multiplicative log-affine process |
| Encode state on a circle without retaining winding index | Wrapped exponential | Constant radius but lossy |
| Handle noncollinear affine drift and diffusion at most times | Moving-line radius \(R(t,\theta)\) | Explicit time remains; origin-crossing time is singular |
| Factor an arbitrary random variable measurably | Borel phase/radius factorization | May lack continuity, uniqueness, or \(C^2\) regularity for Itô calculus |

## 5. Constant radius and rotation

### 5.1 Cayley compactification

For a real scalar state \(Y_t\),

\[
U_t
=
\frac{1+iY_t/c}{1-iY_t/c}
=e^{i\Theta_t},
\qquad
\Theta_t=2\arctan(Y_t/c)\in(-\pi,\pi).
\]

This is lossless and has constant radius. The missing point \(-1\) represents
infinity and is inaccessible at finite time. However:

- \(U_t\) is a transformed state, not the original \(Z_t\);
- \(\Theta_t\) cannot wind through the missing point; and
- its angular diffusion is state dependent, so it is not ordinary Brownian
  motion on a circle.

### 5.2 Compatible logarithmic spiral

For

\[
Z_t=Z_0e^{\kappa t+BW_t},
\qquad B=\sigma+i\beta,
\]

a time-independent, lossless, winding phase exists exactly when

\[
\beta\ne0,\qquad \kappa=\gamma B,\quad\gamma\in\mathbb R.
\]

Then

\[
\theta_t=\beta(\gamma t+W_t),
\qquad
Z_t
=
Z_0
\exp\left(\frac{\sigma}{\beta}\theta_t\right)
e^{i\theta_t}.
\]

This phase can wind on the full real line. It resolves the winding requirement
by changing from an additive affine model to a compatible multiplicative
model.

## 6. Itô calculus and complex rotation

The symbolic similarity

\[
(dW_t)^2=dt,\qquad i^2=-1
\]

must be interpreted carefully:

- \(d[W,W]_t=dt\) is a quadratic-variation statement;
- finite Brownian increments do not satisfy
  \((\Delta W)^2=\Delta t\) pathwise;
- \(i^2=-1\) is an algebraic identity in \(\mathbb C\); and
- multiplication by \(i\) rotates a deterministic tangent vector but does not
  create another independent noise.

The useful bridge is not an identification of these squares. It is Itô's
formula applied to a complex curve:

\[
dF(\theta_t)
=
\left(F'm+\frac12F''s^2\right)dt+F's\,dW_t.
\]

The \(F''s^2/2\) term converts scalar quadratic variation into a geometric
drift correction. In the canonical secant map, that correction cancels the
nonlinear phase drift and reconstructs the original affine diffusion exactly.

## 7. What the representation genuinely adds

### 7.1 Mathematical value

Phase 5 establishes a single coherent package:

- a measurable factorization criterion;
- a gap-free affine existence and impossibility theorem;
- exact line geometry, inverse, domain, and uniqueness;
- the phase SDE in Itô and Stratonovich forms;
- generator, transition density, semigroup, and natural boundaries;
- Cayley and transported-group comparisons;
- a drift-complete line/spiral rigidity classification;
- the compatible winding multiplicative case; and
- the time-dependent fallback with its singular time.

Individual ingredients are elementary or classical coordinate-transform
ideas. The contribution claimed here is the rigorous synthesis and
classification around the user's exact representation requirements, not the
invention of polar form, arctangent compactification, the Cayley transform,
or diffusion transformations.

### 7.2 Geometric value

The complex form organizes tangents, normals, rotations, and invariant
checks. It makes the rank-one nature of the curve-valued noise transparent.
For the additive secant case, the represented curve is still a straight line
with zero curvature.

### 7.3 Numerical value

The experiments show:

- independent nonlinear SDE schemes converge with their expected strong
  orders;
- exact phase steps respect the natural interval where naive Euler may fail;
- the Cayley transform preserves unit modulus exactly;
- arctangent compactification improved central-region heat-equation accuracy
  at matched grid size in the tested case; and
- the improvement was scale dependent and accompanied by worse conditioning.

They also show that a lossless phase round trip leaves ordinary Monte Carlo,
quasi-Monte Carlo, and importance-sampling estimators unchanged sample by
sample and adds trigonometric work.

## 8. What it does not add

Phase 5 does not support any of the following claims:

- a second stochastic dimension is created by complex notation;
- additive Brownian motion undergoes unlimited lossless rotation;
- the Cayley image is the original process or circular Brownian motion;
- complex embedding makes arbitrary payoffs holomorphic;
- terminal phase records an entire Brownian path;
- a coordinate change automatically reduces Monte Carlo variance;
- compactification is universally better conditioned;
- a previously numerical-only stochastic problem has become analytic; or
- numerical agreement proves a theorem or a novelty claim.

The vector and derivative analysis is in
[PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md](PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md).
The matched numerical comparisons are in
[PHASE_5_NUMERICAL_IMPLICATIONS.md](PHASE_5_NUMERICAL_IMPLICATIONS.md).

## 9. Verification summary

The implemented model passed 23 Phase 5 tests and 33 tests in the full
project suite. After the final review corrections, the notebook executed
three times from clean kernels with 18
sequential code cells, zero error outputs, two independent seed families, and
byte-identical CSV/JSON evidence. Its aggregate ordered-evidence SHA-256 hash
was:

```text
fa8fd5f517c9f321f3426cfdbd5fe2e9f8bea4e213ad945a8207a87a9736619e
```

Key measured values and limitations are reported in
[PHASE_5_SIMULATION_RESULTS.md](PHASE_5_SIMULATION_RESULTS.md).

## 10. Novelty boundary

The literature review places the work beside classical results on:

- Itô transformations and one-dimensional diffusion coordinates;
- support and hypoellipticity;
- projected-normal and angular Gaussian distributions;
- Cayley compactification and Brownian winding;
- exact diffusion simulation and geometric integration;
- unbounded-domain coordinate maps;
- Wirtinger derivatives; and
- complex-step differentiation.

No claim is made that the secant identity or Cayley map is new. The strongest
defensible research claim is:

> Phase 5 gives a complete, drift-aware classification and comparative
> verification of lossless one-phase Euler forms for the specified
> one-driver additive and compatible multiplicative models.

Even that statement is presented as a synthesis derived here, not as a claim
of priority. See
[PHASE_5_LITERATURE_REVIEW.md](PHASE_5_LITERATURE_REVIEW.md).

## 11. Open questions

1. For a specified unbounded-domain PDE, how should the phase scale \(c\) be
   selected optimally from error and conditioning estimates?
2. Can a phase coordinate enable a useful control variate or smoothing
   strategy for a nonsmooth payoff, beyond a lossless round trip?
3. Which genuinely curved manifold-valued SDEs admit similarly explicit
   phase-amplitude coordinates and invariant-preserving exact steps?
4. Can the line/spiral rigidity classification be extended to
   multidimensional drivers, time-dependent coefficients, or jump processes?
5. Under what genuine analyticity assumptions do complex semigroup methods
   yield more than a notational reformulation?
6. Can topology-preserving maps improve long-time numerical behavior in a
   model with actual recurrent rotation?

These are separate research problems. Their answers cannot be inferred from
the affine identity alone.

## 12. Final answer

The requested one-stochastic-variable Euler form exists exactly for
nonradial, fixed affine support lines. In its cleanest canonical version,

\[
\boxed{
\mathcal Z_t
=
Z_0\sec\theta_t\,e^{i\theta_t},
\qquad
X_t=X_0+c\tan\theta_t.
}
\]

Thus \(r_{\theta_t}=\sec\theta_t\), and \(\theta_t\) is the only stochastic
state coordinate in the displayed formula. For the general original affine
complex process, replace the secant by
\(\sin\phi/\sin(\phi-\theta_t)\) and impose
\(a/b\in\mathbb R\), \(b/Z_0\notin\mathbb R\).

This is an exact and useful geometric representation. Its rotation is a
bounded half-turn for the additive model; unlimited lossless winding belongs
to a different, compatible multiplicative spiral model.
