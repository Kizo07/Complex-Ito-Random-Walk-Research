"""Tests for Phase 12 pegged-asset economics."""

import math
import unittest

import numpy as np

import phase12_peg as p12


class TestReflectedBand(unittest.TestCase):
    def test_zero_drift_stationary_is_uniform(self):
        band = p12.BandSpec(lo=-0.02, hi=0.02)
        stat = p12.reflected_band_stationary(band, drift=0.0, sigma=0.01)
        self.assertAlmostEqual(stat["mean"], 0.0, places=12)
        expected_sd = (band.hi - band.lo) / math.sqrt(12.0)
        self.assertAlmostEqual(stat["sd"], expected_sd, places=7)

    def test_positive_drift_shifts_mass_up(self):
        band = p12.BandSpec(lo=-0.02, hi=0.02)
        stat_up = p12.reflected_band_stationary(band, drift=2e-4, sigma=0.01)
        stat_dn = p12.reflected_band_stationary(band, drift=-2e-4, sigma=0.01)
        self.assertGreater(stat_up["mean"], 0.0)
        self.assertLess(stat_dn["mean"], 0.0)


class TestPegHazard(unittest.TestCase):
    def setUp(self):
        self.peg = p12.PegModel(
            lam=-0.25, sigma_z=0.9, scale=1.1, rho0=0.3, rho_star=0.85,
            rate=0.05,
        )

    def test_depeg_probability_matches_phase7(self):
        import phase6_correlation as p6c

        for horizon in (0.5, 1.5, 3.0):
            distance = p6c.correlation_barrier_distance(
                rho0=self.peg.rho0, rho_star=self.peg.rho_star,
                scale=self.peg.scale)
            legacy = p6c.brownian_hitting_cdf(
                horizon, distance=distance,
                drift=self.peg.lam * self.peg.sigma_z**2,
                volatility=self.peg.sigma_z)
            self.assertAlmostEqual(
                self.peg.depeg_probability(horizon), legacy, places=12)

    def test_pay_at_hit_laplace_quadrature(self):
        # Deterministic verification: the closed form must equal the exact
        # integral of e^{-rt} against the Milestone-1 IG hitting density.
        from scipy.integrate import quad

        import phase6_correlation as p6c

        distance = self.peg.distance
        nu = self.peg.lam * self.peg.sigma_z**2
        density = lambda t: p6c.brownian_hitting_density(
            t, distance=distance, drift=nu, volatility=self.peg.sigma_z)
        value, _ = quad(
            lambda t: math.exp(-self.peg.rate * t) * density(t),
            1e-12, 2000.0, limit=800)
        closed = self.peg.pay_at_hit_laplace()
        self.assertAlmostEqual(closed, value, places=6)

    def test_shortfall_swap_positive_and_increasing_in_strike(self):
        band = p12.BandSpec(lo=-0.02, hi=0.03)
        values = [
            self.peg.shortfall_swap(k, horizon=2.0, band=band,
                                    mu_free=-0.15, sigma_free=0.35)
            for k in (0.05, 0.10, 0.20)
        ]
        self.assertTrue(all(v > 0 for v in values))
        self.assertTrue(all(a < b for a, b in zip(values[:-1], values[1:])))

    def test_depeg_digital_discounting(self):
        horizon = 1.0
        raw = self.peg.depeg_probability(horizon)
        priced = self.peg.depeg_digital(horizon)
        self.assertAlmostEqual(priced, math.exp(-self.peg.rate * horizon) * raw,
                               places=14)

    def test_simulation_benchmark_depeg_frequency(self):
        band = p12.BandSpec(lo=-0.02, hi=0.03)
        res = p12.simulate_peg_paths(
            band=band, drift_band=0.0, sigma_band=0.008, peg=self.peg,
            horizon=2.0, mu_free=-0.15, sigma_free=0.35,
            n_paths=100000, n_steps=250, seed=20260821,
        )
        exact = self.peg.depeg_probability(2.0)
        se = math.sqrt(exact * (1 - exact) / 100000)
        self.assertLess(abs(res["depeg_freq"] - exact), 4 * se + 0.002)


if __name__ == "__main__":
    unittest.main()
