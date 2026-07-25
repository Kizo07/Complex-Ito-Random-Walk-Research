# Thorough Review of *Native Complex Geometric Brownian Motion*

## Itô Correction, Stochastic Rotation, Noise-Dimension Geometry, Novelty, and Quantitative-Finance Value

**Paper reviewed:** *Native Complex Geometric Brownian Motion: Itô correction, stochastic rotation, and noise-dimension geometry*  
**Length reviewed:** 30 pages, including derivations, tables, numerical results, appendices, and figures  
**Review scope:** Mathematical verification, numerical consistency, novelty, usefulness, value to quantitative finance, value to mathematics, literature positioning, limitations, and publication readiness

---

# Overall verdict

I reviewed the full 30-page paper, including its derivations, tables, numerical results, and figures: *Native Complex Geometric Brownian Motion: Itô correction, stochastic rotation, and noise-dimension geometry*.

**Overall rating as a research paper: 6.1/10**

**As an expository or computational stochastic-calculus note: 8.3/10**

**As a genuinely new mathematical contribution: 3.0/10**

**As a direct contribution to quantitative finance: 2.5/10**

The central mathematics is correct. I found no fatal error in the construction, Itô correction, transition law, moments, covariance-rank argument, or two-driver comparison. The paper is unusually clear about a subtle and often mishandled distinction: the pathwise Itô correction involves the **bilinear complex square** $B^2$, while energy and mean-square calculations involve the **Hermitian quantity** $|B|^2$.

The principal weakness is novelty. The process is exactly the familiar constant-coefficient scalar complex linear SDE, expressed in a log-polar parameterization. Its radial component is ordinary GBM, and with one Brownian driver its angular randomness contains no independent information. The paper therefore adds much more as a careful tutorial and reproducible benchmark than as new stochastic-analysis theory or a new financial model.

## Scorecard

| Dimension | Rating | Assessment |
|---|---:|---|
| Mathematical correctness | **9.2/10** | Core equations and derivations are correct |
| Mathematical rigor | **8.0/10** | Strong derivations, but some terminology and boundary statements need qualification |
| Novelty in stochastic analysis | **3.0/10** | Primarily a reparameterization and synthesis of established theory |
| Novelty as exposition | **6.5/10** | The $B^2$ versus $|B|^2$ explanation and noise-rank presentation are valuable |
| Numerical verification | **8.5/10** | Well designed; several headline numbers independently reproduce |
| Reproducibility from the PDF alone | **6.5/10** | Excellent claimed workflow, but notebook, code, and manifests were not supplied here |
| Presentation and figures | **8.5/10** | Polished and readable, though somewhat over-illustrated |
| Direct quant-finance usefulness | **2.5/10** | No new asset-price law, pricing result, calibration, or empirical application |
| Pedagogical usefulness for quants | **7.5/10** | Good complex-Itô example and software test problem |
| Publication readiness as a research article | **4.5/10** | Requires a substantially stronger contribution or reframing as an expository note |

---

# 1. Mathematical verification

Let

$$
\mathcal Z_t
=
\mathcal Z_0
\exp\left(
\left[\left(\mu-\frac{\sigma^2}{2}\right)+i\omega\right]t
+
(\sigma+i\beta)W_t
\right),
$$

and define

$$
\kappa=\left(\mu-\frac{\sigma^2}{2}\right)+i\omega,
\qquad
B=\sigma+i\beta.
$$

The paper then writes

$$
\mathcal Z_t=\mathcal Z_0e^{\kappa t+BW_t}.
$$

That is the correct starting point.

## 1.1 Modulus and phase

Since $|e^z|=e^{\operatorname{Re}z}$,

$$
R_t:=|\mathcal Z_t|
=
R_0
\exp\left[
\left(\mu-\frac{\sigma^2}{2}\right)t+\sigma W_t
\right].
$$

Therefore

$$
\frac{dR_t}{R_t}
=
\mu\,dt+\sigma\,dW_t.
$$

