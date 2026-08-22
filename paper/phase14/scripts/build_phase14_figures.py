"""Build deterministic figures and evidence tables for the Phase 14 paper.

Exact identities, deterministic quadrature, and Monte Carlo checks remain
separate. Numerical experiments validate derivations; they never replace them.
"""

from __future__ import annotations

import csv
import json
import math
import platform
import sys
from pathlib import Path
from typing import Any, Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
import scipy
from scipy.optimize import brentq
from scipy.special import ndtr

SEED: int = 20260822
HERE = Path(__file__).resolve().parent
PAPER_ROOT = HERE.parent
REPO_ROOT = PAPER_ROOT.parents[1]
FIGURE_ROOT = PAPER_ROOT / "figures"
RASTER_ROOT = FIGURE_ROOT / "raster"
VECTOR_ROOT = FIGURE_ROOT / "vector"
TABLE_ROOT = PAPER_ROOT / "tables"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

NAVY = "#153B55"
TEAL = "#0F6573"
RUST = "#A24D2F"
GOLD = "#C58B2A"
SLATE = "#657985"
PALE_TEAL = "#EAF4F5"
PALE_RUST = "#F8EEE9"
PALE_BLUE = "#EBF1F5"
INK = "#18232D"
PHI0 = 1.0 / math.sqrt(2.0 * math.pi)


def _ensure_directories() -> None:
    for path in (RASTER_ROOT, VECTOR_ROOT, TABLE_ROOT):
        path.mkdir(parents=True, exist_ok=True)


def _save_figure(fig: plt.Figure, basename: str) -> None:
    """Save deterministic raster and vector companions."""

    fig.savefig(
        RASTER_ROOT / f"{basename}.png",
        dpi=300,
        bbox_inches="tight",
        facecolor="white",
        metadata={"Software": "Phase 14 deterministic figure builder"},
    )
    fig.savefig(
        VECTOR_ROOT / f"{basename}.pdf",
        bbox_inches="tight",
        facecolor="white",
        metadata={
            "Creator": "Phase 14 deterministic figure builder",
        },
    )
    plt.close(fig)


def _float_text(value: Any) -> Any:
    if isinstance(value, (float, np.floating)):
        return f"{float(value):.12g}"
    if isinstance(value, (int, np.integer)):
        return int(value)
    return value


def _write_csv(name: str, rows: Iterable[dict[str, Any]], fields: list[str]) -> None:
    with (TABLE_ROOT / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _float_text(row.get(key, "")) for key in fields})


