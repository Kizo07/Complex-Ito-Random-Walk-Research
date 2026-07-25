# Phase 5 literature review and novelty boundary

## 1. Research question

Phase 5 asks whether the one-driver complex affine process

\[
Z_t=Z_0+a t+bW_t
\]

can be written, without retaining \(t\) and \(W_t\) as state coordinates, as

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t},
\]

where the real phase \(\theta_t\) is the only stochastic state variable and the
radius is a deterministic, time-independent function of that phase.

The literature search had four purposes:

1. determine whether this precise representation/classification is already a
   named result;
2. locate the construction inside established stochastic transformation,
   directional-statistics, and polar Brownian theory;
3. identify mathematically justified applications to vector geometry,
   complex calculus, PDEs, and numerical methods;
4. prevent ordinary coordinate identities from being presented as a new
   stochastic calculus.

Searches were conducted through journal, society, institutional-repository,
Numdam, Project Euclid, J-STAGE, AMS, SIAM, and publisher records. Search terms
included combinations of:

- Brownian motion, arctangent transform, secant polar equation, affine line,
  one-phase Euler form;
- Lamperti transform, Doss--Sussmann transform, stochastic change of
  variables;
- Cayley transform, stereographic projection, compactified diffusion;
- projected normal, angular Gaussian, singular Gaussian angle;
- planar Brownian winding and skew-product decomposition;
- exact diffusion simulation, stochastic Lie group integrator,
  symmetry-adapted coordinates;
- rational Chebyshev, unbounded-domain compactification, Fokker--Planck;
- complex-valued semimartingale calculus, Wirtinger calculus, and complex-step
  differentiation.

This is a focused mathematical literature review, not a claim that every
publication containing an equivalent elementary identity has been exhausted.

## 2. Primary-source map