This is exactly ordinary GBM. The imaginary parameters $\omega$ and $\beta$ have no effect on the modulus, pathwise or distributionally.

The continuous phase lift is

$$
\Theta_t
=
\Theta_0+\omega t+\beta W_t,
$$

so

$$
\mathcal Z_t=R_te^{i\Theta_t}.
$$

This treatment correctly distinguishes the continuous phase lift from the principal argument, which may jump by $2\pi$ at the branch cut.

**Verdict:** fully correct.

---

## 1.2 Complex Itô correction

For $F(z)=e^z$ and $\Lambda_t=\kappa t+BW_t$,

$$
d\mathcal Z_t
=
\mathcal Z_t\,d\Lambda_t
+
\frac12\mathcal Z_t\,d[\Lambda,\Lambda]_t.
$$

Because this is the bilinear complex bracket,

$$
d[\Lambda,\Lambda]_t=B^2dt,
$$

not $|B|^2dt$.

Now

$$
B^2
=
(\sigma+i\beta)^2
=
\sigma^2-\beta^2+2i\sigma\beta.
$$

Consequently,

$$
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(\kappa+\frac12B^2\right)dt+B\,dW_t,
$$

and

$$
\kappa+\frac12B^2
=
\mu-\frac{\beta^2}{2}
+
i(\omega+\sigma\beta).
$$

Thus

$$
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left[
\mu-\frac{\beta^2}{2}
+i(\omega+\sigma\beta)
\right]dt
+
(\sigma+i\beta)dW_t.
}
$$

This is the most important calculation in the paper, and it is correct.

The two correction terms have clear meanings:

$$
-\frac{\beta^2}{2}
$$

is needed to prevent Brownian rotation from generating artificial radial growth, while

$$
i\sigma\beta
$$

comes from the shared quadratic covariation

$$
d(\sigma W_t)\,d(\beta W_t)=\sigma\beta\,dt.
$$

The paper is also correct that replacing $B^2$ by $|B|^2$ would destroy the intended modulus and phase dynamics.

**Verdict:** fully correct and pedagogically strong.

---

## 1.3 Pure stochastic rotation

Setting $\mu=\sigma=0$ gives

$$
\mathcal Z_t
=
\mathcal Z_0e^{i\omega t+i\beta W_t},
$$

whose modulus is constant.

The SDE is

$$
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left(-\frac12\beta^2+i\omega\right)dt
+i\beta\,dW_t.
$$

The real drift $-\beta^2/2$ is necessary. Omitting it would yield the exact solution

$$
\widetilde{\mathcal Z}_t
=
\mathcal Z_0
 e^{\beta^2t/2}
 e^{i\omega t+i\beta W_t},
$$

which has spurious exponential radial growth.

**Verdict:** correct.

---

## 1.4 Ordinary exponential versus Doléans exponential

Let

$$
Y_t=At+BW_t,
\qquad
A=\kappa+\frac12B^2.
$$

For a continuous complex semimartingale,

$$
\mathcal E(Y)_t
=
\exp\left(
Y_t-Y_0-\frac12[Y,Y]_t
\right).
$$

Since $[Y,Y]_t=B^2t$,

$$
\mathcal E(Y)_t
=
\exp\left[
\left(A-\frac12B^2\right)t+BW_t
\right]
=
e^{\kappa t+BW_t}.
$$

Hence

$$
\mathcal Z_t=\mathcal Z_0\mathcal E(Y)_t.
$$

The paper also correctly distinguishes

$$
\log_{\mathrm{cont}}\frac{\mathcal Z_t}{\mathcal Z_0}
=
\kappa t+BW_t
$$

from the stochastic logarithm

$$
\int_0^t\frac{d\mathcal Z_s}{\mathcal Z_s}
=
At+BW_t.
$$

Their difference is $B^2t/2$.

These relationships belong to established stochastic-exponential theory, including complex-valued semimartingales. See, for example, the literature on stochastic exponentials and logarithms: <https://arxiv.org/abs/1702.03573>.

