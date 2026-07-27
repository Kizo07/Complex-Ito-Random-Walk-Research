"""Tests for the joint two-asset barrier layer in phase6_joint."""

from __future__ import annotations

import math
import unittest

from scipy.integrate import quad

from phase6_joint import (
    clock_moments,
    driftless_touch_probability,
    gamma_touch_price,
    occupation_moments,
    q_variance,
)

DRIVER = dict(x0=0.0, drift=0.3, volatility=0.8, scale=1.0)
ASSETS = dict(alpha1=1.0, alpha2=-1.0, sigma1=1.5, sigma2=2.5)


class ClockVarianceTests(unittest.TestCase):
    def test_spread_and_basket_coefficient_signs(self) -> None:
        base_spread = q_variance(0.0, **ASSETS)
        self.assertAlmostEqual(base_spread, 1.5**2 + 2.5**2, places=15)
        spread_up = q_variance(0.5, **ASSETS)
        basket_up = q_variance(0.5, alpha1=1.0, alpha2=1.0, sigma1=1.5, sigma2=2.5)
        # Correlation reduces spread variance, increases basket variance.
        self.assertLess(spread_up, base_spread)
        self.assertGreater(basket_up, base_spread)

    def test_single_asset_limit(self) -> None:
        # alpha2 = 0 removes correlation from the clock entirely.
        mean_v, var_v = clock_moments(
            1.0, alpha1=1.0, alpha2=0.0, sigma1=1.5, sigma2=2.5, **DRIVER
        )
        self.assertAlmostEqual(mean_v, 1.5**2, places=15)
        self.assertEqual(var_v, 0.0)


class OccupationMomentTests(unittest.TestCase):
    def test_symmetric_driver_has_zero_mean(self) -> None:
        mean_a, var_a = occupation_moments(
            1.2, x0=0.0, drift=0.0, volatility=0.8, scale=1.0
        )
        self.assertAlmostEqual(mean_a, 0.0, places=12)
        self.assertGreater(var_a, 0.0)

    def test_zero_correlation_vol_collapses(self) -> None:
        # With zero driver volatility and zero drift, X is frozen at x0 and
        # A_T = rho(x0) * T deterministically.
        x0, scale = 0.7, 1.3
        frozen = x0 / math.sqrt(x0 * x0 + scale * scale)
        mean_a, var_a = occupation_moments(
            2.0, x0=x0, drift=0.0, volatility=0.0, scale=scale
        )
        self.assertAlmostEqual(mean_a, frozen * 2.0, places=12)
        self.assertAlmostEqual(var_a, 0.0, places=15)

    def test_deterministic_driver_path_integrates_exactly(self) -> None:
        # With zero driver volatility but nonzero drift, rho_s = f(x0 + mu*s)
        # deterministically and the mean is the integral of a smooth function.
        x0, scale, drift = 0.7, 1.3, 0.3
        maturity = 2.0
        mean_a, var_a = occupation_moments(
            maturity, x0=x0, drift=drift, volatility=0.0, scale=scale
        )
        expected, _ = quad(
            lambda s: (x0 + drift * s) / math.sqrt((x0 + drift * s) ** 2 + scale**2),
            0.0, maturity, epsabs=1e-13,
        )
        self.assertAlmostEqual(mean_a, expected, places=10)
        self.assertAlmostEqual(var_a, 0.0, places=15)

    def test_quadrature_order_convergence(self) -> None:
        # Gauss-Hermite convergence is rate-limited by the complex
        # singularities of x/sqrt(x^2+c^2) at x = +/-i*c; order 64 is
        # converged to ~1e-9 for these parameters.
        coarse = occupation_moments(1.5, **DRIVER, gh_order=64, gl_order=64)
        fine = occupation_moments(1.5, **DRIVER, gh_order=128, gl_order=128)
        self.assertAlmostEqual(coarse[0], fine[0], places=8)
        self.assertAlmostEqual(coarse[1], fine[1], places=7)

    def test_mean_bounded_by_horizon(self) -> None:
        mean_a, _ = occupation_moments(1.5, **DRIVER)
        self.assertLess(abs(mean_a), 1.5)


class TouchPriceTests(unittest.TestCase):
    def test_deterministic_clock_matches_closed_form(self) -> None:
        # sigma = 0 freezes rho at rho(x0); the clock is q * T and the price
        # must equal the reflection-principle formula for vol sqrt(q).
        x0, scale = 0.5, 1.0
        frozen = x0 / math.sqrt(x0 * x0 + 1.0)
        q = q_variance(frozen, **ASSETS)
        maturity, distance, rate = 1.3, 2.0, 0.04
        mean_v, var_v = clock_moments(maturity, **ASSETS, x0=x0, drift=0.0,
                                      volatility=0.0, scale=scale)
        self.assertEqual(var_v, 0.0)
        price = gamma_touch_price(
            distance, maturity=maturity, rate=rate,
            mean_clock=mean_v, var_clock=var_v,
        )
        expected = math.exp(-rate * maturity) * 2.0 * (
            1.0 - 0.5 * (1.0 + math.erf(distance / math.sqrt(2.0 * q * maturity)))
        )
        self.assertAlmostEqual(price, expected, places=12)

    def test_barrier_limit_and_monotonicity(self) -> None:
        mean_v, var_v = clock_moments(1.0, **ASSETS, **DRIVER)
        near = gamma_touch_price(
            1e-6, maturity=1.0, rate=0.05, mean_clock=mean_v, var_clock=var_v
        )
        self.assertAlmostEqual(near, math.exp(-0.05), places=6)
        prices = [
            gamma_touch_price(d, maturity=1.0, rate=0.05,
                              mean_clock=mean_v, var_clock=var_v)
            for d in (0.5, 1.5, 3.0, 6.0)
        ]
        self.assertTrue(all(later < earlier for earlier, later in zip(prices, prices[1:])))
        self.assertTrue(all(0.0 < p < math.exp(-0.05) for p in prices))

    def test_gamma_shape_normalization(self) -> None:
        # Gamma-matched price must be a genuine expectation: positive and
        # below the discount factor, for both spread and basket.
        for alpha2 in (-1.0, 1.0):
            mean_v, var_v = clock_moments(
                1.0, alpha1=1.0, alpha2=alpha2, sigma1=1.5, sigma2=2.5, **DRIVER
            )
            price = gamma_touch_price(
                2.0, maturity=1.0, rate=0.05, mean_clock=mean_v, var_clock=var_v
            )
            self.assertGreater(price, 0.0)
            self.assertLess(price, math.exp(-0.05))


class InputValidationTests(unittest.TestCase):
    def test_invalid_inputs_raise(self) -> None:
        with self.assertRaises(ValueError):
            q_variance(1.5, **ASSETS)
        with self.assertRaises(ValueError):
            occupation_moments(-1.0, **DRIVER)
        with self.assertRaises(ValueError):
            clock_moments(1.0, alpha1=0.0, alpha2=0.0, sigma1=1.0, sigma2=1.0, **DRIVER)
        with self.assertRaises(ValueError):
            driftless_touch_probability(0.0, 1.0)
        with self.assertRaises(ValueError):
            gamma_touch_price(1.0, maturity=1.0, rate=0.05,
                              mean_clock=0.0, var_clock=0.0)


if __name__ == "__main__":
    unittest.main()
