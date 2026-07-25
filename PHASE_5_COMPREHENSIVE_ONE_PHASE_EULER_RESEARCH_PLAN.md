# Phase 5 Comprehensive Research Plan: One-Phase Euler Representations and Their Consequences

**Status:** Proposed — awaiting user approval  
**Date:** 2026-07-24  
**Scope:** Phase 5 research, mathematics, computation, and implications only  
**Planning status:** This document authorizes no research execution,
derivation, code, simulation, publication, commit, or external review  
**Relationship to the earlier plan:** This is a new, expanded successor to
`PHASE_5_ONE_PHASE_EULER_BROWNIAN_PLAN.md`. The earlier plan remains preserved
as a historical draft.  
**Working title:** *One-Phase Euler Coordinates for Brownian Motion: Exact
Representations, Rigidity, and Computational Consequences*

## 1. Central objective

The first objective is to determine exactly when the additive one-driver
complex process

\[
Z_t=Z_0+a t+bW_t
\]

admits a lossless, time-independent, one-phase Euler representation

\[
\boxed{
Z_t=Z_0\,r(\theta_t)e^{i\theta_t},
}
\]

where:

- \(\theta_t\) is the only stochastic state variable appearing in the final
  state formula;
- \(\theta_t\) is real;
- \(r\) is real, nonnegative, deterministic, single-valued, and has no
  explicit time dependence;
- the identity holds pathwise for the complete process, not merely at one
  time or along one selected sample path; and
- the original Brownian state can be recovered from \(\theta_t\) whenever
  “lossless” is claimed.

The second objective is to compare every serious alternative raised by:

- `possible_solution.md`;
- `single-phase-euler-representation.md`; and
- `exact_one_phase_euler_representation_additive_brownian_motion.md`.

The third objective is to investigate, without presuming a positive answer,
whether these representations have consequences beyond a coordinate change:

1. Do they unlock useful vector or geometric mathematics for stochastic
   calculus?
2. Do they simplify complex differentiation or complex-valued stochastic
   problems?
3. Do they convert any presently numerical-only stochastic problems into
   analytically solvable ones?
4. Do they materially improve simulation, PDE solution, stability,
   conditioning, variance, or geometric preservation?

The standard for a positive answer to any of these questions is a proved
result or a reproducible measured advantage. Visual elegance or rewriting a
known scalar process in complex notation will not count.

## 2. The exact meaning of “one stochastic phase”

Phase 5 will distinguish the following increasingly strong properties.

### Level 0 — Ordinary polar decomposition

\[
Z_t=R_te^{i\Theta_t},
\]

where both \(R_t\) and \(\Theta_t\) may be stochastic. This is always available
away from zero and does not answer the research question.

### Level 1 — Phase-determined radius

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t},
\]

with deterministic \(r\). The complex state lies on one polar graph, but the
map from the original state to \(\theta\) need not be injective.

### Level 2 — Lossless one-phase encoding

There is a deterministic inverse

\[
X_t=G(\theta_t)
\]

or an equivalent inverse for the original scalar driver. At this level the
phase filtration and original-state filtration can be compared precisely.

### Level 3 — Time-independent state map

The radius is \(r(\theta)\), not \(R(t,\theta)\). A moving affine line or
time-dependent deterministic rotation is therefore excluded.

### Level 4 — Phase-first Markov construction

The phase is defined intrinsically by an SDE, generator, martingale problem,
semigroup, or transition kernel. The final complex state does not need
\(W_t\) as a second state coordinate.

### Level 5 — Homomorphic increment composition

Addition of the underlying real coordinate is transported either to:

- ordinary complex multiplication; or
- a clearly defined nonlinear phase operation such as \(\oplus\).

These are different properties and must not be described as equivalent.

### Level 6 — Constant radius

\[
r(\theta)\equiv r_0.
\]

This is the strongest geometric restriction and is generally incompatible
with preserving a nontrivial additive affine process.

Every theorem and experiment will state which levels it proves. This prevents
claims about “one phase” from silently changing meaning between sections.

## 3. Candidate catalogue

No candidate is accepted merely because it appears in one of the supplied
documents.

### Candidate A — Canonical secant affine lift

For arithmetic Brownian motion

\[
X_t=X_0+\mu t+\sigma W_t,
\]

choose \(c>0\), \(Z_0\neq0\), and define

\[
\mathcal Z_t
=
Z_0\left(1+i\frac{X_t-X_0}{c}\right).
\]

The proposed phase representation is

\[
\theta_t=\arctan\left(\frac{X_t-X_0}{c}\right),
\qquad
\mathcal Z_t=Z_0\sec(\theta_t)e^{i\theta_t},
\]

with inverse

\[
X_t=X_0+c\tan\theta_t.
\]

This is the primary candidate when the additive law must be preserved.

### Candidate B — General oblique affine-line representation

If

\[
\frac{a}{b}\in\mathbb R,
\qquad
\frac{b}{Z_0}=\rho e^{i\phi}\notin\mathbb R,
\]

the proposed general radius is

\[
r(\theta)
=
\frac{\sin\phi}{\sin(\phi-\theta)}
\]

on a specific reachable interval of length \(\pi\). This is the general
additive candidate and the proposed source of an if-and-only-if theorem.

### Candidate C — Brownian motion retained in the real coordinate

\[
\widetilde Z_t=ic+X_t-X_0,
\qquad
\theta_t=-\arctan\left(\frac{X_t-X_0}{c}\right),
\]

so

\[
\widetilde Z_t=ic\,\sec(\theta_t)e^{i\theta_t}.
\]

For standard Brownian motion:

\[
ic+W_t=ic\,\sec(\theta_t)e^{i\theta_t},
\qquad
W_t=-c\tan\theta_t.
\]

This candidate most literally leaves \(W_t\) in a Cartesian component while
still requiring the nonreal offset \(ic\).

### Candidate D — Cayley or stereographic compactification

\[
U_t
=
\frac{1+i(X_t-X_0)/c}{1-i(X_t-X_0)/c}
=e^{i\Theta_t},
\qquad
\Theta_t=2\arctan\left(\frac{X_t-X_0}{c}\right).
\]

This is constant-radius and invertible for every finite real state. It is not
the original additive process; it is a nonlinear encoding of it.

### Candidate E — Wrapped circular phase

