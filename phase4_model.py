"""Numerical helpers for the Phase 4 coordinate-free complex GBM."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass(frozen=True)
class ComplexGBMParameters:
    """Constant coefficients of the modulus-preserving complex GBM."""

    mu: float
    sigma: float
    omega: float
    beta: float

    def __post_init__(self) -> None:
        coefficients = (self.mu, self.sigma, self.omega, self.beta)
        if not all(np.isfinite(value) for value in coefficients):
            raise ValueError("all model parameters must be finite")

    @property
    def log_drift(self) -> complex:
        return complex(self.mu - 0.5 * self.sigma**2, self.omega)

    @property
    def diffusion(self) -> complex:
        return complex(self.sigma, self.beta)

    @property
    def sde_drift(self) -> complex:
        return complex(
            self.mu - 0.5 * self.beta**2,
            self.omega + self.sigma * self.beta,
        )


def exact_path(
    times: ArrayLike,
    brownian: ArrayLike,
    z0: complex,
    params: ComplexGBMParameters,
) -> NDArray[np.complex128]:
    """Evaluate the exact one-driver complex GBM on a Brownian path."""
    t = np.asarray(times, dtype=float)
    w = np.asarray(brownian, dtype=float)
    if t.shape != w.shape:
        raise ValueError("times and brownian must have the same shape")
    if complex(z0) == 0.0j:
        raise ValueError("z0 must be nonzero")
    return np.asarray(
        complex(z0) * np.exp(params.log_drift * t + params.diffusion * w),
        dtype=np.complex128,
    )


def gbm_radius(
    times: ArrayLike,
    brownian: ArrayLike,
    r0: float,
    params: ComplexGBMParameters,
) -> NDArray[np.float64]:
    """Evaluate the exact GBM modulus on a Brownian path."""
    t = np.asarray(times, dtype=float)
    w = np.asarray(brownian, dtype=float)
    return np.asarray(
        float(r0)
        * np.exp(
            (params.mu - 0.5 * params.sigma**2) * t
            + params.sigma * w
        ),
        dtype=np.float64,
    )


def unwrapped_phase(
    times: ArrayLike,
    brownian: ArrayLike,
    theta0: float,
    params: ComplexGBMParameters,
) -> NDArray[np.float64]:
    """Evaluate the continuous phase lift on a Brownian path."""
    t = np.asarray(times, dtype=float)
    w = np.asarray(brownian, dtype=float)
    return np.asarray(
        float(theta0) + params.omega * t + params.beta * w,
        dtype=np.float64,
    )


def exact_step(
    z: complex,
    h: float,
    d_w: float,
    params: ComplexGBMParameters,
) -> complex:
    """Apply one exact multiplicative transition using a Brownian increment."""
    if float(h) < 0.0:
        raise ValueError("h must be nonnegative")
    return complex(
        complex(z)
        * np.exp(params.log_drift * float(h) + params.diffusion * float(d_w))
    )


def euler_maruyama_path(
    z0: complex,
    h: float,
    brownian_increments: ArrayLike,
    params: ComplexGBMParameters,
) -> NDArray[np.complex128]:
    """Approximate one path of the complex Itô SDE by Euler--Maruyama."""
    d_w = np.asarray(brownian_increments, dtype=float)
    path = np.empty(d_w.size + 1, dtype=np.complex128)
    path[0] = complex(z0)
    factor_drift = params.sde_drift * float(h)
    for index, increment in enumerate(d_w):
        path[index + 1] = path[index] * (
            1.0 + factor_drift + params.diffusion * increment
        )
    return path


def log_polar_covariance(
    params: ComplexGBMParameters,
) -> NDArray[np.float64]:
    """Return the instantaneous one-driver covariance of log-radius and phase."""
    noise = np.array([params.sigma, params.beta], dtype=np.float64)
    return np.outer(noise, noise)


def radial_moment(
    r0: float,
    t: float,
    order: float,
    params: ComplexGBMParameters,
) -> float:
    """Return the analytic radial moment E[R_t**order]."""
    exponent = (
        order * params.mu
        + 0.5 * order * (order - 1.0) * params.sigma**2
    ) * float(t)
    return float(float(r0) ** order * np.exp(exponent))


def complex_moment(
    z0: complex,
    t: float,
    order: int,
    params: ComplexGBMParameters,
) -> complex:
    """Return the analytic integer complex moment E[Z_t**order]."""
    exponent = (
        order * params.log_drift
        + 0.5 * order**2 * params.diffusion**2
    ) * float(t)
    return complex(complex(z0) ** order * np.exp(exponent))


def mixed_log_polar_moment(
    r0: float,
    t: float,
    radial_order: float,
    phase_frequency: float,
    params: ComplexGBMParameters,
) -> complex:
    """Return E[R_t**p exp(i q (Theta_t-Theta_0))]."""
    gaussian_coefficient = (
        radial_order * params.sigma
        + 1j * phase_frequency * params.beta
    )
    exponent = (
        radial_order * (params.mu - 0.5 * params.sigma**2)
        + 1j * phase_frequency * params.omega
        + 0.5 * gaussian_coefficient**2
    ) * float(t)
    return complex(float(r0) ** radial_order * np.exp(exponent))


def complex_bracket_rates(
    z: complex,
    params: ComplexGBMParameters,
) -> tuple[complex, float]:
    """Return bilinear and Hermitian quadratic-variation rates at z."""
    bilinear = params.diffusion**2 * complex(z) ** 2
    hermitian = abs(params.diffusion) ** 2 * abs(complex(z)) ** 2
    return complex(bilinear), float(hermitian)


def two_driver_path(
    times: ArrayLike,
    radial_brownian: ArrayLike,
    angular_brownian: ArrayLike,
    z0: complex,
    params: ComplexGBMParameters,
) -> NDArray[np.complex128]:
    """Evaluate the independent radial/angular two-driver comparator."""
    t = np.asarray(times, dtype=float)
    w_r = np.asarray(radial_brownian, dtype=float)
    w_theta = np.asarray(angular_brownian, dtype=float)
    exponent = (
        params.log_drift * t
        + params.sigma * w_r
        + 1j * params.beta * w_theta
    )
    return np.asarray(complex(z0) * np.exp(exponent), dtype=np.complex128)