def _write_json(name: str, payload: dict[str, Any]) -> None:
    def normalize(value: Any) -> Any:
        if isinstance(value, dict):
            return {str(key): normalize(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [normalize(item) for item in value]
        if isinstance(value, np.ndarray):
            return [normalize(item) for item in value.tolist()]
        if isinstance(value, (float, np.floating)):
            return float(f"{float(value):.10g}")
        if isinstance(value, (int, np.integer)):
            return int(value)
        return value

    with (TABLE_ROOT / name).open("w", encoding="utf-8") as handle:
        json.dump(normalize(payload), handle, indent=2, sort_keys=True)
        handle.write("\n")


def bachelier_call(total_std: float, signed_moneyness: float) -> float:
    """Undiscounted centered Bachelier call in total-standard-deviation units."""

    if not math.isfinite(total_std) or total_std <= 0.0:
        raise ValueError("total_std must be finite and strictly positive")
    if not math.isfinite(signed_moneyness):
        raise ValueError("signed_moneyness must be finite")
    d = signed_moneyness / total_std
    return total_std * PHI0 * math.exp(-0.5 * d * d) - signed_moneyness * float(
        ndtr(-d)
    )


def implied_total_std(price: float, signed_moneyness: float) -> float:
    """Invert a Bachelier call price to total implied standard deviation."""

    intrinsic = max(-signed_moneyness, 0.0)
    if not math.isfinite(price) or price <= intrinsic:
        raise ValueError("price must be finite and strictly above intrinsic value")
    high = max(1.0, abs(signed_moneyness), price * math.sqrt(2.0 * math.pi))
    objective = lambda scale: bachelier_call(scale, signed_moneyness) - price
    while objective(high) < 0.0:
        high *= 2.0
        if high > 1e12:
            raise RuntimeError("failed to bracket implied standard deviation")
    return float(brentq(objective, 1e-12, high, xtol=1e-13, rtol=1e-13))


def centered_mixture_identities(
    scales: np.ndarray, weights: np.ndarray
) -> dict[str, float]:
    """Exact ATM level and curvature for a finite centered Gaussian mixture."""

    scales_arr = np.asarray(scales, dtype=float)
    weights_arr = np.asarray(weights, dtype=float)
    if scales_arr.ndim != 1 or weights_arr.shape != scales_arr.shape:
        raise ValueError("scales and weights must be aligned vectors")
    if np.any(scales_arr <= 0.0) or np.any(weights_arr < 0.0):
        raise ValueError("scales must be positive and weights nonnegative")
    mass = float(np.sum(weights_arr))
    if mass <= 0.0:
        raise ValueError("weights must have positive mass")
    weights_arr = weights_arr / mass
    e_scale = float(np.dot(weights_arr, scales_arr))
    e_inverse = float(np.dot(weights_arr, 1.0 / scales_arr))
    e_square = float(np.dot(weights_arr, scales_arr**2))
    variance = e_square - e_scale**2
    return {
        "e_scale": e_scale,
        "e_inverse_scale": e_inverse,
        "variance_scale": variance,
        "atm_implied_std": e_scale,
        "atm_implied_std_second": e_inverse - 1.0 / e_scale,
        "atm_implied_variance_second": 2.0 * (e_scale * e_inverse - 1.0),
    }


def phase8_clock_density() -> tuple[np.ndarray, np.ndarray]:
    """Deterministic Phase 8 clock density on its bounded support."""

    import phase6_fk as p6f

    grid, density = p6f.clock_density_grid(
        maturity=1.0,
        x0=0.0,
        drift=0.3,
        volatility=0.8,
        scale=1.0,
        n_modes=160,
        n_points=2001,
        n_grid=1600,
        margin=8.0,
    )
    mass = float(np.trapezoid(density, grid))
    if not math.isfinite(mass) or abs(mass - 1.0) > 1e-8:
        raise AssertionError(f"clock density mass is {mass}, expected 1")
    return np.asarray(grid), np.asarray(density) / mass


def _phase8_wedge_evidence(
    grid: np.ndarray, density: np.ndarray
) -> tuple[list[dict[str, float | str]], dict[str, float]]:
    import phase6_joint as p6j

    beta = 1.5**2 + 2.5**2
    mean_a, variance_a = p6j.occupation_moments(
        1.0,
        x0=0.0,
        drift=0.3,
        volatility=0.8,
        scale=1.0,
        gh_order=64,
        gl_order=64,
    )
    density_mean = float(np.trapezoid(grid * density, grid))
    density_variance = float(
        np.trapezoid((grid - density_mean) ** 2 * density, grid)
    )
    mean_error = density_mean - mean_a
    variance_error = density_variance - variance_a
    if abs(mean_error) >= 2e-6:
        raise AssertionError(
            f"clock density mean error {mean_error} exceeds convergence gate"
        )
    if abs(variance_error) >= 2e-6:
        raise AssertionError(
            f"clock density variance error {variance_error} exceeds convergence gate"
        )
    rows: list[dict[str, float | str]] = []
    summary: dict[str, float] = {
        "clock_mean": mean_a,
        "clock_variance": variance_a,
        "density_clock_mean": density_mean,
        "density_clock_variance": density_variance,
        "density_mean_error": mean_error,
        "density_variance_error": variance_error,
        "density_mass": float(np.trapezoid(density, grid)),
    }
    for label, alpha in (("spread", -7.5), ("basket", 7.5)):
        variances = beta + alpha * grid
        if np.min(variances) <= 0.0:
            raise AssertionError("reference total variance must remain positive")
        scales = np.sqrt(variances)
        e_scale = float(np.trapezoid(scales * density, grid))
        e_inverse = float(np.trapezoid(density / scales, grid))
        formula_rho = (e_scale**2 - beta) / alpha
        inverted_scale = implied_total_std(PHI0 * e_scale, 0.0)
        inverted_rho = (inverted_scale**2 - beta) / alpha
        curvature = 2.0 * (e_scale * e_inverse - 1.0) / alpha
        correction = formula_rho - mean_a
        rows.append(
            {
                "case": label,
                "alpha": alpha,
                "clock_mean": mean_a,
                "e_sqrt_variance": e_scale,
                "e_inverse_sqrt_variance": e_inverse,
                "formula_atm_correlation": formula_rho,
                "inverted_atm_correlation": inverted_rho,
                "jensen_correction": correction,
                "local_correlation_curvature": curvature,
            }
        )
        summary[f"{label}_formula_atm"] = formula_rho
        summary[f"{label}_inverted_atm"] = inverted_rho
        summary[f"{label}_curvature"] = curvature
        summary[f"{label}_jensen_correction"] = correction
    return rows, summary


def _simulate_leverage_cf() -> tuple[list[dict[str, float]], dict[str, float]]:
    """Direct, conditional, and Ito-gauge characteristic-function check."""

    maturity = 0.8
    n_steps = 512
    n_paths = 100_000
    batch = 10_000
    x0 = 0.2
    drift = -0.1
    factor_vol = 0.7
    scale = 0.8
    p_load = 0.9
    q_load = -0.6
    leverage = np.array([0.35, -0.25])
    residual_cov = np.eye(2) - np.outer(leverage, leverage)
    residual_root = np.linalg.cholesky(residual_cov)
    u_grid = np.linspace(0.0, 2.8, 15)
    dt = maturity / n_steps
    root_dt = math.sqrt(dt)
    rng = np.random.default_rng(SEED)

    z_all = np.empty(n_paths)
    mean_all = np.empty(n_paths)
    variance_all = np.empty(n_paths)
    gauge_mean_all = np.empty(n_paths)

    def primitive(x: np.ndarray) -> np.ndarray:
        return (
            leverage[0] * p_load * x
            + q_load * leverage[0] * np.sqrt(x * x + scale * scale)
            + q_load * leverage[1] * scale * np.arcsinh(x / scale)
        ) / factor_vol

    for offset in range(0, n_paths, batch):
        count = min(batch, n_paths - offset)
        x = np.full(count, x0)
        z = np.zeros(count)
        conditional_mean = np.zeros(count)
        conditional_variance = np.zeros(count)
        drift_integral = np.zeros(count)
        for _ in range(n_steps):
            radius = np.sqrt(x * x + scale * scale)
            bounded = x / radius
            complement = scale / radius
            g1 = p_load + q_load * bounded
            g2 = q_load * complement
            common = leverage[0] * g1 + leverage[1] * g2
            residual_variance = g1 * g1 + g2 * g2 - common * common
            common_prime = (
                q_load
                * scale
                * (leverage[0] * scale - leverage[1] * x)
                / radius**3
            )
            gauge_drift = (
                drift * common / factor_vol
                + 0.5 * factor_vol * common_prime
            )
            d_w0 = root_dt * rng.standard_normal(count)
            d_u = root_dt * rng.standard_normal((2, count))
            d_assets = leverage[:, None] * d_w0 + residual_root @ d_u
            z += g1 * d_assets[0] + g2 * d_assets[1]
            conditional_mean += common * d_w0
            conditional_variance += residual_variance * dt
            drift_integral += gauge_drift * dt
            x += drift * dt + factor_vol * d_w0
        gauge_mean = primitive(x) - primitive(np.array(x0)) - drift_integral
        selection = slice(offset, offset + count)
        z_all[selection] = z
        mean_all[selection] = conditional_mean
        variance_all[selection] = conditional_variance
        gauge_mean_all[selection] = gauge_mean

    rows: list[dict[str, float]] = []
    max_gap = 0.0
    max_gap_se = 0.0
    max_gauge_gap = 0.0
    for frequency in u_grid:
        direct_values = np.exp(1j * frequency * z_all)
        conditional_values = np.exp(
            1j * frequency * mean_all
            - 0.5 * frequency * frequency * variance_all
        )
        gauge_values = np.exp(
            1j * frequency * gauge_mean_all
            - 0.5 * frequency * frequency * variance_all
        )
        direct = complex(np.mean(direct_values))
        conditional = complex(np.mean(conditional_values))
        gauge = complex(np.mean(gauge_values))
        differences = direct_values - conditional_values
        gap_se = math.sqrt(
            float(np.var(differences.real, ddof=1))
            + float(np.var(differences.imag, ddof=1))
        ) / math.sqrt(n_paths)
        direct_real_se = float(np.std(direct_values.real, ddof=1)) / math.sqrt(
            n_paths
        )
        direct_imag_se = float(np.std(direct_values.imag, ddof=1)) / math.sqrt(
            n_paths
        )
        gap = abs(direct - conditional)
        gauge_gap = abs(conditional - gauge)
        max_gap = max(max_gap, gap)
        max_gap_se = max(max_gap_se, gap_se)
        max_gauge_gap = max(max_gauge_gap, gauge_gap)
        rows.append(
            {
                "u": float(frequency),
                "direct_real": direct.real,
                "direct_imag": direct.imag,
                "direct_real_se": direct_real_se,
                "direct_imag_se": direct_imag_se,
                "conditional_real": conditional.real,
                "conditional_imag": conditional.imag,
                "gauge_real": gauge.real,
                "gauge_imag": gauge.imag,
                "direct_conditional_gap": gap,
                "gap_standard_error": gap_se,
                "conditional_gauge_gap": gauge_gap,
            }
        )
    summary = {
        "direct_conditional_cf_max_gap": max_gap,
        "direct_mc_se_max": max_gap_se,
        "conditional_gauge_cf_max_gap": max_gauge_gap,
        "ito_gauge_rms": float(
            np.sqrt(np.mean((mean_all - gauge_mean_all) ** 2))
        ),
        "residual_covariance_min_eigenvalue": float(
            np.linalg.eigvalsh(residual_cov).min()
        ),
        "n_paths": n_paths,
        "n_steps": n_steps,
    }
    return rows, summary


def leveraged_characteristic_check() -> dict[str, float]:
    """Return the fixed-seed leveraged transform validation summary."""

    _, summary = _simulate_leverage_cf()
    return summary


def phasegram_finite_moment(
    m: int, time: float, theta0: np.ndarray, sigmas: np.ndarray
) -> float:
    """Exact integer moment of the Phase-Gram determinant."""

    if m < 1 or int(m) != m:
        raise ValueError("m must be a positive integer")
    if time < 0.0:
        raise ValueError("time must be nonnegative")
    theta = np.asarray(theta0, dtype=float)
    vols = np.asarray(sigmas, dtype=float)
    if theta.ndim != 1 or vols.shape != theta.shape or np.any(vols < 0.0):
        raise ValueError("theta0 and nonnegative sigmas must be aligned vectors")
    factors = np.full(theta.shape, math.comb(2 * m, m) / 4.0**m)
    for harmonic in range(1, m + 1):
        factors += (
            2.0
            / 4.0**m
            * (-1) ** harmonic
            * math.comb(2 * m, m - harmonic)
            * np.exp(-2.0 * harmonic**2 * vols**2 * time)
            * np.cos(2.0 * harmonic * theta)
        )
    return float(np.prod(factors))


def phasegram_stationary_logdet(
    n_assets: int, n_paths: int, rng: np.random.Generator
) -> np.ndarray:
    """Sample stationary Phase-Gram log determinants."""

    if n_assets < 2 or n_paths < 1:
        raise ValueError("need at least two assets and one path")
    dimension = n_assets * (n_assets - 1) // 2
    angles = rng.uniform(0.0, 2.0 * math.pi, size=(n_paths, dimension))
    return np.sum(np.log(np.sin(angles) ** 2), axis=1)


def nonautonomous_linear_transform(time: float, lam: float) -> dict[str, float]:
    """True and misordered transforms for mu(t)=t and sigma(t)^2=1+t."""

    if time < 0.0 or not math.isfinite(lam):
        raise ValueError("time must be nonnegative and lam finite")
    x0 = 0.2
    true_mean = x0 * time + time**3 / 6.0
    misordered_mean = x0 * time + time**3 / 3.0
    true_variance = time**3 / 3.0 + time**4 / 12.0
    misordered_variance = time**3 / 3.0 + time**4 / 4.0
    true_transform = math.exp(
        lam * true_mean + 0.5 * lam * lam * true_variance
    )
    misordered_transform = math.exp(
        lam * misordered_mean + 0.5 * lam * lam * misordered_variance
    )
    return {
        "time": time,
        "lambda": lam,
        "true_mean": true_mean,
        "misordered_mean": misordered_mean,
        "true_variance": true_variance,
        "misordered_variance": misordered_variance,
        "true_transform": true_transform,
        "misordered_transform": misordered_transform,
        "absolute_gap": abs(true_transform - misordered_transform),
        "ratio": misordered_transform / true_transform,
    }


def _figure_contribution_map() -> None:
    fig, ax = plt.subplots(figsize=(11.0, 6.4))
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.axis("off")

    def box(
        x: float,
        y: float,
        width: float,
        height: float,
        text: str,
        face: str,
        edge: str,
        size: float = 10.0,
    ) -> None:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0.012,rounding_size=0.012",
                linewidth=1.3,
                edgecolor=edge,
                facecolor=face,
            )
        )
        ax.text(
            x + width / 2.0,
            y + height / 2.0,
            text,
            ha="center",
            va="center",
            fontsize=size,
            color=INK,
            linespacing=1.25,
        )

    inputs = [
        (0.04, 0.75, "Phases 6–8\nclock reduction and smiles"),
        (0.04, 0.51, "Phase 9\nidentifiability"),
        (0.04, 0.27, "Phase 10\nGaussian-angle Gram maps"),
        (0.04, 0.03, "Phases 7 & 11\nnonautonomy and jumps"),
    ]
    majors = [
        (0.40, 0.68, "Exact ATM level\nand curvature identities"),
        (0.40, 0.42, "Leverage-preserving\n1-D transform closure"),
        (0.40, 0.16, "Phase-Gram stationarity,\ndeterminants, and boundary times"),
    ]
    support = [
        (0.78, 0.72, "Correct scale orbit"),
        (0.78, 0.52, "Operator-order correction"),
        (0.78, 0.32, "Endpoint–clock density"),
        (0.78, 0.12, "One-sided Lévy barriers"),
    ]
    for x, y, text in inputs:
        box(x, y, 0.24, 0.16, text, PALE_BLUE, NAVY, 9.3)
    for x, y, text in majors:
        box(x, y, 0.28, 0.18, text, PALE_TEAL, TEAL, 10.0)
    for x, y, text in support:
        box(x, y, 0.18, 0.13, text, PALE_RUST, RUST, 9.0)
    connections = [
        ((0.28, 0.83), (0.40, 0.77), "#9AABB5"),
        ((0.28, 0.79), (0.40, 0.51), "#9AABB5"),
        ((0.28, 0.59), (0.40, 0.77), "#9AABB5"),
        ((0.28, 0.35), (0.40, 0.25), "#9AABB5"),
        ((0.28, 0.11), (0.40, 0.51), "#9AABB5"),
        ((0.28, 0.59), (0.78, 0.785), "#B69A8D"),
        ((0.28, 0.11), (0.78, 0.585), "#B69A8D"),
        ((0.28, 0.79), (0.78, 0.385), "#B69A8D"),
        ((0.28, 0.07), (0.78, 0.185), "#B69A8D"),
    ]
    for start, end, color in connections:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=9,
                linewidth=0.9,
                color=color,
                alpha=0.68,
            )
        )
    _save_figure(fig, "f01_contribution_map")


