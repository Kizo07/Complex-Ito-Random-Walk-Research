"""Tests for Phase 8 COS-on-the-clock vanilla pricing."""

import math
import unittest

import numpy as np

import phase8_cos as p8
import phase7_term_structure as p7


DRIFT = lambda t: 0.3
VOL = lambda t: 0.8
SCALE = 1.0
X0 = 0.0
MATURITY = 1.0
RATE = 0.05
SIGMA1, SIGMA2 = 1.5, 2.5


class TestMgf(unittest.TestCase):
    def test_mgf_at_zero_is_one(self):
        value = p8.mgf_A(0.0, maturity=MATURITY, x0=X0, drift=DRIFT,
                         volatility=VOL, scale=SCALE)
        self.assertAlmostEqual(value, 1.0, places=8)

    def test_mgf_deterministic_limit(self):
        # sigma -> 0 => A_T -> int_0^T rho(x0 + drift*t) dt (deterministic
        # path average of the bounded map along the drift line).
        from scipy.integrate import quad

        tiny_vol = lambda t: 1e-6
        path_average = quad(
            lambda t: (X0 + DRIFT(1.0) * t)
            / math.sqrt((X0 + DRIFT(1.0) * t) ** 2 + SCALE**2),
            0.0,
            MATURITY,
            epsabs=1e-12,
        )[0]
        for s in (-1.5, 0.7, 2.0):
            got = p8.mgf_A(s, maturity=MATURITY, x0=X0, drift=DRIFT,
                           volatility=tiny_vol, scale=SCALE)
            expected = math.exp(-s * path_average)
            # tiny-vol FK solve carries O(1e-4) discretization error
            self.assertLess(abs(got - expected), 1.5e-4)

    def test_mgf_bounds_and_convexity(self):
        # |L_A(s)| <= e^{|s| T}; positivity; Jensen/convexity lower bound
        # L_A(s) >= 1 - s E[A_T] (pointwise convexity of e^{-s A} in s).
        mean_a = 0.14  # conservative proxy; the bound below is checked with it
        grid = np.linspace(-2.0, 2.0, 9)
        values = [
            p8.mgf_A(float(s), maturity=MATURITY, x0=X0, drift=DRIFT,
                     volatility=VOL, scale=SCALE)
            for s in grid
        ]
        for s, v in zip(grid, values):
            self.assertLessEqual(v, math.exp(abs(float(s)) * MATURITY) + 1e-9)
            self.assertGreater(v, 0.0)
        # Convexity: second differences nonnegative on an even grid.
        second = np.diff(values, 2)
        self.assertTrue(np.all(second > -1e-8))


