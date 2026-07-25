Yes. There is an exact construction that gets very close to what you want, and there is also a precise theorem describing when your requested form is possible for an arbitrary additive complex Brownian process.

The key distinction is this:

* A **real Brownian motion itself** cannot have all its randomness stored in its ordinary polar angle, because it lies on the real axis and its geometric angle is only (0) or (\pi).
* A **complex affine lift** of that Brownian motion, placed on a line that does not pass through the origin, can be represented exactly as
  [
  Z_t=Z_0,r(\theta_t)e^{i\theta_t},
  ]
  where (r) is a deterministic function of the single stochastic phase (\theta_t).
* The cleanest choice gives
  [
  \boxed{Z_t=Z_0\sec(\theta_t)e^{i\theta_t}}.
  ]

This is not an approximation.

# 1. Exact one-phase Euler representation

Start with the real arithmetic Brownian motion

[
X_t=X_0+\mu t+\sigma W_t.
]

Let

[
Y_t=X_t-X_0=\mu t+\sigma W_t.
]

Choose any scale (c>0) and any nonzero complex initial value (Z_0). Define the complex affine lift

[
Z_t
===

Z_0\left(1+i\frac{Y_t}{c}\right).
]

Expanded out,

[
Z_t
===

Z_0
+
\frac{i\mu Z_0}{c}t
+
\frac{i\sigma Z_0}{c}W_t.
]

Thus it is exactly of the requested additive form

[
Z_t=Z_0+a t+bW_t,
]

with

[
a=\frac{i\mu Z_0}{c},
\qquad
b=\frac{i\sigma Z_0}{c}.
]

Now define the single stochastic phase

[
\boxed{
\theta_t=\arctan\left(\frac{X_t-X_0}{c}\right)
}
]

with

[
-\frac{\pi}{2}<\theta_t<\frac{\pi}{2}.
]

Because

[
\tan\theta_t=\frac{X_t-X_0}{c},
]

we have

[
1+i\frac{X_t-X_0}{c}
====================

1+i\tan\theta_t.
]

But

[
1+i\tan\theta
=============

# \frac{\cos\theta+i\sin\theta}{\cos\theta}

\sec\theta,e^{i\theta}.
]

Therefore

[
\boxed{
Z_t
===

Z_0\sec(\theta_t)e^{i\theta_t}.
}
]

Equivalently, as a single exponential,

[
\boxed{
Z_t
===

Z_0
\exp\left[
\log\sec(\theta_t)+i\theta_t
\right].
}
]

There is no explicit (t) or (W_t) in this final state representation. The only stochastic state variable is (\theta_t), and the radius is the deterministic function

[
\boxed{r(\theta)=\sec\theta.}
]

The original Brownian motion is exactly recoverable:

[
\boxed{
X_t=X_0+c\tan\theta_t.
}
]

So this representation loses no information.

# 2. Geometric interpretation

The normalized process

[
\frac{Z_t}{Z_0}
===============

1+i\frac{X_t-X_0}{c}
]

moves on the vertical line

[
\operatorname{Re}\left(\frac{Z_t}{Z_0}\right)=1.
]

A point on that line can be described either by its vertical coordinate

[
\frac{X_t-X_0}{c},
]

or by the angle that the ray from the origin makes with the positive real axis.

For a ray at angle (\theta), the intersection with the line (x=1) has radius

[
r\cos\theta=1,
]

hence

[
r=\frac1{\cos\theta}=\sec\theta.
]

That is why the formula is so simple:

[
1+i\tan\theta=\sec\theta e^{i\theta}.
]

This is ordinary polar geometry applied to a line that does not pass through the origin.

# 3. A version that leaves Brownian motion in the real coordinate

Perhaps you want the actual Brownian process to remain the real part. Then take

[
\widetilde Z_t=ic+X_t-X_0.
]

Since

[
\widetilde Z_0=ic,
]

define

[
\theta_t
========

-\arctan\left(\frac{X_t-X_0}{c}\right).
]

Then

[
ic,\sec\theta_t e^{i\theta_t}
=============================

# ic-c\tan\theta_t

ic+X_t-X_0.
]

Therefore

[
\boxed{
ic+X_t-X_0
==========

ic,\sec(\theta_t)e^{i\theta_t},
\qquad
\theta_t=-\arctan\left(\frac{X_t-X_0}{c}\right).
}
]

Here the real part is exactly (X_t-X_0), while the constant imaginary coordinate (c) prevents the line from passing through the origin.