def _figure_atm_wedge(rows: list[dict[str, float | str]]) -> None:
    mean_clock = float(rows[0]["clock_mean"])
    spread = float(rows[0]["formula_atm_correlation"])
    basket = float(rows[1]["formula_atm_correlation"])
    labels = ["Mean clock", "Spread ATM", "Basket ATM"]
    values = [mean_clock, spread, basket]
    colors = [SLATE, RUST, TEAL]
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    positions = np.arange(3)
    ax.scatter(positions, values, s=115, color=colors, zorder=3)
    ax.vlines(positions, mean_clock, values, colors=colors, linewidth=3, alpha=0.7)
    ax.axhline(mean_clock, color=SLATE, linestyle="--", linewidth=1.2)
    for x, value, color in zip(positions, values, colors):
        ax.annotate(
            f"{value:.5f}",
            (x, value),
            xytext=(0, 10 if value >= mean_clock else -18),
            textcoords="offset points",
            ha="center",
            color=color,
            fontweight="bold",
        )
    ax.annotate(
        f"+{spread - mean_clock:.5f}",
        (1, (spread + mean_clock) / 2.0),
        xytext=(12, 0),
        textcoords="offset points",
        color=RUST,
        va="center",
    )
    ax.annotate(
        f"{basket - mean_clock:.5f}",
        (2, (basket + mean_clock) / 2.0),
        xytext=(12, 0),
        textcoords="offset points",
        color=TEAL,
        va="center",
    )
    ax.set_xticks(positions, labels)
    ax.set_ylabel("Correlation level")
    ax.set_ylim(min(values) - 0.014, max(values) + 0.014)
    ax.grid(axis="y", alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    _save_figure(fig, "f02_atm_jensen_wedge")


def _curvature_evidence() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for dispersion in np.linspace(0.0, 0.72, 73):
        e_scale = math.cosh(dispersion)
        e_inverse = math.cosh(dispersion)
        numerator = 2.0 * (e_scale * e_inverse - 1.0)
        for label, alpha in (("spread", -7.5), ("basket", 7.5)):
            rows.append(
                {
                    "case": label,
                    "log_scale_half_spread": dispersion,
                    "curvature_numerator": numerator,
                    "alpha": alpha,
                    "correlation_curvature": numerator / alpha,
                }
            )
    return rows


def _figure_curvature(rows: list[dict[str, float | str]]) -> None:
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    for label, color in (("spread", RUST), ("basket", TEAL)):
        selected = [row for row in rows if row["case"] == label]
        x = [float(row["log_scale_half_spread"]) for row in selected]
        y = [float(row["correlation_curvature"]) for row in selected]
        ax.plot(x, y, color=color, linewidth=2.4, label=label.capitalize())
    ax.axhline(0.0, color=SLATE, linewidth=1.0)
    ax.set_xlabel("Dispersion of the two-point log-scale mixture")
    ax.set_ylabel(r"Exact ATM correlation curvature $\rho_{\rm imp}''(0)$")
    ax.legend(frameon=False)
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    _save_figure(fig, "f03_local_curvature")


def _figure_leverage_geometry() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.axis("off")
    boxes = [
        (0.04, 0.58, 0.19, 0.24, "Factor driver\n$W^0$\n$X_t=x_0+\\mu t+\\nu W_t^0$", PALE_BLUE, NAVY),
        (0.31, 0.68, 0.20, 0.18, "Common component\n$h(X_t)dW_t^0$", PALE_RUST, RUST),
        (0.31, 0.28, 0.20, 0.18, "Independent residual\n$r(X_t)^\\top dU_t$", PALE_TEAL, TEAL),
        (0.59, 0.50, 0.18, 0.22, "Linear asset state\n$dZ_t=h(X_t)dW_t^0$\n$\\quad+r(X_t)^\\top dU_t$", "#F4F6F7", SLATE),
        (0.82, 0.66, 0.15, 0.19, "European claims\n1-D complex\nFeynman–Kac", PALE_TEAL, TEAL),
        (0.82, 0.25, 0.15, 0.19, "Barriers\nrandom moving\nboundary", PALE_RUST, RUST),
    ]
    for x, y, width, height, text, face, edge in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                width,
                height,
                boxstyle="round,pad=0.015,rounding_size=0.015",
                facecolor=face,
                edgecolor=edge,
                linewidth=1.4,
            )
        )
        ax.text(
            x + width / 2,
            y + height / 2,
            text,
            ha="center",
            va="center",
            fontsize=9.5,
            linespacing=1.3,
            color=INK,
        )
    arrows = [
        ((0.23, 0.70), (0.31, 0.77), RUST),
        ((0.23, 0.64), (0.31, 0.37), TEAL),
        ((0.51, 0.77), (0.59, 0.64), RUST),
        ((0.51, 0.37), (0.59, 0.56), TEAL),
        ((0.77, 0.64), (0.82, 0.75), TEAL),
        ((0.77, 0.55), (0.82, 0.35), RUST),
    ]
    for start, end, color in arrows:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=12,
                color=color,
                linewidth=1.3,
            )
        )
    _save_figure(fig, "f04_leverage_geometry")


