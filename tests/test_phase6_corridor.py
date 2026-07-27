"""Tests for the corridor occupation layer in phase6_corridor."""

from __future__ import annotations

import math
import unittest

import numpy as np

from phase6_corridor import (
    arcsine_cdf,
    corridor_call_price,
    corridor_characteristic,
    corridor_density_grid,
    corridor_digital_price,
    corridor_potential,
    corridor_survival_atom,
    mean_occupation,
)

T = 0.5
ARC = dict(maturity=T, x_lower=0.0, x_upper=30.0, x0=0.0, drift=0.0, volatility=1.0)


class ArcsineAnchorTests(unittest.TestCase):
    """Driftless half-line corridor: the exact law is Levy's arcsine."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.o_grid, cls.p_grid, cls.atom = corridor_density_grid(
            **ARC, n_modes=48, n_points=801, n_grid=800
        )

    def test_no_atom_in_half_line_case(self) -> None:
        self.assertAlmostEqual(self.atom, 0.0, places=12)

    def test_mass_normalized(self) -> None:
        mass = float(np.trapezoid(self.p_grid, self.o_grid))
        self.assertAlmostEqual(mass + self.atom, 1.0, places=8)

    def test_first_moment(self) -> None:
        m1 = float(np.trapezoid(self.o_grid * self.p_grid, self.o_grid))
        self.assertAlmostEqual(m1 + self.atom * T, 0.5 * T, places=4)

    def test_tail_probabilities_match_arcsine(self) -> None:
        for kappa in (0.1, 0.25, 0.5, 0.75, 0.9):
            fk = corridor_digital_price(
                kappa, maturity=T, rate=0.0,
                o_grid=self.o_grid, p_grid=self.p_grid, atom=self.atom,
            )
            exact = 1.0 - arcsine_cdf(kappa)
            self.assertLess(abs(fk - exact), 2e-3)

    def test_characteristic_at_zero_and_symmetry(self) -> None:
        self.assertAlmostEqual(
            corridor_characteristic(0.0, **ARC, n_grid=400), 1.0, places=12
        )
        plus = corridor_characteristic(2.0, **ARC, n_grid=400)
        minus = corridor_characteristic(-2.0, **ARC, n_grid=400)
        self.assertAlmostEqual(plus, minus.conjugate(), places=10)


class MeanOccupationTests(unittest.TestCase):
    def test_full_line_occupies_everything(self) -> None:
        value = mean_occupation(
            T, x_lower=-1e6, x_upper=1e6, x0=0.0, drift=0.3, volatility=0.8
        )
        self.assertAlmostEqual(value, T, places=6)

    def test_matches_direct_quadrature(self) -> None:
        from scipy.integrate import quad

        value = mean_occupation(
            T, x_lower=-0.5, x_upper=1.0, x0=0.2, drift=0.3, volatility=0.8
        )

        def cdf(z: float) -> float:
            return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

        expected, _ = quad(
            lambda t: cdf((1.0 - 0.2 - 0.3 * t) / (0.8 * math.sqrt(t)))
            - cdf((-0.5 - 0.2 - 0.3 * t) / (0.8 * math.sqrt(t))),
            0.0, T, epsabs=1e-12, limit=200,
        )
        self.assertAlmostEqual(value, expected, places=10)


class SurvivalAtomTests(unittest.TestCase):
    def test_atom_bounds_and_limits(self) -> None:
        # Wide corridor, short horizon: atom close to 1.
        wide = corridor_survival_atom(
            maturity=0.05, x_lower=-3.0, x_upper=3.0, x0=0.0,
            drift=0.0, volatility=0.5,
        )
        self.assertGreater(wide, 0.95)
        # Narrow corridor, long horizon: atom close to 0.
        narrow = corridor_survival_atom(
            maturity=10.0, x_lower=-0.1, x_upper=0.1, x0=0.0,
            drift=0.0, volatility=1.0,
        )
        self.assertLess(narrow, 0.05)

    def test_unbounded_corridor_closed_form(self) -> None:
        # [x_lower, inf) with positive drift: atom = 1 - exp(-2 mu (x0-xl)/sig^2).
        drift, vol = 0.6, 0.8
        x0, xl = 0.5, 0.0
        expected = 1.0 - math.exp(-2.0 * drift * (x0 - xl) / vol**2)
        value = corridor_survival_atom(
            maturity=5.0, x_lower=xl, x_upper=math.inf, x0=x0,
            drift=drift, volatility=vol,
        )
        self.assertAlmostEqual(value, expected, places=12)
        # Opposite drift: certain to leave eventually, atom is zero.
        self.assertEqual(
            corridor_survival_atom(
                maturity=5.0, x_lower=xl, x_upper=math.inf, x0=x0,
                drift=-drift, volatility=vol,
            ),
            0.0,
        )


class BoundedCorridorTests(unittest.TestCase):
    """Process starting inside a bounded corridor: atom at T handled."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.kwargs = dict(maturity=T, x_lower=-0.8, x_upper=1.2, x0=0.0,
                          drift=0.3, volatility=0.8)
        cls.o_grid, cls.p_grid, cls.atom = corridor_density_grid(
            **cls.kwargs, n_modes=48, n_points=801, n_grid=800
        )

    def test_atom_positive_and_substantial(self) -> None:
        self.assertGreater(self.atom, 0.5)
        self.assertLess(self.atom, 1.0)

    def test_mass_and_first_moment(self) -> None:
        mass = float(np.trapezoid(self.p_grid, self.o_grid))
        self.assertAlmostEqual(mass + self.atom, 1.0, places=6)
        m1 = float(np.trapezoid(self.o_grid * self.p_grid, self.o_grid))
        anchor = mean_occupation(
            T, x_lower=-0.8, x_upper=1.2, x0=0.0, drift=0.3, volatility=0.8
        )
        # Residual Fourier-truncation bias in the continuous part abutting a
        # large atom; shrinks with K and grid (see notebook convergence study).
        self.assertLess(abs(m1 + self.atom * T - anchor), 5e-3)

    def test_price_ordering(self) -> None:
        digital = corridor_digital_price(
            0.5, maturity=T, rate=0.05,
            o_grid=self.o_grid, p_grid=self.p_grid, atom=self.atom,
        )
        call = corridor_call_price(
            0.5, maturity=T, rate=0.05,
            o_grid=self.o_grid, p_grid=self.p_grid, atom=self.atom,
        )
        self.assertGreater(digital, 0.0)
        self.assertGreater(call, 0.0)
        self.assertLessEqual(call, digital)
        # The atom alone guarantees at least its discounted mass.
        self.assertGreaterEqual(digital, math.exp(-0.05 * T) * self.atom)

    def test_mode_convergence(self) -> None:
        o2, p2, atom2 = corridor_density_grid(
            **self.kwargs, n_modes=96, n_points=801, n_grid=800
        )
        coarse = corridor_digital_price(
            0.5, maturity=T, rate=0.05,
            o_grid=self.o_grid, p_grid=self.p_grid, atom=self.atom,
        )
        fine = corridor_digital_price(
            0.5, maturity=T, rate=0.05, o_grid=o2, p_grid=p2, atom=atom2,
        )
        self.assertLess(abs(coarse - fine), 5e-3)


