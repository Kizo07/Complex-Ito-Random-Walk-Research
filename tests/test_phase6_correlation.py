"""Tests for the exact bounded-correlation laws in phase6_correlation."""

from __future__ import annotations

import math
import unittest

from scipy.integrate import quad

from phase6_correlation import (
    brownian_hitting_cdf,
    brownian_hitting_density,
    correlation_barrier_distance,
    correlation_digital_price,
    discounted_hitting_laplace,
    first_exit_probability_upper,
    one_touch_price_at_expiry,
    one_touch_price_at_hit,
    perpetual_hitting_probability,
    range_accrual_price,
    rho_from_x,
    rho_ito_diffusion,
    rho_ito_drift,
    rho_transition_density,
    x_from_rho,
)


class ConjugateCoordinateTests(unittest.TestCase):
    """The sin-of-phase / rational map must be an exact involution pair."""

    def test_rho_is_sin_of_phase(self) -> None:
        for x in (-3.7, -0.4, 0.0, 0.9, 12.5):
            self.assertAlmostEqual(
                rho_from_x(x, scale=2.0),
                math.sin(math.atan(x / 2.0)),
                places=15,
            )

    def test_x_from_rho_inverts_rho_from_x(self) -> None:
        for x in (-3.7, -0.4, 0.0, 0.9, 12.5):
            self.assertAlmostEqual(
                x_from_rho(rho_from_x(x, scale=1.3), scale=1.3), x, places=12
            )

    def test_conjugate_distance_sign_and_limits(self) -> None:
        distance = correlation_barrier_distance(rho0=0.2, rho_star=0.7, scale=1.0)
        self.assertGreater(distance, 0.0)
        # As rho* -> 1 the conjugate level escapes to infinity.
        self.assertGreater(
            correlation_barrier_distance(rho0=0.2, rho_star=0.999999, scale=1.0), 500.0
        )


class ItoCoefficientTests(unittest.TestCase):
    """The rho-SDE coefficients must match direct Ito differentiation in x."""

    def test_drift_and_diffusion_match_x_coordinate_ito(self) -> None:
        # Independent transcription: Ito derivatives evaluated analytically in
        # the x-coordinate, f'(x) = c^2/(x^2+c^2)^(3/2),
        # f''(x) = -3 c^2 x/(x^2+c^2)^(5/2). A slip in the rho-substitution
        # used inside the module must fail this test.
        mu, sigma, c = 0.31, 0.72, 1.6
        for rho in (-0.8, -0.1, 0.35, 0.9):
            x = x_from_rho(rho, scale=c)
            denom = (x * x + c * c) ** 1.5
            first = c * c / denom
            second = -3.0 * c * c * x / (denom * (x * x + c * c))
            expected_drift = mu * first + 0.5 * sigma**2 * second
            expected_diffusion = sigma * first
            self.assertAlmostEqual(
                rho_ito_drift(rho, drift=mu, volatility=sigma, scale=c),
                expected_drift,
                places=12,
            )
            self.assertAlmostEqual(
                rho_ito_diffusion(rho, volatility=sigma, scale=c),
                expected_diffusion,
                places=12,
            )

    def test_diffusion_vanishes_at_boundaries(self) -> None:
        for rho in (-0.999999, 0.999999):
            self.assertLess(
                rho_ito_diffusion(rho, volatility=1.0, scale=1.0), 1e-7
            )


class TransitionDensityTests(unittest.TestCase):
    """The exact finite-time density must normalize and peak correctly."""

    def test_density_integrates_to_one(self) -> None:
        for maturity in (0.05, 0.5, 3.0):
            total, error = quad(
                lambda r: rho_transition_density(
                    r,
                    maturity=maturity,
                    rho0=0.15,
                    drift=0.2,
                    volatility=0.6,
                    scale=1.1,
                ),
                -1.0,
                1.0,
                epsabs=1e-12,
            )
            self.assertAlmostEqual(total, 1.0, places=9)
            self.assertLess(error, 1e-8)

    def test_density_matches_gaussian_in_conjugate_coordinate(self) -> None:
        # Direct hand evaluation at one point.
        maturity, rho0, mu, sigma, c = 0.7, -0.2, 0.1, 0.5, 2.0
        rho = 0.4
        x = c * rho / math.sqrt(1.0 - rho * rho)
        x0 = c * rho0 / math.sqrt(1.0 - rho0 * rho0)
        sd = sigma * math.sqrt(maturity)
        expected = (
            c
            / (1.0 - rho * rho) ** 1.5
            * math.exp(-0.5 * ((x - x0 - mu * maturity) / sd) ** 2)
            / (sd * math.sqrt(2.0 * math.pi))
        )
        self.assertAlmostEqual(
            rho_transition_density(
                rho, maturity=maturity, rho0=rho0, drift=mu, volatility=sigma, scale=c
            ),
            expected,
            places=15,
        )


