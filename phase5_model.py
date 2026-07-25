"""Exact helpers for the Phase 5 one-phase Euler representations.

The module keeps three objects distinct:

* the original one-dimensional affine diffusion;
* its exact secant phase coordinate;
* the Cayley unit-circle transform, which is not the original affine state.

All stochastic transitions supplied here are deterministic transforms of a
standard-normal increment.  Numerical schemes in the Phase 5 notebook use
these functions as exact references.
"""

from dataclasses import dataclass
from typing import TypeAlias

import numpy as np
from numpy.typing import ArrayLike, NDArray


RealValue: TypeAlias = float | NDArray[np.float64]
ComplexValue: TypeAlias = complex | NDArray[np.complex128]


def _is_finite_complex(value: complex) -> bool:
    z = complex(value)
    return bool(np.isfinite(z.real) and np.isfinite(z.imag))


def _as_real(value: ArrayLike) -> NDArray[np.float64]:
    array = np.asarray(value, dtype=np.float64)
    if not np.all(np.isfinite(array)):
        raise ValueError("real inputs must be finite")
    return array


def _as_complex(value: ArrayLike) -> NDArray[np.complex128]:
    array = np.asarray(value, dtype=np.complex128)
    if not np.all(np.isfinite(array.real)) or not np.all(np.isfinite(array.imag)):
        raise ValueError("complex inputs must be finite")
    return array


def _positive_scale(c: float) -> float:
    value = float(c)
    if not np.isfinite(value) or value <= 0.0:
        raise ValueError("c must be finite and positive")
    return value


def _nonnegative_step(h: float) -> float:
    value = float(h)
    if not np.isfinite(value) or value < 0.0:
        raise ValueError("h must be finite and nonnegative")
    return value


def _positive_step(h: float) -> float:
    value = _nonnegative_step(h)
    if value == 0.0:
        raise ValueError("h must be positive")
    return value


def _validate_open_interval(
    theta: NDArray[np.float64],
    lower: float,
    upper: float,
) -> None:
    if np.any(theta <= lower) or np.any(theta >= upper):
        raise ValueError(f"phase must lie in the open interval ({lower}, {upper})")


@dataclass(frozen=True)
class AffinePhaseParameters:
    """Parameters of an eligible time-independent affine-line phase chart."""

    z0: complex
    a: complex
    b: complex
    tolerance: float = 1e-12

    def __post_init__(self) -> None:
        if not all(_is_finite_complex(value) for value in (self.z0, self.a, self.b)):
            raise ValueError("z0, a, and b must be finite")
        if complex(self.z0) == 0.0j:
            raise ValueError("z0 must be nonzero")
        if complex(self.b) == 0.0j:
            raise ValueError("b must be nonzero")
        if not np.isfinite(self.tolerance) or self.tolerance <= 0.0:
            raise ValueError("tolerance must be finite and positive")

        ratio = complex(self.a) / complex(self.b)
        ratio_scale = max(1.0, abs(ratio))
        if abs(ratio.imag) > self.tolerance * ratio_scale:
            raise ValueError("a and b must be real-collinear")

        normalized_diffusion = complex(self.b) / complex(self.z0)
        diffusion_scale = max(1.0, abs(normalized_diffusion))
        if (
            abs(normalized_diffusion.imag)
            <= self.tolerance * diffusion_scale
        ):
            raise ValueError("the affine support line must miss the origin")

    @property
    def c(self) -> complex:
        """Normalized complex diffusion direction b/z0."""
        return complex(self.b) / complex(self.z0)

    @property
    def drift_ratio(self) -> float:
        """The real scalar lambda in a=lambda*b."""
        return float((complex(self.a) / complex(self.b)).real)

    @property
    def rho(self) -> float:
        return float(abs(self.c))

    @property
    def phi(self) -> float:
        # __post_init__ rejects real b/z0, so this principal angle cannot be
        # 0 or +/-pi and every downstream division by sin(phi) is well-defined.
        return float(np.angle(self.c))

    @property
    def phase_interval(self) -> tuple[float, float]:
        phi = self.phi
        if np.sin(phi) > 0.0:
            return float(phi - np.pi), phi
        return phi, float(phi + np.pi)


def canonical_phase(y: ArrayLike, c: float) -> RealValue:
    """Return theta=atan(y/c) in the canonical open half-turn."""
    scale = _positive_scale(c)
    return np.asarray(np.arctan(_as_real(y) / scale), dtype=np.float64)


