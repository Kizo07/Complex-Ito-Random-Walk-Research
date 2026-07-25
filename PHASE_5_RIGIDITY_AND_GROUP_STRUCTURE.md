# Phase 5 rigidity and group structure

## 1. Why a rigidity theorem is needed

Writing

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t}
\]

does not by itself determine the law of \(Z\). For any sufficiently smooth
positive radius and any scalar diffusion \(\theta\), Itô's formula produces
some complex diffusion on the chosen curve. The stronger question is:

> Which phase curves can produce a constant-coefficient additive or
> multiplicative complex SDE?

The diffusion term determines the curve family; the drift term supplies an
additional compatibility equation. Omitting that second equation gives an
incomplete classification.

## 2. General induced Itô dynamics

Let \(I\subset\mathbb R\) be an open interval and

\[
F(\theta)=r(\theta)e^{i\theta},
\qquad
r\in C^2(I;(0,\infty)).
\tag{1}
\]

Let

\[
d\theta_t=m(\theta_t)\,dt+s(\theta_t)\,dW_t,
\qquad
s(\theta)\ne0,
\tag{2}
\]

on \(I\), and set

\[
Z_t=Z_0F(\theta_t),\qquad Z_0\ne0.
\tag{3}
\]

Itô's formula gives

\[
\boxed{
dZ_t
=
Z_0
\left[
F'm+\frac12F''s^2
\right](\theta_t)dt
+
Z_0F'(\theta_t)s(\theta_t)dW_t.
}
\tag{4}
\]

The representation is classical only because \(F\) is \(C^2\). A merely
Borel radius can define a state map but cannot be substituted into (4).

## 3. Additive rigidity

### Theorem 1 (complete local additive classification)

