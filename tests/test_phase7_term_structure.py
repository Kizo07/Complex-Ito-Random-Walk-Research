"""Tests for Phase 7 time-inhomogeneous exactness and term structure."""

import math
import unittest

import numpy as np
from scipy.special import ndtr as scipy_special_ndtr

import phase6_correlation as p6c
import phase7_term_structure as p7


def const_drift(mu: float):
    return lambda t: mu


def const_vol(sigma: float):
    return lambda t: sigma


class TestCurveHelpers(unittest.TestCase):
    def test_mean_curve_constant(self):
        times = [0.25, 1.0, 2.5]
        m = p7.mean_curve(times, x0=0.3, drift=const_drift(0.4))
        np.testing.assert_allclose(m, 0.3 + 0.4 * np.array(times), atol=1e-10)

    def test_variance_curve_linear_vol(self):
        # sigma(t) = a*t  =>  v(t) = a^2 t^3 / 3
        a = 0.7
        v = p7.variance_curve([2.0], volatility=lambda t: a * t)
        self.assertAlmostEqual(v[0], a * a * 8.0 / 3.0, places=10)

    def test_interval_coefficients(self):
        mean_st, var_st = p7.interval_coefficients(
            0.5, 2.0, drift=const_drift(0.3), volatility=const_vol(0.8)
        )
        self.assertAlmostEqual(mean_st, 0.45, places=12)
        self.assertAlmostEqual(var_st, 0.64 * 1.5, places=12)


class TestStaticInheritance(unittest.TestCase):
    """Constant coefficients must reproduce Phase 6 exactly."""

    MU, SIGMA, SCALE, RHO0 = 0.3, 0.8, 1.2, 0.1

    def setUp(self):
        self.drift = const_drift(self.MU)
        self.vol = const_vol(self.SIGMA)

    def test_transition_density_matches_phase6(self):
        for maturity in (0.05, 0.5, 3.0):
            for rho in (-0.5, 0.0, 0.7):
                exact = p7.rho_transition_density_inhom(
                    rho,
                    start=0.0,
                    maturity=maturity,
                    rho_start=self.RHO0,
                    scale=self.SCALE,
                    drift=self.drift,
                    volatility=self.vol,
                )
                legacy = p6c.rho_transition_density(
                    rho,
                    maturity=maturity,
                    rho0=self.RHO0,
                    drift=self.MU,
                    volatility=self.SIGMA,
                    scale=self.SCALE,
                )
                self.assertAlmostEqual(exact, legacy, places=13)

    def test_transition_normalization(self):
        from scipy.integrate import quad

        for maturity in (0.2, 1.7):
            total, _ = quad(
                lambda r: p7.rho_transition_density_inhom(
                    r,
                    start=0.0,
                    maturity=maturity,
                    rho_start=self.RHO0,
                    scale=self.SCALE,
                    drift=self.drift,
                    volatility=self.vol,
                ),
                -1.0,
                1.0,
                epsabs=1e-11,
            )
            self.assertAlmostEqual(total, 1.0, places=8)

    def test_digital_matches_phase6(self):
        for maturity in (0.3, 2.0):
            exact = p7.digital_price_inhom(
                0.6,
                maturity=maturity,
                rho0=self.RHO0,
                scale=self.SCALE,
                rate=0.05,
                drift=self.drift,
                volatility=self.vol,
            )
            legacy = p6c.correlation_digital_price(
                0.6,
                maturity=maturity,
                rho0=self.RHO0,
                drift=self.MU,
                volatility=self.SIGMA,
                scale=self.SCALE,
                rate=0.05,
            )
            self.assertAlmostEqual(exact, legacy, places=13)

    def test_forward_digital_equals_unconditional_at_zero_start(self):
        # With no intermediate information (start=0 observed at rho0), the
        # conditional forward price must equal the expiry digital.
        forward = p7.forward_digital_price_conditional(
            0.55,
            start=0.0,
            maturity=1.4,
            rho_start_observed=self.RHO0,
            scale=self.SCALE,
            rate=0.03,
            drift=self.drift,
            volatility=self.vol,
        )
        direct = p7.digital_price_inhom(
            0.55,
            maturity=1.4,
            rho0=self.RHO0,
            scale=self.SCALE,
            rate=0.03,
            drift=self.drift,
            volatility=self.vol,
        )
        self.assertAlmostEqual(forward, direct, places=12)

    def test_forward_digital_tower_property(self):
        # E over the start marginal of the conditional forward price equals
        # the unconditional digital (law of iterated expectations).  The
        # outer expectation is evaluated by Gauss-Hermite in the conjugate
        # x coordinate, where the start marginal is exactly Gaussian.
        import numpy as np
        from numpy.polynomial.hermite_e import hermegauss

        start, maturity = 0.9, 2.2
        rate = 0.02
        unconditional = p7.digital_price_inhom(
            0.5,
            maturity=maturity,
            rho0=self.RHO0,
            scale=self.SCALE,
            rate=rate,
            drift=self.drift,
            volatility=self.vol,
        )
        mean_st, var_st = p7.interval_coefficients(
            start, maturity, drift=self.drift, volatility=self.vol
        )
        m_s = float(p7.mean_curve([start], x0=p6c.x_from_rho(self.RHO0, scale=self.SCALE),
                                  drift=self.drift)[0])
        v_s = float(p7.variance_curve([start], volatility=self.vol)[0])
        nodes, weights = hermegauss(120)
        x_s = m_s + math.sqrt(v_s) * nodes
        x_star = p6c.x_from_rho(0.5, scale=self.SCALE)
        conditional = scipy_special_ndtr(
            (x_s + mean_st - x_star) / math.sqrt(var_st)
        )
        # Price at 0 = e^{-rT} * E[probability] (discounting from T only).
        tower = (
            math.exp(-rate * maturity)
            * float(weights @ conditional)
            / math.sqrt(2.0 * math.pi)
        )
        self.assertAlmostEqual(tower, unconditional, places=10)

    def test_range_accrual_matches_phase6(self):
        dates = (0.25, 0.5, 1.0, 2.0)
        exact = p7.range_accrual_price_inhom(
            -0.4,
            0.7,
            pay_dates=dates,
            rho0=self.RHO0,
            scale=self.SCALE,
            rate=0.04,
            drift=self.drift,
            volatility=self.vol,
        )
        legacy = p6c.range_accrual_price(
            -0.4,
            0.7,
            pay_dates=dates,
            rho0=self.RHO0,
            drift=self.MU,
            volatility=self.SIGMA,
            scale=self.SCALE,
            rate=0.04,
        )
        self.assertAlmostEqual(exact, legacy, places=12)

    def test_quantile_monotone_and_anchored(self):
        alphas = [0.05, 0.25, 0.5, 0.75, 0.95]
        times = [0.5, 1.0, 2.0]
        q = p7.quantile_term_structure(
            alphas, times, rho0=self.RHO0, scale=self.SCALE,
            drift=self.drift, volatility=self.vol,
        )
        self.assertEqual(q.shape, (5, 3))
        # Monotone in alpha at each time.
        for j in range(q.shape[1]):
            self.assertTrue(np.all(np.diff(q[:, j]) > 0))
        # Median at time 0 equals f(x0) = rho0.
        q0 = p7.quantile_term_structure(
            [0.5], [1e-9], rho0=self.RHO0, scale=self.SCALE,
            drift=self.drift, volatility=self.vol,
        )
        self.assertAlmostEqual(float(q0[0, 0]), self.RHO0, places=6)


