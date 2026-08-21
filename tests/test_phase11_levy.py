"""Tests for Phase 11 Levy-powered bounded factors."""

import math
import unittest

import numpy as np

import phase11_levy as p11


VG = p11.VGParams(sigma=0.35, nu=0.8, theta=-0.12)
NIG = p11.NIGParams(alpha=6.0, beta=-1.5, delta=0.9, mu=0.05)


class TestSamplers(unittest.TestCase):
    def test_vg_cumulants(self):
        rng = np.random.default_rng(1)
        sample = p11.sample_vg(1.0, VG, 400000, rng)
        expected_mean = VG.theta
        expected_var = VG.sigma**2 + VG.nu * VG.theta**2
        self.assertLess(abs(float(sample.mean()) - expected_mean), 0.01)
        self.assertLess(abs(float(sample.var()) - expected_var) / expected_var, 0.03)

    def test_nig_cumulants(self):
        rng = np.random.default_rng(2)
        sample = p11.sample_nig(1.0, NIG, 400000, rng)
        g0 = NIG.gamma0
        expected_mean = NIG.mu + NIG.delta * NIG.beta / g0
        expected_var = NIG.delta * NIG.alpha**2 / g0**3
        self.assertLess(abs(float(sample.mean()) - expected_mean), 0.02)
        self.assertLess(abs(float(sample.var()) - expected_var) / expected_var, 0.04)

    def test_exponent_matches_sampler_characteristic_function(self):
        rng = np.random.default_rng(3)
        for u in (0.3, -0.2):
            sample = p11.sample_vg(1.0, VG, 300000, rng)
            empirical = complex(np.mean(np.exp(1j * u * sample)))
            analytic = complex(VG.exponent(u))
            self.assertLess(abs(empirical - np.exp(analytic)), 0.02)


class TestGilPelaez(unittest.TestCase):
    def test_cdf_matches_empirical_vg(self):
        rng = np.random.default_rng(4)
        sample = np.sort(p11.sample_vg(1.0, VG, 200000, rng))
        for q in (0.25, 0.5, 0.75):
            x = float(sample[int(q * sample.size)])
            cdf = p11.gil_pelaez_cdf(x, VG.exponent, maturity=1.0)
            self.assertLess(abs(cdf - q), 0.01)

    def test_digital_price_bounds_and_monotonicity(self):
        prices = [
            p11.digital_price_levy(
                rho_star, maturity=1.0, x0=0.0, scale=1.0, rate=0.03,
                exponent=VG.exponent)
            for rho_star in (0.2, 0.5, 0.8)
        ]
        self.assertTrue(all(lo > hi for lo, hi in zip(prices[:-1], prices[1:])))
        self.assertTrue(all(0.0 <= p <= 1.0 for p in prices))


class TestFKPide(unittest.TestCase):
    def test_phi_zero_is_one(self):
        value = p11.fk_characteristic_levy(
            0.0, maturity=0.7, x0=0.1, drift=0.2, params=VG,
            scale=1.0, n_steps=60, n_grid=400)
        self.assertAlmostEqual(abs(value), 1.0, places=6)

    def test_linear_potential_closed_form_vg(self):
        u, maturity, x0, drift = 0.4, 1.0, 0.2, 0.15
        closed = p11.integrated_exponent_expectation(
            u, maturity=maturity, x0=x0, drift=drift, exponent=VG.exponent)
        approx = p11.fk_characteristic_levy(
            u, maturity=maturity, x0=x0, drift=drift, params=VG,
            scale=1e6, n_steps=250, n_grid=1600, margin_scale=14.0,
            potential=lambda x: x)
        # scale huge => f(x)=x/sqrt(x^2+c^2) ~ x/c; fold into u_eff = u/scale
        # by passing potential directly, so compare with the same u.
        self.assertLess(abs(approx - closed), 0.01)

    def test_mc_benchmark_bounded_map_vg(self):
        rng = np.random.default_rng(5)
        n_paths = 200000
        maturity, x0, scale = 1.0, 0.0, 1.0
        paths = x0 + p11.sample_vg(maturity, VG, n_paths, rng)
        rho_t = paths / np.sqrt(paths**2 + scale**2)
        dts = np.linspace(0.0, maturity, 201)
        # trapezoid clock along the single marginal is impossible; instead
        # benchmark E[exp(i xi A_T)] via conditional decomposition is not
        # available -- benchmark the MARGINAL digital instead.
        price_pide = None
        _ = price_pide
        # Marginal check: P(rho_T >= 0.5): Gil-Pelaez vs MC.
        exact = p11.digital_price_levy(
            0.5, maturity=maturity, x0=x0, scale=scale, rate=0.0,
            exponent=VG.exponent)
        mc = float(np.mean(rho_t >= 0.5))
        se = math.sqrt(mc * (1 - mc) / n_paths)
        self.assertLess(abs(exact - mc), 4 * se + 1e-3)

    def test_gaussian_limit_matches_phase7(self):
        # Tiny-jump NIG limit: alpha large, delta small => near-Gaussian
        # driver; the PIDE must approach the Phase-7 forward-FK result.
        import phase7_term_structure as p7

        tiny = p11.NIGParams(alpha=400.0, beta=0.0, delta=2.0, mu=0.0)
        # variance per unit time ~ delta*alpha^2/gamma^3 = 2*400^2/400^3? 
        # gamma0=alpha => var = delta/alpha = 0.005... choose to match sigma=0.8:
        tiny = p11.NIGParams(alpha=100.0, beta=0.0, delta=64.0, mu=0.0)
        # var = delta*alpha^2/alpha^3 = delta/alpha = 0.64 => sd 0.8
        xi = 0.9
        got = p11.fk_characteristic_levy(
            xi, maturity=1.0, x0=0.0, drift=0.3, params=tiny,
            scale=1.0, n_steps=150, n_grid=1200, margin_scale=10.0)
        reference = p7.fk_characteristic_inhom(
            xi, maturity=1.0, x0=0.0,
            drift=lambda t: 0.3, volatility=lambda t: 0.8, scale=1.0,
            n_steps=400, n_grid=900)
        self.assertLess(abs(got - reference), 0.02)


if __name__ == "__main__":
    unittest.main()
