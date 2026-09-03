"""Tests for Phase 15: American options via complex-GBM spiral geometry."""

import math
import unittest

import numpy as np

import phase15_american as p15

S0, K = 100.0, 100.0
R, Q, SIG, T = 0.05, 0.05, 0.2, 1.0


class TestFoundations(unittest.TestCase):

    def test_european_put_call_parity_with_dividends(self):
        for r, q in ((0.05, 0.05), (0.07, 0.03), (0.03, 0.07)):
            c = p15.bs_european(S0, K, r, q, SIG, T, "call")
            p = p15.bs_european(S0, K, r, q, SIG, T, "put")
            self.assertAlmostEqual(c - p,
                                   S0 * math.exp(-q * T)
                                   - K * math.exp(-r * T),
                                   places=10)

    def test_perpetual_value_match_and_smooth_past(self):
        for kind in ("call", "put"):
            _, b_inf = p15.perpetual_american(S0, K, R, Q, SIG, kind)
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
        # r = q: both anchors at the strike
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.05, 0.05,
                                                        "call"), K)
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.05, 0.05,
                                                        "put"), K)
        # r > q: call anchor above strike, put anchor below
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.07, 0.03,
                                                        "call"),
                               K * 0.07 / 0.03)
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.07, 0.03,
                                                        "put"), K)
        # q >= r: call anchor at the strike
        self.assertAlmostEqual(p15.boundary_at_maturity(K, 0.03, 0.07,
                                                        "call"), K)
        # zero dividends: call never exercised
        self.assertTrue(math.isinf(p15.boundary_at_maturity(K, 0.05, 0.0,
                                                            "call")))

    def test_american_call_q0_is_european(self):
        price, k1, k2, eta = p15.american_spiral(S0, K, 0.05, 0.0, SIG, T,
                                                 "call")
        euro = p15.bs_european(S0, K, 0.05, 0.0, SIG, T, "call")
        self.assertAlmostEqual(price, euro, places=12)
        self.assertIsNone(k1)


