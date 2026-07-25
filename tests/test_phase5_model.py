import unittest

import numpy as np
from scipy.integrate import quad

from phase5_model import (
    AffinePhaseParameters,
    additive_required_phase_drift,
    affine_exact_phase_step,
    affine_forward,
    affine_phase,
    affine_phase_coefficients,
    affine_radius,
    affine_scalar_from_phase,
    affine_transition_density,
    canonical_embedding,
    canonical_exact_phase_step,
    canonical_inverse,
    canonical_phase,
    canonical_phase_coefficients,
    canonical_phase_density,
    canonical_radius,
    cayley_complex_coefficients,
    cayley_exact_phase_step,
    cayley_inverse,
    cayley_phase,
    cayley_phase_coefficients,
    cayley_transform,
    cayley_transported_add,
    induced_ito_coefficients,
    moving_line_phase,
    moving_line_radius,
    moving_line_state,
    multiplicative_phase_parameters,
    phase_noise_covariance,
    spiral_eligible,
    spiral_phase,
    spiral_radius,
    spiral_state,
    transported_add,
)


class AffinePhaseParameterTests(unittest.TestCase):
    def test_eligible_parameters_expose_the_exact_line_geometry(self):
        params = AffinePhaseParameters(
            z0=1.2 - 0.4j,
            a=0.7 * (0.3 + 0.8j),
            b=0.3 + 0.8j,
        )

        self.assertAlmostEqual(params.drift_ratio, 0.7)
        self.assertAlmostEqual(params.rho, abs(params.b / params.z0))
        self.assertNotAlmostEqual(np.sin(params.phi), 0.0)
        lower, upper = params.phase_interval
        self.assertAlmostEqual(upper - lower, np.pi)
        self.assertLess(lower, 0.0)
        self.assertGreater(upper, 0.0)

    def test_noncollinear_drift_and_radial_lines_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "collinear"):
            AffinePhaseParameters(z0=1.0 + 0.5j, a=0.4 + 0.1j, b=0.2 + 0.9j)
        with self.assertRaisesRegex(ValueError, "origin"):
            AffinePhaseParameters(z0=2.0 + 0.0j, a=0.3 + 0.0j, b=0.8 + 0.0j)

    def test_zero_and_nonfinite_inputs_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "z0"):
            AffinePhaseParameters(z0=0.0j, a=0.0j, b=1.0j)
        with self.assertRaisesRegex(ValueError, "b"):
            AffinePhaseParameters(z0=1.0 + 0.0j, a=0.0j, b=0.0j)
        with self.assertRaisesRegex(ValueError, "finite"):
            AffinePhaseParameters(z0=1.0 + 0.0j, a=np.nan + 0.0j, b=1.0j)