def _figure_leverage_cf(rows: list[dict[str, float]]) -> None:
    u = np.array([row["u"] for row in rows])
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2), sharex=True)
    for ax, component in zip(axes, ("real", "imag")):
        direct = np.array([row[f"direct_{component}"] for row in rows])
        conditional = np.array([row[f"conditional_{component}"] for row in rows])
        gauge = np.array([row[f"gauge_{component}"] for row in rows])
        se = np.array([row[f"direct_{component}_se"] for row in rows])
        ax.fill_between(u, direct - 2 * se, direct + 2 * se, color=SLATE, alpha=0.15)
        ax.plot(u, direct, "o", color=INK, markersize=4, label="Direct simulation")
        ax.plot(u, conditional, color=TEAL, linewidth=2.0, label="Conditional law")
        ax.plot(u, gauge, "--", color=RUST, linewidth=1.7, label="Itô gauge")
        ax.set_xlabel("Fourier frequency $u$")
        ax.set_ylabel(f"{component.capitalize()} part")
        ax.grid(alpha=0.18)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(frameon=False, fontsize=8.5)
    fig.tight_layout()
    _save_figure(fig, "f05_leverage_cf")


def _phasegram_evidence() -> tuple[list[dict[str, float | int | str]], dict[str, Any]]:
    n_assets = 4
    dimension = n_assets * (n_assets - 1) // 2
    theta0 = np.linspace(0.35, 1.20, dimension)
    sigmas = np.linspace(0.25, 0.70, dimension)
    exact_rows: list[dict[str, float | int | str]] = []
    for time in np.linspace(0.0, 6.0, 61):
        for moment in (1, 2):
            exact_rows.append(
                {
                    "source": "exact",
                    "time": float(time),
                    "moment_order": moment,
                    "value": phasegram_finite_moment(moment, time, theta0, sigmas),
                    "standard_error": 0.0,
                }
            )

    rng = np.random.default_rng(SEED + 10)
    n_paths = 140_000
    for time in (0.5, 2.0, 5.0):
        terminal = theta0 + sigmas * math.sqrt(time) * rng.standard_normal(
            (n_paths, dimension)
        )
        determinants = np.prod(np.sin(terminal) ** 2, axis=1)
        for moment in (1, 2):
            values = determinants**moment
            estimate = float(np.mean(values))
            standard_error = float(np.std(values, ddof=1)) / math.sqrt(n_paths)
            exact = phasegram_finite_moment(moment, time, theta0, sigmas)
            if abs(estimate - exact) > 4.0 * standard_error + 2e-5:
                raise AssertionError("Phase-Gram moment missed exact value")
            exact_rows.append(
                {
                    "source": "monte_carlo",
                    "time": time,
                    "moment_order": moment,
                    "value": estimate,
                    "standard_error": standard_error,
                }
            )

    logdet_summary: dict[str, Any] = {}
    for stationary_n in (3, 6, 10):
        n_stationary = 120_000
        logdet = phasegram_stationary_logdet(stationary_n, n_stationary, rng)
        d = stationary_n * (stationary_n - 1) // 2
        exact_mean = -2.0 * d * math.log(2.0)
        exact_variance = d * math.pi**2 / 3.0
        mean_mc = float(np.mean(logdet))
        variance_mc = float(np.var(logdet, ddof=1))
        mean_se = math.sqrt(exact_variance / n_stationary)
        variance_se_proxy = exact_variance * math.sqrt(2.0 / (n_stationary - 1))
        if abs(mean_mc - exact_mean) > 4.0 * mean_se:
            raise AssertionError("stationary logdet mean missed exact value")
        if abs(variance_mc - exact_variance) > 5.0 * variance_se_proxy:
            raise AssertionError("stationary logdet variance missed exact value")
        standardized = (logdet - exact_mean) / math.sqrt(exact_variance)
        histogram, edges = np.histogram(
            standardized, bins=np.linspace(-4.0, 4.0, 101), density=True
        )
        logdet_summary[str(stationary_n)] = {
            "n_assets": stationary_n,
            "dimension": d,
            "n_paths": n_stationary,
            "mean_mc": mean_mc,
            "mean_exact": exact_mean,
            "mean_standard_error": mean_se,
            "variance_mc": variance_mc,
            "variance_exact": exact_variance,
            "histogram_density": histogram,
            "histogram_edges": edges,
        }
    return exact_rows, logdet_summary


