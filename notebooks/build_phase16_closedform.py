"""Build the deterministic Phase 16 closed-form notebook."""

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
        # Phase 16: Toward closed-form American option prices

        Computational record for the Phase 16 paper. Phase 15 delivered the
        collocated logarithmic-spiral formula — European Black–Scholes plus
        **one numerical integral** over an explicit boundary. Phase 16
        removes the integral.

        The key is the drifted-Brownian **occupation resolvent**: for a
        phase-affine boundary (\(\log b\) affine in time to maturity) the
        early-exercise-premium integral collapses to the closed form

        \[
        J(\tau;a,m,\lambda)=\int_0^\tau e^{-\lambda s}
        \Phi\!\left(\frac{a+ms}{\sqrt s}\right)ds
        =R(a;\lambda,m)
        -e^{-\lambda\tau}\Big[\tfrac{1}{\nu(\nu+m)}+\tfrac{1}{\nu(\nu-m)}\Big]
        \Phi\!\Big(\tfrac{a+m\tau}{\sqrt\tau}\Big)
        +\tfrac{e^{-(m+\nu)a}}{\nu(\nu+m)}\Phi\!\Big(\tfrac{a-\nu\tau}{\sqrt\tau}\Big)
        -\tfrac{e^{(\nu-m)a}}{\nu(\nu-m)}\Phi\!\Big(\tfrac{-a-\nu\tau}{\sqrt\tau}\Big)
        \]

        with \(\nu=\sqrt{m^2+2\lambda}\) and the perpetual resolvent
        \(R=1/\lambda-e^{-(m+\nu)a}/(\nu(\nu+m))\) for \(a\ge0\),
        \(R=e^{(\nu-m)a}/(\nu(\nu-m))\) for \(a<0\). Multipiece
        phase-affine (PPA) boundaries then give American prices as **finite
        sums of closed-form terms** — no quadrature anywhere — with the
        knot values fixed by sequential value-matching collocation and
        perpetual pinning at long maturity.
        """
    ),
    code(
        r"""
        from pathlib import Path
        import json, math, platform, sys, time

        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np
        import scipy
        from scipy import special

        ROOT = Path.cwd().resolve()
        if not (ROOT / "phase16_closedform.py").exists():
            candidates = [ROOT, *ROOT.parents]
            ROOT = next(p for p in candidates
                        if (p / "phase16_closedform.py").exists())
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))

        import phase15_american as p15
        import phase16_closedform as p16

        SEED = 20260903
        FIGURES = ROOT / "phase16_figures"
        FIGURES.mkdir(exist_ok=True)
        TABLES = ROOT / "phase16_tables"
        TABLES.mkdir(exist_ok=True)

        K = 100.0
        environment = {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
            "seed": SEED,
        }
        print(json.dumps(environment, indent=2))
        started = time.time()
        """
    ),
    md(
        r"""
        ## 1. The occupation resolvent, validated

        \(J(\tau;a,m,\lambda)\) against 160-point Gauss–Legendre
        quadrature of its definition, plus the four analytic limits
        (\(\tau\to0\), \(\tau\to\infty\), \(a\to\pm\infty\)).
        """
    ),
    code(
        r"""
        from scipy import integrate

        rng = np.random.default_rng(SEED)
        worst = 0.0
        errs = []
        for _ in range(60):
            a = float(rng.uniform(-4.0, 4.0))
            m = float(rng.uniform(-2.0, 2.0))
            lam = float(rng.uniform(0.01, 0.3))
            tau = float(rng.uniform(0.01, 4.0))
            # adaptive reference (fixed-order GL resolves the thin
            # transition layer only slowly; the closed form is checked
            # against the adaptive integral)
            quad = integrate.quad(
                lambda s: math.exp(-lam * s)
                * special.ndtr((a + m * s) / math.sqrt(s)),
                0.0, tau, limit=300, epsabs=1e-13, epsrel=1e-13)[0]
            errs.append(abs(p16.occupation_J(tau, a, m, lam) - quad))
        worst = max(errs)
        print(f"60 random trials: worst abs error = {worst:.3e}")
        assert worst < 1e-10

        tau, lam, m, a = 2.0, 0.05, 0.3, 0.4
        nu = math.sqrt(m * m + 2 * lam)
        limits = {
            "J(0+)": p16.occupation_J(0.0, a, m, lam),
            "J(a->+inf) vs (1-e^-lt)/l": abs(
                p16.occupation_J(tau, 30.0, m, lam)
                - (1 - math.exp(-lam * tau)) / lam),
            "J(a->-inf)": p16.occupation_J(tau, -30.0, m, lam),
            "J(tau->inf) vs R": abs(
                p16.occupation_J(400.0, a, m, lam)
                - (1 / lam - math.exp(-(m + nu) * a) / (nu * (nu + m)))),
        }
        for name, v in limits.items():
            print(f"  {name}: {v:.3e}")
        assert max(limits.values()) < 1e-6
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
        taus = np.linspace(0.0, 4.0, 401)
        for a, m_, lam in ((0.5, 0.3, 0.1), (0.0, 0.0, 0.1),
                           (-0.5, -0.3, 0.1), (1.0, 0.5, 0.3)):
            js = [p16.occupation_J(t, a, m_, lam) for t in taus]
            axes[0].plot(taus, js, label=f"a={a}, m={m_}, λ={lam}")
        axes[0].set_xlabel(r"$\tau$")
        axes[0].set_ylabel(r"$J(\tau;a,m,\lambda)$")
        axes[0].set_title("Closed-form occupation functional")
        axes[0].legend(fontsize=7)
        xs = np.linspace(-3.0, 3.0, 241)
        R = [1 / 0.1 - math.exp(-(0.3 + math.sqrt(0.09 + 0.2)) * x)
             / (math.sqrt(0.29) * (math.sqrt(0.29) + 0.3)) if x >= 0
             else math.exp((math.sqrt(0.29) - 0.3) * x)
             / (math.sqrt(0.29) * (math.sqrt(0.29) - 0.3)) for x in xs]
        axes[1].plot(xs, R)
        axes[1].set_xlabel("a")
        axes[1].set_ylabel("R(a; 0.1, 0.3)")
        axes[1].set_title("Perpetual resolvent")
        fig.tight_layout()
        fig.savefig(FIGURES / "f01_occupation.png", dpi=160)
        plt.close(fig)
        print("saved f01_occupation.png")
        """
    ),
    md(
        r"""
        ## 2. Closed-form EEP for affine boundaries

        Single phase-affine boundary \(\ln b(u)=A-\gamma u\): the Phase 16
        closed form against the Phase 15 quadrature pipeline.
        """
    ),
    code(
        r"""
        worst = 0.0
        trials = [(math.log(110.0), 0.3, "call"),
                  (math.log(90.0), -0.2, "call"),
                  (math.log(95.0), 0.4, "put"),
                  (math.log(80.0), -0.1, "put"),
                  (math.log(95.0), 0.2, "put")]
        for A, gamma, kind in trials:
            bd = lambda u, A=A, gamma=gamma: math.exp(A - gamma * u)
            quad = p15.eep(100.0, 1.0, bd, K, 0.05, 0.05, 0.2, kind,
                           n_quad=128)
            cf = p16.eep_affine_closed(100.0, 1.0, A, gamma, K, 0.05, 0.05,
                                       0.2, kind)
            worst = max(worst, abs(cf - quad))
            print(f"{kind} A={A:.3f} gamma={gamma:+.1f}: "
                  f"quad={quad:.8f} closed={cf:.8f}")
        print(f"worst abs error: {worst:.3e}")
        assert worst < 1e-8
        """
    ),
    md(
        r"""
        ## 3. Multipiece phase-affine boundaries (PPA)

        Knots \(0=u_0<\cdots<u_m=T\) (1.5-clustered), continuity at knots,
        \(v_0=\ln b(0^+)\) at the maturity anchor, sequential
        value-matching collocation for \(v_1,\ldots,v_m\); the price is
        European + a sum of closed-form piece contributions. Convergence
        in \(m\) on the base case:
        """
    ),
    code(
        r"""
        R, Q, SIG, T = 0.05, 0.05, 0.2, 1.0
        refs = {}
        t0 = time.time()
        for kind in ("call", "put"):
            taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, kind,
                                             n_grid=250, n_quad=48,
                                             delta=1e-8)
            bd = lambda tau, ts=taus, bv=bvals: float(np.interp(tau, ts, bv))
            refs[kind] = {S: p15.american_from_boundary(
                S, T, bd, K, R, Q, SIG, kind, n_quad=96)
                for S in (90.0, 100.0, 110.0)}
        print(f"reference solves: {time.time() - t0:.1f}s")

        conv = {kind: [] for kind in ("call", "put")}
        for kind in ("call", "put"):
            for m in (2, 4, 6, 8, 12, 16):
                ku, kv = p16.solve_ppa_boundary(K, R, Q, SIG, T, kind, m=m)
                err = max(abs(p16.american_ppa_from_knots(
                    S, T, ku, kv, K, R, Q, SIG, kind) - refs[kind][S])
                    for S in (90.0, 100.0, 110.0))
                conv[kind].append((m, err))
            print(kind + ": " + " ".join(f"m={m}:{e:.5f}"
                                         for m, e in conv[kind]))
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
        ku, kv = p16.solve_ppa_boundary(K, R, Q, SIG, T, "call", m=8)
        bd_fn = p16.ppa_boundary_func(ku, kv)
        us = np.linspace(0.0, T, 300)
        axes[0].plot(us, [bd_fn(u) for u in us], lw=2, color="tab:red",
                     label="PPA boundary (call)")
        axes[0].plot(ku, np.exp(kv), "o", ms=4, color="tab:red")
        taus_r, bv_r = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                          n_grid=250, n_quad=48, delta=1e-8)
        axes[0].plot(taus_r, bv_r, ls="--", color="tab:blue",
                     label="reference (put)")
        axes[0].set_xlabel(r"time to maturity $\tau$")
        axes[0].set_ylabel(r"$b(\tau)$")
        axes[0].set_title("Boundaries, base case")
        axes[0].legend(fontsize=8)
        for kind, color in (("call", "tab:red"), ("put", "tab:blue")):
            axes[1].plot([m for m, _ in conv[kind]],
                         [e for _, e in conv[kind]], "o-", color=color,
                         label=kind)
        axes[1].set_yscale("log")
        axes[1].set_xlabel("number of pieces m")
        axes[1].set_ylabel("max price error vs reference")
        axes[1].set_title("PPA convergence")
        axes[1].legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f02_ppa.png", dpi=160)
        plt.close(fig)
        print("saved f02_ppa.png")
        """
    ),
    md(
        r"""
        ## 4. Perpetual pinning and the reduced-grid benchmark

        For \(T\ge1.5\) the last knot is pinned at \(\ln b_\infty\);
        interior knots are collocated. Recommended configuration:
        \(m=10\). **Revised after the review of 2026-09-02:** all errors
        are measured against the converged Broadie–Detemple
        adjacent-averaged tree oracle (not the grid-sensitive Volterra
        solver), and metric labels are RMSE / true MAE (mean) / maximum
        absolute error.
        """
    ),
    code(
        r"""
        grid = []
        for r_, q_ in ((0.05, 0.05), (0.07, 0.03), (0.03, 0.07)):
            for sig_ in (0.2, 0.4):
                for T_ in (0.5, 1.0, 3.0):
                    for kind in ("call", "put"):
                        grid.append((r_, q_, sig_, T_, kind))

        bench = []
        for r_, q_, sig_, T_, kind in grid:
            ku, kv = p16.solve_ppa_pinned(K, r_, q_, sig_, T_, kind, m=10)
            k1, k2, el, er, _ = p15.spiral_collocation(K, r_, q_, sig_,
                                                       T_, kind)
            for S in (90.0, 100.0, 110.0):
                oracle, spread = p15.tree_oracle(S, K, r_, q_, sig_, T_,
                                                 kind, Ns=(8000, 12000))
                ppa = p16.american_ppa_from_knots(S, T_, ku, kv, K, r_, q_,
                                                  sig_, kind)
                sp, *_ = p15.american_spiral(S, K, r_, q_, sig_, T_, kind,
                                             params=(k1, k2, el, er))
                bw = p15.baw(S, K, r_, q_, sig_, T_, kind)
                bench.append(dict(r=r_, q=q_, sigma=sig_, T=T_, kind=kind,
                                  S=S, oracle=oracle, spread=spread,
                                  ppa=ppa, spiral=sp, baw=bw))

        arr = {k: np.array([x[k] for x in bench])
               for k in ("oracle", "ppa", "spiral", "baw")}
        summary = {}
        print(f"{'method':>8} {'RMSE':>9} {'MAE':>9} {'MaxAE':>9}")
        for name in ("ppa", "spiral", "baw"):
            d = arr[name] - arr["oracle"]
            summary[name] = dict(rmse=float(np.sqrt(np.mean(d ** 2))),
                                 mae=float(np.mean(np.abs(d))),
                                 maxae=float(np.max(np.abs(d))))
            print(f"{name:>8} {summary[name]['rmse']:>9.5f} "
                  f"{summary[name]['mae']:>9.5f} "
                  f"{summary[name]['maxae']:>9.5f}")
        with open(TABLES / "benchmark_reduced.csv", "w") as f:
            f.write("r,q,sigma,T,kind,S,oracle,spread,ppa,spiral,baw\n")
            for x in bench:
                f.write(f"{x['r']},{x['q']},{x['sigma']},{x['T']},"
                        f"{x['kind']},{x['S']},{x['oracle']:.6f},"
                        f"{x['spread']:.6f},{x['ppa']:.6f},"
                        f"{x['spiral']:.6f},{x['baw']:.6f}\n")
        print("saved phase16_tables/benchmark_reduced.csv")
        worst_row = max(bench, key=lambda x: abs(x["ppa"] - x["oracle"]))
        print(f"worst PPA case: r={worst_row['r']} q={worst_row['q']} "
              f"sig={worst_row['sigma']} T={worst_row['T']} "
              f"{worst_row['kind']} S={worst_row['S']} "
              f"err={worst_row['ppa'] - worst_row['oracle']:+.5f}")
        """
    ),
    code(
        r"""
        fig, ax = plt.subplots(figsize=(5.6, 3.4))
        names = ["PPA", "Phase-15 spiral", "BAW"]
        keys = ("ppa", "spiral", "baw")
        xs = np.arange(3)
        ax.bar(xs - 0.27, [summary[k]["rmse"] for k in keys], width=0.27,
               label="RMSE")
        ax.bar(xs, [summary[k]["mae"] for k in keys], width=0.27,
               label="MAE")
        ax.bar(xs + 0.27, [summary[k]["maxae"] for k in keys], width=0.27,
               label="MaxAE")
        ax.set_xticks(xs)
        ax.set_xticklabels(names)
        ax.set_ylabel("error vs tree oracle")
        ax.set_title("Reduced-grid benchmark (Phase 16)")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f03_benchmark.png", dpi=160)
        plt.close(fig)
        print("saved f03_benchmark.png")
        """
    ),
    md(
        r"""
        ## 5. Structural finding: the perpetual approach is not exponential

        Fits of \(\ln|b(\tau)-b_\infty|\) on successively later windows show
        a *decreasing* effective rate (no pure exponential), most extremely
        at \(r=q\) where the linearized boundary-memory kernel is
        proportional to \(r-q\) and degenerates. This is why long-maturity
        pricing uses perpetual pinning rather than an extrapolated decay.
        """
    ),
    code(
        r"""
        decay = {}
        for r_, q_, kind, tag in ((0.05, 0.05, "put", "r=q"),
                                  (0.07, 0.03, "put", "r>q")):
            taus, bvals = p15.solve_boundary(K, r_, q_, SIG, 16.0, kind,
                                             n_grid=500, n_quad=48,
                                             delta=1e-9, cluster=1.0)
            _, binf = p15.perpetual_american(K, K, r_, q_, SIG, kind)
            rows = []
            for lo_t in (2.0, 6.0, 10.0):
                sel = taus >= lo_t
                d = bvals[sel] - binf
                ok = np.abs(d) > 1e-9
                A = np.vstack([np.ones(ok.sum()), taus[sel][ok]]).T
                coef = np.linalg.lstsq(A, np.log(np.abs(d[ok])),
                                       rcond=None)[0]
                rows.append((lo_t, -coef[1]))
            decay[tag] = (taus, bvals, binf, rows)
            print(f"{tag}: " + " ".join(f"[{lo:.0f},16]:{k:.4f}"
                                        for lo, k in rows))

        fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
        for ax, (tag, color) in zip(axes, (("r=q", "tab:blue"),
                                           ("r>q", "tab:red"))):
            taus, bvals, binf, rows = decay[tag]
            ax.semilogy(taus, np.abs(bvals - binf), color=color, lw=1.5)
            ax.set_xlabel(r"time to maturity $\tau$")
            ax.set_ylabel(r"$|b(\tau)-b_\infty|$")
            ax.set_title(f"perpetual approach ({tag})")
        fig.tight_layout()
        fig.savefig(FIGURES / "f04_decay.png", dpi=160)
        plt.close(fig)
        print("saved f04_decay.png")
        """
    ),
    md(
        r"""
        ## 6. Tier B probe: eliminating the collocation solves

        Can the spiral's collocated parameters
        \((\kappa_1,\kappa_2,h_{\log},h_{\mathrm{root}})\) be replaced
        by explicit surfaces over \((r,q,\sigma,T)\), removing even the
        scalar solves? We fit 13-term quadratic feature surfaces per
        parameter and per kind on the reduced grid, then price
        end-to-end against the oracle. Measured degradation below —
        documented as an open direction (likely needs \(T\)-band
        partitioning or richer bases); the PPA collocation remains the
        operative recipe.
        """
    ),
    code(
        r"""
        def features(r_, q_, sig_, T_):
            d = r_ - q_
            return np.array([1.0, sig_, d, T_, sig_ ** 2, d ** 2, T_ ** 2,
                             sig_ * T_, d * T_, sig_ * d, sig_ ** 2 * T_,
                             sig_ * T_ ** 2, d * sig_ * T_])

        cfgs = [(r_, q_, sig_, T_, kind)
                for r_, q_, sig_, T_, kind in grid]
        prm = {}
        for c in cfgs:
            r_, q_, sig_, T_, kind = c
            k1, k2, el, er, _ = p15.spiral_collocation(K, r_, q_, sig_,
                                                       T_, kind)
            s_phi = 1.0 if kind == "call" else -1.0
            prm[c] = (k1, k2, s_phi * el, s_phi * er)  # magnitudes
        coefs = {kind: [] for kind in ("call", "put")}
        fit_rms = []
        for kind in ("call", "put"):
            sub = [c for c in cfgs if c[4] == kind]
            F = np.vstack([features(*c[:4]) for c in sub])
            ks = np.array([prm[c] for c in sub])
            for j in range(4):
                coef, *_ = np.linalg.lstsq(F, ks[:, j], rcond=None)
                coefs[kind].append(coef)
                fit_rms.append(float(np.sqrt(np.mean(
                    (F @ coef - ks[:, j]) ** 2))))
        print("surface fit RMS (k1,k2,h_log,h_root per kind): "
              + " ".join(f"{v:.3f}" for v in fit_rms))

        # end-to-end: surface-driven spiral prices vs oracle
        d_col = []
        d_surf = []
        for c in cfgs:
            r_, q_, sig_, T_, kind = c
            k1, k2, el, er = prm[c]
            s_phi = 1.0 if kind == "call" else -1.0
            f = features(*c[:4])
            k1s, k2s, hls, hrs = [float(f @ coefs[kind][j])
                                  for j in range(4)]
            for S in (90.0, 100.0, 110.0):
                oracle, _ = p15.tree_oracle(S, K, r_, q_, sig_, T_, kind,
                                            Ns=(8000,))
                pc, *_ = p15.american_spiral(S, K, r_, q_, sig_, T_, kind,
                                             params=(k1, k2, s_phi * el,
                                                     s_phi * er))
                ps, *_ = p15.american_spiral(S, K, r_, q_, sig_, T_, kind,
                                             params=(k1s, k2s, s_phi * hls,
                                                     s_phi * hrs))
                d_col.append(pc - oracle)
                d_surf.append(ps - oracle)
        d_col = np.array(d_col)
        d_surf = np.array(d_surf)
        tierb = {
            "collocated_rmse": float(np.sqrt(np.mean(d_col ** 2))),
            "surface_rmse": float(np.sqrt(np.mean(d_surf ** 2))),
            "surface_maxae": float(np.max(np.abs(d_surf))),
        }
        print(f"end-to-end vs oracle: collocated RMSE="
              f"{tierb['collocated_rmse']:.5f}  surface RMSE="
              f"{tierb['surface_rmse']:.5f}  surface MaxAE="
              f"{tierb['surface_maxae']:.5f}")
        """
    ),
    md("## 7. Evidence summary"),
    code(
        r"""
        # timing: PPA solve + closed-form price vs reference solve
        t0 = time.time()
        for _ in range(3):
            ku, kv = p16.solve_ppa_pinned(K, R, Q, SIG, T, "put", m=10)
            p16.american_ppa_from_knots(100.0, T, ku, kv, K, R, Q, SIG,
                                        "put")
        ppa_time = (time.time() - t0) / 3
        results = {
            "occupation_J_worst_error": worst,
            "affine_eep_worst_error": worst,
            "benchmark_reduced": summary,
            "perpetual_approach_rates": {
                tag: [{"window_lo": lo, "kappa_eff": k} for lo, k in rows]
                for tag, (_, _, _, rows) in decay.items()},
            "tierb_probe": tierb,
            "ppa_wall_seconds": ppa_time,
            "runtime_seconds": time.time() - started,
        }
        with open(TABLES / "phase16_summary.json", "w") as f:
            json.dump(results, f, indent=2)
        print(json.dumps(results, indent=2))
        print(f"notebook runtime: {results['runtime_seconds']:.1f}s")
        """
    ),
]

nb = nbf.v4.new_notebook()
nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python",
                   "name": "python3"},
    "language_info": {"name": "python", "version": "3.12"},
}

out = Path(__file__).parent / "phase16_closedform.ipynb"
nbf.write(nb, out)
print(f"wrote {out}")
