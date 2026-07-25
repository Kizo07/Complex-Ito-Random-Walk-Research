# One-Phase Euler Coordinates for Affine Brownian Factors — Paper Design

**Date:** 2026-07-25

**Status:** Approved

**Owner:** Codex under the standing user-authorized direct implementation
exception

**Independent reviewer:** OpenCode `zai-coding-plan/glm-5.2`, review and
second opinion only

## 1. Objective

Create a self-contained, venue-neutral mathematical-finance paper that
classifies exactly when the affine complex Brownian process

\[
Z_t=Z_0+a t+bW_t
\]

admits a lossless, time-independent Euler representation

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t}
\]

whose phase \(\theta_t\) is the sole stochastic coordinate. The paper will
derive the resulting phase diffusion, establish its transition and boundary
theory, connect it rigorously to normal/Bachelier financial factors, and audit
the geometric, analytic, and numerical consequences.

The manuscript must read as an independent academic article. It must not
mention internal task names, planning documents, critiques, repository
history, or development-phase labels.

## 2. Central contribution and novelty boundary

The paper's primary mathematical contribution is the complete classification
of nondegenerate affine complex Brownian processes admitting the requested
representation. For \(Z_0b\ne0\), such a representation exists if and only if

\[
\frac{a}{b}\in\mathbb R,
\qquad
\frac{b}{Z_0}\notin\mathbb R.
\]

Writing

\[
a=\lambda b,\qquad
\frac b{Z_0}=\rho e^{i\phi},\qquad
x_t=\lambda t+W_t,
\]

the exact representation is

\[
Z_t
=
Z_0\frac{\sin\phi}{\sin(\phi-\theta_t)}e^{i\theta_t},
\qquad
\theta_t=\arg\!\left(1+\rho e^{i\phi}x_t\right)\in I_\phi.
\]

The paper will claim novelty only for the precise classification, its
necessity and sufficiency proof, the unified phase-domain stochastic theory,
the additive-versus-multiplicative rigidity synthesis, and the explicit
financial-pricing conjugacy with a controlled numerical audit.

The paper will not claim to invent:

- the arctangent transformation;
- compactification of an unbounded financial domain;
- Itô changes of variables;
- the Lamperti, Doss--Sussmann, or Zvonkin transformations;
- complex-valued linear stochastic differential equations;
- stochastic exponentials or complex geometric Brownian motion;
- projected angular distributions;
- the Cayley or stereographic transform;
- structure-preserving stochastic integration; or
- Bachelier/normal option pricing.

## 3. Intended readership and style

The manuscript targets researchers in stochastic analysis, mathematical
finance, computational finance, and geometric numerical integration. It will
use a theorem-led exposition, precise probabilistic assumptions, numbered
equations, cross-referenced propositions, reproducible numerical evidence, and
primary-source citations.

The format remains venue-neutral so that it can later be adapted to a journal
template without rewriting the mathematical narrative. The target is
approximately 35--50 letter-size pages, including appendices and references.

## 4. Assumption framework

The paper will state all assumptions before the main theorem:

1. \((\Omega,\mathcal F,(\mathcal F_t)_{t\ge0},\mathbb P)\) satisfies the usual
   conditions.
2. \(W\) is a one-dimensional standard Brownian motion.
3. \(Z_0,a,b\in\mathbb C\), with degenerate cases \(Z_0=0\), \(b=0\), and
   collinear rays treated separately.
4. A *genuine one-phase representation* means a deterministic,
   time-independent map \(F:I\to\mathbb C\), expressible as
   \(F(\theta)=r(\theta)e^{i\theta}\), together with a scalar adapted process
   \(\theta_t\), such that \(Z_t=Z_0F(\theta_t)\) pathwise up to any stated
   stopping time.
5. Losslessness means that the scalar driver state can be recovered from
   \(\theta_t\) by a deterministic inverse on the selected phase interval.
6. Borel factorization is distinguished from the \(C^2\) regularity required
   for direct application of Itô's formula.
7. Polar arguments and logarithms are localized away from zeros and supplied
   with an explicit branch or continuous lift.
8. Equalities are labeled as pathwise, almost sure, distributional, weak, or
   numerical approximations as appropriate.
9. Quadratic variation is stated as \(d[W,W]_t=dt\); no finite Brownian
   increment is asserted to satisfy \((\Delta W)^2=\Delta t\).
10. Financial pricing statements introduce an equivalent martingale measure,
    numeraire, integrability conditions, and payoff regularity separately from
    the physical-measure geometry.

## 5. Mathematical architecture

### 5.1 Measurable factorization

The paper first separates the abstract question "does \(Z_t\) factor through
one scalar state?" from the stronger Euler-coordinate question. The
Doob--Dynkin principle motivates measurable factorization, while the support
of the affine process identifies the geometry that any time-independent
factorization must encode.

### 5.2 Classification theorem

The sufficiency proof will construct the phase map explicitly. The necessity
proof will show that:

