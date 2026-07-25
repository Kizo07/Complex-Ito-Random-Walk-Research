# Representing Brownian Motion in a Single Euler Form

**Question.** Given $Z_t = Z_0 + at + bW_t$, can it be written as
$$Z_t \;=\; Z_0\, r(\theta_t)\, e^{i\theta_t}$$
with $\theta_t$ the *only* stochastic variable and $r$ a deterministic function of $\theta$ (or a constant)?

**Date:** July 24, 2026 · **Companion to:** `possible_solution.md`, Phase 3/Phase 4 complex-GBM project

---

## 0. Executive summary

**Verdict on the attached `possible_solution.md`: the mathematics is correct.** Every symbolic
identity in it was verified independently (§11). The secant construction, the general line formula
$r(\theta)=\sin\phi/\sin(\phi-\theta)$, the phase SDE in both Itô and Stratonovich form, the exact
transition kernel, the Cayley/constant-radius section, and the two necessary conditions
$a/b\in\mathbb{R}$, $b/Z_0\notin\mathbb{R}$ are all right.

Three things are missing or wrong, in ascending order of importance:

1. **The impossibility proof in its §8 has a genuine gap** (§4 below). The ray-counting argument
   shows a polar graph cannot *contain* a 2-D region, but the hypothesis only supplies that the
   graph contains almost every point of each line $L_t$. Closing that gap needs a measure-theoretic
   step, and therefore a measurability hypothesis on $r$ that the document never states.

2. **The phase range is never stated.** For the additive family $\theta_t$ is confined for all time
   to an open interval of length exactly $\pi$ (§3.3). The phase can *never wind*. That is a
   structural limitation of the whole additive family, and it is the thing that should have
   motivated looking elsewhere.

3. **The best answer to the question is in the document but goes unrecognized.** Its §13 lists
   $e^{(\alpha+i\beta)x}$ in a trade-off table and moves on. That map *is* the requested form, with
   $r(\theta)=e^{(\alpha/\beta)\theta}$ and $\theta_t$ **equal to a Brownian motion** — no
   arctangent, no bounded phase, free winding (§5). It is also exactly the Phase 3 family from the
   earlier paper, meaning **Phase 3 already solved this problem**, and Phase 4's release of
   $\omega$ and $\beta$ is precisely the step that destroys the property (§5.4).

**What I add beyond the document:**

- A single master criterion covering every case at once: *argument monotonicity* (§2).
- A repaired, rigorous impossibility theorem, with the measurability hypothesis made explicit and
  its necessity discussed (§4).
- The logarithmic-spiral family, where the phase is literally Brownian motion (§5).
- **A uniqueness classification** (§6): straight lines and logarithmic spirals are the *only* two
  polar-graph families compatible with constant-coefficient dynamics. This closes the problem — it
  is no longer "here are some constructions," it is "here is the complete list."
- A design dictionary letting you pick any $r(\theta)$ and read off the resulting process (§7).
- A constructive fallback for the impossible case that keeps one stochastic variable (§8).

---

## 1. Precise statement of the problem

Fix $Z_0\in\mathbb{C}\setminus\{0\}$. We seek a **Borel** function $r:\mathbb{R}\to[0,\infty)$ and a
real-valued process $(\theta_t)$ such that, almost surely for every $t$,

$$Z_t \;=\; Z_0\, r(\theta_t)\, e^{i\theta_t}. \tag{1}$$

Three points make this precise, and the document is silent on all three:

**(a) $\theta$ is an unwrapped lift, not a principal argument.** $\theta_t$ ranges over $\mathbb{R}$,
not $(-\pi,\pi]$. This matters: for the spiral family of §5 the curve winds infinitely often, so
$r$ is single-valued as a function of the *lift* but multivalued as a function of the geometric
angle. For the line family of §3 the two coincide.

**(b) Equation (1) forces $\arg F(\theta)=\theta$**, where $F(\theta):=r(\theta)e^{i\theta}$. So the
range of $F$ is a **polar graph** — a curve specified in polar coordinates as $r=r(\theta)$. This is
the entire content of the constraint, and it is what makes the problem nontrivial. (Without the
normalisation $\arg F(\theta)=\theta$ — i.e. if $r$ were allowed to be complex — the problem is
vacuous: $\mathbb{R}$ and $\mathbb{C}$ have the same cardinality, so a set-theoretic bijection
$F$ exists and (1) holds for *any* process. The polar normalisation is doing all the work.)

**(c) $r$ must be Borel.** Otherwise $r(\theta_t)$ need not be a random variable and (1) is not even
a well-formed statement. §4 shows this hypothesis is not cosmetic.

