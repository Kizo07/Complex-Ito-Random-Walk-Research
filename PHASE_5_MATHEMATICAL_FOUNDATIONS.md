# Phase 5 mathematical foundations

## 1. Scope

Let \(W\) be a standard real Brownian motion and consider

\[
Z_t=Z_0+a t+bW_t,
\qquad
Z_0\in\mathbb C\setminus\{0\},\quad
a\in\mathbb C,\quad
b\in\mathbb C\setminus\{0\}.
\tag{1}
\]

We seek a real stochastic process \(\theta\) and a deterministic function
\(r:\mathbb R\to[0,\infty)\) such that

\[
\boxed{
\frac{Z_t}{Z_0}=r(\theta_t)e^{i\theta_t}.
}
\tag{2}
\]

Unless a result explicitly says otherwise, “one-phase representation” means:

1. \(r\) is Borel, single-valued, and has no explicit time dependence;
2. \(\theta_t\bmod 2\pi\) is the geometric argument of \(Z_t/Z_0\)
   whenever \(Z_t\ne0\);
3. the representation holds almost surely for every deterministic time in a
   nontrivial interval;
4. it holds for the complete probability law/full support, not only for one
   selected trajectory;
5. it is lossless: the real scalar state that drives \(Z_t\) is a measurable
   function of the chosen unwrapped phase.

Classical Itô calculations below use \(C^2\) state maps. Borel regularity alone
is used only for the representation and impossibility theorems.

## 2. The Itô table is not complex arithmetic

The mnemonic

\[
(dW_t)^2=dt
\tag{3}
\]

records the quadratic variation

\[
[W]_t
=
\lim_{\lvert\Pi\rvert\to0}
\sum_j\left(W_{t_{j+1}}-W_{t_j}\right)^2
=t
\quad\text{in probability (and along standard refining sequences a.s.).}
\tag{4}
\]

It does not mean that each finite increment satisfies

\[
(\Delta W)^2=\Delta t.
\]

Indeed, for an interval of length \(h\),

\[
\Delta W=\sqrt h\,\xi,\qquad \xi\sim N(0,1),
\]

so

\[
(\Delta W)^2=h\xi^2,
\qquad
\mathbb E[(\Delta W)^2]=h,
\qquad
\operatorname{Var}((\Delta W)^2)=2h^2.
\tag{5}
\]

By contrast,

\[
i^2=-1
\tag{6}
\]

is a deterministic algebraic identity. Multiplication by \(i\) is a
quarter-turn in \(\mathbb R^2\simeq\mathbb C\); quadratic variation is a
limiting property of rough stochastic paths. The formal resemblance “a
square produces a deterministic term” is motivational only.

For a complex continuous semimartingale \(Z=X+iY\), it is useful to retain
both quadratic covariations

\[
[Z,Z]=[X]-[Y]+2i[X,Y],
\qquad
[Z,\overline Z]=[X]+[Y].
\tag{7}
\]

A rank-one complex diffusion \(dZ=b\,dW\) has

\[
d[Z,Z]_t=b^2dt,
\qquad
d[Z,\overline Z]_t=|b|^2dt.
\tag{8}
\]

The complex coefficient \(b\) encodes a direction and scale, but there is
still only one Brownian driver.

## 3. Measurable phase-radius factorization

### Theorem 1 (exact measurable criterion)

Let \(E\) be a standard Borel space, let
\(f:E\to\mathbb C\setminus\{0\}\) be Borel, and let
\(\vartheta:E\to\mathbb R\) be a Borel genuine argument lift:

\[
e^{i\vartheta(s)}=\frac{f(s)}{|f(s)|}.
\]

There is a Borel \(r:\mathbb R\to[0,\infty)\) satisfying

\[
f(s)=r(\vartheta(s))e^{i\vartheta(s)}
\tag{9}
\]

if and only if \(|f|\) is measurable with respect to
\(\sigma(\vartheta)\).

#### Proof

