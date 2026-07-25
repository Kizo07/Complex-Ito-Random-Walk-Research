# Phase 5 Plan: A One-Phase Euler Representation of Additive Brownian Motion

**Status:** Proposed — awaiting user approval  
**Date:** 2026-07-24  
**Scope:** Phase 5 only; this document authorizes no implementation  
**Working title:** *Encoding Additive Brownian Motion in One Euler Phase*  
**Primary objective:** Determine rigorously when an additive one-driver process

\[
Z_t=Z_0+a t+bW_t
\]

can be written exactly as

\[
Z_t=Z_0\,r(\theta_t)e^{i\theta_t},
\]

where \(\theta_t\) is the only stochastic state variable in the final state
formula and \(r\) is either constant or a deterministic function of
\(\theta_t\).

## 1. Motivation and precise interpretation

Phase 4 packaged \(t\) and \(W_t\) inside a complex exponential, but it did not
eliminate them as separate coordinates of the exponent. It also reduced, up
to deterministic rotation, to a deterministic transformation of an ordinary
one-factor GBM. Phase 5 returns to the additive process and asks a more exact
question:

> Can all state randomness be encoded by one real phase, just as
> \(a+ib=r e^{i\theta}\) encodes a complex number by modulus and angle?

The phrase “no \(t\) or \(W_t\)” must be separated into two claims:

1. **State representation:** the displayed state
   \(Z_t=Z_0r(\theta_t)e^{i\theta_t}\) contains no explicit \(t\) or \(W_t\).
2. **Process specification:** the law or dynamics of \(\theta_t\) must still
   specify the passage of time and the source of randomness. These cannot be
   removed from a nontrivial stochastic process; they can instead be encoded
   in an SDE, generator, semigroup, or exact transition kernel for
   \(\theta_t\).

Phase 5 will call a representation successful only if the first claim holds
exactly and the second is supplied rigorously without pretending that
randomness has disappeared.

Throughout the main result, “Euler form” will mean

\[
r(\theta)e^{i\theta},
\qquad r(\theta)\geq0,\quad \theta\in\mathbb R,
\]

not the Euler--Maruyama numerical method.

## 2. Central working construction

Begin with arithmetic Brownian motion

\[
X_t=X_0+\mu t+\sigma W_t
\]

with the conventional \(\sigma>0\), and choose \(c>0\) and
\(Z_0\in\mathbb C\setminus\{0\}\). Consider the nonradial affine lift

\[
\mathcal Z_t
=
Z_0\left(1+i\frac{X_t-X_0}{c}\right)
=
Z_0+\frac{i\mu Z_0}{c}t+\frac{i\sigma Z_0}{c}W_t.
\]

The candidate phase and radius are

\[
\theta_t=\arctan\left(\frac{X_t-X_0}{c}\right),
\qquad
r(\theta)=\sec\theta,
\qquad
-\frac{\pi}{2}<\theta<\frac{\pi}{2}.
\]

The proposed exact state identity is

\[
\boxed{
\mathcal Z_t=Z_0\sec(\theta_t)e^{i\theta_t}.
}
\]

The inverse relation is

\[
\boxed{
X_t=X_0+c\tan\theta_t.
}
\]

For standard Brownian motion, set \(\mu=0\) and \(\sigma=1\). This construction
is the leading candidate because it is exact, injective, time-independent as a
state map, and uses only \(\theta_t\) as its stochastic coordinate.

It must not be oversold: it is a complex affine lift of the original real
Brownian motion, not a claim that a real-axis Brownian path acquires a
nontrivial ordinary polar angle without an offset.

## 3. Candidate representations to compare

### Candidate A — Secant affine-line representation

\[
\mathcal Z_t=Z_0\sec(\theta_t)e^{i\theta_t}.
\]

**Expected strengths:** preserves an additive affine complex process exactly;
is invertible; gives a deterministic phase-dependent radius; admits an exact
transition law.

**Expected limitations:** requires a line that misses the origin; the phase is
confined to an interval of length \(\pi\), so it describes angular position
rather than unlimited winding; the radius cannot be constant.

### Candidate B — Cayley or stereographic constant-radius encoding

