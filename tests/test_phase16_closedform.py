"""Tests for Phase 16: closed-form American pricing via phase-affine boundaries."""

import math
import unittest

import numpy as np
from scipy import special

import phase15_american as p15
import phase16_closedform as p16

K = 100.0
R, Q, SIG, T = 0.05, 0.05, 0.2, 1.0


class TestOccupationIntegral(unittest.TestCase):

    def test_against_quadrature(self):
        rng = np.random.default_rng(20260903)
        worst = 0.0
        for _ in range(20):
            a = float(rng.uniform(-3.0, 3.0))
            m = float(rng.uniform(-1.5, 1.5))
            lam = float(rng.uniform(0.01, 0.3))
            tau = float(rng.uniform(0.02, 3.0))
            xs, ws = np.polynomial.legendre.leggauss(160)
            s = 0.5 * tau * (xs + 1.0)
            vals = np.exp(-lam * s) * special.ndtr((a + m * s) / np.sqrt(s))
            quad = 0.5 * tau * float(np.dot(ws, vals))
            worst = max(worst, abs(p16.occupation_J(tau, a, m, lam) - quad))
        self.assertLess(worst, 1e-9)

    def test_limits(self):
        tau, lam, m = 2.0, 0.05, 0.3
        big_a = 30.0
        self.assertAlmostEqual(p16.occupation_J(tau, big_a, m, lam),
                               (1 - math.exp(-lam * tau)) / lam, places=9)
        self.assertAlmostEqual(p16.occupation_J(tau, -big_a, m, lam),
                               0.0, places=9)
        self.assertAlmostEqual(p16.occupation_J(0.0, 0.5, m, lam), 0.0)
        # tau -> infinity approaches the perpetual resolvent
        a = 0.4
        nu = math.sqrt(m * m + 2 * lam)
        R_inf = 1.0 / lam - math.exp(-(m + nu) * a) / (nu * (nu + m))
        self.assertAlmostEqual(p16.occupation_J(400.0, a, m, lam), R_inf,
                               places=6)


class TestClosedFormEEP(unittest.TestCase):

    def test_single_piece_matches_phase15_quadrature(self):
        worst = 0.0
        for A, gamma, kind in ((math.log(110.0), 0.3, "call"),
                               (math.log(90.0), -0.2, "call"),
                               (math.log(95.0), 0.4, "put"),
                               (math.log(80.0), -0.1, "put")):
            bd = lambda u, A=A, gamma=gamma: math.exp(A - gamma * u)
            quad = p15.eep(100.0, 1.0, bd, K, R, Q, SIG, kind, n_quad=128)
            cf = p16.eep_affine_closed(100.0, 1.0, A, gamma, K, R, Q, SIG,
                                       kind)
            worst = max(worst, abs(cf - quad))
        self.assertLess(worst, 1e-9)

    def test_single_piece_with_zero_dividend(self):
        bd = lambda u: math.exp(math.log(95.0) - 0.2 * u)
        quad = p15.eep(100.0, 1.0, bd, K, R, 0.0, SIG, "put", n_quad=128)
        # boundary ln b(u) = ln 95 - 0.2 u means gamma = +0.2
        cf = p16.eep_affine_closed(100.0, 1.0, math.log(95.0), 0.2, K, R,
                                   0.0, SIG, "put")
        self.assertAlmostEqual(cf, quad, places=9)

    def test_multipiece_equals_single_piece(self):
        A, gamma = math.log(110.0), 0.3
        knots_u = [0.0, 1.0]
        knots_v = [A, A - gamma]
        for kind in ("call", "put"):
            mp = p16.eep_ppa_closed(100.0, 1.0, knots_u, knots_v, K, R, Q,
                                    SIG, kind)
            sp = p16.eep_affine_closed(100.0, 1.0, A, gamma, K, R, Q, SIG,
                                       kind)
            self.assertAlmostEqual(mp, sp, places=11)

    def test_multipiece_matches_quadrature(self):
        # a kinked boundary, checked against Phase 15 quadrature
        knots_u = [0.0, 0.4, 1.0]
        knots_v = [math.log(100.0), math.log(92.0), math.log(85.0)]
        bd = p16.ppa_boundary_func(knots_u, knots_v)
        for kind in ("call", "put"):
            quad = p15.eep(100.0, 1.0, bd, K, R, Q, SIG, kind, n_quad=160)
            cf = p16.eep_ppa_closed(100.0, 1.0, knots_u, knots_v, K, R, Q,
                                    SIG, kind)
            # tolerance set by the quadrature error of the kinked integrand
            self.assertAlmostEqual(cf, quad, places=7)