class TestBoundarySolver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.taus_c, cls.bvals_c = p15.solve_boundary(
            K, R, Q, SIG, T, "call", n_grid=250, n_quad=48, delta=1e-8)
        cls.taus_p, cls.bvals_p = p15.solve_boundary(
            K, R, Q, SIG, T, "put", n_grid=250, n_quad=48, delta=1e-8)

    def test_anchors_and_monotonicity(self):
        self.assertAlmostEqual(self.bvals_c[0], K)
        self.assertAlmostEqual(self.bvals_p[0], K)
        self.assertTrue(np.all(np.diff(self.bvals_c) >= -1e-9))
        self.assertTrue(np.all(np.diff(self.bvals_p) <= 1e-9))
        _, b_inf_c = p15.perpetual_american(K, K, R, Q, SIG, "call")
        self.assertLess(self.bvals_c[-1], b_inf_c * 1.001)
        # one year of the way to the perpetual limit: a loose band
        self.assertGreater(self.bvals_c[-1], 0.6 * b_inf_c)

    def test_value_matching_residuals_small(self):
        for taus, bvals, kind in ((self.taus_c, self.bvals_c, "call"),
                                  (self.taus_p, self.bvals_p, "put")):
            res = [abs(p15.boundary_residual_grid(i, taus, bvals, K, R, Q,
                                                  SIG, kind, n_quad=48))
                   for i in range(1, len(taus), len(taus) // 20)]
            self.assertLess(max(res), 5e-2)

    def test_reference_prices_external_true_values(self):
        # Ju (1998/2000) exhibits: TRUE values from 10,000-step binomial.
        taus, bvals = p15.solve_boundary(40.0, 0.0488, 0.0, 0.2, 0.5833,
                                         "put", n_grid=300, n_quad=48,
                                         delta=1e-8)
        bd = lambda tau: float(np.interp(tau, taus, bvals))
        price = p15.american_from_boundary(40.0, 0.5833, bd, 40.0, 0.0488,
                                           0.0, 0.2, "put", n_quad=96)
        self.assertAlmostEqual(price, 1.990, delta=6e-3)

        taus, bvals = p15.solve_boundary(100.0, 0.03, 0.07, 0.4, 0.5,
                                         "call", n_grid=300, n_quad=48,
                                         delta=1e-8)
        bd = lambda tau: float(np.interp(tau, taus, bvals))
        price = p15.american_from_boundary(100.0, 0.5, bd, 100.0, 0.03,
                                           0.07, 0.4, "call", n_quad=96)
        self.assertAlmostEqual(price, 10.239, delta=6e-3)

    def test_put_call_symmetry(self):
        r, q = 0.07, 0.03
        taus_p, bv_p = p15.solve_boundary(K, r, q, SIG, T, "put",
                                          n_grid=250, n_quad=48, delta=1e-9)
        taus_c, bv_c = p15.solve_boundary(K, q, r, SIG, T, "call",
                                          n_grid=250, n_quad=48, delta=1e-9)
        bd_p = lambda tau: float(np.interp(tau, taus_p, bv_p))
        bd_c = lambda tau: float(np.interp(tau, taus_c, bv_c))
        P = p15.american_from_boundary(S0, T, bd_p, K, r, q, SIG, "put",
                                       n_quad=96)
        C = p15.american_from_boundary(K, T, bd_c, K, q, r, SIG, "call",
                                       n_quad=96)
        self.assertAlmostEqual(P, C, delta=3e-3)

    def test_price_bounds_and_cross_methods(self):
        bd_c = lambda tau: float(np.interp(tau, self.taus_c, self.bvals_c))
        bd_p = lambda tau: float(np.interp(tau, self.taus_p, self.bvals_p))
        CA = p15.american_from_boundary(S0, T, bd_c, K, R, Q, SIG, "call",
                                        n_quad=96)
        PA = p15.american_from_boundary(S0, T, bd_p, K, R, Q, SIG, "put",
                                        n_quad=96)
        ce = p15.bs_european(S0, K, R, Q, SIG, T, "call")
        pe = p15.bs_european(S0, K, R, Q, SIG, T, "put")
        self.assertGreaterEqual(CA, ce)
        self.assertGreaterEqual(PA, pe)
        crr_c = p15.crr_richardson(S0, K, R, Q, SIG, T, "call",
                                   Ns=(1500, 3000, 6000))
        crr_p = p15.crr_richardson(S0, K, R, Q, SIG, T, "put",
                                   Ns=(1500, 3000, 6000))
        self.assertAlmostEqual(CA, crr_c, delta=5e-3)
        self.assertAlmostEqual(PA, crr_p, delta=5e-3)


class TestSpiralFormula(unittest.TestCase):

    def test_spiral_limits(self):
        b0 = p15.boundary_at_maturity(K, R, Q, "call")
        _, b_inf = p15.perpetual_american(K, K, R, Q, SIG, "call")
        self.assertAlmostEqual(p15.spiral_boundary(0.0, b0, b_inf, 2.0), b0)
        self.assertAlmostEqual(p15.spiral_boundary(50.0, b0, b_inf, 2.0),
                               b_inf, places=6)

    def test_refined_spiral_short_maturity_asymptotics(self):
        b0 = p15.boundary_at_maturity(K, R, Q, "put")
        _, b_inf = p15.perpetual_american(K, K, R, Q, SIG, "put")
        tau = 1e-6
        b = p15.spiral_refined_boundary(tau, b0, b_inf, SIG, -1.0, 1.0, 1.0)
        expected = b0 - SIG * b0 * math.sqrt(2.0 * tau * abs(math.log(tau)))
        self.assertAlmostEqual(b / expected, 1.0, places=3)

    def test_collocation_residuals(self):
        for kind in ("call", "put"):
            k1, k2, eta, info = p15.spiral_collocation(K, R, Q, SIG, T, kind)
            self.assertLess(info["objective"], (1e-2 * K) ** 2)
            self.assertTrue(1e-3 < k1 < 60.0)
            self.assertTrue(1e-3 < k2 < 60.0)
            self.assertTrue(0.0 <= eta <= 2.5)

    def test_spiral_beats_baw_atm(self):
        taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                         n_grid=250, n_quad=48, delta=1e-8)
        bd = lambda tau: float(np.interp(tau, taus, bvals))
        err_sp = 0.0
        err_bw = 0.0
        for S in (90.0, 100.0, 110.0):
            ref = p15.american_from_boundary(S, T, bd, K, R, Q, SIG, "put",
                                             n_quad=96)
            sp, _, _, _ = p15.american_spiral(S, K, R, Q, SIG, T, "put")
            bw = p15.baw(S, K, R, Q, SIG, T, "put")
            err_sp = max(err_sp, abs(sp - ref))
            err_bw = max(err_bw, abs(bw - ref))
        self.assertLess(err_sp, err_bw)
        self.assertLess(err_sp, 2e-2)

    def test_spiral_price_bounds(self):
        sp, _, _, _ = p15.american_spiral(S0, K, R, Q, SIG, T, "call")
        euro = p15.bs_european(S0, K, R, Q, SIG, T, "call")
        self.assertGreaterEqual(sp, euro - 1e-10)
        self.assertLessEqual(sp, S0)
        sp, _, _, _ = p15.american_spiral(S0, K, R, Q, SIG, T, "put")
        self.assertLessEqual(sp, K)


if __name__ == "__main__":
    unittest.main()
