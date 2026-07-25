"""Tests for the financial layer of the one-phase Euler coordinates."""

from __future__ import annotations

import math
import unittest

from phase5_finance import (
    bachelier_call_delta,
    bachelier_call_gamma,
    bachelier_call_price,
    canonical_phase_coefficients,
    phase_generator_action,
    phase_bachelier_call_price,
    scalar_delta_from_phase,
    scalar_gamma_from_phase,
)


class CanonicalPhaseFinanceTests(unittest.TestCase):
    """Catch errors in the transformed arithmetic-Brownian coefficients."""

    def test_coefficients_at_quarter_turn_match_hand_derived_values(self) -> None:
        """A missing Itô term or Jacobian factor must fail this test."""

        drift, diffusion = canonical_phase_coefficients(
            math.pi / 4.0,
            drift=0.3,
            volatility=0.8,
            scale=2.0,
        )

        self.assertAlmostEqual(drift, 0.035, places=14)
        self.assertAlmostEqual(diffusion, 0.2, places=14)

    def test_at_the_money_bachelier_value_and_greeks_are_exact(self) -> None:
        """Wrong normal scaling or discounting must fail this test."""

        discount = 0.97
        standard_deviation = 3.0
        expected_density = 1.0 / math.sqrt(2.0 * math.pi)

        value = bachelier_call_price(
            100.0,
            100.0,
            normal_volatility=standard_deviation,
            maturity=1.0,
            discount=discount,
        )
        delta = bachelier_call_delta(
            100.0,
            100.0,
            normal_volatility=standard_deviation,
            maturity=1.0,
            discount=discount,
        )
        gamma = bachelier_call_gamma(
            100.0,
            100.0,
            normal_volatility=standard_deviation,
            maturity=1.0,
            discount=discount,
        )

        self.assertAlmostEqual(
            value,
            discount * standard_deviation * expected_density,
            places=14,
        )
        self.assertAlmostEqual(delta, discount / 2.0, places=14)
        self.assertAlmostEqual(
            gamma,
            discount * expected_density / standard_deviation,
            places=14,
        )

    def test_phase_price_is_identical_to_scalar_price(self) -> None:
        """Any altered payoff under the coordinate map must fail this test."""

        theta = math.atan(105.0 / 100.0)
        scalar = bachelier_call_price(
            105.0,
            101.0,
            normal_volatility=7.0,
            maturity=0.75,
            discount=0.96,
        )
        phase = phase_bachelier_call_price(
            theta,
            scale=100.0,
            strike=101.0,
            normal_volatility=7.0,
            maturity=0.75,
            discount=0.96,
        )

        self.assertAlmostEqual(phase, scalar, places=13)

    def test_zero_variance_limit_is_discounted_intrinsic_value(self) -> None:
        """Division by zero or a false time value at zero variance must fail."""

        self.assertAlmostEqual(
            bachelier_call_price(
                103.0,
                100.0,
                normal_volatility=0.0,
                maturity=2.0,
                discount=0.95,
            ),
            2.85,
            places=14,
        )
        self.assertEqual(
            bachelier_call_delta(
                103.0,
                100.0,
                normal_volatility=0.0,
                maturity=2.0,
                discount=0.95,
            ),
            0.95,
        )
        self.assertEqual(
            bachelier_call_gamma(
                103.0,
                100.0,
                normal_volatility=0.0,
                maturity=2.0,
                discount=0.95,
            ),
            0.0,
        )

    def test_phase_derivatives_recover_scalar_delta_and_gamma(self) -> None:
        """A wrong Jacobian or Hessian correction must fail this test."""

        scale = 2.0
        theta = math.pi / 4.0
        # For V(x)=x^3 and v(theta)=scale^3 tan(theta)^3, at theta=pi/4:
        # v_theta=6 scale^3 and v_theta_theta=36 scale^3.
        phase_first = 6.0 * scale**3
        phase_second = 36.0 * scale**3

        delta = scalar_delta_from_phase(
            theta,
            scale=scale,
            phase_first=phase_first,
        )
        gamma = scalar_gamma_from_phase(
            theta,
            scale=scale,
            phase_first=phase_first,
            phase_second=phase_second,
        )

        self.assertAlmostEqual(delta, 3.0 * scale**2, places=13)
        self.assertAlmostEqual(gamma, 6.0 * scale, places=13)

    def test_phase_generator_is_conjugate_to_arithmetic_brownian_generator(
        self,
    ) -> None:
        """Dropping either Itô correction must break operator conjugacy."""

        scale = 2.0
        theta = math.pi / 4.0
        drift = 0.3
        volatility = 0.8
        phase_first = 6.0 * scale**3
        phase_second = 36.0 * scale**3

        phase_value = phase_generator_action(
            theta,
            drift=drift,
            volatility=volatility,
            scale=scale,
            phase_first=phase_first,
            phase_second=phase_second,
        )
        # V(x)=x^3 at x=scale: L_X V = drift*3x^2 + 0.5*sigma^2*6x.
        scalar_value = drift * 3.0 * scale**2 + 3.0 * volatility**2 * scale

        self.assertAlmostEqual(phase_value, scalar_value, places=13)


if __name__ == "__main__":
    unittest.main()