class PotentialAndValidationTests(unittest.TestCase):
    def test_potential_values(self) -> None:
        grid = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])
        values = corridor_potential(-1.0, 1.0)(grid)
        np.testing.assert_array_equal(values, [0.0, 1.0, 1.0, 1.0, 0.0])

    def test_invalid_inputs_raise(self) -> None:
        with self.assertRaises(ValueError):
            corridor_potential(1.0, -1.0)
        with self.assertRaises(ValueError):
            corridor_density_grid(maturity=-1.0, x_lower=0.0, x_upper=1.0,
                                  x0=0.0, drift=0.0, volatility=1.0)
        with self.assertRaises(ValueError):
            corridor_density_grid(maturity=1.0, x_lower=0.0, x_upper=1.0,
                                  x0=2.0, drift=0.0, volatility=1.0)
        with self.assertRaises(ValueError):
            corridor_digital_price(1.5, maturity=1.0, rate=0.0,
                                   o_grid=np.array([0.0, 1.0]), p_grid=np.array([1.0, 1.0]))
        with self.assertRaises(ValueError):
            mean_occupation(-1.0, x_lower=0.0, x_upper=1.0, x0=0.0,
                            drift=0.0, volatility=1.0)
        with self.assertRaises(ValueError):
            arcsine_cdf(1.5)


if __name__ == "__main__":
    unittest.main()