class CanonicalSecantTests(unittest.TestCase):
    def test_secant_euler_identity_and_inverse_are_exact(self):
        y = np.array([-8.0, -1.5, 0.0, 2.0, 11.0])
        c = 1.7
        z0 = 1.2 - 0.4j

        theta = canonical_phase(y, c)
        reconstructed_y = canonical_inverse(theta, c)
        embedded = canonical_embedding(theta, z0)
        direct = z0 * (1.0 + 1j * y / c)

        np.testing.assert_allclose(reconstructed_y, y, rtol=2e-15, atol=2e-15)
        np.testing.assert_allclose(embedded, direct, rtol=2e-15, atol=2e-15)
        np.testing.assert_allclose(
            canonical_radius(theta),
            np.abs(1.0 + 1j * y / c),
            rtol=2e-15,
            atol=2e-15,
        )
        self.assertTrue(np.all(np.abs(theta) < np.pi / 2.0))

    def test_canonical_phase_coefficients_match_the_ito_derivatives(self):
        theta = np.array([-0.7, -0.1, 0.4])
        mu = 0.35
        sigma = 0.8
        c = 1.4

        drift, diffusion = canonical_phase_coefficients(theta, mu, sigma, c)
        expected_diffusion = sigma * np.cos(theta) ** 2 / c
        expected_drift = (
            mu * np.cos(theta) ** 2 / c
            - sigma**2 * np.sin(theta) * np.cos(theta) ** 3 / c**2
        )

        np.testing.assert_allclose(diffusion, expected_diffusion, rtol=2e-15)
        np.testing.assert_allclose(drift, expected_drift, rtol=2e-15)

    def test_exact_phase_step_is_the_transformed_gaussian_step(self):
        theta = np.array([-0.3, 0.2, 0.7])
        normal = np.array([0.5, -1.2, 0.1])
        h = 0.15
        mu = -0.2
        sigma = 0.9
        c = 1.3

        stepped = canonical_exact_phase_step(theta, h, normal, mu, sigma, c)
        expected_y = c * np.tan(theta) + mu * h + sigma * np.sqrt(h) * normal

        np.testing.assert_allclose(
            c * np.tan(stepped),
            expected_y,
            rtol=2e-15,
            atol=2e-15,
        )

    def test_phase_density_normalizes_and_obeys_the_semigroup(self):
        u = 0.23
        v = -0.31
        mu = 0.2
        sigma = 0.75
        c = 1.1
        h = 0.35
        s = 0.22

        mass, mass_error = quad(
            lambda q: canonical_phase_density(q, u, h, mu, sigma, c),
            -np.pi / 2.0,
            np.pi / 2.0,
            epsabs=2e-11,
        )
        composed, composed_error = quad(
            lambda q: canonical_phase_density(v, q, h, mu, sigma, c)
            * canonical_phase_density(q, u, s, mu, sigma, c),
            -np.pi / 2.0,
            np.pi / 2.0,
            epsabs=2e-10,
        )
        direct = canonical_phase_density(v, u, h + s, mu, sigma, c)

        self.assertLess(mass_error, 2e-9)
        self.assertAlmostEqual(mass, 1.0, places=10)
        self.assertLess(composed_error, 2e-8)
        self.assertAlmostEqual(composed, direct, places=9)

    def test_invalid_canonical_inputs_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            canonical_phase(0.0, 0.0)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            canonical_exact_phase_step(0.0, -0.1, 0.0, 0.0, 1.0, 1.0)
        with self.assertRaisesRegex(ValueError, "nonzero"):
            canonical_phase_density(0.0, 0.0, 0.1, 0.0, 0.0, 1.0)