That constant perpendicular offset is essential.

# 4. Dynamics of the single phase variable

Although (t) and (W_t) disappear from the state representation

[
Z_t=Z_0\sec\theta_t e^{i\theta_t},
]

the phase must still evolve randomly.

From

[
\theta_t
========

\arctan\left(\frac{X_t-X_0}{c}\right),
]

we have

[
f'(x)=\frac{c}{c^2+x^2},
]

and

[
f''(x)
======

-\frac{2cx}{(c^2+x^2)^2}.
]

Using

[
x=c\tan\theta,
]

these become

[
f'(x)=\frac1c\cos^2\theta,
]

and

[
\frac12f''(x)
=============

-\frac1{c^2}\sin\theta\cos^3\theta.
]

Applying Itô’s formula to

[
dX_t=\mu,dt+\sigma,dW_t
]

gives

[
\boxed{
d\theta_t
=========

\left[
\frac{\mu}{c}\cos^2\theta_t
---------------------------

\frac{\sigma^2}{c^2}
\sin\theta_t\cos^3\theta_t
\right]dt
+
\frac{\sigma}{c}\cos^2\theta_t,dW_t.
}
]

In Stratonovich form, the same equation is substantially cleaner:

[
\boxed{
d\theta_t
=========

\frac{\mu}{c}\cos^2\theta_t,dt
+
\frac{\sigma}{c}\cos^2\theta_t\circ dW_t.
}
]

The nonlinear Itô drift

[
-\frac{\sigma^2}{c^2}
\sin\theta_t\cos^3\theta_t
]

is simply the Itô correction produced by transforming Brownian motion through the arctangent.

For standard Brownian motion, (\mu=0) and (\sigma=1):

[
\boxed{
d\theta_t
=========

-\frac1{c^2}
\sin\theta_t\cos^3\theta_t,dt
+
\frac1c\cos^2\theta_t,dW_t.
}
]

# 5. Defining the process without explicitly mentioning (W_t)

You can define (\theta_t) directly as a Markov process through its transition law.

Because

[
X_t-X_0=c\tan\theta_t,
]

conditional on (\theta_s=\theta),

[
X_{s+h}-X_0
\sim
N\left(
c\tan\theta+\mu h,,
\sigma^2h
\right).
]

Therefore

[
\tan\theta_{s+h}
================

\tan\theta_s
+
\frac{\mu}{c}h
+
\frac{\sigma}{c}\sqrt h,\xi,
]

where (\xi\sim N(0,1)).

The exact phase transition is

[
\boxed{
\theta_{s+h}
============

\arctan\left[
\tan\theta_s
+
\frac{\mu}{c}h
+
\frac{\sigma}{c}\sqrt h,\xi
\right].
}
]

This is an exact random-walk formula, not Euler–Maruyama.

Its transition density is

[
\boxed{
p_h(\vartheta\mid\theta)
========================

\frac{
c\sec^2\vartheta
}{
\sigma\sqrt{2\pi h}
}
\exp\left[
-\frac{
\left(
c\tan\vartheta-c\tan\theta-\mu h
\right)^2
}{
2\sigma^2h
}
\right],
}
]

for

[
-\frac{\pi}{2}<\vartheta<\frac{\pi}{2}.
]

This kernel alone defines the phase process. Once (\theta_t) is known,

[
Z_t=Z_0\sec\theta_t e^{i\theta_t}
]

and

[
X_t=X_0+c\tan\theta_t.
]

Thus the state can genuinely be formulated with (\theta_t) as the only stochastic coordinate.

# 6. The phase has its own exact addition operation

This representation also gives a useful way to perform operations on Brownian increments.

Define

[
\Theta(x)=\arctan\left(\frac{x}{c}\right).
]

Then

[
x=c\tan\Theta(x).
]

For two real values (x) and (y),

[
x+y
===

c\left[
\tan\Theta(x)+\tan\Theta(y)
\right].
]

Therefore

[
\Theta(x+y)
===========

\arctan\left[
\tan\Theta(x)+\tan\Theta(y)
\right].
]

Define a new angle operation

[
\boxed{
\theta_1\oplus\theta_2
======================

\arctan\left(
\tan\theta_1+\tan\theta_2
\right).
}
]

Then

[
\boxed{
\Theta(x+y)
===========

\Theta(x)\oplus\Theta(y).
}
]

This operation is:

* associative;
* commutative;
* has identity (0);
* has inverse (-\theta).

