# Research record: exact bounded correlation (Phase 6)

**Audit date:** 2026-07-27

**Scope:** stochastic correlation models, derivative pricing, first-passage
problems, Feynman–Kac methods, occupation-time laws

**Purpose:** preserve the source audit, novelty boundary, and claims
deliberately excluded from the manuscript

## 1. Search and verification method

The audit proceeded from the six milestones' dependency list: for each
external claim (what competitors have, what is unsolved), locate the original
source; verify against full text where accessible; mark snippet-level items
provisional. Verified status per source is recorded in
`PHASE_6_LITERATURE_REVIEW.md` §5a at the repository root. Key outcomes:

- **Teng–Ehrhardt–Günther (2016)** verified **full-text** (open access).
  Their closed form is the *stationary* density of the tanh-transformed
  modified OU; the finite-time transition density is not closed form. They
  explicitly considered and rejected the arctan-family map
  $\rho=\frac{2}{\pi}\arctan(\frac{\pi}{2}x)$ ("rather complicate"; tail
  estimation critique). The manuscript cites and answers this (§9).
- **Higgins (2014)** verified as **spot/volatility** correlation
  (arXiv:1404.4028), not asset–asset; used as evidence that barrier/touch
  structures under stochastic correlation are approximation territory.
- **Majumdar (2024)** verified at abstract level (circle/von Mises
  correlation; no closed-form transition density; approximate likelihood).
- **van Emmerich (2006)** verified **second-hand** through Teng et al.
  (2016) §2.3, which derives the van Emmerich SDE as a special tanh case and
  quotes its boundary condition. The original Wuppertal preprint was not
  obtained; no manuscript claim depends on details beyond what Teng et al.
  quote.
- **OU first-passage** (Ricciardi–Sato 1988; Alili–Patie–Pedersen 2005):
  classical series/special-function representations; treated as established
  that no elementary closed form exists.
- A PhD-thesis construction using the bijection
  $b(x)=x/\sqrt{1-x^{2}}=\tan(\arcsin x)$ with an OU driver was identified
  as the closest neighbor to our conjugate map; full text not obtained.
  It is a simulation/calibration construction with no exact-kernel or
  barrier-pricing content claimed; the manuscript's contributions (exact
  first-passage, derivative prices, clock reduction, resolvent law,
  classification) are orthogonal to it.

## 2. Novelty-boundary matrix

| Topic | Prior status | Permitted claim |
|:--|:--|:--|
| Bounded correlation via transform of Gaussian factor | Established (van Emmerich 2006; Teng et al. 2016) | Not claimed |
| $\rho=\sin\theta$ of the one-phase Euler chart | Companion paper (chart); closest neighbor $x/\sqrt{1-x^2}$ bijection (thesis, no kernels/pricing) | Financial reading + all exact content below |
| Exact finite-time transition density of bounded correlation | Competitors: stationary-only, spectral, or approximate | Claimed (closed form, single expression) |
| Reflection-principle first-passage laws for correlation | Not found in audited literature | Claimed (Thm. first-passage) |
| Closed-form correlation derivative prices (digital, touches, accrual) | Approximations only (Higgins 2014, spot-vol context) | Claimed; pay-at-hit form is new |
| DDS variance-clock reduction for spread/basket barriers | DDS theorem classical; this application with sign theorem not found | Claimed |
| Deterministic full clock law (FK + Fourier on bounded support) | FK standard; bounded-support Fourier assembly not found in correlation literature | Claimed as method |
| Corridor occupation pricing with atom separation | Occupation laws classical (arcsine); corridor pricing via atom-separated resolvent not found | Claimed as method |
| Stationarity–tractability classification (BM vs OU) | Trade-off folklore in scattered remarks | Claimed as unified theorem (Thm. classification) |
| Arctan-family correlation maps | Considered and rejected by Teng et al. (2016) | Rejection cited and answered honestly (polynomial tail cost accepted) |

## 3. Claims deliberately excluded

The manuscript does not state or imply:

1. A new correlation model in the empirical/calibration sense.
2. That the Brownian-driver coordinate is stationary (it is not; the OU
   variant and the classification address this).
3. That the boundaries $\pm1$ are approached as fast as in
   exponential-transform models (approach is polynomial — accepted cost).
4. Leverage/correlation-of-correlation-with-returns (excluded by the
   independence assumption $W\perp(W_1,W_2)$; stated).
5. Automatic Monte Carlo variance reduction from coordinate maps (the
   reduction's benefit is effective dimension, demonstrated with standard
   errors, not asserted as universal acceleration).
6. That the Gamma moment match is exact (it is a screening tool; its error
   is measured against the resolvent price per parameter set).
7. Statistical agreement where there is only bias-explained consistency
   (corridor prices: the $\sim7\times10^{-3}$ gap is reported with both
   identified biases, not as "~2 SE").
8. That OU first passage has a closed form (it does not; the FK resolvent
   is the deterministic replacement).
9. Estimation/calibration results (deferred; exact likelihoods noted as
   available).
10. That the correlation risk premium is identified (prices are conditional
    on a chosen constant premium; sensitivity is a closed-form comparative
    static).

## 4. Claim-to-evidence matrix

| Manuscript claim | Evidence |
|:--|:--|
| Transition density (Thm. density) | Derivation; unit tests (normalization to $10^{-9}$); notebook fig. kernels |
| First-passage laws (Thm. first-passage) | Reflection principle; unit tests (CDF=density integral, limits); notebook fig. kernels |
| Measure-change invariance (Prp. measurechange) | Girsanov; construction |
| Four derivative prices (§4) | Derivations; 9 pricing unit tests (limits, orderings, anchors); notebook table |
| DDS reduction (Thm. clock, Cor. scalar, Cor. sign) | DDS theorem; full 3-driver MC vs scalar reduction ($z=-1.16,+1.19$); fig. mispricing |
| Clock moments | Triangle-aware quadrature; convergence to machine precision; MC cross-check |
| Full clock law (Thm. fk) | FK; Fourier; unit tests (13); price vs MC ($|z|<1$ all vols) |
| Corridor atom separation (Prp. atom) | Absorbing PDE vs MC; mass = 1 − atom to 6 decimals |
| Arcsine anchor (Thm. arcsine) | Tail probabilities to $5\times10^{-4}$; fig. arcsine |
| Classification (Thm. classification) | Row-by-row: density normalization, digital=density integral, OU FK tests, $\kappa\to0$ anchors (2×10⁻⁷, 6×10⁻⁸) |
| OU price | FK vs exact OU simulation ($z=+0.92$; notebook $z=-0.14$ at paper config) |

## 5. Verification status

- 77/77 unit tests pass across five test modules.
- Six executed milestone notebooks plus the paper notebook (seed 20260727,
  all runtimes recorded).
- Every bibliography key cited by `index.qmd` resolves; each entry is used.
- Manuscript figure/table assets regenerate deterministically from the
  paper notebook.
- External-agent claims from the initial audit are superseded by the
  verification record above (§1).