class GeneralAffinePhaseTests(unittest.TestCase):
    def setUp(self):
        self.params = AffinePhaseParameters(
            z0=1.1 - 0.6j,
            a=-0.45 * (0.25 + 0.9j),
            b=0.25 + 0.9j,
        )

    def test_general_formula_reconstructs_the_full_affine_line(self):
        x = np.array([-40.0, -2.5, 0.0, 1.2, 33.0])
        theta = affine_phase(x, self.params)
        radius = affine_radius(theta, self.params)
        reconstructed_x = affine_scalar_from_phase(theta, self.params)
        reconstructed_z = affine_forward(theta, self.params)
        direct_z = self.params.z0 + self.params.b * x

        np.testing.assert_allclose(reconstructed_x, x, rtol=2e-13, atol=2e-13)
        np.testing.assert_allclose(reconstructed_z, direct_z, rtol=2e-13, atol=2e-13)
        np.testing.assert_allclose(
            radius,
            np.abs(direct_z / self.params.z0),
            rtol=2e-13,
            atol=2e-13,
        )
        lower, upper = self.params.phase_interval
        self.assertTrue(np.all(theta > lower))
        self.assertTrue(np.all(theta < upper))
        self.assertTrue(np.all(radius > 0.0))

    def test_general_phase_sde_matches_derivatives_and_exact_step(self):
        theta = affine_phase(np.array([-1.0, 0.0, 1.5]), self.params)
        drift, diffusion = affine_phase_coefficients(theta, self.params)
        eps = 1e-6
        numerical_derivative = (
            affine_phase(
                affine_scalar_from_phase(theta, self.params) + eps,
                self.params,
            )
            - affine_phase(
                affine_scalar_from_phase(theta, self.params) - eps,
                self.params,
            )
        ) / (2.0 * eps)

        np.testing.assert_allclose(diffusion, numerical_derivative, rtol=2e-9, atol=2e-10)

        normal = np.array([0.1, -0.7, 1.3])
        h = 0.08
        stepped = affine_exact_phase_step(theta, h, normal, self.params)
        expected_x = (
            affine_scalar_from_phase(theta, self.params)
            + self.params.drift_ratio * h
            + np.sqrt(h) * normal
        )
        np.testing.assert_allclose(
            affine_scalar_from_phase(stepped, self.params),
            expected_x,
            rtol=3e-14,
            atol=3e-14,
        )

        # The drift must include the Itô correction, not only lambda*g.
        phi = self.params.phi
        rho = self.params.rho
        g_prime = (
            -2.0
            * rho
            * np.sin(phi - theta)
            * np.cos(phi - theta)
            / np.sin(phi)
        )
        np.testing.assert_allclose(
            drift,
            self.params.drift_ratio * diffusion + 0.5 * diffusion * g_prime,
            rtol=2e-15,
            atol=2e-15,
        )

    def test_general_transition_density_normalizes_for_reversed_orientation(self):
        reversed_params = AffinePhaseParameters(
            z0=1.0 + 0.0j,
            a=-0.45 * (0.25 - 0.9j),
            b=0.25 - 0.9j,
        )
        self.assertLess(np.sin(reversed_params.phi), 0.0)
        lower, upper = reversed_params.phase_interval
        u = affine_phase(0.4, reversed_params)
        mass, error = quad(
            lambda v: affine_transition_density(v, u, 0.3, reversed_params),
            lower,
            upper,
            epsabs=2e-11,
        )

        self.assertLess(error, 2e-9)
        self.assertAlmostEqual(mass, 1.0, places=10)