def canonical_inverse(theta: ArrayLike, c: float) -> RealValue:
    """Return y=c*tan(theta) from the canonical phase."""
    scale = _positive_scale(c)
    angle = _as_real(theta)
    _validate_open_interval(angle, -np.pi / 2.0, np.pi / 2.0)
    return np.asarray(scale * np.tan(angle), dtype=np.float64)


def canonical_radius(theta: ArrayLike) -> RealValue:
    """Return the positive canonical radius sec(theta)."""
    angle = _as_real(theta)
    _validate_open_interval(angle, -np.pi / 2.0, np.pi / 2.0)
    return np.asarray(1.0 / np.cos(angle), dtype=np.float64)


def canonical_embedding(theta: ArrayLike, z0: complex = 1.0 + 0.0j) -> ComplexValue:
    """Evaluate z0*sec(theta)*exp(i*theta)."""
    if not _is_finite_complex(z0) or complex(z0) == 0.0j:
        raise ValueError("z0 must be finite and nonzero")
    angle = _as_real(theta)
    radius = canonical_radius(angle)
    return np.asarray(
        complex(z0) * radius * np.exp(1j * angle),
        dtype=np.complex128,
    )


def canonical_phase_coefficients(
    theta: ArrayLike,
    mu: float,
    sigma: float,
    c: float,
) -> tuple[RealValue, RealValue]:
    """Return the Itô drift and diffusion of theta=atan(Y/c)."""
    scale = _positive_scale(c)
    angle = _as_real(theta)
    _validate_open_interval(angle, -np.pi / 2.0, np.pi / 2.0)
    mu_value, sigma_value = float(mu), float(sigma)
    if not np.isfinite(mu_value) or not np.isfinite(sigma_value):
        raise ValueError("mu and sigma must be finite")
    cosine = np.cos(angle)
    diffusion = sigma_value * cosine**2 / scale
    drift = (
        mu_value * cosine**2 / scale
        - sigma_value**2 * np.sin(angle) * cosine**3 / scale**2
    )
    return (
        np.asarray(drift, dtype=np.float64),
        np.asarray(diffusion, dtype=np.float64),
    )


def canonical_exact_phase_step(
    theta: ArrayLike,
    h: float,
    normal: ArrayLike,
    mu: float,
    sigma: float,
    c: float,
) -> RealValue:
    """Apply one exact transformed-Gaussian phase transition."""
    step = _nonnegative_step(h)
    scale = _positive_scale(c)
    angle = _as_real(theta)
    state = canonical_inverse(angle, scale)
    normal_value = _as_real(normal)
    mu_value, sigma_value = float(mu), float(sigma)
    if not np.isfinite(mu_value) or not np.isfinite(sigma_value):
        raise ValueError("mu and sigma must be finite")
    updated = state + mu_value * step + sigma_value * np.sqrt(step) * normal_value
    return canonical_phase(updated, scale)


def canonical_phase_density(
    v: ArrayLike,
    u: ArrayLike,
    h: float,
    mu: float,
    sigma: float,
    c: float,
) -> RealValue:
    """Evaluate the exact canonical phase transition density."""
    step = _positive_step(h)
    scale = _positive_scale(c)
    sigma_value = float(sigma)
    mu_value = float(mu)
    if not np.isfinite(mu_value) or not np.isfinite(sigma_value):
        raise ValueError("mu and sigma must be finite")
    if sigma_value == 0.0:
        raise ValueError("sigma must be nonzero for a transition density")
    destination = _as_real(v)
    source = _as_real(u)
    _validate_open_interval(destination, -np.pi / 2.0, np.pi / 2.0)
    _validate_open_interval(source, -np.pi / 2.0, np.pi / 2.0)
    residual = (
        scale * np.tan(destination)
        - scale * np.tan(source)
        - mu_value * step
    )
    jacobian = scale / np.cos(destination) ** 2
    density = (
        jacobian
        / (abs(sigma_value) * np.sqrt(2.0 * np.pi * step))
        * np.exp(-(residual**2) / (2.0 * sigma_value**2 * step))
    )
    return np.asarray(density, dtype=np.float64)


def affine_phase(x: ArrayLike, params: AffinePhaseParameters) -> RealValue:
    """Return the continuous argument of 1+(b/z0)*x."""
    scalar = _as_real(x)
    normalized = 1.0 + params.c * scalar
    return np.asarray(np.angle(normalized), dtype=np.float64)


