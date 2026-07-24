# Complex Numbers, Itô Calculus, and Random Walks

## Research objective

Develop a precise bridge between:

1. the polar/exponential representation of a complex number,
   \[
   z=r(\cos\theta+i\sin\theta)=re^{i\theta},
   \]
2. the Itô rule
   \[
   (dW_t)^2=dt,
   \]
3. and the drift-diffusion model
   \[
   dX_t=\mu\,dt+\sigma\,dW_t.
   \]

The main goal is to determine what a mathematically meaningful “polar” or
“exponential” form of a random walk or diffusion should mean, derive the
candidate forms with Itô's lemma, and identify exactly where the analogy with
complex numbers succeeds and where it fails.

## First mathematical guardrail

The expressions
\[
i^2=-1
\qquad\text{and}\qquad
(dW_t)^2=dt
\]
are both multiplication rules, but they belong to very different algebras.

- \(i^2=-1\) is an exact algebraic identity. Multiplication by \(i\) is a
  quarter-turn in the complex plane.
- \((dW_t)^2=dt\) is shorthand in Itô calculus for Brownian quadratic
  variation. More precisely, along refining time partitions,
  \[
  \sum_k (W_{t_{k+1}}-W_{t_k})^2\longrightarrow t
  \]
  in an appropriate probabilistic sense.
- A Brownian path has no ordinary derivative, so \(dW_t\) is not an ordinary
  number whose pointwise square literally equals \(dt\).

The first-order Itô multiplication table is
\[
\begin{array}{c|cc}
       &dt&dW_t\\ \hline
dt     &0&0\\
dW_t   &0&dt
\end{array}.
\]
Formally, if \(dt=(dW_t)^2\), then \((dW_t)^3=0\) at the retained Itô order.
This is nilpotent/truncated behavior, not the rotational behavior of \(i\).
The analogy is therefore structural and potentially useful, but it is not an
identification of \(dW_t\) with \(i\).

## Three meanings of “a similar form”

We will distinguish three questions that can otherwise be conflated.

### 1. Polar form of one finite increment

For a time step \(\Delta t\),
\[
\Delta X=\mu\Delta t+\sigma\sqrt{\Delta t}\,\xi,
\qquad \xi\sim N(0,1).
\]
If \(\Delta X\) is real, its complex polar form is only
\[
\Delta X=|\Delta X|e^{i\Theta},
\qquad
\Theta\in\{0,\pi\}.
\]
This is valid but geometrically trivial. A nontrivial continuously varying
angle requires a two-dimensional or genuinely complex process.

### 2. Exponential closed form of a stochastic process

The arithmetic diffusion
\[
dX_t=\mu\,dt+\sigma\,dW_t
\]
has the additive solution
\[
X_t=X_0+\mu t+\sigma W_t.
\]
It does not naturally exponentiate in the way \(re^{i\theta}\) does.

The closest exponential analogue is obtained from the multiplicative SDE
\[
dZ_t=\mu Z_t\,dt+\sigma Z_t\,dW_t.
\]
Itô's lemma gives
\[
Z_t
=Z_0\exp\!\left[\left(\mu-\frac{\sigma^2}{2}\right)t+\sigma W_t\right].
\]
The term \(-\sigma^2t/2\) is the Itô correction. This solution is the
stochastic-exponential analogue of ordinary exponential coordinates.

More generally, for a continuous semimartingale \(M_t\), the stochastic
exponential is
\[
\mathcal E(M)_t
=\exp\!\left(M_t-\frac12[M]_t\right),
\]
where \([M]_t\) is its quadratic variation. This formula is likely to be the
central bridge between exponential algebra and Itô calculus.

### 3. A genuine stochastic rotation

Let Brownian motion drive an angle:
\[
Z_t=r_0
\exp\!\left(i\left[\theta_0+\omega t+\beta W_t\right]\right).
\]
Then \(|Z_t|=r_0\), while its phase undergoes a drifted random walk. Applying
Itô's lemma yields
\[
dZ_t
=\left(i\omega-\frac{\beta^2}{2}\right)Z_t\,dt
+i\beta Z_t\,dW_t.
\]
This is a precise stochastic counterpart of rotation by \(e^{i\theta}\).
The drift \(-\beta^2Z_t/2\) is essential: it compensates for the quadratic
variation of the random phase so that the modulus remains constant.

This construction is the strongest initial candidate for connecting complex
rotation with the Itô rule.

## Working hypotheses

1. The direct comparison \(dW_t\leftrightarrow i\) will fail because the Itô
   differential algebra is nilpotent while the complex algebra is rotational.
2. The correct exponential bridge is the stochastic exponential
   \(\mathcal E(M)\), not a direct polar decomposition of \(dX_t\).
3. A true random angle arises only after moving to a complex or
   two-dimensional process.
4. The Itô correction is the mechanism that converts quadratic variation into
   deterministic drift.
5. A unified amplitude-phase model should take the schematic form
   \[
   Z_t=R_t e^{i\Theta_t},
   \]
   where both \(\log R_t\) and \(\Theta_t\) may be drifted Brownian motions.

## Research program

### Phase 1 — Make the \(dW^2=dt\) rule rigorous

- Start with a discrete symmetric or Gaussian random walk:
  \[
  \Delta W_k=\sqrt{\Delta t}\,\xi_k.
  \]
- Compute its mean, variance, and accumulated squared increments.
- Show how Brownian scaling leads to quadratic variation.
- Derive the full Itô table:
  \[
  (dt)^2=0,\qquad dt\,dW_t=0,\qquad(dW_t)^2=dt.
  \]
- Compare this truncated algebra with the complex relation \(i^2=-1\).
- Investigate whether truncated polynomial algebras or related hypercomplex
  systems offer a useful formal language for Itô differentials.

