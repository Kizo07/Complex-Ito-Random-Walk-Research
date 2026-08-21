# Phase 8 — Synthesis: vanilla spread/basket options under stochastic correlation

**Date:** 2026-08-21
**Status:** complete — 14/14 unit tests, clean notebook, COS vs MC within
4 SE at all strikes, opposite-curvature smile signature verified.

---

## 1. What was asked

European vanilla pricing under stochastic correlation. Phases 3–6 solved
barrier/touch/correlation-level payoffs via the DDS clock; the missing piece
was the bread-and-butter product class (spread/basket vanillas), where the
audited literature has only Monte Carlo or approximations.

## 2. The result

**Theorem (exact one-dimensional transform).** Under the bounded-factor
correlation model, for any linear combination \(Z=\alpha_1F_1+\alpha_2F_2\),

\[
\phi_Z(u)=\mathbb E\big[e^{-rT}e^{iuZ_T}\big]
= e^{-rT}e^{iuz_0-\frac12u^2\beta T}\;L_A\!\Big(\frac{\alpha u^2}{2}\Big),
\qquad L_A(s)=\mathbb E\big[e^{-sA_T}\big],
\]

where \(L_A\) is a real-potential forward Feynman–Kac resolvent. The bounded
factor is not cosmetic here: it confines \(A_T\) to \((-T,T)\), so \(L_A\)
exists for **all** real \(s\) — the transform is globally defined, unlike
unbounded-variance models where moment explosions bound the inversion strip.

**Pricing.** Two deterministic routes, cross-validated to \(10^{-5}\):
(i) COS inversion of \(\phi_Z\) (spectral in modes; one sparse PDE solve per
mode, reusable across strikes); (ii) quadrature against the Milestone-4
clock density (robust at all moneynesses). Both match conditional-Gaussian
Monte Carlo within 4 SE across strikes 88–112.

**Greeks.** Delta/gamma/vegas as one-dimensional integrals of closed-form
Bachelier sensitivities against the clock density — semi-analytic, no
pathwise estimators.

## 3. The falsifiable signature: implied-correlation smiles

Inverting constant-correlation Bachelier quotes:

- both smiles are exactly **symmetric** in moneyness (zero linear slope);
- curvatures are **opposite**: spread wings down (−2.385e-3), basket wings
  up (+1.770e-3);
- ATM implied correlations equal \(E[A_T]\) exactly (spread +0.1345) — a
  direct model-free read-out of the occupation mean.

Mechanism: a variance mixture fattens tails, raising wing implied variance;
higher variance maps to *lower* implied correlation for spreads and *higher*
for baskets. This extends the Milestone-3 sign corollary from barrier prices
to full smile geometry and gives traders a direct test: if stochastic
correlation is the true driver, spread and basket implied-correlation curves
must curve away from each other symmetrically.

## 4. Numerical findings worth recording

1. The naive backward-FK extension fails off constant coefficients (Phase 7's
   pitfall); Phase 8's resolvent uses the corrected forward equation.
2. Large-|s| Laplace tilts concentrate mass near localization boundaries;
   the clock-density route (bounded oscillating frequencies only) is the
   robust default and both routes are provided.
3. COS payoff coefficients were derived for arbitrary strike position
   relative to the truncation band (three cases), with explicit failure for
   out-of-band strikes rather than silent wrong answers.

## 5. Novelty boundary (post-audit)

Claimed as new: the exact global characteristic function for spreads/baskets
under stochastic correlation; deterministic European pricing where the
audited field has only MC/approximation; the opposite-curvature smile
signature; clock-density Greeks. Not claimed: COS methodology (Fang–
Oosterlee), multidimensional COS variants (Ruijter–Oosterlee; COS-TT-CHF),
conditional Gaussianity itself.

## 6. Deliverables

`PHASE_8_LITERATURE_REVIEW.md`, `phase8_cos.py`,
`tests/test_phase8_cos.py` (14/14),
`notebooks/build_phase8_cos_vanillas.py` + executed notebook (~173 s,
seed 20260821), `PHASE_8_SIMULATION_RESULTS.md`, `phase8_figures/`.
