# Research record: one-phase Euler coordinates for affine Brownian factors

**Audit date:** 2026-07-25

**Scope:** probability, stochastic analysis, mathematical finance,
computational finance, angular statistics, geometric integration, and complex
differentiation

**Purpose:** preserve the section-by-section source audit, novelty boundary,
and claims deliberately excluded from the manuscript

## 1. Search and source-selection method

The search proceeded by mathematical dependency rather than by title
similarity. Each planned manuscript section was decomposed into the external
claims it requires, and each claim was searched against publisher pages,
primary archives, original papers, or authoritative monographs. DOI metadata,
volume, issue, and page ranges were cross-checked where available.

The following source hierarchy was used:

1. original journal papers and monographs for foundational results;
2. publisher or institutional repository records for bibliographic
   verification;
3. authoritative modern monographs for standardized formulations and
   examples; and
4. peer-reviewed surveys only for contemporary context or literature
   consolidation.

Search-engine snippets, encyclopedias, informal web pages, preprints superseded
by journal articles, and generative summaries were not accepted as authority
for central claims. A 2024 preprint surveying risk-neutral arithmetic-Brownian
option valuation was useful for discovery but is not needed to support the
paper's central financial statements because original and peer-reviewed
sources are available.

## 2. Primary mathematical lineage

### 2.1 Brownian motion, diffusion limits, and finance

Bachelier's dissertation introduced a Gaussian diffusion model in speculative
finance and developed an option-pricing calculation decades before modern
semimartingale theory [@bachelier1900]. Wiener's construction supplied the
mathematical path-space foundation [@wiener1923], while Donsker later
formalized the random-walk-to-Brownian invariance principle
[@donsker1951]. These sources support the historical bridge between a discrete
random walk and the continuous arithmetic Brownian factor. Mörters and Peres
provide modern Brownian-motion notation, path properties, and support facts
used in the preliminaries [@mortersperes2010].

The paper must not retrospectively attribute modern risk-neutral pricing,
equivalent martingale measures, or Itô calculus to Bachelier. Those belong to a
later mathematical framework.

### 2.2 Itô calculus and change of measure

Itô's 1944 stochastic-integral paper is the foundational primary source
[@ito1944]; his 1951 paper gives the change-of-variables formula in the form
closest to the manuscript's derivations [@ito1951]. Girsanov's original
measure-change result supports the statement that an equivalent change of
measure changes drift while preserving the diffusion direction
[@girsanov1960]. Kac's Wiener-functional representation supplies the
probabilistic/PDE connection used in modern Feynman--Kac valuation
[@kac1949].

The manuscript will write quadratic variation as
\(d[W,W]_t=dt\). It will not state that a finite Brownian increment literally
satisfies \((\Delta W)^2=\Delta t\), and it will not identify quadratic
variation with the algebraic relation \(i^2=-1\).

### 2.3 Risk-neutral valuation

Black and Scholes derive option valuation from dynamic replication and
no-arbitrage [@blackscholes1973]; Merton supplies a broader rational-pricing
framework [@merton1973]. Harrison and Pliska place continuous trading,
stochastic integration, and martingale valuation in a general semimartingale
setting [@harrisonpliska1981]. These sources support the pricing-measure and
hedging discussion.

The auxiliary complex coordinate in this paper is not a new traded asset. The
financial state remains real, and prices are pulled back or pushed forward by
an invertible deterministic coordinate map.

## 3. Transformations of stochastic differential equations

### 3.1 Established transformation families

Lamperti's construction is the standard precedent for transforming scalar
diffusions, especially for normalizing a state-dependent diffusion coefficient
[@lamperti1964]. Doss and Sussmann develop pathwise transformations between
classes of stochastic and ordinary differential equations [@doss1977;
@sussmann1977]. Zvonkin constructs a one-to-one phase-space transformation
that removes irregular drift [@zvonkin1974].

These works establish that nonlinear coordinates for diffusions are a mature
subject. The paper therefore cannot claim novelty for applying a smooth
function to Brownian motion or for converting one scalar SDE into another.

### 3.2 Direct arctangent precedent

Särkkä and Solin use the exact solution

\[
X_t=\arctan\!\left(0.1\,W_t+\tan X_0\right)
\]

as a numerical-SDE benchmark [@sarkkasolin2019]. This is essentially the
canonical angular diffusion used here after scaling and drift are specialized.
The same exercise also appears in advanced stochastic-calculus teaching
material. Consequently:

- \(\arctan(W_t)\) is not a new stochastic process;
- its Itô coefficients are not a new formula in isolation; and
- boundary preservation under the exact inverse transform is not, by itself,
  a publishable novelty claim.