def _figure_phasegram_moments(
    rows: list[dict[str, float | int | str]]
) -> None:
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    for moment, color in ((1, TEAL), (2, RUST)):
        exact = [
            row
            for row in rows
            if row["source"] == "exact" and row["moment_order"] == moment
        ]
        mc = [
            row
            for row in rows
            if row["source"] == "monte_carlo" and row["moment_order"] == moment
        ]
        ax.plot(
            [float(row["time"]) for row in exact],
            [float(row["value"]) for row in exact],
            color=color,
            linewidth=2.2,
            label=rf"Exact $\mathbb{{E}}[(\det R_t)^{moment}]$",
        )
        ax.errorbar(
            [float(row["time"]) for row in mc],
            [float(row["value"]) for row in mc],
            yerr=[2.0 * float(row["standard_error"]) for row in mc],
            fmt="o",
            color=color,
            capsize=3,
            markersize=5,
        )
    ax.set_xlabel("Time")
    ax.set_ylabel("Determinant moment")
    ax.set_yscale("log")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False, fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    _save_figure(fig, "f06_phasegram_moments")


def _figure_phasegram_logdet(summary: dict[str, Any]) -> None:
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    for n_assets, color in (("3", GOLD), ("6", TEAL), ("10", RUST)):
        item = summary[n_assets]
        edges = np.asarray(item["histogram_edges"])
        centers = 0.5 * (edges[:-1] + edges[1:])
        density = np.asarray(item["histogram_density"])
        ax.plot(
            centers,
            density,
            color=color,
            linewidth=1.7,
            label=f"n={n_assets}, d={item['dimension']}",
        )
    x = np.linspace(-4.0, 4.0, 401)
    ax.plot(
        x,
        PHI0 * np.exp(-0.5 * x * x),
        color=INK,
        linestyle="--",
        label="N(0,1)",
    )
    ax.set_xlabel("Standardized stationary log determinant")
    ax.set_ylabel("Density")
    ax.grid(alpha=0.18)
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    _save_figure(fig, "f07_phasegram_logdet")


