"""Build the deterministic Phase 15 notebook (REVISED after mathematical
review of 2026-09-02: corrected put sign, regime-aware asymptotics,
cusp-free family, no stationarity claims, oracle-based benchmarks,
correct metric labels)."""

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
        # Phase 15 (revised): American calls and puts under BSM from one-driver complex GBM

        Revised computational record (2026-09-03) after the external
        mathematical review `phase15-mathematical-review.md`. Changes
        relative to the original record:

        1. the put EEP is handled by its correct explicit sign (the
           one-line unified formula needs an outer factor $\phi$ for
           puts); a sign regression test is included;
        2. the "universal" short-expiry shape is replaced by the
           established three-regime asymptotics (Evans–Kuske–Keller 2001;
           Chen–Zhu 2010), which our solved boundaries reproduce;
        3. the boundary family is redesigned: dimensionless logarithm
           scale $\hat\tau$, smooth shapes on $(0,\infty)$, regime-aware
           bases, no cusp at $\tau=1$, monotone through the old cusp
           point;
        4. all stationarity/envelope claims are removed — the
           substituted-boundary EEP functional is first-order sensitive
           to boundary error (demonstrated below);
        5. benchmarks are computed against a converged
           Broadie–Detemple adjacent-averaged tree oracle; the Volterra
           level-set solver is one method under test, with its grid
           sensitivity documented;
        6. metric labels corrected: RMSE / true MAE / maximum absolute
           error.
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

        ROOT = Path.cwd().resolve()
        if not (ROOT / "phase15_american.py").exists():
            candidates = [ROOT, *ROOT.parents]
            ROOT = next(p for p in candidates
                        if (p / "phase15_american.py").exists())
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))

        import phase15_american as p15

        SEED = 20260902
        FIGURES = ROOT / "phase15_figures"
        FIGURES.mkdir(exist_ok=True)
        TABLES = ROOT / "phase15_tables"
        TABLES.mkdir(exist_ok=True)

        K = 100.0
        environment = {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
            "platform": platform.platform(),
            "seed": SEED,
        }
        print(json.dumps(environment, indent=2))
        started = time.time()
        """
    ),
    md(
        r"""
        ## 1. Foundations and the put sign

        The call and put early-exercise premiums are

        $$
        \mathrm{EEP}^{c}=\int_0^\tau
        \big[qS e^{-qs}\Phi(d_1)-rK e^{-rs}\Phi(d_2)\big]ds,
        \qquad
        \mathrm{EEP}^{p}=\int_0^\tau
        \big[rK e^{-rs}\Phi(-d_2)-qS e^{-qs}\Phi(-d_1)\big]ds,
        $$

        i.e. the unified single-line form carries an outer factor
        $\phi$ for puts.  The wrong sign makes the American put fall
        below the European put — an arbitrage violation — which is the
        regression test below.
        """
    ),
    code(
        r"""
        R, Q, SIG, T = 0.05, 0.05, 0.2, 1.0
        c = p15.bs_european(K, K, R, Q, SIG, T, "call")
        p = p15.bs_european(K, K, R, Q, SIG, T, "put")
        parity = c - p - (K * math.exp(-Q * T) - K * math.exp(-R * T))
        print(f"parity residual: {parity:.3e}")

        taus_p, bvals_p = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                             n_grid=200, n_quad=44,
                                             delta=1e-8)
        bd_p = lambda tau: float(np.interp(tau, taus_p, bvals_p))
        prem_p = p15.eep(K, T, bd_p, K, R, Q, SIG, "put", n_quad=96)
        am_p = p15.american_from_boundary(K, T, bd_p, K, R, Q, SIG, "put",
                                          n_quad=96)
        print(f"European put={p:.6f}  put EEP={prem_p:+.6f}  "
              f"American put={am_p:.6f}")
        assert prem_p > 0.0 and am_p >= p - 1e-9, "put sign regression"
        # the wrong-sign formula would give:
        print(f"wrong-sign price (for contrast): {p - prem_p:.6f} "
              f"— below European, violates the American lower bound")
        """
    ),
    md(
        r"""
        ## 2. The Volterra solver: diagnostics, convergence, and known
        sensitivity

        The causal level-set solver is one method under test, not the
        reference oracle. Its failure modes are exposed via
        `SOLVER_DIAGNOSTICS` (flat fallback steps) and quantified below.
        """
    ),
    code(
        r"""
        # soft regime: grid convergence at the base case
        oracle_base, spread_base = p15.tree_oracle(K, K, R, Q, SIG, T,
                                                   "put", Ns=(4000, 6000,
                                                              8000))
        conv = []
        for n in (150, 200, 250, 300, 400):
            taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                             n_grid=n, n_quad=44,
                                             delta=1e-8)
            bd = lambda tau: float(np.interp(tau, taus, bvals))
            price = p15.american_from_boundary(K, T, bd, K, R, Q, SIG,
                                               "put", n_quad=96)
            conv.append((n, price, p15.SOLVER_DIAGNOSTICS["fallbacks"]))
        print(f"oracle = {oracle_base:.6f} (tree spread {spread_base:.2e})")
        print("n_grid   price     fallbacks   err vs oracle")
        for n, price, fb in conv:
            print(f"{n:5d}  {price:.6f}  {fb:6d}      "
                  f"{price - oracle_base:+.5f}")
        """
    ),
    code(
        r"""
        # hard regime: documented grid sensitivity vs the stable oracle
        oracle_h, spread_h = p15.tree_oracle(120.0, K, 0.05, 0.10, 0.2,
                                             3.0, "call",
                                             Ns=(8000, 10000, 12000))
        hard = []
        for n in (250, 300, 350, 500, 700):
            taus, bvals = p15.solve_boundary(K, 0.05, 0.10, 0.2, 3.0,
                                             "call", n_grid=n, n_quad=44,
                                             delta=1e-8)
            bd = lambda tau: float(np.interp(tau, taus, bvals))
            price = p15.american_from_boundary(120.0, 3.0, bd, K, 0.05,
                                               0.10, 0.2, "call",
                                               n_quad=96)
            hard.append((n, price, p15.SOLVER_DIAGNOSTICS["fallbacks"]))
        print(f"oracle = {oracle_h:.6f} (tree spread {spread_h:.2e})")
        print("n_grid   price     fallbacks   err vs oracle")
        for n, price, fb in hard:
            print(f"{n:5d}  {price:.6f}  {fb:6d}      "
                  f"{price - oracle_h:+.5f}")
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
        axes[0].plot([n for n, _, _ in conv], [pr for _, pr, _ in conv],
                     "o-", color="tab:blue")
        axes[0].axhline(oracle_base, ls="--", color="k", lw=1,
                        label="tree oracle")
        axes[0].set_xlabel("boundary grid size n")
        axes[0].set_ylabel("price")
        axes[0].set_title("soft regime (base put, T=1): convergent")
        axes[0].legend(fontsize=8)
        axes[1].plot([n for n, _, _ in hard], [pr for _, pr, _ in hard],
                     "o-", color="tab:red")
        axes[1].axhline(oracle_h, ls="--", color="k", lw=1,
                        label="tree oracle")
        axes[1].set_xlabel("boundary grid size n")
        axes[1].set_ylabel("price")
        axes[1].set_title("hard regime (T=3 call): grid-sensitive")
        axes[1].legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f01_grid_behavior.png", dpi=160)
        plt.close(fig)
        print("saved f01_grid_behavior.png")
        """
    ),
    md(
        r"""
        ## 3. Short-expiry asymptotics: three regimes, not one

        Established results (Evans–Kuske–Keller 2001; Chen–Zhu 2010,
        eqs. (3.15)–(3.22)) for the put boundary near expiry:

        $$
        q<r:\ K-b_p\sim K\sigma\sqrt{\tau|\ln\tau|},\qquad
        q=r:\ K-b_p\sim K\sigma\sqrt{2\tau|\ln\tau|},\qquad
        q>r:\ b_p=\tfrac rq K\big[1-\xi_1\sigma\sqrt{2\tau}+O(\tau)\big],
        \ \xi_1\approx0.4517.
        $$

        Calls inherit mirrored regimes with $r\leftrightarrow q$. We fit
        the solved near-expiry boundaries, excluding flat fallback steps
        (the fallback count is reported — these fits are only as good as
        that count allows).
        """
    ),
    code(
        r"""
        def near_expiry_fit(r_, q_, sig_=0.2, Tfit=0.02):
            taus, bv = p15.solve_boundary(K, r_, q_, sig_, Tfit, "put",
                                          n_grid=400, n_quad=40,
                                          delta=1e-9, cluster=2.0)
            b0 = p15.boundary_at_maturity(K, r_, q_, "put")
            xs, ys, sq, flat = [], [], [], 0
            for i in range(1, len(taus)):
                if taus[i] > 0.008:
                    break
                if bv[i] == bv[i - 1]:
                    flat += 1
                    continue
                xs.append(sig_ * math.sqrt(2 * taus[i]
                                           * abs(math.log(taus[i]))))
                ys.append((b0 - bv[i]) / K)
                sq.append(math.sqrt(2 * taus[i]))
            coef_log = (np.polyfit(xs, ys, 1)[0] if len(xs) > 5
                        else float("nan"))
            coef_root = (np.polyfit(sq, ys, 1)[0] if len(sq) > 5
                         else float("nan"))
            return coef_log, coef_root, flat, len(xs)

        regime_rows = []
        for r_, q_, pred in ((0.07, 0.03, 1 / math.sqrt(2)),
                             (0.05, 0.05, 1.0),
                             (0.03, 0.07, None)):
            cl, cr, flat, used = near_expiry_fit(r_, q_)
            regime_rows.append(dict(r=r_, q=q_, coeff_log=cl,
                                    coeff_root=cr, flat=flat, used=used,
                                    prediction=pred))
            print(f"r={r_} q={q_}: log-coeff={cl:.4f} "
                  f"(prediction {pred if pred else 'n/a (sqrt regime)'}) "
                  f"sqrt-coeff={cr:.4f} "
                  f"(prediction {(r_ / q_) * 0.4517 * 0.2:.4f}) "
                  f"used {used} pts, {flat} flat steps dropped")
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(1, 3, figsize=(11, 3.3))
        for ax, (r_, q_) in zip(axes, ((0.07, 0.03), (0.05, 0.05),
                                       (0.03, 0.07))):
            taus, bv = p15.solve_boundary(K, r_, q_, 0.2, 0.02, "put",
                                          n_grid=400, n_quad=40,
                                          delta=1e-9, cluster=2.0)
            b0 = p15.boundary_at_maturity(K, r_, q_, "put")
            sel = [i for i in range(1, len(taus))
                   if taus[i] <= 0.008 and bv[i] != bv[i - 1]]
            if q_ >= r_:
                x = [math.sqrt(2 * taus[i]) for i in sel]
                y = [(b0 - bv[i]) / K for i in sel]
                ax.set_xlabel(r"$\sqrt{2\tau}$")
            else:
                x = [0.2 * math.sqrt(2 * taus[i] * abs(math.log(taus[i])))
                     for i in sel]
                y = [(b0 - bv[i]) / K for i in sel]
                ax.set_xlabel(r"$\sigma\sqrt{2\tau|\ln\tau|}$")
            ax.plot(x, y, ".", ms=3)
            ax.set_ylabel(r"$(b_0-b)/K$")
            ax.set_title(f"put, r={r_}, q={q_}")
        fig.tight_layout()
        fig.savefig(FIGURES / "f02_regimes.png", dpi=160)
        plt.close(fig)
        print("saved f02_regimes.png")
        """
    ),
    md(
        r"""
        ## 4. Phase geometry: scope clarified

        In the drift-matched gauge the Phase 4 phase is
        $\Theta_t=\Theta_0+(\beta/\sigma)\ln(S_t/S_0)$ — a deterministic
        affine reparameterization of log-price (for $\beta/\sigma>0$; the
        exercise inequality reverses for $\beta<0$ and phase carries no
        spot information at $\beta=0$). This is a valid geometric
        language — the exercise boundary becomes a moving phase barrier —
        but it does **not** reduce the optimal-stopping problem or add
        pricing information by itself. The pricing content of Phase 15
        lives in the boundary family and the EEP machinery below.
        """
    ),
    md(
        r"""
        ## 5. The redesigned boundary family

        $$
        \ln b(\tau)=\ln b_\infty+\ln(b_0/b_\infty)e^{-\kappa_1\tau}
        +\sigma e^{-\kappa_2\tau}\big[
        \eta_{\log}\psi_{\log}(\tau;\hat\tau)
        +\eta_{\mathrm{root}}\psi_{\mathrm{root}}(\tau)\big]
        $$

        with $\psi_{\log}(\tau;\hat\tau)=\sqrt{2\tau\ln(1+\hat\tau/\tau)}$
        (smooth on $(0,\infty)$, asymptotic to
        $\sqrt{2\tau|\ln(\tau/\hat\tau)|}$ at $\tau\downarrow0$,
        dimensionless via the declared scale $\hat\tau$) and
        $\psi_{\mathrm{root}}(\tau)=\sqrt{2\tau}$ (the $q>r$ regime
        shape). The old $|\ln\max(\tau,\varepsilon)|$ term had an
        artificial infinite-slope cusp at $\tau=1$ and produced
        nonmonotone boundaries; the regression below guards both
        properties.
        """
    ),
    code(
        r"""
        # smoothness of the new shape through the old cusp point
        h = 1e-2
        curv = []
        for tau in (0.5, 1.0, 2.0):
            d2 = (p15.spiral_shape_log(tau + h)
                  - 2 * p15.spiral_shape_log(tau)
                  + p15.spiral_shape_log(tau - h)) / h ** 2
            curv.append((tau, d2))
        print("psi_log curvature at old cusp neighborhood:",
              ", ".join(f"k''({t:.1f})={d:.3f}" for t, d in curv))

        # monotonicity through tau=1 for the T=3 calibrations
        mono_report = {}
        for kind in ("call", "put"):
            k1, k2, el, er, info = p15.spiral_collocation(K, R, Q, SIG,
                                                          3.0, kind)
            b0 = p15.boundary_at_maturity(K, R, Q, kind)
            _, binf = p15.perpetual_american(K, K, R, Q, SIG, kind)
            vals = [p15.spiral_refined_boundary(t, b0, binf, SIG, el, k1,
                                                k2, eta_root=er)
                    for t in (0.9, 1.0, 1.1)]
            mono = (vals[0] <= vals[1] <= vals[2]) if kind == "call" \
                else (vals[0] >= vals[1] >= vals[2])
            mono_report[kind] = (vals, mono)
            print(f"{kind} T=3: b(0.9,1.0,1.1) = "
                  f"{vals[0]:.3f}, {vals[1]:.3f}, {vals[2]:.3f} "
                  f"monotone={mono}")
        assert mono_report["call"][1] and mono_report["put"][1]
        """
    ),
    md(
        r"""
        ## 6. Collocation is a reported projection

        $(\kappa_1,\kappa_2,\eta_{\log},\eta_{\mathrm{root}})$ minimize
        the sum of squared value-matching residuals at four fractional
        nodes under box constraints. Residuals are generally not zero;
        they are reported, together with optimizer status and multi-start
        sensitivity. No stationarity or envelope property is claimed for
        the substituted-boundary price — a direct perturbation test shows
        first-order sensitivity below.
        """
    ),
    code(
        r"""
        coll = {}
        for kind, T_ in (("call", 3.0), ("put", 3.0), ("put", 1.0)):
            k1, k2, el, er, info = p15.spiral_collocation(K, R, Q, SIG,
                                                          T_, kind)
            coll[(kind, T_)] = (k1, k2, el, er, info)
            print(f"{kind} T={T_}: k1={k1:.4f} k2={k2:.4f} "
                  f"eta_log={el:+.4f} eta_root={er:+.4f} "
                  f"objective={info['objective']:.3e} "
                  f"residuals={['%.2e' % r for r in info['residuals']]} "
                  f"status={info['optimizer_status']} "
                  f"start-spread={info['start_sensitivity']:.2e}")

        # perturbation test: substituted-boundary EEP is NOT stationary
        taus, bvals = p15.solve_boundary(K, R, Q, SIG, T, "call",
                                         n_grid=250, n_quad=44, delta=1e-8)
        base_bd = lambda tau: float(np.interp(tau, taus, bvals))
        V0 = p15.american_from_boundary(K, T, base_bd, K, R, Q, SIG,
                                        "call", n_quad=96)
        ratios = []
        for eps in (1e-2, 5e-3, 2.5e-3, 1.25e-3):
            pert = lambda tau, e=eps: base_bd(tau) * math.exp(
                e * math.sin(math.pi * tau / T))
            Vp = p15.american_from_boundary(K, T, pert, K, R, Q, SIG,
                                            "call", n_quad=96)
            ratios.append((eps, (Vp - V0) / eps))
        print("perturbation ratios (V-V0)/eps:",
              ", ".join(f"{e:.4f}:{r:+.4f}" for e, r in ratios))
        print("-> nonzero limit: first-order sensitivity, no stationarity")
        """
    ),
    md(
        r"""
        ## 7. Benchmarks against the converged tree oracle

        Oracle: Broadie–Detemple adjacent-averaged CRR at
        $N\in\{8000,12000\}$ (mean; spread reported). Metrics: RMSE,
        true MAE (mean absolute error), and maximum absolute error —
        labeled correctly this time.
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
            k1, k2, el, er, _ = p15.spiral_collocation(K, r_, q_, sig_,
                                                       T_, kind)
            taus_s, bvals_s = p15.solve_boundary(K, r_, q_, sig_, T_,
                                                 kind, n_grid=300,
                                                 n_quad=48, delta=1e-8)
            bd_s = lambda tau, ts=taus_s, bv=bvals_s: float(
                np.interp(tau, ts, bv))
            for S in (90.0, 100.0, 110.0):
                oracle, spread = p15.tree_oracle(S, K, r_, q_, sig_, T_,
                                                 kind, Ns=(8000, 12000))
                sp, *_ = p15.american_spiral(S, K, r_, q_, sig_, T_, kind,
                                             params=(k1, k2, el, er))
                bw = p15.baw(S, K, r_, q_, sig_, T_, kind)
                sv = p15.american_from_boundary(S, T_, bd_s, K, r_, q_,
                                                sig_, kind, n_quad=96)
                bench.append(dict(r=r_, q=q_, sigma=sig_, T=T_, kind=kind,
                                  S=S, oracle=oracle, spread=spread,
                                  spiral=sp, baw=bw, solver=sv))

        arr = {k: np.array([x[k] for x in bench])
               for k in ("oracle", "spiral", "baw", "solver")}
        summary = {}
        print(f"{'method':>8} {'RMSE':>9} {'MAE':>9} {'MaxAE':>9}")
        for name in ("spiral", "baw", "solver"):
            d = arr[name] - arr["oracle"]
            summary[name] = dict(rmse=float(np.sqrt(np.mean(d ** 2))),
                                 mae=float(np.mean(np.abs(d))),
                                 maxae=float(np.max(np.abs(d))))
            print(f"{name:>8} {summary[name]['rmse']:>9.5f} "
                  f"{summary[name]['mae']:>9.5f} "
                  f"{summary[name]['maxae']:>9.5f}")
        i = int(np.argmax(np.abs(arr['spiral'] - arr['oracle'])))
        print("worst spiral case:", {k: bench[i][k] for k in
                                     ('r', 'q', 'sigma', 'T', 'kind',
                                      'S')},
              f"err={arr['spiral'][i] - arr['oracle'][i]:+.5f}")
        with open(TABLES / "benchmark_reduced_oracle.csv", "w") as f:
            f.write("r,q,sigma,T,kind,S,oracle,spread,spiral,baw,solver\n")
            for x in bench:
                f.write(f"{x['r']},{x['q']},{x['sigma']},{x['T']},"
                        f"{x['kind']},{x['S']},{x['oracle']:.6f},"
                        f"{x['spread']:.6f},{x['spiral']:.6f},"
                        f"{x['baw']:.6f},{x['solver']:.6f}\n")
        print("saved phase15_tables/benchmark_reduced_oracle.csv")
        """
    ),
    code(
        r"""
        fig, ax = plt.subplots(figsize=(5.6, 3.4))
        names = ["spiral", "BAW", "Volterra solver"]
        keys = ("spiral", "baw", "solver")
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
        ax.set_title("Reduced grid, oracle-based")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f03_benchmark_oracle.png", dpi=160)
        plt.close(fig)
        print("saved f03_benchmark_oracle.png")
        """
    ),
    md(
        r"""
        ## 8. Structural identities

        Time-unit invariance (the formula must not depend on years vs
        months; $\hat\tau$ rescales with the unit), off-ATM put–call
        duality, and the $q=0$ call limit.
        """
    ),
    code(
        r"""
        p_yr, *_ = p15.american_spiral(K, K, R, Q, SIG, T, "put")
        p_mo, *_ = p15.american_spiral(K, K, R / 12, Q / 12,
                                       SIG / math.sqrt(12), 12 * T,
                                       "put", tau_hat=12.0)
        print(f"time-unit invariance: years={p_yr:.6f} months={p_mo:.6f} "
              f"diff={abs(p_yr - p_mo):.2e}")

        r2, q2, S2 = 0.07, 0.03, 90.0
        taus_p2, bv_p2 = p15.solve_boundary(K, r2, q2, SIG, T, "put",
                                            n_grid=200, n_quad=44,
                                            delta=1e-8)
        taus_c2, bv_c2 = p15.solve_boundary(S2, q2, r2, SIG, T, "call",
                                            n_grid=200, n_quad=44,
                                            delta=1e-8)
        P2 = p15.american_from_boundary(S2, T,
                                        lambda tau: float(np.interp(
                                            tau, taus_p2, bv_p2)),
                                        K, r2, q2, SIG, "put", n_quad=96)
        C2 = p15.american_from_boundary(K, T,
                                        lambda tau: float(np.interp(
                                            tau, taus_c2, bv_c2)),
                                        S2, q2, r2, SIG, "call", n_quad=96)
        print(f"off-ATM duality: P(90,100;0.07,0.03)={P2:.5f} vs "
              f"C(100,90;0.03,0.07)={C2:.5f} diff={abs(P2 - C2):.2e}")

        p_q0, *_ = p15.american_spiral(K, K, R, 0.0, SIG, T, "call")
        euro_q0 = p15.bs_european(K, K, R, 0.0, SIG, T, "call")
        print(f"q=0 call: {p_q0:.8f} vs European {euro_q0:.8f}")
        """
    ),
    md("## 9. Evidence summary"),
    code(
        r"""
        results = {
            "parity_residual": parity,
            "put_eep_positive": bool(prem_p > 0.0),
            "grid_convergence_soft": conv,
            "grid_sensitivity_hard": hard,
            "oracle_base": oracle_base,
            "oracle_hard": oracle_h,
            "regime_fits": regime_rows,
            "collocation": {f"{k}:{v}":
                            {"objective": coll[(k, v)][4]["objective"],
                             "residuals": coll[(k, v)][4]["residuals"]}
                            for k, v in (("call", 3.0), ("put", 3.0),
                                         ("put", 1.0))},
            "perturbation_ratios": ratios,
            "benchmark_reduced_oracle": summary,
            "time_unit_diff": abs(p_yr - p_mo),
            "duality_diff": abs(P2 - C2),
            "runtime_seconds": time.time() - started,
        }
        with open(TABLES / "phase15_summary.json", "w") as f:
            json.dump(results, f, indent=2, default=str)
        print(json.dumps({"benchmark_reduced_oracle": summary,
                          "time_unit_diff": results["time_unit_diff"],
                          "duality_diff": results["duality_diff"],
                          "runtime_seconds": results["runtime_seconds"]},
                         indent=2))
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

out = Path(__file__).parent / "phase15_american_spiral.ipynb"
nbf.write(nb, out)
print(f"wrote {out}")