If (9) holds, then \(|f|=r\circ\vartheta\), so \(|f|\) is
\(\sigma(\vartheta)\)-measurable. Conversely, the Doob--Dynkin
factorization lemma applied to \(|f|\) and \(\vartheta\) gives a Borel
\(r\) such that \(|f|=r\circ\vartheta\). Combining this equality with the
genuine-argument identity proves (9). \(\square\)

### Corollary 1 (fiber condition)

A necessary condition is

\[
\vartheta(s_1)=\vartheta(s_2)
\Longrightarrow
|f(s_1)|=|f(s_2)|.
\tag{10}
\]

If \(\vartheta\) is Borel and injective, the Lusin--Souslin theorem makes
its inverse Borel on its image, and the condition is sufficient. In
particular, a continuous strictly monotone argument on an interval gives a
lossless phase coordinate.

Injectivity is not necessary for representation alone. The continuous curve

\[
f(s)=e^{i\sin s}
\]

has

\[
\vartheta(s)=\sin s,\qquad r(\theta)=1,
\]

although \(\vartheta\) is not injective. Injectivity becomes necessary when
the original scalar \(s\), rather than only the point \(f(s)\), must be
recovered from the phase.

## 4. Complete affine existence theorem

Normalize (1):

\[
\zeta_t:=\frac{Z_t}{Z_0}
=1+\alpha t+cW_t,
\qquad
\alpha=\frac a{Z_0},\quad c=\frac b{Z_0}.
\tag{11}
\]

### Theorem 2 (lossless time-independent affine classification)

Under the five requirements in Section 1, (2) exists if and only if

\[
\boxed{
\frac ab\in\mathbb R
\quad\text{and}\quad
\frac b{Z_0}\notin\mathbb R.
}
\tag{12}
\]

Equivalently,

\[
\operatorname{Im}(a\overline b)=0,
\qquad
\operatorname{Im}(b\overline{Z_0})\ne0.
\tag{13}
\]

### 4.1 Sufficiency

Suppose

\[
a=\lambda b,\qquad \lambda\in\mathbb R,
\]

and write

\[
c=\frac b{Z_0}=\rho e^{i\phi},
\qquad
\rho>0,\quad
\phi\in(-\pi,\pi)\setminus\{0\}.
\tag{14}
\]

Then

\[
\zeta_t=1+cx_t,
\qquad
x_t=\lambda t+W_t.
\tag{15}
\]

Because \(\operatorname{Im}c\ne0\), the affine line

\[
L=\{1+cx:x\in\mathbb R\}
\tag{16}
\]

misses the origin. Its continuous argument anchored by
\(\theta(0)=0\) has derivative

\[
\frac{d\theta}{dx}
=
\operatorname{Im}\frac{c}{1+cx}
=
\frac{\operatorname{Im}c}{|1+cx|^2},
\tag{17}
\]

which never vanishes. Thus \(x\mapsto\theta\) is strictly monotone and
lossless.

Writing \(1+\rho e^{i\phi}x=re^{i\theta}\), multiplying by
\(e^{-i\phi}\), and equating imaginary parts gives

\[
r\sin(\theta-\phi)=-\sin\phi.
\]

Therefore

\[
\boxed{
r(\theta)=\frac{\sin\phi}{\sin(\phi-\theta)}
}
\tag{18}
\]

and

\[
\boxed{
x(\theta)
=
\frac{\sin\theta}
{\rho\sin(\phi-\theta)}.
}
\tag{19}
\]

Equations (15), (18), and (19) prove existence and lossless recovery.

### 4.2 A Borel polar graph is planar-null

Let \(r:\mathbb R\to[0,\infty)\) be Borel and define

\[
C_r=\{r(\theta)e^{i\theta}:\theta\in\mathbb R\}.
\tag{20}
\]

The image of a Borel map from a standard Borel space is analytic and hence
Lebesgue measurable. For a geometric angle
\(\psi\in[0,2\pi)\), the positive ray at \(\psi\) can meet \(C_r\) only at
the countable family

\[
\{r(\psi+2\pi k)e^{i\psi}:k\in\mathbb Z\}.
\]

Polar-coordinate Fubini therefore gives