**Verdict:** correct.

---

## 1.5 Exact transition formula

For $h=t_{n+1}-t_n$ and

$$
\Delta W_n\sim N(0,h),
$$

the paper obtains

$$
\mathcal Z_{n+1}
=
\mathcal Z_n
\exp\left(
\kappa h+B\Delta W_n
\right).
$$

Equivalently,

$$
\Delta\log R_n
=
\left(\mu-\frac12\sigma^2\right)h
+
\sigma\Delta W_n,
$$

and

$$
\Delta\Theta_n
=
\omega h+\beta\Delta W_n.
$$

This is an exact transition, not a discretization scheme.

**Verdict:** correct.

---

## 1.6 Log-polar transition law

At fixed $t$,

$$
\begin{pmatrix}
\log(R_t/R_0)\\
\Theta_t-\Theta_0
\end{pmatrix}
=
\begin{pmatrix}
(\mu-\sigma^2/2)t\\
\omega t
\end{pmatrix}
+
\begin{pmatrix}
\sigma\\
\beta
\end{pmatrix}W_t.
$$

Therefore it is Gaussian with covariance

$$
t
\begin{pmatrix}
\sigma^2 & \sigma\beta\\
\sigma\beta & \beta^2
\end{pmatrix}.
$$

Its determinant is zero:

$$
\sigma^2\beta^2-(\sigma\beta)^2=0.
$$

For $\sigma\neq0$,

$$
\Theta_t-\Theta_0-\omega t
=
\frac{\beta}{\sigma}
\left[
\log(R_t/R_0)
-
\left(\mu-\frac{\sigma^2}{2}\right)t
\right].
$$

Thus the unwrapped phase and log-radius are perfectly correlated or anticorrelated whenever $\sigma\beta\neq0$.

**Verdict:** correct.

---

## 1.7 Moment formulas

For the radial moments,

$$
R_t^p
=
R_0^p
\exp\left[
p\left(\mu-\frac12\sigma^2\right)t
+p\sigma W_t
\right].
$$

Using

$$
\mathbb E[e^{cW_t}]=e^{c^2t/2},
$$

gives

$$
\boxed{
\mathbb E[R_t^p]
=
R_0^p
\exp\left[
\left(
p\mu+\frac12p(p-1)\sigma^2
\right)t
\right].
}
$$

This is correct for every real $p$ at finite $t$.

For integer $n$,

$$
\mathcal Z_t^n
=
\mathcal Z_0^n
 e^{n\kappa t+nBW_t},
$$

so

$$
\boxed{
\mathbb E[\mathcal Z_t^n]
=
\mathcal Z_0^n
\exp\left[
\left(
n\kappa+\frac12n^2B^2
\right)t
\right].
}
$$

For mixed log-polar moments,

$$
\boxed{
\mathbb E\left[
R_t^pe^{iq(\Theta_t-\Theta_0)}
\right]
=
R_0^p
\exp\left[
p\left(\mu-\frac12\sigma^2\right)t
+iq\omega t
+\frac12(p\sigma+iq\beta)^2t
\right].
}
$$

All three formulas are correct.

---

## 1.8 Cartesian local covariance

Writing $\mathcal Z_t=X_t+iY_t$, the diffusion vector at state $z$ is

$$
g(z)
=
\begin{pmatrix}
\operatorname{Re}(Bz)\\
\operatorname{Im}(Bz)
\end{pmatrix}.
$$

The local covariance is

$$
g(z)g(z)^\top dt.
$$

This is an outer product, so its rank is at most one.

When $B\neq0$ and $z\neq0$, it has rank exactly one. When $B=0$, it has rank zero.

**Verdict:** correct, subject to the degenerate-case qualification discussed below.

---

## 1.9 Bilinear and Hermitian brackets

From

$$
d\mathcal Z_t=B\mathcal Z_t\,dW_t+\text{drift},
$$

the bilinear bracket is

