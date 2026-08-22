# Phase 14 source audit and claim boundary

**Audit date:** 2026-08-22

**Paper:** *Hidden Exactness in Bounded-Factor Stochastic Models*

**Author:** Kanav Mehta

## Audit method

The bibliography was assembled in three independent searches:

1. Bachelier implied volatility, Gaussian mixtures, stochastic correlation,
   and leverage;
2. hyperspherical correlation matrices, determinant laws, and compact
   Brownian dynamics; and
3. nonautonomous evolution, Hörmander smoothing, and spectrally negative
   Lévy fluctuation theory.

Primary papers or authoritative monographs were preferred. Full text was
checked for the closest claims whenever accessible; otherwise the publisher
abstract and canonical metadata were checked. Search snippets were used only
to locate sources. The manuscript cites every bibliography entry and makes no
priority claim for a classical ingredient.

## 1. Bachelier and normal implied volatility

| Key | Verified role |
|---|---|
| bachelier1900 | Original arithmetic-Brownian option-pricing framework. |
| choikimkwak2009 | Numerical inversion and uniqueness of implied normal volatility. |
| jaeckel2017 | Stable analytical inversion of the Bachelier formula. |
| choikwakteewang2022 | Modern Bachelier conventions and comparison with Black pricing. |
| poitras1998 | Arithmetic-Brownian spread and exchange option pricing. |
| carmonadurrleman2003 | Standard spread-pricing theory and correlation dependence. |

The Bachelier formula, normal implied volatility, symmetry under centered
laws, and numerical inversion are established. Phase 14 does not claim them.

## 2. Variance mixtures and ATM curvature

| Key | Verified role |
|---|---|
| andrewsmallows1974 | Classical normal scale-mixture characterization. |
| barndorffnielsenkentsorensen1982 | Normal variance-mean mixtures and the centered subclass. |
| clark1973 | Brownian motion under a random clock in finance. |
| hullwhite1987 | Independent stochastic-volatility pricing as integrated-variance mixing. |
| renaulttouzi1996 | Symmetric implied smiles and ATM behavior under independent stochastic volatility. |
| alosnualartpravosud2024 | Bachelier stochastic-volatility ATM level and skew. |
| alosgarcialorite2025 | Exact fixed-maturity Bachelier ATM curvature decomposition. |
| alosbures2026 | ATM Bachelier volatility as volatility-swap strike and negative-half-moment expansions. |

The identities

\[
I(0)=E[S],\qquad
I''(0)=E[S^{-1}]-E[S]^{-1}
\]

are short exact consequences of the centered-mixture price and are closely
foreshadowed, and partly contained in more general form, in the recent
Bachelier-curvature literature. They are presented as a compact specialization,
not a world-priority theorem.

The defensible project contribution is narrower:

\[
\rho_{\mathrm{imp}}(0)
=\frac{E[A_T]}{T}
-\frac{\operatorname{Var}(\sqrt{V_T})}{\alpha T},
\]

together with the spread/basket sign corollary for the specified stochastic-
correlation clock. No checked source stated that clock-specific correction.
It remains a direct corollary of the known ATM volatility-swap identity and is
described accordingly.

## 3. Stochastic correlation and multi-asset transforms

| Key | Verified role |
|---|---|
| skintzirefenes2005 | Option-implied correlation measurement. |
| lindersschoutens2014 | Model dependence and robustness of implied correlation. |
| driessenmaenhoutvilkov2009 | Economic importance of correlation risk in options. |
| dafonsecagrassellitebaldi2007 | Stochastic covariance with analytical transforms and leverage. |
| ma2009 | Mean-reverting stochastic correlation for multi-asset pricing. |
| escobargotzsecozagst2009 | Spread options under stochastic correlation. |
| gourierouxsufana2010 | Wishart stochastic covariance and conditional Laplace transforms. |
| escobarkrausezagst2016 | Basket-pricing dimension reduction under stochastic covariance. |

Stochastic correlation, stochastic covariance, and transform-based multi-asset
pricing are established. The paper does not call the bounded factor a new
correlation model merely because it has exact coordinates.

## 4. Brownian leverage and conditional Gaussianity

| Key | Verified role |
|---|---|
| romanotouzi1997 | Correlated asset/volatility noise in a general stochastic-volatility setting. |
| willard1997 | Conditional mixing for path-independent claims in multifactor models. |
| alos2006 | Correlated extension of Hull–White-type conditional decomposition. |
| heston1993 | Leverage-induced skew with characteristic-function tractability. |
| scott1997 | Fourier inversion with correlated return/factor shocks. |
| duffiepansingleton2000 | General transform analysis for dependent Markov states. |
| daslangrene2022 | Modern correlated mixing representation with random mean and residual variance. |
| rolloos2022 | Barrier formulas under correlated stochastic volatility in a different structure. |

