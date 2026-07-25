# Review: *Native Complex Geometric Brownian Motion*

**Subtitle:** Itô correction, stochastic rotation, and noise-dimension geometry
**Source:** `phase4-native-complex-geometric-brownian-motion.pdf`, dated July 24, 2026
**Review date:** July 24, 2026

---

## Verdict up front

The mathematics is **correct** — every derivation and every reported number that could be
reconstructed independently checks out, and no errors were found in the analysis. The
computational work is **genuinely well executed** and internally consistent to a degree that
indicates real simulation, not decoration.

But the paper contains **no new mathematical result**. The central object is the general solution
of the scalar complex linear SDE, known since the 1950s, presented in a relabeled coordinate
system. The paper is admirably honest about this in places ("We do not claim to have invented
complex GBM") while its framing elsewhere — "four-parameter synthesis," "rank-one theorem,"
"noise-dimension boundary" — implies more than is delivered.

There is also one structural observation the paper misses that substantially deflates its own
central claim. See §4.

---

## 1. Mathematical verification

Each derivation was checked independently.

| Claim | Status |
|---|---|
| $R_t = \lvert\mathcal{Z}_t\rvert$ is exactly GBM$(\mu,\sigma)$ | ✅ Correct, pathwise |
| $\Theta_t = \Theta_0 + \omega t + \beta W_t$ | ✅ Correct |
| $A = \kappa + B^2/2 = \mu - \beta^2/2 + i(\omega + \sigma\beta)$ | ✅ Correct |
| Spurious factor $e^{\beta^2 t/2}$ when $-\beta^2/2$ omitted | ✅ Correct |
| $\mathcal{E}(Y)_t$ reconciliation; $\log_{\text{cont}}$ vs. $\mathcal{L}$ differ by $B^2t/2$ | ✅ Correct |
| Exact one-step transition (Eq. 12) | ✅ Correct |
| Singular log-polar Gaussian law + support line (Eq. 14) | ✅ Correct |
| Radial moments (Eq. 15) | ✅ Correct |
| Complex integer moments (Eq. 16) | ✅ Correct |
| Mixed moments (Eq. 17) | ✅ Correct |
| $g(z)g(z)^\mathsf{T}$ has rank $\le 1$ | ✅ Correct (rank exactly 1 for $z \ne 0$, $B \ne 0$) |
| $\Sigma_1$ eigenvalues $\{\sigma^2+\beta^2,\, 0\}$ | ✅ Correct |
| $d[\mathcal{Z},\mathcal{Z}] = B^2\mathcal{Z}^2 dt$ vs. $d[\mathcal{Z},\bar{\mathcal{Z}}] = \lvert B\rvert^2\lvert\mathcal{Z}\rvert^2 dt$ | ✅ Correct |
| Phase 3 restrictions $\beta = \gamma\sigma$, $\omega = \gamma(\mu - \sigma^2/2)$ | ✅ Correct, and necessary + sufficient as claimed |
| Two-driver drift loses the $\sigma\beta$ cross term (Eq. 24) | ✅ Correct |

The Appendix A derivation via $(d\Lambda)^2 = (dU)^2 - (dV)^2 + 2i\,dU\,dV$ is clean and is the
right way to make the "$i^2 = -1$ is not quadratic variation" point rigorous. That distinction, and
the $[\mathcal{Z},\mathcal{Z}]$ vs. $[\mathcal{Z},\bar{\mathcal{Z}}]$ distinction, are the paper's
best pedagogical content — both are real traps.

**Coefficient arithmetic (Table 2):**
$\kappa = 0.0918 + 0.9i$ ✅, $B^2 = -0.2461 + 0.546i$, $A = -0.03125 + 1.173i$ ✅,
$A - B^2/2 = \kappa$ ✅.

---

## 2. Numerical verification

The analytic targets were reconstructed and the Monte Carlo standard errors stress-tested — the
check that distinguishes real output from plausible-looking fabrication.

- $\mathbb{E}[R_T] = 1.25\,e^{0.27} =$ **1.637455** vs. reported 1.63746 ✅
- $\mathbb{E}[R_T^2] =$ **3.49348** vs. 3.49344 ✅
- $\mathbb{E}[\mathcal{Z}_T] =$ **$-0.61192 + 1.02384i$** vs. $-0.61191 + 1.02383i$ ✅
- $\mathbb{E}[\mathcal{Z}_T^2] =$ **$0.31460 - 0.93181i$** vs. $0.31462 - 0.93185i$ ✅
- Table 4 analytic means/variances (0.13770, 1.35000, 0.26460, 0.63375) all ✅

The standard-error consistency check is the strong one. From the reported residual 1.250 for
$\mathbb{E}[R_T]$ and $N = 600{,}000$, the implied sample sd is 0.899; the true sd is
$\sqrt{3.49344 - 1.63746^2} =$ **0.9012**. Same for $\mathbb{E}[R_T^2]$: implied 4.774 vs. true
4.792. Same for $\operatorname{Re}\mathcal{Z}_T$: implied 1.2394 vs. true 1.2369. These agree to
within sampling error of the variance estimate itself. The simulation is real.

Two further internal checks pass:

- The Table 5 empirical one-driver covariance satisfies
  $\hat\Sigma_{01}^2 = \hat\Sigma_{00}\hat\Sigma_{11}$ to five digits, as a rank-one construction
  must.
- The §11.2 eigenvalue ratio $5.54 \times 10^{-16}$ is exactly
  $3.33\times10^{-16} / 0.60139$ from Table 5.

The Euler–Maruyama slopes decrease monotonically toward 0.5 (0.657 → 0.567 → 0.531 → 0.508) with
fitted 0.5625 — the correct pre-asymptotic signature for multiplicative noise, matching Higham's
GBM experiment.

---

## 3. Issues found

### (a) Figure 6 appears to use the wrong $\beta$ — worth checking the code

With $\beta = 0.65$, $R_0 = 1.25$, $T = 1.5$, the spurious factor gives a terminal modulus of
$1.25\,e^{0.3169} =$ **1.72**. The plotted dashed curve terminates near **2.29**. That value is
reproduced exactly by $\beta = 0.90$ — which is the paper's $\omega$. This looks like an argument
swap in the stress-test plotting call.

Note that the Table 3 assertion ($4.44\times10^{-16}$) only exercises the *correct* branch, so a
wrong $\beta$ in the erroneous branch would pass silently.

*Caveat:* this reading is from a rasterized figure, so treat it as "check the call site," not a
certainty.

### (b) Undocumented parameters

- §13.6 doesn't state $T$ for the quadratic-variation experiment; Figure 17 implies $T = 1.0$ while
  everything else uses $T = 1.5$.
- §13.5 doesn't say what the EM error is measured *against* (presumably Eq. 4 on the shared path —
  it should say so).