- the support at each time lies on an affine line directed by \(b\);
- a single time-independent curve must contain the union of these supports;
- the deterministic drift cannot move that line transversely, forcing
  \(a/b\in\mathbb R\); and
- if the support line passes through the polar origin, ordinary angle loses
  injectivity, forcing \(b/Z_0\notin\mathbb R\) for a genuine lossless phase.

All degenerate and exceptional configurations will be catalogued.

### 5.3 Canonical secant representation

After an affine rotation and scale change, the support becomes a vertical
line:

\[
1+iy=\sec\theta\,e^{i\theta},
\qquad
y=\tan\theta,
\qquad
\theta\in\left(-\frac\pi2,\frac\pi2\right).
\]

This canonical representation supplies the clearest bridge to an arithmetic
Brownian financial factor.

### 5.4 Phase diffusion

For

\[
dX_t=\mu\,dt+\sigma\,dW_t,
\qquad
\theta_t=\arctan(X_t/c),
\]

Itô's formula gives

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

The inverse \(X_t=c\tan\theta_t\) will be used to verify the SDE independently.
The general affine formula will then be recovered by rotation and scale.

### 5.5 Generator, kernel, and boundaries

The phase generator is

\[
\mathcal L_\theta f
=
A(\theta)f'(\theta)
+
\frac12B^2(\theta)f''(\theta),
\]

with \(A\) and \(B\) as above. The transition density is obtained by
change of variables from the Gaussian kernel:

\[
p_\theta(s,\vartheta;t,\eta)
=
p_X\!\left(s,c\tan\vartheta;t,c\tan\eta\right)
c\sec^2\eta.
\]

The paper will verify density normalization, Chapman--Kolmogorov consistency,
the forward equation, and the natural/inaccessible character of the phase
endpoints for finite times.

### 5.6 Rigidity and group structure

The additive line family will be contrasted with the logarithmic-spiral family
arising from multiplicative stochastic exponentials. The transported group
law

\[
\theta_1\oplus\theta_2
=
\arctan\!\left(\tan\theta_1+\tan\theta_2\right)
\]

on the canonical chart will be identified as an isomorphic copy of real
addition, not ordinary multiplication on \(S^1\). The paper will derive the
corresponding general-affine operation and state its domain restrictions.

## 6. Financial architecture

### 6.1 Normal/Bachelier factor

Under a suitable pricing measure, an arithmetic factor or forward satisfies

\[
dF_t=\sigma_N\,dW_t.
\]

Its phase representation is

\[
\mathcal Z_t
=
1+iF_t/c
=
\sec\theta_t e^{i\theta_t},
\qquad
\theta_t=\arctan(F_t/c).
\]

The complex quantity is a coordinate representation of the real financial
factor, not a claim that market prices are intrinsically complex-valued.

### 6.2 Pricing conjugacy

For

\[
V(t,x)
=
\mathbb E^\mathbb Q\!\left[
e^{-\int_t^T r_s\,ds}g(X_T)\mid X_t=x
\right],
\]

define \(v(t,\theta)=V(t,c\tan\theta)\). The transformed pricing equation is

\[
v_t
+A(\theta)v_\theta
+\frac12B^2(\theta)v_{\theta\theta}
-rv
=0,
\qquad
v(T,\theta)=g(c\tan\theta).
\]

The paper will prove this both by generator conjugacy and direct chain-rule
substitution.

### 6.3 Greeks

The coordinate relations are

\[
V_x
=
\frac{\cos^2\theta}{c}v_\theta,
\]

\[
V_{xx}
=
\frac{\cos^4\theta}{c^2}v_{\theta\theta}
-
\frac{2\sin\theta\cos^3\theta}{c^2}v_\theta.
\]

Normal-model European calls provide closed-form validation. The manuscript
will also discuss the transformed payoff regularity near the compactified
boundary and the implications for finite differences and spectral methods.

### 6.4 Measure changes and hedging

Girsanov changes the scalar drift but not the one-dimensional diffusion
direction. Consequently, eligibility for the canonical phase chart is
preserved for scalar arithmetic factors under equivalent measure changes.
Prices, deltas, gammas, and self-financing hedges remain coordinate-invariant
after correct Jacobian conversion.

### 6.5 Financial limitations

The paper will state explicitly:

- an exact invertible coordinate change cannot change an exact option value;
- round-trip Monte Carlo or quasi-Monte Carlo has identical samples and
  variance absent an additional algorithmic change;
- path-dependent claims require history or additional Markov state;
- stochastic volatility and multifactor models generally cannot be compressed
  losslessly into one smooth phase;
- compactification may improve spatial resolution while worsening operator
  conditioning near the endpoints; and
- no general closed-form solution follows merely from Euler notation.

## 7. Literature design

Each major section will be supported by primary papers or authoritative
monographs. The research record will contain:

- verified bibliographic metadata and stable DOI/publisher links;
- a claim-to-source matrix;
- a novelty-boundary matrix;
- page or theorem pointers where available;
- a record of sources rejected as weak, derivative, or irrelevant; and
- an audit showing that every cited key is used and every substantive
  historical claim has support.