Deliverable: `01_ITO_ALGEBRA.md`.

### Phase 2 — Derive the additive random-walk solution

- Integrate
  \[
  dX_t=\mu\,dt+\sigma\,dW_t
  \]
  to obtain \(X_t=X_0+\mu t+\sigma W_t\).
- Derive the finite-step transition law:
  \[
  X_{t+\Delta t}-X_t
  \sim N(\mu\Delta t,\sigma^2\Delta t).
  \]
- Explain why a one-dimensional real increment has no nontrivial angular
  degree of freedom.
- Record precisely which additional structure is needed for polar coordinates.

Deliverable: `02_ARITHMETIC_DIFFUSION.md`.

### Phase 3 — Derive the stochastic exponential

- Apply Itô's lemma to \(\log Z_t\) for
  \[
  dZ_t=\mu Z_t\,dt+\sigma Z_t\,dW_t.
  \]
- Derive geometric Brownian motion and the \(-\sigma^2/2\) correction.
- Derive \(\mathcal E(M)_t\) from the Itô differential of an exponential.
- Compare ordinary exponentiation,
  \[
  e^{x+y}=e^xe^y,
  \]
  with stochastic exponentiation and quadratic variation.
- Test the local formal expansion
  \[
  e^{a\,dt+b\,dW_t}
  =1+b\,dW_t+\left(a+\frac{b^2}{2}\right)dt
  \]
  under the Itô multiplication table.

Deliverable: `03_STOCHASTIC_EXPONENTIAL.md`.

### Phase 4 — Build stochastic amplitude and phase

- Begin with the constant-radius phase model
  \[
  Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)}.
  \]
- Derive its complex SDE with Itô's lemma.
- Verify directly that \(d|Z_t|^2=0\).
- Generalize to
  \[
  Z_t=R_t e^{i\Theta_t}
  \]
  with stochastic log-amplitude and stochastic phase.
- Study whether the radial and angular noises should be independent,
  correlated, or driven by the same Brownian motion.
- State the branch and near-origin issues associated with the angle.

Deliverable: `04_STOCHASTIC_POLAR_FORM.md`.

### Phase 5 — Connect with planar Brownian motion

- Define a complex diffusion by
  \[
  Z_t=X_t+iY_t
  \]
  with one or two Brownian drivers.
- Apply the two-dimensional Itô formula to
  \[
  R_t=\sqrt{X_t^2+Y_t^2},
  \qquad
  \Theta_t=\operatorname{atan2}(Y_t,X_t).
  \]
- Derive the radial and angular SDEs away from the origin.
- Compare:
  - noise in Cartesian coordinates,
  - noise only in the phase,
  - noise only in the radius,
  - and correlated amplitude-phase noise.
- Determine which construction best deserves the name “polar random walk.”

Deliverable: `05_PLANAR_BROWNIAN_POLAR_COORDINATES.md`.

### Phase 6 — Discrete verification and simulation

- Simulate the arithmetic walk and confirm its Gaussian transition law.
- Simulate geometric Brownian motion using both:
  - Euler-Maruyama steps, and
  - the exact stochastic-exponential solution.
- Simulate stochastic phase and verify numerically that its radius stays
  constant only when the Itô correction is included in the SDE.
- Simulate planar Brownian motion and compare empirical radial/angular behavior
  with the derived equations.
- Keep numerical experiments separate from proofs.

Deliverable: `notebooks/ito_complex_bridge.ipynb`.

### Phase 7 — Final synthesis

Classify every proposed analogy as one of:

- exact identity,
- equality in the Itô differential calculus,
- equality in distribution,
- limiting statement,
- or heuristic analogy.

The final note should answer:

1. In what sense is \((dW_t)^2=dt\) true?
2. Why does this rule not make \(dW_t\) an imaginary unit?
3. What is the exponential form associated with a stochastic differential?
4. When is \(Z_t=R_te^{i\Theta_t}\) useful?
5. What SDE represents pure stochastic rotation?
6. How do additive random walks, geometric Brownian motion, and planar Brownian
   motion fit into one framework?

Deliverable: `FINAL_SYNTHESIS.md`.

## Immediate next steps

1. Write `01_ITO_ALGEBRA.md`, beginning with a scaled discrete random walk and
   deriving Brownian quadratic variation.
2. Derive the two benchmark formulas side by side:
   \[
   X_t=X_0+\mu t+\sigma W_t
   \]
   and
   \[
   Z_t=Z_0e^{(\mu-\sigma^2/2)t+\sigma W_t}.
   \]
3. Derive and independently verify the stochastic-rotation identity:
   \[
   Z_t=r_0e^{i(\theta_0+\omega t+\beta W_t)}
   \Longleftrightarrow
   dZ_t
   =\left(i\omega-\frac{\beta^2}{2}\right)Z_tdt
   +i\beta Z_tdW_t.
   \]
4. Decide whether the main object of the project should be:
   - the stochastic exponential,
   - stochastic phase,
   - or the full amplitude-phase process.

The recommended route is to treat the stochastic exponential as the algebraic
bridge and stochastic phase as the geometric bridge, then unite them in the
general form \(Z_t=R_te^{i\Theta_t}\).

## Success criteria

- Every use of differential notation is assigned a precise meaning.
- Discrete random walks and continuous diffusions are connected explicitly.
- The Itô correction is derived rather than asserted.
- One-dimensional and two-dimensional constructions are not conflated.
- The final amplitude-phase formula includes its corresponding SDE.
- Analytical identities are checked with at least one independent derivation
  and a numerical experiment.
- The final synthesis clearly separates rigorous results from analogy.
