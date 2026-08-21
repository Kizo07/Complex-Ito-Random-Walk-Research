"""Tests for Phase 10 correlation-matrix processes (Phase-Gram)."""

import math
import unittest

import numpy as np

import phase10_matrix as p10


class TestAngleMap(unittest.TestCase):
    def test_two_assets(self):
        # n=2: single angle; R12 = cos(theta). Orthogonality at pi/2.
        r = p10.correlation_from_angles(np.array([math.pi / 2]), 2)
        np.testing.assert_allclose(r, np.eye(2), atol=1e-14)
        r2 = p10.correlation_from_angles(np.array([math.pi / 3]), 2)
        self.assertAlmostEqual(r2[0, 1], math.cos(math.pi / 3), places=14)
        r0 = p10.correlation_from_angles(np.array([0.0]), 2)
        self.assertAlmostEqual(r0[0, 1], 1.0, places=14)

    def test_psd_and_unit_diagonal_random(self):
        rng = np.random.default_rng(0)
        for n in (2, 3, 4, 5):
            d = p10.n_angles(n)
            angles = rng.uniform(-math.pi, math.pi, d)
            corr = p10.correlation_from_angles(angles, n)
            np.testing.assert_allclose(corr, corr.T, atol=1e-14)
            np.testing.assert_allclose(np.diag(corr), 1.0, atol=1e-12)
            eigenvalues = np.linalg.eigvalsh(corr)
            self.assertGreaterEqual(float(eigenvalues.min()), -1e-10)

    def test_three_asset_free_entry_formula(self):
        # For n=3 the map must satisfy R23 = cos a cos b + sin a sin b cos g.
        rng = np.random.default_rng(1)
        for _ in range(50):
            a, b, g = rng.uniform(-3, 3, 3)
            corr = p10.correlation_from_angles(np.array([a, b, g]), 3)
            expected = math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(g)
            self.assertAlmostEqual(corr[1, 2], expected, places=12)

    def test_deterministic_limit_matches_static_map(self):
        # Zero volatilities: the simulated matrix equals the static map.
        angles0 = np.array([0.4, -0.7, 1.1])
        paths = p10.simulate_angle_system(
            maturity=1.0,
            volatilities=np.zeros(3),
            initial_angles=angles0,
            n_steps=5,
            n_paths=3,
            seed=0,
        )
        static = p10.correlation_from_angles(angles0, 3)
        final = np.array([
            p10.correlation_from_angles(paths[p, -1], 3) for p in range(3)
        ])
        np.testing.assert_allclose(final, np.broadcast_to(static, final.shape), atol=1e-14)


class TestExactMarginals(unittest.TestCase):
    def test_pairwise_marginal_matches_closed_form(self):
        theta0, sigma, maturity = 0.35, 0.9, 2.0
        mean_exact, sd_exact = p10.pairwise_marginal_cos_gaussian(theta0, sigma, maturity)

        paths = p10.simulate_angle_system(
            maturity=maturity,
            volatilities=np.array([sigma]),
            initial_angles=np.array([theta0]),
            n_steps=1,
            n_paths=400000,
            seed=42,
        )
        sample = np.cos(paths[:, -1, 0])
        se_mean = float(sample.std() / math.sqrt(sample.size))
        self.assertLess(abs(float(sample.mean()) - mean_exact), 4 * se_mean + 1e-6)
        self.assertLess(abs(float(sample.std()) - sd_exact), 0.004)

    def test_gh_expectation_matches_closed_form(self):
        theta0, sigma, maturity = 0.35, 0.9, 2.0
        mean_exact, _ = p10.pairwise_marginal_cos_gaussian(theta0, sigma, maturity)
        got = p10.gh_expectation(
            lambda pts: np.cos(pts[:, 0]),
            mean=np.array([theta0]),
            stds=np.array([sigma * math.sqrt(maturity)]),
            n_points=40,
        )
        self.assertAlmostEqual(got, mean_exact, places=10)