Under (1)--(3), with \(F'\ne0\), the process satisfies

\[
dZ_t=a\,dt+b\,dW_t,
\qquad
b\ne0,
\tag{5}
\]

if and only if

\[
F'(\theta)s(\theta)=\frac b{Z_0}
\tag{6}
\]

and

\[
\boxed{
\frac ab\in\mathbb R,
\qquad
m(\theta)
=
\frac ab\,s(\theta)
+\frac12s(\theta)s'(\theta).
}
\tag{7}
\]

Equation (6) forces the image of \(F\) to lie on a straight line. In genuine
polar coordinates, every nonradial member has the local form

\[
\boxed{
r(\theta)=\frac{C}{\sin(\delta-\theta)}
}
\tag{8}
\]

on an interval where the right-hand side is positive.

#### Proof

Matching diffusion terms in (4) and (5) gives (6). Differentiate (6) with
respect to \(\theta\):

\[
F''s+F's'=0.
\]

Because \(F'=b/(Z_0s)\),

\[
F''=-\frac b{Z_0}\frac{s'}{s^2}.
\tag{9}
\]

Matching drift terms and using (9),

\[
\frac a{Z_0}
=
\frac b{Z_0}
\left(
\frac m{s}-\frac12s'
\right).
\]

Thus

\[
\frac ab=\frac m{s}-\frac12s'\in\mathbb R,
\]

which is equivalent to (7).

Conversely, (6) and (7) substituted into (4) give (5).

Since \(s\) is real, (6) says that \(F'\) always has the fixed complex
direction \(b/Z_0\), up to orientation. Therefore \(F(I)\) is contained in a
straight line. To obtain its polar equation, write

\[
F'=e^{i\theta}(r'+ir).
\]

If the constant tangent direction has argument \(\delta\), then

\[
\arg(r'+ir)=\delta-\theta
\]

and hence

\[
\frac{r'}r=\cot(\delta-\theta).
\]

Integration on an interval of constant sign yields (8). \(\square\)

### Remarks

1. The curve-shape conclusion comes from the diffusion equation (6).
2. The drift conclusion (7) is independent and necessary.
3. A line through the origin can satisfy a local tangent equation, but it
   cannot provide the global lossless genuine-phase representation of a
   nonatomic affine Brownian line established in Phase 5 foundations.
4. The canonical secant family is (8) with
   \(\delta=\pi/2\) and \(C=1\).

For the general eligible affine construction,

\[
s(\theta)=g(\theta),\qquad
m(\theta)=\lambda g(\theta)+\frac12g(\theta)g'(\theta),
\]

so (7) holds with \(a/b=\lambda\).

## 4. Multiplicative rigidity

### Theorem 2 (complete local multiplicative classification)

Under (1)--(3), suppose

\[
dZ_t=A Z_t\,dt+B Z_t\,dW_t
\tag{10}
\]

with \(B\ne0\). A genuine phase representation with \(s\ne0\) satisfies
(10) if and only if, writing

\[
B=\sigma+i\beta,
\]

the following conditions hold:

\[
\boxed{
\beta\ne0,\qquad
s(\theta)\equiv\beta,\qquad
r(\theta)=r_0e^{k\theta},
\qquad
k=\frac{\sigma}{\beta},
}
\tag{11}
\]

and the phase drift is a real constant \(m_0\) satisfying

\[
\boxed{
A=(k+i)m_0+\frac12(k+i)^2\beta^2.
}
\tag{12}
\]

Equivalently,

\[
\boxed{
A-\frac12B^2\in B\mathbb R.
}
\tag{13}
\]

#### Proof

Matching diffusion terms in (4) and (10) gives

\[
\frac{F'}F\,s=B.
\tag{14}
\]

But

\[
\frac{F'}F=\frac{r'}r+i.
\tag{15}
\]

Because \(s\) is real, imaginary parts of (14) give

\[
s=\operatorname{Im}B=\beta.
\]

Thus \(\beta\ne0\) and \(s\) is constant. Real parts give

\[
\frac{r'}r=\frac{\operatorname{Re}B}{\operatorname{Im}B}=k,
\]

so \(r=r_0e^{k\theta}\).

Let \(q=k+i\). Then

\[
\frac{F'}F=q,\qquad
\frac{F''}F=q^2.
\]

Matching drifts in (4) and (10) gives

\[
A=q\,m(\theta)+\frac12q^2\beta^2.
\tag{16}
\]

Since \(A,q,\beta\) are constant and \(q\ne0\), \(m\) must be a real
constant \(m_0\), and (12) follows.

Finally \(B=q\beta\), so

\[
A-\frac12B^2=q m_0=B\frac{m_0}{\beta}\in B\mathbb R.
\]

The converse follows by substituting (11)--(12) into (4). \(\square\)

### Corollary 1 (circle)

The constant-radius case is \(k=0\). It requires

\[
B=i\beta,\qquad
d\theta=m_0dt+\beta dW,
\]

and

\[
\frac{dZ}{Z}
=
\left(im_0-\frac12\beta^2\right)dt+i\beta\,dW.
\tag{17}
\]

A state-dependent phase drift would make the multiplicative drift
state-dependent; it would not satisfy a constant-coefficient SDE.

### Corollary 2 (logarithmic form)

The solution of (10) is

\[
Z_t
=Z_0
\exp\left[
\left(A-\frac12B^2\right)t+BW_t
\right].
\]

Condition (13) is exactly the condition that log drift and log diffusion are
real-collinear. It is therefore the same compatibility condition obtained by
the fixed-support-line argument in logarithmic coordinates.

## 5. Exhaustive line-versus-spiral dictionary

Within the stated \(C^2\), nondegenerate, genuine-phase setting:

| Desired complex SDE | Diffusion matching condition | Forced curve | Additional drift condition |
|---|---|---|---|
| \(dZ=a\,dt+b\,dW\) | \(F's=b/Z_0\) constant | straight line, \(r=C/\sin(\delta-\theta)\) | \(a/b\in\mathbb R\), \(m=(a/b)s+\tfrac12ss'\) |
| \(dZ/Z=A\,dt+B\,dW\) | \(F's/F=B\) constant | logarithmic spiral, \(r=r_0e^{k\theta}\) | \(s=\operatorname{Im}B\), \(m\) constant, \(A-\tfrac12B^2\in B\mathbb R\) |

Other smooth polar curves are valid design choices, but their induced complex
SDE coefficients are generally state dependent. The line and spiral are
rigid only relative to the requested constant-coefficient additive and
multiplicative laws.

## 6. Transported group law for the secant phase

Let

\[
\Phi_c:\mathbb R\to
\left(-\frac\pi2,\frac\pi2\right),
\qquad
\Phi_c(x)=\arctan(x/c),
\quad c>0.
\tag{18}
\]

Transport ordinary addition through this bijection:

\[
\theta_1\oplus\theta_2
:=
\Phi_c\left(
\Phi_c^{-1}(\theta_1)+\Phi_c^{-1}(\theta_2)
\right).
\]

Since \(\Phi_c^{-1}(\theta)=c\tan\theta\),

\[
\boxed{
\theta_1\oplus\theta_2
=
\arctan(\tan\theta_1+\tan\theta_2).
}
\tag{19}
\]

Therefore

\[
\left(
\left(-\frac\pi2,\frac\pi2\right),\oplus
\right)
\cong
(\mathbb R,+).
\tag{20}
\]

The operation is associative and commutative, has identity \(0\), and has
inverse \(-\theta\). These facts are inherited from real addition; no
trigonometric identity proof is needed.

For Gaussian increments \(x_j\),

\[
\Phi_c\left(\sum_jx_j\right)
=
\bigoplus_j\Phi_c(x_j).
\tag{21}
\]

This is exact but normally more expensive than summing \(x_j\) directly,
because it requires tangent/arctangent evaluations.

### The polar embedding is not a multiplicative representation

The normalized secant curve is

\[
F(\Phi_c(x))=1+i\frac{x}{c}.
\]

In general,

\[
F(\Phi_c(x+y))
=1+i\frac{x+y}{c},
\]

whereas

\[
F(\Phi_c(x))F(\Phi_c(y))
=
1+i\frac{x+y}{c}-\frac{xy}{c^2}.
\]

Thus

\[
F(\theta_1\oplus\theta_2)
\ne F(\theta_1)F(\theta_2)
\tag{22}
\]

except in degenerate cases. The state-space group law is not ordinary complex
multiplication.

## 7. Cayley transported group law

For

\[
\Psi_c(x)=2\arctan(x/c)\in(-\pi,\pi),
\]

the transported addition is

\[
\boxed{
\Theta_1\boxplus\Theta_2
=
2\arctan\left(
\tan\frac{\Theta_1}{2}
+
\tan\frac{\Theta_2}{2}
\right).
}
\tag{23}
\]

Again,

\[
((-\pi,\pi),\boxplus)\cong(\mathbb R,+).
\]

Although \(e^{i\Theta}\) lies on the unit circle, \(\boxplus\) is not
ordinary angular addition. In particular,

\[
e^{i(\Theta_1\boxplus\Theta_2)}
\ne e^{i\Theta_1}e^{i\Theta_2}
\]

in general.

The omitted endpoint \(-1\) is the compactification point at infinity, not a
group element reached by a finite real coordinate.

## 8. General affine-line group law

For any eligible affine line, let

\[
h(x)=\arg(1+cx)
\]

be the continuous monotone lift from \(\mathbb R\) to \(I_\phi\), with
inverse (from the Phase 5 foundations)

\[
h^{-1}(\theta)
=
\frac{\sin\theta}
{\rho\sin(\phi-\theta)}.
\]

Define

\[
\theta_1\oplus_c\theta_2
:=
h\left(h^{-1}(\theta_1)+h^{-1}(\theta_2)\right).
\tag{24}
\]

Then \((I_\phi,\oplus_c)\cong(\mathbb R,+)\). The identity is \(0\).
Unless the line has the canonical perpendicular symmetry, the group inverse
need not look like ordinary angle negation; it is

\[
h(-h^{-1}(\theta)).
\]

This generalization confirms that the group structure comes from the scalar
coordinate, not from rotation symmetry of the plane.

## 9. Impossibility of lossless ordinary unit-circle multiplication

### Theorem 3

There is no continuous injective group homomorphism

\[
\chi:(\mathbb R,+)\longrightarrow(S^1,\cdot).
\tag{25}
\]

#### Proof

Every continuous one-parameter subgroup of \(S^1\) has the form

\[
\chi(x)=e^{i\kappa x}
\]

for some \(\kappa\in\mathbb R\). One elementary proof lifts \(\chi\)
continuously near the identity, applies the continuous Cauchy functional
equation to the local argument, and extends by the homomorphism property.

If \(\kappa=0\), the map is constant. If \(\kappa\ne0\), it has period
\(2\pi/|\kappa|\). In neither case is it injective. \(\square\)

Consequently, the following three properties cannot coexist:

1. constant radius;
2. lossless recovery of an unrestricted real coordinate;
3. ordinary real addition represented by ordinary complex multiplication.

The Cayley transform keeps (1) and (2) but replaces (3) by the transported
law (23). The pure exponential \(e^{i\kappa x}\) keeps (1) and (3) but loses
(2).

## 10. Why the logarithmic spiral resolves the tradeoff

The complex exponential

\[
\chi_{\alpha,\beta}(x)
=e^{(\alpha+i\beta)x}
\tag{26}
\]

is a homomorphism from \((\mathbb R,+)\) to
\((\mathbb C\setminus\{0\},\cdot)\):

\[
\chi_{\alpha,\beta}(x+y)
=
\chi_{\alpha,\beta}(x)\chi_{\alpha,\beta}(y).
\]

If \(\alpha\ne0\), its changing modulus makes the map injective. If also
\(\beta\ne0\), its unwrapped genuine phase \(\beta x\) is itself a lossless
coordinate and the image is a logarithmic spiral:

\[
r(\theta)=e^{(\alpha/\beta)\theta}.
\tag{27}
\]

If \(\alpha=0,\ \beta\ne0\), the image is a circle and the map is periodic.
If \(\beta=0\), the map may be injective through its radius but its genuine
phase is constant and cannot be the lossless state variable.

Thus changing radius is exactly what permits ordinary multiplicative
composition and lossless winding to coexist.

## 11. State-space group versus Markov semigroup

Two algebraic structures must not be confused.

The transported operation \(\oplus\) combines **states or increments**:

\[
\Phi_c(x+y)=\Phi_c(x)\oplus\Phi_c(y).
\]

The transition operators

\[
(P_tf)(\theta)
=
\mathbb E_\theta[f(\theta_t)]
\]

form a **Markov semigroup**:

\[
P_{t+s}=P_tP_s,\qquad t,s\ge0.
\tag{28}
\]

The Markov semigroup is generally not a group because diffusion loses
information when distributions are propagated forward and has no
positivity-preserving inverse for negative time. The exact transition-density
semigroup in Phase 5 follows from Gaussian convolution, independently of the
state-space operation.

## 12. Consequences for “vector stochastic calculus”

The rigidity results give a precise boundary:

- A scalar phase curve has one tangent direction \(F'(\theta)\) at each
  state and therefore differential rank one.
- Constant additive complex noise can remain on that curve only when all
  tangents are parallel: a line.
- Constant multiplicative complex noise can remain on that curve only when
  the logarithmic tangent \(F'/F\) is constant: a logarithmic spiral.
- A circle is a special multiplicative family, not an additive affine family.
- A general two-coordinate or hypoelliptic diffusion is not reducible to one
  phase simply because its notation uses one \(dW\).

Complex notation can organize tangent/normal vectors, rotations, and
Stratonovich flows. It does not evade rank, support, or drift-compatibility
conditions.