Write throughout
$$\alpha=\frac{a}{Z_0},\qquad c=\frac{b}{Z_0}=\rho e^{i\phi},\qquad
\zeta_t=\frac{Z_t}{Z_0}=1+\alpha t+cW_t .$$

---

## 2. Master criterion: argument monotonicity

Everything below is a corollary of one observation.

> **Theorem 1 (master criterion).** Suppose $Z_t=Z_0 f(S_t)$ where $S$ is a real process whose range
> is an interval $I$ with $\mathbb{P}(S_t\in J)>0$ for every open $J\subseteq I$, and
> $f:I\to\mathbb{C}\setminus\{0\}$ is continuous. Let $\vartheta:I\to\mathbb{R}$ be a continuous
> argument lift of $f$, so $f(s)=|f(s)|e^{i\vartheta(s)}$.
>
> Then a representation (1) exists **iff $\vartheta$ is injective** (equivalently, strictly
> monotone), in which case
> $$\theta_t=\vartheta(S_t),\qquad r=|f|\circ\vartheta^{-1}.$$

*Proof.* ($\Leftarrow$) Immediate: $Z_0 r(\theta_t)e^{i\theta_t}=Z_0|f(S_t)|e^{i\vartheta(S_t)}=Z_0f(S_t)$.
($\Rightarrow$) If $\vartheta(s_1)=\vartheta(s_2)$ with $|f(s_1)|\neq|f(s_2)|$, then by continuity and
the support assumption both values are attained with positive probability, and $r$ would have to take
two values at one point. $\square$

This immediately reduces the problem to: **is the argument of the driving map monotone?** Three
applications:

| $f(s)$ | curve | $\vartheta(s)$ | monotone? |
|---|---|---|---|
| $1+cs$, $\operatorname{Im}c\neq0$ | line missing origin | $\arg(1+cs)$ | yes — §3 |
| $1+cs$, $c\in\mathbb{R}$ | line through origin | jumps between two values | **no** |
| $e^{Bs}$, $B=\sigma+i\beta$, $\beta\neq0$ | logarithmic spiral | $\beta s$ | yes — §5 |

The second row is the reason a real Brownian motion cannot be represented directly: its motion is
purely radial, so the phase carries only a sign.

The requirement that $f$ carry **no $t$** is separate and is what forces the collinearity conditions.

---

## 3. Case A — the additive process: lines and the secant family

### 3.1 Existence

$Z_t=Z_0+at+bW_t$ has, at each fixed $t$, support equal to the full line
$L_t=\{Z_0+at+bw:w\in\mathbb{R}\}$. For a single $t$-free curve to contain all of them, all $L_t$ must
coincide, i.e. $a=\lambda b$ for some $\lambda\in\mathbb{R}$. Then with $S_t=\lambda t+W_t$,

$$\zeta_t = 1 + cS_t,$$

and by Theorem 1 we need $\operatorname{Im}c\neq0$.

> **Theorem 2.** For $b\neq0$, representation (1) exists **iff**
> $$\operatorname{Im}(a\bar b)=0 \quad\text{and}\quad \operatorname{Im}(b\bar Z_0)\neq0,$$
> i.e. $a/b\in\mathbb{R}$ and $b/Z_0\notin\mathbb{R}$. This matches the document's conditions.

### 3.2 Explicit form

$$\boxed{\;Z_t=Z_0\,\frac{\sin\phi}{\sin(\phi-\theta_t)}\,e^{i\theta_t},\qquad
\theta_t=\arg\!\left(1+cS_t\right),\qquad c=\rho e^{i\phi}\;}$$

with inverse $S_t=\dfrac{\sin\theta_t}{\rho\sin(\phi-\theta_t)}$. Verified to $4.4\times10^{-14}$
relative error over 2000 random parameter draws (§11).

An equivalent perpendicular-foot form, sometimes more convenient:
$$r(\theta)=\frac{d}{\cos(\theta-\varphi)},\qquad
d=\frac{|\operatorname{Im}c|}{|c|},\qquad \varphi=\arg\!\big(-i\operatorname{Im}(c)\,c\big),$$
where $d$ is the distance from the origin to the line and $\varphi$ the angle of the perpendicular
foot. The canonical normalisation $c=i/c_0$ gives $\phi=\pi/2$, $d=1$, $\varphi=0$ and recovers the
document's headline result
$$1+i\tan\theta=\sec\theta\,e^{i\theta}.$$

### 3.3 The phase is trapped in a half-turn — the structural limitation

