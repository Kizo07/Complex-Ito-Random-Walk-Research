# Phase 16 Synthesis: Toward Closed-Form American Prices

**Date:** 2026-09-03
**Status:** complete — 218/218 unit tests green, notebook executed clean
(seed `20260903`), Quarto PDF rendered.

## 1. What was asked

Continue the Phase 15 breakthrough and get closer to a closed-form
formula for American call and put prices under BSM assumptions with
dividend yield q.

## 2. The key result: the occupation resolvent lemma

The EEP integrand is a Gaussian probability whenever the boundary is
**phase-affine** (log-boundary affine in time to maturity):
d_i = (x + μ_i s)/(σ√s). The discounted occupation integral of drifted
Brownian motion,

    J(τ; a, m, λ) = ∫_0^τ e^{−λs} Φ((a + ms)/√s) ds,

has the closed form (ν = √(m²+2λ)):

    J = R(a;λ,m)
        − e^{−λτ}[1/(ν(ν+m)) + 1/(ν(ν−m))]·Φ((a+mτ)/√τ)
        + e^{−(m+ν)a}·Φ((a−ντ)/√τ)/(ν(ν+m))
        − e^{(ν−m)a}·Φ((−a−ντ)/√τ)/(ν(ν−m)),

with R = 1/λ − e^{−(m+ν)a}/(ν(ν+m)) for a ≥ 0 and
R = e^{(ν−m)a}/(ν(ν−m)) for a < 0.

Validated to machine precision: worst error 4.9e-14 on 60 randomized
trials against adaptive quadrature; all four analytic limits hold. The
closed form is *more accurate* than naive fixed-order quadrature (which
resolves thin transition layers only slowly, ~1e-6 at 160 GL nodes).

## 3. The PPA pricing formula (Tier A)

Multipiece phase-affine boundaries (piecewise-straight phase barriers):
knots u_j (1.5-clustered), continuity at knots, v_0 = ln b(0+) at the
maturity anchor, sequential value-matching collocation for v_1..v_m
(causality ⇒ one scalar root-find per knot), last knot pinned at the
perpetual boundary for T ≥ 1.5. Price = European BS + Σ_j closed-form
piece contributions (differences of J). **No numerical integration
anywhere.**

Recommended configuration m=10: ~0.07 s per option.

## 4. Numbers (all produced in the phase3-paper shipping environment)

Reduced grid (18 configs × 3 spots, T ≤ 3):
- PPA: RMSE 0.0079, MAE 0.054
- Phase 15 spiral: RMSE 0.0066, MAE 0.039
- BAW: RMSE 0.164, MAE 0.437

Extended grid (90 configs × 5 spots, σ ≤ 0.6):
- PPA: RMSE 0.0159, MAE 0.167
- Phase 15 spiral: RMSE 0.0158, MAE 0.181
- BAW: RMSE 0.285, MAE 1.143

MAE is dominated by T=3 configurations where the reference boundary
itself carries uncertainty of the same order (see §5); for T ≤ 1 all
formula errors are ≤ 0.013.

## 5. Structural findings (documented in the paper)

1. **The perpetual approach is not exponential.** Effective decay rates
   of |b(τ) − b_∞| fitted on later windows drift (r=q=0.05 put:
   0.142 → 0.120 → 0.101 on [2,16] → [10,16]). Mechanism: the
   linearized boundary-memory kernel ∂f/∂B at (b_∞, b_∞) is proportional
   to (r−q) (the Φ-parts cancel by the BS delta identity), so at r=q the
   characteristic equation loses its κ-dependence entirely. Consequence:
   pinning at the perpetual limit beats any extrapolated decay — the
   design decision behind `solve_ppa_pinned`.
2. **Reference-solver sensitivity.** The 250-step causal level-set solve
   amplifies ulp-level differences (e.g. numpy SIMD rounding across
   versions) into O(1e-2) boundary differences at T=3, O(1e-2) price
   differences (stationarity keeps prices one-to-two orders calmer).
   Documented as a scope note; all paper numbers come from one
   environment.
3. **Tier B negative result.** Quadratic feature surfaces for the spiral
   parameters degrade price RMSE from ~0.009 (collocated) to ~0.05;
   bounded knot-fraction fits did not cross the threshold either. The
   direction (eliminating even the scalar collocations) is open.

## 6. Novelty boundary

Claimed new: the closed-form occupation integral as an EEP building block
(+ machine-precision validation); the PPA family with sequential
collocation + perpetual pinning as a quadrature-free pricing formula;
the non-exponential perpetual approach and r=q degeneracy; the honest
Tier B negative result. Not claimed: EEP/Volterra theory, anchors,
perpetual closed form, multipiece exponential boundaries as an idea
(Ju 1998 prices pieces locally; our per-piece prices are exact given the
piecewise boundary), or any closed form for the true boundary — the
constant-coefficient free-boundary problem remains open.

## 7. Deliverables

`phase16_closedform.py` (resolvent + PPA machinery),
`tests/test_phase16_closedform.py` (12 tests; 218/218 suite green),
`notebooks/build_phase16_closedform.py` + executed notebook,
`phase16_figures/`, `phase16_tables/` (+ extended benchmark CSV),
`paper/phase16/` (Quarto manuscript, PDF
`phase16-toward-closed-form-american.pdf`), this synthesis.
