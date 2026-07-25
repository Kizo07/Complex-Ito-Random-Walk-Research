# Exact One-Phase Euler Representation of Additive Brownian Motion

## Complete mathematical analysis, classification theorem, phase dynamics, transition laws, Cayley compactification, impossibility results, and research positioning

**Date:** July 24, 2026

This document consolidates the complete analysis of whether an additive one-driver complex Brownian process

\[
Z_t = Z_0 + a t + b W_t
\]

can be represented in the phase-only Euler form

\[
Z_t = Z_0\,r(\theta_t)e^{i\theta_t},
\]

where \(\theta_t\) is the only stochastic state variable and \(r(\theta)\) is either constant or a deterministic function of \(\theta\).

The attached proposed solution, `possible_solution.md`, was checked carefully. Its central secant construction, Cayley transform, and general existence conditions are mathematically sound when the assumptions and angular domains are stated precisely. This document includes all of those results, the detailed derivations, the necessary qualifications, and several extensions.

---

## Table of contents

1. [Main result](#1-main-result)
2. [What “only \(\theta_t\) is stochastic” means](#2-what-only-theta_t-is-stochastic-means)
3. [The exact secant construction](#3-the-exact-secant-construction)
4. [Keeping Brownian motion in the real coordinate](#4-keeping-brownian-motion-in-the-real-coordinate)
5. [Geometric explanation](#5-geometric-explanation)
6. [General existence and classification theorem](#6-general-existence-and-classification-theorem)
7. [Explicit formula in the general case](#7-explicit-formula-in-the-general-case)
8. [The required angular domain](#8-the-required-angular-domain)
9. [Why the two existence conditions are necessary](#9-why-the-two-existence-conditions-are-necessary)
10. [Uniqueness of the phase representation](#10-uniqueness-of-the-phase-representation)
11. [Phase dynamics in the secant case](#11-phase-dynamics-in-the-secant-case)
12. [Defining \(\theta_t\) without explicitly defining \(W_t\)](#12-defining-theta_t-without-explicitly-defining-w_t)
13. [Verification by reconstructing the additive SDE](#13-verification-by-reconstructing-the-additive-sde)
14. [Exact transition law of the phase](#14-exact-transition-law-of-the-phase)
15. [General phase dynamics](#15-general-phase-dynamics)
16. [Why literal real Brownian motion cannot do this directly](#16-why-literal-real-brownian-motion-cannot-do-this-directly)
17. [Why \(r(\theta)\) cannot be constant for the same additive process](#17-why-rtheta-cannot-be-constant-for-the-same-additive-process)
18. [Constant-radius encoding through the Cayley transform](#18-constant-radius-encoding-through-the-cayley-transform)
19. [Dynamics of the Cayley phase](#19-dynamics-of-the-cayley-phase)
20. [SDE for the unit-circle process](#20-sde-for-the-unit-circle-process)
21. [Exact addition in the phase coordinate](#21-exact-addition-in-the-phase-coordinate)
22. [A fundamental impossibility theorem](#22-a-fundamental-impossibility-theorem)
23. [Relationship to the earlier complex-GBM construction](#23-relationship-to-the-earlier-complex-gbm-construction)
24. [Connection to projected-normal distributions](#24-connection-to-projected-normal-distributions)
25. [Assessment and refinements of the attached solution](#25-assessment-and-refinements-of-the-attached-solution)
26. [Novelty and mathematical positioning](#26-novelty-and-mathematical-positioning)
27. [Final result](#27-final-result)
28. [References and related sources](#28-references-and-related-sources)

---

# 1. Main result

The complete answer is that

\[
\boxed{
Z_t = Z_0 + a t + bW_t
=
Z_0\,r(\theta_t)e^{i\theta_t}
}
\]

with a **real, nonnegative, deterministic, time-independent** function \(r(\theta)\), and with \(\theta_t\) as the only stochastic state variable, is possible for the entire process precisely when

\[
\boxed{
\frac{a}{b}\in\mathbb R
\qquad\text{and}\qquad
\frac{b}{Z_0}\notin\mathbb R,
}
\]

assuming

\[
Z_0\neq0,\qquad b\neq0.
\]

The first condition means that the deterministic drift and Brownian diffusion move in the same real direction in the complex plane.

The second condition means that the resulting affine line does not pass through the origin.

The cleanest special case is

\[
\boxed{
Z_t
=
Z_0\sec(\theta_t)e^{i\theta_t},
\qquad
\theta_t
=
\arctan\!\left(\frac{X_t-X_0}{c}\right),
}
\]

where

\[
X_t=X_0+\mu t+\sigma W_t
\]

and

\[
Z_t
=
Z_0\left(1+i\frac{X_t-X_0}{c}\right).
\]

In the final state representation, neither \(t\) nor \(W_t\) appears explicitly:

\[
\boxed{
Z_t=Z_0\exp\!\left(\log\sec\theta_t+i\theta_t\right).
}
\]

All randomness is carried by the single real process \(\theta_t\), and

\[
\boxed{
r(\theta)=\sec\theta
}
\]

is deterministic.

For a literal standard Brownian motion in the real coordinate, the most direct exact form is

\[
\boxed{
ic+W_t
=
ic\,\sec\theta_t\,e^{i\theta_t},
\qquad
\theta_t=-\arctan\!\left(\frac{W_t}{c}\right),
}
\]

with inverse

\[
\boxed{
W_t=-c\tan\theta_t.
}
\]

---

# 2. What “only \(\theta_t\) is stochastic” means

There are three different requirements that can easily be conflated.

## 2.1 Ordinary polar decomposition

Every nonzero complex random variable can be written as

\[
Z_t=R_te^{i\Theta_t}.
\]

But in general both \(R_t\) and \(\Theta_t\) are stochastic variables.

That alone does not satisfy the stronger requirement.

## 2.2 Phase-only state representation

The stronger requirement is

\[
Z_t=Z_0r(\theta_t)e^{i\theta_t},
\]

where \(r\) is a fixed deterministic function. Once \(\theta_t\) is known, the radius is known automatically.

This means that the normalized process \(Z_t/Z_0\) is constrained to one deterministic polar curve,

\[
\Gamma_r
=
\left\{
r(\theta)e^{i\theta}:\theta\in I
\right\}.
\]

The complex state has two real coordinates, but it has only one stochastic degree of freedom.

## 2.3 Removing time from the stochastic law

It is not possible to remove time from the law of Brownian motion itself. Brownian variance is \(t\), so any stochastic evolution necessarily contains a time parameter somewhere.

What can be done is

\[
\boxed{
\text{remove explicit }t\text{ and }W_t
\text{ from the state map }Z_t=F(\theta_t).
}
\]

The phase process can then be defined intrinsically by its generator or transition kernel, without treating \(W_t\) as an additional state variable.

---

# 3. The exact secant construction

Let

\[
X_t=X_0+\mu t+\sigma W_t
\]

be arithmetic Brownian motion, and define

\[
Y_t=X_t-X_0=\mu t+\sigma W_t.
\]

Choose a constant

\[
c>0,
\]

and a nonzero complex initial value

\[
Z_0\neq0.
\]

Define

\[
\boxed{
Z_t
=
Z_0\left(1+i\frac{Y_t}{c}\right).
}
\]

This is an additive complex Brownian process because

\[
Z_t
=
Z_0+
\frac{i\mu Z_0}{c}t+
\frac{i\sigma Z_0}{c}W_t.
\]

Thus it has the form

\[
Z_t=Z_0+a t+bW_t
\]

with

\[
a=\frac{i\mu Z_0}{c},
\qquad
b=\frac{i\sigma Z_0}{c}.
\]

Now define

\[
\boxed{
\theta_t
=
\arctan\left(\frac{Y_t}{c}\right)
}
\]

with state space

\[
-\frac{\pi}{2}<\theta_t<\frac{\pi}{2}.
\]

Then

\[
\tan\theta_t=\frac{Y_t}{c}.
\]

Using the elementary identity

\[
1+i\tan\theta
=
\frac{\cos\theta+i\sin\theta}{\cos\theta}
=
\sec\theta\,e^{i\theta},
\]

we obtain

\[
\boxed{
Z_t
=
Z_0\sec\theta_t\,e^{i\theta_t}.
}
\]

This is an exact algebraic identity. It is not an approximation, asymptotic formula, or discretization scheme.

The inverse transformation is

\[
\boxed{
Y_t=c\tan\theta_t,
}
\]

and therefore

\[
\boxed{
X_t=X_0+c\tan\theta_t.
}
\]

The phase contains all the information in the original arithmetic Brownian motion.

More precisely, the filtrations generated by the two processes coincide:

\[
\boxed{
\sigma(\theta_s:0\le s\le t)
=
\sigma(X_s-X_0:0\le s\le t).
}
\]

Thus \(\theta\) is not merely correlated with the Brownian coordinate. It is an invertible reparameterization of it.

---

# 4. Keeping Brownian motion in the real coordinate

The preceding construction makes the Brownian coordinate the imaginary part of \(Z_t/Z_0\). To keep the arithmetic Brownian process literally in the real coordinate, define

\[
\widetilde Z_t
=
ic+X_t-X_0.
\]

Then

\[
\widetilde Z_t
=
ic+\mu t+\sigma W_t,
\]

and

\[
\widetilde Z_0=ic.
\]

Define

\[
\boxed{
\theta_t
=
-\arctan\left(\frac{X_t-X_0}{c}\right).
}
\]

Since

\[
ic\sec\theta_t e^{i\theta_t}
=
ic\left(1+i\tan\theta_t\right)
=
ic-c\tan\theta_t,
\]

and

\[
-c\tan\theta_t=X_t-X_0,
\]

we get

\[
\boxed{
ic+X_t-X_0
=
ic\,\sec\theta_t e^{i\theta_t}.
}
\]

For standard Brownian motion, set

\[
\mu=0,\qquad \sigma=1.
\]

Then

\[
\boxed{
ic+W_t
=
ic\,\sec\theta_t e^{i\theta_t},
\qquad
\theta_t=-\arctan\left(\frac{W_t}{c}\right).
}
\]

The Brownian motion is exactly recovered by

\[
\boxed{
W_t=-c\tan\theta_t.
}
\]

This is the closest literal realization of the desired objective.

The fixed imaginary offset \(ic\) is essential. It moves the Brownian line away from the origin, allowing every point on that line to have a unique geometric angle.

---

# 5. Geometric explanation

Consider the normalized process

\[
\frac{Z_t}{Z_0}
=
1+i\frac{Y_t}{c}.
\]

It lies on the vertical line

\[
\operatorname{Re}\left(\frac{Z_t}{Z_0}\right)=1.
\]

A point on this line can be described by either

\[
\frac{Y_t}{c},
\]

its vertical Cartesian coordinate, or by the angle \(\theta_t\) made by the ray from the origin.

For a ray at angle \(\theta\), the intersection with the line \(x=1\) has polar coordinates satisfying

\[
r\cos\theta=1.
\]

Therefore

\[
r=\frac{1}{\cos\theta}=\sec\theta.
\]

Hence

\[
\boxed{
r(\theta)=\sec\theta
}
\]

is simply the polar equation of a vertical line.

This also explains why the radius diverges as

\[
\theta\to\pm\frac{\pi}{2}.
\]

Those angular endpoints correspond to traveling to positive or negative infinity along the vertical line.

At every finite time, Brownian motion is finite, so

\[
-\frac{\pi}{2}<\theta_t<\frac{\pi}{2}
\]

almost surely.

---

# 6. General existence and classification theorem

Consider the general one-driver complex affine process

\[
Z_t=Z_0+a t+bW_t,
\]

where

\[
Z_0\neq0,\qquad a,b\in\mathbb C,\qquad b\neq0.
\]

Impose the following natural requirements:

1. \(\theta_t\) is real.
2. \(r(\theta)\) is real and nonnegative.
3. \(r\) is deterministic and single-valued.
4. \(r\) has no explicit time dependence.
5. The identity holds for the entire process, not merely at one fixed horizon.
6. \(\theta_t\) is a genuine phase, so its value modulo \(2\pi\) is the geometric argument of \(Z_t/Z_0\).
7. The representation is valid across the full support of the process, not only along one selected sample path.

Normalize:

\[
\frac{Z_t}{Z_0}
=
1+\alpha t+\gamma W_t,
\]

where

\[
\alpha=\frac{a}{Z_0},
\qquad
\gamma=\frac{b}{Z_0}.
\]

## The theorem

There exists a real phase process \(\theta_t\) and a deterministic, nonnegative, time-independent function \(r\) such that

\[
\frac{Z_t}{Z_0}
=
r(\theta_t)e^{i\theta_t}
\]

for the complete process if and only if

\[
\boxed{
\frac{a}{b}\in\mathbb R
}
\]

and

\[
\boxed{
\frac{b}{Z_0}\notin\mathbb R.
}
\]

An equivalent coordinate-free version of the second condition is

\[
\boxed{
\operatorname{Im}(b\overline{Z_0})\neq0.
}
\]

Geometrically:

- \(a/b\in\mathbb R\) means drift and diffusion point along one fixed real direction in the complex plane.
- \(\operatorname{Im}(b\overline{Z_0})\neq0\) means that the affine line has a nonzero perpendicular distance from the origin.

---

# 7. Explicit formula in the general case

Suppose

\[
a=\lambda b,
\qquad
\lambda\in\mathbb R.
\]

Write

\[
\gamma=\frac{b}{Z_0}
=
\rho e^{i\phi},
\qquad
\rho>0,
\]

where

\[
\sin\phi\neq0.
\]

Define

\[
x_t=\lambda t+W_t.
\]

Then

\[
\frac{Z_t}{Z_0}
=
1+\rho e^{i\phi}x_t.
\]

The process moves on the fixed affine line

\[
L=
\left\{
1+\rho e^{i\phi}x:x\in\mathbb R
\right\}.
\]

Let \(\theta_t\) be the continuous argument of

\[
1+\rho e^{i\phi}x_t,
\]

using the branch that contains

\[
\theta_0=0.
\]

The exact radial function is

\[
\boxed{
r(\theta)
=
\frac{\sin\phi}{\sin(\phi-\theta)}.
}
\]

Therefore

\[
\boxed{
Z_t
=
Z_0
\frac{\sin\phi}{\sin(\phi-\theta_t)}
e^{i\theta_t}.
}
\]

The inverse relation is

\[
\boxed{
x_t
=
\frac{\sin\theta_t}
{\rho\sin(\phi-\theta_t)}.
}
\]

Consequently,

\[
\boxed{
\lambda t+W_t
=
\frac{\sin\theta_t}
{\rho\sin(\phi-\theta_t)}.
}
\]

The single phase coordinate contains the full Brownian information.

## Derivation

Start from

\[
re^{i\theta}
=
1+\rho e^{i\phi}x.
\]

Multiply by \(e^{-i\phi}\):

\[
re^{i(\theta-\phi)}
=
e^{-i\phi}+\rho x.
\]

The right-hand side has constant imaginary part

\[
-\sin\phi.
\]

Therefore

\[
r\sin(\theta-\phi)
=
-\sin\phi.
\]

Hence

\[
r
=
-\frac{\sin\phi}{\sin(\theta-\phi)}
=
\frac{\sin\phi}{\sin(\phi-\theta)}.
\]

The special case

\[
\phi=\frac{\pi}{2}
\]

gives

\[
r(\theta)
=
\frac{1}{\cos\theta}
=
\sec\theta.
\]

The secant representation is therefore the perpendicular-line member of the general family.

---

# 8. The required angular domain

The formula

\[
r(\theta)
=
\frac{\sin\phi}{\sin(\phi-\theta)}
\]

is positive only on the angular interval corresponding to the side of the origin on which the line lies.

Choose

\[
\phi\in(-\pi,\pi)\setminus\{0\}.
\]

Then the correct interval is

\[
\boxed{
I_\phi
=
\begin{cases}
(\phi-\pi,\phi),&\sin\phi>0,\\[4pt]
(\phi,\phi+\pi),&\sin\phi<0.
\end{cases}
}
\]

This is the unique open interval of length \(\pi\) that contains \(0\) and on which

\[
\frac{\sin\phi}{\sin(\phi-\theta)}>0.
\]

At the initial state,

\[
r(0)=1.
\]

At either endpoint of \(I_\phi\),

\[
r(\theta)\to\infty.
\]

The phase never reaches those endpoints at finite time because doing so would require

\[
|x_t|=\infty.
\]

This domain restriction is an important qualification of the general formula.

---

# 9. Why the two existence conditions are necessary

## 9.1 Drift and diffusion must be collinear

At each fixed time \(t\), the support of \(Z_t\) is the affine line

\[
Z_0+a t+b\mathbb R.
\]

If \(a\) and \(b\) are linearly independent as vectors in

\[
\mathbb R^2\simeq\mathbb C,
\]

then the union

\[
\left\{
Z_0+a t+bw:t>0,\ w\in\mathbb R
\right\}
\]

has nonempty two-dimensional interior. It is an affine half-plane or strip-type region, depending on the time domain.

By contrast, a phase graph

\[
\Gamma_r
=
\left\{
Z_0r(\theta)e^{i\theta}:\theta\in\mathbb R
\right\}
\]

cannot contain a two-dimensional region.

For any fixed geometric ray with angle \(\psi\), the possible unwrapped phase values are only

\[
\psi+2\pi k,
\qquad
k\in\mathbb Z.
\]

A single-valued \(r\) therefore gives at most countably many points on any one ray. A two-dimensional open region contains an interval of radii on every ray passing through its interior.

Therefore a phase-only graph cannot contain the complete support unless

\[
a=\lambda b
\]

for some real \(\lambda\).

Equivalently,

\[
\boxed{
\frac{a}{b}\in\mathbb R.
}
\]

## 9.2 The fixed affine line cannot pass through the origin

Once

\[
a=\lambda b,
\]

the complete process lies on

\[
L=Z_0+b\mathbb R.
\]

This line passes through the origin if and only if there exists an \(x\in\mathbb R\) such that

\[
Z_0+bx=0.
\]

That is equivalent to

\[
-\frac{Z_0}{b}\in\mathbb R,
\]

or

\[
\frac{b}{Z_0}\in\mathbb R.
\]

If the line passes through the origin, it contains continuously many points on the same positive ray and continuously many points on the opposite ray. A phase value identifies the direction but cannot identify the continuously varying magnitude.

Therefore the line must avoid the origin:

\[
\boxed{
\frac{b}{Z_0}\notin\mathbb R.
}
\]

---

# 10. Uniqueness of the phase representation

When the affine line does not pass through the origin, the phase construction is essentially unique.

Let

\[
z(x)=1+\gamma x.
\]

The derivative of the argument is

\[
\frac{d}{dx}\arg z(x)
=
\operatorname{Im}\left(\frac{\gamma}{1+\gamma x}\right).
\]

Since

\[
\operatorname{Im}\left(
\frac{\gamma}{1+\gamma x}
\right)
=
\frac{\operatorname{Im}\gamma}{|1+\gamma x|^2},
\]

we have

\[
\boxed{
\frac{d\theta}{dx}
=
\frac{\operatorname{Im}\gamma}
{|1+\gamma x|^2}.
}
\]

If

\[
\operatorname{Im}\gamma\neq0,
\]

this derivative never vanishes.

Thus the map

\[
x\longmapsto\theta
\]

is strictly monotone and gives a bijection from \(\mathbb R\) to the angular interval \(I_\phi\).

Consequently:

- the continuous phase is uniquely determined after choosing \(\theta_0=0\);
- the radius is necessarily \(|1+\gamma x|\);
- eliminating \(x\) necessarily gives

\[
r(\theta)
=
\frac{\sin\phi}{\sin(\phi-\theta)}.
\]

The secant/cosecant form is not merely one arbitrary construction. It is the natural and essentially unique polar form of a fixed affine line that does not pass through the origin.

---

# 11. Phase dynamics in the secant case

Return to

\[
Y_t=\mu t+\sigma W_t
\]

and

\[
\theta_t
=
\arctan\left(\frac{Y_t}{c}\right).
\]

Let

\[
f(y)=\arctan(y/c).
\]

Then

\[
f'(y)=\frac{c}{c^2+y^2},
\]

and

\[
f''(y)
=
-\frac{2cy}{(c^2+y^2)^2}.
\]

Using

\[
y=c\tan\theta,
\]

we obtain

\[
f'(y)
=
\frac{1}{c}\cos^2\theta,
\]

and

\[
\frac12f''(y)
=
-\frac{1}{c^2}\sin\theta\cos^3\theta.
\]

Applying Itô's formula gives

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
\]

In Stratonovich form, the correction is absorbed:

\[
\boxed{
d\theta_t
=
\frac{\mu}{c}\cos^2\theta_t\,dt
+
\frac{\sigma}{c}\cos^2\theta_t\circ dW_t.
}
\]

For standard Brownian motion,

\[
\mu=0,\qquad \sigma=1,
\]

so

\[
\boxed{
d\theta_t
=
-\frac{1}{c^2}
\sin\theta_t\cos^3\theta_t\,dt
+
\frac{1}{c}
\cos^2\theta_t\,dW_t.
}
\]

The nonlinear drift is precisely the Itô correction generated by the arctangent transformation.

---

# 12. Defining \(\theta_t\) without explicitly defining \(W_t\)

The phase can be made the primitive process and defined by its infinitesimal generator.

For a smooth test function \(f\),

\[
\boxed{
\begin{aligned}
\mathcal L_\theta f(\theta)
={}&
\left[
\frac{\mu}{c}\cos^2\theta
-
\frac{\sigma^2}{c^2}
\sin\theta\cos^3\theta
\right]f'(\theta)\\
&+
\frac{\sigma^2}{2c^2}
\cos^4\theta\,f''(\theta).
\end{aligned}
}
\]

Take the state space to be

\[
I=\left(-\frac{\pi}{2},\frac{\pi}{2}\right)
\]

and the initial condition

\[
\theta_0=0.
\]

The phase process can be defined as the diffusion solving the martingale problem associated with this generator.

Then define

\[
\boxed{
Z_t=Z_0\sec\theta_t e^{i\theta_t}.
}
\]

This is a mathematically complete phase-first construction. \(W_t\) need not appear in the definition of the state.

The inverse coordinate

\[
X_t=X_0+c\tan\theta_t
\]

has generator

\[
\mathcal L_X f(x)
=
\mu f'(x)+\frac{\sigma^2}{2}f''(x),
\]

so it is arithmetic Brownian motion.

Therefore,

\[
\boxed{
\text{the phase diffusion and arithmetic Brownian motion are isomorphic Markov processes.}
}
\]

---

# 13. Verification by reconstructing the additive SDE

Define

\[
F(\theta)
=
\sec\theta\,e^{i\theta}.
\]

On the interval

\[
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
\]

we have

\[
F(\theta)=1+i\tan\theta.
\]

Therefore

\[
F'(\theta)=i\sec^2\theta,
\]

and

\[
F''(\theta)=2i\sec^2\theta\tan\theta.
\]

Write the phase SDE as

\[
d\theta_t=A(\theta_t)dt+B(\theta_t)dW_t,
\]

where

\[
A(\theta)
=
\frac{\mu}{c}\cos^2\theta
-
\frac{\sigma^2}{c^2}\sin\theta\cos^3\theta
\]

and

\[
B(\theta)
=
\frac{\sigma}{c}\cos^2\theta.
\]

Applying Itô's formula to

\[
Z_t=Z_0F(\theta_t)
\]

gives

\[
dF(\theta_t)
=
F'(\theta_t)d\theta_t
+
\frac12F''(\theta_t)B(\theta_t)^2dt.
\]

The two \(\sigma^2\)-drift terms cancel exactly, leaving

\[
dF(\theta_t)
=
\frac{i\mu}{c}dt+
\frac{i\sigma}{c}dW_t.
\]

Hence

\[
\boxed{
dZ_t
=
\frac{i\mu Z_0}{c}dt+
\frac{i\sigma Z_0}{c}dW_t.
}
\]

This reconstructs exactly

\[
Z_t
=
Z_0+
\frac{i\mu Z_0}{c}t+
\frac{i\sigma Z_0}{c}W_t.
\]

The nonlinear phase SDE is therefore not merely compatible with the additive process; it reproduces it exactly.

---

# 14. Exact transition law of the phase

Since

\[
Y_t=c\tan\theta_t,
\]

conditional on

\[
\theta_s=\theta,
\]

we have

\[
Y_{s+h}
=
c\tan\theta+\mu h+\sigma\sqrt h\,\xi,
\]

where

\[
\xi\sim N(0,1).
\]

Therefore the exact transition is

\[
\boxed{
\theta_{s+h}
=
\arctan\left(
\tan\theta_s+
\frac{\mu}{c}h+
\frac{\sigma}{c}\sqrt h\,\xi
\right).
}
\]

This is exact. It is not Euler–Maruyama.

For \(\sigma\neq0\), the transition density is

\[
\boxed{
p_h(\vartheta\mid\theta)
=
\frac{
c\sec^2\vartheta
}{
|\sigma|\sqrt{2\pi h}
}
\exp\left[
-\frac{
\left(
c\tan\vartheta-c\tan\theta-\mu h
\right)^2
}{
2\sigma^2h
}
\right]
}
\]

for

\[
-\frac{\pi}{2}<\vartheta<\frac{\pi}{2}.
\]

Starting from

\[
\theta_0=0,
\]

the marginal density is

\[
\boxed{
p_t(\theta)
=
\frac{
c\sec^2\theta
}{
|\sigma|\sqrt{2\pi t}
}
\exp\left[
-\frac{
(c\tan\theta-\mu t)^2
}{
2\sigma^2t
}
\right].
}
\]

This transition kernel defines the phase process without explicitly referring to an underlying Brownian path.

Time \(h\) still appears because a stochastic process must evolve in time. What has been eliminated is the need for \(t\) and \(W_t\) to appear in the complex state map.

---

# 15. General phase dynamics

For the general eligible process, write

\[
\frac{b}{Z_0}
=
\rho e^{i\phi},
\qquad
\frac{a}{b}=\lambda\in\mathbb R,
\]

and

\[
x_t=\lambda t+W_t.
\]

Recall that

\[
\theta(x)
=
\arg(1+\rho e^{i\phi}x).
\]

Define

\[
\boxed{
g(\theta)
=
\frac{
\rho\sin^2(\phi-\theta)
}{
\sin\phi
}.
}
\]

Then

\[
\frac{d\theta}{dx}=g(\theta).
\]

Its derivative is

\[
g'(\theta)
=
-\frac{
2\rho\sin(\phi-\theta)\cos(\phi-\theta)
}{
\sin\phi
}.
\]

The phase SDE is

\[
\boxed{
d\theta_t
=
\left[
\lambda g(\theta_t)
+
\frac12g(\theta_t)g'(\theta_t)
\right]dt
+
g(\theta_t)dW_t.
}
\]

Expanded,

\[
\boxed{
\begin{aligned}
d\theta_t
={}&
\left[
\lambda
\frac{\rho\sin^2(\phi-\theta_t)}{\sin\phi}
-
\frac{
\rho^2
\sin^3(\phi-\theta_t)
\cos(\phi-\theta_t)
}{
\sin^2\phi
}
\right]dt\\
&+
\frac{
\rho\sin^2(\phi-\theta_t)
}{
\sin\phi
}
dW_t.
\end{aligned}
}
\]

In Stratonovich form,

\[
\boxed{
d\theta_t
=
\lambda g(\theta_t)dt
+
g(\theta_t)\circ dW_t.
}
\]

The inverse phase coordinate is

\[
\boxed{
x(\theta)
=
\frac{
\sin\theta
}{
\rho\sin(\phi-\theta)
}.
}
\]

Its derivative is

\[
\frac{dx}{d\theta}
=
\frac{\sin\phi}
{\rho\sin^2(\phi-\theta)}.
\]

Therefore the exact transition density is

\[
\boxed{
\begin{aligned}
p_h(\vartheta\mid\theta)
={}&
\frac{
|\sin\phi|
}{
\rho\sin^2(\phi-\vartheta)\sqrt{2\pi h}
}\\
&\times
\exp\left[
-\frac{
\left(
x(\vartheta)-x(\theta)-\lambda h
\right)^2
}{
2h
}
\right].
\end{aligned}
}
\]

This gives a complete phase-only Markov formulation for every affine process satisfying the two existence conditions.

---

# 16. Why literal real Brownian motion cannot do this directly

Suppose

\[
Z_t=Z_0+a t+bW_t
\]

with

\[
Z_0,a,b\in\mathbb R
\]

and

\[
b\neq0.
\]

Then \(Z_t\) lies on the real axis.

Its ordinary polar angle is only

\[
0
\]

when

\[
Z_t>0,
\]

or

\[
\pi
\]

when

\[
Z_t<0.
\]

Thus its ordinary polar phase contains only the sign of the process. It does not contain its continuously varying magnitude.

The standard polar representation is

\[
Z_t
=
|Z_t|
e^{i\pi\mathbf 1_{\{Z_t<0\}}},
\]

but the radius

\[
|Z_t|
\]

remains an independent stochastic quantity. It is not a deterministic function of the two-valued phase.

Allowing an unwrapped phase does not solve the issue. On the positive ray,

\[
\theta=2\pi k,
\qquad
k\in\mathbb Z,
\]

and on the negative ray,

\[
\theta=\pi+2\pi k.
\]

There are only countably many such phase values, while the Brownian magnitude has uncountably many possible values.

Therefore,

\[
\boxed{
\text{a nondegenerate real-axis Brownian process cannot be encoded losslessly by its ordinary polar angle alone.}
}
\]

There is also an immediate obstruction if the literal standard Brownian motion is written as

\[
Z_t=W_t.
\]

Then

\[
Z_0=0,
\]

and a representation with multiplicative prefactor \(Z_0\) gives

\[
Z_0r(\theta_t)e^{i\theta_t}=0
\]

for every \(t\), which cannot equal nontrivial Brownian motion.

A nonzero perpendicular offset such as \(ic\) resolves both obstructions.

The wrapped process

\[
e^{iW_t}
\]

does put Brownian motion into a phase, but it is not equal to \(W_t\) and loses information modulo \(2\pi\).

---

# 17. Why \(r(\theta)\) cannot be constant for the same additive process

Suppose

\[
r(\theta)\equiv r_0.
\]

Then

\[
|Z_t|=|Z_0|r_0
\]

would be constant.

At any fixed time \(t>0\), Brownian motion has support on all of \(\mathbb R\). Therefore

\[
|Z_0+a t+bw|^2
\]

would have to be constant as a function of \(w\).

But

\[
|Z_0+a t+bw|^2
=
|b|^2w^2
+
2\operatorname{Re}\!\left((Z_0+a t)\overline b\right)w
+
|Z_0+a t|^2.
\]

For this polynomial to be constant for every \(w\), its quadratic coefficient must vanish:

\[
|b|^2=0.
\]

Hence

\[
b=0.
\]

Then constant modulus for the remaining deterministic affine path

\[
Z_t=Z_0+a t
\]

for every \(t\) similarly forces

\[
a=0.
\]

Thus

\[
\boxed{
r(\theta)\text{ can be constant for the original additive process only when }a=b=0.
}
\]

A nontrivial affine Brownian line cannot lie on a circle.

---

# 18. Constant-radius encoding through the Cayley transform

Although the original additive process cannot have constant radius, Brownian motion can be transformed invertibly into a unit-circle process.

Let

\[
Y_t=\mu t+\sigma W_t.
\]

Define

\[
\boxed{
U_t
=
\frac{1+iY_t/c}{1-iY_t/c}.
}
\]

Because the denominator is the complex conjugate of the numerator,

\[
|U_t|=1.
\]

Using the tangent half-angle identity,

\[
\frac{1+i\tan u}{1-i\tan u}
=
e^{2iu},
\]

we obtain

\[
\boxed{
U_t=e^{i\Theta_t},
\qquad
\Theta_t
=
2\arctan\left(\frac{Y_t}{c}\right).
}
\]

The inverse is

\[
\boxed{
Y_t=c\tan\left(\frac{\Theta_t}{2}\right).
}
\]

This is an injective, lossless, constant-radius phase encoding of the real line.

The state space is

\[
-\pi<\Theta_t<\pi.
\]

The missing point

\[
U=-1
\]

corresponds to infinity. Since \(Y_t\) is finite at every finite time,

\[
U_t\neq-1
\]

at every finite time.

This is the inverse stereographic or Cayley compactification of the real line.

The important qualification is

\[
\boxed{
U_t\text{ is not the original additive process. It is an invertible nonlinear transformation of it.}
}
\]

---

# 19. Dynamics of the Cayley phase

Since

\[
\Theta_t
=
2\arctan(Y_t/c),
\]

Itô's formula gives

\[
\boxed{
\begin{aligned}
d\Theta_t
={}&
\left[
\frac{2\mu}{c}
\cos^2\frac{\Theta_t}{2}
-
\frac{2\sigma^2}{c^2}
\sin\frac{\Theta_t}{2}
\cos^3\frac{\Theta_t}{2}
\right]dt\\
&+
\frac{2\sigma}{c}
\cos^2\frac{\Theta_t}{2}\,dW_t.
\end{aligned}
}
\]

In Stratonovich form,

\[
\boxed{
d\Theta_t
=
\frac{2\mu}{c}
\cos^2\frac{\Theta_t}{2}\,dt
+
\frac{2\sigma}{c}
\cos^2\frac{\Theta_t}{2}\circ dW_t.
}
\]

For standard Brownian motion,

\[
\mu=0,\qquad \sigma=1.
\]

Then the angular diffusion coefficient is

\[
\frac{2}{c}\cos^2\frac{\Theta}{2}.
\]

It tends to zero as

\[
\Theta\to\pm\pi.
\]

Thus the missing point is inaccessible in finite time.

This process is not ordinary Brownian motion on the circle. Circular Brownian motion has constant angular diffusion, whereas the stereographic/Cayley image has a state-dependent coefficient that slows down near the missing point.

The exact Cayley-phase transition is

\[
\boxed{
\Theta_{s+h}
=
2\arctan\left[
\tan\frac{\Theta_s}{2}
+
\frac{\mu}{c}h
+
\frac{\sigma}{c}\sqrt h\,\xi
\right],
}
\]

where

\[
\xi\sim N(0,1).
\]

---

# 20. SDE for the unit-circle process

Let

\[
U_t
=
\frac{c+iY_t}{c-iY_t},
\]

where

\[
dY_t=\mu\,dt+\sigma\,dW_t.
\]

Direct differentiation gives

\[
\boxed{
\begin{aligned}
dU_t
={}&
\left[
\frac{i\mu}{2c}(1+U_t)^2
-
\frac{\sigma^2}{4c^2}(1+U_t)^3
\right]dt\\
&+
\frac{i\sigma}{2c}(1+U_t)^2\,dW_t.
\end{aligned}
}
\]

In Stratonovich form,

\[
\boxed{
dU_t
=
\frac{i\mu}{2c}(1+U_t)^2dt
+
\frac{i\sigma}{2c}(1+U_t)^2\circ dW_t.
}
\]

Although this SDE looks complex and nonlinear, its solution remains exactly on the unit circle because it is the Cayley transform of a real process.

---

# 21. Exact addition in the phase coordinate

For the secant representation, define

\[
\Theta_c(x)=\arctan(x/c).
\]

Then

\[
x=c\tan\Theta_c(x).
\]

For \(x,y\in\mathbb R\),

\[
\Theta_c(x+y)
=
\arctan\left(
\tan\Theta_c(x)+\tan\Theta_c(y)
\right).
\]

Define

\[
\boxed{
\theta_1\oplus\theta_2
=
\arctan\left(
\tan\theta_1+\tan\theta_2
\right).
}
\]

Then

\[
\boxed{
\Theta_c(x+y)
=
\Theta_c(x)\oplus\Theta_c(y).
}
\]

On

\[
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
\]

the operation \(\oplus\) is

- associative;
- commutative;
- equipped with identity \(0\);
- equipped with inverse \(-\theta\).

This follows because \(\oplus\) is ordinary addition transported through the bijection

\[
x\longleftrightarrow\arctan(x/c).
\]

For Brownian increments,

\[
\theta_{\mathrm{total}}
=
\arctan\left(
\sum_j\tan\theta_j
\right).
\]

The phase interval is therefore a nonlinear coordinate version of the additive real line.

For the Cayley phase, the corresponding operation is

\[
\boxed{
\Theta_1\boxplus\Theta_2
=
2\arctan\left[
\tan\frac{\Theta_1}{2}
+
\tan\frac{\Theta_2}{2}
\right].
}
\]

This is not ordinary angular addition.

---

# 22. A fundamental impossibility theorem

There are three attractive properties one might hope to obtain simultaneously:

1. constant radius;
2. lossless recovery of the real coordinate;
3. ordinary real addition becoming ordinary complex multiplication.

These three properties cannot coexist in a single continuous phase on the unit circle.

Suppose

\[
F:\mathbb R\to S^1
\]

is continuous and satisfies

\[
F(x+y)=F(x)F(y).
\]

Because \(\mathbb R\) is simply connected, write

\[
F(x)=e^{if(x)}
\]

for a continuous real lift \(f\) satisfying

\[
f(0)=0.
\]

The homomorphism property implies

\[
f(x+y)-f(x)-f(y)\in2\pi\mathbb Z.
\]

The left side is continuous in \((x,y)\), so it must be identically zero. Therefore

\[
f(x+y)=f(x)+f(y).
\]

A continuous additive function is linear:

\[
f(x)=\kappa x.
\]

Hence

\[
F(x)=e^{i\kappa x}.
\]

If

\[
\kappa\neq0,
\]

then

\[
F\left(x+\frac{2\pi}{\kappa}\right)=F(x),
\]

so \(F\) is not injective.

If

\[
\kappa=0,
\]

then \(F\) is constant.

Consequently,

\[
\boxed{
\text{there is no continuous injective homomorphism from }(\mathbb R,+)\text{ into the one-dimensional unit circle.}
}
\]

The resulting structural tradeoff is:

| Encoding | Constant radius | Injective | Addition becomes multiplication |
|---|---:|---:|---:|
| \(e^{i\kappa x}\) | Yes | No | Yes |
| Cayley transform | Yes | Yes | No; it uses \(\boxplus\) |
| \(e^{(\alpha+i\beta)x}\), \(\alpha\neq0\) | No | Yes | Yes |
| \(1+ix/c=\sec\theta\,e^{i\theta}\) | No | Yes | No; it uses \(\oplus\) |

The changing radius in a logarithmic spiral is exactly what allows the exponential map

\[
e^{(\alpha+i\beta)x}
\]

to remain injective while preserving multiplication.

---

# 23. Relationship to the earlier complex-GBM construction

The earlier complex-geometric-Brownian-motion construction used

\[
Z_t
=
Z_0e^{\kappa t+BW_t}.
\]

There, one scalar Brownian coordinate is mapped through the exponential to a logarithmic spiral or another one-dimensional complex support curve.

The additive and multiplicative constructions can be contrasted as follows.

## 23.1 Additive affine geometry

The map

\[
x\longmapsto1+i\frac{x}{c}
\]

sends the real line to an affine line in the complex plane.

Its polar law is

\[
\boxed{
r(\theta)=\sec\theta.
}
\]

More generally, an affine line not passing through the origin has

\[
\boxed{
r(\theta)
=
\frac{\sin\phi}{\sin(\phi-\theta)}.
}
\]

## 23.2 Multiplicative exponential geometry

The map

\[
x\longmapsto e^{(\alpha+i\beta)x}
\]

sends the real line to a logarithmic spiral.

When

\[
\beta\neq0,
\]

we have

\[
\theta=\beta x,
\]

and

\[
r=e^{\alpha x}
=
e^{(\alpha/\beta)\theta}.
\]

Thus its polar law is

\[
\boxed{
r(\theta)=e^{(\alpha/\beta)\theta}.
}
\]

Both processes are one-dimensional in stochastic content:

- the additive process traces an affine line;
- the multiplicative process traces a logarithmic spiral;
- in both cases the radius is a deterministic function of phase;
- neither construction creates a second independent Brownian coordinate.

---

# 24. Connection to projected-normal distributions

At a fixed time, the vector

\[
\left(
1,\frac{Y_t}{c}
\right)
\]

is an affine Gaussian vector supported on a line.

Dividing it by its Euclidean norm produces the unit direction

\[
(\cos\theta_t,\sin\theta_t).
\]

This is closely related to the projected-normal or angular-Gaussian construction, in which a multivariate Gaussian vector is normalized onto a sphere.

The standard projected-normal literature usually considers a nondegenerate multivariate Gaussian. The present construction is a singular, rank-one affine case with an especially simple closed form.

The phase density is simple because the inverse map is explicit:

\[
Y=c\tan\theta.
\]

Its Jacobian is

\[
\frac{dY}{d\theta}=c\sec^2\theta,
\]

which directly produces the exact phase density derived above.

The Cayley form is likewise a stereographic compactification of the real line onto the unit circle with one point removed.

---

# 25. Assessment and refinements of the attached solution

The attached proposed solution is mathematically strong. Its central claims survive detailed checking.

| Claim in the attached solution | Assessment |
|---|---|
| \(1+i\tan\theta=\sec\theta e^{i\theta}\) | Correct |
| Exact recovery \(X_t=X_0+c\tan\theta_t\) | Correct |
| Phase SDE and its Itô correction | Correct |
| Exact phase transition kernel | Correct |
| Transported addition operation \(\oplus\) | Correct |
| General condition \(a/b\in\mathbb R\) | Correct for a time-independent representation of the whole process |
| General condition \(b/Z_0\notin\mathbb R\) | Correct |
| General radius \(\sin\phi/\sin(\phi-\theta)\) | Correct |
| Real-axis phase-only impossibility | Correct under the ordinary polar-phase requirement |
| Constant-radius Cayley encoding | Correct |
| Constant radius for the original affine process | Impossible except for \(a=b=0\) |

The following refinements should be made explicit.

## 25.1 Specify the phase domain

The formula

\[
r(\theta)
=
\frac{\sin\phi}{\sin(\phi-\theta)}
\]

must be restricted to the unique interval \(I_\phi\) of length \(\pi\) containing \(0\) on which \(r>0\).

## 25.2 State the assumptions behind the “if and only if”

The classification assumes:

- a real phase;
- a nonnegative, single-valued radius;
- no explicit time dependence in \(r\);
- representation of the complete process;
- a deterministic representation valid across the full process support;
- ordinary geometric phase modulo \(2\pi\).

## 25.3 Distinguish representation from transformation

The Cayley process

\[
U_t=\frac{1+iY_t/c}{1-iY_t/c}
\]

is not equal to the original additive process. It is a lossless nonlinear encoding of it.

## 25.4 Scope the real-Brownian impossibility claim

The real-axis process itself cannot store magnitude in its ordinary polar phase. A fixed nonreal offset such as

\[
ic+W_t
\]

does permit the phase-only representation.

Also,

\[
e^{iW_t}
\]

puts Brownian motion into a phase but loses information modulo \(2\pi\) and is not equal to the original additive state.

## 25.5 Literature reference caution

The final literature link in the attached note should be checked carefully before being cited as the specific source of this construction.

Cleaner literature anchors are:

- Itô's change-of-variables formula for the phase SDE;
- stereographic and Cayley geometry for the compactification;
- projected-normal literature for Gaussian directions on spheres;
- the earlier complex-GBM paper for the one-driver rank-one support comparison.

---

# 26. Novelty and mathematical positioning

The individual ingredients are classical:

- the polar equation of a line;
- the identity

  \[
  1+i\tan\theta=\sec\theta e^{i\theta};
  \]

- the arctangent coordinate on the real line;
- the Cayley transform;
- Itô's formula under smooth coordinate changes;
- projected-normal angular distributions;
- stereographic compactification.

The exact full-process classification theorem

\[
\frac{a}{b}\in\mathbb R,
\qquad
\frac{b}{Z_0}\notin\mathbb R
\]

is a direct consequence of affine-line geometry and the fact that a single-valued polar graph cannot contain a two-dimensional region.

The theorem may be a useful original synthesis, but failing to find the exact statement in selected sources would not prove that it has never appeared elsewhere.

The most defensible research contribution would be framed as follows:

> **A complete classification of time-independent phase-only polar representations of scalar-driven affine complex diffusions, together with their exact phase generators, transition kernels, transported group operations, and constant-radius compactifications.**

That is stronger and more precise than claiming a new form of Brownian motion.

The principal value is not that Brownian motion itself has changed. Rather, the value lies in:

- identifying the exact geometric condition under which an affine complex diffusion has a one-phase polar representation;
- deriving the unique radial law;
- obtaining the intrinsic phase generator and transition density;
- separating exact representation from nonlinear compactification;
- proving the constant-radius/injectivity/homomorphism tradeoff;
- connecting additive affine geometry to multiplicative logarithmic-spiral geometry.

---

# 27. Final result

For a standard real Brownian motion, the cleanest exact phase-only Euler representation is

\[
\boxed{
ic+W_t
=
ic\,\sec\theta_t e^{i\theta_t},
\qquad
\theta_t=-\arctan(W_t/c).
}
\]

Equivalently,

\[
\boxed{
W_t=-c\tan\theta_t.
}
\]

A completely phase-first definition is obtained by taking \(\theta_t\) to be the diffusion on

\[
-\frac{\pi}{2}<\theta<\frac{\pi}{2}
\]

with initial condition

\[
\theta_0=0
\]

and generator

\[
\boxed{
\mathcal L_\theta f(\theta)
=
-\frac{1}{c^2}
\sin\theta\cos^3\theta\,f'(\theta)
+
\frac{1}{2c^2}
\cos^4\theta\,f''(\theta).
}
\]

Then define

\[
\boxed{
Z_t
=
Z_0\sec\theta_t e^{i\theta_t}.
}
\]

For the fully general process

\[
Z_t=Z_0+a t+bW_t,
\]

the exact phase-only representation exists for the entire process precisely when

\[
\boxed{
\frac{a}{b}\in\mathbb R
\quad\text{and}\quad
\frac{b}{Z_0}\notin\mathbb R.
}
\]

When

\[
\frac b{Z_0}=\rho e^{i\phi},
\]

the representation is

\[
\boxed{
Z_t
=
Z_0
\frac{\sin\phi}{\sin(\phi-\theta_t)}
e^{i\theta_t},
}
\]

with inverse

\[
\boxed{
\frac{a}{b}t+W_t
=
\frac{\sin\theta_t}
{\rho\sin(\phi-\theta_t)}.
}
\]

A constant radius is impossible for the same nontrivial additive process.

The exact constant-radius alternative is the transformed Cayley encoding

\[
\boxed{
U_t
=
\frac{1+iY_t/c}{1-iY_t/c}
=
e^{i\Theta_t},
\qquad
Y_t=c\tan\frac{\Theta_t}{2}.
}
\]

Therefore the requested representation is achievable exactly, but the minimal geometric requirement is that the Brownian affine line be displaced away from the origin.

---

# 28. References and related sources

## Source documents reviewed

- `possible_solution.md` — the proposed secant, general affine-line, and Cayley construction.
- `phase4-native-complex-geometric-brownian-motion.pdf` — the earlier one-driver complex-GBM construction and rank-one stochastic-geometry analysis.

## Mathematical references

1. **Kiyosi Itô (1951), “On a Formula Concerning Stochastic Differentials.”**  
   Foundational source for the stochastic change-of-variables formula used to derive the phase SDE.  
   DOI: <https://doi.org/10.1017/S0027763000012216>

2. **Brownian motion and stereographic projection.**  
   Related geometric literature on mapping Euclidean Brownian paths to spheres through stereographic projection, including the role of time changes and conditioning.  
   EuDML record: <https://eudml.org/doc/77256>

3. **The General Projected Normal Distribution of Arbitrary Dimension: Modeling and Bayesian Inference.**  
   Related literature on normalizing Gaussian vectors to obtain angular distributions on spheres.  
   Project Euclid: <https://projecteuclid.org/journals/bayesian-analysis/volume-12/issue-1/The-General-Projected-Normal-Distribution-of-Arbitrary-Dimension--Modeling/10.1214/15-BA989.full>

4. **Earlier complex-GBM analysis.**  
   The multiplicative construction

   \[
   Z_t=Z_0e^{\kappa t+BW_t}
   \]

   gives a logarithmic-spiral analogue of the affine-line construction. Both retain only one Brownian stochastic degree of freedom when driven by one real Brownian motion.