def _nonautonomous_rows() -> list[dict[str, float]]:
    return [
        nonautonomous_linear_transform(float(time), 0.7)
        for time in np.linspace(0.10, 2.0, 39)
    ]


def _figure_operator_ordering(rows: list[dict[str, float]]) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5))
    left = axes[0]
    left.axis("off")
    left.set_xlim(0.0, 1.0)
    left.set_ylim(0.0, 1.0)
    box_specs = [
        (0.07, 0.68, "$Q_{0,t}$", PALE_BLUE, NAVY),
        (0.62, 0.68, "$\\mathcal{A}_t$", PALE_RUST, RUST),
        (0.07, 0.17, "$\\partial_t Q_{0,t}$", PALE_TEAL, TEAL),
        (0.62, 0.17, "$[Q_{0,t},\\mathcal{A}_t]$", "#F7F1E6", GOLD),
    ]
    for x, y, text, face, edge in box_specs:
        left.add_patch(
            FancyBboxPatch(
                (x, y),
                0.29,
                0.17,
                boxstyle="round,pad=0.015",
                facecolor=face,
                edgecolor=edge,
                linewidth=1.4,
            )
        )
        left.text(x + 0.145, y + 0.085, text, ha="center", va="center", fontsize=12)
    left.add_patch(
        FancyArrowPatch(
            (0.36, 0.765),
            (0.62, 0.765),
            arrowstyle="-|>",
            mutation_scale=12,
            color=TEAL,
            linewidth=1.5,
        )
    )
    left.text(0.49, 0.82, "correct right action", ha="center", color=TEAL, fontsize=8.5)
    left.add_patch(
        FancyArrowPatch(
            (0.215, 0.68),
            (0.215, 0.34),
            arrowstyle="-|>",
            mutation_scale=12,
            color=NAVY,
            linewidth=1.5,
        )
    )
    left.add_patch(
        FancyArrowPatch(
            (0.70, 0.68),
            (0.70, 0.34),
            arrowstyle="-|>",
            mutation_scale=12,
            color=RUST,
            linewidth=1.5,
        )
    )
    left.text(
        0.5,
        0.47,
        "$\\partial_tQ_{0,t}=Q_{0,t}\\mathcal{A}_t$,\nnot $\\mathcal{A}_tQ_{0,t}$",
        ha="center",
        va="center",
        fontsize=10,
        color=INK,
    )

    right = axes[1]
    time = np.array([row["time"] for row in rows])
    true = np.array([row["true_transform"] for row in rows])
    wrong = np.array([row["misordered_transform"] for row in rows])
    right.plot(time, true, color=TEAL, linewidth=2.2, label="True two-time transform")
    right.plot(time, wrong, color=RUST, linewidth=2.2, label="Misordered horizon PDE")
    right.fill_between(time, true, wrong, color=RUST, alpha=0.10)
    right.set_xlabel("Horizon $T$")
    right.set_ylabel("Linear-potential transform")
    right.grid(alpha=0.18)
    right.legend(frameon=False, fontsize=8.5)
    right.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    _save_figure(fig, "f08_operator_ordering")