As $s$ runs over $\mathbb{R}$, $\arg(1+cs)$ traverses monotonically an open interval of length
**exactly $\pi$**:
$$\theta_t\in\begin{cases}(\phi-\pi,\ \phi) & \operatorname{Im}c>0\\[2pt] (\phi,\ \phi+\pi) & \operatorname{Im}c<0\end{cases}$$
Numerically confirmed: span $=3.141592$ against $\pi=3.141593$ for four different $c$ (§11).

Three consequences the document does not draw:

- **The phase never winds.** It cannot complete even one revolution, ever. So this representation
  can never look like "$e^{i\theta}$ going around" — it is a chart of a straight line, not a rotation.
- The endpoints are unattainable in finite time but are attained in the limit; $r(\theta)\to\infty$
  at both, corresponding to $|S_t|\to\infty$.
- The diffusion coefficient of $\theta$ vanishes quadratically at both endpoints, which is exactly
  what keeps the process inside the interval without any boundary condition.

### 3.4 Phase dynamics

With $dS_t=\lambda\,dt+\sigma\,dW_t$, set $\nu=|c|^2/\operatorname{Im}c$ and $\psi=\theta-\varphi$:

$$\boxed{\;d\theta_t=\Big[\lambda\nu\cos^2\psi_t-\sigma^2\nu^2\sin\psi_t\cos^3\psi_t\Big]dt
+\sigma\nu\cos^2\psi_t\,dW_t\;}$$

This is **autonomous and time-homogeneous** — no $t$, no $S$. In the document's normalisation
($\nu=1/c_0$, $\varphi=0$, $\lambda=\mu$) it reduces exactly to its boxed §4 equation. Verified by
Euler–Maruyama against the exact $\arg(1+cS_t)$: max error $3.7\times10^{-2}\to3.5\times10^{-3}$ as
steps go $2\,000\to128\,000$, i.e. order $\approx\tfrac12$, as expected (§11).