\[
\lambda_2(C_r)
=
\int_0^{2\pi}\int_0^\infty
\mathbf 1_{C_r}(q e^{i\psi})\,q\,dq\,d\psi
=0.
\tag{21}
\]

The origin, if present, does not change the result.

### 4.3 Necessity of drift-diffusion collinearity

Assume a representation exists on every \(t\) in a finite interval
\(T=[t_0,t_1]\) with \(0<t_0<t_1\). Suppose, for contradiction, that

\[
\operatorname{Im}(a\overline b)\ne0.
\tag{22}
\]

Let \(\tau\) be uniform on \(T\), independent of \(W\). The pair
\((\tau,W_\tau)\) has joint density

\[
f_{\tau,W_\tau}(t,w)
=
\frac{\mathbf 1_T(t)}{t_1-t_0}
\frac{1}{\sqrt{2\pi t}}
\exp\!\left(-\frac{w^2}{2t}\right).
\tag{23}
\]

The real-affine map

\[
(t,w)\longmapsto Z_0+at+bw
\tag{24}
\]

has nonzero real determinant, equal up to orientation to
\(\operatorname{Im}(a\overline b)\). Hence \(Z_\tau\) has a density with
respect to planar Lebesgue measure.

On the other hand, let \(C_r\) be (20). The assumed equality at every
deterministic \(t\) gives

\[
\mathbb P(Z_t\in Z_0C_r)=1
\quad(t\in T).
\]

Fubini and independence of \(\tau\) imply

\[
\mathbb P(Z_\tau\in Z_0C_r)=1.
\tag{25}
\]

But (21) implies \(\lambda_2(Z_0C_r)=0\), so absolute continuity gives
\(\mathbb P(Z_\tau\in Z_0C_r)=0\), contradicting (25). Thus

\[
\operatorname{Im}(a\overline b)=0,
\qquad
a/b\in\mathbb R.
\tag{26}
\]

This random-time step closes the almost-sure quantifier gap in an informal
“the support lines sweep a region” argument.

### 4.4 Necessity that the fixed line miss the origin

Under (26), all fixed-time supports equal

\[
L=Z_0+b\mathbb R.
\tag{27}
\]

If \(b/Z_0\in\mathbb R\), then \(L\) passes through the origin. Every
nonzero point of \(L/Z_0\) has geometric argument \(0\) or \(\pi\). Its
possible unwrapped genuine phases therefore belong to

\[
\{2\pi k:k\in\mathbb Z\}
\cup
\{\pi+2\pi k:k\in\mathbb Z\}.
\tag{28}
\]

A single-valued \(r\) maps (28) to only countably many points on the two
rays. At every \(t>0\), however, \(Z_t\) has a nonatomic Gaussian law along
the full line (27). It cannot be supported on a countable set. Therefore

\[
\frac b{Z_0}\notin\mathbb R.
\tag{29}
\]

Sections 4.1--4.4 prove Theorem 2. \(\square\)

## 5. Exact phase domain and uniqueness

With (14), the phase domain is

\[
\boxed{
I_\phi=
\begin{cases}
(\phi-\pi,\phi),&\sin\phi>0,\\[3pt]
(\phi,\phi+\pi),&\sin\phi<0.
\end{cases}
}
\tag{30}
\]

It is the unique open interval of length \(\pi\) containing \(0\) on which
(18) is positive. The map (17) is a bijection

\[
\theta:\mathbb R\longrightarrow I_\phi.
\]

At both endpoints,

\[
|x(\theta)|\to\infty,
\qquad
r(\theta)\to\infty.
\tag{31}
\]

Thus the additive phase never completes one full revolution.

### Proposition 1 (continuous-lift uniqueness)

For the fixed affine line (16), require \(\theta(x)\) to be continuous,
genuine, and anchored by \(\theta(0)=0\). Then \(\theta\) is unique,
\(x\mapsto\theta\) is the monotone map (17), and eliminating \(x\) forces
(18).

#### Proof