class TestProportionalDrift(unittest.TestCase):
    """The proportional class with constant sigma must reproduce Milestone 1."""

    LAM, SIGMA, SCALE, RHO0 = 0.35, 0.9, 1.1, -0.2

    def setUp(self):
        self.model = p7.ProportionalDriftModel(
            lam=self.LAM, scale=self.SCALE,
            volatility=const_vol(self.SIGMA), rho0=self.RHO0,
        )
        # Equivalent constant-coefficient Milestone 1 model:
        # mu = lam * sigma**2.
        self.mu = self.LAM * self.SIGMA**2

    def test_hitting_cdf_matches_phase6_constant_case(self):
        for maturity in (0.4, 1.0, 2.5):
            for rho_star in (0.3, 0.6):
                ours = self.model.hitting_cdf(rho_star, maturity)
                distance = p6c.correlation_barrier_distance(
                    rho0=self.RHO0, rho_star=rho_star, scale=self.SCALE
                )
                legacy = p6c.brownian_hitting_cdf(
                    maturity, distance=distance, drift=self.mu, volatility=self.SIGMA
                )
                self.assertAlmostEqual(ours, legacy, places=12)

    def test_hitting_density_matches_phase6_and_integrates_to_cdf(self):
        from scipy.integrate import quad

        rho_star = 0.5
        for maturity in (0.6, 1.8):
            ours = self.model.hitting_density(maturity, rho_star)
            distance = p6c.correlation_barrier_distance(
                rho0=self.RHO0, rho_star=rho_star, scale=self.SCALE
            )
            legacy = p6c.brownian_hitting_density(
                maturity, distance=distance, drift=self.mu, volatility=self.SIGMA
            )
            self.assertAlmostEqual(ours, legacy, places=12)
        # Finite-horizon identity: the calendar-time density integrates to
        # the hitting CDF at the same horizon.
        horizon = 2.5
        total, _ = quad(
            lambda t: self.model.hitting_density(t, rho_star), 1e-9, horizon,
            epsabs=1e-11, limit=400,
        )
        self.assertAlmostEqual(total, self.model.hitting_cdf(rho_star, horizon), places=7)
        # Perpetual mass (slow IG tail at small lam; loose absolute tolerance).
        total_inf, _ = quad(
            lambda t: self.model.hitting_density(t, rho_star), 1e-9, 800.0,
            epsabs=1e-9, limit=800,
        )
        self.assertAlmostEqual(
            total_inf, self.model.perpetual_hitting_probability(rho_star), places=3
        )

    def test_perpetual_and_band_match_phase6(self):
        rho_star = 0.4
        distance = p6c.correlation_barrier_distance(
            rho0=self.RHO0, rho_star=rho_star, scale=self.SCALE
        )
        legacy_perp = p6c.perpetual_hitting_probability(
            distance=distance, drift=self.mu, volatility=self.SIGMA
        )
        self.assertAlmostEqual(
            self.model.perpetual_hitting_probability(rho_star), legacy_perp, places=13
        )
        band = self.model.band_exit_probability_upper(rho_lower=-0.7, rho_upper=0.5)
        legacy_band = p6c.first_exit_probability_upper(
            start=p6c.x_from_rho(self.RHO0, scale=self.SCALE),
            lower=p6c.x_from_rho(-0.7, scale=self.SCALE),
            upper=p6c.x_from_rho(0.5, scale=self.SCALE),
            drift=self.mu,
            volatility=self.SIGMA,
        )
        self.assertAlmostEqual(band, legacy_band, places=12)

    def test_sigma_level_irrelevance(self):
        """Barrier laws depend on sigma only through v(t): doubling sigma and
        quartering calendar time leaves the CDF unchanged (v invariant)."""

        model_fast = p7.ProportionalDriftModel(
            lam=self.LAM, scale=self.SCALE, volatility=const_vol(2 * self.SIGMA),
            rho0=self.RHO0,
        )
        self.assertAlmostEqual(
            model_fast.hitting_cdf(0.4, 1.3 / 4.0),
            self.model.hitting_cdf(0.4, 1.3),
            places=12,
        )

    def test_time_varying_sigma_same_integrated_variance(self):
        """Two different sigma curves with equal integrated variance give
        identical hitting CDFs (parsimony corollary)."""

        horizon = 1.4

        def vol2(t):
            return math.sqrt(1.0 + math.cos(2.0 * math.pi * t / horizon))

        model_flat = p7.ProportionalDriftModel(
            lam=self.LAM, scale=self.SCALE, volatility=const_vol(1.0), rho0=self.RHO0
        )
        model2 = p7.ProportionalDriftModel(
            lam=self.LAM, scale=self.SCALE, volatility=vol2, rho0=self.RHO0
        )
        self.assertAlmostEqual(
            float(p7.variance_curve([horizon], volatility=vol2)[0]), horizon, places=10
        )
        self.assertAlmostEqual(
            model2.hitting_cdf(0.45, horizon),
            model_flat.hitting_cdf(0.45, horizon),
            places=10,
        )