\[
U_t
=
\frac{1+i(X_t-X_0)/c}{1-i(X_t-X_0)/c}
=e^{i\Theta_t},
\qquad
\Theta_t=2\arctan\left(\frac{X_t-X_0}{c}\right).
\]

**Expected strengths:** constant unit radius; invertible for every finite
Brownian state; uses one stochastic angle.

**Expected limitations:** \(U_t\) is a nonlinear Möbius transformation of the
additive process, not the original \(Z_0+a t+bW_t\); its phase dynamics are not
ordinary circular Brownian motion; the missing circle point represents
infinity.

### Candidate C — Pure circular exponential

\[
U_t=e^{i\lambda(X_t-X_0)}.
\]

**Expected strengths:** constant radius; ordinary addition becomes complex
multiplication; it produces genuine repeated rotation and winding.

**Expected limitations:** it is not injective and recovers the Brownian state
only modulo \(2\pi/\lambda\). It therefore fails exact global recovery.

### Recommended Phase 5 focus

Candidate A is the primary answer to the exact affine-process requirement.
Candidates B and C will be rigorous comparators that expose the unavoidable
tradeoff among:

1. preserving the original affine process;
2. constant radius;
3. injective recovery of the Brownian state; and
4. ordinary multiplication representing additive increments.

The research must determine whether this tradeoff is already formalized in
the literature and must state it as established theory when appropriate.

## 4. Deep-research programme

Research will precede theorem writing and simulation. The first gate is a
prior-art and triviality audit, added specifically to avoid repeating the
Phase 4 novelty problem.

### 4.1 Literature families

Search primary mathematical literature for:

1. Brownian motion under smooth one-dimensional coordinate transformations;
2. arctangent-transformed Brownian motion and transformed Gaussian diffusions;
3. stereographic projection and Cayley or Möbius transforms of Brownian
   motion;
4. diffusion processes on the circle, the punctured circle, and compactified
   real line;
5. polar equations of affine lines and star-shaped curves;
6. projected-normal, angular-Gaussian, wrapped-normal, and related directional
   distributions;
7. conjugacy of Markov generators and semigroups under diffeomorphisms;
8. Feller boundary classification for transformed diffusions on bounded open
   intervals;
9. transported group laws, Lie-group structures isomorphic to
   \((\mathbb R,+)\), and the tangent-addition coordinate;
10. topological or group-theoretic obstructions to an injective continuous
    homomorphism from \((\mathbb R,+)\) into the ordinary unit-circle group;
11. complex affine Brownian processes and one-dimensional support in
    \(\mathbb C\); and
12. exact simulation and numerical convergence for state-transformed SDEs.

Initial search phrases will include:

- “arctangent of Brownian motion diffusion”;
- “stereographic projection Brownian motion circle”;
- “Cayley transform Brownian motion unit circle”;
- “Brownian motion compactification real line”;
- “Möbius transformed Brownian motion”;
- “transformed Brownian motion transition density”;
- “polar equation affine line secant”;
- “tangent group law real line interval”;
- “diffusion natural boundary arctan transform”; and
- “injective homomorphism real line circle group.”

### 4.2 Source standards

The research record will:

- prioritize original papers, monographs, and authoritative textbook
  treatments over summaries;
- record full bibliographic metadata, DOI or stable URL, exact pages, and the
  role of each source;
- distinguish a source that proves a result from one that merely uses it;
- retain a claim-to-source matrix;
- quote no source beyond copyright-safe limits;
- document unsuccessful searches where terminology is ambiguous;
- distinguish ordinary one-dimensional Brownian motion from planar Brownian
  motion and ordinary circular Brownian motion; and
- state explicitly which parts of `possible_solution.md` are established,
  elementary consequences of established theory, corrected, or unsupported.

### 4.3 Prior-art and contribution gate

Before proceeding to a synthesis, answer:

1. Does the exact secant representation already appear in this form?
2. Is the phase diffusion known under a standard name?
3. Is the claimed existence theorem a known fact about polar graphs or
   star-shaped sets?
4. Is the Cayley comparator standard in stochastic-process literature?
5. Is the transported angle operation a known Lie-group coordinate?
6. Is there any nontrivial new result, or is Phase 5 best framed as a rigorous
   explanatory synthesis?

