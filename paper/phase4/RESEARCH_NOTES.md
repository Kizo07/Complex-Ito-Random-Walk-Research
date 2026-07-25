# Phase 4 research and claim audit

Research checked on 2026-07-24. This file records the source trail used for
the Phase 4 manuscript; it is not a substitute for the manuscript's
derivations. Publisher pages, journal records, institutional repositories, and
the original papers were preferred over tertiary summaries.

## Question and research verdict

The paper asks whether a single native complex exponential can encode a
prescribed geometric Brownian modulus together with deterministic and
stochastic rotation, without defining a Cartesian pair first. The answer is
yes:

\[
\mathcal Z_t=\mathcal Z_0
\exp\!\left(
\left[\left(\mu-\frac12\sigma^2\right)+i\omega\right]t
+(\sigma+i\beta)W_t
\right).
\]

This is a parameterized member of the established family of complex scalar
linear Itô equations. Complex geometric Brownian motion, the exact exponential
solution, and stochastic exponentials are not new. The paper's focus is the
modulus-preserving four-parameter synthesis, its pathwise polar
interpretation, its rank-one one-driver covariance, its relation to Phase 3,
and the precise two-driver boundary.

## Bibliography audit

| Key | Verified bibliographic record | Type | Claim supported |
|---|---|---|---|
| `ito1951` | K. Itô, *Nagoya Mathematical Journal* 3, 55–65; DOI 10.1017/S0027763000012216 | Foundational primary paper | Itô's change-of-variables formula and the quadratic-variation drift correction. |
| `doleansdade1970` | C. Doléans-Dade, *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete* 16, 181–194 | Foundational primary paper | Historical source for the multiplicative semimartingale exponential. No DOI was added because none was verified. |
| `higham2001` | D. J. Higham, *SIAM Review* 43(3), 525–546; DOI 10.1137/S0036144500378302 | Primary exposition/research article | Exact solution of the scalar linear SDE and numerical simulation/convergence methodology. |
| `buckwar2006` | E. Buckwar, R. Horváth-Bokor, R. Winkler, *BIT Numerical Mathematics* 46(2), 261–282; DOI 10.1007/s10543-006-0060-5 | Primary research article | On p. 262, a scalar linear SDE with complex coefficients and one real Brownian driver is explicitly said to have “the complex geometric Brownian motion as exact solution.” |
| `perret2010` | C. Perret, ETH Zürich dissertation no. 18868; DOI 10.3929/ethz-a-006026507 | Primary thesis | Complex linear SDEs, their exact exponential solution, moments, and numerical stability. |
| `larssonruf2019` | M. Larsson, J. Ruf, *Journal of Mathematical Analysis and Applications* 476(1), 2–12; DOI 10.1016/j.jmaa.2018.11.040 | Peer-reviewed survey | Stochastic exponentials and stochastic logarithms on stochastic intervals. |
| `cernyruf2022` | A. Černý, J. Ruf, *Electronic Journal of Probability* 27, article 3, 1–32; DOI 10.1214/21-EJP729 | Primary research article | Semimartingale representations that include complex-valued transformations. |
| `cernyruf2023` | A. Černý, J. Ruf, *Stochastic Processes and their Applications* 161, 572–602; DOI 10.1016/j.spa.2023.04.010 | Primary research article | Multiplicative compensators and complex-valued semimartingale calculus. |
| `spitzer1958` | F. Spitzer, *Transactions of the AMS* 87(1), 187–197; DOI 10.1090/S0002-9947-1958-0104296-5 | Primary research article | Classical planar Brownian radial and winding behavior; used to distinguish the paper's one-driver process from planar Brownian motion. |
| `pitmanyor1986` | J. Pitman, M. Yor, *The Annals of Probability* 14(3), 733–779; DOI 10.1214/aop/1176992436 | Primary research article | Planar Brownian asymptotic winding laws and time-change geometry; a distinction source, not a derivation source for this model. |
| `mora2015` | C. M. Mora et al., *SIAM Journal on Numerical Analysis* 53(4), 1613–1641; DOI 10.1137/140984488 | Primary research article | Direction-and-norm numerical decompositions for multiplicative-noise SDEs; contextual comparison. |
| `abdulle2013` | A. Abdulle, G. Vilmart, K. C. Zygalakis, *BIT Numerical Mathematics* 53(4), 827–840; DOI 10.1007/s10543-013-0430-8 | Primary research article | Complex scalar linear equations as numerical stability test equations. |
| `mortersperes2010` | P. Mörters, Y. Peres, *Brownian Motion*, Cambridge University Press; DOI 10.1017/CBO9780511750489 | Research monograph | Brownian scaling, quadratic variation, and planar Brownian reference background. |

The entries above are encoded in `references.bib`. Where a DOI exists, the
DOI is the canonical resolver. Perret's thesis uses the ETH Research
Collection record. Doléans-Dade's 1970 item is recorded using verified journal,
volume, and page metadata rather than inventing a DOI.