def affine_radius(
    theta: ArrayLike,
    params: AffinePhaseParameters,
) -> RealValue:
    """Return sin(phi)/sin(phi-theta) on the admissible branch."""
    angle = _as_real(theta)
    lower, upper = params.phase_interval
    _validate_open_interval(angle, lower, upper)
    radius = np.sin(params.phi) / np.sin(params.phi - angle)
    return np.asarray(radius, dtype=np.float64)


def affine_scalar_from_phase(
    theta: ArrayLike,
    params: AffinePhaseParameters,
) -> RealValue:
    """Recover x from the general affine phase."""
    angle = _as_real(theta)
    lower, upper = params.phase_interval
    _validate_open_interval(angle, lower, upper)
    scalar = np.sin(angle) / (
        params.rho * np.sin(params.phi - angle)
    )
    return np.asarray(scalar, dtype=np.float64)


def affine_forward(
    theta: ArrayLike,
    params: AffinePhaseParameters,
) -> ComplexValue:
    """Evaluate z0*r(theta)*exp(i*theta) on the eligible affine line."""
    angle = _as_real(theta)
    radius = affine_radius(angle, params)
    return np.asarray(
        complex(params.z0) * radius * np.exp(1j * angle),
        dtype=np.complex128,
    )


def affine_phase_coefficients(
    theta: ArrayLike,
    params: AffinePhaseParameters,
) -> tuple[RealValue, RealValue]:
    """Return the general affine phase Itô drift and diffusion."""
    angle = _as_real(theta)
    lower, upper = params.phase_interval
    _validate_open_interval(angle, lower, upper)
    phi, rho = params.phi, params.rho
    diffusion = rho * np.sin(phi - angle) ** 2 / np.sin(phi)
    derivative = (
        -2.0
        * rho
        * np.sin(phi - angle)
        * np.cos(phi - angle)
        / np.sin(phi)
    )
    drift = (
        params.drift_ratio * diffusion
        + 0.5 * diffusion * derivative
    )
    return (
        np.asarray(drift, dtype=np.float64),
        np.asarray(diffusion, dtype=np.float64),
    )


def affine_exact_phase_step(
    theta: ArrayLike,
    h: float,
    normal: ArrayLike,
    params: AffinePhaseParameters,
) -> RealValue:
    """Apply one exact transition in a general eligible affine chart."""
    step = _nonnegative_step(h)
    scalar = affine_scalar_from_phase(theta, params)
    updated = (
        scalar
        + params.drift_ratio * step
        + np.sqrt(step) * _as_real(normal)
    )
    return affine_phase(updated, params)


def affine_transition_density(
    v: ArrayLike,
    u: ArrayLike,
    h: float,
    params: AffinePhaseParameters,
) -> RealValue:
    """Evaluate the exact general affine phase transition density."""
    step = _positive_step(h)
    destination = _as_real(v)
    source = _as_real(u)
    x_destination = affine_scalar_from_phase(destination, params)
    x_source = affine_scalar_from_phase(source, params)
    residual = (
        x_destination
        - x_source
        - params.drift_ratio * step
    )
    jacobian = abs(np.sin(params.phi)) / (
        params.rho * np.sin(params.phi - destination) ** 2
    )
    density = (
        jacobian
        / np.sqrt(2.0 * np.pi * step)
        * np.exp(-(residual**2) / (2.0 * step))
    )
    return np.asarray(density, dtype=np.float64)


def cayley_transform(y: ArrayLike, c: float) -> ComplexValue:
    """Map the real line losslessly to the unit circle minus -1."""
    scale = _positive_scale(c)
    q = _as_real(y) / scale
    return np.asarray((1.0 + 1j * q) / (1.0 - 1j * q), dtype=np.complex128)


def cayley_inverse(u: ArrayLike, c: float, tolerance: float = 1e-10) -> RealValue:
    """Invert the Cayley map on the unit circle excluding -1."""
    scale = _positive_scale(c)
    value = _as_complex(u)
    if np.any(np.abs(np.abs(value) - 1.0) > tolerance):
        raise ValueError("u must lie on the unit circle")
    if np.any(np.abs(value + 1.0) <= tolerance):
        raise ValueError("the Cayley point -1 represents infinity")
    inverse = scale * np.real(-1j * (value - 1.0) / (value + 1.0))
    return np.asarray(inverse, dtype=np.float64)