class TestFKInhomogeneous(unittest.TestCase):
    def test_reduces_to_phase6_constant_coefficients(self):
        # Forward-FK CN solver vs the backward expm solver of Milestone 4
        # (both are exact for time-homogeneous coefficients).
        import phase6_fk as p6f

        xi_values = [0.7, 2.1]
        for xi in xi_values:
            ours = p7.fk_characteristic_inhom(
                xi,
                maturity=1.0,
                x0=0.0,
                drift=const_drift(0.3),
                volatility=const_vol(0.8),
                scale=1.0,
                n_steps=1200,
                n_grid=2000,
            )
            reference = p6f.fk_characteristic(
                xi, maturity=1.0, x0=0.0, drift=0.3, volatility=0.8, scale=1.0,
                n_grid=500,
            )
            # Second-order spatial convergence verified: error ~2e-4 at this
            # discretization level (see PHASE_7_SIMULATION_RESULTS.md).
            self.assertAlmostEqual(ours.real, reference.real, places=3)
            self.assertAlmostEqual(ours.imag, reference.imag, places=3)

    def test_linear_potential_closed_form_variable_coefficients(self):
        # Decisive correctness test for the forward-FK solver: with potential
        # f(x) = x and deterministic mu(t), sigma(t), the functional
        # int_0^T X_s ds is Gaussian with mean x0*T + int_0^T (T-s) mu(s) ds
        # and variance int_0^T (T-s)^2 sigma(s)^2 ds, so phi has a closed form.
        from scipy.integrate import quad

        maturity, x0 = 2.0, -0.2247
        drift = lambda t: 0.3 * (1.0 + 0.5 * math.exp(-t))
        vol = lambda t: 0.9 + 0.4 * t * math.exp(-t)
        mean_g = x0 * maturity + quad(
            lambda s: (maturity - s) * drift(s), 0.0, maturity, epsabs=1e-12
        )[0]
        var_g = quad(
            lambda s: (maturity - s) ** 2 * vol(s) ** 2, 0.0, maturity, epsabs=1e-12
        )[0]
        for xi in (0.3, 0.8):
            expected = complex(
                math.cos(xi * mean_g), math.sin(xi * mean_g)
            ) * math.exp(-0.5 * xi * xi * var_g)
            approx = p7.fk_characteristic_inhom(
                xi,
                maturity=maturity,
                x0=x0,
                drift=drift,
                volatility=vol,
                scale=1.0,
                n_steps=800,
                n_grid=3600,
                margin=10.0,
                potential=lambda x: x,
            )
            # Second-order convergence verified: 1.7e-3 -> 4.2e-4 -> 1.1e-4
            # across grid doublings (PHASE_7_SIMULATION_RESULTS.md).
            self.assertAlmostEqual(approx.real, expected.real, places=3)
            self.assertAlmostEqual(approx.imag, expected.imag, places=3)

    def test_first_moment_matches_marginal_quadrature(self):
        # E[A_T] from phi'(0) must match the exact marginal quadrature
        # int_0^T E[rho_s] ds under variable coefficients.
        import numpy as np
        from numpy.polynomial.hermite_e import hermegauss
        from scipy.integrate import quad

        maturity, scale = 2.0, 1.1
        x0 = p7.x_from_rho(-0.2, scale=scale)
        drift = lambda t: 0.3 * (1.0 + 0.5 * math.exp(-t))
        vol = lambda t: 0.9 + 0.4 * t * math.exp(-t)
        nodes, weights = hermegauss(160)
        w = weights / math.sqrt(2.0 * math.pi)

        def e_rho(t):
            m = float(p7.mean_curve([t], x0=x0, drift=drift)[0])
            sd = math.sqrt(float(p7.variance_curve([t], volatility=vol)[0]))
            xs = m + sd * nodes
            return float(w @ (xs / np.sqrt(xs * xs + scale * scale)))

        exact_ea = quad(e_rho, 0.0, maturity, epsabs=1e-11, limit=200)[0]
        h = 2e-3
        p_plus = p7.fk_characteristic_inhom(
            h, maturity=maturity, x0=x0, drift=drift, volatility=vol,
            scale=scale, n_steps=800, n_grid=900,
        )
        p_minus = p7.fk_characteristic_inhom(
            -h, maturity=maturity, x0=x0, drift=drift, volatility=vol,
            scale=scale, n_steps=800, n_grid=900,
        )
        ea_pde = ((p_plus - p_minus) / (2.0 * h)).imag
        self.assertAlmostEqual(ea_pde, exact_ea, places=4)

    def test_phi_zero_is_one(self):
        value = p7.fk_characteristic_inhom(
            0.0,
            maturity=0.8,
            x0=0.2,
            drift=lambda t: 0.5 * math.cos(3.0 * t),
            volatility=lambda t: 0.6 + 0.2 * math.sin(2.0 * t),
            scale=1.0,
            n_steps=120,
            n_grid=200,
        )
        self.assertAlmostEqual(abs(value), 1.0, places=6)

    def test_localization_margin(self):
        # Keep spatial resolution h fixed while doubling the margin (scale
        # the grid with the margin); the residual difference isolates the
        # localization error, which decays like exp(-margin**2 / 2).
        def run(margin: float) -> complex:
            return p7.fk_characteristic_inhom(
                1.3,
                maturity=1.0,
                x0=0.1,
                drift=lambda t: 0.4 * (1.0 + 0.3 * math.sin(2.0 * t)),
                volatility=lambda t: 0.7 + 0.15 * math.cos(t),
                scale=1.0,
                n_steps=800,
                n_grid=int(56 * margin),
                margin=margin,
            )

        base = run(8.0)
        refined = run(16.0)
        self.assertLess(abs(base - refined), 1e-3)


class TestBootstrap(unittest.TestCase):
    def test_recovers_synthetic_parameters(self):
        true_scale, true_lam = 1.3, 0.4
        vol = const_vol(0.85)
        model = p7.ProportionalDriftModel(
            lam=true_lam, scale=true_scale, volatility=vol, rho0=0.0
        )
        quotes = [
            (T, rho_star, model.digital_price(rho_star, maturity=T, rate=0.04))
            for T, rho_star in [(0.5, 0.3), (1.0, 0.5), (2.0, 0.7), (1.5, 0.2)]
        ]
        fit = p7.bootstrap_proportional(quotes, rho0=0.0, rate=0.04, volatility=vol)
        self.assertAlmostEqual(fit["scale"], true_scale, places=6)
        self.assertAlmostEqual(fit["lam"], true_lam, places=6)
        self.assertLess(fit["max_abs_residual"], 1e-8)


if __name__ == "__main__":
    unittest.main()