\[
U_t=e^{i\lambda(X_t-X_0)}.
\]

This gives unrestricted angular winding and ordinary multiplication of
increments, but it loses information modulo \(2\pi/\lambda\).

### Candidate F — Logarithmic-spiral multiplicative representation

\[
Z_t
=
Z_0e^{\kappa t+BW_t},
\qquad
B=\sigma+i\beta.
\]

When the log-drift and log-diffusion are real-collinear,

\[
\kappa=\gamma B,
\qquad
\beta\neq0,
\]

the proposed one-phase form is

\[
\boxed{
Z_t
=
Z_0e^{(\sigma/\beta)\theta_t}e^{i\theta_t},
\qquad
\theta_t=\beta(\gamma t+W_t).
}
\]

Here the phase itself is drifted Brownian motion, has unbounded range, and can
wind indefinitely. This is multiplicative rather than additive and appears
to coincide with the restricted Phase 3 construction. It must therefore be
treated as an alternative answer, not silently substituted for the user's
additive requirement.

### Candidate G — Arbitrary polar-curve design

Choose

\[
F(\theta)=r(\theta)e^{i\theta}
\]

and a scalar phase diffusion

\[
d\theta_t=m(\theta_t)dt+s(\theta_t)dW_t.
\]

Then formally

\[
dZ_t
=
Z_0\left[
F'(\theta_t)m(\theta_t)
+\frac12F''(\theta_t)s(\theta_t)^2
\right]dt
+
Z_0F'(\theta_t)s(\theta_t)dW_t.
\]

This is a design dictionary only when the regularity, existence, uniqueness,
nonvanishing, branch, and inverse conditions are made explicit.

### Candidate H — Time-dependent moving-line fallback

When \(a\) and \(b\) are not real-collinear, a time-independent radius may
fail, but a representation

\[
Z_t=Z_0R(t,\theta_t)e^{i\theta_t}
\]

may still exist by using the polar equation of the time-dependent support
line. This candidate relaxes Level 3 while retaining one stochastic state
variable. It requires a separate analysis of times when the moving line
passes through the origin.

## 4. Candidate comparison questions

For every candidate, answer the same questions:

1. Does it preserve the original additive process exactly?
2. Is it an embedding, a reparameterization, or a nonlinear transformation?
3. Is the radius deterministic?
4. Is the radius time-independent?
5. Is the radius constant?
6. Is the phase the geometric argument modulo \(2\pi\)?
7. Is the phase principal, continuous, or unwrapped?
8. Is the phase map injective?
9. Is the original Brownian state recoverable?
10. Do the generated filtrations coincide?
11. What is the exact phase state space?
12. Can the phase wind?
13. Are any boundary points reachable in finite time?
14. Does ordinary addition become ordinary multiplication?
15. If not, what transported operation is required?
16. Is the process Markov in the phase coordinate alone?
17. What is its generator and transition kernel?
18. What local covariance rank does it have?
19. Does the construction introduce any stochastic information?
20. Which claims are classical, which are derived, and which may be novel?

The comparison will be recorded as a generated evidence table, not only as
prose.

## 5. Required audit of `single-phase-euler-representation.md`

Every section of this candidate document will receive a claim-level audit.

### Section 0 — Executive summary

- Verify the assertion that all symbolic identities in `possible_solution.md`
  are correct.
- Reconcile that assertion with the later admission of a major proof gap.
- Check all reported numerical tolerances and determine whether the scripts or
  raw evidence exist.
- Audit the claim that the logarithmic-spiral construction is the “best”
  answer against the requirement that the original process remain additive.
- Verify the claim that Phase 3 already supplies a single-phase Euler form.
- Verify the claim that Phase 4's extra deterministic rotation destroys a
  time-independent single-spiral representation.

### Section 1 — Precise statement

- Require \(r\) to be Borel for measurability.
- Decide when stronger continuity, local absolute continuity, \(C^1\), or
  \(C^2\) hypotheses are necessary.
- Separate a principal phase from a continuous lift.
- Define a polar graph when an unwrapped phase revisits the same geometric
  ray.
- Exclude set-theoretic encodings that make the problem vacuous.
- State the exact quantifier: pathwise for all \(t\), almost surely for every
  fixed \(t\), or indistinguishably as processes.

### Section 2 — “Argument monotonicity” master criterion

Treat the stated theorem as provisional. In particular:

- Test whether injectivity of the argument lift is truly necessary for a
  phase-determined radius.
- Examine counterexamples where the argument lift is noninjective but the
  modulus is constant on every argument fiber.
- Derive the more general factorization condition
  \[
  |f(s)|=r(\vartheta(s)),
  \]
  meaning that \(|f|\) must be constant on fibers of the selected argument
  lift.
- Distinguish existence of a polar representation from lossless recovery of
  \(S_t\). Injectivity may be necessary for the latter but not the former.
- State measurable-factorization conditions and verify that the resulting
  \(r\) is Borel.
- Clarify what “the range of \(S\) is an interval” means: path range, state
  space, or topological support of a fixed-time law.

### Section 3 — Additive line/secant family

- Prove or correct the full-support argument.
- Verify the equivalent conditions
  \[
  \operatorname{Im}(a\overline b)=0,
  \qquad
  \operatorname{Im}(b\overline{Z_0})\neq0.
  \]
- Verify the oblique radial formula and inverse map.
- Derive the perpendicular-foot form and check its orientation convention.
- Prove the reachable phase interval has exactly length \(\pi\).
- Establish that the additive phase cannot wind.
- Classify both endpoints using one-dimensional diffusion boundary theory.
- Verify the general phase SDE, including signs when
  \(\operatorname{Im}(b/Z_0)<0\).
- Verify the claimed scale function and identify the speed measure.

### Section 4 — Measure-theoretic impossibility theorem

- Reconstruct the Borel-image and polar-Fubini null-set proof.
- Verify that a Borel image of \(\mathbb R\) is analytic and universally
  measurable in the form required.
- Check the treatment of \(r=0\), the origin, negative radius, and repeated
  unwrapped angles.
- Replace “uniform on \(T\)” when \(T\) is an arbitrary positive-measure set
  by a precisely normalized density on a finite positive-measure subset.
