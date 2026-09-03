# Phase 15 Synthesis: American Calls and Puts from One-Driver Complex GBM

**Date:** 2026-09-03
**Status:** complete — 14/14 unit tests green, notebook executed clean
(seed `20260902`), Quarto PDF rendered.

## 1. What was asked

Pricing formulas for American call and put options under Black–Scholes–
Merton assumptions with continuous dividend yield q, expanding the Phase 3/4
findings (faithful one-driver complex embeddings; native complex GBM whose
modulus is exactly GBM).

## 2. The geometry

Under the risk-neutral measure the Phase 4 process

    Z_t = Z_0 exp( [(μ−σ²/2)+iω]t + (σ+iβ)W_t ),   μ = r−q,

carries the stock price as its modulus, |Z_t| = S_t. In the drift-matched
gauge the phase is a pure scale of the log-price, Θ = Θ_0 + (β/σ)ln(S/S_0),
and the American exercise boundary b(t) becomes a moving angular barrier
θ_B(t) = Θ_0 + (β/σ)ln(b(t)/S_0): calls exercise above the curve, puts
below it, both running from the maturity anchor to the perpetual phase
line. The rank-one (one-driver) structure is exactly what keeps the
barrier one-dimensional.

## 3. Exact machinery (validated)

- EEP representation (Kim 1990 / Jacka 1991 / Carr–Jarrow–Myneni 1992):
  American = European + EEP integral against the boundary, with the
  integrand in closed form (Φ(d₁), Φ(d₂) at boundary "strikes").
- Structural facts established numerically and used algorithmically:
  1. **Causality**: the boundary equation at τ uses the boundary only at
     smaller arguments → sequential solve.
  2. **Plateau**: for the call the value-matching residual F(y;τ) < 0 for
     y < b and F ≡ 0 for y ≥ b (deep-ITM calls exercise immediately) —
     the boundary is where the residual *reaches* zero, not where it
     crosses; the put mirrors with a positive hump.
  3. **Traction loss**: ∂F/∂y → 0 as τ→0 — the maturity anchors
     b_c(0⁺)=K·max(1,r/q), b_p(0⁺)=K·min(1,r/q) must be imposed.
  4. **Stationarity**: prices are insensitive to boundary error at first
     order (envelope property) — approximate boundaries price far better
     than they look.
- Causal level-set reference solver (δ-level crossing + linear
  correction + adaptive diffusion-scaled scan window).
- Validation: Ju-exhibit 10,000-step binomial TRUE values reproduced to
  ≤2.2e-3; McDonald–Schroder put–call symmetry ≤2.4e-3 with independently
  solved boundaries; CRR–Richardson agreement ≤7e-4 at ATM.

## 4. The breakthrough: the collocated logarithmic-spiral formula

Short-maturity asymptotics measured on the reference solutions: the
boundary approaches its anchor with infinite slope in the universal SHAPE

    b(τ) = b_0 + η·c·σ·b_0·√(2τ|ln τ|) + …

The coefficient c ≈ 1 only at zero drift (r = q); nonzero r−q shifts it
(0.24–0.77 in the tested cases) at accessible maturities.

The Phase 15 boundary family is exact at both asymptotic limits:

    ln b(τ) = ln b_∞ + ln(b_0/b_∞)·e^{−κ₁τ}
              + η·σ·√(2τ|ln max(τ,ε)|)·e^{−κ₂τ}

- b(0⁺) = b_0 (maturity anchor) and b(∞) = b_∞ (perpetual boundary) by
  construction;
- the square-root term carries the short-maturity shape with exponential
  cutoff κ₂;
- (κ₁, κ₂, η) are fixed by COLLOCATION — the value-matching residual of
  the spiral boundary itself is driven to zero at τ ∈ {T/4, T/2, 3T/4}
  (bounded least squares, multi-start). No boundary fitting anywhere.

Pricing formula: V_A = European BS + EEP integral on the collocated
spiral boundary — one scalar system solve + one smooth 1-D integral.

## 5. Benchmark results (vs the reference solver)

Extended grid: 90 configurations (r,q in 5 pairs, σ∈{0.2,0.4,0.6},
T∈{0.5,1,3}, call+put) × 5 spots = 450 prices.

| Method | RMSE | MAE |
|---|---|---|
| **Phase 15 spiral formula** | **0.016** | **0.186** |
| Barone-Adesi–Whaley | 0.285 | 1.142 |
| CRR–Richardson (N≤6000) | 0.019 | 0.298 |

Reduced grid (18 configs × 3 spots): spiral RMSE 0.0066 / MAE 0.039 vs
BAW 0.164 / 0.437. Errors concentrate in long-maturity high-volatility
dividend-heavy puts (T=3, σ=0.6); the formula is designed for T ≲ 1–2.

Structural identities verified: q=0 call = European (machine precision);
monotone + convex in S; perpetual approach at T=30 within 2.6% and
monotone.

## 6. Novelty boundary

Claimed new: the phase-barrier reformulation on the Phase 4 complex GBM;
the causal level-set reference solver and its structural diagnostics;
the measured short-maturity shape and coefficient dependence on r−q; the
anchor-exact logarithmic-spiral family; the collocation-fixed pricing
formula and its benchmark performance.

Not claimed: the EEP/Volterra machinery itself (Kim/Jacka/CJM); the
anchors; the perpetual closed form; BAW/MacMillan/Ju approximations; and
— explicitly — NO closed form for the true boundary. The
constant-coefficient free-boundary problem remains open; the honest
position is "exact representation + fast formula + reference solver".

## 7. Deliverables

`phase15_american.py` (machinery + formula + benchmarks),
`tests/test_phase15_american.py` (14/14),
`notebooks/build_phase15_american_spiral.py` + executed notebook,
`phase15_figures/`, `phase15_tables/` (benchmark CSVs + JSON summary),
`paper/phase15/` (Quarto manuscript, PDF
`phase15-american-options-complex-gbm.pdf`), this synthesis.
