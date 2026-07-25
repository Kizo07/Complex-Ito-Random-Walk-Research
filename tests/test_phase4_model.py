import unittest

import numpy as np

from phase4_model import (
    ComplexGBMParameters,
    complex_bracket_rates,
    complex_moment,
    euler_maruyama_path,
    exact_path,
    exact_step,
    gbm_radius,
    log_polar_covariance,
    mixed_log_polar_moment,
    radial_moment,
    two_driver_path,
    unwrapped_phase,
)


class ComplexGBMParametersTests(unittest.TestCase):
    def test_coefficients_include_the_shared_driver_ito_correction(self):
        """Catches replacing the complex square by a modulus square."""
        params = ComplexGBMParameters(
            mu=0.08,
            sigma=0.30,
            omega=0.40,
            beta=0.20,
        )

        self.assertAlmostEqual(params.log_drift.real, 0.035)
        self.assertAlmostEqual(params.log_drift.imag, 0.40)
        self.assertEqual(params.diffusion, 0.30 + 0.20j)
        self.assertAlmostEqual(params.sde_drift.real, 0.06)
        self.assertAlmostEqual(params.sde_drift.imag, 0.46)
        self.assertAlmostEqual(
            params.sde_drift - 0.5 * params.diffusion**2,
            params.log_drift,
        )

    def test_nonfinite_parameters_are_rejected(self):
        """Catches silent propagation of invalid coefficients."""
        with self.assertRaisesRegex(ValueError, "finite"):
            ComplexGBMParameters(0.08, np.nan, 0.40, 0.20)


class ExactPathTests(unittest.TestCase):
    def test_exact_path_has_the_prescribed_modulus_and_unwrapped_phase(self):
        """Catches mixing the radial and angular coefficients in the exponent."""
        params = ComplexGBMParameters(0.08, 0.30, 0.40, 0.20)
        times = np.array([0.0, 1.0, 2.0])
        brownian = np.array([0.0, 0.5, -0.25])
        z0 = 2.0 * np.exp(0.3j)

        z = exact_path(times, brownian, z0, params)
        expected_radius = 2.0 * np.exp(0.035 * times + 0.30 * brownian)
        expected_phase = 0.3 + 0.40 * times + 0.20 * brownian

        np.testing.assert_allclose(np.abs(z), expected_radius, rtol=2e-15)
        np.testing.assert_allclose(
            np.unwrap(np.angle(z)),
            expected_phase,
            rtol=2e-15,
            atol=2e-15,
        )
        np.testing.assert_allclose(
            gbm_radius(times, brownian, abs(z0), params),
            expected_radius,
            rtol=2e-15,
        )
        np.testing.assert_allclose(
            unwrapped_phase(times, brownian, 0.3, params),
            expected_phase,
            rtol=2e-15,
        )

    def test_exact_step_combines_h_and_brownian_increment_in_one_exponent(self):
        """Catches using the SDE drift instead of the compensated log drift."""
        params = ComplexGBMParameters(0.08, 0.30, 0.40, 0.20)
        z0 = 1.2 - 0.7j
        h = 0.25
        d_w = -0.10
        expected = z0 * np.exp((0.035 + 0.40j) * h + (0.30 + 0.20j) * d_w)

        self.assertAlmostEqual(exact_step(z0, h, d_w, params), expected)

    def test_euler_maruyama_uses_the_complex_sde_drift(self):
        """Catches advancing EM with the compensated exponent drift."""
        params = ComplexGBMParameters(0.08, 0.30, 0.40, 0.20)
        z0 = 1.2 - 0.7j
        h = 0.25
        d_w = np.array([-0.10])
        expected = z0 * (
            1.0 + (0.06 + 0.46j) * h + (0.30 + 0.20j) * d_w[0]
        )

        path = euler_maruyama_path(z0, h, d_w, params)

        self.assertEqual(path.shape, (2,))
        self.assertEqual(path[0], z0)
        self.assertAlmostEqual(path[1], expected)

    def test_invalid_path_inputs_are_rejected(self):
        """Catches broadcasting mismatched paths or admitting the zero state."""
        params = ComplexGBMParameters(0.08, 0.30, 0.40, 0.20)
        with self.assertRaisesRegex(ValueError, "same shape"):
            exact_path([0.0, 1.0], [0.0], 1.0 + 0.0j, params)
        with self.assertRaisesRegex(ValueError, "nonzero"):
            exact_path([0.0], [0.0], 0.0j, params)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            exact_step(1.0 + 0.0j, -0.1, 0.0, params)