The defensible contribution begins with the exact *classification* of which
affine complex Brownian processes can be encoded by a time-independent,
lossless Euler phase, then develops the financial and rigidity consequences as
one synthesis.

### 3.3 Measurable versus smooth factorization

Kallenberg supplies the measurable-factorization principles and standard
probability-space language needed to distinguish a Borel state map from a
\(C^2\) Itô coordinate [@kallenberg2002]. This distinction is essential:
measurable scalar encoding can exist in pathological ways that have no useful
geometric or stochastic-differential interpretation.

## 4. Support, boundary behavior, and stochastic dimension

Feller's one-dimensional diffusion theory is the primary source for scale,
speed, and endpoint classification [@feller1954]. The manuscript's endpoints
are most simply classified by exact conjugacy to the real line, but Feller's
framework provides the conventional terminology.

Stroock and Varadhan identify diffusion support through controlled skeletons
[@stroockvaradhan1972]. Hörmander's hypoellipticity theorem shows why the
number of Brownian drivers alone does not determine fixed-time support
dimension: Lie brackets can spread one driver's influence through a
higher-dimensional state [@hormander1967]. The paper will therefore keep four
notions separate:

1. number of Brownian drivers;
2. instantaneous covariance rank;
3. fixed-time support dimension; and
4. dimension of a sufficient Markov state.

For the affine process studied here, the support is explicitly a line, so no
deep support theorem is required for the proof. The cited theory is used to
prevent an invalid generalization from this special case.

## 5. Angular variables, projection, and planar Brownian motion

### 5.1 Projected normal laws

Pukkila and Rao derive angular Gaussian distributions through scale-invariant
projection [@pukkilarao1988]. Wang and Gelfand develop the general projected
normal distribution for circular data [@wanggelfand2013]. These models clarify
that taking the argument of a Gaussian vector is an established operation.

The present process is more specialized: the Gaussian randomness lies on an
affine line in \(\mathbb C\), not in a nondegenerate planar Gaussian vector.
Its phase density is therefore obtained from a one-dimensional monotone change
of variables, not from a generic projected bivariate normal law.

### 5.2 Brownian winding

Spitzer and Pitman--Yor study the winding of genuine two-dimensional Brownian
motion [@spitzer1958; @pitmanyor1986]. Their results require two independent
planar coordinates and exhibit behavior absent from the rank-one affine line
model. They are used as a contrast, not as a derivation of the paper's phase
process.

### 5.3 Stereographic compactification

Carne studies Brownian motion under stereographic projection and the
associated time changes [@carne1985]. This confirms that compactifying
Euclidean Brownian state onto a sphere has substantial prior theory. The
canonical secant chart used in this paper is an exact coordinate chart for a
line; it must not be presented as the invention of stochastic
compactification.

## 6. Multiplicative stochastic structure and complex semimartingales

