# Mathematical Review of the Phase 15 American-Options Paper

**Reviewed manuscript:** [`paper/phase15/output/phase15-american-options-complex-gbm.pdf`](paper/phase15/output/phase15-american-options-complex-gbm.pdf)  
**Review date:** 2026-09-02  
**Primary focus:** Mathematical correctness, numerical validation, and agreement between the manuscript and implementation

## Overall assessment

**Major revision is required.** The classical Black–Scholes–Merton framework is mostly sound, and the complex-GBM modulus and phase identities are algebraically correct subject to minor qualifications. However, several central mathematical and numerical claims are incorrect or unsupported:

1. the boxed put equations have the wrong sign;
2. the claimed universal short-expiry boundary law conflicts with established asymptotic regimes;
3. the proposed boundary family has an artificial, dimension-dependent cusp at exactly one time unit and violates boundary monotonicity;
4. the claimed second-order insensitivity to boundary error is false for the EEP pricing functional actually used;
5. the reference solver is strongly grid-sensitive in cases included in the headline benchmark; and
6. every quantity labeled “MAE” is actually a maximum absolute error.

The collocation construction may remain useful as an empirical approximation, but the paper is not ready to support its current accuracy or novelty claims.

## 1. The boxed put equations have the wrong sign

Equations (5), (7), and (12) use

\[
V_A=V_E+\int_0^\tau
\left[
qSe^{-qs}\Phi(\phi d_1)-rKe^{-rs}\Phi(\phi d_2)
\right]ds,
\]

with \(\phi=+1\) for calls and \(\phi=-1\) for puts. This expression is correct for calls but has the wrong sign for puts. A correct unified expression is

\[
\boxed{
V_A=V_E+\phi\int_0^\tau
\left[
qSe^{-qs}\Phi(\phi d_1)-rKe^{-rs}\Phi(\phi d_2)
\right]ds
}.
\]

Equivalently, the put premium must be written explicitly as

\[
\int_0^\tau
\left[
rKe^{-rs}\Phi(-d_2)-qSe^{-qs}\Phi(-d_1)
\right]ds.
\]

The same outer factor \(\phi\), or an explicit put-specific expression, is needed in the boundary equation.

This is not merely cosmetic. For

\[
S=K=100,\qquad r=q=0.05,\qquad \sigma=0.2,\qquad T=1,
\]

the European put is approximately \(7.5771\). The correct EEP is approximately \(+0.0853\), giving an American value near \(7.6624\). The printed formula instead applies approximately \(-0.0853\), giving \(7.4918\), below the European price and therefore violating the American-option lower bound.