### 2.1 Stochastic calculus and one-dimensional diffusion transforms

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| K. Itô, [“Stochastic Integral” (1944)](https://doi.org/10.3792/pia/1195572786) | Construction of the stochastic integral underlying Itô calculus. | Foundational distinction between stochastic quadratic variation and ordinary complex multiplication. | It does not identify \(i^2=-1\) with \((dW)^2=dt\), and it does not state the Phase 5 polar classification. |
| J. Lamperti, [“A simple construction of certain diffusion processes” (1964)](https://doi.org/10.1215/kjm/1250524711) | State transformations for one-dimensional diffusions; the work is the classical source associated with the Lamperti transform. | Places \(\theta=\arctan(x/c)\) in the established tradition of invertible scalar diffusion coordinates. | Phase 5 uses a specific bounded coordinate with an exact inverse and polar geometry; it is not a new general diffusion-transform theory. |
| H. Doss, [“Liens entre équations différentielles stochastiques et ordinaires” (1977)](https://www.numdam.org/item/AIHPB_1977__13_2_99_0/) | Relates classes of stochastic differential equations to ordinary differential equations. | Supports the general principle that a stochastic state may be encoded through a deterministic flow/coordinate map. | The Phase 5 secant and Cayley maps are direct Itô diffeomorphisms, not applications of the full Doss theorem. |
| H. J. Sussmann, [“An interpretation of stochastic differential equations as ordinary differential equations which depend on the sample point” (1977)](https://doi.org/10.1090/S0002-9904-1977-14312-7) and [“On the gap between deterministic and stochastic ordinary differential equations” (1978)](https://doi.org/10.1214/aop/1176995608) | Pathwise/flow interpretations and the distinction between stochastic and deterministic differential equations. | Context for the Stratonovich form and for not confusing a coordinate pullback with removal of randomness. | These works do not make a one-driver process deterministic or increase its stochastic dimension. |
| A. Černý and J. Ruf, [“Simplified stochastic calculus via semimartingale representations” (2022)](https://doi.org/10.1214/21-EJP729) | A unified treatment of real- and complex-valued semimartingales and predictable transformations. | Modern evidence that complex notation can organize semimartingale transformations without changing their probabilistic content. | It does not make a phase curve holomorphic or supply the affine iff theorem. |

The primary conclusion from this strand is conservative: a one-phase Euler
form is an invertible stochastic coordinate when its inverse exists. The
change-of-variables formula determines the new drift and diffusion. It does not
identify the new coordinate as an independent noise source.

### 2.2 Boundary theory, support, and stochastic dimension

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| W. Feller, [“Diffusion processes in one dimension” (1954)](https://doi.org/10.1090/S0002-9947-1954-0063607-6) | Classical scale/speed and boundary theory for one-dimensional diffusions. | Classifies the finite angular endpoints corresponding to \(x=\pm\infty\). | The boundary label follows only after the scale/speed integrals or the global diffeomorphism are checked. |
| D. Stroock and S. R. S. Varadhan, [“On the Support of Diffusion Processes with Applications to the Strong Maximum Principle” (1972)](https://doi.org/10.1525/9780520375918-020) | Characterizes diffusion support through deterministic skeletons under regularity hypotheses. | Provides wider context for distinguishing the number of drivers from the dimension swept out through drift/noise geometry. | The Phase 5 affine impossibility proof is elementary and uses a randomized-time density; it does not require invoking the full support theorem. |
| L. Hörmander, [“Hypoelliptic second order differential equations” (1967)](https://doi.org/10.1007/BF02392081) | Lie-bracket conditions can yield smooth higher-dimensional densities even when the instantaneous diffusion matrix is degenerate. | Supplies the key negative-control lesson: one Brownian driver need not confine a time-evolving system to one fixed curve. | A scalar phase chart cannot encode a genuinely two-dimensional Markov state merely because the original SDE has one driver. |

This strand is essential to the “vector mathematics” question. The equality
\(\mathbb C\simeq\mathbb R^2\) offers convenient planar notation, but a curve
\(F(\theta)\) has differential of rank at most one. Conversely, drift and
brackets can make a one-driver, multi-state diffusion have a two-dimensional
density. Driver count, instantaneous covariance rank, support dimension, and
state-space dimension are related but not interchangeable notions.

### 2.3 Directional statistics and projected Gaussian angles

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| T. M. Pukkila and C. R. Rao, [“Pattern recognition based on scale invariant discriminant functions” (1988)](https://doi.org/10.1016/0020-0255(88)90012-6) | Derives angular Gaussian and related scale-invariant distributions by radial projection. | Establishes the projected-normal family as the correct statistical neighborhood for Gaussian arguments. | The usual density formulas concern nondegenerate multivariate Gaussian models. The Phase 5 affine state is a rank-one singular Gaussian on a line. |
| A. Wang and A. E. Gelfand, [“Directional data analysis under the general projected normal distribution” (2013)](https://doi.org/10.1016/j.stamet.2012.07.005) | Develops the general projected normal as a flexible model for circular data. | Confirms terminology and the distinction between a Gaussian vector and its angular projection. | The Phase 5 phase law should be called a singular or degenerate projected-normal case, not silently assigned a full-rank projected-normal density. |

At each fixed \(t\), the real and imaginary parts of \(Z_t\) form a degenerate
bivariate Gaussian with rank-one covariance \(t\,bb^\mathsf T\) in real
coordinates. Its argument is therefore naturally related to projected-normal
statistics, but its line support makes the phase distribution much simpler:
it is an arctangent transform of a scalar normal variable.

### 2.4 Stereographic projection and Cayley compactification

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| T. K. Carne, [“Brownian motion and stereographic projection” (1985)](https://www.numdam.org/item/AIHPB_1985__21_2_187_0/) | Relates stereographic projection of Euclidean Brownian paths to conditioned spherical Brownian motion, with the appropriate probabilistic structure. | Shows that Brownian/stereographic relations are classical and provides the closest geometric literature to the Cayley transform. | Carne's spherical process, conditioning, dimension, and time/conformal structure are not the same as the direct one-dimensional Cayley image used here. |
| L. Schwartz, [“Le mouvement brownien sur \(\mathbb R^N\), en tant que semi-martingale dans \(S_N\)” (1985)](https://eudml.org/doc/77244) | Treats Euclidean Brownian motion as a semimartingale in a spherical compactification. | Reinforces the legitimacy of compactified semimartingale coordinates. | It does not imply that the Cayley image of real Brownian motion is standard Brownian motion on \(S^1\). |

The Phase 5 Cayley variable

\[
U_t=\frac{1+iY_t/c}{1-iY_t/c}=e^{i\Theta_t},
\qquad
\Theta_t=2\arctan(Y_t/c),
\]

is an exact one-point compactification coordinate on \(\mathbb R\). Its angular
diffusion coefficient vanishes at the omitted point. It is therefore not
ordinary circular Brownian motion, whose angle has constant diffusion
coefficient before taking a value modulo \(2\pi\).

### 2.5 Planar Brownian polar theory and winding

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| F. Spitzer, [“Some theorems concerning 2-dimensional Brownian motion” (1958)](https://doi.org/10.1090/S0002-9947-1958-0104296-5) | Classical results for planar Brownian radius and winding, including the Cauchy scaling law for the argument. | Benchmark for what genuine two-dimensional Brownian winding looks like. | A one-driver affine line phase stays in an interval of length \(\pi\) and has no Spitzer-type winding. |
| J. Pitman and M. Yor, [“Asymptotic laws of planar Brownian motion” (1986)](https://doi.org/10.1214/aop/1176992436) | Develops planar Brownian winding and crossing laws through random time changes, martingale calculus, and excursion theory. | Supports the classical radial/angular skew-product comparison. | The radius and angle of planar Brownian motion are not deterministic functions of one another; two independent Brownian coordinates appear after time change. |

This comparison fixes terminology. The Phase 5 additive phase is a polar chart
of a rank-one affine Gaussian process. It is not a replacement for the
classical two-dimensional skew product. The compatible multiplicative spiral
can wind, but its radius is deliberately locked to its unwrapped phase and its
fixed-time support remains one-dimensional.

### 2.6 Exact simulation and geometric numerical integration

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| A. Beskos and G. O. Roberts, [“Exact simulation of diffusions” (2005)](https://doi.org/10.1214/105051605000000485) | Exact finite-dimensional simulation for a class of diffusions via rejection methods. | Establishes the importance of separating exact transition sampling from time-discretization approximations. | The Phase 5 diffusion is easier: its exact step follows immediately by transforming a Gaussian increment and requires no rejection sampler. |
| S. J. A. Malham and A. Wiese, [“Stochastic Lie Group Integrators” (2008)](https://doi.org/10.1137/060666743) | Pulls stochastic flows to Lie groups/algebras and pushes approximations back so they remain on the target manifold. | Supplies a rigorous example of geometry improving invariant preservation and, for some methods, accuracy. | The transported secant group law is only an isomorphic copy of \((\mathbb R,+)\); it does not by itself produce a superior integrator. |
| F. C. De Vecchi, A. Romano, and S. Ugolini, [“A symmetry-adapted numerical scheme for SDEs” (2019)](https://doi.org/10.3934/jgm.2019018) | Uses Lie symmetries to construct adapted coordinates and symmetry-preserving schemes, with error estimates for linear SDEs. | Demonstrates the correct standard for claiming a coordinate-based numerical benefit: preserve a structure and measure/prove an error improvement. | A visual polar representation alone is not such evidence. |
| C. C. Chen, D. Cohen, and J. L. Hong, [“Conservative Methods for Stochastic Differential Equations with a Conserved Quantity” (2016)](https://global-sci.com/index.php/ijnam/article/view/10245) | Constructs conservative stochastic schemes with mean-square/weak convergence results. | Motivates testing the Cayley representation for exact unit-modulus preservation. | The original additive state has no unit-circle invariant; only its Cayley transform does. |

The immediate computational conclusion is negative but useful. For the
canonical additive model, the best phase sampler is

\[
\theta_{s+h}
=
\arctan\!\left(
\tan\theta_s+\frac{\mu h}{c}
+\frac{\sigma\sqrt h}{c}\xi
\right),
\qquad \xi\sim N(0,1).
\]

This is exact because it transports the known Gaussian step. It is not faster
than simulating the scalar Gaussian state and applying one arctangent; it is
the same computation in a different order. Approximate phase SDE schemes are
valuable only as controlled examples of boundary/invariant behavior.

### 2.7 Compactification and PDE discretization

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| J. P. Boyd, [“Spectral methods using rational basis functions on an infinite interval” (1987)](https://doi.org/10.1016/0021-9991(87)90158-6) | Maps an infinite interval to a finite angular interval and develops rational spectral bases, with convergence and sparsity results for suitable problems. | Shows a legitimate route by which \(x=c\tan\theta\) can help PDE computation on \(\mathbb R\). | Endpoint coefficient degeneracy and transformed-function regularity determine whether the map helps. A bounded interval alone is not an accuracy theorem. |
| C. E. Grosch and S. A. Orszag, [“Numerical solution of problems in unbounded regions: coordinate transforms” (1977)](https://doi.org/10.1016/0021-9991(77)90102-4) | Studies coordinate mappings for unbounded-domain numerical problems. | Earlier basis for comparing truncation in \(x\) with compactification in \(\theta\). | The Phase 5 numerical experiment is a small benchmark, not a general spectral convergence result. |

The backward generator transforms exactly:

\[
\mu\,\partial_x+\frac{\sigma^2}{2}\partial_{xx}
\quad\longleftrightarrow\quad
A(\theta)\partial_\theta
+\frac{B(\theta)^2}{2}\partial_{\theta\theta}.
\]

Thus analytic difficulty is conjugated, not erased. Potential numerical
benefit comes from representing infinity by natural finite endpoints or from a
basis adapted to the map. Potential harm comes from coefficient degeneracy,
endpoint singularities, and extra trigonometric evaluations.

### 2.8 Complex differentiation

| Source | Primary result relevant here | Phase 5 use | Limit of the connection |
|---|---|---|---|
| W. Squire and G. Trapp, [“Using Complex Variables to Estimate Derivatives of Real Functions” (1998)](https://doi.org/10.1137/S003614459631241X) | Introduces a practical complex-variable derivative approximation that avoids subtractive cancellation for suitable analytic extensions. | Provides a concrete, existing numerical advantage from complex arithmetic against which the Phase 5 embedding can be compared. | The complex-step method requires analyticity of the extended computation. Embedding a real curve in \(\mathbb C\) does not make a nonholomorphic payoff analytic. |
| D. H. Brandwood, [“A complex gradient operator and its application in adaptive array theory” (1983)](https://doi.org/10.1049/ip-f-1.1983.0003) | Develops complex-gradient/Wirtinger-style tools for nonanalytic complex functions. | Supports using \(z,\bar z\) derivatives when a real two-coordinate calculation is written compactly in complex form. | Wirtinger notation repackages two real derivatives; a rank-one phase curve supplies only a directional derivative unless an off-curve extension is chosen. |

For \(F(\theta)=r(\theta)e^{i\theta}\), differentiating
\(h(F(\theta))\) gives a derivative along the curve:

\[
\frac{d}{d\theta}h(F(\theta))
=
h_z(F,\overline F)F'(\theta)
+h_{\bar z}(F,\overline F)\overline{F'(\theta)}.
\]

This is useful notation, but it neither supplies a unique derivative normal to
the curve nor repairs failure of the Cauchy--Riemann equations.

## 3. Claim-to-source matrix

The following matrix records exactly which Phase 5 claims rely on literature
and which are proved directly in this project.

| Phase 5 claim | Evidence type | Source or proof location |
|---|---|---|
| Itô calculus is governed by quadratic covariation, not the identity \(i^2=-1\). | Foundational literature plus direct calculation. | Itô (1944); `PHASE_5_MATHEMATICAL_FOUNDATIONS.md`. |
| Smooth invertible scalar changes of variable produce equivalent one-dimensional diffusions. | Classical transformation literature. | Lamperti (1964), Itô formula; direct conjugacy proof. |
| The exact affine one-phase representation exists iff \(a/b\in\mathbb R\) and \(b/Z_0\notin\mathbb R\). | Project theorem, proved directly. | `PHASE_5_MATHEMATICAL_FOUNDATIONS.md`. |
| A Borel polar graph is planar-null, and randomizing time makes the noncollinear process absolutely continuous in the plane. | Direct measure-theoretic proof. | `PHASE_5_MATHEMATICAL_FOUNDATIONS.md`; no novelty attributed to the component lemmas. |
| The phase endpoints are natural. | Classical boundary framework plus direct scale/speed/diffeomorphism calculation. | Feller (1954); Phase 5 foundations and notebook evidence. |
| The phase angle of a rank-one affine Gaussian is a singular projected-normal variable. | Directional-statistics positioning plus direct covariance-rank calculation. | Pukkila--Rao (1988), Wang--Gelfand (2013). |
| The Cayley image is not ordinary circular Brownian motion. | Direct generator comparison; stereographic literature establishes nearby but different constructions. | Carne (1985), Schwartz (1985), direct SDE calculation. |
| One Brownian driver does not imply one-dimensional state support for a multi-state diffusion. | Classical support/hypoelliptic context plus explicit negative control. | Stroock--Varadhan (1972), Hörmander (1967), notebook hypoelliptic example. |
| Planar Brownian winding is structurally different from the affine phase. | Classical primary results. | Spitzer (1958), Pitman--Yor (1986). |
| Geometry-preserving stochastic coordinates can matter numerically only when a structure/error result is demonstrated. | Primary numerical literature plus Phase 5 benchmarks. | Malham--Wiese (2008), De Vecchi--Romano--Ugolini (2019), Chen--Cohen--Hong (2016). |
| Arctangent compactification may help some unbounded-domain PDE discretizations. | Primary spectral literature plus matched benchmark. | Grosch--Orszag (1977), Boyd (1987), Phase 5 notebook. |
| Complex embedding does not automatically unlock holomorphic differentiation. | Complex differentiation literature plus direct Cauchy--Riemann/Wirtinger analysis. | Squire--Trapp (1998), Brandwood (1983), Phase 5 implications document. |

## 4. Search result for the exact proposed representation

Focused searches did not locate a primary paper that states the following
package as one theorem:

1. the measurable lossless, time-independent genuine-phase formulation;
2. the affine iff conditions \(a/b\in\mathbb R\) and
   \(b/Z_0\notin\mathbb R\);
3. the explicit sine/secant radius, inverse, and angular domain;
4. the randomized-time Borel impossibility proof;
5. the exact phase generator, transition density, semigroup, and boundary
   classification;
6. the corresponding Cayley, group, multiplicative-spiral, and rigidity
   comparison.

This negative search result is not proof of absolute novelty. Several
components are elementary or classical:

- the polar equation of a line;
- the arctangent and tangent half-angle identities;
- Itô change of variables;
- Gaussian change-of-variable densities;
- the Cayley transform;
- logarithmic spirals;
- pullback group operations.

Accordingly, the defensible contribution is a **rigorous synthesis and
classification tailored to a stochastic representation question**, together
with proof repairs and controlled computational comparisons. Phase 5 will not
claim discovery of the component identities.

## 5. Terminology decisions

The paper will use:

- **one-phase Euler representation** for
  \(Z/Z_0=r(\theta)e^{i\theta}\);
- **lossless** only when the underlying scalar state is recoverable from the
  chosen unwrapped phase;
- **time-independent** only when \(r\) has no explicit \(t\);
- **genuine phase** only when \(\theta\bmod 2\pi\) is the geometric argument;
- **rank-one affine Gaussian** for the fixed-time complex law;
- **singular projected-normal angle** as a literature connection, not as an
  assertion that a full-rank projected-normal density applies;
- **Cayley compactification** for the unit-circle transform;
- **transported group law** for the tangent/arctangent operation;
- **coordinate equivalence** for the Brownian/phase Markov isomorphism.

The paper will avoid:

- “Brownian rotation” for the bounded secant phase;
- “circular Brownian motion” for the Cayley image;
- “two-dimensional Brownian motion” for a one-driver affine line;
- “new stochastic dimension” for a complex embedding;
- “analytic solution” when only a coordinate identity has been written;
- “numerical improvement” without a matched error-and-cost comparison.

## 6. Research conclusions that constrain implementation

The literature changes the implementation plan in six concrete ways.

1. **Exact sampling is the primary baseline.** The phase transition is a
   transformed Gaussian, so Euler--Maruyama must be compared against this
   exact step rather than treated as ground truth.
2. **Boundary behavior is proved, not inferred from plots.** The arctangent
   chart is conjugate to the entire real line, and Feller scale/speed
   calculations will be reported.
3. **The Cayley experiment compares generators.** It must demonstrate both
   exact unit modulus and nonconstant angular diffusion.
4. **Vector claims use negative controls.** Planar Brownian motion and the
   hypoelliptic system \(dX=dW,\ dY=X\,dt\) show why driver count is not a
   one-phase classification.
5. **PDE claims are benchmarked.** Compactification will be compared with a
   scalar/unbounded-domain baseline at matched resolution and evaluated for
   error, conditioning, and runtime.
6. **Complex-derivative claims are scoped.** Directional, Wirtinger, and
   complex-step derivatives will be tested separately so that complex notation
   is not confused with holomorphic structure.

## 7. Bottom line

Existing research strongly supports the ingredients of Phase 5:
one-dimensional diffusion transforms, compactifications, projected Gaussian
angles, polar Brownian theory, complex semimartingale notation, and
geometry-aware numerics are all established fields.

The literature does **not** support the stronger idea that placing a scalar
Brownian state into one Euler factor creates an independent rotational
mechanism or a generally more powerful stochastic calculus. What Phase 5 can
contribute is the exact boundary between:

- a valid, lossless phase coordinate;
- a visually suggestive but information-losing angle;
- a transformed process rather than the original process;
- a compatible logarithmic spiral that truly winds;
- and a genuinely higher-dimensional diffusion that no single phase can
  encode.