Leverage preserving conditional mixing and Fourier reduction is not a new
general principle. The Phase 14 results worth retaining are the exact PSD
region for the particular primitive-driver construction, the explicit
bounded-factor primitive, the specialized complex-potential representation,
the model-specific third-moment coefficient, and the precise failure of the
terminal scalar-clock reflection formula.

The manuscript must not say that leverage generally destroys all reduced-
dimensional barrier formulas.

## 5. Nonautonomous Feynman–Kac and evolution families

| Key | Verified role |
|---|---|
| kac1949 | Additive Wiener functionals and PDE correspondence. |
| karatzasshreve1991 | Time-dependent Feynman–Kac theorem with terminal data. |
| kato1953 | Two-parameter Banach-space evolution operators. |
| pazy1983 | Semigroup/evolution-equation foundations and Duhamel formulas. |
| acquistapaceterreni1987 | Nonautonomous parabolic evolution and regularity. |
| lunardi1995 | Analytic nonautonomous parabolic equations. |
| magnus1954 | Operator exponentials and commutator corrections. |
| blanescasasoteoros2009 | Time ordering and the Magnus expansion. |

Two-time evolution families, right-versus-left generator ordering,
time-ordered exponentials, and commutator corrections are classical. The
paper presents an internal correction and a tailored Gaussian diagnostic
example. It does not claim that the operator-ordering identity is new.

The exact identity is valid on a common invariant core under the usual
well-posedness and strong-differentiability hypotheses:

\[
[Q_{0,t},\mathcal A_t]
=\int_0^tQ_{0,r}[\mathcal A_r,\mathcal A_t]Q_{r,t}\,dr.
\]

Pairwise commutation is sufficient, not necessary.

## 6. Hyperspherical and random correlation matrices

| Key | Verified role |
|---|---|
| pinheirobates1996 | Unconstrained hyperspherical covariance parameterization. |
| rebonatojackel2000 | Finance-specific valid-correlation construction. |
| rapisardabrigomercurio2007 | Gram/unit-vector and Euler-angle interpretation. |
| joe2006 | Partial-correlation determinant/Jacobian and random correlation generation. |
| lewandowskikurowickajoe2009 | Vine/onion construction and LKJ family. |
| pourahmadiwang2015 | Hyperspherical Jacobian and nonuniform angle laws for determinant-power matrices. |
| forresterzhang2020 | Equivalence of hyperspherical and partial-correlation charts. |
| eastmanetal2016 | Elliptope volume from spherical coordinates. |
| muirhead1982 | Multivariate Jacobian and sample-correlation background. |
| holmes1991 | Classical random correlation matrices. |
| bendelmickey1978 | Population correlation matrices for simulation. |
| barnardmccullochmeng2000 | Correlation-matrix prior modeling. |
| archakovhansenluo2024 | Modern comparison of random correlation generators. |
| buccherietal2021 | Time-varying hyperspherical correlation parameters in dynamics. |

The triangular map, PSD-by-construction property, determinant factorization,
Jacobian, random-angle ideas, and determinant-power matrix distributions are
classical. The stationary law induced by flat independent angles is not
uniform on the elliptope, is not LKJ for dimensions at least three, is
boundary-singular with respect to off-diagonal Lebesgue coordinates, and
depends on variable ordering.

The paper uses “lower-triangular hyperspherical Gram factor,” not “Cholesky
factor,” outside the canonical positive-diagonal chart.

The possibly distinctive package is the specified dynamic construction:
finite-time Fourier determinant moments, the compact stationary pushforward
law, and the product interval-exit survival law. These are presented as a new
analysis of the model, not new determinant or compact-group machinery.

## 7. Compact Brownian dynamics and product-Beta asymptotics

| Key | Verified role |
|---|---|
| applebaum2014 | Probability and Brownian semigroups on compact Lie groups. |
| liao2004 | Convergence of Lévy processes on compact groups to Haar measure. |
| maher2012 | Wrapped Brownian motion and heat kernels. |
| borodinsalminen2002 | Killed Brownian interval-exit formulas. |
| springerthompson1970 | Product distributions and Mellin methods. |
| tanggupta1984 | Products of independent Beta variables. |
| johnsonkotzbalakrishnan1995 | Beta log moments and polygamma identities. |
| rouault2007 | Random determinant asymptotics in Gram/Jacobi ensembles. |
| haneanane2018 | Correlation-matrix determinant asymptotics. |

Haar measure refers to the coordinate torus only. The elliptope is not a
group. Stationarity of the pushforward does not automatically prove that the
matrix image is Markov at singular fibers.