No novelty claim will survive unless this audit gives positive evidence for
it.

## 5. Mathematical programme

### 5.1 Formalize the representation problem

Specify:

- \(Z_0\neq0\);
- \(a,b\in\mathbb C\);
- \(b\neq0\) for the stochastic case;
- a real-valued phase process \(\theta_t\);
- a deterministic, single-valued, time-independent radius
  \(r:D\to[0,\infty)\);
- the reachable phase domain \(D\), rather than silently defining the polar
  formula on all of \(\mathbb R\);
- the phase branch and initial condition;
- exact equality pathwise for all finite times; and
- whether the representation must be injective and recover the original
  additive coordinate.

Analyze separately what changes if one permits a signed radius, a
time-dependent radius, a multivalued phase, or equality only in distribution.

### 5.2 Prove the secant construction

Establish pathwise:

\[
1+i\tan\theta=\sec\theta\,e^{i\theta}
\]

on the correct branch, prove that \(\sec\theta>0\), and prove the inverse
formula. Show that the affine line remains a positive distance from the
origin and that the phase never reaches \(\pm\pi/2\) at a finite time.

### 5.3 Prove the general affine-line theorem

For

\[
Z_t=Z_0+a t+bW_t,
\]

investigate and either prove or correct the proposed criterion

\[
\frac{a}{b}\in\mathbb R,
\qquad
\frac{b}{Z_0}\notin\mathbb R.
\]

The proof must address:

- sufficiency through the polar equation of the fixed affine line;
- necessity of real collinearity of \(a\) and \(b\);
- necessity that the line miss the origin;
- the exact reachable angle interval;
- positivity of
  \[
  r(\theta)=\frac{\sin\phi}{\sin(\phi-\theta)};
  \]
- phase continuity and branch uniqueness;
- support in \(\mathbb C\) versus sample-path range;
- \(a=0\), \(b=0\), \(Z_0=0\), radial direction, and zero-hitting cases; and
- whether the theorem remains “if and only if” under every stated
  regularity and injectivity assumption.

The proof will not rely on a dimension-counting slogan alone. It will use the
support of \(W_t\), the geometry of polar graphs, and the fact that a
single-valued nonnegative radius assigns at most one radius to each unwrapped
phase value.

### 5.4 Prove the direct real-axis obstruction

Show precisely why a nondegenerate real Brownian motion cannot use its own
ordinary polar angle as its only stochastic coordinate: away from zero the
angle contains only the sign, while the magnitude has a continuum of values.
Address whether unwrapped angles, signed radii, zero crossings, or local time
alter this conclusion.

### 5.5 Derive phase dynamics independently

From

\[
\theta_t=\arctan\left(\frac{X_t-X_0}{c}\right),
\]

derive with Itô's lemma:

\[
d\theta_t
=
\left[
\frac{\mu}{c}\cos^2\theta_t
-
\frac{\sigma^2}{c^2}\sin\theta_t\cos^3\theta_t
\right]dt
+
\frac{\sigma}{c}\cos^2\theta_t\,dW_t.
\]

Independently derive:

- the Stratonovich form;
- the infinitesimal generator;
- the transformed Kolmogorov forward equation;
- quadratic variation;
- the scale and speed measures if useful for boundary classification; and
- the standard-Brownian specialization \((\mu,\sigma)=(0,1)\).

Verify each derivation in both directions by applying Itô's lemma to
\(X_t=X_0+c\tan\theta_t\).

### 5.6 Derive the exact phase law

Derive the exact transition

\[
\theta_{s+h}
=
\arctan\left(
\tan\theta_s+\frac{\mu}{c}h
+\frac{\sigma}{c}\sqrt h\,\xi
\right),
\qquad \xi\sim N(0,1),
\]

and its change-of-variables density. Prove:

- normalization;
- the required \(|\sigma|\) Jacobian factor if signed diffusion
  coefficients are permitted instead of adopting \(\sigma>0\);
- the Chapman--Kolmogorov property;
- equivalence with the transformed Gaussian semigroup;
- the exact fixed-time CDF and quantile function;
- the natural/inaccessible character of the endpoints, if confirmed by the
  boundary analysis; and