The literature groups are:

1. Brownian motion, Bachelier, and diffusion limits;
2. Itô calculus, stochastic transformations, and measure changes;
3. one-dimensional support, boundary classification, and hypoellipticity;
4. polar/angular distributions, Brownian winding, and stereographic maps;
5. stochastic exponentials and complex-valued SDEs;
6. normal-model derivative pricing and risk-neutral valuation;
7. financial PDE compactification and unbounded-domain numerics;
8. Monte Carlo and quasi-Monte Carlo in finance;
9. geometric and structure-preserving stochastic integration; and
10. Wirtinger calculus, complex-step differentiation, and Fourier methods in
    finance.

## 8. Computational and visual design

The paper receives a new deterministic discovery notebook generated from a
plain Python builder. It will import the already tested root mathematical
model rather than duplicate core formulas.

The notebook will:

- record the unchanged `phase3-paper` conda environment and package versions;
- execute top to bottom from a clean kernel;
- use deterministic seeds in the `20260725` family;
- save all figures as vector PDF and raster PNG;
- save numerical evidence as CSV or JSON;
- report Monte Carlo standard errors and numerical tolerances;
- assert exact identities and acceptance thresholds; and
- avoid absolute paths in notebook code.

Planned publication figures include:

1. line support and one-phase Euler geometry;
2. general affine rotation/scale construction;
3. admissible and obstructed parameter configurations;
4. exact phase-radius reconstruction;
5. scalar and phase sample paths;
6. phase drift and diffusion coefficients;
7. exact versus Euler phase stepping near the boundary;
8. transition-density and probability-integral-transform diagnostics;
9. generator and Fokker--Planck diagnostics;
10. natural-boundary and tail behavior;
11. transported additive group geometry;
12. additive secant line versus multiplicative logarithmic spiral;
13. one driver, covariance rank, and support dimension;
14. Bachelier forward mapped to the phase interval;
15. normal-call value surface in scalar and phase coordinates;
16. delta and gamma transformation;
17. direct versus compactified pricing-PDE error;
18. PDE error versus conditioning trade-off;
19. Monte Carlo and quasi-Monte Carlo samplewise equivalence;
20. path-dependent and multifactor non-compressibility controls;
21. Wirtinger and complex-step limitations; and
22. contribution, implication, and limitation map.

## 9. Manuscript structure

1. Abstract
2. Keywords, MSC classifications, and JEL classifications
3. Introduction
4. Literature review and novelty boundary
5. Probabilistic and financial setup
6. From complex embeddings to the one-phase question
7. Measurable factorization and support geometry
8. Exact affine classification theorem
9. Canonical secant chart and reconstruction
10. Phase SDE, generator, kernel, and boundary theory
11. Additive and multiplicative rigidity
12. Transported group structure
13. Risk-neutral pricing conjugacy
14. Normal-model option values and Greeks
15. Numerical methodology
16. Numerical and financial results
17. Stochastic dimension and vector geometry
18. Complex differentiation and analytic implications
19. Computational implications
20. Limitations
21. Research agenda
22. Conclusion
23. Appendices: proofs, Itô algebra, pricing derivations, numerical details,
    and reproducibility manifest

## 10. Rendering and accessibility

The self-contained Quarto project will render:

- a LuaLaTeX PDF with embedded fonts, numbered sections, cross-references,
  vector figures, and retained TeX;
- an HTML companion with raster figures, table of contents, code folding, and
  accessible alt text; and
- an executed notebook with saved outputs.

The render is rejected for unresolved citations or references, missing local
assets, empty alt text, clipped equations or tables, substituted fonts,
non-letter page sizes, notebook errors, or inconsistent reported numerical
values.

## 11. Verification

Acceptance requires:

1. all existing and new unit tests pass;
2. central formulas are independently re-derived in the manuscript;
3. the notebook executes twice from clean kernels;
4. deterministic tables and summary streams agree across executions;
5. every figure and table appears in a manifest;
6. every bibliography key resolves and is cited;
7. the PDF and HTML render without warnings that affect correctness;
8. PDF pages receive both automated and visual inspection;
9. HTML links, image sources, and alt text validate;
10. manuscript values match the notebook evidence;
11. `git diff --check` passes; and
12. OpenCode GLM 5.2 independently reviews the mathematics, novelty claims,
    finance, computation, and rendered artifacts.

## 12. Non-goals

The project will not:

- assert that complex algebra explains quadratic variation;
- call a one-driver curve-valued process planar Brownian motion;
- claim the coordinate map creates a new stochastic dimension;
- claim automatic variance reduction, dimensional reduction, or analytic
  solvability;
- represent a multifactor market losslessly with one phase without a theorem;
- interpret the auxiliary complex coordinate as a directly traded price;
- install or upgrade packages;
- alter prior completed papers or protected critique documents; or
- commit, push, publish, or open a pull request unless separately requested.