- §13.3's numerical-rank threshold of $10^{-4}$ is absolute where it should be relative to the
  large eigenvalue.

### (c) The MC "validation" is largely circular

Since simulation uses the exact transition (Eq. 12), Tables 3, 4, and 6 verify that Gaussian
formulas match Gaussian sampling — they cannot detect a modeling error. Only two experiments have
real diagnostic power:

1. The Euler–Maruyama convergence test, which genuinely cross-validates Eq. 10 against Eq. 4 and
   would catch a wrong $-\beta^2/2$ or $\sigma\beta$.
2. The quadratic-variation test.

The paper half-concedes this but then presents Table 3 — essentially a floating-point roundoff
table — as though it were evidence of correctness.

---

## 4. The structural problem the paper misses

Solve Eq. 5 for the driver,
$W_t = \big[\log(R_t/R_0) - (\mu-\sigma^2/2)t\big]/\sigma$, and substitute back. For $\sigma \ne 0$:

$$
\mathcal{Z}_t \;=\; \mathcal{Z}_0 \cdot \left(\frac{R_t}{R_0}\right)^{1 + i\beta/\sigma}
\cdot \exp\!\Big( i\big[\omega - (\beta/\sigma)(\mu - \tfrac{1}{2}\sigma^2)\big]\,t \Big)
$$

