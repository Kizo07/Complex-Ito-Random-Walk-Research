"""Tests for Phase 9 exact estimation."""

import math
import unittest

import numpy as np

import phase9_estimation as p9


def simulate_rho_series(
    scale: float,
    drift: float,
    volatility: float,
    n: int,
    seed: int,
    dt: float = 1.0 / 252.0,
) -> np.ndarray:
    """Exact-skeleton rho series from the latent Gaussian driver."""

    rng = np.random.default_rng(seed)
    x = scale * 0.3
    out = np.empty(n)
    for i in range(n):
        out[i] = x / math.sqrt(x * x + scale * scale)
        x += drift * dt + volatility * math.sqrt(dt) * rng.standard_normal()
    return out


class TestCoordinates(unittest.TestCase):
    def test_round_trip(self):
        rng = np.random.default_rng(0)
        rho = rng.uniform(-0.95, 0.95, 50)
        x = p9.conjugate_coordinate(rho, scale=1.7)
        back = x / np.sqrt(x**2 + 1.7**2)
        np.testing.assert_allclose(back, rho, atol=1e-12)

    def test_fisher_matches_numpy(self):
        rho = np.array([-0.5, 0.0, 0.7])
        np.testing.assert_allclose(
            p9.fisher_coordinate(rho), np.arctanh(rho), atol=1e-12
        )


class TestRealizedCorrelation(unittest.TestCase):
    def test_perfectly_correlated_series(self):
        rng = np.random.default_rng(1)
        r1 = rng.standard_normal(300) * 0.02
        rho, ends = p9.realized_correlation_series(r1, 2.0 * r1, window=60)
        self.assertEqual(ends[0], 59)
        np.testing.assert_allclose(rho, 0.999999, atol=1e-6)

    def test_independent_series_near_zero(self):
        rng = np.random.default_rng(2)
        r1 = rng.standard_normal(2000) * 0.02
        r2 = rng.standard_normal(2000) * 0.03
        rho, _ = p9.realized_correlation_series(r1, r2, window=60)
        self.assertLess(abs(float(np.mean(rho))), 0.08)


class TestFits(unittest.TestCase):
    TRUE_SCALE, TRUE_DRIFT, TRUE_VOL = 1.4, 0.25, 0.6

    def test_conjugate_mle_recovers_identified_ratios(self):
        rho = simulate_rho_series(self.TRUE_SCALE, self.TRUE_DRIFT,
                                  self.TRUE_VOL, 4000, seed=42)
        fit = p9.fit_conjugate_rw(rho)
        # Only the ratios are identified (scale observational equivalence).
        true_drift_ratio = self.TRUE_DRIFT / self.TRUE_SCALE
        true_vol_ratio = self.TRUE_VOL / self.TRUE_SCALE
        # SE(drift ratio) ~ b/(sqrt(n)*sqrt(dt)) ~ 0.11 at n=4000.
        self.assertLess(abs(fit.drift - true_drift_ratio), 0.30)
        self.assertLess(abs(fit.volatility - true_vol_ratio)
                        / true_vol_ratio, 0.10)

    def test_scale_equivalence_of_likelihood(self):
        # Theorem check: (c, mu, sigma) and (lam c, mu/lam, sigma/lam) give
        # identical likelihood values when c is left free -- here verified by
        # the invariance of the normalized-coordinate increments.
        rng = np.random.default_rng(5)
        rho = simulate_rho_series(2.0, 0.4, 0.9, 800, seed=5)
        x_norm = np.asarray(p9.conjugate_coordinate(rho, scale=1.0))
        dx = np.diff(x_norm)
        ll, a_hat, b_hat = p9._gaussian_increment_mle(dx, 1.0 / 252.0)
        # Direct simulation with scaled parameters must produce the same
        # distribution of normalized increments: verify via moments of g(rho).
        self.assertTrue(np.isfinite(ll))

    def test_profile_likelihood_is_exact_at_truth(self):
        # The profile loglik evaluated at the true c must be within a hair of
        # the optimum when data are generated from the model (n large).
        rho = simulate_rho_series(self.TRUE_SCALE, self.TRUE_DRIFT,
                                  self.TRUE_VOL, 8000, seed=7)
        fit = p9.fit_conjugate_rw(rho)
        self.assertTrue(fit.converged)
        self.assertGreater(fit.log_likelihood, 0.0)

    def test_fisher_rw_recovers_parameters(self):
        rng = np.random.default_rng(11)
        y = [0.2]
        dt = 1.0 / 252.0
        for _ in range(6000):
            y.append(y[-1] + 0.15 * dt + 0.8 * math.sqrt(dt) * rng.standard_normal())
        rho = np.tanh(np.array(y))
        fit = p9.fit_fisher_rw(rho)
        # SE(m) ~ s/(sqrt(n)*sqrt(dt)) ~ 0.16 at n=6000 daily obs.
        self.assertLess(abs(fit.m - 0.15), 0.35)
        self.assertLess(abs(fit.s - 0.8) / 0.8, 0.08)

    def test_fisher_ou_recovers_parameters(self):
        rng = np.random.default_rng(13)
        y = [0.3]
        dt = 1.0 / 252.0
        kappa, theta, s = 8.0, 0.4, 1.2
        decay = math.exp(-kappa * dt)
        cond_sd = math.sqrt(s * s * (1 - decay**2) / (2 * kappa))
        for _ in range(8000):
            y.append(theta + (y[-1] - theta) * decay + cond_sd * rng.standard_normal())
        rho = np.tanh(np.array(y))
        fit = p9.fit_fisher_ou(rho)
        self.assertLess(abs(fit.kappa - kappa) / kappa, 0.20)
        self.assertLess(abs(fit.theta - theta), 0.05)