The log-determinant law quantifies exponential determinant decay. It does not
by itself establish a smallest-eigenvalue limit or prove that this ensemble is
more ill-conditioned than standard random-correlation baselines.

## 8. Hörmander and integrated diffusions

| Key | Verified role |
|---|---|
| kolmogoroff1934 | Classical degenerate integrated-diffusion prototype. |
| hormander1967 | Bracket-condition hypoellipticity. |
| malliavin1978 | Probabilistic hypoellipticity via stochastic variations. |
| kusuokastroock1985 | Smooth-density consequences of Hörmander conditions. |
| norris1986 | Simplified Malliavin covariance arguments. |
| nualart2006 | Authoritative regularity-of-laws treatment. |
| hairer2011 | Stratonovich bracket convention and smooth-density theorem. |
| delaruemenozzi2010 | Density estimates for noise propagated through chains. |

For the endpoint-clock pair, use the Stratonovich fields

\[
V_1=\nu\partial_x,\qquad
V_0=\mu\partial_x+f_c(x)\partial_a.
\]

Because \(V_1\) is constant, Itô and Stratonovich drifts coincide, and
\([V_1,V_0]=\nu f_c'(x)\partial_a\). The bracket spans at each finite state.
It is not uniform because \(f_c'(x)\to0\) at infinity. The paper claims a
smooth density under bounded-derivative and nonexplosion hypotheses, not
global Gaussian lower bounds or strict positivity.

## 9. Spectrally negative Lévy fluctuation theory

| Key | Verified role |
|---|---|
| bertoin1996 | General Lévy fluctuation theory. |
| doney2007 | Wiener–Hopf and one-sided passage. |
| kyprianou2014 | Canonical scale functions and exit identities. |
| kuznetsovkyprianourivero2013 | Exact normalization and one-/two-sided exit theorems. |
| suprun1976 | Early resolvent/scale-function treatment. |
| avramkyprianoupistorius2004 | Exit and reflected-exit transforms. |
| alilikyprianou2005 | Passage, creeping, and overshoot distinctions. |
| chankyprianousavov2011 | Smoothness conditions for scale functions. |
| landriaultrenaudzhou2011 | Occupation times of a half-line. |
| loeffenrenaudzhou2014 | Joint interval occupation and first passage. |
| lipalmowski2018 | State-dependent Omega killing and generalized scale functions. |
| itomckean1996 | One-dimensional diffusion scale and hitting-time context. |

The scale-function formulas and monotone barrier transport are classical.
Passage times use the standard strict conventions

\[
\tau_b^+=\inf\{t>0:X_t>b\},\qquad
\tau_a^-=\inf\{t>0:X_t<a\}.
\]

The scale function is zero on the negative half-line and normalized by

\[
\int_0^\infty e^{-\theta x}W^{(\delta)}(x)\,dx
=\frac{1}{\psi(\theta)-\delta},
\qquad \theta>\Phi(\delta).
\]

The paper’s role is to correct the overly broad statement that all exact
barriers die under jumps. It does not claim scale-function theory. The sharper
open problem concerns analytic continuation and usable inversion for the
sign-changing complex killing potential
\(\omega_\xi(x)=\delta-i\xi f_c(x)\), in light of existing Omega-scale work.

## 10. Final novelty ledger

### Retain as project-specific results

1. The exact clock-specific ATM Jensen wedge and its spread/basket sign
   corollary.
2. The explicit bounded-factor Itô primitive and resulting complex-potential
   transform representation.
3. The model-specific short-time third-moment coefficient.
4. The finite-time determinant-moment, stationary pushforward, and
   first-boundary product package for Brownian triangular angles.
5. The correction of the written scale orbit and the explicit Gaussian
   operator-order diagnostic.

### Present as classical specializations or corrections

1. Centered-mixture ATM level, evenness, and curvature differentiation.
2. Conditional mixing and Fourier reduction under leverage.
3. Hyperspherical Gram parameterization and determinant factorization.
4. Brownian convergence on a torus and product-Beta calculations.
5. Nonautonomous evolution-family ordering and commutator calculus.
6. Hörmander smoothing of integrated diffusions.
7. Spectrally negative scale-function exit identities.

### Exclude

- claims that the stationary flat-angle law is uniform or LKJ;
- claims that the observable matrix is automatically Markov;
- a global wing-curvature theorem derived only from the ATM calculation;
- claims that leverage prevents all reduced barrier formulas;
- claims of uniform Hörmander bounds;
- claims that state-dependent killing or occupation scale functions are open
  in general; and
- world-priority language unsupported by a direct literature match.