def cayley_phase(y: ArrayLike, c: float) -> RealValue:
    """Return the Cayley phase 2*atan(y/c) in (-pi, pi)."""
    scale = _positive_scale(c)
    return np.asarray(2.0 * np.arctan(_as_real(y) / scale), dtype=np.float64)


def cayley_phase_coefficients(
    theta: ArrayLike,
    mu: float,
    sigma: float,
    c: float,
) -> tuple[RealValue, RealValue]:
    """Return the Itô drift and diffusion of the Cayley phase."""
    scale = _positive_scale(c)
    angle = _as_real(theta)
    _validate_open_interval(angle, -np.pi, np.pi)
    mu_value, sigma_value = float(mu), float(sigma)
    if not np.isfinite(mu_value) or not np.isfinite(sigma_value):
        raise ValueError("mu and sigma must be finite")
    half = angle / 2.0
    cosine = np.cos(half)
    diffusion = 2.0 * sigma_value * cosine**2 / scale
    drift = (
        2.0 * mu_value * cosine**2 / scale
        - 2.0
        * sigma_value**2
        * np.sin(half)
        * cosine**3
        / scale**2
    )
    return (
        np.asarray(drift, dtype=np.float64),
        np.asarray(diffusion, dtype=np.float64),
    )


def cayley_complex_coefficients(
    u: ArrayLike,
    mu: float,
    sigma: float,
    c: float,
) -> tuple[ComplexValue, ComplexValue]:
    """Return the Itô drift and diffusion of the unit-circle process."""
    scale = _positive_scale(c)
    value = _as_complex(u)
    mu_value, sigma_value = float(mu), float(sigma)
    if not np.isfinite(mu_value) or not np.isfinite(sigma_value):
        raise ValueError("mu and sigma must be finite")
    drift = (
        1j * mu_value * (1.0 + value) ** 2 / (2.0 * scale)
        - sigma_value**2 * (1.0 + value) ** 3 / (4.0 * scale**2)
    )
    diffusion = 1j * sigma_value * (1.0 + value) ** 2 / (2.0 * scale)
    return (
        np.asarray(drift, dtype=np.complex128),
        np.asarray(diffusion, dtype=np.complex128),
    )


def cayley_exact_phase_step(
    theta: ArrayLike,
    h: float,
    normal: ArrayLike,
    mu: float,
    sigma: float,
    c: float,
) -> RealValue:
    """Apply one exact transformed-Gaussian Cayley phase transition."""
    step = _nonnegative_step(h)
    scale = _positive_scale(c)
    angle = _as_real(theta)
    _validate_open_interval(angle, -np.pi, np.pi)
    mu_value, sigma_value = float(mu), float(sigma)
    if not np.isfinite(mu_value) or not np.isfinite(sigma_value):
        raise ValueError("mu and sigma must be finite")
    state = scale * np.tan(angle / 2.0)
    updated = state + mu_value * step + sigma_value * np.sqrt(step) * _as_real(normal)
    return cayley_phase(updated, scale)


def transported_add(theta1: ArrayLike, theta2: ArrayLike) -> RealValue:
    """Transport real addition through theta=atan(x/c)."""
    first, second = _as_real(theta1), _as_real(theta2)
    _validate_open_interval(first, -np.pi / 2.0, np.pi / 2.0)
    _validate_open_interval(second, -np.pi / 2.0, np.pi / 2.0)
    return np.asarray(
        np.arctan(np.tan(first) + np.tan(second)),
        dtype=np.float64,
    )


def cayley_transported_add(theta1: ArrayLike, theta2: ArrayLike) -> RealValue:
    """Transport real addition through Theta=2*atan(x/c)."""
    first, second = _as_real(theta1), _as_real(theta2)
    _validate_open_interval(first, -np.pi, np.pi)
    _validate_open_interval(second, -np.pi, np.pi)
    return np.asarray(
        2.0
        * np.arctan(
            np.tan(first / 2.0) + np.tan(second / 2.0)
        ),
        dtype=np.float64,
    )


def spiral_eligible(
    kappa: complex,
    b: complex,
    tolerance: float = 1e-12,
) -> bool:
    """Return whether log drift and diffusion admit a lossless spiral phase."""
    if not _is_finite_complex(kappa) or not _is_finite_complex(b):
        return False
    diffusion = complex(b)
    if diffusion == 0.0j:
        return False
    if abs(diffusion.imag) <= tolerance * max(1.0, abs(diffusion)):
        return False
    ratio = complex(kappa) / diffusion
    return bool(abs(ratio.imag) <= tolerance * max(1.0, abs(ratio)))