class StructuralFormulaTests(unittest.TestCase):
    def setUp(self):
        self.params = ComplexGBMParameters(0.08, 0.30, 0.40, 0.20)

    def test_log_polar_covariance_is_the_expected_rank_one_outer_product(self):
        """Catches introducing a hidden second Brownian driver."""
        covariance = log_polar_covariance(self.params)
        expected = np.array([[0.09, 0.06], [0.06, 0.04]])

        np.testing.assert_allclose(covariance, expected, atol=2e-17)
        eigenvalues = np.linalg.eigvalsh(covariance)
        self.assertAlmostEqual(eigenvalues[0], 0.0, places=15)
        self.assertAlmostEqual(eigenvalues[1], 0.13, places=15)

    def test_exact_moments_use_gaussian_exponential_factors(self):
        """Catches omitting the half-variance term in analytic benchmarks."""
        r0 = 2.0
        z0 = 1.2 - 0.7j
        expected_radial_second = 4.0 * np.exp(0.25)
        expected_complex_second = z0**2 * np.exp(
            2.0 * (0.035 + 0.40j) + 2.0 * (0.30 + 0.20j) ** 2
        )
        expected_mixed = r0 * np.exp(
            0.035 + 0.40j + 0.5 * (0.30 + 0.20j) ** 2
        )

        self.assertAlmostEqual(
            radial_moment(r0, 1.0, 2.0, self.params),
            expected_radial_second,
        )
        self.assertAlmostEqual(
            complex_moment(z0, 1.0, 2, self.params),
            expected_complex_second,
        )
        self.assertAlmostEqual(
            mixed_log_polar_moment(r0, 1.0, 1.0, 1.0, self.params),
            expected_mixed,
        )

    def test_complex_brackets_keep_bilinear_and_hermitian_squares_distinct(self):
        """Catches replacing B squared with its absolute square."""
        z = 1.2 - 0.7j
        bilinear, hermitian = complex_bracket_rates(z, self.params)

        self.assertAlmostEqual(
            bilinear,
            (0.30 + 0.20j) ** 2 * z**2,
        )
        self.assertAlmostEqual(
            hermitian,
            (0.30**2 + 0.20**2) * abs(z) ** 2,
        )

    def test_two_driver_path_preserves_gbm_modulus_and_uses_independent_phase(self):
        """Catches using radial Brownian noise in the two-driver phase."""
        times = np.array([0.0, 0.5, 1.0])
        radial_brownian = np.array([0.0, 0.2, -0.1])
        angular_brownian = np.array([0.0, -0.4, 0.3])
        z0 = 2.0 * np.exp(0.3j)

        z = two_driver_path(
            times,
            radial_brownian,
            angular_brownian,
            z0,
            self.params,
        )
        expected_radius = 2.0 * np.exp(
            0.035 * times + 0.30 * radial_brownian
        )
        expected_phase = 0.3 + 0.40 * times + 0.20 * angular_brownian

        np.testing.assert_allclose(np.abs(z), expected_radius, rtol=2e-15)
        np.testing.assert_allclose(
            np.unwrap(np.angle(z)),
            expected_phase,
            rtol=2e-15,
            atol=2e-15,
        )


if __name__ == "__main__":
    unittest.main()
