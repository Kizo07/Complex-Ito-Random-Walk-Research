# Hidden Exactness and Corrected Frontiers in Bounded-Factor Stochastic Calculus

## Phase 14 mathematical discovery paper

**Date:** 2026-08-22

**Scope:** mathematics only

**Status:** theorem draft after independent phase-by-phase audit

---

## Abstract

This phase re-examines the points at which the earlier exact-law program was
said to stop. Three substantial results survive a deliberately severe filter.

First, every centered Gaussian variance mixture has an exact at-the-money
Bachelier implied-standard-deviation level and curvature. Applied to the
stochastic-correlation clock, these identities prove the opposite local
curvatures of spread and basket implied-correlation smiles, but they also show
that the earlier claim that at-the-money implied correlation equals the mean
correlation clock is false except in the deterministic-clock limit. The exact
level contains a Jensen correction equal to the variance of the square root of
the clock.

Second, Brownian leverage between the correlation driver and the asset
drivers does not destroy conditional Gaussianity. It creates a random
conditional mean. Orthogonal Brownian decomposition and an Itô gauge transform
reduce the leveraged terminal characteristic function to a one-dimensional
complex Feynman--Kac equation. European pricing therefore remains
one-dimensional. What leverage genuinely destroys is the centered
variance-mixture representation and the scalar-clock reflection formula for
barriers. A short-time moment calculation proves that leverage generically
creates skewness.

Third, the Phase-Gram correlation-matrix process has a stationary matrix law
even though its unwrapped angles do not. Its determinant is exactly a product
of squared sines. This gives finite-time determinant moments, a stationary
product-Beta law, closed log-determinant cumulants, a high-dimensional central
limit theorem, and an exact first-singularity distribution. Thus the process
is stationary after periodic quotienting, but it also hits the boundary of the
elliptope infinitely often.

Four supporting results repair or sharpen other phase boundaries: the exact
scale-identifiability group is simultaneous scaling, not inverse scaling; the
standard two-time backward Feynman--Kac theorem never fails in the
nonautonomous setting, while the misordered one-parameter horizon equation has
an exact commutator defect; the joint endpoint--clock density is a Fourier
inversion of one-dimensional tilted kernels and is hypoelliptically smooth; and
spectrally one-sided Levy drivers retain exact barrier transforms through scale
functions even though the reflection principle is lost.

No priority claim is made here. The purpose of Phase 14 is to isolate and prove
the strongest mathematics latent in Phases 1--13, including corrections where
the earlier synthesis overstated a claim.

---

## 1. Selection result from Phases 1--13

The filter used in this phase was:

1. the statement must be theorem-shaped;
2. it must not be merely a restatement of an invertible coordinate change;
3. it must survive direct algebraic and stochastic-calculus checks;
4. it must either cross a previously stated tractability frontier or correct a
   mathematically consequential claim; and
5. a negative or corrective theorem is admissible.

Under that filter, Phases 1--5 yield no new Phase 14 theorem. Their strongest
result remains the already-completed affine one-phase classification. The new
material begins where the bounded-factor finance program introduced path
functionals, leverage, matrix-valued states, and nonautonomous evolution.

The three major Phase 14 results are:

- exact implied-correlation level and curvature identities;
- leverage-preserving one-dimensional transform closure; and
- Phase-Gram quotient stationarity, determinant laws, and boundary times.

The scale symmetry, nonautonomous Feynman--Kac ordering, joint
endpoint--clock density, and Levy fluctuation formulas are retained as
supporting results because they materially repair the mathematical frontier.

---

## 2. Common bounded-factor setup

Let

\[
f_c(x)=\frac{x}{\sqrt{x^2+c^2}},
\qquad
s_c(x)=\sqrt{1-f_c(x)^2}=\frac{c}{\sqrt{x^2+c^2}},
\qquad c>0.
\]

The inverse and Jacobian are

\[
f_c^{-1}(r)=\frac{cr}{\sqrt{1-r^2}},
\qquad
\frac{d}{dr}f_c^{-1}(r)=\frac{c}{(1-r^2)^{3/2}}.
\]

For the Gaussian driver,

\[
dX_t=\mu\,dt+\nu\,dW_t^0,
\qquad \nu>0,
\qquad \rho_t=f_c(X_t).
\]

Two forward assets are modeled by

\[
dF_{1,t}=\sigma_1\,dW_t^1,
\]

\[
dF_{2,t}=\sigma_2
\bigl(\rho_t\,dW_t^1+s_c(X_t)\,dW_t^2\bigr),
\]

where \(W^1\) and \(W^2\) are standard Brownian motions with zero mutual
quadratic covariation. For a linear combination

\[
Z_t=\alpha_1F_{1,t}+\alpha_2F_{2,t},
\]

write

\[
p=\alpha_1\sigma_1,
\qquad
q=\alpha_2\sigma_2.
\]

Its instantaneous variance is

\[
Q(x)=(p+qf_c(x))^2+q^2s_c(x)^2
=p^2+q^2+2pqf_c(x).
\]

Under independence of \(W^0\) from \((W^1,W^2)\),

\[
Z_T\mid \rho_{[0,T]}
\sim N\!\left(z_0,V_T\right),
\qquad
V_T=\beta T+\alpha A_T,
\]

where

\[
\beta=p^2+q^2,
\qquad
\alpha=2pq,
\qquad
A_T=\int_0^T\rho_t\,dt.
\]

The next section extracts exact smile identities from this representation
without using the specific law of \(A_T\).

---

## 3. Exact implied-correlation identities for every centered variance mixture

### 3.1 Bachelier notation

Let \(S>0\) be a random total standard deviation. Conditional on \(S\), let

\[
Y\mid S\sim N(0,S^2).
\]

For signed moneyness \(k=K-z_0\), define the undiscounted Bachelier call

