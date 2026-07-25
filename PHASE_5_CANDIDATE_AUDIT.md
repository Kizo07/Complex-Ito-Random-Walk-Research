# Phase 5 candidate-solution audit

## Purpose and verdict standard

This document audits the three supplied Phase 5 candidates before their claims
are reused:

1. `possible_solution.md`;
2. `single-phase-euler-representation.md`;
3. `exact_one_phase_euler_representation_additive_brownian_motion.md`.

The target problem is the nondegenerate one-driver affine process

\[
Z_t=Z_0+a t+bW_t,\qquad Z_0\ne0,\quad b\ne0,
\]

and a representation

\[
\frac{Z_t}{Z_0}=r(\theta_t)e^{i\theta_t}
\tag{1}
\]

in which:

- \(\theta_t\) is a real genuine phase, so its value modulo \(2\pi\) is
  the geometric argument;
- \(r:\mathbb R\to[0,\infty)\) is deterministic, single-valued, and has
  no explicit time dependence;
- (1) holds across the full process, rather than at only one horizon or
  on one selected path;
- the representation is lossless: the scalar state driving \(Z_t\) can
  be recovered from \(\theta_t\);
- Borel measurability is the minimum regularity used in the support
  impossibility theorem, while classical Itô derivations require
  \(C^2\) state maps.

The verdicts below have the following meanings.

| Verdict | Meaning |
|---|---|
| Correct | The claim follows under its stated assumptions. |
| Correct with qualifications | The main formula is valid, but its domain, regularity, quantifiers, or interpretation must be narrowed. |
| Incomplete | A necessary step or condition is missing, so the stated conclusion is not established as written. |
| Incorrect | A counterexample or calculation contradicts the claim. |
| Interpretive only | A useful analogy or motivation, not a mathematical theorem. |

## Executive findings

The central secant construction is exact:

\[
1+i\tan\theta=\sec\theta\,e^{i\theta},
\qquad -\frac{\pi}{2}<\theta<\frac{\pi}{2}.
\]

More generally, a lossless, time-independent, genuine one-phase
representation of the full affine process exists exactly when

\[
\boxed{\frac ab\in\mathbb R,\qquad \frac b{Z_0}\notin\mathbb R.}
\tag{2}
\]

Under (2), write

\[
a=\lambda b,\qquad
\frac b{Z_0}=\rho e^{i\phi},\qquad
x_t=\lambda t+W_t.
\]

Then

\[
\frac{Z_t}{Z_0}
=
\frac{\sin\phi}{\sin(\phi-\theta_t)}e^{i\theta_t},
\qquad
x_t=
\frac{\sin\theta_t}{\rho\sin(\phi-\theta_t)}.
\tag{3}
\]

The phase occupies one open interval of length \(\pi\); it never winds.
The construction is therefore a nonlinear coordinate chart on a fixed
affine line, not a new rotational degree of freedom.

The candidate documents also contain four material gaps:

1. **Argument injectivity is sufficient for lossless recovery, but it is
   not necessary merely for a phase-radius representation.** For example,
   \(f(s)=e^{i\sin s}\) has the representation
   \(r(\theta)=1,\ \theta=\sin s\), although its argument lift is not
   injective.
2. **The first support proof in the exact candidate is not by itself
   gap-free.** Almost-sure containment on each fixed-time line does not
   immediately imply setwise containment of the entire swept region.
   Randomizing time repairs the proof.
3. **The proposed rigidity theorem omits drift compatibility.** The
   diffusion coefficient forces a line or logarithmic spiral, but the
   drift equation imposes additional relations on the phase drift.
4. **A Borel radius is enough for a measure-theoretic representation but
   not for classical Itô calculus.** Any differentiation of
   \(F(\theta)=r(\theta)e^{i\theta}\) requires the stated smoothness.

## 1. Exact factorization criterion

Fix a state space \(E\), a nonzero map \(f:E\to\mathbb C\), and a
chosen genuine argument lift \(\vartheta:E\to\mathbb R\):

\[
e^{i\vartheta(s)}=\frac{f(s)}{|f(s)|}.
\]

The exact measurable criterion is

\[
\boxed{|f|\text{ is }\sigma(\vartheta)\text{-measurable}.}
\tag{4}
\]

By the Doob--Dynkin factorization lemma, (4) is equivalent to the
existence of a Borel \(r\) such that