class CayleyTests(unittest.TestCase):
    def test_cayley_transform_has_unit_modulus_and_exact_inverse(self):
        y = np.array([-20.0, -1.0, 0.0, 3.0, 25.0])
        c = 1.6

        u = cayley_transform(y, c)
        theta = cayley_phase(y, c)

        np.testing.assert_allclose(np.abs(u), 1.0, atol=2e-15)
        np.testing.assert_allclose(u, np.exp(1j * theta), rtol=2e-15, atol=2e-15)
        np.testing.assert_allclose(cayley_inverse(u, c), y, rtol=2e-14, atol=2e-14)
        self.assertTrue(np.all(np.abs(theta) < np.pi))
        self.assertTrue(np.all(np.abs(u + 1.0) > 0.0))

    def test_cayley_phase_and_complex_sdes_match_the_closed_forms(self):
        theta = np.array([-1.2, -0.1, 0.8])
        mu = 0.25
        sigma = 0.7
        c = 1.4

        drift, diffusion = cayley_phase_coefficients(theta, mu, sigma, c)
        half = theta / 2.0
        expected_diffusion = 2.0 * sigma * np.cos(half) ** 2 / c
        expected_drift = (
            2.0 * mu * np.cos(half) ** 2 / c
            - 2.0
            * sigma**2
            * np.sin(half)
            * np.cos(half) ** 3
            / c**2
        )
        np.testing.assert_allclose(diffusion, expected_diffusion, rtol=2e-15)
        np.testing.assert_allclose(drift, expected_drift, rtol=2e-15)

        u = np.exp(1j * theta)
        complex_drift, complex_diffusion = cayley_complex_coefficients(
            u, mu, sigma, c
        )
        expected_complex_diffusion = 1j * sigma * (1.0 + u) ** 2 / (2.0 * c)
        expected_complex_drift = (
            1j * mu * (1.0 + u) ** 2 / (2.0 * c)
            - sigma**2 * (1.0 + u) ** 3 / (4.0 * c**2)
        )
        np.testing.assert_allclose(complex_diffusion, expected_complex_diffusion)
        np.testing.assert_allclose(complex_drift, expected_complex_drift)

        # Itô applied to |U|^2 must have zero drift and diffusion.
        modulus_drift = (
            2.0 * np.real(np.conjugate(u) * complex_drift)
            + np.abs(complex_diffusion) ** 2
        )
        modulus_diffusion = 2.0 * np.real(np.conjugate(u) * complex_diffusion)
        np.testing.assert_allclose(modulus_drift, 0.0, atol=3e-16)
        np.testing.assert_allclose(modulus_diffusion, 0.0, atol=3e-16)

    def test_cayley_exact_step_and_group_law_transport_real_addition(self):
        theta = np.array([-0.5, 0.2, 1.0])
        normal = np.array([0.2, -0.4, 1.1])
        c = 1.2
        h = 0.17
        mu = -0.1
        sigma = 0.8

        stepped = cayley_exact_phase_step(theta, h, normal, mu, sigma, c)
        expected_y = (
            c * np.tan(theta / 2.0) + mu * h + sigma * np.sqrt(h) * normal
        )
        np.testing.assert_allclose(
            c * np.tan(stepped / 2.0),
            expected_y,
            rtol=2e-15,
            atol=2e-15,
        )

        a = cayley_phase(0.7, c)
        b = cayley_phase(-1.1, c)
        combined = cayley_transported_add(a, b)
        self.assertAlmostEqual(combined, cayley_phase(-0.4, c))


class GroupLawTests(unittest.TestCase):
    def test_secant_transported_addition_is_an_abelian_group(self):
        a, b, d = 0.31, -0.52, 0.44

        self.assertAlmostEqual(transported_add(a, 0.0), a)
        self.assertAlmostEqual(transported_add(a, -a), 0.0)
        self.assertAlmostEqual(transported_add(a, b), transported_add(b, a))
        self.assertAlmostEqual(
            transported_add(transported_add(a, b), d),
            transported_add(a, transported_add(b, d)),
        )
        self.assertAlmostEqual(
            np.tan(transported_add(a, b)),
            np.tan(a) + np.tan(b),
        )


class SpiralTests(unittest.TestCase):
    def test_compatible_log_process_reconstructs_a_winding_spiral(self):
        b = 0.35 + 0.8j
        gamma = -0.4
        kappa = gamma * b
        z0 = 1.3 - 0.2j
        t = np.array([0.0, 0.4, 1.2])
        w = np.array([0.0, -0.7, 1.1])

        self.assertTrue(spiral_eligible(kappa, b))
        theta = spiral_phase(t, w, kappa, b)
        radius = spiral_radius(theta, b)
        represented = spiral_state(z0, theta, b)
        direct = z0 * np.exp(kappa * t + b * w)

        np.testing.assert_allclose(represented, direct, rtol=2e-15, atol=2e-15)
        np.testing.assert_allclose(radius, np.abs(direct / z0), rtol=2e-15)
        np.testing.assert_allclose(theta, b.imag * (gamma * t + w), rtol=2e-15)

    def test_incompatible_or_nonangular_log_process_is_rejected(self):
        self.assertFalse(spiral_eligible(0.2 + 0.1j, 0.3 + 0.8j))
        self.assertFalse(spiral_eligible(0.2 + 0.0j, 0.3 + 0.0j))
        with self.assertRaisesRegex(ValueError, "compatible"):
            spiral_phase(1.0, 0.2, 0.2 + 0.1j, 0.3 + 0.8j)