\[
B(s,k)=s\varphi(k/s)-k\Phi(-k/s),
\qquad s>0,
\]

and the mixture call

\[
C(k)=\mathbb E[B(S,k)].
\]

The total implied standard deviation \(I(k)\) is the unique positive solution
of

\[
B(I(k),k)=C(k).
\]

The strict positivity of Bachelier vega,

\[
B_s(s,k)=\varphi(k/s)>0,
\]

gives uniqueness.

### 3.2 The level-and-curvature theorem

**Theorem 3.1 (exact centered-mixture smile identities).**  Assume

\[
0<\mathbb E[S]<\infty.
\]

Then the implied standard deviation is even and its at-the-money level is

\[
\boxed{I(-k)=I(k),\qquad I(0)=\mathbb E[S].}
\]

If additionally

\[
\mathbb E[S^{-1}]<\infty,
\]

then \(I\) is twice differentiable at zero and

\[
\boxed{
I''(0)=\mathbb E[S^{-1}]-\frac{1}{\mathbb E[S]}.
}
\]

Consequently,

\[
\boxed{
\left(I^2\right)''(0)
=2\left(\mathbb E[S]\mathbb E[S^{-1}]-1\right)\ge0.
}
\]

Equality holds if and only if \(S\) is almost surely constant.

**Proof.** Bachelier put--call parity in signed-moneyness form is

\[
B(s,-k)=B(s,k)+k.
\]

Taking expectations gives \(C(-k)=C(k)+k\). Hence

\[
B(I(k),-k)=B(I(k),k)+k=C(-k).
\]

Strict monotonicity in \(s\) implies \(I(-k)=I(k)\).

At zero moneyness,

\[
B(s,0)=\varphi(0)s,
\]

so

\[
\varphi(0)I(0)=C(0)=\varphi(0)\mathbb E[S].
\]

For the second derivative, direct differentiation gives

\[
B_k(s,k)=-\Phi(-k/s),
\qquad
B_{kk}(s,k)=\frac{\varphi(k/s)}{s}.
\]

The inverse-moment assumption permits differentiation under the expectation
near zero because

\[
0\le \frac{\varphi(k/S)}{S}\le\frac{\varphi(0)}{S}.
\]

Thus

\[
C'(0)=-\frac12,
\qquad
C''(0)=\varphi(0)\mathbb E[S^{-1}].
\]