\[
|f(s)|=r(\vartheta(s)).
\]

At the set-theoretic level, a necessary condition is

\[
\vartheta(s_1)=\vartheta(s_2)
\Longrightarrow
|f(s_1)|=|f(s_2)|.
\tag{5}
\]

Under the regular interval settings used in the candidates, (5) plus
the relevant measurability/quotient condition is also sufficient.
Injectivity of \(\vartheta\) is a convenient stronger condition. It is
also necessary if the phase alone must recover \(s\), but not if only
\(f(s)\) must be represented.

This distinction separates three notions that the candidates sometimes
merge:

| Level | Requirement |
|---|---|
| Phase-radius representation | \(f=r(\vartheta)e^{i\vartheta}\). |
| State representation | \(|f|\) factors measurably through \(\vartheta\). |
| Lossless coordinate | \(s\) itself factors measurably through \(\vartheta\); injectivity is the usual sufficient condition. |

## 2. Audit of `possible_solution.md`

### 2.1 Secant construction and geometry

| Candidate claim | Verdict | Resolution |
|---|---|---|
| \(1+i\tan\theta=\sec\theta e^{i\theta}\). | Correct with qualifications | Exact only on a branch where \(\cos\theta>0\), canonically \((-\pi/2,\pi/2)\). With a signed secant outside that interval, the radius would not remain nonnegative. |
| \(Z_t=Z_0[1+i(X_t-X_0)/c]\) has a one-phase Euler form. | Correct | Set \(\theta_t=\arctan((X_t-X_0)/c)\), \(c>0\). Then \(Z_t=Z_0\sec\theta_t e^{i\theta_t}\). |
| \(X_t=X_0+c\tan\theta_t\) recovers the real process. | Correct | The arctangent chart is a bijection from \(\mathbb R\) to \((-\pi/2,\pi/2)\). |
| The radius is stochastic only through the phase. | Correct | \(r(\theta)=\sec\theta\) is deterministic; \(\theta_t\) is the single random state variable. |
| This realizes rotation in the same sense as an unrestricted Euler angle. | Interpretive only | It is genuine polar angle, but it is trapped in one half-turn and never winds. The image remains a straight line. |
| A version can leave Brownian motion in the real coordinate. | Correct with qualifications | The shifted embedding \(ic+X_t-X_0\) works, with a sign/branch convention fixed explicitly. It is still an embedding of the real process, not literal equality to the original real-valued state. |

For the real-coordinate convention

\[
\widetilde Z_t=ic+X_t-X_0,
\]

one consistent choice is

\[
\theta_t=-\arctan\!\left(\frac{X_t-X_0}{c}\right),
\qquad
\widetilde Z_t=ic\,\sec\theta_t e^{i\theta_t},
\qquad
X_t-X_0=-c\tan\theta_t.
\]

### 2.2 Phase SDE, generator, and phase-first construction