Two consequences follow immediately.

### First: $\mathcal{Z}_t$ is a deterministic function of $(t, R_t)$ alone

§4 sets up Requirement 1 by rejecting "a post-processing map $\mathcal{Z}_t = f(S_t)$ of a
pre-existing scalar state." But the constructed process *is* exactly such a map. "Nativeness" is a
property of how the formula is written, not of the object. §3 hedges this ("operational language"),
which makes Requirement 1 vacuous as a mathematical constraint — it constrains notation, not the
process. The paper should either drop the requirement or state plainly that it is stylistic.

### Second, and more damaging: Phase 4 = Phase 3 × a deterministic rotation

Setting $\gamma = \beta/\sigma$ and $\delta = \omega - \gamma(\mu - \sigma^2/2)$, the formula above
is precisely $\mathcal{Z}_0 e^{(1+i\gamma)L_t} \cdot e^{i\delta t}$.

So the "independence of $\omega$ and $\beta$" that §12.1 and Figure 15 present as Phase 4's
contribution over Phase 3 is *entirely* a deterministic phase spin. For the paper's own parameters,
$\gamma = 1.548$, the Phase-3-implied $\omega$ would be 0.142, actual $\omega = 0.90$, so
$\delta = 0.758$ — a constant 1.137 rad rotation over $T = 1.5$. That is the whole of the
difference between the two curves in Figure 15's right panel.

The four-parameter family is, up to a deterministic rotation, the three-parameter Phase 3 family.
**The headline claim of the paper does not survive this.**

---

## 5. Novelty

Low, and the paper's own framing makes the case against itself.
$\mathcal{Z}_t = \mathcal{Z}_0\exp(\kappa t + BW_t)$ with $\kappa, B \in \mathbb{C}$ and $W$ real is
the general solution of $dX = \lambda X\,dt + \eta X\,dW$ for complex $\lambda, \eta$ — Itô 1951
plus algebra, and explicitly named "complex geometric Brownian motion" by the very reference the
paper cites (Buckwar et al. 2006, p. 262).

The stated contribution is a reparameterization
$(\lambda,\eta) \leftrightarrow (\mu,\sigma,\omega,\beta)$ via $\kappa = A - B^2/2$. That map is a
bijection; it is the complex version of "log-drift versus arithmetic drift," which every GBM
treatment already performs. Reparameterizations can be contributions when they make something
previously opaque transparent, or when they produce a new theorem in the new coordinates. Neither
happens here.

The "rank-one theorem" of §11 is the observation that $vv^\mathsf{T}$ has rank one. That one
Brownian driver yields a rank-one diffusion covariance, and that independent radial and angular
noise requires two drivers, are immediate and universally understood. Presenting them across §11,
§12, Figures 8, 9, 13, and 14 — five figures for one trivial fact — inflates apparent substance.

---

## 6. Usefulness

### To quant finance: essentially none, and the paper says so

§16.8 explicitly disclaims any pricing, calibration, or no-arbitrage content. Worse, the §4
derivation above shows the process carries no information beyond $R_t$. As a financial model, the
complex state is one-dimensional dressed as two. A modeler wanting genuine planar dynamics needs
the two-driver comparator of §12.2, which is also textbook. There is no filtration argument, no
measure change, no derivative on $\mathcal{Z}$, no calibration target for $\omega$ and $\beta$, and
no stated financial meaning for "phase." The GBM terminology in the title courts a quant audience
and then delivers nothing for it.

### To mathematics: negligible as research, moderate as exposition