Stratonovich form (the document's, verified): $d\theta=\tfrac{\mu}{c_0}\cos^2\theta\,dt
+\tfrac{\sigma}{c_0}\cos^2\theta\circ dW$; the Itô–Stratonovich correction
$\tfrac12BB' = -\tfrac{\sigma^2}{c_0^2}\sin\theta\cos^3\theta$ is confirmed symbolically.

**Closed-form inverse (cleaner than the document's, and worth having):**
$$\tan(\theta_t-\varphi)=\nu\,(S_t-s_*),\qquad s_*=-\frac{\operatorname{Re}c}{|c|^2}.$$
Verified to $2.1\times10^{-13}$. In words: **the phase of an additive complex Brownian motion is the
arctangent of a drifted Brownian motion.** Correspondingly $\tan(\theta_t-\varphi)$ is, up to an
affine map, a drifted Brownian motion — which also identifies the scale function of $\theta$ as
$s(\theta)\propto e^{-(2\lambda/\nu)\tan(\theta-\varphi)}$, matching the scale function $e^{-2\lambda s}$
of $S$ as it must.

---

## 4. The impossibility theorem, done properly

The document's §8 argues: non-collinear $a,b$ make the lines sweep a 2-D region, and a polar graph
meets each ray in at most countably many points, so it cannot contain such a region.

**The first half of that is right and the second half does not connect to it.** The hypothesis
gives, for each $t$, that $C$ contains *almost every point of the line $L_t$* — not that $C$
contains the swept region. And a set meeting every ray countably *can* contain uncountably many
points of uncountably many lines, because each ray crosses each line at most once. So no
contradiction follows from ray-counting alone. Here is a proof that does close.

> **Theorem 3 (impossibility).** Let $Z_0\neq0$ and $a,b\in\mathbb{C}$ with
> $\operatorname{Im}(a\bar b)\neq0$, and $Z_t=Z_0+at+bW_t$. Then there is no **Borel**
> $r:\mathbb{R}\to[0,\infty)$ and no real-valued process $(\theta_t)$ satisfying (1) for all $t$ in
> a set $T$ of positive Lebesgue measure.

*Proof.* Let $C=\{r(\theta)e^{i\theta}:\theta\in\mathbb{R}\}$.

**Step 1: $C$ is Lebesgue-null.** $C$ is the image of $\mathbb{R}$ under a Borel map, hence analytic,
hence universally measurable. For a fixed direction $e^{i\alpha}$,
$$C\cap\{\varrho e^{i\alpha}:\varrho>0\}\subseteq\{r(\alpha+2\pi k)e^{i\alpha}:k\in\mathbb{Z}\},$$
a countable set, hence 1-D null. Fubini in polar coordinates,
$\lambda_2(C)=\int_0^{2\pi}\!\!\int_0^\infty \mathbf 1_C(\varrho e^{i\alpha})\,\varrho\,d\varrho\,d\alpha$,
gives $\lambda_2(C)=0$. Since $Z_0\neq0$, $\lambda_2(Z_0C)=0$ too.

**Step 2: randomise the time.** Let $\tau$ be uniform on $T$, independent of $W$. Then
$\mathbb{P}(Z_\tau\in Z_0C)=\frac1{|T|}\int_T\mathbb{P}(Z_t\in Z_0C)\,dt=1$.

**Step 3: $Z_\tau$ has a planar density.** The pair $(\tau,W_\tau)$ has joint density
$\frac{1}{|T|}\mathbf 1_T(t)\,\varphi_t(w)$ on $\mathbb{R}^2$. Because
$\operatorname{Im}(a\bar b)\neq0$, the map $(t,w)\mapsto Z_0+at+bw$ is an invertible real-affine map
$\mathbb{R}^2\to\mathbb{C}$, so $Z_\tau$ has a density with respect to $\lambda_2$. Hence
$\mathbb{P}(Z_\tau\in Z_0C)=0$, contradicting Step 2. $\square$

**Remark (the measurability hypothesis is load-bearing).** Step 1 is the only place regularity is
used, and it is not removable by the ray argument, for the reason given above. I do not claim a
pathological counterexample exists — only that the theorem as stated needs the hypothesis and that
the document's argument does not establish the unrestricted version.

**Numerical confirmation.** Bin $\arg\zeta$ finely and measure the relative spread of $|\zeta|$
inside each bin. If $r$ is a function of $\theta$ the spread must vanish with bin width:

| bins over $2\pi$ | collinear $a=0.7b$ | non-collinear $a=0.6,\ b=i$ |
|---|---|---|
| 180 | 0.0273 | 0.7358 |
| 720 | 0.0064 | 0.7230 |
| 2880 | 0.0014 | 0.7259 |
| 11520 | 0.00042 | 0.7518 |

The collinear column decays proportionally to bin width; the non-collinear column is flat. That is
the theorem, visible directly in the data.

### 4.1 Corollary: real Brownian motion, and constant radius

- **Real BM cannot be represented directly.** If $Z_0,a,b$ are all real, $Z_t$ lies on the real axis
  and $e^{i\theta_t}\in\{\pm1\}$, so the phase records only a sign while the magnitude varies
  continuously. A fixed non-radial complex offset is the minimal repair. (Document §9 — correct.)
- **Constant $r$ is impossible for any nondegenerate additive process**, since it would force
  $|Z_t|\equiv|Z_0|r_0$. (Document §10 — correct.) The Cayley construction of its §11 evades this
  legitimately but represents an invertible Möbius *transform* of the process, not the process; the
  document flags this honestly.

---

## 5. Case B — the multiplicative process: the answer the document walked past

### 5.1 Construction

Take the multiplicative model instead:
$$Z_t=Z_0\exp\!\big(\kappa t+BW_t\big),\qquad B=\sigma+i\beta,\ \ \beta\neq0 .$$
In the log plane $\Lambda_t=\log(Z_t/Z_0)$ the fixed-time support is the line through $\kappa t$ with
direction $B$. A polar graph in $Z$ is exactly a **graph of $\operatorname{Re}\Lambda$ over
$\operatorname{Im}\Lambda$** in the log plane. So:

- all these lines coincide iff $\kappa=\gamma B$ for some $\gamma\in\mathbb{R}$;
- the common line is a graph over the imaginary axis iff $\beta\neq0$.

Then with $S_t=\gamma t+W_t$,

$$\boxed{\;Z_t=Z_0\,e^{(\sigma/\beta)\,\theta_t}\,e^{i\theta_t},\qquad \theta_t=\beta S_t\;}$$

$$\boxed{\;r(\theta)=e^{(\sigma/\beta)\theta}\;}$$

Verified to $1.6\times10^{-15}$ relative error over 2000 random parameter draws (§11).

### 5.2 Why this is the better answer to the question as asked

| | additive (§3) | multiplicative (§5) |
|---|---|---|
| curve | straight line | logarithmic spiral |
| $r(\theta)$ | $\sin\phi/\sin(\phi-\theta)$ | $e^{(\sigma/\beta)\theta}$ |
| phase | $\arctan$ of drifted BM | **drifted BM, exactly** |
| phase SDE | nonlinear, state-dependent | $d\theta=\gamma\beta\,dt+\beta\,dW$ — constant coefficients |
| phase range | interval of length $\pi$, never winds | all of $\mathbb{R}$, winds forever |
| singularities of $r$ | two, at the interval ends | none |
| $Z$ hits $0$? | no | no |

Take $\gamma=0$, $\beta=1$:
$$\boxed{\;Z_t=Z_0\,e^{\sigma\theta_t}e^{i\theta_t},\qquad \theta_t=W_t\;}$$
The phase **is** standard Brownian motion, and the radius is a pure exponential of it. Confirmed to
wind: 15.06 rad $=2.40$ full turns over a typical path with $\beta=2$, $T=40$. This is as close as
the requested form can possibly come to the algebraic analogy $a+ib=re^{i\theta}$ — a single scalar
Gaussian coordinate, a genuine rotation, and a closed-form radius.

### 5.3 What it costs

$Z$ is no longer $Z_0+at+bW_t$; it satisfies $dZ/Z = A\,dt+B\,dW$ instead. If the additive law is
non-negotiable, §3 is the best available and its bounded phase is unavoidable. If what matters is
"one stochastic phase, deterministic radius, Euler form," §5 dominates on every axis.

### 5.4 This is Phase 3, and Phase 4 breaks it

The earlier project's Phase 3 was $Z_t=Z_0e^{(1+i\gamma)L_t}$ with $L_t=(\mu-\tfrac12\sigma^2)t+\sigma W_t$.
That is exactly $\kappa=\gamma_{\!*}B$ with $B=(1+i\gamma)\sigma$ — the condition above. So

> **Phase 3 already was a single-phase Euler representation**, with $r(\theta)=e^{\theta/\gamma}$,
> and nobody noticed.

Conversely, Phase 4's general $(\kappa,B)$ satisfies $\kappa\parallel B$ iff
$\operatorname{Im}(\kappa\bar B)=0$ iff
$$\omega=\frac{\beta}{\sigma}\Big(\mu-\tfrac12\sigma^2\Big),$$
which is precisely Phase 4's own Eq. (21). So **the "independence of $\omega$ and $\beta$" that
Phase 4 advertises as its contribution is exactly the loss of the single-phase Euler form.** This is
the same fact as the earlier review's observation that Phase 4 equals Phase 3 times a deterministic
rotation $e^{i\delta t}$: that rotation is what lifts the process off the fixed spiral onto a
$t$-dependent one.

---

## 6. Classification: these are the only two families

The constructions above are not a grab-bag. They are exhaustive.

> **Theorem 4 (rigidity).** Let $F(\theta)=r(\theta)e^{i\theta}$ with $r>0$, $C^2$, and let $\theta$
> be an Itô diffusion $d\theta=m(\theta)dt+s(\theta)dW$ with $s>0$. Set $Z_t=Z_0F(\theta_t)$. Then:
>
> **(a)** $Z$ satisfies a constant-coefficient **linear** SDE $dZ=AZ\,dt+BZ\,dW$ **iff**
> $r(\theta)=r_0e^{k\theta}$ — a logarithmic spiral — with $s$ constant, $B=(k+i)s$.
>
> **(b)** $Z$ satisfies a constant-coefficient **additive** SDE $dZ=a\,dt+b\,dW$ **iff**
> $r(\theta)=C/\sin(k-\theta)$ — a straight line.
>
> The circle $r\equiv r_0$ is the $k=0$ member of family (a), giving $dZ/Z=(im-\tfrac12s^2)dt+is\,dW$
> — constant modulus with the $-\tfrac12s^2$ Itô drift, i.e. the "pure stochastic rotation" case of
> the Phase 4 paper.

*Proof.* Itô on $Z_t=Z_0F(\theta_t)$ gives
$$dZ = Z_0\Big[F'(\theta)m(\theta)+\tfrac12F''(\theta)s(\theta)^2\Big]dt + Z_0F'(\theta)s(\theta)\,dW,$$
with $F'=(r'+ir)e^{i\theta}$ and $F''=(r''+2ir'-r)e^{i\theta}$.

(a) Linearity requires $\dfrac{F'(\theta)s(\theta)}{F(\theta)}=B$ constant. Now
$F'/F=r'/r+i$, whose imaginary part is $1$; so $s\equiv\operatorname{Im}B$ is constant and
$r'/r=\operatorname{Re}B/\operatorname{Im}B=:k$ is constant, giving $r=r_0e^{k\theta}$. Solving
$r'/r=k$ symbolically returns $r=C_1e^{k\theta}$. ✔

(b) Additivity requires $F'(\theta)s(\theta)=b/Z_0$ constant, so in particular $\arg F'$ is constant.
Writing $r'+ir=|r'+ir|e^{i\chi}$ this says $\chi+\theta\equiv k$, i.e.
$\tan(k-\theta)=r/r'$, i.e. $r'/r=\cot(k-\theta)$. Integrating, $r=C/\sin(k-\theta)$. Solving
symbolically returns $C_1\sqrt{\tan^2(k-\theta)+1}\,/\tan(k-\theta)=C_1/\sin(k-\theta)$ up to sign. ✔

Direct check of the two claims: for $r=C/\sin(k-\theta)$,
$$F'(\theta)=\frac{C e^{ik}}{\sin^2(k-\theta)},$$
whose argument is the constant $k$ — the line family is exactly the family with constant $\arg F'$.
For $r=r_0e^{k\theta}$, $F'/F=k+i$, constant — the spiral family is exactly the family with constant
$F'/F$. $\square$

This is the clean closure of the problem:

$$\boxed{\ \text{constant } \arg F' \iff \text{lines} \iff \text{additive BM};\qquad
\text{constant } F'/F \iff \text{spirals} \iff \text{geometric BM}\ }$$

Any other $r(\theta)$ — Archimedean $r=a+b\theta$, hyperbolic $r=1/\theta$, cardioid, anything — still
yields a perfectly valid one-phase process (numerically confirmed, §11), but its $Z$-dynamics will
have state-dependent, non-constant coefficients.

---

## 7. Design dictionary

Reading Theorem 4 backwards turns this into a construction tool: **pick the curve, get the process.**

$$\boxed{\;dZ_t = Z_0\Big[F'(\theta_t)m(\theta_t)+\tfrac12F''(\theta_t)s(\theta_t)^2\Big]dt
+ Z_0F'(\theta_t)s(\theta_t)\,dW_t\;}$$
$$F=re^{i\theta},\qquad F'=(r'+ir)e^{i\theta},\qquad F''=(r''+2ir'-r)e^{i\theta}$$

| chosen $r(\theta)$ | curve | resulting $Z$ | phase law |
|---|---|---|---|
| $d\sec(\theta-\varphi)$ | line | arithmetic BM $Z_0+at+bW$ | $\arctan$ of drifted BM, bounded |
| $r_0e^{k\theta}$ | log spiral | geometric BM $dZ/Z=A\,dt+B\,dW$ | drifted BM, unbounded |
| $r_0$ | circle | $dZ/Z=(im-\tfrac12s^2)dt+is\,dW$ | drifted BM |
| $a+b\theta$ | Archimedean spiral | state-dependent coefficients | free choice |
| arbitrary Borel $r>0$ | arbitrary polar graph | state-dependent coefficients | free choice |

Verified numerically for all four named rows: Euler–Maruyama on the induced $Z$-SDE reproduces
$Z_0F(\theta_T)$ to $\sim10^{-3}$ at $4\times10^5$ steps, consistent with order-$\tfrac12$
discretisation error (§11).

Note what the last row means: **every** polar graph carries a one-phase process. The classification
in §6 is not about which curves are allowed, but about which curves give *nice* dynamics. That
distinction is worth keeping straight.

---

## 8. Constructive fallback when $a\not\parallel b$

Theorem 3 forbids a $t$-free radius. But the weaker goal — *one stochastic variable* — is always
achievable, with the radius carrying explicit deterministic time dependence:

$$\boxed{\;Z_t=Z_0\,R(t,\theta_t)\,e^{i\theta_t},\qquad R(t,\theta)=\frac{d_t}{\cos(\theta-\varphi_t)}\;}$$

$$p_t=1+\alpha t,\qquad d_t=\frac{|\operatorname{Im}(p_t\bar c)|}{|c|},\qquad
\varphi_t=\arg\!\Big(i\operatorname{Im}(p_t\bar c)\,\tfrac{c}{|c|^2}\Big),$$

i.e. the polar equation of the moving line $L_t$. Verified to $1.4\times10^{-13}$ over 3000 random
$(Z_0,a,b,t)$ draws (§11).

The phase closes autonomously in $(t,\theta)$:
$$d\theta_t=\left[\frac{\operatorname{Im}(\alpha e^{-i\theta_t})}{\varrho_t}
-\frac{\operatorname{Im}(c^2e^{-2i\theta_t})}{2\varrho_t^{2}}\right]dt
+\frac{\operatorname{Im}(ce^{-i\theta_t})}{\varrho_t}\,dW_t,\qquad \varrho_t=R(t,\theta_t).$$

So the honest general statement is: **one stochastic driver always suffices; a $t$-free radius does
not.** That is a more useful conclusion than "impossible, stop."

---

## 9. Relation to the classical literature

The classical polar representation of planar Brownian motion is the **skew-product decomposition**,
which <cite index="2-1">represents the process in polar coordinates as an autonomously Markovian radial part together with an angular part that is an independent Brownian motion on the unit circle, time-changed according to the radial part</cite>. Concretely, for planar BM,
$\log Z_t=\beta_{H_t}+i\gamma_{H_t}$ with $\beta,\gamma$ independent and
$H_t=\int_0^t|Z_s|^{-2}ds$.

The contrast is exactly the point of this note:

| | classical skew-product | one-phase Euler form |
|---|---|---|
| drivers | two independent | one |
| radius vs. angle | independent | radius is a **deterministic function** of angle |
| time change | required | none |
| support at fixed $t$ | 2-D | 1-D curve |
| winding | Spitzer's $2/\log t$ Cauchy limit | $\theta_t/t\to\omega$ a.s.; CLT at rate $\sqrt t$ |

So the object here is the rank-one degeneration of the classical decomposition. That framing also
supplies a genuine theorem the Phase 4 paper asserted only via scatter plots: for the spiral family,
$\theta_t=\beta(\gamma t+W_t)$ gives immediately $\theta_t/t\to\beta\gamma$ a.s. and
$(\theta_t-\beta\gamma t)/\sqrt t\sim N(0,\beta^2)$, in sharp contrast to Spitzer's law.

**Citation correction.** The attached document's only reference is a bare ScienceDirect link
(`S0022247X14005009`) attached to the claim that Brownian motion under stereographic or Cayley-type
projection has been studied. I could not verify that this identifier supports that claim. The
appropriate classical reference is **T. K. Carne, "Brownian motion and stereographic projection,"
*Annales de l'I.H.P. Probabilités et statistiques* 21(2), 1985, 187–196.** Replace it.

---

## 10. Itemised corrections to `possible_solution.md`

| § | Issue | Severity |
|---|---|---|
| 8 | Necessity argument does not close; ray-counting does not connect to the "a.e. point of each $L_t$" hypothesis. Needs the randomised-time density argument (§4). | **major** |
| 1, 7 | Measurability of $r$ never assumed; without it (1) is not well-formed and Theorem 3 fails. | **major** |
| 3, 7 | Phase range never stated. $\theta_t$ is confined to an interval of length $\pi$ and can never wind. | **major** |
| 13 | $e^{(\alpha+i\beta)x}$ is listed in a trade-off table without recognising that it *is* the requested form, with $\theta_t$ a Brownian motion — and that it is the project's own Phase 3. | **major (missed result)** |
| — | No uniqueness/classification result; the two families are presented as constructions rather than as the complete list. | **major (missing)** |
| 6 | The "$\oplus$ phase group" is ordinary addition conjugated by $\tan$. It is correct but contentless, and the claim that it "may be more useful operationally" is not defensible — computing $\arctan(\sum\tan\theta_j)$ is strictly more work than $\sum x_j$. | moderate |
| 11 | Unverified citation; see §9 above. | moderate |
| 14 | "much stronger and cleaner foundation … than the earlier complex-GBM construction" overstates. Both are elementary polar geometry; the secant and Cayley material is textbook. | moderate |
| 7 | The branch statement "using the branch containing $\theta_0=0$" is right but should note that $\theta_0=0$ automatically since $x_0=0$, and that no branch ambiguity ever arises because the phase never crosses a cut. | minor |
| 5 | Transition density is correct; worth adding that it integrates to 1 by the substitution $u=c\tan\vartheta$ (verified symbolically). | minor |

Everything else — §§1–5, 7, 9–13 — is mathematically correct as written.

---

## 11. Verification log

All checks seeded at `20260724`; Python 3, NumPy 2.4.4, SymPy 1.14.0, SciPy 1.17.1.

**Symbolic (SymPy, exact zero residuals):**

| identity | residual |
|---|---|
| $1+i\tan\theta-\sec\theta e^{i\theta}$ | $0$ |
| $r(\theta)e^{i\theta}-(1+\rho e^{i\phi}x(\theta))$ with $r=\sin\phi/\sin(\phi-\theta)$ | $0$ |
| $f'(x)=c/(c^2+x^2)$ at $x=c\tan\theta$ minus $\cos^2\theta/c$ | $0$ |
| $f''$ at $x=c\tan\theta$ plus $2\sin\theta\cos^3\theta/c^2$ | $0$ |
| Itô–Stratonovich correction $\tfrac12BB'+\sigma^2\sin\theta\cos^3\theta/c^2$ | $0$ |
| Cayley $(1+i\tan\theta)/(1-i\tan\theta)-e^{2i\theta}$ | $0$ |
| transition density $\int p_h\,d\vartheta$ | $1$ |
| spiral $\exp((\sigma/\beta)\theta)\big|_{\theta=\beta s}-e^{\sigma s}$ | $0$ |
| $F'$ for $r=C/\sin(k-\theta)$ | $Ce^{ik}/\sin^2(k-\theta)$, constant argument |
| $F'/F$ for $r=r_0e^{k\theta}$ | $k+i$, constant |
| ODE $r'/r=k$ | $r=C_1e^{k\theta}$ |
| ODE $r'/r=\cot(k-\theta)$ | $r=C_1/\sin(k-\theta)$ |

**Numerical:**

| check | result |
|---|---|
| additive one-phase identity, 2000 random parameter sets | max rel err $4.39\times10^{-14}$ |
| phase span for four values of $c$ | $3.141592$ vs $\pi=3.141593$; ranges match prediction |
| autonomous $\theta$-SDE vs exact, EM at $2\text{k}/8\text{k}/32\text{k}/128\text{k}$ steps | $3.7\text{e-}2 / 1.9\text{e-}2 / 8.8\text{e-}3 / 3.5\text{e-}3$ (order $\approx\tfrac12$) |
| inverse map $\tan(\theta-\varphi)=\nu(S-s_*)$, $10^5$ samples | max abs err $2.13\times10^{-13}$ |
| radius spread vs bin width, collinear | $0.0273\to0.00042$ as bins $180\to11520$ |
| radius spread vs bin width, non-collinear | $0.736\to0.752$ (flat) |
| spiral one-phase identity, 2000 random parameter sets | max rel err $1.64\times10^{-15}$ |
| spiral winding, $\beta=2$, $T=40$ | 15.06 rad $=2.40$ turns |
| $t$-dependent fallback, 3000 random parameter sets | max rel err $1.44\times10^{-13}$ |
| design dictionary, four curve families | $\sim10^{-3}$ at $4\times10^5$ EM steps |

---

## 12. What is and is not new

**Not new.** The polar equation of a line ($r=d\sec(\theta-\varphi)$) is classical analytic geometry.
$1+i\tan\theta=\sec\theta e^{i\theta}$ is a trigonometric identity. The Cayley transform between the
real line and the unit circle is standard, and Brownian motion under stereographic projection dates
to Carne (1985). Complex geometric Brownian motion and its log-spiral fixed-time support are
established. The skew-product decomposition of planar BM is textbook.

**Possibly worth writing down.** The rigidity classification of §6 — that constant $\arg F'$
characterises lines/additive dynamics and constant $F'/F$ characterises spirals/multiplicative
dynamics, and that these exhaust the constant-coefficient cases — is elementary but I have not seen
it stated in this form, and it is the result that turns a collection of constructions into a closed
answer. The design dictionary of §7 follows from it and is genuinely useful for the project.

**Honest assessment.** None of this is a research contribution to probability. All of it is
correct, and §§6–7 give you a complete and usable framework rather than a set of examples. If the
larger project wants a real theorem, the stability-region observation from the Phase 4 review still
looks like the most promising unclaimed ground: in the $(\mu,\sigma,\omega,\beta)$ parameterisation,
mean-square stability collapses to $2\mu+\sigma^2<0$ and almost-sure stability to $\mu<\sigma^2/2$,
both completely independent of the rotational parameters — which is exactly the kind of statement a
reparameterisation is supposed to buy.

---

## 13. Answers, in one place

**If the process must stay additive:**
$$Z_t=Z_0\frac{\sin\phi}{\sin(\phi-\theta_t)}e^{i\theta_t},\qquad
\theta_t=\arg(1+cS_t),\qquad \frac{b}{Z_0}=\rho e^{i\phi}$$
requires $a/b\in\mathbb{R}$ and $b/Z_0\notin\mathbb{R}$; phase confined to a half-turn.
Canonical case: $\;1+iW_t=\sec(\theta_t)e^{i\theta_t},\ \theta_t=\arctan W_t,\ W_t=\tan\theta_t$.

**If the process may be multiplicative — the better answer:**
$$Z_t=Z_0\,e^{(\sigma/\beta)\theta_t}e^{i\theta_t},\qquad \theta_t=\beta W_t$$
Phase is Brownian motion, radius is a deterministic exponential of it, curve is a logarithmic
spiral, winding is unrestricted, no singularities.

**If neither condition holds:** no $t$-free radius exists (Theorem 3), but
$Z_t=Z_0R(t,\theta_t)e^{i\theta_t}$ always does, with one stochastic variable and deterministic
$R(t,\theta)=d_t/\cos(\theta-\varphi_t)$.

**And that is the complete list**: by Theorem 4, lines and logarithmic spirals are the only polar
graphs compatible with constant-coefficient dynamics.