A continuous argument lift of a nonvanishing continuous curve is unique after
its initial value is fixed. Equation (17) makes the lift strictly monotone.
The radius must equal \(|1+cx|\); eliminating \(x\) by the imaginary-part
identity used in Section 4.1 gives (18). \(\square\)

Without continuity, one can add state-dependent multiples of \(2\pi\).
Those pathological lifts are excluded because they destroy the continuous
diffusion coordinate being studied.

## 6. Canonical secant representation

Let

\[
dX_t=\mu\,dt+\sigma\,dW_t,
\qquad
Y_t=X_t-X_0,
\qquad
c>0,
\tag{32}
\]

and embed it as

\[
\mathcal Z_t
=
Z_0\left(1+i\frac{Y_t}{c}\right).
\tag{33}
\]

Define

\[
\theta_t=\arctan\left(\frac{Y_t}{c}\right)
\in\left(-\frac\pi2,\frac\pi2\right).
\tag{34}
\]

Then

\[
\boxed{
\mathcal Z_t=Z_0\sec\theta_t\,e^{i\theta_t},
\qquad
X_t=X_0+c\tan\theta_t.
}
\tag{35}
\]

This is the \(\rho=1/c,\ \phi=\pi/2\) member of (18).

If the real Brownian coordinate is to remain the real part, one may instead
use

\[
\widetilde Z_t=ic+Y_t
=ic\,\sec\widetilde\theta_t e^{i\widetilde\theta_t},
\qquad
\widetilde\theta_t=-\arctan(Y_t/c),
\qquad
Y_t=-c\tan\widetilde\theta_t.
\tag{36}
\]

Both are embeddings; neither says that a literal real-valued process has a
lossless nonconstant geometric phase without an offset.

## 7. Phase SDEs and generators

### 7.1 Canonical case

For \(f(y)=\arctan(y/c)\),

\[
f'(y)=\frac{c}{c^2+y^2},
\qquad
f''(y)=-\frac{2cy}{(c^2+y^2)^2}.
\]

Using \(y=c\tan\theta\), Itô's formula gives

\[
\boxed{
d\theta_t
=
\left[
\frac{\mu}{c}\cos^2\theta_t
-
\frac{\sigma^2}{c^2}
\sin\theta_t\cos^3\theta_t
\right]dt
+
\frac{\sigma}{c}\cos^2\theta_t\,dW_t.
}
\tag{37}
\]

The Stratonovich form is

\[
\boxed{
d\theta_t
=
\frac{\mu}{c}\cos^2\theta_t\,dt
+
\frac{\sigma}{c}\cos^2\theta_t\circ dW_t.
}
\tag{38}
\]

The generator is

\[
\boxed{
\mathcal L_\theta h
=
\left[
\frac{\mu}{c}\cos^2\theta
-
\frac{\sigma^2}{c^2}\sin\theta\cos^3\theta
\right]h'
+
\frac{\sigma^2}{2c^2}\cos^4\theta\,h''.
}
\tag{39}
\]

The martingale problem for (39), on
\((-\pi/2,\pi/2)\), is a phase-first definition that does not name \(W\)
in the state formula. It defines the same Markov law as (32) under the
diffeomorphism \(x=X_0+c\tan\theta\).

### 7.2 General eligible affine case

Let \(x_t=\lambda t+W_t\) and define

\[
g(\theta)
:=
\frac{\rho\sin^2(\phi-\theta)}{\sin\phi}.
\tag{40}
\]

Equations (17)--(19) give

\[
\frac{d\theta}{dx}=g(\theta),
\qquad
g'(\theta)
=
-\frac{2\rho\sin(\phi-\theta)\cos(\phi-\theta)}
{\sin\phi}.
\tag{41}
\]

Therefore

\[
\boxed{
d\theta_t
=
\left[
\lambda g(\theta_t)
+\frac12g(\theta_t)g'(\theta_t)
\right]dt
+g(\theta_t)dW_t,
}
\tag{42}
\]

or

\[
\boxed{
d\theta_t
=
\lambda g(\theta_t)dt
+g(\theta_t)\circ dW_t.
}
\tag{43}
\]

