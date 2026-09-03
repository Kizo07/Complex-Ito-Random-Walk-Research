"""Tests for Phase 15: American options via complex-GBM spiral geometry.

Revised 2026-09-03 after external mathematical review.  New coverage per
review section 9.8: put EEP sign, off-ATM put–call duality, short-expiry
regime asymptotics (Evans–Kuske–Keller / Chen–Zhu), time-unit invariance,
boundary monotonicity through the tau=1 neighborhood, absence of hidden
clipping, solver diagnostics, and grid behavior (soft convergence plus
the documented hard-regime sensitivity) against a converged tree oracle.
"""

import math
import unittest

import numpy as np

import phase15_american as p15

K = 100.0
R, Q, SIG, T = 0.05, 0.05, 0.2, 1.0


def interp_bd(taus, bvals):
    return lambda tau: float(np.interp(tau, taus, bvals))


class TestFoundations(unittest.TestCase):

    def test_european_put_call_parity_with_dividends(self):
        for r, q in ((0.05, 0.05), (0.07, 0.03), (0.03, 0.07)):
            c = p15.bs_european(K, K, r, q, SIG, T, "call")
            p = p15.bs_european(K, K, r, q, SIG, T, "put")
            self.assertAlmostEqual(c - p,
                                   K * math.exp(-q * T)
                                   - K * math.exp(-r * T),
                                   places=10)

    def test_perpetual_value_match_and_smooth_past(self):
        for kind in ("call", "put"):
            _, b_inf = p15.perpetual_american(K, K, R, Q, SIG, kind)
            price, _ = p15.perpetual_american(b_inf, K, R, Q, SIG, kind)
            intrinsic = (b_inf - K) if kind == "call" else (K - b_inf)
            self.assertAlmostEqual(price, intrinsic, places=10)
            h = 1e-5 * K
            up, _ = p15.perpetual_american(b_inf + h, K, R, Q, SIG, kind)
            dn, _ = p15.perpetual_american(b_inf - h, K, R, Q, SIG, kind)
            delta = (up - dn) / (2 * h)
            self.assertAlmostEqual(delta, 1.0 if kind == "call" else -1.0,
                                   places=4)

    def test_maturity_anchors(self):
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.05, 0.05,
                                                        "call"), K)
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.05, 0.05,
                                                        "put"), K)
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.07, 0.03,
                                                        "call"),
                               K * 0.07 / 0.03)
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.07, 0.03,
                                                        "put"), K)
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.03, 0.07,
                                                        "call"), K)
        self.assertTrue(math.isinf(p15.boundary_at_maturity(K, 0.05, 0.0,
                                                            "call")))

    def test_put_eep_has_correct_sign(self):
        # Regression for review claim 1: the put premium must be added,
        # i.e. the American put is at least its European price.
        taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                         n_grid=200, n_quad=44, delta=1e-8)
        bd = interp_bd(taus, bvals)
        prem = p15.eep(K, T, bd, K, R, Q, SIG, "put", n_quad=96)
        self.assertGreater(prem, 0.0)
        am = p15.american_from_boundary(K, T, bd, K, R, Q, SIG, "put",
                                        n_quad=96)
        euro = p15.bs_european(K, K, R, Q, SIG, T, "put")
        self.assertGreaterEqual(am, euro - 1e-9)
        self.assertAlmostEqual(am, euro + prem, places=10)

    def test_american_call_q0_is_european(self):
        price, *_ = p15.american_spiral(K, K, R, 0.0, SIG, T, "call")
        euro = p15.bs_european(K, K, R, 0.0, SIG, T, "call")
        self.assertAlmostEqual(price, euro, places=12)

    def test_raw_formula_has_no_hidden_clipping(self):
        # Review claim 7: american_from_boundary must equal European + EEP
        # exactly, even when a crude boundary pushes the raw value below
        # intrinsic.
        crude = lambda tau: 30.0  # absurd put boundary: deep below spot
        euro = p15.bs_european(K, K, R, Q, SIG, T, "put")
        prem = p15.eep(K, T, crude, K, R, Q, SIG, "put", n_quad=64)
        raw = p15.american_from_boundary(K, T, crude, K, R, Q, SIG, "put",
                                         n_quad=64)
        self.assertAlmostEqual(raw, euro + prem, places=12)