$$
\boxed{
d[\mathcal Z,\mathcal Z]_t
=
B^2\mathcal Z_t^2dt.
}
$$

The conjugate/Hermitian bracket is

$$
\boxed{
d[\mathcal Z,\overline{\mathcal Z}]_t
=
|B|^2|\mathcal Z_t|^2dt.
}
$$

These are different objects. The first is complex and retains orientation information; the second is real and nonnegative.

**Verdict:** correct.

---

## 1.10 Two-driver comparison

For independent Brownian motions $W^{(r)}$ and $W^{(\theta)}$,

$$
\mathcal Z_t^{(2)}
=
\mathcal Z_0
\exp\left[
\kappa t+\sigma W_t^{(r)}
+i\beta W_t^{(\theta)}
\right].
$$

The log-polar covariance is

$$
\begin{pmatrix}
\sigma^2&0\\
0&\beta^2
\end{pmatrix}dt,
$$

which has rank two when $\sigma\beta\neq0$.

The complex quadratic variation of the logarithm is

$$
\sigma^2dt+(i\beta)^2dt
=
(\sigma^2-\beta^2)dt,
$$

because the cross-bracket vanishes. Hence

$$
\boxed{
\frac{d\mathcal Z_t^{(2)}}{\mathcal Z_t^{(2)}}
=
\left(
\mu-\frac12\beta^2+i\omega
\right)dt
+
\sigma dW_t^{(r)}
+i\beta dW_t^{(\theta)}.
}
$$

The $i\sigma\beta$ cross drift disappears.

**Verdict:** correct.

---

# 2. Independent numerical checks

I independently recomputed the main analytical numbers using the paper's stated parameters

$$
(\mu,\sigma,\omega,\beta)
=
(0.18,0.42,0.90,0.65),
\qquad
R_0=1.25,\quad
\Theta_0=0.35.
$$

The coefficient calculations reproduce exactly:

$$
\kappa=0.0918+0.9000i,
$$

$$
B=0.4200+0.6500i,
$$

$$
B^2=-0.2461+0.5460i,
$$

and

$$
A
=
\kappa+\frac12B^2
=
-0.03125+1.1730i.
$$

At $T=1.5$, I obtain

$$
\mathbb E[R_T]=1.6374555634,
$$

$$
\mathbb E[R_T^2]=3.4934406236,
$$

$$
\mathbb E[\mathcal Z_T]
=
-0.6119132801+1.0238332761i,
$$

and

$$
\mathbb E[\mathcal Z_T^2]
=
0.3146173961-0.9318454878i,
$$

matching the paper's tables.

I also independently reran an Euler–Maruyama strong-convergence experiment with 12,000 paths, 512 fine increments, and the stated seed base. Using $T=1$, which is implied by the reported step sizes, I obtained approximately:

| Steps | Independent RMS error | Paper |
|---:|---:|---:|
| 16 | 0.21326 | 0.21371 |
| 32 | 0.13730 | 0.13548 |
| 64 | 0.09177 | 0.09148 |
| 128 | 0.06348 | 0.06331 |
| 256 | 0.04403 | 0.04450 |

My fitted slope was $0.5665$, versus the paper's $0.5625$. That is excellent agreement.

The analytical tables and the strong-convergence experiment therefore appear trustworthy.

I could not independently verify the assertions about two clean notebook executions, artifact hashes, or the exact Monte Carlo streams because the source notebook, model file, JSON evidence, and manifests were not included with the PDF.

---

# 3. Mathematical issues and needed corrections

There are no major errors in the central derivations, but several points should be corrected or more precisely stated.

## 3.1 “Rank one” should sometimes be “rank at most one”

The abstract and conclusion occasionally say that one driver “forces rank-one covariance.” The precise statement is:

$$
\operatorname{rank}\Sigma\leq1,
$$

and the rank is exactly one only when

$$
(\sigma,\beta)\neq(0,0)
$$

or equivalently $B\neq0$.

If $\sigma=\beta=0$, the covariance rank is zero.

**Severity:** minor.