def build_all() -> None:
    """Generate all paper figures, tables, and terminal assertions."""

    _ensure_directories()
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10.0,
            "axes.labelcolor": INK,
            "axes.edgecolor": SLATE,
            "xtick.color": INK,
            "ytick.color": INK,
            "text.color": INK,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    two_point = centered_mixture_identities(
        np.array([1.0, 2.5]), np.array([0.35, 0.65])
    )
    two_point_price = 0.35 * bachelier_call(1.0, 0.0) + 0.65 * bachelier_call(
        2.5, 0.0
    )
    two_point_inverted = implied_total_std(two_point_price, 0.0)
    if abs(two_point_inverted - two_point["atm_implied_std"]) > 1e-11:
        raise AssertionError("two-point ATM identity failed")

    clock_grid, clock_density = phase8_clock_density()
    wedge_rows, wedge_summary = _phase8_wedge_evidence(clock_grid, clock_density)
    if abs(
        wedge_summary["spread_formula_atm"] - wedge_summary["spread_inverted_atm"]
    ) >= 2e-10:
        raise AssertionError("spread ATM inversion missed exact formula")
    if abs(
        wedge_summary["basket_formula_atm"] - wedge_summary["basket_inverted_atm"]
    ) >= 2e-10:
        raise AssertionError("basket ATM inversion missed exact formula")
    if not (
        wedge_summary["spread_curvature"] < 0.0
        < wedge_summary["basket_curvature"]
    ):
        raise AssertionError("opposite curvature signs failed")

    curvature_rows = _curvature_evidence()
    leverage_rows, leverage_summary = _simulate_leverage_cf()
    if leverage_summary["direct_conditional_cf_max_gap"] >= (
        4.0 * leverage_summary["direct_mc_se_max"] + 1e-4
    ):
        raise AssertionError("direct and conditional leveraged CFs disagree")
    if leverage_summary["conditional_gauge_cf_max_gap"] >= 1e-4:
        raise AssertionError("conditional and gauge leveraged CFs disagree")

    phasegram_rows, logdet_summary = _phasegram_evidence()
    nonautonomous_rows = _nonautonomous_rows()
    reference_nonautonomous = nonautonomous_linear_transform(1.3, 0.7)
    if reference_nonautonomous["absolute_gap"] <= 0.5:
        raise AssertionError("nonautonomous counterexample is too small")

    _write_csv(
        "phase14_atm_wedge.csv",
        wedge_rows,
        [
            "case",
            "alpha",
            "clock_mean",
            "e_sqrt_variance",
            "e_inverse_sqrt_variance",
            "formula_atm_correlation",
            "inverted_atm_correlation",
            "jensen_correction",
            "local_correlation_curvature",
        ],
    )
    _write_csv(
        "phase14_curvature.csv",
        curvature_rows,
        [
            "case",
            "log_scale_half_spread",
            "curvature_numerator",
            "alpha",
            "correlation_curvature",
        ],
    )
    _write_csv(
        "phase14_leverage_cf.csv",
        leverage_rows,
        [
            "u",
            "direct_real",
            "direct_imag",
            "direct_real_se",
            "direct_imag_se",
            "conditional_real",
            "conditional_imag",
            "gauge_real",
            "gauge_imag",
            "direct_conditional_gap",
            "gap_standard_error",
            "conditional_gauge_gap",
        ],
    )
    _write_csv(
        "phase14_phasegram_moments.csv",
        phasegram_rows,
        ["source", "time", "moment_order", "value", "standard_error"],
    )
    _write_json("phase14_phasegram_logdet.json", logdet_summary)
    _write_csv(
        "phase14_nonautonomous_check.csv",
        nonautonomous_rows,
        [
            "time",
            "lambda",
            "true_mean",
            "misordered_mean",
            "true_variance",
            "misordered_variance",
            "true_transform",
            "misordered_transform",
            "absolute_gap",
            "ratio",
        ],
    )
    _write_json(
        "phase14_identity_checks.json",
        {
            "seed": SEED,
            "two_point_mixture": two_point,
            "two_point_inverted_atm_std": two_point_inverted,
            "phase8_wedge": wedge_summary,
            "leverage": leverage_summary,
            "nonautonomous_reference": reference_nonautonomous,
        },
    )
    _write_json(
        "phase14_software_versions.json",
        {
            "seed": SEED,
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
            "platform": platform.platform(),
            "script": "scripts/build_phase14_figures.py",
        },
    )

    _figure_contribution_map()
    _figure_atm_wedge(wedge_rows)
    _figure_curvature(curvature_rows)
    _figure_leverage_geometry()
    _figure_leverage_cf(leverage_rows)
    _figure_phasegram_moments(phasegram_rows)
    _figure_phasegram_logdet(logdet_summary)
    _figure_operator_ordering(nonautonomous_rows)

    print("Phase 14 figures and evidence built successfully")
    print(
        json.dumps(
            {
                "clock_mean": wedge_summary["clock_mean"],
                "spread_atm": wedge_summary["spread_formula_atm"],
                "basket_atm": wedge_summary["basket_formula_atm"],
                "leverage_cf_max_gap": leverage_summary[
                    "direct_conditional_cf_max_gap"
                ],
                "leverage_gauge_max_gap": leverage_summary[
                    "conditional_gauge_cf_max_gap"
                ],
                "phasegram_cases": sorted(logdet_summary),
                "nonautonomous_gap": reference_nonautonomous["absolute_gap"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    build_all()