## Claim-to-source matrix

| Manuscript claim | Evidence | Status |
|---|---|---|
| Itô's formula contributes the second-order drift term. | @ito1951 | Established. |
| \(d[W,W]_t=dt\) is a quadratic-variation statement, not ordinary algebra. | @ito1951; @mortersperes2010 | Established; state carefully. |
| A scalar linear multiplicative SDE has an exact exponential solution. | @higham2001; @perret2010 | Established. |
| The scalar coefficients and state may be complex while the Brownian driver remains real. | @buckwar2006; @perret2010 | Established. |
| “Complex geometric Brownian motion” is existing terminology. | @buckwar2006 | Established; no novelty claim permitted. |
| The Doléans exponential is the canonical multiplicative semimartingale solution. | @doleansdade1970; @larssonruf2019 | Established. |
| Modern stochastic exponential/semimartingale frameworks include complex-valued processes. | @cernyruf2022; @cernyruf2023 | Established. |
| The proposed \(A\) is uniquely determined after \(B=\sigma+i\beta\) and the log-polar drift/diffusion targets are fixed. | Direct coefficient matching in the present paper. | Phase 4 derivation. |
| The modulus is exactly a prescribed real GBM. | Direct pathwise calculation plus Monte Carlo diagnostics. | Phase 4 synthesis and verification. |
| The unwrapped phase is \(\Theta_0+\omega t+\beta W_t\). | Direct pathwise calculation. | Phase 4 synthesis. |
| One real driver forces rank at most one in log-polar covariance. | Outer-product covariance calculation. | Phase 4 derivation, consistent with Phase 3. |
| Independent radial and angular diffusion requires at least two drivers. | Covariance rank argument and two-driver comparator. | Phase 4 boundary result. |
| The model is not planar Brownian motion. | Rank and path-law comparison; @spitzer1958; @pitmanyor1986 | Explicit distinction. |
| Phase 3 is the subfamily \(\beta=\gamma\sigma\), \(\omega=\gamma(\mu-\sigma^2/2)\). | Direct coefficient comparison. | Phase 4 bridge result. |

## Novelty boundary

| Statement | Paper position |
|---|---|
| Complex scalar linear SDEs exist. | Prior theory, not new. |
| Complex GBM terminology exists. | Prior terminology, not new. |
| Stochastic exponentials and logarithms exist. | Prior theory, not new. |
| The displayed four-parameter family is an existence theorem for complex GBM. | Not claimed. |
| A modulus-preserving \((\mu,\sigma,\omega,\beta)\) reparameterization makes radial growth and rotational dynamics explicit. | Central Phase 4 synthesis. |
| The SDE drift correction \(A=\mu-\beta^2/2+i(\omega+\sigma\beta)\) follows uniquely from the chosen log-polar targets. | Central Phase 4 derivation. |
| The one-driver covariance is rank one and differs from the two-driver comparator. | Central geometric limitation. |
| The process is planar Brownian motion. | Rejected. |
| \(dW_t^2=dt\) and \(i^2=-1\) are the same kind of equality. | Rejected. |

## Terminology controls

- **Native complex formula** means that the defining state equation uses
  \(\mathcal Z_0\), \(W_t\), and complex coefficients directly. It does not
  mean invariance under arbitrary coordinate changes.
- **Unwrapped phase** means the continuous lift
  \(\Theta_t=\Theta_0+\omega t+\beta W_t\). It is not silently identified with
  the principal argument.
- **Complex quadratic variation** uses the bilinear bracket
  \(d[\mathcal Z,\mathcal Z]_t\); the energy-like bracket
  \(d[\mathcal Z,\overline{\mathcal Z}]_t\) is Hermitian and different.
- **One-driver** means a single real Brownian motion. The resulting real and
  imaginary components are generally correlated and do not form standard
  planar Brownian motion.
- **Rotation** is generated by the imaginary part of the complex log
  increment. It does not turn the Itô table into complex-number algebra.

## Excluded or weakened claims

1. No claim of inventing complex GBM, stochastic exponentials, or an exact
   solution for scalar linear SDEs.
2. No claim that the four-parameter parameterization has been proved absent
   from all prior literature. It is presented as the paper's organizing
   synthesis.
3. No use of the slogan \(dW^2=dt\) without identifying quadratic variation
   or finite-mesh convergence.
4. No claim that one source of randomness fills two independent spatial
   directions.
5. No use of planar Brownian winding laws as if they were laws of the proposed
   process.
6. No identification of a continuous phase lift with a globally single-valued
   complex logarithm.

## Research-driven manuscript structure

The paper follows the exact-linear-SDE pedagogy of @higham2001: begin with the
modeling question, derive the exact solution before introducing a numerical
method, separate pathwise identities from distributional results, and use
reproducible simulations as diagnostics rather than proof. Historical and
theoretical attribution comes before the Phase 4 parameterization. The
planar-winding references are isolated in a comparison section so they cannot
be mistaken for sources of the model.