---

## 3.2 The fixed-time support needs a topology qualification

The paper states that the fixed-time complex support is

$$
\left\{
\mathcal Z_0e^{\kappa t+Bw}:w\in\mathbb R
\right\}.
$$

That is accurate as the image of the Gaussian coordinate and as the support relative to the state space

$$
\mathbb C^\times=\mathbb C\setminus\{0\}.
$$

But the topological support of the distribution considered as a measure on all of $\mathbb C$ is closed. When $\sigma\neq0$, the spiral or ray approaches zero, and every neighborhood of zero has positive probability. Therefore the support in $\mathbb C$ also contains $0$, even though

$$
\mathbb P(\mathcal Z_t=0)=0.
$$

A precise version would say:

> The law is concentrated on a one-dimensional spiral in $\mathbb C^\times$; its support in $\mathbb C$ is the closure of that spiral.

**Severity:** minor but mathematically real.

---

## 3.3 The one-driver “boundary” is local and model-specific

One real Brownian driver always gives a diffusion matrix with local rank at most one. But it does **not** generally imply that the fixed-time law of a two-dimensional SDE is one-dimensional.

For example,

$$
dX_t=dW_t,
\qquad
dY_t=X_tdt
$$

has only one Brownian driver, yet

$$
X_t=W_t,
\qquad
Y_t=\int_0^tW_s\,ds
$$

has covariance

$$
\begin{pmatrix}
t&t^2/2\\
t^2/2&t^3/3
\end{pmatrix},
$$

whose determinant is

$$
\frac{t^4}{12}>0.
$$

Its terminal distribution is genuinely two-dimensional.

The reviewed model has one-dimensional fixed-time support because its two log-polar coordinates depend only on the single terminal variable $W_t$, and because the constant complex drift and diffusion multiplications commute. It is not a universal consequence of having one Brownian driver.

The paper mostly uses the correct phrase “local covariance,” but the broader “noise-dimension boundary” language should explicitly distinguish:

1. instantaneous diffusion rank;
2. number of Brownian drivers; and
3. dimension of the finite-horizon transition law.

**Severity:** moderate framing issue.

---

## 3.4 Standard volatility sign conventions

The paper allows

$$
\sigma,\beta\in\mathbb R
$$

while calling both volatilities. Conventionally, a volatility is nonnegative.

In the one-driver model, the relative sign of $\sigma$ and $\beta$ determines whether radial and angular shocks are perfectly positively or negatively correlated. A cleaner parameterization would use

$$
\sigma\geq0,
\qquad
\beta\geq0,
\qquad
\rho\in[-1,1]
$$

and reserve $\rho$ for the correlation.

There is also a global sign redundancy: replacing $(\sigma,\beta)$ by $(-\sigma,-\beta)$ produces the same process law because $-W$ is again Brownian motion.

**Severity:** minor modeling and identifiability issue.

---

## 3.5 Numerical horizon ambiguity

Section 13.1 calls $T=1.50$ the primary terminal horizon. But Table 7 reports

$$
h=0.0625
$$

for 16 time steps, which implies

$$
T=16(0.0625)=1,
$$

not $1.5$.

My independent replication confirms that the convergence experiment used $T=1$. With $T=1.5$, the errors are materially different.

The quadratic-variation figure also appears to use the interval $[0,1]$.

The paper should list the horizon separately for each experiment rather than implying that all experiments use the primary $T=1.5$.

**Severity:** minor reproducibility issue.

---

# 4. An important literature discrepancy the paper should address

Prior literature clearly establishes the scalar complex linear SDE. Buckwar, Horváth-Bokor, and Winkler consider

$$
dX_t=\lambda X_tdt+\eta X_tdW_t
$$

with complex coefficients and a real Wiener process, and explicitly call its exact solution “complex geometric Brownian motion.” See the full paper: <https://edoc.hu-berlin.de/bitstreams/b5e2e91d-e876-45fd-bfae-9f9c57dbef71/download>.

However, their displayed pathwise solution uses