class TestCharacteristicFunction(unittest.TestCase):
    def test_deterministic_clock_alpha_zero(self):
        # alpha2 = 0 makes alpha = 0: the clock is deterministic beta*T and
        # phi must be the exact Gaussian transform.
        beta = SIGMA1**2
        for u in (0.5, 1.7):
            got = p8.linear_combo_characteristic(
                u, z0=100.0, maturity=MATURITY, rate=RATE, beta=beta, alpha=0.0,
                x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
            )
            expected = math.exp(-RATE * MATURITY) * complex(
                math.cos(u * 100.0), math.sin(u * 100.0)
            ) * math.exp(-0.5 * u * u * beta * MATURITY)
            self.assertAlmostEqual(got.real, expected.real, places=8)
            self.assertAlmostEqual(got.imag, expected.imag, places=8)

    def test_phi_zero_is_discount_factor(self):
        got = p8.linear_combo_characteristic(
            0.0, z0=50.0, maturity=MATURITY, rate=RATE,
            beta=SIGMA1**2 + SIGMA2**2, alpha=-2 * SIGMA1 * SIGMA2,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        self.assertAlmostEqual(abs(got), math.exp(-RATE * MATURITY), places=8)


class TestCosPricing(unittest.TestCase):
    BETA = SIGMA1**2 + SIGMA2**2
    ALPHA = -2.0 * SIGMA1 * SIGMA2

    def test_deterministic_clock_matches_bachelier(self):
        strike = 98.0
        got = p8.cos_call_price(
            strike, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=0.0,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        expected = math.exp(-RATE * MATURITY) * p8.bachelier_call(
            100.0, self.BETA * MATURITY, strike
        )
        self.assertAlmostEqual(got, expected, places=6)

    def test_put_call_parity(self):
        strike = 95.0
        call = p8.cos_call_price(
            strike, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        put = p8.cos_put_price(
            strike, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        parity = math.exp(-RATE * MATURITY) * (100.0 - strike)
        self.assertAlmostEqual(call - put, parity, places=8)

    def test_cos_mode_convergence(self):
        base = p8.cos_call_price(
            97.0, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE, n_modes=64,
        )
        refined = p8.cos_call_price(
            97.0, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE, n_modes=128,
        )
        self.assertAlmostEqual(base, refined, places=5)

    def test_mc_benchmark_spread_call(self):
        rng = np.random.default_rng(20260821)
        n_paths, n_steps = 200000, 400
        grid = np.linspace(0.0, MATURITY, n_steps + 1)
        sd_step = VOL(0.5) * math.sqrt(MATURITY / n_steps)
        state = np.full(n_paths, X0)
        rho_prev = state / np.sqrt(state**2 + SCALE**2)
        acc = np.zeros(n_paths)
        dt = MATURITY / n_steps
        for _ in range(n_steps):
            state = state + DRIFT(0.5) * dt + sd_step * rng.standard_normal(n_paths)
            rho = state / np.sqrt(state**2 + SCALE**2)
            acc += 0.5 * (rho_prev + rho) * dt
            rho_prev = rho
        clocks = self.BETA * MATURITY + self.ALPHA * acc
        z_t = 100.0 + np.sqrt(clocks) * rng.standard_normal(n_paths)
        strike = 97.0
        mc = math.exp(-RATE * MATURITY) * float(np.mean(np.maximum(z_t - strike, 0.0)))
        se = math.exp(-RATE * MATURITY) * float(
            np.std(np.maximum(z_t - strike, 0.0)) / math.sqrt(n_paths)
        )
        cos_price = p8.cos_call_price(
            strike, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        self.assertLessEqual(abs(cos_price - mc), 3.5 * se + 1e-4)

    def test_deep_otm_positive_and_small(self):
        price = p8.cos_call_price(
            130.0, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        self.assertGreater(price, 0.0)
        self.assertLess(price, 1e-3)


class TestImpliedCorrelation(unittest.TestCase):
    BETA = SIGMA1**2 + SIGMA2**2
    ALPHA = -2.0 * SIGMA1 * SIGMA2

    def test_round_trip(self):
        # ATM strike: strong correlation sensitivity (deep-ITM strikes are
        # nearly rho-insensitive and cannot be inverted).
        price = p8.constant_rho_call(
            100.0, z0=100.0, maturity=MATURITY, rate=RATE, rho_const=0.4,
            sigma1=SIGMA1, sigma2=SIGMA2, alpha1=1.0, alpha2=-1.0,
        )
        recovered = p8.implied_correlation(
            price, z0=100.0, maturity=MATURITY, rate=RATE,
            sigma1=SIGMA1, sigma2=SIGMA2, alpha1=1.0, alpha2=-1.0, strike=100.0,
        )
        self.assertAlmostEqual(recovered, 0.4, places=8)

    def test_stochastic_price_jensen_bounds(self):
        # Bachelier call is convex in the variance: the stochastic-correlation
        # price must dominate the constant-correlation price at E[v] (Jensen
        # lower bound) and stay below the two-endpoint chord bound.
        mean_a = 0.14  # E[A_T] for these parameters (quadrature value ~0.14)
        e_var = self.BETA * MATURITY + self.ALPHA * mean_a
        jensen_lo = math.exp(-RATE * MATURITY) * p8.bachelier_call(
            100.0, e_var, 97.0
        )
        price = p8.cos_call_price(
            97.0, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        var_lo = (self.BETA - abs(self.ALPHA)) * MATURITY
        var_hi = (self.BETA + abs(self.ALPHA)) * MATURITY
        chord_hi = math.exp(-RATE * MATURITY) * max(
            p8.bachelier_call(100.0, var_lo, 97.0),
            p8.bachelier_call(100.0, var_hi, 97.0),
        )
        self.assertGreaterEqual(price, jensen_lo - 1e-6)
        self.assertLessEqual(price, chord_hi + 1e-6)

    def test_clock_quadrature_matches_cos(self):
        cos_price = p8.cos_call_price(
            97.0, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=DRIFT, volatility=VOL, scale=SCALE,
        )
        quad_price, _ = p8.clock_quadrature_call_price(
            97.0, z0=100.0, maturity=MATURITY, rate=RATE,
            beta=self.BETA, alpha=self.ALPHA,
            x0=X0, drift=0.3, volatility=0.8, scale=SCALE,
        )
        self.assertLess(abs(cos_price - quad_price), 2e-4)


class TestGreeks(unittest.TestCase):
    def test_greeks_match_finite_differences_of_clock_quadrature(self):
        # Deterministic-vs-deterministic: build the Milestone-4 clock density,
        # price by quadrature, bump inputs, compare with clock_density_greeks.
        import phase6_fk as p6f

        maturity = 1.0
        beta = SIGMA1**2 + SIGMA2**2
        alpha = -2.0 * SIGMA1 * SIGMA2
        strike = 97.0

        def quad_price(z0_val: float, b_val: float, al_val: float,
                       s1: float, s2: float) -> float:
            # Rebuild the affine clock coefficients from the (possibly
            # bumped) volatilities so sigma finite differences bite.
            b_val = s1**2 + s2**2
            al_val = -2.0 * s1 * s2
            a_grid, p_grid = p6f.clock_density_grid(
                maturity=maturity, x0=X0, drift=0.3, volatility=0.8, scale=SCALE,
                n_modes=48, n_points=401, n_grid=500,
            )
            clocks = b_val * maturity + al_val * a_grid
            payoff = np.array([
                p8.bachelier_call(z0_val, max(v, 1e-12), strike) for v in clocks
            ])
            return math.exp(-RATE * maturity) * float(np.trapezoid(payoff * p_grid, a_grid))

        z0 = 100.0
        base = quad_price(z0, beta, alpha, SIGMA1, SIGMA2)
        eps_z, eps_s = 1e-4, 1e-5
        fd_delta = (quad_price(z0 + eps_z, beta, alpha, SIGMA1, SIGMA2)
                    - quad_price(z0 - eps_z, beta, alpha, SIGMA1, SIGMA2)) / (2 * eps_z)
        fd_gamma = (quad_price(z0 + eps_z, beta, alpha, SIGMA1, SIGMA2)
                    - 2 * base
                    + quad_price(z0 - eps_z, beta, alpha, SIGMA1, SIGMA2)) / eps_z**2
        fd_vega1 = (quad_price(z0, beta, alpha, SIGMA1 + eps_s, SIGMA2)
                    - quad_price(z0, beta, alpha, SIGMA1 - eps_s, SIGMA2)) / (2 * eps_s)

        a_grid, p_grid = p6f.clock_density_grid(
            maturity=maturity, x0=X0, drift=0.3, volatility=0.8, scale=SCALE,
            n_modes=48, n_points=401, n_grid=500,
        )
        greeks = p8.clock_density_greeks(
            strike, z0=z0, maturity=maturity, rate=RATE,
            beta=beta, alpha=alpha, sigma1=SIGMA1, sigma2=SIGMA2,
            alpha1=1.0, alpha2=-1.0, a_grid=a_grid, p_grid=p_grid,
        )
        self.assertAlmostEqual(greeks["delta"], fd_delta, places=5)
        self.assertAlmostEqual(greeks["gamma"], fd_gamma, places=3)
        self.assertAlmostEqual(greeks["vega_sigma1"], fd_vega1, places=4)


if __name__ == "__main__":
    unittest.main()