The $[\mathcal{Z},\mathcal{Z}]$ vs. $[\mathcal{Z},\bar{\mathcal{Z}}]$ section and the "quadratic
variation is not $i^2 = -1$" argument are worth teaching. Figure 14's line-cloud vs. area-cloud
contrast is a good visual for a course. The reproducibility scaffolding — pinned versions, seeded
streams, evidence tables, executed-twice notebooks — is better practice than most published
applied-probability papers.

---

## 7. What would make this an actual contribution

Three concrete options, in ascending order of value.

### 1. Stability regions in the new coordinates

The paper cites Buckwar et al. and Abdulle et al., both of whom use the complex scalar test
equation for mean-square stability analysis, and then contributes nothing to that literature. Yet
its parameterization gives a one-line result: MS-stability requires
$2\operatorname{Re}(\lambda) + \lvert\eta\rvert^2 < 0$, which here collapses to

$$2\mu + \sigma^2 < 0,$$

completely independent of $\omega$ and $\beta$. Almost-sure stability is $\mu - \sigma^2/2 < 0$,
likewise. So the MS-stability region, normally drawn as an awkward domain in
$(h\lambda, h\eta) \subset \mathbb{C}^2$, becomes a half-plane in $(\mu,\sigma)$ crossed with all of
$\mathbb{R}^2$ in the rotational parameters. That is exactly the kind of "the reparameterization
makes something transparent" payoff the paper needs, it sits in a literature the paper already
cites, and it costs one paragraph.

### 2. A winding-law contrast with an actual limit theorem

§2 and §11 assert the distinction from planar BM but only demonstrate it with covariance rank.
$\Theta_t/t \to \omega$ a.s. and $(\Theta_t - \omega t)/\sqrt{t} \sim N(0,\beta^2)$ is trivially
derivable here, and contrasts sharply with Spitzer's $2/\log t$ Cauchy limit. That converts a
scatter-plot claim into a theorem.

### 3. A reason to want the phase

Absent an interpretation of $\omega$ and $\beta$ — a physical, financial, or signal-processing
quantity they measure — the four-parameter family is a solution without a problem. Eq. 17 is a
joint Mellin–Fourier transform; connecting it to characteristic-function pricing methods would at
least give the object an anchor in a real technique.

---

## 8. Scores

| Dimension | Score |
|---|---|
| Mathematical correctness | **9.5 / 10** |
| Numerical execution & internal consistency | **9 / 10** |
| Reproducibility practice | **8.5 / 10** |
| Novelty | **1.5 / 10** |
| Value to quantitative finance | **1.5 / 10** |
| Value to mathematics (research) | **2 / 10** |
| Value as exposition / pedagogy | **6.5 / 10** |
| Framing honesty | **6.5 / 10** — candid in §2 and §16, oversold in the abstract and §12 |
| **Overall as a research contribution** | **3 / 10** |
| **Overall as a verified teaching artifact** | **7 / 10** |

**Venue reality check:** desk-reject at any probability, numerical analysis, or mathematical finance
journal on novelty grounds — the referee's first sentence would be "this is the solution of the
scalar complex linear SDE." Viable as an arXiv expository preprint, a lecture note, or internal
documentation of a verification pipeline. If the stability-region result in §7.1 above were added
and the Phase 3 collapse acknowledged honestly, it could become a short, legitimate technical note.

---

## Closing observation

One note about the shape of the failure. Everything *local* here is excellent: every derivation is
correct, every assertion is checked, every number reconciles, the seeds are pinned and the notebook
executes twice cleanly. What's missing is entirely *global*: no step in the process asked "is this
already known?", "is the four-parameter family actually four-parameter?", or "who would use this
and for what?"

That combination — flawless verification of a result that didn't need verifying, with no check on
whether the result matters — is a recognizable pattern in staged research pipelines, where each
stage validates the previous stage's output rather than the premise. Worth building a "prior art and
triviality check" gate before the write-up stage, if this came out of something like that.