class HittingLawTests(unittest.TestCase):
    """Closed-form drifted-Brownian hitting laws transferred to correlation."""

    def test_cdf_integrates_density(self) -> None:
        b, mu, sigma = 0.9, 0.25, 0.8
        for horizon in (0.3, 1.0, 5.0):
            integrated, _ = quad(
                lambda t: brownian_hitting_density(
                    t, distance=b, drift=mu, volatility=sigma
                ),
                1e-12,
                horizon,
                epsabs=1e-12,
            )
            self.assertAlmostEqual(
                brownian_hitting_cdf(
                    horizon, distance=b, drift=mu, volatility=sigma
                ),
                integrated,
                places=8,
            )

    def test_cdf_converges_to_perpetual_probability(self) -> None:
        b, sigma = 1.2, 0.9
        # Driftless hitting tails decay like T**(-1/2), so that case needs a
        # much longer horizon; defective cases converge exponentially fast.
        cases = ((0.4, 1.0, 400.0, 3), (0.0, 1.0, 400000.0, 2), (-0.6, math.exp(2.0 * (-0.6) * b / sigma**2), 400.0, 3))
        for mu, expected, horizon, places in cases:
            limit = brownian_hitting_cdf(
                horizon, distance=b, drift=mu, volatility=sigma
            )
            self.assertAlmostEqual(
                perpetual_hitting_probability(distance=b, drift=mu, volatility=sigma),
                expected,
                places=12,
            )
            self.assertAlmostEqual(limit, expected, places=places)

    def test_density_is_inverse_gaussian_hand_value(self) -> None:
        t, b, mu, sigma = 1.3, 0.8, -0.2, 0.7
        expected = (
            b
            / (sigma * math.sqrt(2.0 * math.pi * t**3))
            * math.exp(-((b - mu * t) ** 2) / (2.0 * sigma**2 * t))
        )
        self.assertAlmostEqual(
            brownian_hitting_density(t, distance=b, drift=mu, volatility=sigma),
            expected,
            places=15,
        )

    def test_driftless_cdf_reflection_principle(self) -> None:
        # For mu = 0, P(tau <= T) = 2 * (1 - Phi(b / (sigma*sqrt(T)))).
        b, sigma, horizon = 1.1, 0.65, 2.2
        expected = 2.0 * (
            1.0 - 0.5 * (1.0 + math.erf(b / (sigma * math.sqrt(2.0 * horizon))))
        )
        self.assertAlmostEqual(
            brownian_hitting_cdf(horizon, distance=b, drift=0.0, volatility=sigma),
            expected,
            places=12,
        )


class ExitProbabilityTests(unittest.TestCase):
    """Two-sided band exit through the scale function."""

    def test_driftless_exit_is_linear(self) -> None:
        self.assertAlmostEqual(
            first_exit_probability_upper(
                start=0.3, lower=-1.0, upper=2.0, drift=0.0, volatility=0.9
            ),
            (0.3 + 1.0) / 3.0,
            places=15,
        )

    def test_strong_positive_drift_favours_upper_exit(self) -> None:
        probability = first_exit_probability_upper(
            start=0.0, lower=-1.0, upper=1.0, drift=5.0, volatility=0.4
        )
        self.assertGreater(probability, 0.999)

    def test_exit_probability_bounds_and_monotonicity(self) -> None:
        for start in (-0.5, 0.0, 0.5):
            probability = first_exit_probability_upper(
                start=start, lower=-1.2, upper=0.8, drift=-0.7, volatility=1.1
            )
            self.assertGreater(probability, 0.0)
            self.assertLess(probability, 1.0)
        lower_start = first_exit_probability_upper(
            start=-0.5, lower=-1.2, upper=0.8, drift=-0.7, volatility=1.1
        )
        higher_start = first_exit_probability_upper(
            start=0.5, lower=-1.2, upper=0.8, drift=-0.7, volatility=1.1
        )
        self.assertLess(lower_start, higher_start)