def spiral_phase(
    times: ArrayLike,
    brownian: ArrayLike,
    kappa: complex,
    b: complex,
) -> RealValue:
    """Return the unwrapped phase of a compatible log-affine process."""
    if not spiral_eligible(kappa, b):
        raise ValueError("kappa and b must define a compatible angular spiral")
    t, w = _as_real(times), _as_real(brownian)
    gamma = float((complex(kappa) / complex(b)).real)
    beta = float(complex(b).imag)
    return np.asarray(beta * (gamma * t + w), dtype=np.float64)


def spiral_radius(theta: ArrayLike, b: complex) -> RealValue:
    """Return exp((Re b / Im b)*theta) for a logarithmic spiral."""
    if not _is_finite_complex(b):
        raise ValueError("b must be finite")
    diffusion = complex(b)
    if diffusion.imag == 0.0:
        raise ValueError("b must have nonzero imaginary part")
    angle = _as_real(theta)
    return np.asarray(
        np.exp((diffusion.real / diffusion.imag) * angle),
        dtype=np.float64,
    )


def spiral_state(
    z0: complex,
    theta: ArrayLike,
    b: complex,
) -> ComplexValue:
    """Evaluate the logarithmic-spiral one-phase state."""
    if not _is_finite_complex(z0) or complex(z0) == 0.0j:
        raise ValueError("z0 must be finite and nonzero")
    angle = _as_real(theta)
    radius = spiral_radius(angle, b)
    return np.asarray(
        complex(z0) * radius * np.exp(1j * angle),
        dtype=np.complex128,
    )


def additive_required_phase_drift(
    phase_diffusion: ArrayLike,
    phase_diffusion_derivative: ArrayLike,
    drift_ratio: complex,
    tolerance: float = 1e-12,
) -> RealValue:
    """Return m=lambda*s+0.5*s*s' from additive rigidity."""
    ratio = complex(drift_ratio)
    if not _is_finite_complex(ratio):
        raise ValueError("drift ratio must be finite")
    if abs(ratio.imag) > tolerance * max(1.0, abs(ratio)):
        raise ValueError("additive drift ratio must be real")
    s = _as_real(phase_diffusion)
    derivative = _as_real(phase_diffusion_derivative)
    return np.asarray(
        ratio.real * s + 0.5 * s * derivative,
        dtype=np.float64,
    )


def induced_ito_coefficients(
    z0: complex,
    f: ArrayLike,
    f_prime: ArrayLike,
    f_second: ArrayLike,
    phase_drift: ArrayLike,
    phase_diffusion: ArrayLike,
) -> tuple[ComplexValue, ComplexValue]:
    """Return the complex drift/diffusion induced by Z=z0*F(theta)."""
    if not _is_finite_complex(z0) or complex(z0) == 0.0j:
        raise ValueError("z0 must be finite and nonzero")
    # Reading f validates the represented state and broadcasting inputs even
    # though only its derivatives enter Itô's differential.
    _as_complex(f)
    first = _as_complex(f_prime)
    second = _as_complex(f_second)
    drift_theta = _as_real(phase_drift)
    diffusion_theta = _as_real(phase_diffusion)
    drift = complex(z0) * (
        first * drift_theta + 0.5 * second * diffusion_theta**2
    )
    diffusion = complex(z0) * first * diffusion_theta
    return (
        np.asarray(drift, dtype=np.complex128),
        np.asarray(diffusion, dtype=np.complex128),
    )


def multiplicative_phase_parameters(
    a: complex,
    b: complex,
    tolerance: float = 1e-12,
) -> tuple[float, float, float]:
    """Return spiral slope, phase diffusion, and phase drift for dZ/Z."""
    if not _is_finite_complex(a) or not _is_finite_complex(b):
        raise ValueError("a and b must be finite")
    diffusion = complex(b)
    if diffusion.imag == 0.0:
        raise ValueError("b must have nonzero imaginary part")
    log_drift = complex(a) - 0.5 * diffusion**2
    gamma = log_drift / diffusion
    if abs(gamma.imag) > tolerance * max(1.0, abs(gamma)):
        raise ValueError("log drift and diffusion are not compatible")
    k = diffusion.real / diffusion.imag
    beta = diffusion.imag
    phase_drift = gamma.real * beta
    return float(k), float(beta), float(phase_drift)