class TestThreeAssetLaw(unittest.TestCase):
    SIGMAS = np.array([0.8, 0.6, 0.7])
    ANGLES0 = np.array([0.3, -0.2, 0.5])
    MATURITY = 1.0

    def _mc_moments(self, n_paths=300000, n_steps=200, seed=7):
        paths = p10.simulate_angle_system(
            maturity=self.MATURITY,
            volatilities=self.SIGMAS,
            initial_angles=self.ANGLES0,
            n_steps=n_steps,
            n_paths=n_paths,
            seed=seed,
        )
        a = paths[:, -1, 0]
        b = paths[:, -1, 1]
        g = paths[:, -1, 2]
        return p10.r23_entry(a, b, g)

    def test_r23_mean_gh_vs_mc(self):
        mean_gh = p10.gh_expectation(
            lambda pts: p10.r23_entry(pts[:, 0], pts[:, 1], pts[:, 2]),
            mean=self.ANGLES0,
            stds=self.SIGMAS * math.sqrt(self.MATURITY),
            n_points=30,
        )
        sample = self._mc_moments()
        se = float(sample.std() / math.sqrt(sample.size))
        self.assertLess(abs(mean_gh - float(sample.mean())), 4 * se + 1e-4)

    def test_r23_second_moment_gh_vs_mc(self):
        second_gh = p10.gh_expectation(
            lambda pts: p10.r23_entry(pts[:, 0], pts[:, 1], pts[:, 2]) ** 2,
            mean=self.ANGLES0,
            stds=self.SIGMAS * math.sqrt(self.MATURITY),
            n_points=30,
        )
        sample = self._mc_moments(n_paths=200000)
        se = float((sample**2).std() / math.sqrt(sample.size))
        self.assertLess(abs(second_gh - float(np.mean(sample**2))), 4 * se + 1e-4)

    def test_short_horizon_drift_matches_analytic(self):
        # E[R23(dt)] - R23(0) ~ drift(R23(0)) * dt for small dt.
        dt = 1e-3
        paths = p10.simulate_angle_system(
            maturity=dt,
            volatilities=self.SIGMAS,
            initial_angles=self.ANGLES0,
            n_steps=1,
            n_paths=400000,
            seed=11,
        )
        sample = p10.r23_entry(paths[:, -1, 0], paths[:, -1, 1], paths[:, -1, 2])
        start = float(p10.r23_entry(*self.ANGLES0))
        analytic = p10.r23_drift(
            self.ANGLES0[0], self.ANGLES0[1], self.ANGLES0[2],
            sig_a=self.SIGMAS[0], sig_b=self.SIGMAS[1], sig_g=self.SIGMAS[2],
        )
        empirical = (float(sample.mean()) - start) / dt
        se = float(sample.std() / math.sqrt(sample.size)) / dt
        self.assertLess(abs(empirical - analytic), 5 * se + 1e-3)


class TestEuropeanPayoffs(unittest.TestCase):
    """Correlation derivatives priced by exact Gauss-Hermite vs MC."""

    SIGMAS = np.array([0.8, 0.6, 0.7])
    ANGLES0 = np.array([0.3, -0.2, 0.5])
    MATURITY = 1.0

    def test_correlation_digital(self):
        strike = 0.4
        price_gh = p10.gh_expectation(
            lambda pts: (p10.r23_entry(pts[:, 0], pts[:, 1], pts[:, 2]) >= strike).astype(float),
            mean=self.ANGLES0,
            stds=self.SIGMAS * math.sqrt(self.MATURITY),
            n_points=40,
        )
        paths = p10.simulate_angle_system(
            maturity=self.MATURITY,
            volatilities=self.SIGMAS,
            initial_angles=self.ANGLES0,
            n_steps=100,
            n_paths=300000,
            seed=99,
        )
        sample = p10.r23_entry(paths[:, -1, 0], paths[:, -1, 1], paths[:, -1, 2])
        mc = float(np.mean(sample >= strike))
        se = math.sqrt(mc * (1 - mc) / sample.size)
        self.assertLess(abs(price_gh - mc), 4 * se + 5e-3)

    def test_correlation_call_convergence_in_nodes(self):
        payoff = lambda pts: np.maximum(
            p10.r23_entry(pts[:, 0], pts[:, 1], pts[:, 2]) - 0.3, 0.0
        )
        coarse = p10.gh_expectation(payoff, mean=self.ANGLES0,
                                    stds=self.SIGMAS * math.sqrt(self.MATURITY),
                                    n_points=20)
        fine = p10.gh_expectation(payoff, mean=self.ANGLES0,
                                  stds=self.SIGMAS * math.sqrt(self.MATURITY),
                                  n_points=40)
        # Kinked payoff: product-rule GH converges polynomially; 2.4e-4 at
        # these node counts is the expected level.
        self.assertLess(abs(coarse - fine), 5e-4)


if __name__ == "__main__":
    unittest.main()