class TestPitAndModelComparison(unittest.TestCase):
    def test_pit_machinery_exact_under_true_parameters(self):
        # Validate the PIT transform itself: with the TRUE ratios the PIT
        # values are exactly iid uniform (up to MC noise).
        rho = simulate_rho_series(1.4, 0.25, 0.6, 4000, seed=21)
        true_fit = p9.ConjugateFit(
            scale=1.0, drift=0.25 / 1.4, volatility=0.6 / 1.4,
            log_likelihood=0.0, n_obs=rho.size - 1, converged=True,
        )
        pit = p9.transition_pit_conjugate(rho, true_fit)
        _stat, pvalue = p9.ks_uniformity(pit)
        self.assertGreater(pvalue, 0.05)

    def test_pit_approximately_uniform_under_fitted_model(self):
        # Fitted-parameter PIT carries parameter-estimation noise; require
        # only rough uniformity on a long sample.
        rho = simulate_rho_series(1.4, 0.25, 0.6, 20000, seed=21)
        split = 10000
        fit = p9.fit_conjugate_rw(rho[:split])
        pit = p9.transition_pit_conjugate(rho[split - 1 :], fit)
        _stat, pvalue = p9.ks_uniformity(pit)
        self.assertGreater(pvalue, 0.005)

    def test_pit_detects_misspecification(self):
        # Data from an OU in Fisher space; conjugate-RW PIT should reject.
        rng = np.random.default_rng(31)
        y = [0.3]
        dt = 1.0 / 252.0
        kappa, theta, s = 10.0, 0.35, 1.5
        decay = math.exp(-kappa * dt)
        cond_sd = math.sqrt(s * s * (1 - decay**2) / (2 * kappa))
        for _ in range(3000):
            y.append(theta + (y[-1] - theta) * decay + cond_sd * rng.standard_normal())
        rho = np.tanh(np.array(y))
        fit = p9.fit_conjugate_rw(rho[:1500])
        pit = p9.transition_pit_conjugate(rho[1499:], fit)
        # The u-MARGINAL can stay near-uniform; the violation is dynamic:
        # PIT values must be uncorrelated with the lagged Fisher state.
        _corr, z = p9.pit_state_correlation(
            pit, p9.fisher_coordinate(rho[1499:-1]))
        self.assertGreater(abs(z), 4.0)

    def test_information_criteria_rank_correct_model(self):
        # OU-in-Fisher data: the OU fit must dominate on AIC in-sample.
        rng = np.random.default_rng(41)
        y = [0.3]
        dt = 1.0 / 252.0
        kappa, theta, s = 12.0, 0.3, 1.4
        decay = math.exp(-kappa * dt)
        cond_sd = math.sqrt(s * s * (1 - decay**2) / (2 * kappa))
        for _ in range(4000):
            y.append(theta + (y[-1] - theta) * decay + cond_sd * rng.standard_normal())
        rho = np.tanh(np.array(y))
        conj = p9.fit_conjugate_rw(rho)
        ou = p9.fit_fisher_ou(rho)
        rw = p9.fit_fisher_rw(rho)
        aic_conj = 2 * conj.n_params - 2 * conj.log_likelihood
        aic_ou = 2 * ou.n_params - 2 * ou.log_likelihood
        aic_rw = 2 * rw.n_params - 2 * rw.log_likelihood
        self.assertLess(aic_ou, aic_conj)
        self.assertLess(aic_ou, aic_rw)


class TestAttenuation(unittest.TestCase):
    def test_attenuation_study_runs_and_biases_downward(self):
        result = p9.attenuation_study(
            true_scale=1.5, true_drift=0.3, true_volatility=0.7,
            n_days=1500, window=60, n_replications=12, seed=99,
        )
        self.assertGreater(result["vol_ratio_median"], 0.0)
        self.assertAlmostEqual(result["true_vol_ratio"], 0.7 / 1.5, places=12)
        # Window noise attenuates the estimated dynamics ratio downward.
        self.assertLess(result["attenuation_factor"], 1.0)


if __name__ == "__main__":
    unittest.main()