The implementation contains the correct separate formulas at [`phase15_american.py`](phase15_american.py#L131), whereas the manuscript equations begin at [`paper/phase15/index.qmd`](paper/phase15/index.qmd#L184). The manuscript and executable formula therefore disagree.

## 2. The short-expiry shape is not universal

Section 4.2 claims that

\[
b(\tau)-b_0\propto \sqrt{\tau|\ln\tau|}
\]

is universal, with a parameter-dependent effective coefficient. Established asymptotic analysis gives distinct regimes.

For an American put under constant coefficients, the leading forms are

\[
\begin{aligned}
q<r:
&\quad K-b_p(\tau)
\sim K\sigma\sqrt{\tau|\ln\tau|},\\
q=r:
&\quad K-b_p(\tau)
\sim K\sigma\sqrt{2\tau|\ln\tau|},\\
q>r:
&\quad b_p(\tau)
=\frac rqK\left[1-\xi_1\sigma\sqrt{2\tau}+O(\tau)\right],
\qquad \xi_1\approx0.4517.
\end{aligned}
\]

Calls inherit the corresponding regimes through put–call duality, with \(r\) and \(q\) interchanged and the direction of the boundary movement reversed.

These regimes appear, including the constant-volatility specialization, in Wen-Ting Chen and Song-Ping Zhu, [“Optimal Exercise Price of American Options Near Expiry”](https://doi.org/10.1017/S1446181110000052), especially equations (3.15)–(3.22). That paper also cites the earlier constant-volatility treatment by Evans, Kuske, and Keller, [“American Options on Assets with Dividends Near Expiry”](https://doi.org/10.1111/1467-9965.02008).

The Phase 15 fitted coefficients are consistent with these known regimes rather than with the paper’s interpretation:

- values near \(0.73\) are close to \(1/\sqrt2\), the limiting coefficient obtained when a \(\sqrt{\tau|\ln\tau|}\) result is normalized by the paper’s \(\sqrt{2\tau|\ln\tau|}\);
- values near \(1\) correspond to the critical \(q=r\) regime; and
- values near \(0.24\), where the expiry boundary is away from the strike, are finite-window artifacts from fitting a true \(\sqrt\tau\) law with a \(\sqrt{\tau|\ln\tau|}\) regressor. Under that normalization the apparent coefficient should tend to zero as \(\tau\downarrow0\).

There are two further problems with the numerical evidence:

- the reported regression uses `np.polyfit(xs, ys, 1)`, which estimates a free intercept even though the stated fitted model fixes the intercept at the known anchor; and
- in reproduced near-expiry solves, more than half of the boundary increments were flat fallback steps, so the fitted data do not provide a reliable asymptotic test.

Section 4.2 and the corresponding novelty statements should therefore be replaced by a regime-aware analysis with the established literature cited explicitly.

## 3. The refined boundary has an artificial cusp at \(\tau=1\)

The refined term is

\[
g(\tau)=\sqrt{2\tau\,|\ln\max(\tau,\varepsilon)|}\,e^{-\kappa_2\tau}.
\]

For \(\tau>\varepsilon\), it vanishes at \(\tau=1\). Since

\[
|\ln\tau|\sim|\tau-1|
\qquad\text{as }\tau\to1,
\]

the function behaves locally like \(\sqrt{2|\tau-1|}\). It is continuous but has an infinite-slope cusp at exactly one time unit.

This point is arbitrary and dimension-dependent. If the same model is expressed in days instead of years, the cusp moves from one year to one day. The logarithm also acts directly on dimensional time; a valid logarithmic argument must be dimensionless.

The cusp produces nonmonotone candidate exercise boundaries. For the paper’s \(r=q=0.05\), \(\sigma=0.2\), \(T=3\) call calibration, the implementation gives

\[
b(0.9)=132.276,qquad
b(1)=129.937,qquad
b(1.1)=136.216.
\]

A true American-call boundary under constant coefficients is nondecreasing with time to maturity: the value for a longer exercise horizon is at least the value for a shorter one, so the longer-horizon exercise region cannot expand downward. The candidate above violates that property sharply. The put candidate has the mirrored violation.

For every \(T=3\) benchmark, the EEP integral traverses the cusp. The integrand is therefore not “smooth” as claimed. The relevant implementation is [`phase15_american.py`](phase15_american.py#L460).

The fixed cutoff also prevents the literal claimed asymptotic. For \(0<\tau<\varepsilon\),

\[
g(\tau)\propto\sqrt\tau,
\]

not \(\sqrt{\tau|\ln\tau|}\). A replacement family should be dimensionless, smooth on \((0,\infty)\), monotonicity-preserving, and regime-aware.

## 4. The EEP price is not stationary under boundary substitution

The paper repeatedly claims that a small boundary error produces a second-order price error by an envelope or stationarity property. That does not hold for the functional used in the implementation: European price plus the exact-boundary EEP formula with an arbitrary approximate boundary substituted into it.

For

\[
d_{1,2}(S,B,s)
=\frac{\ln(S/B)+(r-q\pm\tfrac12\sigma^2)s}{\sigma\sqrt{s}},
\]

the Gaussian-density identity

\[
Se^{-qs}\varphi(d_1)=Be^{-rs}\varphi(d_2)
\]

shows that the derivative of either the correct call or put EEP integrand with respect to \(B\) is

\[
\frac{e^{-rs}\varphi(d_2)}{B\sigma\sqrt{s}}
\left(rK-qB\right).
\]

Consequently, for an additive perturbation \(h\), the first variation contains

\[
\int_0^\tau
\frac{e^{-rs}\varphi(d_2)}{b(\tau-s)\sigma\sqrt{s}}
\left[rK-qb(\tau-s)\right]
h(\tau-s)\,ds,
\]

which is generally nonzero.

A numerical check using an endpoint-preserving perturbation

\[
b_\epsilon(u)=b(u)\exp\!\left(\epsilon\sin(\pi u/T)\right)
\]

confirmed first-order behavior. For the base call case, the ratios \(\Delta V/\epsilon\) were approximately

\[
-0.3433,\;-0.3457,\;-0.3469,\;-0.3475
\]

as \(\epsilon\) was successively halved. A second-order error would instead make \(\Delta V/\epsilon\to0\).

The value of an explicitly defined suboptimal stopping rule may have a different variational property because of smooth pasting, but the substituted-boundary EEP expression is not automatically that stopping-rule value. The paper’s stationarity justification should be removed unless a correct functional and proof are supplied.

## 5. The reference solver is grid-sensitive

The claimed reference solver does not exhibit stable convergence in several configurations used in the extended benchmark. A particularly clear case is

\[
S=120,\quad K=100,\quad r=0.05,\quad q=0.10,
\quad\sigma=0.2,\quad T=3,\quad\text{call}.
\]

Reproducing the CSV settings and varying only the boundary-grid size gives:

| Method/settings | Price |
|---|---:|
| Reference solver, \(n=250\) | 20.634273 |
| Reference solver, \(n=300\), the CSV value | 20.391586 |
| Reference solver, \(n=350\) | 20.676551 |
| Reference solver, \(n=700\) | 20.670680 |
| Adjacent-averaged CRR, \(N=8{,}000\) | 20.689421 |
| Adjacent-averaged CRR, \(N=10{,}000\) | 20.689433 |
| Adjacent-averaged CRR, \(N=12{,}000\) | 20.689399 |

The paper’s reference value is an isolated grid-dependent outlier by about \(0.30\). Its own stored Richardson-tree result, \(20.689706\), points to the same problem.

The spiral value for this case is approximately \(20.4842\). Its discrepancy from the stable high-step tree range is approximately \(0.205\), rather than the approximately \(0.093\) discrepancy measured against the paper’s reference.

The solver implementation explains some of this behavior. When no suitable crossing or bracket is found, it silently copies the previous boundary value. It then clips the result to enforce monotonic movement toward the perpetual boundary. See [`phase15_american.py`](phase15_american.py#L351). This creates staircase boundaries and makes the monotonicity test partly circular: monotonicity is enforced rather than independently demonstrated.

The existing validation is insufficient because:

- only two external published price points are tested;
- the principal cross-method test is a single ATM \(r=q\) case;
- residual tests use the same equation and quadrature as the solver;
- there is no grid, quadrature, or level-set convergence table; and
- the put–call symmetry test uses \(S=K\), so it exercises only a restricted special case of the transformation.

The two quoted Ju benchmark checks do pass, but they do not establish the solver as a reference across the stated grid. The headline comparison must be recomputed against an independently converged tree, PDE/LCP solver, or established benchmark dataset.

## 6. “MAE” is actually maximum absolute error

The notebook computes

```python
mae = float(np.max(np.abs(d)))
```

at [`notebooks/build_phase15_american_spiral.py`](notebooks/build_phase15_american_spiral.py#L521). This is maximum absolute error, not mean absolute error. The published tables are internally recognizable as mislabeled because their reported “MAE” exceeds RMSE.

Recomputed from the stored CSV files, the statistics against the paper’s own reference are:

### Reduced grid

| Method | RMSE | True MAE | Maximum absolute error |
|---|---:|---:|---:|
| Spiral | 0.006603 | 0.003242 | 0.039365 |
| BAW | 0.164462 | 0.099031 | 0.436657 |
| CRR–Richardson | 0.008856 | 0.003755 | 0.068548 |

### Extended grid

| Method | RMSE | True MAE | Maximum absolute error |
|---|---:|---:|---:|
| Spiral | 0.015972 | 0.005947 | 0.185970 |
| BAW | 0.284917 | 0.166460 | 1.141799 |
| CRR–Richardson | 0.018984 | 0.005983 | 0.298120 |

These figures only correct the metric labels; they do not repair the unreliable reference values discussed above.

The scope section also misidentifies the location of the worst stored spiral error. The largest absolute discrepancy in the extended CSV is the \(T=3\), \(\sigma=0.2\), \(r=0.07\), \(q=0.03\) put at \(S=80\), not a high-volatility, dividend-heavy case.

## 7. Other mathematical and specification issues

### Exact put residual behavior

With the true boundary and

\[
F_p(y;\tau)=K-y-V_E(y,\tau)-\operatorname{EEP}_p(y,\tau),
\]

the exact residual equals zero throughout the put exercise region \(y\le b_p(\tau)\) and is negative in the continuation region. A “positive hump” is not an exact structural fact; it is generated by numerical boundary/history error. The solver explicitly relies on that numerical hump when choosing a put root.

### The executable formula includes undisclosed clipping

`american_from_boundary` returns

```python
max(european_plus_eep, european, intrinsic)
```

at [`phase15_american.py`](phase15_american.py#L154), whereas equation (12) states only European plus EEP. At least one extended-grid value is materially changed by the clip: for the \(r=0.10,q=0.05,\sigma=0.2,T=3\) put at \(S=80\), the raw formula is approximately \(19.8216\) but the reported value is clipped to intrinsic value \(20\).

If clipping is part of the proposed method, it must appear in the mathematical definition and benchmarks. It can also introduce additional kinks and does not enforce the upper bounds \(C_A\le S\) and \(P_A\le K\).

### Signed \(\eta\) is inconsistent with the optimization box

Equation (10) declares \(\eta>0\) for calls and \(\eta<0\) for puts, while Section 5.2 states \(0\le\eta\le2.5\) for the optimizer. The code actually optimizes a nonnegative magnitude and multiplies it by a separate sign. The paper should use distinct notation, such as \(s_\phi\eta\) with \(\eta\ge0\).

### Collocation does not always solve three equations

The text repeatedly says that the three residual equations are driven to zero. For the \(r=q=0.05,\sigma=0.2,T=3\) call, the selected objective is approximately \(0.0210\), with residuals near

\[
(0.0378,-0.1191,0.0736).
\]

Thus the method performs a bounded least-squares projection but does not solve the three equations. The wording should say “minimizes” and report residuals, parameter-bound activity, optimizer status, and sensitivity to starting points.

### Complex-phase qualifications

The identities

\[
|\mathcal Z_t|
=|\mathcal Z_0|e^{(\mu-\sigma^2/2)t+\sigma W_t}
\]

and

\[
\Theta_t=\Theta_0+\omega t+\beta W_t
\]

are correct, assuming \(|\mathcal Z_0|=S_0\) and that \(\Theta\) denotes an unwrapped phase lift rather than the argument modulo \(2\pi\). However:

- the exercise inequality stated in phase coordinates assumes \(\beta/\sigma>0\);
- it reverses when \(\beta<0\); and
- when \(\beta=0\), phase carries no information about spot.

In the drift-matched gauge the phase is a deterministic affine transformation of log-price. This is a valid reparameterization, but it does not reduce the optimal-stopping problem or supply new pricing information by itself. The claimed geometric contribution should be described accordingly.

### Endpoint and rendering issues

- The finite-anchor spiral formula is undefined for the \(q=0\) call because both the maturity and perpetual call boundaries are infinite; the implementation handles this by a separate European-price branch.
- The perpetual-root formula should state the assumptions under which \(s_+>1\); at \(q=0\), \(s_+=1\) and the call boundary is interpreted as infinite.
- The PDF contains unresolved references `?@sec-structure` and `merton1973-style?`.
- The short-expiry literature needed for the paper’s central asymptotic claims is absent from the bibliography.

## 8. What is mathematically sound

The following components are substantially correct, subject to the qualifications above:

- the modulus identity for the proposed one-driver complex exponential;
- the unwrapped phase relation and drift-matched gauge;
- risk-neutral BSM dynamics and dividend-adjusted European formulas;
- European put–call parity;
- the separately implemented call and put EEP expressions;
- the maturity boundary anchors;
- the perpetual-option characteristic equation and finite-boundary formulas for the applicable parameter regimes; and
- the \(q=0\) American-call equality with its European counterpart.

The existing unit suite also executes successfully: all 14 tests in [`tests/test_phase15_american.py`](tests/test_phase15_american.py) pass. That confirms consistency with the assertions currently encoded, but the missing tests described above prevent it from validating the disputed claims.

## 9. Required revision sequence

1. Correct equations (5), (7), and (12), including the put sign and the actual clipping rule if clipping is retained.
2. Replace the universal short-expiry claim with the established three-regime asymptotics and add the missing literature.
3. Redesign the boundary family so it is dimensionally meaningful, smooth away from expiry, regime-aware, and monotonicity-preserving. In particular, remove the \(|\ln\tau|\) continuation through \(\tau=1\).
4. Remove the stationarity claim or replace it with a precisely defined stopping-rule functional and a valid proof.
5. Replace or repair the reference solver and publish systematic convergence tables over the benchmark’s difficult regimes.
6. Recompute all performance results against independent, converged reference prices, preferably with at least two unrelated methods and equal-cost timing comparisons.
7. Correct RMSE/MAE/maximum-error labels and identify the actual worst configurations.
8. Expand the tests to cover off-ATM put–call duality, all short-expiry regimes, time-unit invariance, boundary monotonicity, the \(\tau=1\) neighborhood, clipping activation, and reference-grid convergence.
9. Repair unresolved cross-references and align all notation and algorithm descriptions with the code.

Until these revisions are completed, the most defensible description of Phase 15 is: **a promising but presently unvalidated collocation heuristic built on otherwise standard EEP machinery and an invertible complex-phase reparameterization of log-price.**