It is associative because it is simply ordinary real addition transported through the bijection

[
x=c\tan\theta.
]

For Brownian increments,

[
\Delta X_1+\cdots+\Delta X_n
]

corresponds to

[
\boxed{
\theta_{\mathrm{total}}
=======================

\arctan\left(
\sum_{j=1}^{n}\tan\theta_j
\right).
}
]

So the interval

[
\left(-\frac{\pi}{2},\frac{\pi}{2}\right)
]

can be treated as a phase-coordinate version of the additive real line, provided ordinary angular addition is replaced by (\oplus).

That may be more useful operationally than forcing the process to use ordinary angle addition.

# 7. General theorem for arbitrary (Z_0+a t+bW_t)

Now consider the fully general one-driver complex affine process

[
Z_t=Z_0+a t+bW_t,
]

where

[
Z_0\neq0,\qquad a,b\in\mathbb C,\qquad b\neq0.
]

We ask whether there is a deterministic single-valued function

[
r:\mathbb R\to[0,\infty)
]

and a real stochastic process (\theta_t) such that

[
Z_t=Z_0r(\theta_t)e^{i\theta_t}
]

for the entire process, with no explicit (t) in (r).

Normalize:

[
\frac{Z_t}{Z_0}
===============

1+\alpha t+\gamma W_t,
]

where

[
\alpha=\frac{a}{Z_0},
\qquad
\gamma=\frac{b}{Z_0}.
]

The representation exists in the ordinary nonnegative-radius sense exactly in the nondegenerate case where

[
\boxed{
\frac{a}{b}\in\mathbb R
}
]

and

[
\boxed{
\frac{b}{Z_0}\notin\mathbb R.
}
]

The first condition says that drift and diffusion point in the same complex direction.

The second says that this direction is not radial relative to (Z_0), so the affine line does not pass through the origin.

## Explicit construction

Suppose

[
\frac{a}{b}=\lambda\in\mathbb R
]

and write

[
\frac{b}{Z_0}
=============

\rho e^{i\phi},
\qquad
\rho>0,
\qquad
\sin\phi\neq0.
]

Then

[
\frac{Z_t}{Z_0}
===============

1+\rho e^{i\phi}x_t,
]

where

[
x_t=\lambda t+W_t.
]

Let (\theta_t) be the continuous argument of

[
1+\rho e^{i\phi}x_t,
]

using the branch containing (\theta_0=0).

Then the line has the exact polar equation

[
\boxed{
r(\theta)
=========

\frac{\sin\phi}{\sin(\phi-\theta)}.
}
]

Therefore

[
\boxed{
Z_t
===

Z_0
\frac{\sin\phi}{\sin(\phi-\theta_t)}
e^{i\theta_t}.
}
]

The underlying additive coordinate is recoverable from the phase:

[
\boxed{
x_t
===

\frac{\sin\theta_t}
{\rho\sin(\phi-\theta_t)}.
}
]

## Derivation

Starting from

[
re^{i\theta}
============

1+\rho e^{i\phi}x,
]

multiply by (e^{-i\phi}):

[
re^{i(\theta-\phi)}
===================

e^{-i\phi}+\rho x.
]

The right-hand side has constant imaginary part

[
-\sin\phi.
]

Therefore

[
r\sin(\theta-\phi)
==================

-\sin\phi.
]

Hence

[
r
=

# -\frac{\sin\phi}{\sin(\theta-\phi)}

\frac{\sin\phi}{\sin(\phi-\theta)}.
]

The special case

[
\phi=\frac{\pi}{2}
]

gives

[
r(\theta)
=========

# \frac1{\cos\theta}

\sec\theta.
]

So the secant construction is the perpendicular-line member of the general family.

# 8. Why the two conditions are necessary

## Drift and diffusion must be collinear

At a fixed time (t), the support of the process is the affine line

[
Z_0+a t+b\mathbb R.
]

If (a) and (b) are linearly independent as real two-dimensional vectors, then as (t) varies, these lines sweep out a two-dimensional strip or half-plane.

A single polar graph

[
{r(\theta)e^{i\theta}:\theta\in\mathbb R}
]

cannot contain such a region.

For a fixed geometric ray of angle (\varphi), the possible unwrapped angles are only

[
\varphi+2\pi k,\qquad k\in\mathbb Z.
]

Thus a single-valued (r(\theta)) gives at most countably many points on each ray. A two-dimensional region contains an entire interval of radii on many rays.