class TestPPAPricing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.refs = {}
        for kind in ("call", "put"):
            taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, kind,
                                             n_grid=250, n_quad=48,
                                             delta=1e-8)
            bd = lambda tau, ts=taus, bv=bvals: float(np.interp(tau, ts, bv))
            cls.refs[kind] = bd

    def test_ppa_close_to_reference(self):
        for kind in ("call", "put"):
            bd = self.refs[kind]
            for S in (90.0, 100.0, 110.0):
                ref = p15.american_from_boundary(S, T, bd, K, R, Q, SIG,
                                                 kind, n_quad=96)
                price, _, _ = p16.american_ppa_auto(S, K, R, Q, SIG, T,
                                                    kind, m=8)
                self.assertLess(abs(price - ref), 2e-2)

    def test_q0_call_is_european(self):
        price, _, _ = p16.american_ppa_auto(100.0, K, R, 0.0, SIG, T,
                                            "call", m=8)
        euro = p15.bs_european(100.0, K, R, 0.0, SIG, T, "call")
        self.assertAlmostEqual(price, euro, places=12)

    def test_boundary_monotone_and_anchored(self):
        for kind, sign in (("call", 1), ("put", -1)):
            ku, kv = p16.solve_ppa_pinned(K, R, Q, SIG, T, kind, m=8)
            b0 = p15.boundary_at_maturity(K, R, Q, kind)
            self.assertAlmostEqual(math.exp(kv[0]), b0)
            diffs = np.diff(kv)
            self.assertTrue(np.all(sign * diffs >= -1e-9))

    def test_pinning_at_long_maturity(self):
        ku, kv = p16.solve_ppa_pinned(K, R, Q, SIG, 3.0, "put", m=8)
        _, b_inf = p15.perpetual_american(K, K, R, Q, SIG, "put")
        self.assertAlmostEqual(math.exp(kv[-1]), b_inf, places=10)
        ku2, kv2 = p16.solve_ppa_pinned(K, R, Q, SIG, 0.5, "put", m=8)
        self.assertNotAlmostEqual(math.exp(kv2[-1]), b_inf, places=1)

    def test_price_bounds(self):
        price, _, _ = p16.american_ppa_auto(100.0, K, R, Q, SIG, T, "call",
                                            m=8)
        euro = p15.bs_european(100.0, K, R, Q, SIG, T, "call")
        self.assertGreaterEqual(price, euro - 1e-10)
        self.assertLessEqual(price, 100.0)

    def test_ppa_beats_baw_atm(self):
        bd = self.refs["put"]
        err_ppa = err_baw = 0.0
        for S in (90.0, 100.0, 110.0):
            ref = p15.american_from_boundary(S, T, bd, K, R, Q, SIG, "put",
                                             n_quad=96)
            price, _, _ = p16.american_ppa_auto(S, K, R, Q, SIG, T, "put",
                                                m=8)
            err_ppa = max(err_ppa, abs(price - ref))
            err_baw = max(err_baw, abs(p15.baw(S, K, R, Q, SIG, T, "put")
                                       - ref))
        self.assertLess(err_ppa, err_baw)


if __name__ == "__main__":
    unittest.main()