$$
X_t
=
X_0
\exp\left[
\left(\lambda-\frac12|\eta|^2\right)t+\eta W_t
\right].
$$

That formula appears directly in their paper.

As written, it does **not** solve the displayed Itô SDE for a genuinely non-real $\eta$. Applying Itô gives

$$
\frac{dX_t}{X_t}
=
\left[
\lambda
+
\frac12(\eta^2-|\eta|^2)
\right]dt
+
\eta dW_t.
$$

The correct pathwise correction is

$$
-\frac12\eta^2,
$$

not

$$
-\frac12|\eta|^2.
$$

Their mean-square stability condition involving $|\eta|^2$ is nevertheless correct, because $|\eta|^2$ governs the evolution of $\mathbb E|X_t|^2$. Thus the likely issue is a pathwise-solution typo or conflation of the bilinear and Hermitian quantities, rather than an error in the eventual stability criterion.

This is highly relevant to the reviewed paper. Its treatment of $B^2$ versus $|B|^2$ is correct and resolves exactly this type of confusion. But the manuscript currently cites Buckwar et al. only as prior art and does not mention the discrepancy.

That is a missed scholarly opportunity. A carefully documented correction would make the paper more valuable and improve its novelty positioning.

---

# 5. Novelty assessment

## 5.1 The process itself is not new

The constant-coefficient scalar complex SDE

$$
\frac{dZ_t}{Z_t}=A\,dt+B\,dW_t
$$

already has the exact solution

$$
Z_t
=
Z_0
\exp\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
$$

The paper's four parameters are simply a change of coordinates from the real and imaginary parts of $A$ and $B$:

$$
\sigma=\operatorname{Re}B,
\qquad
\beta=\operatorname{Im}B,
$$

$$
\mu=\operatorname{Re}A+\frac12\beta^2,
\qquad
\omega=\operatorname{Im}A-\sigma\beta.
$$

Conversely,

$$
B=\sigma+i\beta,
$$

$$
A
=
\mu-\frac12\beta^2+i(\omega+\sigma\beta).
$$

This mapping is essentially bijective, apart from ordinary sign and interpretation conventions. Therefore the paper does not introduce a new model family; it reparameterizes the established complex scalar linear SDE so that radial and angular target parameters are immediately interpretable.

The stochastic exponential and logarithm framework is also established, as is a general stochastic calculus for complex-valued semimartingales. See <https://arxiv.org/abs/1702.03573>.

## 5.2 What is genuinely useful in the synthesis

The strongest original or semi-original elements are:

- The clean separation of the target parameters $(\mu,\sigma)$ and $(\omega,\beta)$.
- The explicit interpretation of the imaginary cross drift $+\sigma\beta$.
- The side-by-side distinction between $B^2$ and $|B|^2$.
- The log-polar covariance-rank presentation.
- The contrast between one shared driver and two independent drivers.
- The reproducible numerical and visual validation package.
- The recovery of the earlier “Phase 3” construction as a constrained parameter subfamily.

These are useful organizational and pedagogical contributions. They are not substantial new stochastic-analysis theorems.

## 5.3 Novelty rating

Under a strict pure- or applied-mathematics research standard:

$$
\boxed{\text{Novelty: }3.0/10}
$$

As a carefully designed expository synthesis:

$$
\boxed{\text{Expository novelty: }6.5/10}
$$

If the manuscript explicitly documented the $\eta^2$ versus $|\eta|^2$ inconsistency in prior literature and developed a formal correction theorem, I would raise the scholarly novelty modestly, perhaps to approximately $4.0$–$4.5/10$.

---

# 6. Value to quantitative finance

## 6.1 The radial asset dynamics are exactly ordinary GBM

The modulus satisfies

$$
\frac{dR_t}{R_t}
=
\mu\,dt+\sigma\,dW_t.
$$

Therefore any payoff depending only on the terminal modulus,

$$
H=f(R_T),
$$