- Handle \(t=0\), where \(W_t\) has no ordinary density.
- Prove that \((\tau,W_\tau)\) has the asserted joint density.
- Prove that the real-affine map \((t,w)\mapsto Z_0+at+bw\) is invertible
  exactly when \(\operatorname{Im}(a\overline b)\neq0\).
- State whether the theorem proves impossibility for all \(t\), almost every
  \(t\), or a set of positive measure.
- Use the numerical angle-bin experiment only as an illustration, not proof.

### Section 5 — Multiplicative/logarithmic-spiral family

- Prove the condition \(\kappa=\gamma B\) with \(\gamma\in\mathbb R\).
- Treat separately \(\beta=0\), \(\sigma=0\), \(B=0\), and pure circular
  rotation.
- Verify the formula
  \[
  r(\theta)=e^{(\sigma/\beta)\theta}.
  \]
- Prove injectivity conditions for the spiral.
- Compare unrestricted winding with the bounded additive phase.
- Map the construction exactly onto Phase 3 parameters.
- Show precisely how a deterministic Phase 4 rotation makes the support curve
  time-dependent unless the Phase 3 compatibility relation holds.
- Keep this result separate from the primary additive theorem.

### Section 6 — Claimed line/spiral rigidity theorem

Treat the classification as unproved until all coefficient equations are
satisfied.

