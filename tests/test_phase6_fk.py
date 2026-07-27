"""Tests for the Feynman-Kac resolvent layer in phase6_fk."""

from __future__ import annotations

import math
import unittest

import numpy as np
from scipy.integrate import quad

from phase6_fk import clock_density_grid, fk_characteristic, fk_touch_price
from phase6_joint import driftless_touch_probability, occupation_moments

DRIVER = dict(x0=0.0, drift=0.3, volatility=0.8, scale=1.0)
T = 0.5


class CharacteristicFunctionTests(unittest.TestCase):
    def test_phi_at_zero_is_one(self) -> None:
        self.assertAlmostEqual(
            fk_characteristic(0.0, maturity=T, **DRIVER, n_grid=400), 1.0, places=12
        )

    def test_modulus_bounded(self) -> None:
        for xi in (1.0, 3.7, 9.2):
            value = fk_characteristic(xi, maturity=T, **DRIVER, n_grid=400)
            self.assertLessEqual(abs(value), 1.0 + 1e-6)

    def test_conjugate_symmetry(self) -> None:
        xi = 2.3
        plus = fk_characteristic(xi, maturity=T, **DRIVER, n_grid=400)
        minus = fk_characteristic(-xi, maturity=T, **DRIVER, n_grid=400)
        self.assertAlmostEqual(plus, minus.conjugate(), places=10)

    def test_first_moment_matches_quadrature(self) -> None:
        h = 0.25
        plus = fk_characteristic(h, maturity=T, **DRIVER, n_grid=600)
        minus = fk_characteristic(-h, maturity=T, **DRIVER, n_grid=600)
        numerical = ((plus - minus) / (2.0 * h) / 1j).real
        mean_q, _ = occupation_moments(T, **DRIVER)
        self.assertAlmostEqual(numerical, mean_q, places=3)

    def test_grid_convergence(self) -> None:
        xi = math.pi / T
        coarse = fk_characteristic(xi, maturity=T, **DRIVER, n_grid=800)
        fine = fk_characteristic(xi, maturity=T, **DRIVER, n_grid=3200)
        self.assertAlmostEqual(coarse, fine, places=3)

    def test_localization_margin(self) -> None:
        xi = math.pi / T
        narrow = fk_characteristic(xi, maturity=T, **DRIVER, n_grid=800, margin=8.0)
        wide = fk_characteristic(xi, maturity=T, **DRIVER, n_grid=800, margin=12.0)
        self.assertAlmostEqual(narrow, wide, places=4)


class DensityGridTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.a_grid, cls.p_grid = clock_density_grid(
            maturity=T, **DRIVER, n_modes=48, n_points=1201, n_grid=800
        )

    def test_mass_normalized(self) -> None:
        self.assertAlmostEqual(float(np.trapezoid(self.p_grid, self.a_grid)), 1.0, places=8)

    def test_density_essentially_nonnegative(self) -> None:
        self.assertGreater(float(self.p_grid.min()), -1e-6)

    def test_density_moments_match_quadrature(self) -> None:
        m1 = float(np.trapezoid(self.a_grid * self.p_grid, self.a_grid))
        m2 = float(np.trapezoid(self.a_grid**2 * self.p_grid, self.a_grid))
        mean_q, var_q = occupation_moments(T, **DRIVER)
        self.assertAlmostEqual(m1, mean_q, places=5)
        self.assertAlmostEqual(m2 - m1**2, var_q, places=4)


class FKPriceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.a_grid, cls.p_grid = clock_density_grid(
            maturity=T, **DRIVER, n_modes=48, n_points=1201, n_grid=800
        )
        cls.kwargs = dict(maturity=T, rate=0.05, a_grid=cls.a_grid, p_grid=cls.p_grid)

    def test_fourier_mode_convergence(self) -> None:
        a2, p2 = clock_density_grid(
            maturity=T, **DRIVER, n_modes=96, n_points=1201, n_grid=800
        )
        beta, alpha = 1.5**2 + 2.5**2, -2.0 * 1.5 * 2.5
        coarse = fk_touch_price(1.0, beta=beta, alpha=alpha, **self.kwargs)
        fine = fk_touch_price(1.0, beta=beta, alpha=alpha, maturity=T, rate=0.05,
                              a_grid=a2, p_grid=p2)
        self.assertAlmostEqual(coarse, fine, places=5)

    def test_deterministic_limit(self) -> None:
        # Tiny driver volatility: A_T concentrates on the deterministic
        # integral of f(x0 + drift*s), and the FK price must approach the
        # deterministic-clock reflection-principle price.
        driver = dict(x0=0.0, drift=0.3, volatility=0.05, scale=1.0)
        a, p = clock_density_grid(
            maturity=T, **driver, n_modes=48, n_points=1201, n_grid=800
        )
        beta, alpha = 1.5**2 + 2.5**2, -2.0 * 1.5 * 2.5
        price = fk_touch_price(1.0, beta=beta, alpha=alpha, maturity=T, rate=0.05,
                               a_grid=a, p_grid=p)
        a_det, _ = quad(
            lambda s: (0.3 * s) / math.sqrt((0.3 * s) ** 2 + 1.0), 0.0, T, epsabs=1e-13
        )
        clock = beta * T + alpha * a_det
        expected = math.exp(-0.05 * T) * driftless_touch_probability(1.0, clock)
        self.assertAlmostEqual(price, expected, places=3)

    def test_price_ordering_and_bounds(self) -> None:
        beta, alpha = 1.5**2 + 2.5**2, -2.0 * 1.5 * 2.5
        prices = [
            fk_touch_price(d, beta=beta, alpha=alpha, **self.kwargs)
            for d in (0.5, 1.0, 2.0)
        ]
        self.assertTrue(all(later < earlier for earlier, later in zip(prices, prices[1:])))
        self.assertTrue(all(0.0 < p < math.exp(-0.05 * T) for p in prices))


class InputValidationTests(unittest.TestCase):
    def test_invalid_inputs_raise(self) -> None:
        with self.assertRaises(ValueError):
            fk_characteristic(1.0, maturity=-1.0, **DRIVER)
        with self.assertRaises(ValueError):
            fk_characteristic(1.0, maturity=1.0, **{**DRIVER, "volatility": 0.0})
        with self.assertRaises(ValueError):
            fk_characteristic(1.0, maturity=1.0, **DRIVER, margin=2.0)
        with self.assertRaises(ValueError):
            clock_density_grid(maturity=1.0, **DRIVER, n_modes=4)
        with self.assertRaises(ValueError):
            fk_touch_price(0.0, maturity=1.0, rate=0.05, beta=1.0, alpha=0.0,
                           a_grid=np.array([-1.0, 1.0]), p_grid=np.array([0.5, 0.5]))


if __name__ == "__main__":
    unittest.main()