The sign of \(g\) records the orientation of the phase chart. A diffusion
coefficient need not be declared positive; changing \(W\) to \(-W\) reverses
that sign without changing the law.

## 8. Exact transition law and semigroup

### Theorem 3 (canonical transition density)

Let \(u,v\in(-\pi/2,\pi/2)\) and \(h>0\). The transition density of (37) is

\[
\boxed{
p_h(v\mid u)
=
\frac{c\sec^2v}{|\sigma|\sqrt{2\pi h}}
\exp\left[
-\frac{
\left(c\tan v-c\tan u-\mu h\right)^2
}{2\sigma^2h}
\right]
}
\tag{44}
\]

for \(\sigma\ne0\).

#### Proof

Conditionally on \(\theta_s=u\),

\[
Y_{s+h}
=c\tan u+\mu h+\sigma\sqrt h\,\xi,
\qquad
\xi\sim N(0,1).
\]

The inverse \(v=\arctan(Y/c)\) has Jacobian
\(dY/dv=c\sec^2v\), yielding (44). \(\square\)

An exact update is

\[
\boxed{
\theta_{s+h}
=
\arctan\left[
\tan\theta_s+\frac{\mu h}{c}
+\frac{\sigma\sqrt h}{c}\xi
\right].
}
\tag{45}
\]

For the general normalized case, let \(x(\theta)\) be (19). Then