def _moving_line_geometry(
    t: float,
    z0: complex,
    a: complex,
    b: complex,
    tolerance: float = 1e-12,
) -> tuple[complex, complex, float]:
    if not all(_is_finite_complex(value) for value in (z0, a, b)):
        raise ValueError("z0, a, and b must be finite")
    if complex(z0) == 0.0j:
        raise ValueError("z0 must be nonzero")
    if complex(b) == 0.0j:
        raise ValueError("b must be nonzero")
    time = float(t)
    if not np.isfinite(time):
        raise ValueError("t must be finite")
    alpha = complex(a) / complex(z0)
    c = complex(b) / complex(z0)
    p = 1.0 + alpha * time
    signed_offset = float(np.imag(p * np.conjugate(c)))
    scale = max(1.0, abs(p) * abs(c))
    if abs(signed_offset) <= tolerance * scale:
        raise ValueError("the moving support line passes through the origin")
    return p, c, signed_offset


def moving_line_phase(
    t: float,
    w: ArrayLike,
    z0: complex,
    a: complex,
    b: complex,
) -> RealValue:
    """Return a continuous argument lift on a nonradial moving support line."""
    p, c, _ = _moving_line_geometry(t, z0, a, b)
    scalar = _as_real(w)
    normalized = p + c * scalar
    # normalized/p starts at 1 and traces a line that cannot cross the
    # negative real axis, so its principal argument is the continuous
    # increment from the anchor arg(p).
    phase = np.angle(p) + np.angle(normalized / p)
    return np.asarray(phase, dtype=np.float64)


def moving_line_radius(
    t: float,
    theta: ArrayLike,
    z0: complex,
    a: complex,
    b: complex,
) -> RealValue:
    """Return the explicit time-dependent polar radius of a support line."""
    _, c, signed_offset = _moving_line_geometry(t, z0, a, b)
    angle = _as_real(theta)
    denominator = np.imag(np.exp(1j * angle) * np.conjugate(c))
    if np.any(np.isclose(denominator, 0.0, rtol=0.0, atol=1e-14)):
        raise ValueError("phase is at a moving-line chart endpoint")
    radius = signed_offset / denominator
    if np.any(radius <= 0.0):
        raise ValueError("phase lies outside the positive-radius line chart")
    return np.asarray(radius, dtype=np.float64)


def moving_line_state(
    t: float,
    theta: ArrayLike,
    z0: complex,
    a: complex,
    b: complex,
) -> ComplexValue:
    """Evaluate z0*R(t,theta)*exp(i*theta)."""
    angle = _as_real(theta)
    radius = moving_line_radius(t, angle, z0, a, b)
    return np.asarray(
        complex(z0) * radius * np.exp(1j * angle),
        dtype=np.complex128,
    )


def phase_noise_covariance(tangent: ArrayLike) -> NDArray[np.float64]:
    """Return the rank-one covariance outer product of one scalar driver."""
    vector = _as_real(tangent)
    if vector.ndim != 1 or vector.size == 0:
        raise ValueError("tangent must be a nonempty one-dimensional vector")
    return np.asarray(np.outer(vector, vector), dtype=np.float64)


__all__ = [
    "AffinePhaseParameters",
    "additive_required_phase_drift",
    "affine_exact_phase_step",
    "affine_forward",
    "affine_phase",
    "affine_phase_coefficients",
    "affine_radius",
    "affine_scalar_from_phase",
    "affine_transition_density",
    "canonical_embedding",
    "canonical_exact_phase_step",
    "canonical_inverse",
    "canonical_phase",
    "canonical_phase_coefficients",
    "canonical_phase_density",
    "canonical_radius",
    "cayley_complex_coefficients",
    "cayley_exact_phase_step",
    "cayley_inverse",
    "cayley_phase",
    "cayley_phase_coefficients",
    "cayley_transform",
    "cayley_transported_add",
    "induced_ito_coefficients",
    "moving_line_phase",
    "moving_line_radius",
    "moving_line_state",
    "multiplicative_phase_parameters",
    "phase_noise_covariance",
    "spiral_eligible",
    "spiral_phase",
    "spiral_radius",
    "spiral_state",
    "transported_add",
]