- the distinction between this process and ordinary Brownian motion on a
  circle.

### 5.7 Analyze the transported addition law

For

\[
\theta_1\oplus\theta_2
=
\arctan(\tan\theta_1+\tan\theta_2),
\]

determine the correct scaled form and prove closure, associativity,
commutativity, identity, inverse, and isomorphism with \((\mathbb R,+)\) on the
open phase interval. Clarify that \(\oplus\) is not ordinary addition modulo
\(2\pi\).

### 5.8 Establish the constant-radius tradeoff

Prove that a nondegenerate affine Brownian process cannot itself have constant
modulus. Then analyze:

- the Cayley transform as an injective constant-radius encoding;
- the missing circle point and its relation to infinity;
- the induced phase SDE and transition law;
- why it is not ordinary circular Brownian motion;
- why \(e^{i\lambda X_t}\) converts addition to multiplication but loses
  injectivity; and
- the precise impossibility of simultaneously retaining the original affine
  state, constant radius, global injectivity, and ordinary multiplicative
  composition.

## 6. Symbolic and analytic verification

The implementation phase will maintain independent derivation routes:

1. elementary trigonometric/polar geometry;
2. real two-dimensional affine-line geometry;
3. Itô's lemma applied to the forward phase map;
4. Itô's lemma applied to the inverse tangent map;
5. generator conjugacy under the diffeomorphism;
6. transition-density change of variables; and
7. symbolic algebra checks for drift, diffusion, inverse identities, and
   general-line formulas.

Acceptance requires agreement among these routes. Numerical experiments will
support these proofs but will not replace them.

## 7. Reproducible notebook and simulation plan

Create a new executed notebook dedicated to Phase 5. It will use the existing
approved conda environment without installing or mutating packages, fixed
seeds, explicit package versions, and clean top-to-bottom execution.

### 7.1 Exact pathwise identity

Using shared Brownian paths, compare:

\[
\mathcal Z_t=Z_0\left(1+i\frac{X_t-X_0}{c}\right)
\]

with

\[
\mathcal Z_t=Z_0\sec\theta_t e^{i\theta_t}.
\]

Report maximum absolute and relative reconstruction errors, including
stress tests near the phase boundaries.

### 7.2 Independent phase-SDE cross-validation

Simulate the nonlinear phase SDE directly with the same Brownian increments,
without calling the closed-form arctangent map inside the update. Compare it
with the exact transformed path and estimate strong convergence across
multiple step sizes. Include:

- Euler--Maruyama;
- Milstein if its independently derived correction is stable; and
- a suitable Stratonovich scheme for checking the Stratonovich formula.

This is the principal non-circular empirical check.

### 7.3 Transition-law verification

For several starting phases, horizons, drifts, volatilities, and values of
\(c\):

- compare empirical and analytic phase CDFs;
- use probability-integral-transform and quantile checks;
- report uncertainty, Monte Carlo standard errors, and test statistics;
- numerically integrate the transition density to one;
- test Chapman--Kolmogorov by numerical quadrature; and
- compare small-time conditional moments with the generator coefficients.

### 7.4 Boundary and scale behavior

Demonstrate that finite paths remain in the open phase interval, quantify
approach toward the endpoints for large \(|X_t|\), and study how \(c\) changes
coordinate compression without changing the recovered Brownian process.

### 7.5 General affine-line cases

Test:

- perpendicular and oblique nonradial lines where the theorem predicts
  success;
- collinear drift and diffusion with different scales;
- a radial line through the origin;
- noncollinear complex \(a\) and \(b\);
- degenerate deterministic and zero-noise cases; and
- branch-sensitive cases.

Successful cases must reconstruct to floating-point accuracy. Failed cases
must be illustrated as violations of a stated theorem hypothesis, not merely
as plots that look different.

### 7.6 Comparator experiments

Compare the secant, Cayley, and pure circular exponential encodings on the
same Brownian paths:

- radius behavior;
- invertibility and reconstruction error;
- phase range and winding;
- increment-composition law; and
- information loss under periodic identification.

### 7.7 Notebook reproducibility gates