class TestOracle(unittest.TestCase):

    def test_tree_oracle_converges(self):
        oracle, spread = p15.tree_oracle(K, K, R, Q, SIG, T, "put",
                                         Ns=(4000, 6000, 8000))
        self.assertLess(spread, 2e-3)
        self.assertAlmostEqual(oracle, 7.662, delta=5e-3)

    def test_tree_oracle_hard_case(self):
        # Review claim 5: stable values where the Volterra solver is
        # grid-sensitive.
        oracle, spread = p15.tree_oracle(120.0, K, 0.05, 0.10, 0.2, 3.0,
                                         "call", Ns=(8000, 10000, 12000))
        self.assertLess(spread, 5e-3)
        self.assertAlmostEqual(oracle, 20.69, delta=2e-2)


class TestBoundarySolver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.taus_c, cls.bvals_c = p15.solve_boundary(K, R, Q, SIG, T,
                                                     "call", n_grid=200,
                                                     n_quad=44, delta=1e-8)
        cls.taus_p, cls.bvals_p = p15.solve_boundary(K, R, Q, SIG, T,
                                                     "put", n_grid=200,
                                                     n_quad=44, delta=1e-8)

    def test_anchors(self):
        self.assertAlmostEqual(self.bvals_c[0], K)
        self.assertAlmostEqual(self.bvals_p[0], K)

    def test_monotonicity_is_solver_enforced(self):
        # Documented: monotone output is a property of the solver's
        # clipping, asserted here as a consistency check only.
        self.assertTrue(np.all(np.diff(self.bvals_c) >= -1e-9))
        self.assertTrue(np.all(np.diff(self.bvals_p) <= 1e-9))

    def test_diagnostics_exposed(self):
        self.assertIn("fallbacks", p15.SOLVER_DIAGNOSTICS)
        # the hard long-maturity case is known to trigger flat steps
        p15.solve_boundary(K, 0.05, 0.10, 0.2, 3.0, "call", n_grid=200,
                           n_quad=40, delta=1e-8)
        self.assertGreater(p15.SOLVER_DIAGNOSTICS["fallbacks"], 0)

    def test_grid_convergence_soft_regime(self):
        oracle, _ = p15.tree_oracle(K, K, R, Q, SIG, T, "put",
                                    Ns=(4000, 6000, 8000))
        prices = []
        for n in (200, 400):
            taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                             n_grid=n, n_quad=44,
                                             delta=1e-8)
            bd = interp_bd(taus, bvals)
            prices.append(p15.american_from_boundary(K, T, bd, K, R, Q,
                                                     SIG, "put", n_quad=96))
        self.assertLess(abs(prices[0] - prices[1]), 5e-3)
        for p_ in prices:
            self.assertLess(abs(p_ - oracle), 1e-2)

    def test_grid_sensitivity_hard_regime_documented(self):
        # Review claim 5: the solver is NOT reliable in this regime; the
        # oracle is.  This test pins the documented behavior, not solver
        # accuracy.
        oracle, spread = p15.tree_oracle(120.0, K, 0.05, 0.10, 0.2, 3.0,
                                         "call", Ns=(8000, 10000, 12000))
        self.assertLess(spread, 5e-3)
        prices = []
        for n in (250, 300, 350):
            taus, bvals = p15.solve_boundary(K, 0.05, 0.10, 0.2, 3.0,
                                             "call", n_grid=n, n_quad=44,
                                             delta=1e-8)
            bd = interp_bd(taus, bvals)
            prices.append(p15.american_from_boundary(120.0, 3.0, bd, K,
                                                     0.05, 0.10, 0.2,
                                                     "call", n_quad=96))
        grid_spread = max(prices) - min(prices)
        self.assertGreater(grid_spread, 0.05)  # sensitivity is real
        for p_ in prices:
            self.assertLess(abs(p_ - oracle), 0.5)  # bounded degradation

    def test_reference_prices_external_true_values(self):
        # Ju-exhibit TRUE prices (10,000-step binomial)
        taus, bvals = p15.solve_boundary(40.0, 0.0488, 0.0, 0.2, 0.5833,
                                         "put", n_grid=250, n_quad=44,
                                         delta=1e-8)
        price = p15.american_from_boundary(40.0, 0.5833,
                                           interp_bd(taus, bvals),
                                           40.0, 0.0488, 0.0, 0.2, "put",
                                           n_quad=96)
        self.assertAlmostEqual(price, 1.990, delta=1e-2)
        taus, bvals = p15.solve_boundary(100.0, 0.03, 0.07, 0.4, 0.5,
                                         "call", n_grid=250, n_quad=44,
                                         delta=1e-8)
        price = p15.american_from_boundary(100.0, 0.5,
                                           interp_bd(taus, bvals),
                                           100.0, 0.03, 0.07, 0.4, "call",
                                           n_quad=96)
        self.assertAlmostEqual(price, 10.239, delta=1.5e-2)

    def test_put_call_symmetry_off_atm(self):
        # Review ask: off-ATM duality P(S,K,r,q) = C(K,S,q,r).
        r, q = 0.07, 0.03
        S = 90.0
        taus_p, bv_p = p15.solve_boundary(K, r, q, SIG, T, "put",
                                          n_grid=200, n_quad=44, delta=1e-8)
        # swapped call: spot K, strike S, rate q, dividend r
        taus_c, bv_c = p15.solve_boundary(S, q, r, SIG, T, "call",
                                          n_grid=200, n_quad=44, delta=1e-8)
        P = p15.american_from_boundary(S, T, interp_bd(taus_p, bv_p), K,
                                       r, q, SIG, "put", n_quad=96)
        C = p15.american_from_boundary(K, T, interp_bd(taus_c, bv_c), S,
                                       q, r, SIG, "call", n_quad=96)
        self.assertAlmostEqual(P, C, delta=1.5e-2)

    def test_short_expiry_regimes(self):
        # Evans–Kuske–Keller / Chen–Zhu regimes for the put boundary:
        #   q < r:  (K - b)/K ~ sigma*sqrt(tau|ln tau|)      -> 1/sqrt(2)
        #           in the sqrt(2 tau |ln tau|) normalization
        #   q = r:  coefficient 1 in that normalization
        #   q > r:  b = (r/q)K(1 - xi1 sigma sqrt(2 tau)), xi1 ~ 0.4517
        def near_expiry(r_, q_, Tfit=0.02):
            taus, bv = p15.solve_boundary(K, r_, q_, 0.2, Tfit, "put",
                                          n_grid=400, n_quad=40, delta=1e-9,
                                          cluster=2.0)
            b0 = p15.boundary_at_maturity(K, r_, q_, "put")
            xs, ys, sq = [], [], []
            for i in range(1, len(taus)):
                if taus[i] > 0.008 or bv[i] == bv[i - 1]:
                    continue
                xs.append(0.2 * math.sqrt(2 * taus[i]
                                          * abs(math.log(taus[i]))))
                ys.append((b0 - bv[i]) / K)
                sq.append(math.sqrt(2 * taus[i]))
            coef_log = np.polyfit(xs, ys, 1)[0] if len(xs) > 5 else None
            coef_root = np.polyfit(sq, ys, 1)[0] if len(sq) > 5 else None
            return coef_log, coef_root

        c_log, _ = near_expiry(0.05, 0.05)
        self.assertIsNotNone(c_log)
        self.assertTrue(0.85 <= c_log <= 1.25, f"q=r coeff {c_log}")

        c_log, _ = near_expiry(0.07, 0.03)
        self.assertIsNotNone(c_log)
        self.assertTrue(0.55 <= c_log <= 0.90, f"q<r coeff {c_log}")

        _, c_root = near_expiry(0.03, 0.07)
        self.assertIsNotNone(c_root)
        theory = (0.03 / 0.07) * 0.4517 * 0.2
        self.assertTrue(0.5 * theory <= c_root <= 1.6 * theory,
                        f"q>r sqrt slope {c_root} vs {theory}")