Implicit differentiation of \(B(I(k),k)=C(k)\) gives \(I'(0)=0\), also
immediate from evenness. Differentiating once more at zero gives

\[
\varphi(0)I''(0)+\frac{\varphi(0)}{I(0)}
=\varphi(0)\mathbb E[S^{-1}],
\]

which yields the claimed formula. Finally,

\[
\mathbb E[S]\mathbb E[S^{-1}]\ge1
\]

by Cauchy--Schwarz, with equality precisely when \(S\) is constant almost
surely. \(\square\)

### 3.3 Exact implied-correlation level and curvature

Now set

\[
S^2=V_T=\beta T+\alpha A_T,
\qquad \alpha\ne0,
\]

and define implied correlation by the constant-correlation variance identity

\[
I(k)^2=\beta T+\alpha T\rho_{\mathrm{imp}}(k).
\]

We assume that the clock takes values in the admissible constant-correlation
variance interval. Then the mixture call lies between the two endpoint
Bachelier prices, so this inversion produces
\(\rho_{\mathrm{imp}}(k)\in[-1,1]\). An interior ATM value is assumed when a
smooth local correlation inversion is discussed.

**Corollary 3.2 (ATM Jensen wedge and exact local curvature).** Under the
assumptions of Theorem 3.1,

\[
\boxed{
\rho_{\mathrm{imp}}(0)
=\frac{\mathbb E[A_T]}{T}
-\frac{\operatorname{Var}(\sqrt{V_T})}{\alpha T}.
}
\]

If \(\mathbb E[V_T^{-1/2}]<\infty\), then

\[
\boxed{
\rho_{\mathrm{imp}}''(0)
=\frac{2}{\alpha T}
\left(
\mathbb E[\sqrt{V_T}]\mathbb E[V_T^{-1/2}]-1
\right).
}
\]

For a nondegenerate clock, the consequences are strict:

- a basket, \(\alpha>0\), has positive local implied-correlation curvature
  and an ATM level below \(\mathbb E[A_T]/T\);
- a spread, \(\alpha<0\), has negative local implied-correlation curvature
  and an ATM level above \(\mathbb E[A_T]/T\).

**Proof.** Since

\[
\mathbb E[V_T]=\beta T+\alpha\mathbb E[A_T]
\]

and

\[
I(0)^2=(\mathbb E\sqrt{V_T})^2
=\mathbb E[V_T]-\operatorname{Var}(\sqrt{V_T}),
\]

the level formula follows by solving for \(\rho_{\mathrm{imp}}(0)\). The
curvature follows from Theorem 3.1 and

\[
\rho_{\mathrm{imp}}''(0)
=\frac{(I^2)''(0)}{\alpha T}.
\]

\(\square\)

### 3.4 Correction to Phase 8

The previous statement

\[
\rho_{\mathrm{imp}}(0)=\mathbb E[A_T]/T
\]

is true only when \(V_T\) is deterministic. The square root in the ATM
Bachelier price cannot be replaced by the square root of the mean variance.

For the Phase 8 parameters

\[
\sigma_1=1.5,
\quad
\sigma_2=2.5,
\quad
x_0=0,
\quad
\mu=0.3,
\quad
\nu=0.8,
\quad
c=T=1,
\]

direct Gaussian quadrature gives

\[
\mathbb E[A_T]=0.1066287216.
\]

The reported ATM implied correlations,

\[
0.13453\quad\text{for the spread},
\qquad
0.08198\quad\text{for the basket},
\]

are not estimates of a common mean. They are the two opposite Jensen shifts
predicted exactly by Corollary 3.2.

The curvature theorem is local. It proves the sign at the money; it does not,
without additional assumptions on the mixing law, prove a fixed curvature
sign at every strike.

---

## 4. Leverage preserves one-dimensional European transform closure

### 4.1 Admissible Brownian leverage

Allow the factor driver to be correlated with the primitive asset drivers:

\[
d\langle W^0,W^1\rangle_t=\ell_1\,dt,
\qquad
d\langle W^0,W^2\rangle_t=\ell_2\,dt,
\qquad
d\langle W^1,W^2\rangle_t=0.
\]

The Brownian correlation matrix is

\[
\Sigma_W=
\begin{pmatrix}
1&0&\ell_1\\
0&1&\ell_2\\
\ell_1&\ell_2&1
\end{pmatrix}.
\]

Here the coordinate order is \((W^1,W^2,W^0)\).

**Lemma 4.1 (PSD constraint).** The above Brownian system exists if and only
if

\[
\boxed{\ell_1^2+\ell_2^2\le1.}
\]

**Proof.** The principal minors are

\[
1,
\qquad
1-\ell_1^2,
\qquad
1-\ell_2^2,
\qquad
1-\ell_1^2-\ell_2^2.
\]

The last nonnegativity condition implies the preceding two, and

\[
\det\Sigma_W=1-\ell_1^2-\ell_2^2.
\]

For this arrowhead matrix those conditions are also sufficient. \(\square\)

Let \(\ell=(\ell_1,\ell_2)^\top\). There is a matrix \(C\) satisfying

\[
CC^\top=I_2-\ell\ell^\top
\]

and an independent two-dimensional Brownian motion \(U\) such that

\[
\binom{dW_t^1}{dW_t^2}
=\ell\,dW_t^0+C\,dU_t.
\]

The construction keeps instantaneous asset correlation equal to \(f_c(X_t)\).
The instantaneous covariance-rate matrix of \((F_1,F_2,X)\) has determinant

\[
\sigma_1^2\sigma_2^2\nu^2s_c(X_t)^2
(1-\ell_1^2-\ell_2^2)\ge0.
\]

### 4.2 Conditional Gaussianity with random mean

Define the two primitive loadings of the linear combination:

\[
g_1(x)=p+qf_c(x),
\qquad
g_2(x)=q s_c(x).
\]

Set

\[
g(x)=(g_1(x),g_2(x))^\top,
\qquad
r(x)=C^\top g(x).
\]

The common-factor loading and residual variance are

\[
h(x)=\ell_1g_1(x)+\ell_2g_2(x),
\]

\[
\Gamma(x)=Q(x)-h(x)^2
=g(x)^\top(I_2-\ell\ell^\top)g(x)\ge0.
\]

Then

\[
dZ_t=h(X_t)dW_t^0+r(X_t)^\top dU_t,
\qquad
\|r(x)\|^2=\Gamma(x).
\]

**Theorem 4.2 (leveraged conditional Gaussian law).** Conditional on the
entire \(X\)-path,

\[
\boxed{
Z_T\mid X_{[0,T]}
\sim N\!\left(
z_0+\int_0^T h(X_t)dW_t^0,
\int_0^T\Gamma(X_t)dt
\right).
}
\]

The whole conditional process is Gaussian with mean curve

\[
M_t=z_0+\int_0^t h(X_s)dW_s^0
\]

and covariance

\[
\operatorname{Cov}(Z_s,Z_t\mid X)
=\int_0^{s\wedge t}\Gamma(X_r)dr.
\]

**Proof.** Given \(X\), the invertibility of the factor SDE with \(\nu>0\)
determines the path of \(W^0\). The first integral is therefore fixed under
the conditioning. The second is an Itô integral with deterministic
conditional integrand against Brownian motion independent of \(X\), hence is
Gaussian with the displayed covariance. \(\square\)

Thus leverage does not destroy conditional Gaussianity. Independence in the
earlier phases was exactly the condition that made the conditional mean zero.

### 4.3 Itô gauge and endpoint--additive representation

Let \(G'(x)=h(x)/\nu\). For the bounded map, one explicit primitive is

\[
\boxed{
G(x)=\frac1\nu\left[
\ell_1px
+q\ell_1\sqrt{x^2+c^2}
+q\ell_2c\,\operatorname{asinh}(x/c)
\right].
}
\]

Its derivative uses

\[
h'(x)=
\frac{qc(\ell_1c-\ell_2x)}{(x^2+c^2)^{3/2}}.
\]

Define

\[
K(x)=\frac{\mu}{\nu}h(x)+\frac{\nu}{2}h'(x).
\]

Itô's formula yields

\[
\boxed{
\int_0^T h(X_t)dW_t^0
=G(X_T)-G(x_0)-\int_0^TK(X_t)dt.
}
\]

Therefore the leveraged conditional mean depends on one endpoint and one
additive functional, while the conditional variance is a second additive
functional:

\[
\boxed{
Z_T\mid X
\sim N\!\left(
z_0+G(X_T)-G(x_0)-\int_0^TK(X_t)dt,
\int_0^T\Gamma(X_t)dt
\right).
}
\]

### 4.4 One-dimensional characteristic-function PDE

The joint generator of \((X,Z-z_0)\) is

\[
\mathcal L
=\mu\partial_x+\frac{\nu^2}{2}\partial_{xx}
+\frac{Q(x)}2\partial_{zz}
+\nu h(x)\partial_{xz}.
\]

Fourier transformation in \(z\) gives the main closure theorem.

**Theorem 4.3 (one-dimensional leveraged transform).** Let

\[
v(\tau,x;u)=\mathbb E_{x,0}[e^{iu(Z_\tau-z_0)}].
\]

Then \(v\) solves

\[
\boxed{
\partial_\tau v
=\frac{\nu^2}{2}v_{xx}
+\bigl(\mu+iu\nu h(x)\bigr)v_x
-\frac{u^2}{2}Q(x)v,
\qquad
v(0,x;u)=1.
}
\]

The terminal characteristic function is

\[
\boxed{
\phi_Z(u)=e^{iuz_0}v(T,x_0;u).
}
\]

Equivalently, with

\[
V_u(x)=-iuK(x)-\frac{u^2}{2}\Gamma(x),
\]

let

\[
w(\tau,x;u)
=\mathbb E_x\left[
\exp\!\left(\int_0^\tau V_u(X_s)ds\right)
e^{iuG(X_\tau)}
\right].
\]

Then

\[
\partial_\tau w
=\frac{\nu^2}{2}w_{xx}+\mu w_x+V_u(x)w,
\qquad
w(0,x;u)=e^{iuG(x)},
\]

and

\[
\boxed{
\phi_Z(u)=e^{iu(z_0-G(x_0))}w(T,x_0;u).
}
\]

When \(\ell=0\), one has \(h=G=K=0\) and \(\Gamma=Q\). The equation
reduces exactly to the real-potential clock transform of Phase 8. Leverage
therefore changes the potential from real to complex, or equivalently adds a
complex drift, but it does not increase the spatial dimension of the
European transform problem.

Because

\[
0\le Q(x)\le(|p|+|q|)^2,
\]

the quadratic variation of \(Z-z_0\) is deterministically bounded. Hence all
real exponential moments of \(Z_T-z_0\) exist and satisfy the sub-Gaussian
bound

\[
\mathbb E[e^{\theta(Z_T-z_0)}]
\le
\exp\!\left(\frac{\theta^2}{2}(|p|+|q|)^2T\right).
\]

### 4.5 Leverage creates skewness

Let \(Y_t=Z_t-z_0\). The generator calculation

\[
\mathcal L(y^3)=3yQ(x)
\]

and

\[
\mathcal L^2(y^3)\big|_{(x_0,0)}
=3\nu h(x_0)Q'(x_0)
\]

gives the short-time expansion

\[
\boxed{
\mathbb E[Y_T^3]
=\frac32\nu h(x_0)Q'(x_0)T^2+o(T^2)
=3pq\nu h(x_0)f_c'(x_0)T^2+o(T^2).
}
\]

Thus generic leverage makes the terminal law asymmetric. The exact even-smile
theorem of Section 3 is restricted to the independent, centered-mixture case.
Special cancellations such as \(pq=0\) or \(h(x_0)=0\) can remove the leading
term, but do not create a general symmetry theorem.

### 4.6 What leverage genuinely breaks

Conditional on \(X\), the entire process satisfies the equality in law

\[
(Z_t\mid X)
\ \stackrel{d}{=}\
(z_0+M_t(X)+B_{J_t(X)}\mid X),
\]

where

\[
M_t=G(X_t)-G(x_0)-\int_0^tK(X_s)ds,
\qquad
J_t=\int_0^t\Gamma(X_s)ds,
\]

and \(B\) is conditionally independent Brownian motion. An upper barrier
event becomes

\[
\sup_{v\le J_T}
\left\{B_v+M_{J^{\leftarrow}(v)}\right\}\ge d-z_0,
\]

where \(J^{\leftarrow}\) is the generalized right-continuous inverse. In the
strictly nondegenerate case \(\ell_1^2+\ell_2^2<1\) and \(Q(X_t)>0\), it is
the ordinary inverse.

This is a Brownian moving-boundary problem driven by the whole factor path.
The Phase 6 reflection formula depending only on the terminal clock therefore
fails generically. The exact boundary is:

- leveraged Europeans remain one-dimensional after Fourier transformation;
- leveraged linear-combination barriers are generically two-state
  \((X,Z)\) problems;
- the original scalar-clock barrier collapse is recovered when the random
  conditional mean vanishes.

---

## 5. Phase-Gram has a stationary law, exact determinant laws, and exact boundary times

### 5.1 Construction

For \(n\) assets let

\[
d=\frac{n(n-1)}2
\]

and let \(\theta_{ij}\), \(i>j\), be the triangular angles. The lower
triangular factor has entries

\[
B_{i,k}
=\cos\theta_{ik}\prod_{m<k}\sin\theta_{im},
\qquad k<i,
\]

\[
B_{i,i}=\prod_{m<i}\sin\theta_{im},
\]

with \(B_{1,1}=1\), and

\[
R=B B^\top.
\]

Let the angles evolve independently:

\[
d\theta_j(t)=\sigma_jdW_j(t),
\qquad \sigma_j>0,
\qquad j=1,\ldots,d.
\]

Unless a stationary random initialization is explicitly specified, the
initial angle vector is deterministic. All driving Brownian motions are
independent of any random initial state.

### 5.2 Determinant factorization and finite-time moments

**Theorem 5.1 (exact determinant process).** For every angle configuration,

\[
\boxed{
\det R_t
=\prod_{j=1}^d\sin^2\theta_j(t).
}
\]

For every positive integer \(m\),

\[
\boxed{
\mathbb E[(\det R_t)^m]
=\prod_{j=1}^d M_{m,j}(t),
}
\]

where

\[
\boxed{
M_{m,j}(t)
=\frac1{4^m}\binom{2m}{m}
+\frac{2}{4^m}
\sum_{r=1}^m
(-1)^r\binom{2m}{m-r}
e^{-2r^2\sigma_j^2t}
\cos(2r\theta_j(0)).
}
\]

The displayed unconditional product formula uses the deterministic initial
angles just specified. For a general random initial vector independent of the
future Brownian increments, the conditional formula is the same and

\[
\mathbb E[(\det R_t)^m]
=\mathbb E\!\left[\prod_{j=1}^dM_{m,j}(t;\theta_j(0))\right].
\]

**Proof.** Since \(B\) is lower triangular,

\[
\det R=(\det B)^2
=\prod_{i=2}^nB_{ii}^2
=\prod_{i=2}^n\prod_{j<i}\sin^2\theta_{ij}.
\]

Independence factorizes determinant moments. The finite Fourier identity

\[
\sin^{2m}x
=\frac1{4^m}\binom{2m}{m}
+\frac{2}{4^m}\sum_{r=1}^m
(-1)^r\binom{2m}{m-r}\cos(2rx)
\]

and

\[
\mathbb E[\cos(2r\theta_j(t))]
=e^{-2r^2\sigma_j^2t}\cos(2r\theta_j(0))
\]

give the result. \(\square\)

In particular,

\[
\mathbb E[\det R_t]
=\prod_{j=1}^d
\frac{1-e^{-2\sigma_j^2t}\cos(2\theta_j(0))}{2}.
\]

### 5.3 Quotient stationarity

The unwrapped angle vector has no stationary probability law on
\(\mathbb R^d\). The matrix does not see the unwrapped lift: it is a periodic
function of the angles. Modulo \(2\pi\), every positive-volatility angle is
Brownian motion on a circle and converges to the uniform law.

**Theorem 5.2 (stationary Phase-Gram matrix law).** Let \(U_1,\ldots,U_d\)
be independent uniform random variables on \([0,2\pi)\), and let

\[
\Pi_n=\operatorname{Law}(R(U_1,\ldots,U_d)).
\]

Then

\[
\boxed{R_t\ \Longrightarrow\ \Pi_n\qquad(t\to\infty).}
\]

If the initial wrapped angles are independent uniform variables and are
independent of the driving Brownian motions, the whole matrix process is
stationary. Moreover,

\[
\boxed{\mathbb E_{\Pi_n}[R]=I_n.}
\]

**Proof.** Independent Brownian motions modulo \(2\pi\) converge to product
Haar measure on the torus. The Gram map is continuous and periodic, so the
continuous-mapping theorem gives convergence of its pushforward. Under Haar
initialization, stationarity of the torus process transfers to the matrix
process. Every off-diagonal Gram entry is a sum of products containing an
independent sine or cosine factor with zero Haar mean, while diagonal entries
equal one. \(\square\)

Thus the earlier statement that long-horizon matrix behavior is diffusive is
incorrect. Only the chosen unwrapped angle lift diffuses. The observable
matrix has a compact stationary law.

### 5.4 Stationary determinant distribution

Under \(\Pi_n\),

\[
Y_j=\sin^2U_j
\sim\operatorname{Beta}\!\left(\frac12,\frac12\right)
\]

independently. Therefore

\[
\boxed{
\det R\ \stackrel{d}{=}\ \prod_{j=1}^dY_j.
}
\]

Its Mellin transform is

\[
\boxed{
\mathbb E_{\Pi_n}[(\det R)^z]
=\left[
\frac{\Gamma(z+\tfrac12)}
{\sqrt\pi\,\Gamma(z+1)}
\right]^d,
\qquad \operatorname{Re}z>-\frac12.
}
\]

The exact log-determinant moments are

\[
\boxed{
\mathbb E_{\Pi_n}[\log\det R]=-2d\log2,
\qquad
\operatorname{Var}_{\Pi_n}(\log\det R)=\frac{d\pi^2}{3}.
}
\]

Also,

\[
\boxed{
\mathbb E_{\Pi_n}[\det R]=2^{-d},
\qquad
\exp(\mathbb E\log\det R)=4^{-d}.
}
\]

Hence a stationary Phase-Gram matrix has identity mean but is typically close
to singular in high dimension. The mean determinant is itself exponentially
small, and the geometric-mean determinant is exponentially smaller again.

For a nested sequence of independent stationary angles,

\[
\boxed{
\frac{\log\det R+2d\log2}{\pi\sqrt{d/3}}
\Longrightarrow N(0,1)
\qquad(d\to\infty),
}
\]

by the classical central limit theorem.

### 5.5 Exact first-singularity law

Assume the initial angle vector is deterministic and \(\det R_0>0\). Let

\[
x_j=\theta_j(0)\bmod\pi\in(0,\pi)
\]

and define

\[
\tau_\partial=\inf\{t>0:\det R_t=0\}.
\]

For a single angle, let \(\tau_j\) be its first exit from the adjacent
interval between multiples of \(\pi\). The killed heat kernel on
\((0,\pi)\) gives

\[
S_j(t):=\mathbb P(\tau_j>t)
=\frac4\pi
\sum_{m=0}^\infty
\frac{\sin((2m+1)x_j)}{2m+1}
\exp\!\left[-\frac12(2m+1)^2\sigma_j^2t\right].
\]

**Theorem 5.3 (boundary-hitting distribution).** The first singularity time
satisfies

\[
\boxed{
\mathbb P(\tau_\partial>t)
=\prod_{j=1}^dS_j(t).
}
\]

In particular,

\[
\boxed{\tau_\partial<\infty\quad\text{almost surely}.}
\]

Indeed, every angle Brownian motion hits multiples of \(\pi\) recurrently,
so the matrix hits the elliptope boundary infinitely often. It is positive
definite at every fixed deterministic time almost surely, but not pathwise
confined to the interior.

---

## 6. The nonautonomous Feynman--Kac issue is operator ordering, not failure of the backward theorem

### 6.1 Correct two-time evolution

Let

\[
\mathcal A_t=\mathcal L_t+V_t
\]

be a time-dependent tilted generator, and let \(Q_{s,t}\) denote its evolution
family on test functions:

\[
Q_{s,t}g(x)
=\mathbb E_{s,x}\left[
e^{\int_s^tV_r(X_r)dr}g(X_t)
\right].
\]

The standard backward Feynman--Kac equation is

\[
\boxed{
-\partial_sQ_{s,t}=\mathcal A_sQ_{s,t},
\qquad
Q_{t,t}=I.
}
\]

It remains valid for nonautonomous coefficients. Differentiation in the
terminal time instead gives the right-ordered identity

\[
\boxed{
\partial_tQ_{0,t}=Q_{0,t}\mathcal A_t.
}
\]

The generally false step is replacing the right action by left action:

\[
Q_{0,t}\mathcal A_t
\not=\mathcal A_tQ_{0,t}.
\]

### 6.2 Exact commutator defect

**Theorem 6.1 (horizon-equation defect).** On a common invariant core on
which the following operations are justified,

\[
\boxed{
(\partial_t-\mathcal A_t)Q_{0,t}g
=[Q_{0,t},\mathcal A_t]g
=\int_0^t
Q_{0,r}[\mathcal A_r,\mathcal A_t]Q_{r,t}g\,dr.
}
\]

**Proof.** The first equality follows from
\(\partial_tQ_{0,t}=Q_{0,t}\mathcal A_t\). For the second, differentiate

\[
F(r)=Q_{0,r}\mathcal A_tQ_{r,t}.
\]

Using

\[
\partial_rQ_{0,r}=Q_{0,r}\mathcal A_r,
\qquad
\partial_rQ_{r,t}=-\mathcal A_rQ_{r,t},
\]

one obtains

\[
F'(r)=Q_{0,r}[\mathcal A_r,\mathcal A_t]Q_{r,t}.
\]

Integrating from zero to \(t\) yields the formula. \(\square\)

Pairwise commutation of the generators is therefore sufficient for the naive
one-parameter horizon equation. The displayed defect identity is the exact
statement used here; no general converse from an integrated zero defect to
pairwise commutation is asserted.

### 6.3 Exact Gaussian counterexample and classification

Consider

\[
dX_t=\mu(t)dt+\sigma(t)dW_t,
\qquad
J_T=\int_0^TX_sds,
\]

and a linear potential \(V(x)=\lambda x\). Stochastic Fubini gives

\[
J_T
=xT+\int_0^T(T-r)\mu(r)dr
+\int_0^T(T-r)\sigma(r)dW_r.
\]

Hence the true transform is

\[
\boxed{
\mathbb E_x[e^{\lambda J_T}]
=\exp\!\left(
\lambda\left[xT+\int_0^T(T-r)\mu(r)dr\right]
+\frac{\lambda^2}{2}
\int_0^T(T-r)^2\sigma(r)^2dr
\right).
}
\]

The misordered initial-value PDE

\[
\partial_Tu
=\mu(T)u_x+\frac12\sigma(T)^2u_{xx}+\lambda xu,
\qquad u(0,x)=1,
\]

instead gives

\[
\boxed{
\widetilde u(T,x)
=\exp\!\left(
\lambda\left[xT+\int_0^Tr\mu(r)dr\right]
+\frac{\lambda^2}{2}\int_0^Tr^2\sigma(r)^2dr
\right).
}
\]

These two formulas agree for all \(T\) and all \(\lambda\) if and only if

\[
\mu(t)=\mu_0,
\qquad
\sigma(t)^2=a_0
\]

almost everywhere. Indeed, equality of either the linear or quadratic
coefficient requires

\[
T\int_0^Ta(r)dr=2\int_0^Tra(r)dr
\]

for \(a=\mu\) or \(a=\sigma^2\), and this integral identity for every \(T\)
forces \(a\) to be constant almost everywhere.

The proper backward solution retains both calendar times:

\[
u(s,x;T)
=\exp\!\left(
\lambda\left[(T-s)x+\int_s^T(T-r)\mu(r)dr\right]
+\frac{\lambda^2}{2}\int_s^T(T-r)^2\sigma(r)^2dr
\right),
\]

and satisfies

\[
\partial_su+\mathcal A_su=0,
\qquad
u(T,x;T)=1.
\]

Thus the Phase 7 computational correction to a forward tilted density was
valid, but the conceptual statement must be narrowed: backward
Feynman--Kac did not fail; a time-homogeneous one-parameter operator ordering
was used in a nonautonomous problem.

---

## 7. The exact scale-identifiability group

Fix an observation horizon \([0,T_*]\). Let
\(F:\mathbb R\to(-1,1)\) be a homeomorphism and

\[
\rho_t=F(X_t/c),
\qquad c>0,
\]

with

\[
X_t=x_0+\int_0^t\mu(r)dr+\int_0^t\sigma(r)dW_r.
\]

Assume deterministic \(x_0\), \(\mu\in L^1[0,T_*]\), and nonnegative
deterministic \(\sigma\in L^2[0,T_*]\). Equality of path laws below means
equality as probability laws on \(C([0,T_*])\).

**Theorem 7.1 (maximal Gaussian scale symmetry).** Two parameter sets produce
the same path law for \(\rho\) if and only if

\[
\boxed{
\frac{x_0}{c}=\frac{x_0'}{c'},
\qquad
\frac{\mu(t)}{c}=\frac{\mu'(t)}{c'}\quad\text{a.e.},
\qquad
\frac{\sigma(t)^2}{c^2}
=\frac{\sigma'(t)^2}{c'^2}\quad\text{a.e.}
}
\]

The last equality is equivalently \(\sigma/c=\sigma'/c'\) under the stated
nonnegative-volatility convention. If signed diffusion coefficients are
allowed, only their squares are identified and an additional measurable sign
gauge remains.

For constant coefficients, the positive scaling orbit is

\[
\boxed{
(x_0,c,\mu,\sigma)
\longmapsto
(\lambda x_0,\lambda c,\lambda\mu,\lambda\sigma),
\qquad \lambda>0.
}
\]

**Proof.** Applying \(F^{-1}\) to the observed path shows that its law is
exactly the law of \(Y=X/c\). The latter is a Gaussian process with mean

\[
\frac{x_0}{c}+\int_0^t\frac{\mu(r)}{c}dr
\]

and covariance

\[
\operatorname{Cov}(Y_s,Y_t)
=\int_0^{s\wedge t}\frac{\sigma(r)^2}{c^2}dr.
\]

Equality of Gaussian path laws is equivalent to equality of these mean and
covariance functions, which gives the stated conditions. Simultaneous
scaling also produces a pathwise equality under the same Brownian path.
\(\square\)

The earlier written action

\[
(c,\mu,\sigma)
\mapsto
(\lambda c,\mu/\lambda,\sigma/\lambda)
\]

is not an invariance. For example, starting from \(c=\sigma=1\) and taking
\(\lambda=2\) changes normalized volatility from \(1\) to \(1/4\), hence
changes normalized variance at time \(t\) from \(t\) to \(t/16\).

The identified ratios \(\mu/c\) and \(\sigma/c\) in Phase 9 were correct;
the displayed group action was not.

---

## 8. The joint endpoint--clock law is a family of one-dimensional tilted kernels

Let

\[
A_t=\int_0^tf_c(X_s)ds
\]

and define the tilted endpoint kernel by

\[
K_\xi(t;x,y)dy
=\mathbb E_x\left[e^{i\xi A_t};X_t\in dy\right].
\]

For constant Gaussian coefficients it satisfies

\[
\boxed{
\partial_tK_\xi
=-\mu\partial_yK_\xi
+\frac{\nu^2}{2}\partial_{yy}K_\xi
+i\xi f_c(y)K_\xi,
\qquad
K_\xi(0;x,y)=\delta_x(y).
}
\]

**Theorem 8.1 (joint endpoint--clock density).** Assume \(\nu>0\); the
coefficients are \(C^\infty\) with bounded derivatives; and the diffusion is
nonexplosive. For every \(T>0\), the pair \((A_T,X_T)\) has a smooth density,
and

\[
\boxed{
p_{A_T,X_T}(a,y)
=\frac1{2\pi}\int_{\mathbb R}
e^{-i\xi a}K_\xi(T;x_0,y)d\xi,
}
\]

with Fourier inversion understood in the distributional sense. Pointwise
Fourier inversion additionally requires, for example,
\(\xi\mapsto K_\xi(T;x_0,y)\in L^1(\mathbb R)\), which is not assumed in the
theorem. Consequently,

\[
\boxed{
p_{A_T,\rho_T}(a,r)
=\frac{c}{(1-r^2)^{3/2}}
p_{A_T,X_T}\!\left(
a,\frac{cr}{\sqrt{1-r^2}}
\right).
}
\]

**Proof of smoothness.** In coordinates \((x,a)\), the diffusion vector field
and drift vector field are

\[
V_1=\nu\partial_x,
\qquad
V_0=\mu\partial_x+f_c(x)\partial_a.
\]

Their bracket contains

\[
[V_1,V_0]=\nu f_c'(x)\partial_a,
\]

and

\[
f_c'(x)=\frac{c^2}{(x^2+c^2)^{3/2}}>0.
\]

Thus \(V_1\) and \([V_1,V_0]\) span both state directions at every finite
\(x\). Hörmander's condition holds, giving a smooth density. The transform
formula is the forward Feynman--Kac equation followed by Fourier inversion.
\(\square\)

This closes the earlier endpoint-plus-occupation deferral without solving a
two-spatial-dimensional PDE. One solves a one-dimensional family indexed by
Fourier frequency. Indicator corridor occupation is different: because the
indicator is constant on open regions, paths can remain entirely outside or
inside the corridor, producing singular masses at zero or \(T\). Those atoms
must be separated before inversion.

---

## 9. Spectrally one-sided Levy drivers retain exact barrier transforms

Let \(X\) be a spectrally negative Levy process that is not the negative of a
subordinator. Write \(x=X_0=f_c^{-1}(\rho_0)\). Its Laplace exponent is

\[
\psi(\theta)=\log\mathbb E[e^{\theta(X_1-X_0)}],
\qquad \theta\ge0,
\]

and let \(\Phi(\delta)\) be the largest nonnegative solution of

\[
\psi(\Phi(\delta))=\delta,
\qquad \delta\ge0.
\]

Let \(\rho_t=f_c(X_t)\), and let \(r^*>\rho_0\) with

\[
b=f_c^{-1}(r^*).
\]

Define

\[
\tau_b^+=\inf\{t\ge0:X_t\ge b\},
\qquad
\tau_a^-=\inf\{t\ge0:X_t\le a\}.
\]

Monotonicity gives the pathwise identity

\[
\tau_{r^*}^\rho
=\inf\{t:\rho_t\ge r^*\}
=\inf\{t:X_t\ge b\}
=\tau_b^+.
\]

**Theorem 9.1 (bounded-factor Levy fluctuation formulas).** Under the standard
non-monotone hypotheses for spectrally negative fluctuation theory, for
\(\delta\ge0\) and \(x<b\),

\[
\boxed{
\mathbb E_x[e^{-\delta\tau_{r^*}^\rho};\tau_{r^*}^\rho<\infty]
=e^{-\Phi(\delta)(b-x)}.
}
\]

For \(a<x<b\), define the \(\delta\)-scale function by

\[
\int_0^\infty e^{-\theta y}W^{(\delta)}(y)dy
=\frac1{\psi(\theta)-\delta},
\qquad \theta>\Phi(\delta).
\]

Then

\[
\boxed{
\mathbb E_x[e^{-\delta\tau_b^+};\tau_b^+<\tau_a^-]
=\frac{W^{(\delta)}(x-a)}{W^{(\delta)}(b-a)}.
}
\]

Writing

\[
Z^{(\delta)}(x)=1+\delta\int_0^xW^{(\delta)}(y)dy,
\]

the complementary lower-exit transform is

\[
\boxed{
\mathbb E_x[e^{-\delta\tau_a^-};\tau_a^-<\tau_b^+]
=Z^{(\delta)}(x-a)
-Z^{(\delta)}(b-a)
\frac{W^{(\delta)}(x-a)}{W^{(\delta)}(b-a)}.
}
\]

Thus Phase 11's reflection principle is indeed lost under jumps, but exact
barrier transforms are not universally lost. They survive for spectrally
one-sided drivers through the fluctuation-theory scale-function algebra.
For two-sided VG or NIG drivers, this simplification does not apply directly.

---

## 10. What is genuinely retained for Phase 14

### 10.1 Major results

1. **Exact variance-mixture smile theorem.** The ATM level and curvature are
   exact functions of \(\mathbb E\sqrt V\) and
   \(\mathbb E[V^{-1/2}]\). This both proves the opposite local
   spread/basket curvatures and corrects the ATM mean-clock claim.

2. **Leverage closure.** Brownian leverage preserves conditional Gaussianity
   and one-dimensional European transform pricing. It introduces a random
   conditional mean, a complex Feynman--Kac potential, and generic skewness.
   The true failure boundary is barrier reflection, not terminal European
   tractability.

3. **Phase-Gram quotient theory.** The matrix has a stationary law, an exact
   determinant Mellin transform, explicit log-determinant asymptotics, and an
   exact first-boundary-hitting law. Mean identity coexists with exponential
   typical near-singularity in dimension.

### 10.2 Necessary mathematical repairs

4. **Scale symmetry.** The identified ratios were right, but the group action
   must scale \(c,x_0,\mu,\sigma\) in the same direction.

5. **Nonautonomous Feynman--Kac.** The two-time backward theorem remains
   correct. The error is reversed operator ordering in a one-parameter horizon
   equation, measured exactly by a commutator integral.

### 10.3 Exact extensions worth keeping

6. **Joint endpoint--clock density.** Hypoellipticity and Fourier-tilted
   one-dimensional kernels solve the smooth joint-law problem.

7. **Levy barriers.** Spectrally one-sided drivers retain exact Laplace and
   two-sided-exit transforms through scale functions.

### 10.4 Ideas rejected for this phase

The following are not promoted to Phase 14 headline results:

- sparse-grid acceleration by itself;
- higher-order time stepping for the Levy PIDE by itself;
- additional calibration or attenuation simulations;
- generic angle-volatility fitting;
- more payoff examples without a new theorem;
- Phase 1--4 exponential or polar identities already known or already
  completed; and
- coordinate changes whose only content is invertibility.

---

## 11. New open problems created by the results

The surviving theorems expose sharper questions than the earlier broad
limitations.

1. **Leveraged barrier classification.** Classify all nonzero leverage
   loadings for which the conditional moving boundary becomes affine in the
   residual Brownian clock. Generic leverage fails; exceptional solvable
   families may exist.

2. **Full implied-correlation derivative hierarchy.** Determine which
   positive and negative moments of \(\sqrt V\) appear in the fourth and
   higher ATM derivatives, and whether the full centered mixture law is
   identifiable from one normal-implied smile.

3. **Phase-Gram quotient generator.** Derive the closed matrix generator and
   exact transition density on the positive-definite elliptope, including the
   many-to-one angular fibers and boundary singularities.

4. **Conditioning near singularity.** Use the product-Beta determinant law to
   derive sharp smallest-eigenvalue and condition-number asymptotics.

5. **Leveraged endpoint--clock kernels.** The gauge representation contains
   the endpoint \(X_T\) and two additive functionals. Determine whether a
   matrix-valued tilted kernel yields stable inversion for the full conditional
   law.

6. **Omega-scale bounded factors.** Combine Levy scale functions with the
   state-dependent clock potential to obtain joint barrier--occupation
   transforms.

7. **Maximal symmetry under observation noise.** Extend Theorem 7.1 to
   state-space observation channels and prove exactly which external scale
   measurements break the orbit.

---

## 12. Final conclusion

The most important Phase 14 lesson is that several earlier frontiers were
drawn at the wrong mathematical boundary.

Independence is not required for conditional Gaussianity or one-dimensional
European transforms; it is required for a zero conditional mean and the pure
variance-mixture clock. Unwrapped Gaussian angles are not stationary, but
their periodic Gram image is. Backward Feynman--Kac does not fail under
calendar-time coefficients; a time-homogeneous operator ordering fails.
Jumps kill reflection, but spectrally one-sided fluctuation identities survive.

At the same time, exact calculations expose two consequential corrections.
The scale-equivalence action must be simultaneous scaling, and ATM implied
correlation is not the mean correlation clock. The latter error conceals a
stronger theorem: the ATM Jensen wedge and the opposite spread/basket local
curvatures are exact measurements of clock dispersion.

The central new equation of this phase is therefore not one isolated formula
but a corrected closure principle:

\[
\boxed{
\text{bounded factor}
+\text{Brownian leverage}
+\text{linear asset combination with a terminal European payoff}
\Longrightarrow
\text{one-dimensional complex Feynman--Kac transform}.
}
\]

Together with the exact variance-mixture smile identities and the Phase-Gram
determinant theory, this supplies a mathematically substantive next phase for
the research program.