has exactly the same distribution and pricing problem as under standard GBM. The parameters $\omega$ and $\beta$ do not affect the modulus.

Consequently, the model does not generate:

- stochastic volatility;
- volatility smiles or skews;
- jumps;
- heavy tails;
- leverage effects beyond the deterministic phase mapping;
- multiple economic risk factors;
- richer return distributions;
- different prices for ordinary claims on $R$.

## 6.2 The phase is not an independent financial state

For $\sigma\neq0$,

$$
W_t
=
\frac{
\log(R_t/R_0)
-
(\mu-\sigma^2/2)t
}{\sigma}.
$$

Substituting into the phase gives

$$
\Theta_t
=
\Theta_0+\omega t
+
\frac{\beta}{\sigma}
\left[
\log(R_t/R_0)
-
\left(\mu-\frac12\sigma^2\right)t
\right].
$$

Thus $\Theta_t$ is completely determined by $R_t$ and time. More strongly, the entire phase path is determined by the radial path.

The complex process can therefore be written as a deterministic time-dependent transformation of the ordinary GBM:

$$
\mathcal Z_t=F(t,R_t).
$$

The model has four descriptive parameters, but only one stochastic factor. From a quant perspective, the phase is a feature transformation of the return, not an additional source of economic uncertainty.

If only $R_t$ is observed, $\omega$ and $\beta$ cannot be estimated from asset prices because they have no effect on $R_t$.

## 6.3 No financial model is developed

The paper explicitly disclaims financial assertions, which is appropriate. It does not provide:

- a risk-neutral measure;
- no-arbitrage conditions;
- a numeraire or money-market account;
- a definition of what the complex quantity represents economically;
- hedging arguments;
- market-completeness analysis;
- option-pricing formulas beyond ordinary GBM;
- calibration methodology;
- empirical results;
- comparison with established financial models.

A complex-valued process cannot simply be called a tradable security price under the usual order and positivity structure of financial markets. One must specify a real observable, such as the modulus, real part, energy, or another functional. Once the observable is the modulus, the model collapses back to ordinary GBM.

## 6.4 Where it could still help quants

The paper does have useful secondary applications:

- A unit test for complex-valued SDE libraries.
- A teaching example for Itô versus Hermitian quadratic variation.
- A benchmark for exact simulation and Euler–Maruyama convergence.
- A possible representation of oscillatory signals, Fourier coefficients, or amplitude-phase factors.
- A starting point for a latent cyclic-state model, provided the phase is later allowed to influence the radial dynamics.

## 6.5 Quant-finance rating

As a new financial model:

$$
\boxed{2.0/10}
$$

As a pedagogical or software benchmark for quantitative researchers:

$$
\boxed{7.0/10}
$$

Overall quant-finance value:

$$
\boxed{2.5/10}
$$

---

# 7. Value to mathematics more broadly

The paper is valuable in three limited but real ways.

First, it offers a clean example showing why complex stochastic calculus involves two distinct second-order quantities:

$$
B^2
\quad\text{and}\quad
|B|^2.
$$

That distinction is easy to mishandle and has concrete consequences.

Second, it gives a visually strong illustration of the difference between:

- a process taking values in a two-dimensional state space; and
- a process having two independent stochastic directions.

A path can move in the complex plane while its instantaneous diffusion covariance remains rank one.

Third, it offers a reproducible exact benchmark for numerical methods for complex SDEs.

But it does not establish a new existence theorem, uniqueness result, support theorem, stochastic exponential identity, numerical convergence theorem, or financial pricing result. Most formulas follow in a few lines from a Gaussian exponential and elementary Itô calculus.

Therefore:

$$
\boxed{\text{General mathematical research value: }4.5/10}
$$

$$
\boxed{\text{Pedagogical mathematical value: }7.5/10}
$$

---

# 8. The most important missing extension

The natural generalization is not merely “one driver versus two independent drivers,” but **two correlated drivers**.

Let

$$
d[W^{(r)},W^{(\theta)}]_t=\rho\,dt,
\qquad -1\leq\rho\leq1,
$$

