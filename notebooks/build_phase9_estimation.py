"""Build the Phase 9 empirical estimation notebook."""

import textwrap
from pathlib import Path

import nbformat as nbf


def md(source: str):
    return nbf.v4.new_markdown_cell(textwrap.dedent(source).strip())


def code(source: str):
    return nbf.v4.new_code_cell(textwrap.dedent(source).strip())


cells = [
    md(
        r"""
        # Phase 9: exact estimation and an empirical study of equity pair correlations

        Computational record for `PHASE_9_ESTIMATION.md`.

        **Structural finding (proved in-module, tested in-suite):** the
        bounded-factor correlation model is *scale-observationally-
        equivalent* — \((c,\mu,\sigma)\) and \((\lambda c,\mu/\lambda,
        \sigma/\lambda)\) induce identical laws for every observable
        correlation functional. Only the ratios \(\mu/c\) and \(\sigma/c\)
        are identified from correlation observations; estimation targets
        those ratios in the normalized coordinate
        \(x=\rho/\sqrt{1-\rho^2}\), where increments are exactly Gaussian
        and the MLE is closed-form OLS.

        Empirical content: rolling 60-day realized correlations for four
        liquid S&P 500 pairs from the local alpha-engine store
        (2015–2026), exact MLE against two Fisher-space competitors,
        out-of-sample PIT diagnostics (marginal KS **and** state-correlation,
        which is where random-walk misspecification actually shows up), and
        a deterministic attenuation study across estimation windows.
        """
    ),
    code(
        r"""
        from pathlib import Path
        import json, math, platform, sys, time

        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        import scipy
        from scipy.stats import norm

        ROOT = Path.cwd().resolve()
        if not (ROOT / "phase9_estimation.py").exists():
            candidates = [ROOT, *ROOT.parents]
            ROOT = next(p for p in candidates if (p / "phase9_estimation.py").exists())
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))

        import phase9_estimation as p9

        SEED = 20260821
        FIGURES = ROOT / "phase9_figures"
        FIGURES.mkdir(exist_ok=True)
        DATA_DIR = Path("/home/fire/Documents/alpha_engine/data/prices")

        environment = {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "scipy": scipy.__version__,
            "platform": platform.platform(),
            "seed": SEED,
        }
        print(json.dumps(environment, indent=2))
        started = time.time()
        """
    ),
    md(
        r"""
        ## 1. Data: realized correlation series for four liquid pairs

        Daily log returns on common trading dates, 2015-01-01 onward;
        rolling 60-day Pearson correlation. The series is treated as a noisy
        observation of the latent bounded-factor dynamics (attenuation
        quantified in Section 4).
        """
    ),
    code(
        r"""
        PAIRS = [("XOM", "CVX"), ("JPM", "BAC"), ("KO", "PEP"), ("AAPL", "MSFT")]
        START = "2015-01-01"
        WINDOW = 60

        def load_returns(sym):
            df = pd.read_parquet(DATA_DIR / f"{sym}.parquet")
            df = df.loc[df.index >= START, "adj_close"]
            return np.log(df).diff().dropna()

        series = {}
        for s1, s2 in PAIRS:
            r1, r2 = load_returns(s1), load_returns(s2)
            joined = pd.concat([r1, r2], axis=1, join="inner").dropna()
            rho, ends = p9.realized_correlation_series(
                joined.iloc[:, 0].to_numpy(), joined.iloc[:, 1].to_numpy(),
                window=WINDOW)
            dates = joined.index[ends]
            series[(s1, s2)] = (rho, dates)
            print(f"{s1}/{s2}: {rho.size} windows, "
                  f"mean {rho.mean():+.3f}, sd {rho.std():.3f}, "
                  f"range [{rho.min():+.3f}, {rho.max():+.3f}]")

        fig, ax = plt.subplots(figsize=(10.5, 4.6))
        for (s1, s2), (rho, dates) in series.items():
            ax.plot(dates, rho, lw=0.9, label=f"{s1}/{s2}")
        ax.axhline(0, color="gray", lw=0.6, ls="--")
        ax.set_ylabel("60-day realized correlation")
        ax.set_title("Realized correlation series (local alpha-engine data)")
        ax.legend(fontsize=8, ncol=2)
        fig.tight_layout()
        fig.savefig(FIGURES / "phase9_rho_series.png", dpi=150)
        plt.show()
        """
    ),
    md(
        r"""
        ## 2. Exact MLE vs Fisher-space competitors

        All three models price the observed series with their own consistent
        Jacobian, so likelihoods/AIC/BIC are comparable. The conjugate-RW
        fit reports the identified ratios \((\mu/c,\sigma/c)\).
        """
    ),
    code(
        r"""
        rows = []
        fits_all = {}
        for (s1, s2), (rho, _dates) in series.items():
            conj = p9.fit_conjugate_rw(rho)
            frw = p9.fit_fisher_rw(rho)
            fou = p9.fit_fisher_ou(rho)
            fits_all[(s1, s2)] = (conj, frw, fou)
            aic = lambda ll, k: 2 * k - 2 * ll
            rows.append({
                "pair": f"{s1}/{s2}",
                "conj mu/c": round(conj.drift, 3),
                "conj sigma/c": round(conj.volatility, 3),
                "conj logL": round(conj.log_likelihood, 1),
                "frw m": round(frw.m, 3),
                "frw s": round(frw.s, 3),
                "frw logL": round(frw.log_likelihood, 1),
                "fou kappa": round(fou.kappa, 2),
                "fou theta": round(fou.theta, 3),
                "fou s": round(fou.s, 3),
                "fou logL": round(fou.log_likelihood, 1),
                "AIC conj": round(aic(conj.log_likelihood, conj.n_params), 1),
                "AIC frw": round(aic(frw.log_likelihood, frw.n_params), 1),
                "AIC fou": round(aic(fou.log_likelihood, fou.n_params), 1),
            })
        table = pd.DataFrame(rows)
        print(table.to_string(index=False))
        """
    ),
    code(
        r"""
        # Marginal stationary sd implied by each model (comparable scale-free
        # quantities): conjugate RW has no stationary law (pure diffusion);
        # report instead the annualized drift/vol ratios and, for the OU,
        # the stationary sd s/sqrt(2 kappa) in Fisher space.
        summary = []
        for (s1, s2), (conj, frw, fou) in fits_all.items():
            summary.append({
                "pair": f"{s1}/{s2}",
                "conj vol ratio (sigma/c)": round(conj.volatility, 3),
                "fisher-OU stationary sd": round(fou.s / math.sqrt(2 * fou.kappa), 3),
                "fisher-RW vol": round(frw.s, 3),
            })
        print(pd.DataFrame(summary).to_string(index=False))
        """
    ),
    md(
        r"""
        ## 3. Out-of-sample diagnostics

        Fit on the first 70% of each series; one-step-ahead PIT values on the
        remaining 30%. Two complementary checks:

        - **Marginal KS** — calibration of the predictive CDF;
        - **PIT–state correlation** — dynamic adequacy (this is where the
          random-walk misspecification appears: its u-marginal can stay
          near-uniform while \(u_t\) correlates with the lagged state).

        Also reported: out-of-sample mean log predictive density.
        """
    ),
    code(
        r"""
        def oos_logscore_conjugate(rho, fit, dt=1/252):
            x = np.asarray(p9.conjugate_coordinate(rho, scale=1.0))
            dx = np.diff(x)
            z = (dx - fit.drift * dt) / (fit.volatility * math.sqrt(dt))
            jac = -1.5 * np.log(1.0 - rho[1:] ** 2)
            return float(np.mean(norm.logpdf(z) - math.log(fit.volatility * math.sqrt(dt)) + jac))

        def oos_logscore_fisher_rw(rho, fit, dt=1/252):
            y = np.asarray(p9.fisher_coordinate(rho))
            dy = np.diff(y)
            z = (dy - fit.m * dt) / (fit.s * math.sqrt(dt))
            jac = -np.log(1.0 - rho[1:] ** 2)
            return float(np.mean(norm.logpdf(z) - math.log(fit.s * math.sqrt(dt)) + jac))

        def oos_logscore_fisher_ou(rho, fit, dt=1/252):
            y = np.asarray(p9.fisher_coordinate(rho))
            decay = math.exp(-fit.kappa * dt)
            cond_sd = math.sqrt(fit.s**2 * (1 - decay**2) / (2 * fit.kappa))
            z = (y[1:] - (fit.theta + (y[:-1] - fit.theta) * decay)) / cond_sd
            jac = -np.log(1.0 - rho[1:] ** 2)
            return float(np.mean(norm.logpdf(z) - math.log(cond_sd) + jac))

        diag_rows = []
        pit_store = {}
        for (s1, s2), (rho, _dates) in series.items():
            split = int(0.7 * rho.size)
            train, test = rho[:split], rho[split - 1:]
            conj = p9.fit_conjugate_rw(train)
            frw = p9.fit_fisher_rw(train)
            fou = p9.fit_fisher_ou(train)

            pit_c = p9.transition_pit_conjugate(test, conj)
            pit_rw = p9.transition_pit_fisher_rw(test, frw)
            pit_ou = p9.transition_pit_fisher_ou(test, fou)
            pit_store[(s1, s2)] = (pit_c, pit_rw, pit_ou)

            state = p9.fisher_coordinate(test[:-1])
            row = {"pair": f"{s1}/{s2}", "n_oos": len(pit_c)}
            for name, pit, ls in [
                ("conj", pit_c, oos_logscore_conjugate(test, conj)),
                ("frw", pit_rw, oos_logscore_fisher_rw(test, frw)),
                ("fou", pit_ou, oos_logscore_fisher_ou(test, fou)),
            ]:
                ks_stat, ks_p = p9.ks_uniformity(pit)
                _corr, z_state = p9.pit_state_correlation(pit, state)
                row[f"KS {name}"] = round(ks_stat, 3)
                row[f"KS-p {name}"] = round(ks_p, 3)
                row[f"zstate {name}"] = round(z_state, 2)
                row[f"logscore {name}"] = round(ls, 3)
            diag_rows.append(row)
        diag = pd.DataFrame(diag_rows)
        print(diag.to_string(index=False))
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True, sharey=True)
        for ax, ((s1, s2), (pit_c, pit_rw, pit_ou)) in zip(axes.ravel(), pit_store.items()):
            for pit, label in [(pit_c, "conjugate"), (pit_rw, "Fisher-RW"), (pit_ou, "Fisher-OU")]:
                ax.hist(pit, bins=24, range=(0, 1), histtype="step", lw=1.6, label=label,
                        density=True)
            ax.axhline(1.0, color="gray", lw=0.7, ls="--")
            ax.set_title(f"{s1}/{s2}", fontsize=10)
        axes[0, 0].legend(fontsize=8)
        fig.suptitle("Out-of-sample PIT histograms (uniform = calibrated)")
        fig.tight_layout()
        fig.savefig(FIGURES / "phase9_pit_histograms.png", dpi=150)
        plt.show()
        """
    ),
    md(
        r"""
        ## 4. Attenuation: how window noise biases the estimated dynamics

        Deterministic Monte Carlo (seeded): simulate the TRUE latent system,
        form rolling realized correlations at window lengths 20/40/60/120,
        refit the ratios, and measure the volatility-ratio attenuation
        factor (estimated / true). Window noise mechanically damps the
        measured dynamics; the curve quantifies by how much.
        """
    ),
    code(
        r"""
        true_scale, true_drift, true_vol = 1.5, 0.3, 0.7
        att_rows = []
        for window in (20, 40, 60, 120):
            res = p9.attenuation_study(
                true_scale=true_scale, true_drift=true_drift,
                true_volatility=true_vol, n_days=2500, window=window,
                n_replications=24, seed=SEED + window)
            att_rows.append({
                "window": window,
                "vol ratio median": round(res["vol_ratio_median"], 4),
                "true vol ratio": round(res["true_vol_ratio"], 4),
                "attenuation factor": round(res["attenuation_factor"], 3),
                "IQR": round(res["vol_ratio_iqr"], 4),
            })
        att = pd.DataFrame(att_rows)
        print(att.to_string(index=False))

        fig, ax = plt.subplots(figsize=(7.2, 4.0))
        ax.plot(att["window"], att["attenuation factor"], "o-")
        ax.axhline(1.0, color="gray", lw=0.8, ls="--", label="no attenuation")
        ax.set_xlabel("estimation window (days)")
        ax.set_ylabel("estimated / true volatility ratio")
        ax.set_title("Attenuation of estimated correlation dynamics vs window length")
        ax.legend()
        fig.tight_layout()
        fig.savefig(FIGURES / "phase9_attenuation.png", dpi=150)
        plt.show()
        """
    ),
    md(
        r"""
        ## 5. Record

        All estimation is exact and closed-form (OLS in the normalized
        conjugate coordinate); competitors use their own consistent
        Jacobians. Figures in `phase9_figures/`.
        """
    ),
    code(
        r"""
        elapsed = time.time() - started
        print(f"notebook executed in {elapsed:.1f} s")
        """
    ),
]


def main() -> None:
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {
        "display_name": "Python 3 (phase3-paper)",
        "language": "python",
        "name": "python3",
    }
    out = Path(__file__).with_name("phase9_estimation_empirical.ipynb")
    nbf.write(nb, out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
