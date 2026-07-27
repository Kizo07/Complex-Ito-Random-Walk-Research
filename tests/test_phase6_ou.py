"""Tests for the OU-driver layer in phase6_ou."""

from __future__ import annotations

import math
import unittest

from scipy.integrate import quad

from phase6_correlation import rho_transition_density
from phase6_joint import occupation_moments
from phase6_ou import (
    ou_clock_moments,
    ou_digital_price,
    ou_fk_characteristic,
    ou_occupation_moments,
    ou_rho_stationary_density,
    ou_rho_transition_density,
    ou_transition_mean_var,
)

OU = dict(x0=0.0, kappa=2.0, x_bar=0.1, volatility=0.8, scale=1.0)


class TransitionTests(unittest.TestCase):
    def test_kappa_zero_is_brownian_limit(self) -> None:
        mean, var = ou_transition_mean_var(
            1.5, x0=0.3, kappa=0.0, x_bar=99.0, volatility=0.8
        )
        self.assertEqual((mean, var), (0.3, 0.8**2 * 1.5))

    def test_density_normalization(self) -> None:
        for maturity in (0.2, 1.0, 5.0):
            total, _ = quad(
                lambda r: ou_rho_transition_density(r, maturity=maturity, **OU),
                -1.0, 1.0, epsabs=1e-12,
            )
            self.assertAlmostEqual(total, 1.0, places=9)

    def test_density_matches_bm_as_kappa_vanishes(self) -> None:
        for rho in (-0.4, 0.2, 0.7):
            ou_value = ou_rho_transition_density(
                rho, maturity=1.0, x0=0.0, kappa=1e-9, x_bar=0.0,
                volatility=0.8, scale=1.0,
            )
            bm_value = rho_transition_density(
                rho, maturity=1.0, rho0=0.0, drift=0.0, volatility=0.8, scale=1.0
            )
            self.assertAlmostEqual(ou_value, bm_value, places=6)

    def test_stationary_density_is_long_time_limit(self) -> None:
        for rho in (-0.3, 0.4):
            stationary = ou_rho_stationary_density(rho, **{k: OU[k] for k in ("kappa", "x_bar", "volatility", "scale")})
            long_time = ou_rho_transition_density(rho, maturity=60.0, **OU)
            self.assertAlmostEqual(stationary, long_time, places=4)

    def test_stationary_density_normalization(self) -> None:
        total, _ = quad(
            lambda r: ou_rho_stationary_density(
                r, kappa=2.0, x_bar=0.1, volatility=0.8, scale=1.0
            ),
            -1.0, 1.0, epsabs=1e-12,
        )
        self.assertAlmostEqual(total, 1.0, places=9)


class DigitalTests(unittest.TestCase):
    def test_digital_matches_density_integral(self) -> None:
        kwargs = dict(OU, rate=0.05)
        for rho_star in (-0.3, 0.5):
            price = ou_digital_price(rho_star, maturity=1.0, **kwargs)
            tail, _ = quad(
                lambda r: ou_rho_transition_density(r, maturity=1.0, **OU),
                rho_star, 1.0, epsabs=1e-12,
            )
            self.assertAlmostEqual(price, math.exp(-0.05) * tail, places=10)

    def test_digital_bounds(self) -> None:
        price = ou_digital_price(0.4, maturity=1.0, **OU, rate=0.05)
        self.assertGreater(price, 0.0)
        self.assertLess(price, math.exp(-0.05))


class OccupationMomentTests(unittest.TestCase):
    def test_kappa_vanishes_matches_bm_quadrature(self) -> None:
        kwargs = dict(x0=0.0, x_bar=0.0, volatility=0.8, scale=1.0)
        ou_mean, ou_var = ou_occupation_moments(1.0, kappa=1e-9, **kwargs)
        bm_mean, bm_var = occupation_moments(
            1.0, x0=0.0, drift=0.0, volatility=0.8, scale=1.0
        )
        self.assertAlmostEqual(ou_mean, bm_mean, places=5)
        self.assertAlmostEqual(ou_var, bm_var, places=4)

    def test_mean_reversion_compresses_variance(self) -> None:
        kwargs = dict(x0=0.0, x_bar=0.0, volatility=0.8, scale=1.0)
        _, bm_var = ou_occupation_moments(2.0, kappa=0.0, **kwargs)
        _, ou_var = ou_occupation_moments(2.0, kappa=3.0, **kwargs)
        self.assertLess(ou_var, bm_var)

    def test_clock_moments_relation(self) -> None:
        mean_v, var_v = ou_clock_moments(
            1.0, alpha1=1.0, alpha2=-1.0, sigma1=1.5, sigma2=2.5, **OU
        )
        mean_a, var_a = ou_occupation_moments(1.0, **OU)
        base = 1.5**2 + 2.5**2
        coeff = -2.0 * 1.5 * 2.5
        self.assertAlmostEqual(mean_v, base + coeff * mean_a, places=12)
        self.assertAlmostEqual(var_v, coeff**2 * var_a, places=12)


class FKOuTests(unittest.TestCase):
    def test_phi_zero_and_symmetry(self) -> None:
        self.assertAlmostEqual(
            ou_fk_characteristic(0.0, maturity=0.5, **OU, n_grid=400), 1.0, places=12
        )
        plus = ou_fk_characteristic(2.0, maturity=0.5, **OU, n_grid=400)
        minus = ou_fk_characteristic(-2.0, maturity=0.5, **OU, n_grid=400)
        self.assertAlmostEqual(plus, minus.conjugate(), places=10)

    def test_first_moment_matches_quadrature(self) -> None:
        h = 0.25
        plus = ou_fk_characteristic(h, maturity=0.5, **OU, n_grid=600)
        minus = ou_fk_characteristic(-h, maturity=0.5, **OU, n_grid=600)
        numerical = ((plus - minus) / (2.0 * h) / 1j).real
        mean_q, _ = ou_occupation_moments(0.5, **OU)
        self.assertAlmostEqual(numerical, mean_q, places=3)

    def test_modulus_bounded(self) -> None:
        for xi in (1.0, 5.0, 12.0):
            value = ou_fk_characteristic(xi, maturity=0.5, **OU, n_grid=400)
            self.assertLessEqual(abs(value), 1.0 + 1e-6)


class InputValidationTests(unittest.TestCase):
    def test_invalid_inputs_raise(self) -> None:
        with self.assertRaises(ValueError):
            ou_transition_mean_var(-1.0, x0=0.0, kappa=1.0, x_bar=0.0, volatility=0.8)
        with self.assertRaises(ValueError):
            ou_rho_transition_density(1.5, maturity=1.0, **OU)
        with self.assertRaises(ValueError):
            ou_rho_stationary_density(0.0, kappa=0.0, x_bar=0.0, volatility=0.8, scale=1.0)
        with self.assertRaises(ValueError):
            ou_occupation_moments(1.0, **OU, gh_order=4)
        with self.assertRaises(ValueError):
            ou_clock_moments(1.0, alpha1=0.0, alpha2=0.0, sigma1=1.0, sigma2=1.0, **OU)


if __name__ == "__main__":
    unittest.main()