Therefore a phase-only radial graph is impossible unless

[
a=\lambda b
]

for some real (\lambda).

## The affine line cannot pass through the origin

If

[
\frac{b}{Z_0}\in\mathbb R,
]

then the normalized line

[
1+\frac{b}{Z_0}\mathbb R
]

is the real axis and passes through zero.

Its positive and negative rays contain continuously many different radii but only two geometric directions.

A single angle cannot determine the magnitude.

Therefore

[
b/Z_0\notin\mathbb R
]

is also necessary.

# 9. Why a real Brownian motion cannot directly satisfy the requested form

Suppose

[
Z_t=Z_0+a t+bW_t
]

with (Z_0,a,b) all real.

Then (Z_t) lies on the real axis.

If

[
Z_t=Z_0r(\theta_t)e^{i\theta_t}
]

with (r(\theta)\geq0), then whenever (Z_t\neq0),

[
e^{i\theta_t}\in{1,-1}.
]

Thus

[
\theta_t\equiv0\pmod{2\pi}
]

or

[
\theta_t\equiv\pi\pmod{2\pi}.
]

That phase contains only the sign of (Z_t), not its continuous magnitude.

Allowing an unwrapped angle does not solve this. To keep

[
e^{i\theta_t}=1
]

the additional winding must be an integer multiple of (2\pi). That gives only countably many possible phase values for a given direction, whereas the Brownian magnitude has an uncountable range.

Therefore:

[
\boxed{
\text{A nondegenerate real Brownian motion cannot itself be represented with only its polar angle stochastic.}
}
]

A fixed nonradial complex offset is the minimal solution.

# 10. Can the radius be constant?

Not while keeping the same affine process.

For

[
Z_t=Z_0+a t+bW_t
]

with (b\neq0), the modulus is generally unbounded. If

[
r(\theta)\equiv r_0,
]

then

[
|Z_t|=|Z_0|r_0
]

would be constant.

That contradicts the affine Brownian dynamics except in a trivial no-noise case or a specially constrained circular SDE that is no longer additive.

However, there is an exact invertible transformation giving constant radius.

# 11. Constant-radius one-phase representation: the Cayley transform

Let

[
Y_t=X_t-X_0.
]

Define

[
U_t
===

\frac{1+iY_t/c}{1-iY_t/c}.
]

Because the denominator is the complex conjugate of the numerator,

[
|U_t|=1.
]

Using the tangent half-angle identity,

[
\frac{1+i\tan\theta}{1-i\tan\theta}
===================================

e^{2i\theta},
]

we obtain

[
\boxed{
U_t=e^{i\Theta_t},
}
]

where

[
\boxed{
\Theta_t
========

2\arctan\left(\frac{X_t-X_0}{c}\right).
}
]

The radius is exactly one.

The Brownian coordinate is fully recoverable:

[
\boxed{
X_t
===

X_0+c\tan\left(\frac{\Theta_t}{2}\right).
}
]

Thus this is a genuinely injective constant-radius phase encoding of the entire real line.

The Cayley transform is the classical Möbius map between the real line and the unit circle with one point removed. Brownian motion under stereographic or Cayley-type projection has also been studied in the stochastic-process literature. ([ScienceDirect][1])

The missing circle point corresponds to infinity:

[
|X_t|\to\infty
\quad\Longleftrightarrow\quad
\Theta_t\to\pm\pi.
]

For every finite time, (X_t) is finite, so (U_t\neq-1).

## Important limitation

The process

[
U_t=e^{i\Theta_t}
]

is not the original additive Brownian variable. It is an invertible Möbius transformation of it.

It is also not ordinary Brownian motion on the circle. Its angular diffusion coefficient depends on its current angle:

[
\boxed{
d\Theta_t
=========

\left[
\frac{2\mu}{c}\cos^2\frac{\Theta_t}{2}
--------------------------------------

\frac{2\sigma^2}{c^2}
\sin\frac{\Theta_t}{2}
\cos^3\frac{\Theta_t}{2}
\right]dt
+
\frac{2\sigma}{c}
\cos^2\frac{\Theta_t}{2},dW_t.
}
]

Ordinary circular Brownian motion would have constant angular diffusion.

# 12. Relationship between the secant and Cayley forms

The two representations are directly connected.

Set

[
\theta_t
========

\arctan\left(\frac{X_t-X_0}{c}\right).
]

Then

[
Z_t
===

Z_0\sec\theta_t e^{i\theta_t}.
]