class TestSpiralFormula(unittest.TestCase):

    def test_spiral_limits(self):
        b0 = p15.boundary_at_maturity(K, R, Q, "call")
        _, b_inf = p15.perpetual_american(K, K, R, Q, SIG, "call")
        self.assertAlmostEqual(p15.spiral_boundary(0.0, b0, b_inf, 2.0), b0)
        self.assertAlmostEqual(p15.spiral_boundary(50.0, b0, b_inf, 2.0),
                               b_inf, places=6)
        # refined family: both short-maturity bases vanish at tau->0 and
        # decay at infinity, so both anchors are exact
        for eta_root in (0.0, 0.5):
            self.assertAlmostEqual(
                p15.spiral_refined_boundary(0.0, b0, b_inf, SIG, 0.7, 1.0,
                                            1.0, eta_root=eta_root),
                b0)
            self.assertAlmostEqual(
                p15.spiral_refined_boundary(80.0, b0, b_inf, SIG, 0.7, 1.0,
                                            1.0, eta_root=eta_root),
                b_inf, delta=1e-3 * b_inf)

    def test_shapes_smooth_and_dimensionless(self):
        # psi_log is smooth on (0, inf): bounded second difference through
        # the old cusp point tau = 1
        h = 1e-2
        for tau in (0.5, 1.0, 2.0):
            d2 = (p15.spiral_shape_log(tau + h)
                  - 2.0 * p15.spiral_shape_log(tau)
                  + p15.spiral_shape_log(tau - h)) / h ** 2
            self.assertTrue(math.isfinite(d2) and abs(d2) < 50.0,
                            f"curvature at tau={tau}: {d2}")

    def test_no_cusp_and_monotone_through_tau_one(self):
        # Review claim 3 regression: the old family gave
        # b(0.9)=132.3 > b(1.0)=129.9 < b(1.1)=136.2 for the T=3 call.
        for kind, cmp in (("call", lambda a, b: a <= b),
                          ("put", lambda a, b: a >= b)):
            k1, k2, el, er, _ = p15.spiral_collocation(K, R, Q, SIG, 3.0,
                                                       kind)
            b0 = p15.boundary_at_maturity(K, R, Q, kind)
            _, b_inf = p15.perpetual_american(K, K, R, Q, SIG, kind)
            vals = [p15.spiral_refined_boundary(t, b0, b_inf, SIG, el, k1,
                                                k2, eta_root=er)
                    for t in (0.9, 1.0, 1.1)]
            self.assertTrue(cmp(vals[0], vals[1]) and cmp(vals[1], vals[2]),
                            f"{kind}: {vals}")

    def test_time_unit_invariance(self):
        # Review ask: the formula must not depend on the human time unit.
        # Years:
        p_yr, *_ = p15.american_spiral(K, K, R, Q, SIG, T, "put")
        # Same option expressed in months: rates per month, sigma per
        # sqrt(month), tau in months, tau_hat = 12 months.
        p_mo, *_ = p15.american_spiral(K, K, R / 12.0, Q / 12.0,
                                       SIG / math.sqrt(12.0), 12.0 * T,
                                       "put", tau_hat=12.0)
        self.assertAlmostEqual(p_yr, p_mo, delta=5e-3)

    def test_collocation_is_a_reported_projection(self):
        # Review claim: collocation MINIMIZES residuals under box
        # constraints; the residuals must be reported, not assumed zero.
        *_, info = p15.spiral_collocation(K, R, Q, SIG, T, "put")
        for key in ("objective", "residuals", "optimizer_status",
                    "start_sensitivity", "tau_hat"):
            self.assertIn(key, info)
        self.assertGreaterEqual(info["objective"], 0.0)
        self.assertEqual(len(info["residuals"]), 4)

    def test_spiral_beats_baw_atm(self):
        oracle, _ = p15.tree_oracle(K, K, R, Q, SIG, T, "put",
                                    Ns=(4000, 6000, 8000))
        sp, *_ = p15.american_spiral(K, K, R, Q, SIG, T, "put")
        bw = p15.baw(K, K, R, Q, SIG, T, "put")
        self.assertLess(abs(sp - oracle), abs(bw - oracle))
        self.assertLess(abs(sp - oracle), 5e-3)


if __name__ == "__main__":
    unittest.main()