class RigidityTests(unittest.TestCase):
    def test_additive_required_drift_includes_the_full_drift_constraint(self):
        s = np.array([0.4, 0.7])
        s_prime = np.array([-0.2, 0.3])
        ratio = -0.6
        expected = ratio * s + 0.5 * s * s_prime

        np.testing.assert_allclose(
            additive_required_phase_drift(s, s_prime, ratio),
            expected,
        )
        with self.assertRaisesRegex(ValueError, "real"):
            additive_required_phase_drift(s, s_prime, 0.2 + 0.1j)

    def test_induced_ito_coefficients_reconstruct_the_canonical_additive_sde(self):
        theta = np.array([-0.6, 0.0, 0.4])
        z0 = 1.2 - 0.3j
        c = 1.5
        mu = 0.25
        sigma = 0.8
        phase_drift, phase_diffusion = canonical_phase_coefficients(
            theta, mu, sigma, c
        )

        f = 1.0 + 1j * np.tan(theta)
        f_prime = 1j / np.cos(theta) ** 2
        f_second = 2j * np.tan(theta) / np.cos(theta) ** 2
        drift, diffusion = induced_ito_coefficients(
            z0,
            f,
            f_prime,
            f_second,
            phase_drift,
            phase_diffusion,
        )

        np.testing.assert_allclose(drift, 1j * z0 * mu / c, atol=3e-16)
        np.testing.assert_allclose(diffusion, 1j * z0 * sigma / c, atol=3e-16)

    def test_multiplicative_phase_parameters_enforce_log_drift_compatibility(self):
        b = 0.3 + 0.75j
        gamma = -0.4
        log_drift = gamma * b
        a = log_drift + 0.5 * b**2

        k, beta, phase_drift = multiplicative_phase_parameters(a, b)

        self.assertAlmostEqual(k, b.real / b.imag)
        self.assertAlmostEqual(beta, b.imag)
        self.assertAlmostEqual(phase_drift, gamma * b.imag)

        with self.assertRaisesRegex(ValueError, "compatible"):
            multiplicative_phase_parameters(0.2 + 0.3j, b)
        with self.assertRaisesRegex(ValueError, "imaginary"):
            multiplicative_phase_parameters(0.2 + 0.0j, 0.4 + 0.0j)


class MovingLineTests(unittest.TestCase):
    def test_time_dependent_line_chart_reconstructs_noncollinear_affine_state(self):
        z0 = 1.0 + 0.4j
        a = 0.3 - 0.2j
        b = -0.1 + 0.8j
        t = 0.7
        w = np.array([-1.5, 0.0, 2.2])

        theta = moving_line_phase(t, w, z0, a, b)
        radius = moving_line_radius(t, theta, z0, a, b)
        represented = moving_line_state(t, theta, z0, a, b)
        direct = z0 + a * t + b * w

        np.testing.assert_allclose(represented, direct, rtol=3e-15, atol=3e-15)
        np.testing.assert_allclose(radius, np.abs(direct / z0), rtol=3e-15)

    def test_origin_crossing_support_time_is_rejected(self):
        z0 = 1.0 + 0.0j
        a = 0.0 + 1.0j
        b = 1.0 + 1.0j
        # Im((1 + (a/z0)t) * conj(b/z0)) = t - 1.
        with self.assertRaisesRegex(ValueError, "origin"):
            moving_line_phase(1.0, 0.3, z0, a, b)


class RankTests(unittest.TestCase):
    def test_phase_noise_covariance_is_rank_one(self):
        tangent = np.array([1.2, -0.7])
        covariance = phase_noise_covariance(tangent)
        expected = np.outer(tangent, tangent)

        np.testing.assert_allclose(covariance, expected)
        self.assertAlmostEqual(np.linalg.det(covariance), 0.0, places=15)
        self.assertEqual(np.linalg.matrix_rank(covariance, tol=1e-13), 1)


if __name__ == "__main__":
    unittest.main()