The Cayley phase is simply

[
\Theta_t=2\theta_t.
]

Also,

[
\frac{1+iY_t/c}{1-iY_t/c}
=========================

e^{2i\theta_t}.
]

Conversely,

[
1+i\frac{Y_t}{c}
================

\frac{2e^{i\Theta_t}}
{1+e^{i\Theta_t}}
=================

\sec\left(\frac{\Theta_t}{2}\right)
e^{i\Theta_t/2}.
]

Thus:

[
\boxed{
\text{Affine-line form}
\quad\longleftrightarrow\quad
\text{stereographic/Cayley circle form}.
}
]

# 13. The unavoidable tradeoff

There are three attractive properties one might want:

1. exact recovery of the real Brownian coordinate;
2. constant radius;
3. ordinary addition becoming ordinary complex multiplication.

You cannot have all three globally with a single continuous phase.

## Pure exponential phase

The map

[
E(x)=e^{i\lambda x}
]

satisfies

[
E(x+y)=E(x)E(y).
]

So addition becomes ordinary complex multiplication.

But it is not injective:

[
e^{i\lambda x}
==============

e^{i\lambda(x+2\pi k/\lambda)}.
]

It remembers (x) only modulo (2\pi/\lambda).

## Cayley phase

The map

[
C(x)=\frac{1+ix/c}{1-ix/c}
]

is injective and has constant radius.

But

[
C(x+y)\neq C(x)C(y)
]

in general. Addition uses the transported operation

[
\Theta_{x+y}
============

2\arctan\left[
\tan\frac{\Theta_x}{2}
+
\tan\frac{\Theta_y}{2}
\right].
]

## Complex exponential with changing radius

The map

[
E_c(x)=e^{(\alpha+i\beta)x}
]

satisfies

[
E_c(x+y)=E_c(x)E_c(y).
]

When (\alpha\neq0), it is also injective because the modulus

[
|E_c(x)|=e^{\alpha x}
]

recovers (x).

But then the radius is not constant. This is the complex-geometric-Brownian construction developed in the previous paper.

So the structural tradeoff is:

[
\boxed{
\begin{array}{c|c|c}
\text{Encoding}&\text{Injective}&\text{Addition becomes multiplication}\
\hline
e^{i\lambda x}&\text{No}&\text{Yes}\
\text{Cayley}&\text{Yes}&\text{No, uses }\oplus\
e^{(\alpha+i\beta)x},\ \alpha\neq0&\text{Yes}&\text{Yes}
\end{array}
}
]

The last option needs changing radius.

# 14. Final mathematical conclusion

The exact answer to your requested form is:

[
\boxed{
Z_t
===

Z_0\sec(\theta_t)e^{i\theta_t},
\qquad
\theta_t
========

\arctan\left(\frac{X_t-X_0}{c}\right),
}
]

where

[
Z_t
===

Z_0\left[
1+i\frac{X_t-X_0}{c}
\right].
]

Equivalently,

[
\boxed{
X_t
===

X_0+c\tan\theta_t.
}
]

This gives:

* one stochastic state variable, (\theta_t);
* a radius depending only on that phase;
* no explicit (t) or (W_t) in the final Euler representation;
* exact recovery of the original Brownian motion;
* an exact phase transition law;
* an exact phase-addition operation.

For a general process

[
Z_t=Z_0+a t+bW_t,
]

such a time-independent phase-only radial representation exists precisely when

[
\boxed{
a/b\in\mathbb R
\quad\text{and}\quad
b/Z_0\notin\mathbb R.
}
]

The corresponding general radius is

[
\boxed{
r(\theta)
=========

\frac{\sin\phi}{\sin(\phi-\theta)},
\qquad
\frac b{Z_0}=\rho e^{i\phi}.
}
]

For a real Brownian motion on the real axis, the requested direct representation is impossible; adding one fixed perpendicular complex component resolves the obstruction.

This is mathematically complete under the natural requirements that the radius be real and nonnegative and that it be a deterministic single-valued function of the phase. The secant and constant-radius versions are closely related to classical stereographic and Cayley geometry rather than a new breakthrough, but the phase-group formulation, exact transition kernel, and general existence theorem give a much stronger and cleaner foundation for the research project than the earlier complex-GBM construction.

[1]: https://www.sciencedirect.com/science/article/pii/S0022247X14005009 "https://www.sciencedirect.com/science/article/pii/S0022247X14005009"