- For multiplicative dynamics, use both:
  \[
  \frac{F's}{F}=B
  \]
  and
  \[
  \frac{F'm+\tfrac12F''s^2}{F}=A.
  \]
- Determine whether constant \(B\) forces both \(s\) and \(r'/r\) constant.
- Determine what constant \(A\) additionally forces on \(m\).
- For additive dynamics, use both:
  \[
  F's=b/Z_0
  \]
  and
  \[
  F'm+\tfrac12F''s^2=a/Z_0.
  \]
- Determine the required phase drift and diffusion after the line geometry is
  fixed.
- State whether the theorem classifies radial curves only, complete pairs
  \((r,m,s)\), or SDE coefficients.
- Check all nondegeneracy assumptions: \(F'\neq0\), \(s>0\), \(r>0\),
  \(B\neq0\), and domain connectedness.
- Determine whether affine-linear SDEs containing both additive and
  multiplicative terms create additional curve families.
- Determine whether time-dependent coefficients or Stratonovich dynamics
  change the classification.
- Do not claim that lines and spirals are the “complete list” outside the
  final proved scope.

### Section 7 — Design dictionary

- Separate Borel state maps from \(C^2\) maps eligible for classical Itô
  calculus.
- Determine the minimal regularity for generalized Itô formulas.
- Verify the induced SDE for secant, logarithmic, circular, Archimedean, and
  other example curves.
- Check existence and uniqueness of the resulting phase and complex SDEs.
- Determine whether the dictionary provides practical design value or simply
  restates Itô's formula.

### Section 8 — Time-dependent fallback

- Re-derive \(R(t,\theta)\), the perpendicular distance \(d_t\), and
  orientation \(\varphi_t\).
- Identify all times at which the moving support line intersects the origin.
- Introduce stopping times or chart changes where the phase becomes singular.
- Verify the time-dependent Itô formula, including \(\partial_tR\).
- Check whether the proposed autonomous \((t,\theta)\) equation is correct.
- Distinguish one stochastic coordinate from a genuinely autonomous
  one-dimensional state, since deterministic time is still required.

### Section 9 — Classical literature

- Verify the skew-product formula for planar Brownian motion from primary
  sources.
- Check the Brownian time change, independence claims, origin assumptions,
  and stopping conventions.
- Verify the claimed Carne (1985) stereographic-projection reference.
- Verify that the ScienceDirect identifier criticized by the document does or
  does not support the earlier claim.
- Separate one-dimensional Cayley compactification from conformal invariance
  of planar Brownian motion.
- Verify the stated winding-law comparison and all scaling constants.

### Sections 10–13 — Corrections, evidence, novelty, and conclusions

- Recheck every itemized criticism of `possible_solution.md`.
- Reproduce every symbolic residual from source formulas.
- Reproduce every numerical tolerance with preserved code and seeds.
- Reject the “design group” as computationally useful unless a benchmark
  demonstrates an advantage.
- Audit the stated stability inequalities and parameter conventions.
- Perform a genuine prior-art search before retaining any uniqueness or
  rigidity claim.
- Produce separate final answers for:
  1. additive law required;
  2. multiplicative law allowed;
  3. constant radius required;
  4. unrestricted winding required; and
  5. noncollinear \(a,b\).

## 6. Required audit of `exact_one_phase_euler_representation_additive_brownian_motion.md`

The second document is longer and will be audited section by section.

### Sections 1–5 — Main result, semantics, secant construction, and geometry

- Verify the main if-and-only-if statement under explicit Borel and support
  hypotheses.
- Verify the real-coordinate formula
  \[
  ic+W_t=ic\sec\theta_t e^{i\theta_t}.
  \]
- Check sign and branch conventions for both canonical embeddings.
- Prove pathwise invertibility and filtration equality.
- State what filtration equality means if \(\sigma=0\), and distinguish the
  filtration of \(X\) from the filtration of a possibly larger probability
  space.
- Prove that the nonreal offset is minimal under the declared notion of
  ordinary phase.

### Sections 6–10 — General classification, domain, necessity, and uniqueness

- Replace the informal “union has interior, graph cannot contain it” proof
  with the measure-theoretic randomized-time proof or another complete proof.
- Add measurability of \(r\) explicitly.
- Verify the coordinate-free equivalences involving complex conjugates.
- Verify the polar formula, inverse, and the exact positive angular interval.
- Check the claim of essential uniqueness, including allowed shifts by
  \(2\pi k\), orientation reversal, phase reparameterizations, and null-set
  modifications.
- Separate uniqueness of geometric phase from uniqueness of a stochastic
  process version.

### Sections 11–15 — Phase SDE, generator, reconstruction, and transition law

- Derive the secant Itô and Stratonovich SDEs in both directions.
- Verify cancellation of the two second-order drift contributions.
- Establish well-posedness of the phase SDE on its open interval.
- Prove the martingale problem is well posed.
- Prove generator conjugacy with arithmetic Brownian motion.
- Replace the broad phrase “isomorphic Markov processes” with a precise
  statement about measurable or topological conjugacy of semigroups.
- Verify the exact transition and density, including the \(|\sigma|\)
  Jacobian.
- Prove density normalization, Chapman--Kolmogorov, and boundary behavior.
- Verify the general oblique phase dynamics, inverse derivative, and density.
- Resolve sign conventions when \(g(\theta)\) is negative.

### Sections 16–17 — Real-axis and constant-radius impossibility

- Make the real-axis obstruction measure-theoretically precise.
- Address \(Z_0=0\), zero hits, local time, signed radii, and unwrapped phases.
- Verify the polynomial proof that a constant modulus forces \(b=0\) and then
  \(a=0\).
- Distinguish preservation of the affine process from an invertible
  constant-radius encoding.

### Sections 18–20 — Cayley construction and unit-circle dynamics

- Verify the Cayley identity and inverse.
- Prove that the missing point is inaccessible at finite time.
- Derive the phase SDE independently in Itô and Stratonovich form.
- Derive the complex unit-circle SDE directly from the Möbius map and again
  from \(U=e^{i\Theta}\).
- Verify invariance of \(|U_t|=1\) from the SDE itself.
- Compare the process with ordinary circular Brownian motion and with
  stereographically projected Brownian motion from the literature.
- Determine whether a time change converts one to the other.

### Sections 21–22 — Transported addition and topological obstruction

- Prove all group axioms for \(\oplus\) and \(\boxplus\).
- Identify the precise Lie-group isomorphism with \((\mathbb R,+)\).
- Compare computational cost and numerical stability with ordinary addition.
- Prove the no-injective-continuous-homomorphism theorem for
  \(\mathbb R\to S^1\).
- State exactly which four properties cannot coexist and which assumptions
  are load-bearing: continuity, injectivity, constant radius, and
  homomorphism.
- Investigate measurable or discontinuous homomorphisms only enough to
  explain why they are irrelevant to stochastic continuity.

### Sections 23–24 — Complex GBM and projected-normal connections

- Map additive lines and multiplicative spirals in a common log/polar
  framework.
- Verify the Phase 3 and Phase 4 parameter relations.
- Determine whether the fixed-time angular law is properly called a singular
  projected-normal distribution.
- Compare the affine rank-one Gaussian case with the standard nondegenerate
  projected-normal model.
- Verify bibliographic claims and avoid using terminology unsupported by the
  cited sources.

### Sections 25–28 — Assessment, novelty, final result, and sources

- Re-audit every “Correct” entry rather than accepting the document's own
  assessment.
- Reconcile its informal necessity proof with the stronger proof proposed in
  `single-phase-euler-representation.md`.
- Verify every literature anchor from the primary source.
- Treat “complete classification” and “useful original synthesis” as
  hypotheses pending prior-art search.
- Produce a corrected final result only after all proof and evidence gates
  pass.

## 7. Reconciliation questions across the three candidate documents

The documents disagree or differ materially on the following points:

1. Whether the additive secant construction or multiplicative spiral is the
   best answer.
2. Whether `possible_solution.md` is fully correct despite its incomplete
   impossibility proof.
3. Whether measurability of \(r\) is necessary and where it is used.
4. Whether monotonicity of the argument is necessary for representation or
   only for lossless recovery.
5. Whether lines and logarithmic spirals are the only constant-coefficient
   families.
6. Whether the claimed rigidity theorem constrains only diffusion or both
   drift and diffusion.
7. Whether an arbitrary Borel \(r\) can legitimately be placed into an Itô
   design dictionary.
8. Whether the transported addition law is mathematically useful.
9. Whether the cited stereographic-projection source is correct.
10. Whether the projected-normal label is standard for the singular
    rank-one case.
11. Whether the Phase 3 construction already satisfies the exact intended
    request.
12. Whether the bounded additive phase provides the desired “rotation” at
    all, since it never completes a turn.

The Phase 5 synthesis must resolve each point explicitly.

## 8. Deep primary-source research programme

Research begins only after approval and precedes final theorem writing.

### 8.1 Exact representation and transformed diffusions

Search for:

- arctangent transformations of Brownian motion;
- exact state transformations of scalar diffusions;
- conjugate Markov processes and semigroups;
- martingale problems under diffeomorphisms;
- Lamperti transforms;
- Doss--Sussmann transformations;
- scale functions and speed measures;
- Feller boundary classification;
- compactification of one-dimensional diffusions; and
- exact simulation under invertible transformations.

### 8.2 Directional and circular distributions

Search for:

- projected-normal and angular-Gaussian distributions;
- singular projected-normal laws;
- wrapped normal distributions;
- Brownian motion on the circle;
- stereographic and Cayley projections of Brownian motion;
- directional statistics with degenerate covariance; and
- phase transition densities obtained by tangent transforms.

### 8.3 Stochastic differential geometry

Search for:

- Stratonovich SDEs under coordinate changes;
- stochastic development on manifolds;
- diffusion on embedded curves;
- generators induced on submanifolds;
- stochastic flows and Lie groups;
- exponential maps for stochastic systems;
- geometric and Lie-group numerical integrators; and
- invariant-preserving SDE schemes.

### 8.4 Complex stochastic calculus

Search for:

- complex-valued semimartingales;
- analytic versus nonanalytic complex Itô formulas;
- bilinear and Hermitian quadratic variation;
- Wirtinger derivatives in stochastic calculus;
- conformal maps of planar Brownian motion;
- complex Feynman--Kac formulas;
- holomorphic stochastic flows;
- complex Langevin methods; and
- stochastic differential equations with oscillatory or complex weights.

### 8.5 Algebraic and topological structure

Search for:

- continuous characters of \((\mathbb R,+)\);
- homomorphisms from \(\mathbb R\) to \(S^1\) and \(\mathbb C^\times\);
- transported group laws through tangent coordinates;
- one-parameter subgroups of complex multiplication;
- logarithmic spirals as group orbits;
- rigidity of planar curves under additive or multiplicative flows;
- affine and Möbius group actions; and
- possible extensions using matrices, quaternions, or Clifford algebras.

### 8.6 Numerical analysis and compactification

Search for:

- tangent or rational compactification of unbounded PDE domains;
- spectral methods on compactified real lines;
- mapped Chebyshev and Fourier methods;
- SDE transformations for numerical stability;
- boundary-preserving stochastic integrators;
- exact and exponential integrators for complex SDEs;
- variance reduction under coordinate transformations;
- quasi-Monte Carlo sensitivity to transformed coordinates; and
- numerical conditioning of transformed Kolmogorov equations.

### 8.7 Research record

For every retained source:

- record authors, title, venue, year, volume, pages, DOI, and stable URL;
- save the exact proposition, theorem, formula, or page used;
- distinguish primary proof from later exposition;
- classify the source's role in a claim-to-source matrix;
- verify quotations against the full text;
- document terminology differences;
- record negative searches without treating them as proof of novelty; and
- identify the earliest source found for each classical construction.

## 9. Corrected mathematical programme

### 9.1 Define the probability model and equality notion

Specify:

- filtered probability space and usual conditions;
- real Brownian motion and coefficient conventions;
- complex numbers identified with \(\mathbb R^2\);
- whether identities hold indistinguishably, pathwise outside one null set, or
  only for each fixed time;
- complete-process support versus fixed-time support;
- Borel, continuous, \(C^1\), and \(C^2\) versions of the radius problem;
- phase branch, lift, state space, and initial condition;
- stopping rules at zero or a chart singularity; and
- the exact definition of “only stochastic state variable.”

### 9.2 Derive the correct general factorization criterion

For

\[
Z_t=Z_0f(S_t),
\qquad
f(s)=|f(s)|e^{i\vartheta(s)},
\]

derive separate theorems for:

1. existence of some deterministic radius \(r\);
2. existence of a Borel \(r\);
3. continuous \(r\);
4. lossless recovery of \(S_t\);
5. a time-independent phase-first Markov representation; and
6. an unwrapped phase whose value is itself injective.

The likely minimal representation condition is that \(|f|\) factor through
the selected argument lift:

\[
\vartheta(s_1)=\vartheta(s_2)
\Longrightarrow
|f(s_1)|=|f(s_2)|.
\]

Injectivity of \(\vartheta\) is a sufficient route and may be necessary for
lossless recovery, but it will not be assumed necessary for Level 1 without a
proof.

### 9.3 Prove the additive affine theorem rigorously

Prove or correct:

\[
\boxed{
\frac{a}{b}\in\mathbb R,
\qquad
\frac{b}{Z_0}\notin\mathbb R.
}
\]

The sufficiency proof will use fixed-line geometry. The necessity proof will
use a Borel polar-graph null-set result plus randomized time, not an invalid
exchange of a union with an almost-sure statement.

Include:

- \(a=0\);
- \(b=0\);
- \(Z_0=0\);
- signed diffusion coefficients;
- finite and infinite time horizons;
- a radial line through zero;
- a line avoiding zero;
- noncollinear drift and diffusion;
- equality on a positive-measure time set;
- time-dependent radii; and
- allowed modifications on null sets.

### 9.4 Derive line geometry and phase uniqueness

Prove:

- the secant identity;
- the general cosecant formula;
- the inverse map;
- positivity on the exact phase interval;
- monotonicity and orientation;
- the perpendicular distance and foot-angle representation;
- essential uniqueness under the permitted equivalences;
- no finite-time endpoint hit; and
- no winding for the additive family.

### 9.5 Derive the phase diffusion and Markov conjugacy

Obtain independently:

- Itô SDE;
- Stratonovich SDE;
- quadratic variation;
- generator;
- forward and backward Kolmogorov operators;
- scale function;
- speed measure;
- Feller boundary classification;
- martingale problem;
- pathwise uniqueness;
- strong existence;
- semigroup conjugacy with arithmetic Brownian motion;
- filtration relationships; and
- inverse Itô reconstruction.

### 9.6 Derive exact distributions

Prove:

- exact one-step transition;
- transition density;
- marginal density;
- CDF and quantile;
- normalization;
- Chapman--Kolmogorov;
- moments that exist;
- characteristic function when tractable;
- endpoint tail asymptotics;
- relation to a transformed Gaussian law; and
- relation, if justified, to singular projected-normal distributions.

### 9.7 Complete the Cayley analysis

Prove:

- unit modulus;
- invertibility;
- missing point correspondence;
- exact phase SDE;
- exact complex \(U\)-SDE;
- invariance of the unit circle directly from the SDE;
- exact transition;
- boundary classification;
- group operation;
- relation to stereographic projection; and
- distinction from ordinary circular Brownian motion.

### 9.8 Complete the group and topology analysis

Prove:

- \((I,\oplus)\cong(\mathbb R,+)\);
- the Cayley equivalent;
- continuity and smoothness of the operations;
- the no-injective-continuous-character result for \(S^1\);
- injectivity of \(x\mapsto e^{(\alpha+i\beta)x}\) when
  \(\alpha\neq0\);
- exact conditions for ordinary multiplication to encode increments; and
- numerical stability of each composition law.

### 9.9 Complete the multiplicative spiral analysis

Prove:

- necessary and sufficient conditions for a time-independent spiral;
- exact radius-phase relation;
- unrestricted winding;
- Phase 3 equivalence;
- Phase 4 deterministic-rotation decomposition;
- transition laws and moments;
- local covariance rank;
- almost-sure and mean-square stability in the relevant parameterization; and
- limits of interpreting the phase as independent information.

### 9.10 Repair the rigidity classification

Classify complete triples \((r,m,s)\), not only curve shapes, under:

1. additive constant coefficients;
2. homogeneous multiplicative constant coefficients;
3. affine-linear coefficients;
4. Itô dynamics;
5. Stratonovich dynamics;
6. time-dependent coefficients; and
7. state-dependent coefficients.

The theorem must enforce both drift and diffusion equations. It must state
whether lines and spirals are exhaustive only for the first two narrow
classes or in a broader class.

### 9.11 Validate or reject the design dictionary

For each proposed curve:

- state the phase domain;
- state regularity;
- compute \(F'\) and \(F''\);
- derive the induced SDE;
- establish existence and uniqueness;
- determine whether the curve is invariant;
- determine whether the representation is invertible;
- identify singularities; and
- state whether the example yields any practical simplification.

### 9.12 Analyze the time-dependent fallback

Derive the moving-line polar equation and phase SDE with the full
time-dependent Itô formula. Classify origin-crossing times and determine
whether multiple phase charts or stopping times are required.

## 10. Does this unlock vector mathematics for stochastic calculus?

This implication will be investigated as a falsifiable research question.

### 10.1 Baseline fact to test against

\[
\mathbb C\cong\mathbb R^2
\]

as real vector spaces. Rewriting a scalar diffusion on a curve in complex
notation does not create a second stochastic dimension. The one-phase
process has local diffusion rank at most one.

A claimed vector-calculus benefit must therefore be more than the notation
\(x+iy\).

### 10.2 Potentially useful geometric structures

Investigate whether the phase representation gives a useful formulation of:

- the tangent vector \(F'(\theta)\);
- the normal vector \(iF'(\theta)\);
- speed, curvature, and the Frenet frame;
- drift decomposed into tangential and Itô-curvature components;
- rank-one covariance as a tangent outer product;
- pullback and pushforward of gradients, Hessians, and generators;
- differential one-forms along the curve;
- Stratonovich coordinate invariance;
- stochastic flows on embedded one-dimensional manifolds;
- Lie-group structure for multiplicative spirals or transported addition;
- rotation-dilation matrices represented by complex multiplication; and
- invariant-preserving numerical schemes.

### 10.3 Vector generalization limits

Prove or illustrate:

- why one phase cannot represent generic planar Brownian motion losslessly;
- why one Brownian driver does not always imply one-dimensional fixed-time
  support;
- why hypoelliptic one-driver systems can have two-dimensional terminal laws;
- why a curve encoding cannot replace a true two-dimensional state;
- what changes with two or more independent Brownian drivers;
- whether multiple phases, spherical coordinates, quaternions, matrices, or
  Clifford algebras provide honest higher-dimensional analogues; and
- when such extensions merely rename ordinary vector calculus.

### 10.4 Vector-calculus acceptance test

“Unlocks vector mathematics” may be stated only if at least one of the
following is established:

1. a new coordinate-free theorem becomes simpler and more general;
2. a vector identity yields a nontrivial stochastic result unavailable from
   the scalar coordinate alone;
3. an invariant-preserving algorithm follows naturally and outperforms a
   scalar baseline;
4. a higher-dimensional extension preserves information and has a proved
   advantage; or
5. the representation exposes a geometric obstruction that was hidden in
   scalar notation.

If none holds, the conclusion will be that the representation is a useful
visual and coordinate framework, not an unlocking of new vector mathematics.

## 11. Does this help with complex derivatives?

The phrase “complex derivative” will be disambiguated.

### 11.1 Holomorphic differentiation

Investigate:

- whether functions of \(Z_t\) are holomorphic on an open complex domain;
- why data on a one-dimensional curve generally supply only a directional
  derivative;
- when the identity theorem or analytic continuation is applicable;
- whether the state curve has accumulation points inside a holomorphic
  domain;
- how branch points, zeros, and logarithms affect the analysis; and
- whether the line or spiral parameterization simplifies any Cauchy integral
  or residue calculation.

Embedding a real process in \(\mathbb C\) will not be treated as automatically
granting holomorphic structure.

### 11.2 Wirtinger and real two-dimensional derivatives

For nonholomorphic functions \(f(z,\overline z)\), derive:

- \(\partial_z f\) and \(\partial_{\overline z}f\);
- the relation to the real gradient and Hessian;
- the pullback derivative \(d(f\circ F)/d\theta\);
- the complex Itô formula with bilinear and Hermitian brackets; and
- conditions under which the one-phase constraint reduces the Hessian terms.

### 11.3 Sensitivities and complex-step differentiation

Research whether the representation interacts meaningfully with:

- pathwise sensitivity derivatives;
- likelihood-ratio or Malliavin estimators;
- Greeks in arithmetic or geometric Brownian models;
- automatic differentiation through SDE solvers; and
- the complex-step numerical differentiation method.

The complex-step method will be treated as a separate numerical technique;
similar notation alone will not be claimed as a connection.

### 11.4 Complex-derivative acceptance test

A benefit must show at least one of:

- a derivative becomes closed form when it was not before;
- a regularity theorem is strengthened;
- a branch or singularity is handled more cleanly;
- a sensitivity estimator has lower bias or variance;
- a complex-valued PDE or Feynman--Kac problem becomes simpler; or
- a numerical derivative converges faster or more stably.

## 12. Can it solve problems currently requiring numerical methods?

The default null hypothesis is:

> An invertible coordinate transformation preserves the underlying
> information and usually preserves analytical difficulty. It may improve
> geometry, domain shape, conditioning, or discretization, but it does not
> automatically create a closed-form solution.

Phase 5 will try to falsify or confirm this through a benchmark ladder.

### 12.1 Analytically solvable controls

Use known solutions so transformed results can be checked:

- Brownian transition density;
- arithmetic-Brownian expectations;
- Bachelier European payoffs;
- heat equation on \(\mathbb R\);
- first-passage probability to a constant barrier;
- simple occupation or local-time identities; and
- complex exponential moments.

These controls determine whether the phase formulation preserves correctness.

### 12.2 Compactified PDE experiments

Transform the heat or Kolmogorov equation from \(x\in\mathbb R\) to the bounded
phase interval via \(x=c\tan\theta\). Compare:

- finite differences in \(x\);
- mapped finite differences in \(\theta\);
- Chebyshev or rational spectral methods;
- Cayley-circle Fourier methods when appropriate; and
- analytic control solutions.

Measure:

- error versus degrees of freedom;
- error versus runtime;
- matrix condition numbers;
- endpoint resolution;
- conservation of probability;
- positivity;
- stiffness from degenerate coefficients; and
- sensitivity to \(c\).

Compactification counts as useful only if it improves at least one metric
without unacceptable degradation elsewhere.

### 12.3 SDE simulation experiments

Compare direct and phase-based schemes for:

- arithmetic Brownian motion;
- the nonlinear phase SDE;
- Cayley unit-circle dynamics;
- multiplicative spiral dynamics;
- selected state-dependent one-phase curves; and
- a scalar nonlinear diffusion that admits a known Lamperti transform.

Measure:

- strong and weak error;
- stability;
- invariant preservation;
- boundary violations;
- runtime;
- exact-step availability; and
- sensitivity to step size.

### 12.4 Expectations and Monte Carlo

For identical random streams, compare estimators in original and phase
coordinates:

- ordinary Monte Carlo variance;
- quasi-Monte Carlo convergence;
- importance sampling;
- rare-event estimation;
- discontinuous payoff smoothing;
- pathwise sensitivity estimation; and
- numerical quadrature in transformed coordinates.

An invertible reparameterization alone should not be credited with variance
reduction. Any gain must be tied to a changed estimator or smoother integrand.

### 12.5 Complex and oscillatory problems

Explore carefully selected examples involving:

- complex-valued Feynman--Kac expectations;
- oscillatory characteristic-function integrals;
- Fourier pricing or transform methods;
- phase-amplitude SDEs;
- stochastic oscillators;
- complex linear stability equations; and
- sign or phase cancellation.

Determine whether a one-phase representation simplifies the phase, worsens
radial growth, or merely moves the oscillation into another factor.

### 12.6 Negative controls

Include problems where the representation should not help:

- planar Brownian motion with two independent drivers;
- a one-driver hypoelliptic system such as
  \[
  dX_t=dW_t,\qquad dY_t=X_tdt;
  \]
- a noncollinear additive complex process;
- a genuinely path-dependent payoff;
- a multidimensional nonlinear SDE;
- a process crossing the origin where one polar chart fails; and
- a nonholomorphic complex payoff requiring both \(z\) and \(\overline z\).

These controls prevent selecting only favorable examples.

### 12.7 Numerical-solvability decision rule

The project may claim a practical advance only if a benchmark demonstrates:

- a new exact solution or exact transition;
- a proved reduction in dimension;
- improved asymptotic convergence order;
- materially smaller error at matched runtime;
- improved stability or conditioning;
- exact preservation of a meaningful invariant;
- lower estimator variance at matched cost; or
- reliable treatment of a domain or boundary that defeated the baseline.

Otherwise the conclusion will state that the representation changes
coordinates but not solvability.

## 13. Symbolic, theorem, and proof verification

Every central formula will be checked by at least two independent routes.

### 13.1 Algebra and geometry

- trigonometric secant identity;
- general line polar equation;
- inverse maps;
- Cayley identity;
- spiral radius;
- tangent and normal vectors;
- group operations; and
- support geometry.

### 13.2 Stochastic calculus

- forward Itô map;
- inverse Itô map;
- Stratonovich conversion;
- direct complex SDE derivation;
- generator conjugacy;
- quadratic covariations;
- invariant checks; and
- Fokker--Planck residuals.

### 13.3 Probability and measure theory

- Borel measurability;
- analytic-set measurability;
- polar-Fubini nullity;
- randomized-time density;
- full support;
- filtration equality;
- martingale problem;
- semigroup equivalence; and
- boundary classification.

### 13.4 Classification

- solve all coefficient equations symbolically;
- verify real-valuedness constraints on \(m\) and \(s\);
- test degenerate branches;
- construct counterexamples to claims that are too strong; and
- record the exact scope of any rigidity theorem.

## 14. Reproducible computational programme

Use the existing approved conda environment without installing or mutating
packages. Use fixed seeds in a documented Phase 5 family and record package
versions.

### 14.1 Model and tests

Plan a focused Phase 5 model module with separate functions for:

- canonical secant forward and inverse maps;
- general affine-line forward and inverse maps;
- phase drift and diffusion;
- generator coefficients;
- exact transition and density;
- Cayley forward and inverse maps;
- Cayley phase and complex SDE coefficients;
- spiral forward and inverse maps;
- curve-induced Itô coefficients;
- eligibility predicates for additive and multiplicative cases; and
- time-dependent fallback geometry.

Unit tests will cover algebraic identities, branch domains, degenerate cases,
SDE coefficients, density normalization, group laws, and theorem
counterexamples.

### 14.2 Canonical executed notebook

Create one canonical discovery notebook, generated from a deterministic
builder, with clearly separated sections:

1. assumptions and package record;
2. candidate comparison;
3. secant geometry;
4. general affine geometry;
5. measure-theoretic impossibility;
6. phase SDE;
7. generator and transition law;
8. boundary behavior;
9. Cayley compactification;
10. group operations;
11. logarithmic spiral and Phase 3;
12. rigidity tests;
13. time-dependent fallback;
14. vector geometry;
15. complex derivatives;
16. PDE compactification;
17. stochastic numerical benchmarks;
18. negative controls; and
19. evidence summary.

### 14.3 Non-circular stochastic verification

The principal empirical cross-check will simulate the nonlinear phase SDE
without using the closed-form arctangent inside each update, then compare it
to the exact transformed Brownian path on shared increments.

Include:

- Euler--Maruyama;
- Milstein after independent derivation;
- a Stratonovich method;
- multiple time-step sizes;
- fitted strong convergence slopes;
- confidence intervals or replication uncertainty; and
- boundary stress tests.

### 14.4 Distribution and semigroup verification

- probability-integral-transform diagnostics;
- empirical versus exact quantiles;
- density normalization by independent quadrature;
- Chapman--Kolmogorov quadrature;
- small-time generator moment checks;
- Fokker--Planck residuals;
- endpoint tail checks; and
- signed-\(\sigma\) cases.

### 14.5 Theorem illustrations

- random eligible oblique lines;
- radial line failure;
- noncollinear drift/diffusion failure;
- randomized-time planar density;
- angle-bin radius spread;
- bounded additive phase span;
- unrestricted spiral winding;
- Cayley missing-point approach;
- group-law round trips;
- filtration/inverse reconstruction; and
- time-dependent fallback with origin-crossing warnings.

### 14.6 Implication benchmarks

The notebook will report vector, derivative, PDE, and simulation results
against explicit scalar baselines. Each figure or table must state whether it
supports, refutes, or leaves an implication unresolved.

### 14.7 Reproducibility gates

- execute twice from clean kernels;
- require sequential execution counts;
- allow zero cell errors;
- compare deterministic source and evidence hashes;
- record all horizons and parameter values beside each experiment;
- use shared streams for method comparisons;
- preserve generated evidence tables;
- report Monte Carlo standard errors;
- avoid treating exact-formula sampling as independent validation; and
- rerun selected results with a second seed family.

## 15. Planned deliverables

After approval and a detailed implementation contract, Phase 5 is expected to
produce:

1. `PHASE_5_COMPREHENSIVE_ONE_PHASE_EULER_RESEARCH_PLAN.md` — this plan;
2. `PHASE_5_CANDIDATE_AUDIT.md` — section-by-section audit of all three
   supplied candidate documents;
3. `PHASE_5_LITERATURE_REVIEW.md` — primary-source review and prior-art gate;
4. `PHASE_5_MATHEMATICAL_FOUNDATIONS.md` — definitions, representation
   theorem, impossibility theorem, and phase law;
5. `PHASE_5_RIGIDITY_AND_GROUP_STRUCTURE.md` — corrected classification,
   spiral comparison, Cayley transform, and topology;
6. `PHASE_5_VECTOR_AND_COMPLEX_CALCULUS_IMPLICATIONS.md` — proved benefits,
   obstructions, and negative results;
7. `PHASE_5_NUMERICAL_IMPLICATIONS.md` — PDE, SDE, Monte Carlo, and
   numerical-solvability benchmarks;
8. a focused Phase 5 Python model module;
9. a new Phase 5 unit-test suite;
10. a deterministic notebook builder;
11. an executed Phase 5 discovery notebook;
12. generated figures and structured evidence tables;
13. `PHASE_5_SIMULATION_RESULTS.md`;
14. `PHASE_5_SYNTHESIS.md`; and
15. `.agent/reviews/TASK-007-opencode-glm52-review.md` after Codex completes
    and verifies the work.

A Phase 5 technical paper is explicitly excluded from this phase. It should
receive a separate plan only if the research survives the mathematical,
prior-art, and implications gates.

## 16. Research stages and gates

### Gate 1 — Candidate audit

Every claim in the three supplied documents is classified as:

- verified;
- correct but incompletely proved;
- correct under stronger assumptions;
- ambiguous;
- false or overstated;
- classical;
- unsupported by the cited source; or
- unresolved.

No synthesis begins until the major inconsistencies are resolved.

### Gate 2 — Prior art and triviality

The literature review determines whether each result is:

- classical;
- a direct corollary of known theory;
- a useful synthesis;
- a potentially new elementary theorem; or
- unsupported as a novelty claim.

### Gate 3 — Mathematical foundations

All exact identities, existence theorems, impossibility results, SDEs,
generators, kernels, domains, and boundary statements pass independent
derivations.

### Gate 4 — Computational reproduction

Unit tests, symbolic checks, notebook execution, pathwise reconstruction,
transition checks, and convergence experiments pass.

### Gate 5 — Implications

Vector, complex-derivative, and numerical claims are tested against scalar
baselines and negative controls. Unsupported “unlocking” language is removed.

### Gate 6 — Independent review

OpenCode `zai-coding-plan/glm-5.2` reviews the mathematics, literature,
simulation design, numerical evidence, and claim strength. All critical and
major findings must be resolved.

### Gate 7 — Final synthesis

The synthesis states:

- the shortest correct answer to the user's representation question;
- which candidate is appropriate under each requirement;
- what is genuinely gained;
- what is only a coordinate change;
- whether vector mathematics is materially advanced;
- whether complex derivatives are simplified;
- whether any numerical-only problem became analytic; and
- which questions remain open.

## 17. Acceptance criteria

Phase 5 is complete only when:

1. all three supplied candidate documents have claim-level audits;
2. the correct notion of one-phase representation is formalized;
3. measurability and equality quantifiers are explicit;
4. the general factorization criterion is proved correctly;
5. the additive affine if-and-only-if theorem is proved or corrected;
6. the necessity proof has no union-of-null-sets gap;
7. line geometry, inverse map, and angular domain are verified;
8. phase uniqueness is stated under exact equivalences;
9. real-axis and constant-radius impossibility results are rigorous;
10. the phase SDE is verified forward and backward;
11. generator, semigroup, and martingale-problem statements are precise;
12. transition densities normalize and compose;
13. boundary classifications are proved;
14. Cayley phase and unit-circle SDE agree independently;
15. transported group laws and the topological obstruction are proved;
16. the logarithmic-spiral candidate is reconciled with Phase 3 and Phase 4;
17. the rigidity theorem enforces both drift and diffusion;
18. Borel and \(C^2\) curve claims are not conflated;
19. the moving-line fallback handles origin crossings;
20. every literature citation is verified from a primary or authoritative
    source;
21. no unsupported novelty claim remains;
22. pathwise and distributional simulations meet prespecified tolerances;
23. direct phase-SDE simulations converge to the exact representation;
24. the notebook executes twice cleanly and reproducibly;
25. vector-calculus claims pass explicit acceptance tests or are rejected;
26. complex-derivative claims pass explicit acceptance tests or are rejected;
27. numerical benefits are measured against matched baselines;
28. negative controls are included;
29. no coordinate rewrite is mislabeled as a new stochastic dimension or
    closed-form solution;
30. OpenCode GLM 5.2 leaves no unresolved critical or major issue; and
31. the final synthesis clearly distinguishes proven value from speculation.

## 18. Constraints

- Preserve the completed Phase 3 and Phase 4 mathematics.
- Preserve all user-supplied reviews, critiques, and candidate solutions.
- Do not silently edit a candidate document to make its claims correct; record
  corrections in the Phase 5 audit.
- Do not claim that complex notation creates a second stochastic dimension.
- Do not call the bounded additive phase genuine repeated rotation.
- Do not call the Cayley image ordinary circular Brownian motion.
- Do not call the spiral additive Brownian motion.
- Do not treat a Borel radius as \(C^2\) without a regularity hypothesis.
- Do not use numerical agreement as a substitute for a theorem.
- Do not infer novelty from an unsuccessful search.
- Do not infer analytical solvability from invertibility of a coordinate map.
- Do not claim numerical improvement without a matched baseline and cost
  metric.
- Keep \(d[W,W]_t=dt\), finite-increment approximations, and \(i^2=-1\)
  conceptually distinct.
- Use the existing conda environment without mutation.
- Use the standing Codex-direct implementation exception if execution is
  approved; do not delegate implementation.
- Use OpenCode GLM 5.2 only for independent review and second opinion.
- Do not use `agy`, Copilot, Grok, or another worker for implementation.
- Do not commit, push, open a pull request, publish, or release unless
  separately requested.

## 19. Approval gate

No Phase 5 research, mathematical implementation, code, notebook, simulation,
benchmark, external-model review, or publication work begins until the user
approves this comprehensive plan.