class InputValidationTests(unittest.TestCase):
    def test_invalid_inputs_raise(self) -> None:
        with self.assertRaises(ValueError):
            rho_from_x(0.5, scale=0.0)
        with self.assertRaises(ValueError):
            x_from_rho(1.0, scale=1.0)
        with self.assertRaises(ValueError):
            rho_transition_density(
                0.0, maturity=-1.0, rho0=0.0, drift=0.0, volatility=1.0, scale=1.0
            )
        with self.assertRaises(ValueError):
            brownian_hitting_cdf(1.0, distance=0.0, drift=0.0, volatility=1.0)
        with self.assertRaises(ValueError):
            first_exit_probability_upper(
                start=2.0, lower=-1.0, upper=1.0, drift=0.0, volatility=1.0
            )


class PricingTests(unittest.TestCase):
    """Exact correlation-derivative prices: identities, limits, and orderings."""

    PARAMS = dict(rho0=0.0, drift=0.3, volatility=0.8, scale=1.0, rate=0.05)

    def test_laplace_zero_rate_recovers_hitting_cdf(self) -> None:
        for drift in (-0.5, 0.0, 0.3):
            for horizon in (0.4, 2.0):
                self.assertAlmostEqual(
                    discounted_hitting_laplace(
                        horizon, distance=0.75, drift=drift, volatility=0.8, rate=0.0
                    ),
                    brownian_hitting_cdf(
                        horizon, distance=0.75, drift=drift, volatility=0.8
                    ),
                    places=10,
                )

    def test_laplace_long_horizon_recovers_classical_transform(self) -> None:
        drift, volatility, rate, distance = 0.3, 0.8, 0.05, 0.75
        gamma = math.sqrt(drift * drift + 2.0 * rate * volatility**2)
        expected = math.exp(-distance * (gamma - drift) / volatility**2)
        self.assertAlmostEqual(
            discounted_hitting_laplace(
                2000.0, distance=distance, drift=drift, volatility=volatility, rate=rate
            ),
            expected,
            places=8,
        )

    def test_price_ordering_hit_expiry_digital(self) -> None:
        for rho_star in (0.4, 0.7, 0.9):
            digital = correlation_digital_price(rho_star, maturity=1.5, **self.PARAMS)
            touch_expiry = one_touch_price_at_expiry(rho_star, maturity=1.5, **self.PARAMS)
            touch_hit = one_touch_price_at_hit(rho_star, maturity=1.5, **self.PARAMS)
            self.assertLessEqual(digital, touch_expiry)
            self.assertLessEqual(touch_expiry, touch_hit)
            self.assertLess(touch_hit, 1.0)

    def test_touch_price_decreases_in_barrier(self) -> None:
        prices = [
            one_touch_price_at_expiry(rho_star, maturity=1.0, **self.PARAMS)
            for rho_star in (0.3, 0.5, 0.7, 0.9)
        ]
        self.assertTrue(all(later < earlier for earlier, later in zip(prices, prices[1:])))
        self.assertLess(prices[-1], math.exp(-self.PARAMS["rate"]))

    def test_digital_full_range_anchor(self) -> None:
        # A digital on rho_T >= -0.999999 is almost surely paid.
        price = correlation_digital_price(-0.999999, maturity=1.0, **self.PARAMS)
        self.assertAlmostEqual(price, math.exp(-self.PARAMS["rate"]), places=3)

    def test_range_accrual_full_band_anchor(self) -> None:
        dates = [0.25 * k for k in range(1, 9)]
        price = range_accrual_price(-1.0, 1.0, pay_dates=dates, **self.PARAMS)
        expected = sum(math.exp(-self.PARAMS["rate"] * d) for d in dates)
        self.assertAlmostEqual(price, expected, places=10)

    def test_range_accrual_monotone_in_band_width(self) -> None:
        dates = [0.5, 1.0]
        narrow = range_accrual_price(-0.2, 0.2, pay_dates=dates, **self.PARAMS)
        wide = range_accrual_price(-0.6, 0.6, pay_dates=dates, **self.PARAMS)
        self.assertLess(narrow, wide)
        self.assertGreater(narrow, 0.0)

    def test_range_accrual_zero_width_band_prices_to_zero(self) -> None:
        eps = 1e-9
        price = range_accrual_price(
            0.5 - eps, 0.5, pay_dates=[1.0], **self.PARAMS
        )
        self.assertLess(price, 1e-6)

    def test_one_touch_requires_upper_barrier(self) -> None:
        with self.assertRaises(ValueError):
            one_touch_price_at_expiry(0.0, maturity=1.0, **self.PARAMS)
        with self.assertRaises(ValueError):
            one_touch_price_at_hit(-0.2, maturity=1.0, **self.PARAMS)


if __name__ == "__main__":
    unittest.main()