| Candidate claim | Verdict | Resolution |
|---|---|---|
| The displayed Itô SDE for \(\theta=\arctan(Y/c)\) is exact. | Correct | Direct differentiation gives the stated drift and diffusion. |
| The displayed Stratonovich SDE removes precisely the nonlinear Itô correction. | Correct | The correction is \(\tfrac12BB'=-(\sigma^2/c^2)\sin\theta\cos^3\theta\). |
| The generator can define the phase without naming \(W_t\). | Correct with qualifications | The martingale problem or weak diffusion law is a valid phase-first definition. Existence, uniqueness in law, state space, and inaccessible endpoints must be stated. This removes \(W_t\) from the state formula, not randomness from the model. |
| The phase diffusion is a new process distinct in information content from arithmetic Brownian motion. | Incorrect if interpreted literally | It is a smooth bijective reparameterization of arithmetic Brownian motion. The two Markov processes are isomorphic under \(x=c\tan\theta\). |
| The phase endpoints cannot be reached at finite time. | Correct | They correspond to \(x=\pm\infty\). A finite-valued Brownian diffusion on \(\mathbb R\) cannot reach them in finite time. |

### 2.3 Transported addition

| Candidate claim | Verdict | Resolution |
|---|---|---|
| \(\theta_1\oplus\theta_2=\arctan(\tan\theta_1+\tan\theta_2)\) is an exact addition operation. | Correct | On the open principal interval it is ordinary real addition transported through a bijection. |
| The operation is associative, commutative, and has inverses. | Correct | These properties follow from the group isomorphism \(c\tan:(I,\oplus)\to(\mathbb R,+)\). |
| This produces ordinary angular addition or ordinary complex multiplication. | Incorrect | In general \(\theta_1\oplus\theta_2\ne\theta_1+\theta_2\), and the corresponding secant factors do not multiply as a representation of \((\mathbb R,+)\). |
| The operation offers a computational advantage. | Unsupported | It introduces tangent and arctangent evaluations. Any numerical benefit requires a matched benchmark. |

### 2.4 General affine theorem

| Candidate claim | Verdict | Resolution |
|---|---|---|
| Conditions (2) are necessary and sufficient. | Correct with qualifications | Correct for the full-support, time-independent, Borel, genuine-phase, lossless formulation stated above. Degenerate cases \(b=0\), \(Z_0=0\), fixed horizons, or path-specific encodings are outside the theorem. |
| Formula (3) is the general solution. | Correct | The formula and inverse follow from resolving the fixed affine line in polar coordinates. |
| The candidate's geometric necessity arguments prove the result in full generality. | Incomplete | Collinearity needs a measure-theoretic support argument; pointwise union-of-lines language alone skips an almost-sure quantifier. The corrected random-time proof appears in `PHASE_5_MATHEMATICAL_FOUNDATIONS.md`. |
| A radial affine line cannot admit a lossless genuine phase. | Correct | Only phases congruent to \(0\) or \(\pi\) occur; a single-valued radius then supplies only countably many points per ray, whereas a Gaussian line law has a continuous radial distribution. |

### 2.5 Constant radius and Cayley transform

| Candidate claim | Verdict | Resolution |
|---|---|---|
| A nondegenerate additive affine process cannot itself have constant radius. | Correct | Its support is an unbounded line, not a circle. |
| The Cayley transform gives a lossless unit-circle encoding. | Correct | \(U=(1+iY/c)/(1-iY/c)=e^{i\Theta}\), \(\Theta=2\arctan(Y/c)\), with inverse \(Y=c\tan(\Theta/2)\). |
| The Cayley process is the original additive process in Euler form. | Incorrect; candidate itself warns against this | It is an invertible nonlinear transform of the original state. |
| The missing point \(-1\) represents infinity. | Correct | The phase state space is \((-\pi,\pi)\); \(-1\) is not attained at finite time. |
| The Cayley phase is circular Brownian motion. | Incorrect; candidate itself rejects this | Its angular diffusion coefficient is state dependent and vanishes at the missing point. |

### 2.6 Overall verdict on `possible_solution.md`

The document contains the correct constructive core and most of the correct
interpretive warnings. Its main weaknesses are proof-level: theorem
quantifiers, the Borel versus \(C^2\) distinction, a gap-free necessity
argument, boundary classification, and comparisons showing whether the
transported group law changes any analysis or computation.

## 3. Audit of `single-phase-euler-representation.md`

### 3.1 Master criterion

| Candidate claim | Verdict | Resolution |
|---|---|---|
| A representation exists iff the continuous argument lift is injective. | Incorrect | Injectivity is sufficient and supports lossless recovery, but it is not necessary for representation. \(f(s)=e^{i\sin s}\) is a counterexample. The exact criterion is measurable factorization (4). |
| Injectivity is equivalent to strict monotonicity for a continuous lift on an interval. | Correct | A continuous injective real function on an interval is strictly monotone. |
| The proof establishes the claimed converse. | Incorrect | It only rules out equal phases with unequal moduli. It does not rule out equal phases with equal moduli, which is exactly the counterexample mechanism. |
| A line missing the origin has monotone argument. | Correct | Its derivative has constant nonzero sign. |
| A radial line loses magnitude information in its genuine phase. | Correct | The geometric phase records only the ray. |

### 3.2 Additive classification

| Candidate claim | Verdict | Resolution |
|---|---|---|
| Conditions (2), formula (3), and the length-\(\pi\) phase domain are exact. | Correct | These are retained. |
| The phase never winds and its diffusion coefficient degenerates at the endpoints. | Correct | Both follow from the arctangent coordinate. |
| The randomized-time proof closes the noncollinear impossibility gap. | Correct with a repair | Choose the independent random time on a finite interval bounded away from zero, or more generally give it an ordinary density there. A merely “uniform” law on an arbitrary positive-measure set should be defined carefully. |
| The Borel assumption is load-bearing for the polar-graph null-set proof. | Correct | Without regularity, the displayed Fubini step is unavailable. |
| The numerical binning experiment proves the theorem. | Incorrect if read as proof | It is a useful diagnostic but cannot replace the null-set and density argument. |

### 3.3 Multiplicative logarithmic spiral

| Candidate claim | Verdict | Resolution |
|---|---|---|
| \(Z=Z_0e^{\kappa t+BW_t}\) has a time-independent lossless spiral form when \(\kappa=\gamma B\), \(\gamma\in\mathbb R\), and \(\operatorname{Im}B\ne0\). | Correct | Then \(\theta=\operatorname{Im}(B)(\gamma t+W_t)\) and \(r(\theta)=\exp[(\operatorname{Re}B/\operatorname{Im}B)\theta]\). |
| This phase can wind without bound. | Correct | The unwrapped phase is an affine Brownian motion with nonzero diffusion. |
| The construction is “better” than the additive one. | Interpretive only | It better satisfies the desire for winding, but it changes the stochastic model from additive to multiplicative. It is not a substitute when the additive law is fixed. |
| Phase 3 is exactly the compatible spiral subfamily. | Correct with nonzero-angle qualification | The stated radius formula requires the Phase 3 angle multiplier to be nonzero; the zero case is a radial exponential. |
| Generic Phase 4 parameters destroy the time-independent spiral. | Correct | Compatibility is equivalent to real collinearity of the log drift and log diffusion; otherwise an additional deterministic rotation remains. |

### 3.4 Claimed rigidity theorem

| Candidate claim | Verdict | Resolution |
|---|---|---|
| Constant additive diffusion forces the curve to be a straight-line polar family. | Correct locally | From \(F'(\theta)s(\theta)=b/Z_0\), the tangent has fixed direction. |
| Constant multiplicative diffusion forces a logarithmic spiral and constant phase diffusion. | Correct locally when \(\operatorname{Im}B\ne0\) | From \(F's/F=B\), the imaginary part forces \(s=\operatorname{Im}B\) and \(r'/r=\operatorname{Re}B/\operatorname{Im}B\). |
| These diffusion calculations are iff classifications of the full constant-coefficient SDEs. | Incomplete | The drift equation is missing. For the additive case it requires \(a/b\in\mathbb R\) and \(m=(a/b)s+\tfrac12ss'\). For the multiplicative case it requires \(m\) constant and \(A=(k+i)m+\tfrac12(k+i)^2\beta^2\). |
| The circle is automatically a multiplicative constant-coefficient member for arbitrary \(m(\theta)\). | Incorrect as stated | A constant coefficient \(A\) requires the phase drift \(m\) to be constant. |
| Any other radius produces a valid one-phase process with state-dependent coefficients. | Correct with qualifications | The radius must have enough regularity for the claimed Itô SDE, the map must avoid singularities on its state domain, and lossless recovery may fail if the phase map is not injective. |

### 3.5 Moving-line fallback

| Candidate claim | Verdict | Resolution |
|---|---|---|
| A time-dependent polar equation represents each moving support line when drift and diffusion are noncollinear. | Correct locally | This works at times when the line misses the origin and on a consistently chosen angular chart. |
| The displayed formula works globally for all parameters and times. | Incorrect without exclusions | A moving support line can pass through the origin at one deterministic time. At that time no single-valued genuine polar radius represents the entire line losslessly. |
| A time-dependent phase SDE follows from Itô's formula. | Correct with qualifications | The formula is valid before zero/chart singularities and must include the explicit \(\partial_t\) contribution through the moving coordinate. |
| One stochastic driver always suffices. | Correct in the original SDE sense | The model already has one Brownian driver. This statement does not imply that a time-independent one-phase state chart exists. |

### 3.6 Literature and novelty statements

| Candidate claim | Verdict | Resolution |
|---|---|---|
| Planar Brownian skew-product theory is the relevant two-driver comparison. | Correct | It is a useful contrast, not a derivation of the rank-one result. |
| The one-phase process is a “rank-one degeneration” of the planar skew product. | Correct as geometric positioning | It should not be presented as a standard named theorem without a source. |
| The cited stereographic-projection replacement is relevant. | Correct with scope warning | Carne studies Brownian motion and stereographic projection with conformal/time-change structure. The Cayley image here is a deterministic transform of a one-dimensional diffusion and is not the same process. |
| Numerical verification establishes novelty. | Incorrect | Novelty requires a literature search and precise comparison of claims, not numerical agreement. |

### 3.7 Overall verdict on `single-phase-euler-representation.md`

This document makes the most important proof repair—the randomized-time
argument—and correctly identifies the multiplicative spiral. Its master
criterion is false as stated, its rigidity theorem needs drift conditions,
and its moving-line fallback needs a deterministic singular-time analysis.
Those are substantive but repairable issues.

## 4. Audit of
`exact_one_phase_euler_representation_additive_brownian_motion.md`

### 4.1 Main theorem, formula, and domain

| Candidate claim | Verdict | Resolution |
|---|---|---|
| The affine existence theorem is (2). | Correct with the document's seven requirements | The assumptions should also state Borel measurability for the impossibility proof. |
| The general radius and inverse are (3). | Correct | Direct substitution verifies them. |
| The angular domain is the stated open interval of length \(\pi\). | Correct | Choose \(\phi\in(-\pi,\pi)\setminus\{0\}\); its sign determines the branch. |
| The endpoints are inaccessible. | Correct | A fuller result classifies them as natural boundaries through the diffeomorphism to \(\mathbb R\). |
| The phase representation is essentially unique. | Correct with qualifications | This holds for the continuous argument lift anchored at \(\theta_0=0\). Discontinuous lifts differing by state-dependent multiples of \(2\pi\) are excluded by continuity. |

### 4.2 Necessity proof

| Candidate claim | Verdict | Resolution |
|---|---|---|
| Noncollinear support lines sweep a planar region. | Correct setwise | The affine map \((t,w)\mapsto Z_0+at+bw\) has nonzero determinant. |
| Therefore the phase graph must contain that entire region. | Incomplete | The representation is initially an almost-sure statement for each time. Setwise support containment needs continuity/closedness not guaranteed by Borel \(r\). Randomizing time supplies the missing measure argument. |
| A Borel polar graph has zero planar Lebesgue measure. | Correct | Each geometric ray meets it in at most countably many radii; polar Fubini applies after establishing measurability. |
| A line through the origin is impossible. | Correct | The line law is nonatomic, while a single-valued genuine phase graph has only countably many points on the two available rays. |

### 4.3 Dynamics and transition laws

| Candidate claim | Verdict | Resolution |
|---|---|---|
| The canonical Itô and Stratonovich phase SDEs are exact. | Correct | They follow from arctangent differentiation. |
| The generator reconstructs arithmetic Brownian motion under \(x=c\tan\theta\). | Correct | The generators are conjugate under the diffeomorphism. |
| The general \(g(\theta)\), inverse derivative, and transition density are exact. | Correct | The absolute Jacobian is needed because \(g\) may be negative; the document includes \(|\sin\phi|\) in the density. |
| The phase transition rule gives an exact sampler. | Correct | It is a transformed Gaussian increment and composes by the Markov semigroup. |
| Euler--Maruyama is needed to simulate the phase. | Incorrect if implied | The exact transformed-normal step is available and should be the default benchmark. |

### 4.4 Cayley and group claims

| Candidate claim | Verdict | Resolution |
|---|---|---|
| Cayley phase dynamics, exact transition, and complex SDE are correct. | Correct | Direct symbolic and numerical Itô checks confirm the formulas. |
| The complex SDE preserves unit modulus. | Correct | It follows from the transform and can also be verified directly by applying Itô to \(U\overline U\). |
| Secant and Cayley transported operations are genuine abelian group laws. | Correct | They are pullbacks of \((\mathbb R,+)\). |
| These laws unlock a new algebra distinct from real addition. | Incorrect if interpreted as new structure | They are isomorphic copies of real addition, useful as coordinates but not additional algebraic information. |
| No continuous injective homomorphism \((\mathbb R,+)\to S^1\) exists. | Correct | Nontrivial continuous characters are periodic; the constant character is not injective. |

### 4.5 Projected-normal and research-positioning claims

| Candidate claim | Verdict | Resolution |
|---|---|---|
| The phase law is related to projected-normal distributions. | Correct with qualification | It is the angular law of a rank-one singular Gaussian supported on an affine line. Standard projected-normal work usually starts from a nondegenerate multivariate normal, so “singular/degenerate projected-normal limit” is the safer description. |
| The construction is a stereographic Brownian motion. | Incorrect if unqualified | The map resembles inverse stereographic/Cayley coordinates, but the resulting time parameter and generator must be distinguished from conformally invariant spherical Brownian constructions. |
| The theorem is novel. | Unsupported pending literature audit | Individual formulas are elementary coordinate transforms. Any novelty claim must be limited to the exact package of classification, proof, dynamics, and comparative implications after primary-source review. |

### 4.6 Overall verdict on the exact candidate

This is the most complete additive treatment. Its formulas are largely
correct. The main repair is to replace the informal swept-support proof by the
randomized-time density proof, add the Borel/\(C^2\) regularity split, state
continuous-lift uniqueness precisely, and avoid overstating links to
projected-normal or stereographic Brownian literature.

## 5. Corrected theorem ledger

The implementation and later paper may rely on the following results, subject
to the proofs in the Phase 5 mathematical documents.

| ID | Result | Status after audit |
|---|---|---|
| F1 | Doob--Dynkin measurable factorization is the master criterion. | Retained. |
| F2 | Argument injectivity is sufficient for lossless recovery, not necessary for representation alone. | Corrected. |
| A1 | The affine iff theorem is (2). | Retained with Borel/full-support assumptions. |
| A2 | The general polar line formula, inverse, and length-\(\pi\) domain are (3). | Retained. |
| A3 | Noncollinear affine processes are impossible by a randomized-time planar-density argument. | Repaired. |
| A4 | Radial affine lines are impossible by nonatomicity versus countable polar image. | Retained and formalized. |
| D1 | Canonical and general phase SDEs, generators, transition laws, and exact samplers are transformed Brownian formulas. | Retained. |
| D2 | The angular endpoints are inaccessible natural boundaries. | Strengthened. |
| C1 | Cayley gives a lossless unit-circle transform, not the original affine state. | Retained with distinction. |
| G1 | Transported phase addition is isomorphic to real addition. | Retained without novelty/computational claims. |
| M1 | A compatible multiplicative process has a logarithmic-spiral one-phase form. | Retained. |
| R1 | Constant additive diffusion forces a line, plus the drift constraint \(m=(a/b)s+\tfrac12ss'\). | Corrected. |
| R2 | Constant multiplicative diffusion forces a logarithmic spiral, plus constant phase drift and log-drift compatibility. | Corrected. |
| T1 | Moving-line polar coordinates work away from deterministic origin-crossing times and chart singularities. | Corrected. |

## 6. Claims deliberately rejected

The following statements will not appear as conclusions of Phase 5:

- \(i^2=-1\) and \((dW)^2=dt\) are the same algebraic fact;
- a finite increment satisfies \((\Delta W)^2=\Delta t\);
- a nonlinear coordinate change creates a new stochastic dimension;
- the secant phase winds around the origin;
- the Cayley image is ordinary circular Brownian motion;
- every phase-radius representation requires an injective argument;
- the line/spiral diffusion calculation alone proves an iff theorem for the
  full drift-diffusion SDE;
- a Borel radius may automatically be differentiated with Itô's formula;
- numerical agreement proves a theorem or a novelty claim;
- an invertible transform automatically makes an analytically or numerically
  difficult problem easier.

## 7. Verification obligations carried forward

The remaining Phase 5 work must:

1. prove F1, A1--A4, R1, R2, and the boundary statements with explicit
   quantifiers;
2. verify every retained algebraic identity symbolically and numerically;
3. test the exact transition kernel, semigroup, and invariant geometry;
4. compare exact phase simulation against Euler--Maruyama and scalar
   baselines;
5. include noncollinear, radial-line, planar, multifactor, and
   hypoelliptic negative controls;
6. distinguish coordinate convenience from new solvability or complexity
   reduction;
7. use primary literature to establish terminology and novelty boundaries.

This audit freezes the candidate layer: later Phase 5 artifacts may cite the
corrected ledger above, but they must not silently import stronger claims from
the supplied documents.