- Execute twice from clean kernels.
- Require sequential execution counts and zero error outputs.
- Compare deterministic output hashes or structured evidence tables.
- Use vector figures with raster companions if publication work follows.
- Record every parameter and horizon locally with the experiment.
- Avoid circular “validation” claims when samples come directly from the
  formula being checked.

## 8. Planned Phase 5 deliverables

Subject to approval and later implementation planning:

1. `PHASE_5_LITERATURE_REVIEW.md` — verified primary-source audit and
   claim-to-source matrix;
2. a rigorous derivation chapter for the secant affine-line representation;
3. a theorem chapter for existence, impossibility, branch, and degenerate
   cases;
4. a comparator chapter for Cayley, circular-exponential, and group-law
   encodings;
5. a focused tested Python model module;
6. unit tests for all symbolic and numerical identities;
7. a deterministic notebook builder and executed Phase 5 notebook;
8. `PHASE_5_SIMULATION_RESULTS.md`;
9. `PHASE_5_SYNTHESIS.md`; and
10. an OpenCode `zai-coding-plan/glm-5.2` independent review and second
    opinion after Codex verification.

A technical paper is not automatically part of Phase 5. It should be planned
separately after the mathematical and computational work survives review.

## 9. Final communication requirement

The Phase 5 synthesis must begin with a short, self-contained paragraph that
directly answers the user's question. Its content should be equivalent to:

> A real Brownian motion on the real axis cannot store its full magnitude in
> its ordinary polar angle, but an exact nonradial complex affine lift can.
> For \(c>0\), define
> \(\mathcal Z_t=Z_0[1+i(X_t-X_0)/c]\) and
> \(\theta_t=\arctan((X_t-X_0)/c)\). Then
> \(\mathcal Z_t=Z_0\sec(\theta_t)e^{i\theta_t}\), so the displayed Euler form
> contains only the stochastic phase, while
> \(X_t=X_0+c\tan\theta_t\) recovers the original Brownian state exactly.
> The radius is therefore \(r(\theta)=\sec\theta\); a constant radius is
> possible only after changing the affine process through a nonlinear
> encoding such as the Cayley transform.

The detailed report will then explain the assumptions, phase law, exact
transition, literature status, and limitations.

## 10. Acceptance criteria

Phase 5 will be complete only when:

1. the literature audit identifies prior art and fixes the novelty boundary;
2. the exact state formula contains no explicit \(t\) or \(W_t\);
3. \(\theta_t\) is the only stochastic coordinate and exactly recovers the
   original scalar state;
4. the secant identity is proved pathwise;
5. the general affine existence criterion is proved or corrected;
6. real-axis, zero-crossing, branch, positivity, and degenerate cases are
   resolved;
7. the phase SDE, inverse SDE, generator, and exact transition law agree;
8. the endpoint behavior and distinction from circular Brownian motion are
   explicit;
9. the constant-radius and composition tradeoffs are proved;
10. independent SDE simulations converge to the exact phase construction;
11. transition and semigroup checks pass within prespecified numerical
    tolerances;
12. two clean notebook executions reproduce all deterministic evidence;
13. simulations are reported with uncertainty and are not presented as
    substitutes for proof;
14. OpenCode GLM 5.2 finds no unresolved critical or major mathematical
    issue; and
15. the synthesis begins with the requested short-paragraph answer.

## 11. Constraints

- Do not modify the completed Phase 3 or Phase 4 mathematics while carrying
  out Phase 5.
- Preserve all existing user-supplied review and critique files.
- Do not claim that a coordinate transformation creates new randomness.
- Do not call the phase diffusion ordinary circular Brownian motion.
- Do not claim unlimited rotation for the secant phase, whose reachable
  interval has length \(\pi\).
- Do not claim that \(t\) and stochastic forcing disappear from the process
  law merely because they disappear from the state identity.
- Keep \(d[W,W]_t=dt\), finite-increment approximations, and \(i^2=-1\)
  conceptually distinct.
- Use the standing Codex-direct implementation exception if the user later
  approves execution; do not delegate implementation.
- Use OpenCode GLM 5.2 only for independent review and second opinion.
- Do not commit, push, open a pull request, or publish unless separately
  requested.

## 12. Approval gate

No Phase 5 research, derivation, code, notebook, simulation, or publication
work begins until the user approves this plan.