Dol{\'e}ans-Dade's change-of-variables work is foundational for stochastic
exponentials [@doleansdade1970]. Larsson and Ruf survey stochastic
exponentials and logarithms on stochastic intervals [@larssonruf2019].
Černý and Ruf develop semimartingale representations and multiplicative
compensation in a modern unified calculus [@cernyruf2022; @cernyruf2023].

These references support the comparison between:

- additive affine support, whose polar graph is a secant family; and
- multiplicative stochastic exponentials, whose one-driver complex paths lie
  on logarithmic spirals when log-radius and phase share the same scalar
  driver.

Neither stochastic exponentials nor complex geometric Brownian motion are new.
The contribution is the rigidity comparison and its role in classifying the
requested one-phase representation.

## 7. Bachelier/normal financial context

Schachermayer and Teichmann compare Bachelier and
Black--Merton--Scholes option formulas and explain their short-time proximity
[@schachermayerteichmann2008]. Choi, Kwak, Tee, and Wang give a modern,
peer-reviewed synthesis of the normal model, volatility conversion, risk
management, and its use when negative underlyings are plausible
[@choi2022]. CME's 2020 clearing advisory is the primary institutional source
for the temporary switch to Bachelier valuation for specified energy options
and negative strikes [@cme2020].

The paper uses the Bachelier model for three reasons:

1. its state is an affine Brownian factor, exactly matching the theorem;
2. its European call has a closed-form price and Greeks, giving exact
   verification benchmarks; and
3. normal pricing remains practically relevant for rates, commodities, and
   markets in which negative forwards or strikes can occur.

The paper will not claim that arithmetic Brownian motion is an adequate
universal equity-price model. It will state the familiar limitation that an
unbounded Gaussian level can become negative.

## 8. Financial PDE compactification

Duffie and Kan explicitly use arctangent transformations such as
\(y=\arctan(kx_0)\) when solving a term-structure derivative-pricing PDE
(p. 396) [@duffiekan1996]. This is direct prior use of the same compactifying
function in mathematical finance.

Grosch and Orszag analyze coordinate maps for differential equations on
unbounded regions, emphasizing that usefulness depends on asymptotic solution
behavior [@groschorszag1977]. Boyd develops rational spectral bases induced by
maps between infinite and finite intervals [@boyd1987].

Reisinger and Wittum address high-dimensional option-pricing approximations
[@reisingerwittum2007]. In 't Hout and Snoeijer map
\(\mathbb R^d\) to the open unit cube with a componentwise arctangent after a
logarithmic/principal-component transform [@inthoutsnoeijer2021].
Cont and Voltchkova give a rigorous finite-domain localization analysis in
jump-diffusion option pricing [@contvoltchkova2005].

These sources impose a strict novelty boundary:

- arctangent compactification in finance is established;
- mapping an unbounded PDE to a bounded interval is established;
- the paper may report a new matched benchmark or conditioning analysis, but
  not claim invention of the method; and
- any numerical advantage must be parameter-, payoff-, and discretization-
  specific.

## 9. Simulation and numerical SDE context

Higham supplies the standard shared-path convergence methodology and canonical
Euler--Maruyama/Milstein exposition [@higham2001]. Beskos and Roberts show that
exact diffusion simulation has a precise algorithmic meaning beyond merely
applying a known inverse transformation [@beskosroberts2005]. Malham and Wiese
develop stochastic Lie-group integrators [@malhamwiese2008], while De Vecchi,
Romano, and Ugolini construct symmetry-adapted SDE schemes
[@devecchi2019].

The paper will call the transformed Gaussian step *exact for this explicitly
conjugate model*, not a general exact-simulation algorithm.

Boyle introduced Monte Carlo option valuation under risk neutrality
[@boyle1977]. Paskov and Traub documented the use of low-discrepancy sampling
for financial derivatives [@paskovtraub1995]. Longstaff and Schwartz show why
simulation is valuable for early-exercise, path-dependent, and multifactor
settings [@longstaffschwartz2001]. Zhang's arithmetic-Asian analysis provides
a concrete example in which a simple coordinate transformation does not
produce a Black--Scholes-type closed form [@zhang2003].

These sources support the following negative result: if the phase map is
inverted sample by sample before evaluating the same payoff, Monte Carlo and
quasi-Monte Carlo estimators are exactly unchanged. Any benefit must arise
from an additional step such as a new discretization, importance sampling,
control variate, effective-dimension reordering, or PDE basis.

## 10. Complex differentiation and complex methods in finance

Brandwood's complex gradient formalism is an established form of Wirtinger
calculus for nonholomorphic real objectives [@brandwood1983]. Squire and Trapp
show that complex-step differentiation avoids subtractive cancellation when a
real function has a suitable analytic extension [@squiretrapp1998].

Heston's stochastic-volatility formula uses characteristic functions
[@heston1993], and Carr and Madan use the fast Fourier transform for option
valuation [@carrmadan1999]. These finance references demonstrate real value
from complex analysis, but for reasons different from the one-phase state
coordinate.

The paper will therefore state:

- complex notation can organize tangent/normal directions and two real
  derivatives;
- multiplication by \(i\) rotates a tangent vector by \(90^\circ\);
- that rotation does not create independent stochastic noise;
- a nonholomorphic payoff or value function does not acquire a new complex
  derivative merely because its state is written as \(re^{i\theta}\); and
- complex-step differentiation requires analytic extension and is not
  automatically licensed by the coordinate map.

## 11. Claim-to-source matrix

| Manuscript claim | Authority | Use |
|:--|:--|:--|
| Brownian/normal diffusion entered finance through Bachelier | @bachelier1900 | Historical positioning |
| Random walks converge to Brownian motion under invariance scaling | @donsker1951 | Discrete-to-continuous bridge |
| Smooth diffusion transforms require Itô's correction | @ito1944; @ito1951 | Phase SDE |
| Equivalent measure changes alter drift, not diffusion direction | @girsanov1960 | Pricing-measure invariance |
| Conditional expectations solve compatible parabolic problems | @kac1949 | Pricing PDE |
| No-arbitrage/martingale pricing needs a financial market framework | @blackscholes1973; @merton1973; @harrisonpliska1981 | Pricing section |
| Scalar diffusion transformations are established | @lamperti1964; @doss1977; @sussmann1977; @zvonkin1974 | Novelty boundary |
| Arctangent-transformed Brownian motion is an established exact SDE example | @sarkkasolin2019 | Novelty boundary |
| Endpoint terminology comes from one-dimensional diffusion theory | @feller1954 | Boundary section |
| Driver count need not equal terminal support dimension | @stroockvaradhan1972; @hormander1967 | Dimension discussion |
| Projecting Gaussian vectors onto angles is established | @pukkilarao1988; @wanggelfand2013 | Angular-law comparison |
| Planar Brownian winding requires genuinely planar noise | @spitzer1958; @pitmanyor1986 | Negative control |
| Stereographic Brownian compactification is established | @carne1985 | Compactification boundary |
| Stochastic exponential/logarithm theory is established | @doleansdade1970; @larssonruf2019; @cernyruf2022; @cernyruf2023 | Spiral comparison |
| Normal/Bachelier pricing remains academically and practically relevant | @schachermayerteichmann2008; @choi2022; @cme2020 | Finance motivation |
| Arctangent compactification already appears in financial PDE work | @duffiekan1996; @inthoutsnoeijer2021 | Novelty boundary |
| Mappings on unbounded domains have problem-dependent benefits | @groschorszag1977; @boyd1987; @contvoltchkova2005 | Numerical caution |
| High-dimensional pricing needs methods beyond a one-coordinate relabeling | @reisingerwittum2007; @longstaffschwartz2001 | Limitation |
| MC and QMC are established financial valuation methods | @boyle1977; @paskovtraub1995 | Simulation baseline |
| Path dependence can resist elementary closed forms | @zhang2003 | Limitation |
| Geometric/symmetry-preserving SDE schemes are established | @malhamwiese2008; @devecchi2019 | Numerical context |
| Wirtinger and complex-step methods have specific hypotheses | @brandwood1983; @squiretrapp1998 | Complex-calculus limits |
| Complex characteristic/Fourier methods add value through transform analysis | @heston1993; @carrmadan1999 | Distinct complex-finance precedent |

## 12. Novelty-boundary matrix

| Topic | Prior status | Permitted claim |
|:--|:--|:--|
| \(X\mapsto\arctan(X/c)\) | Established transformation and exact SDE example | Canonical chart used in a new classification/synthesis |
| Euler identity \(re^{i\theta}\) | Elementary complex analysis | Coordinate language only |
| Projected angular Gaussian law | Established directional statistics | The line-supported specialization is derived explicitly |
| Arctangent PDE compactification | Established in computational finance | Exact pricing conjugacy and controlled benchmark |
| Stochastic exponential/complex GBM | Established | Multiplicative rigidity comparator |
| One-driver covariance rank one | Standard linear algebra/stochastic calculus | Applied explicitly to distinguish phase from new noise |
| Affine iff-classification | No directly matching result found in the searched literature | Central theorem, with full proof |
| Secant-line/additive versus spiral/multiplicative rigidity | No unified treatment found in the searched literature | Structural synthesis |
| Pricing/Greek conjugacy for the classified chart | Chain-rule consequence, not a new pricing model | Rigorous application and verification |
| Automatic variance reduction | False for exact round trip | Negative theorem/empirical identity |
| Automatic PDE acceleration | Unsupported | Report only measured, qualified results |
| New holomorphic calculus | False in general | Explain Wirtinger repackaging and analytic-extension requirements |

## 13. Claims deliberately excluded

The manuscript will not state or imply any of the following:

1. \(dt=(dW_t)^2\) as ordinary algebra.
2. \(i^2=-1\) causes Brownian quadratic variation.
3. One phase converts a one-driver process into planar Brownian motion.
4. A single angle can losslessly encode arbitrary two-factor or
   stochastic-volatility models.
5. An invertible coordinate change reduces exact Monte Carlo variance.
6. Compactification is always more accurate or better conditioned.
7. Euler notation creates holomorphic derivatives for nonanalytic payoffs.
8. The arctangent transform or Bachelier formula is newly discovered.
9. The auxiliary complex coordinate is itself a traded asset price.
10. Numerical agreement is proof of the classification theorem.

## 14. Final source-verification status

The publication audit was completed before final rendering:

- every bibliography key cited by `index.qmd` resolves, all 52 bibliography
  entries are cited, and no unused entry remains;
- historical and priority claims are cited in the paragraph in which they
  appear;
- Duffie and Kan's arctangent map was checked at p. 396 of the original
  article;
- Särkkä and Solin are used only for the book-level exact transformed-diffusion
  example, without an unsupported page-specific claim;
- modern normal-model claims use the peer-reviewed Choi et al. article and the
  original CME advisory rather than news summaries;
- primary mathematical results are distinguished from modern expository
  notation; and
- Pandoc citeproc and the complete Quarto PDF/HTML render resolve without
  missing citations or cross-references.