and define

$$
\mathcal Z_t
=
\mathcal Z_0
\exp\left[
\kappa t
+\sigma W_t^{(r)}
+i\beta W_t^{(\theta)}
\right].
$$

Then the log-polar covariance is

$$
\Sigma_\rho
=
\begin{pmatrix}
\sigma^2&\rho\sigma\beta\\
\rho\sigma\beta&\beta^2
\end{pmatrix},
$$

with determinant

$$
\det\Sigma_\rho
=
\sigma^2\beta^2(1-\rho^2).
$$

Thus:

- $|\rho|=1$ gives rank one;
- $|\rho|<1$ gives rank two when $\sigma\beta\neq0$;
- $\rho=0$ gives the paper's independent comparator.

The corresponding SDE is

$$
\boxed{
\frac{d\mathcal Z_t}{\mathcal Z_t}
=
\left[
\mu-\frac12\beta^2
+i(\omega+\rho\sigma\beta)
\right]dt
+
\sigma dW_t^{(r)}
+i\beta dW_t^{(\theta)}.
}
$$

This single formula unifies the one-driver and independent-driver cases and identifies the cross drift directly with the correlation parameter.

It would be a more natural centerpiece than treating only $\rho=1$ and $\rho=0$.

---

# 9. What would make the paper publishable as stronger research

The manuscript would need at least one substantive extension beyond the current synthesis.

The highest-priority revisions are:

1. **Reframe the title and claims.**  
   A more accurate title would be:

   > *A Log-Polar Parameterization of Scalar Complex Geometric Brownian Motion: Itô Corrections and Noise Rank*

2. **Explicitly address the prior-literature $|\eta|^2$ discrepancy.**  
   This is one of the strongest reasons for the note to exist.

3. **Add the correlated-driver model.**  
   The $\rho$-parameterization gives a complete covariance-rank picture rather than two isolated endpoints.

4. **Formalize the results as propositions or theorems.**  
   Separate:
   - solution equivalence;
   - modulus and phase dynamics;
   - transition law;
   - covariance rank;
   - support relative to $\mathbb C^\times$;
   - correlated-driver boundary.

5. **Clarify the scope of the one-driver result.**  
   State that local covariance has rank at most one, while finite-time distributions of general one-driver multidimensional SDEs may be full-dimensional.

6. **Either develop a genuine financial application or remove any implication of one.**  
   A financial extension would require phase feedback into radial volatility or drift, a risk-neutral formulation, identifiability analysis, and empirical calibration.

7. **Supply the notebook and evidence artifacts with the manuscript.**  
   The PDF describes a strong reproducibility package, but the claims should be independently inspectable.

8. **Reduce repetitive figures.**  
   Several figures explain essentially the same facts. A research version could be reduced from 18 figures to roughly 7–9 without losing substance.

---

# 10. Referee-style recommendation

## For a stochastic-analysis or applied-mathematics research journal

**Recommendation: reject in current form, or major revision with a substantially stronger result.**

Reason: the mathematics is correct, but the main process, exact solution, stochastic exponential, and numerical benchmark are established. The manuscript's contribution is mainly parameterization and exposition.

## For an expository mathematics or computational notebook venue

**Recommendation: accept after moderate revision.**

The paper is clear, visually effective, reproducible in design, and teaches an important complex-Itô distinction.

## For a quantitative-finance journal

**Recommendation: reject in current form.**

There is no new price process for real assets, no derivative-pricing result, no calibration, no empirical validation, and no independent phase risk in the one-driver construction.

---

# Final assessment

The paper is **mathematically sound, carefully presented, and pedagogically valuable**, but its core object is a standard complex linear SDE under a useful log-polar reparameterization. Its most significant intellectual value is the clear treatment of $B^2$ versus $|B|^2$, especially because that distinction appears to have been mishandled in at least one cited complex-GBM source. As written, it is a strong technical note rather than a major contribution to either mathematics or quantitative finance.