\[
\boxed{
p_h(v\mid u)
=
\frac{|x'(v)|}{\sqrt{2\pi h}}
\exp\left[
-\frac{(x(v)-x(u)-\lambda h)^2}{2h}
\right],
}
\tag{46}
\]

where

\[
|x'(v)|
=
\frac{|\sin\phi|}
{\rho\sin^2(\phi-v)}.
\tag{47}
\]

Normalization follows by the substitution \(y=x(v)\). The
Chapman--Kolmogorov identity follows from the Gaussian semigroup:

\[
\int_{I_\phi}p_h(v\mid q)p_s(q\mid u)\,dq
=p_{h+s}(v\mid u),
\tag{48}
\]

after substituting \(x(q)\). Thus no numerical convolution is needed to
establish the semigroup.

## 9. Boundary classification

The canonical phase endpoints correspond under \(x=c\tan\theta\) to
\(\pm\infty\) for the constant-coefficient diffusion

\[
dX=\mu\,dt+\sigma\,dW,\qquad \sigma\ne0.
\]

Its scale and speed densities can be chosen as

\[
s'(x)=\exp\left(-\frac{2\mu x}{\sigma^2}\right),
\qquad
m'(x)=\frac{2}{\sigma^2}
\exp\left(\frac{2\mu x}{\sigma^2}\right).
\tag{49}
\]

Here is a direct boundary argument that avoids hiding the nonzero-drift case
inside shorthand about exponential cancellations. For every finite \(T\),

\[
\sup_{0\le t\le T}|X_t|
\le
|X_0|+|\mu|T+|\sigma|\sup_{0\le t\le T}|W_t|
<\infty
\qquad\text{almost surely}.
\]

Thus neither \(+\infty\) nor \(-\infty\) is reachable from the interior in
finite time. Neither endpoint is an entrance boundary either. Indeed, for
any \(t>0\) and compact interval \(K=[-R,R]\),

\[
\mathbb P_x(X_t\in K)
=
\mathbb P\!\left(
x+\mu t+\sigma W_t\in[-R,R]
\right)
\longrightarrow 0
\]

as \(x\to+\infty\), and likewise as \(x\to-\infty\). The Gaussian transition
measures therefore escape every compact subset of \(\mathbb R\); they have no
probability limit on \(\mathbb R\) from which a Feller entrance law at either
endpoint could be defined. In the standard one-dimensional diffusion
classification, an endpoint that is neither reachable from the interior nor
admissible as an entrance is natural. This also agrees with the scale--speed
test: when \(\mu=0\), the relevant integrals reduce immediately to multiples
of \(\int^\infty(x-x_0)\,dx=\infty\), and the exact Gaussian argument covers
all \(\mu\) without a sign split.

Boundary type is invariant under the smooth monotone state diffeomorphism.
Consequently:

\[
\boxed{
-\frac\pi2\ \text{and}\ \frac\pi2
\text{ are inaccessible natural boundaries for (37).}
}
\tag{50}
\]

The same conclusion holds at both endpoints of the general interval
\(I_\phi\). No reflecting or absorbing boundary condition should be added.

## 10. Reconstruction by Itô's formula

Let

\[
F(\theta)=\sec\theta\,e^{i\theta}=1+i\tan\theta.
\]

Then

\[
F'(\theta)=i\sec^2\theta,
\qquad
F''(\theta)=2i\sec^2\theta\tan\theta.
\]

Apply Itô's formula to \(Z_0F(\theta_t)\) with (37). The drift correction
from \(F''(d\theta)^2/2\) cancels the nonlinear Itô drift in (37), leaving

\[
d\left[Z_0F(\theta_t)\right]
=
\frac{iZ_0}{c}
\left(\mu\,dt+\sigma\,dW_t\right).
\tag{51}
\]

This reconstructs (33) exactly. The cancellation is a consequence of a
coordinate transformation, not a cancellation of Brownian randomness.

## 11. Cayley unit-circle transform

Let \(Y\) satisfy (32) and define

\[
\boxed{
U_t
=
\frac{1+iY_t/c}{1-iY_t/c}.
}
\tag{52}
\]

The denominator is the conjugate of the numerator, so \(|U_t|=1\). With

\[
\Theta_t=2\arctan(Y_t/c)\in(-\pi,\pi),
\tag{53}
\]

the tangent half-angle identity gives

\[
\boxed{
U_t=e^{i\Theta_t},
\qquad
Y_t=c\tan(\Theta_t/2).
}
\tag{54}
\]

The missing point \(U=-1\) represents \(|Y|=\infty\) and is inaccessible at
finite time.

Itô's formula gives

\[
\boxed{
\begin{aligned}
d\Theta_t={}&
\left[
\frac{2\mu}{c}\cos^2\frac{\Theta_t}{2}
-
\frac{2\sigma^2}{c^2}
\sin\frac{\Theta_t}{2}\cos^3\frac{\Theta_t}{2}
\right]dt\\
&+
\frac{2\sigma}{c}
\cos^2\frac{\Theta_t}{2}\,dW_t,
\end{aligned}
}
\tag{55}
\]

and, in Stratonovich form,

\[
d\Theta_t
=
\frac{2\mu}{c}\cos^2\frac{\Theta_t}{2}\,dt
+
\frac{2\sigma}{c}\cos^2\frac{\Theta_t}{2}\circ dW_t.
\tag{56}
\]

The exact transition is

\[
\Theta_{s+h}
=2\arctan\left[
\tan\frac{\Theta_s}{2}
+\frac{\mu h}{c}
+\frac{\sigma\sqrt h}{c}\xi
\right].
\tag{57}
\]

Direct differentiation of (52) yields the complex SDE

\[
\boxed{
\begin{aligned}
dU_t={}&
\left[
\frac{i\mu}{2c}(1+U_t)^2
-
\frac{\sigma^2}{4c^2}(1+U_t)^3
\right]dt\\
&+
\frac{i\sigma}{2c}(1+U_t)^2\,dW_t.
\end{aligned}
}
\tag{58}
\]

Applying Itô's product rule to \(U_t\overline U_t\) makes its drift and
martingale terms cancel, verifying \(d|U_t|^2=0\) without referring back to
the transform.

The angular diffusion in (55) is state dependent and vanishes near
\(\pm\pi\). Therefore \(U\) is not standard Brownian motion on the circle.
It is a lossless nonlinear transform of a real diffusion.

## 12. Multiplicative logarithmic-spiral alternative

Consider

\[
Z_t=Z_0\exp(\kappa t+BW_t),
\qquad
B=\sigma+i\beta.
\tag{59}
\]

### Theorem 4 (compatible multiplicative one-phase form)

Assume a continuous genuine phase must losslessly recover the scalar state.
For \(\beta\ne0\), (59) has a time-independent one-phase logarithmic-spiral
form if and only if

\[
\kappa=\gamma B
\quad\text{for some }\gamma\in\mathbb R.
\tag{60}
\]

Then

\[
\theta_t=\beta(\gamma t+W_t),
\qquad
\boxed{
Z_t
=
Z_0
\exp\left(\frac{\sigma}{\beta}\theta_t\right)
e^{i\theta_t}.
}
\tag{61}
\]

#### Proof

In logarithmic coordinates,

\[
\log(Z_t/Z_0)=\kappa t+BW_t.
\]

A time-independent graph of real log-radius over unwrapped phase requires all
fixed-time support lines to coincide, hence real collinearity (60). The
imaginary coordinate must be lossless, requiring \(\beta\ne0\). Under these
conditions, elimination of \(\gamma t+W_t\) gives (61). Conversely, direct
substitution proves the representation. \(\square\)

Unlike the affine secant phase, \(\theta_t\) ranges over \(\mathbb R\) and
can wind without bound. The cost is decisive: (59) is multiplicative, not
the original additive process (1).

If the multiplicative SDE is written

\[
\frac{dZ_t}{Z_t}=A\,dt+B\,dW_t,
\]

then \(\kappa=A-\tfrac12B^2\), and compatibility becomes

\[
A-\frac12B^2\in B\mathbb R.
\tag{62}
\]

## 13. Time-dependent moving-line fallback

For the general normalized affine process

\[
\zeta_t=p_t+cW_t,
\qquad
p_t=1+\alpha t,
\tag{63}
\]

the fixed-time support is \(p_t+c\mathbb R\). Whenever

\[
\operatorname{Im}(p_t\overline c)\ne0,
\tag{64}
\]

that line misses the origin. Its local polar equation is

\[
\boxed{
R(t,\theta)
=
\frac{\operatorname{Im}(p_t\overline c)}
{\operatorname{Im}(e^{i\theta}\overline c)},
}
\tag{65}
\]

on the unique angular interval where the ratio is positive.

Thus

\[
\zeta_t=R(t,\theta_t)e^{i\theta_t}
\tag{66}
\]

is a one-random-variable but explicitly time-dependent representation.

On a nonvanishing chart, the complex Itô formula for a local logarithm gives

\[
d\log\zeta_t
=
\left(
\frac{\alpha}{\zeta_t}
-\frac{c^2}{2\zeta_t^2}
\right)dt
+\frac c{\zeta_t}dW_t.
\]

Taking imaginary parts,

\[
\boxed{
d\theta_t
=
\operatorname{Im}\left(
\frac{\alpha}{\zeta_t}
-\frac{c^2}{2\zeta_t^2}
\right)dt
+
\operatorname{Im}\left(\frac c{\zeta_t}\right)dW_t.
}
\tag{67}
\]

Substituting \(\zeta_t=R(t,\theta_t)e^{i\theta_t}\) closes the coefficients
in \((t,\theta)\).

If \(a\) and \(b\) are noncollinear, the equation

\[
\operatorname{Im}(p_t\overline c)=0
\tag{68}
\]

has at most one solution in \(t\). At such a deterministic time, the support
line passes through the origin and no single-valued genuine phase-radius
graph represents its full nonatomic line law. This remains a support-level
failure even though the event \(\zeta_t=0\) itself has probability zero at a
fixed time.

## 14. What has and has not been eliminated

The state identity (35) contains only \(\theta_t\), not separate symbols
\(t\) and \(W_t\). The law of \(\theta\) may be specified in any of three
equivalent ways:

1. the transformed SDE (37);
2. the generator/martingale problem (39);
3. the exact Markov kernel (44).

The SDE notation still contains \(dt\) and \(dW_t\) because those terms
describe time evolution and stochastic forcing. The generator and transition
kernel hide the driver from the state formula, but they do not remove time or
randomness from the probability law.

The correct conclusion is:

\[
\boxed{
\text{one state coordinate can combine the accumulated drift and Brownian
state; it cannot combine away stochastic calculus itself.}
}
\]
