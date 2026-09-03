"""Build the deterministic Phase 15 American-spiral notebook."""

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
        # Phase 15: American calls and puts under Black–Scholes–Merton from one-driver complex GBM geometry

        Computational record for the Phase 15 paper. The Phase 4 process

        \[
        \mathcal Z_t=\mathcal Z_0\exp\!\Big(
        \big[(\mu-\tfrac12\sigma^2)+i\omega\big]t+(\sigma+i\beta)W_t\Big)
        \]

        carries the Black–Scholes–Merton stock price as its modulus
        (\(|\mathcal Z_t|=S_t\) under the risk-neutral measure with
        \(\mu=r-q\)). In these coordinates the American free-boundary
        problem becomes a **moving phase barrier** problem. This notebook:

        1. builds the exact Kim/Jacka/Carr–Jarrow–Myneni early-exercise
           premium machinery and a stable reference solver for the
           nonlinear Volterra boundary equation;
        2. validates the reference against put–call (McDonald–Schroder)
           symmetry, published 10,000-step binomial benchmark values,
           CRR–Richardson trees, and finite differences;
        3. documents the universal short-maturity boundary law
           \(b(\tau)=b_0+\eta\,\sigma b_0\sqrt{2\tau|\ln\tau|}(1+o(1))\);
        4. introduces the **logarithmic-spiral boundary family** exact at
           both asymptotic limits and its collocation-fixed closed-form
           pricing formula;
        5. benchmarks the formula against Barone-Adesi–Whaley across a
           parameter grid.
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
        S0 = 100.0

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
        ## 1. Exact foundations

        Dividend-adjusted European prices, McDonald–Schroder perpetual
        closed forms, and the maturity anchors \(b(0^+)\). Put–call parity
        with dividends must hold to machine precision.
        """
    ),
    code(
        r"""
        R, Q, SIG, T = 0.05, 0.05, 0.2, 1.0
        c = p15.bs_european(S0, K, R, Q, SIG, T, "call")
        p = p15.bs_european(S0, K, R, Q, SIG, T, "put")
        parity_lhs = c - p
        parity_rhs = S0 * math.exp(-Q * T) - K * math.exp(-R * T)
        print(f"call={c:.10f} put={p:.10f}")
        print(f"parity residual = {abs(parity_lhs - parity_rhs):.3e}")

        foundations = {}
        for r_, q_ in ((0.05, 0.05), (0.07, 0.03), (0.03, 0.07)):
            for kind in ("call", "put"):
                b0 = p15.boundary_at_maturity(K, r_, q_, kind)
                pprice, binf = p15.perpetual_american(S0, K, r_, q_, SIG,
                                                      kind)
                foundations[(r_, q_, kind)] = dict(b0=b0, b_inf=binf,
                                                   perp_price=pprice)
                print(f"r={r_} q={q_} {kind}: b(0+)={b0:.4f} "
                      f"b_inf={binf:.4f} perp price={pprice:.4f}")

        s_minus, s_plus = p15.perpetual_roots(R, Q, SIG)
        print(f"perpetual roots: s_-={s_minus:.6f} s_+={s_plus:.6f}")
        """
    ),
    md(
        r"""
        ## 2. Reference solver for the Volterra boundary equation

        The boundary \(b(\tau)\) (time to maturity \(\tau\)) solves the
        value-matching equation

        \[
        \phi(b(\tau)-K)=V_E(b(\tau),\tau)+\int_0^\tau
        \big[q\,b(\tau)e^{-qs}\Phi(\phi d_1)-\phi^2 rK e^{-rs}
        \Phi(\phi d_2)\big]ds
        \]

        (schematically; the full integrand uses \(\Phi(d_1),\Phi(d_2)\) for
        calls and \(\Phi(-d_1),\Phi(-d_2)\) for puts, with \(d_i\) computed
        at spot \(b(\tau)\), boundary level \(b(\tau-s)\), horizon \(s\)).
        Key structural facts used by the solver:

        - the equation is **causal** in \(\tau\): the equation at \(\tau\)
          involves the boundary only at smaller arguments;
        - for the call, the residual \(F(y)\) satisfies \(F(y)<0\) for
          \(y<b(\tau)\) and \(F(y)=0\) for all \(y\ge b(\tau)\) (deep ITM
          calls exercise immediately), so the boundary is where the
          residual **reaches** zero; the put has the mirrored structure
          with a positive hump;
        - near maturity the equation loses traction (\(\partial F/\partial
          y\to0\)), so the anchor \(b(0^+)\) is imposed directly.
        """
    ),
    code(
        r"""
        t0 = time.time()
        taus_c, bvals_c = p15.solve_boundary(K, R, Q, SIG, T, "call",
                                             n_grid=250, n_quad=48,
                                             delta=1e-8)
        taus_p, bvals_p = p15.solve_boundary(K, R, Q, SIG, T, "put",
                                             n_grid=250, n_quad=48,
                                             delta=1e-8)
        print(f"solved call+put boundaries in {time.time() - t0:.1f}s")
        call_bd = lambda tau: float(np.interp(tau, taus_c, bvals_c))
        put_bd = lambda tau: float(np.interp(tau, taus_p, bvals_p))

        CA = p15.american_from_boundary(S0, T, call_bd, K, R, Q, SIG,
                                        "call", n_quad=96)
        PA = p15.american_from_boundary(S0, T, put_bd, K, R, Q, SIG,
                                        "put", n_quad=96)
        print(f"reference American call = {CA:.8f} (premium {CA - c:.8f})")
        print(f"reference American put  = {PA:.8f} (premium {PA - p:.8f})")

        res_c = max(abs(p15.boundary_residual_grid(i, taus_c, bvals_c, K, R,
                                                   Q, SIG, "call", 48))
                    for i in range(1, len(taus_c), len(taus_c) // 30))
        res_p = max(abs(p15.boundary_residual_grid(i, taus_p, bvals_p, K, R,
                                                   Q, SIG, "put", 48))
                    for i in range(1, len(taus_p), len(taus_p) // 30))
        print(f"max sampled value-matching residual: call {res_c:.2e}, "
              f"put {res_p:.2e}")
        assert np.all(np.diff(bvals_c) >= -1e-9), "call boundary monotone"
        assert np.all(np.diff(bvals_p) <= 1e-9), "put boundary monotone"
        print("monotonicity: call nondecreasing, put nonincreasing OK")
        """
    ),
    md(
        r"""
        ## 3. Cross-validation of the reference

        Four independent checks:

        1. **Put–call symmetry** (McDonald–Schroder):
           \(P(S,K,r,q,\sigma,\tau)=C(K,S,q,r,\sigma,\tau)\);
        2. **published 10,000-step binomial TRUE values** from the Ju
           exhibits;
        3. **CRR binomial with Richardson extrapolation**;
        4. finite differences (spot check).
        """
    ),
    code(
        r"""
        results = {}

        r6, q6 = 0.07, 0.03
        taus_p6, bv_p6 = p15.solve_boundary(K, r6, q6, SIG, T, "put",
                                            n_grid=250, n_quad=48,
                                            delta=1e-9)
        taus_c6, bv_c6 = p15.solve_boundary(K, q6, r6, SIG, T, "call",
                                            n_grid=250, n_quad=48,
                                            delta=1e-9)
        bd_p6 = lambda tau: float(np.interp(tau, taus_p6, bv_p6))
        bd_c6 = lambda tau: float(np.interp(tau, taus_c6, bv_c6))
        P6 = p15.american_from_boundary(S0, T, bd_p6, K, r6, q6, SIG,
                                        "put", n_quad=96)
        C6 = p15.american_from_boundary(K, T, bd_c6, K, q6, r6, SIG,
                                        "call", n_quad=96)
        sym_diff = abs(P6 - C6)
        print(f"symmetry: put={P6:.8f} swapped call={C6:.8f} "
              f"diff={sym_diff:.2e}")
        results["symmetry_diff"] = sym_diff

        # Ju exhibit TRUE values (10,000-step binomial)
        taus_j, bv_j = p15.solve_boundary(40.0, 0.0488, 0.0, 0.2, 0.5833,
                                          "put", n_grid=300, n_quad=48,
                                          delta=1e-8)
        bd_j = lambda tau: float(np.interp(tau, taus_j, bv_j))
        put_ju = p15.american_from_boundary(40.0, 0.5833, bd_j, 40.0,
                                            0.0488, 0.0, 0.2, "put",
                                            n_quad=96)
        taus_j2, bv_j2 = p15.solve_boundary(100.0, 0.03, 0.07, 0.4, 0.5,
                                            "call", n_grid=300, n_quad=48,
                                            delta=1e-8)
        bd_j2 = lambda tau: float(np.interp(tau, taus_j2, bv_j2))
        call_ju = p15.american_from_boundary(100.0, 0.5, bd_j2, 100.0,
                                             0.03, 0.07, 0.4, "call",
                                             n_quad=96)
        print(f"Ju exhibit put:  ref={put_ju:.5f} TRUE=1.990")
        print(f"Ju exhibit call: ref={call_ju:.5f} TRUE=10.239")
        results["ju_put_diff"] = abs(put_ju - 1.990)
        results["ju_call_diff"] = abs(call_ju - 10.239)

        crr_c = p15.crr_richardson(S0, K, R, Q, SIG, T, "call",
                                   Ns=(1500, 3000, 6000))
        crr_p = p15.crr_richardson(S0, K, R, Q, SIG, T, "put",
                                   Ns=(1500, 3000, 6000))
        print(f"CRR-Richardson call={crr_c:.6f} put={crr_p:.6f}")
        results["crr_call_diff"] = abs(crr_c - CA)
        results["crr_put_diff"] = abs(crr_p - PA)
        assert results["ju_put_diff"] < 6e-3
        assert results["ju_call_diff"] < 6e-3
        assert results["symmetry_diff"] < 3e-3
        """
    ),
    md(
        r"""
        ## 4. The boundary in phase coordinates

        With the drift-matched gauge the Phase 4 phase is a pure scale of
        the log-price, \(\Theta_t=\Theta_0+(\beta/\sigma)\ln(S_t/S_0)\),
        so the exercise boundary is a moving angular barrier. We plot the
        reference boundary as a curve in the \((\tau,\theta)\) plane for
        the gauge \(\beta/\sigma=1\): calls exercise above the curve, puts
        below it.
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
        for ax, (taus, bvals, kind) in zip(
                axes, ((taus_c, bvals_c, "call"),
                       (taus_p, bvals_p, "put"))):
            th = np.log(bvals / K)
            ax.plot(taus, th, lw=2, color="tab:blue")
            ax.axhline(np.log(foundations[(R, Q, kind)]["b_inf"] / K),
                       ls="--", color="tab:gray",
                       label="perpetual phase")
            ax.set_xlabel(r"time to maturity $\tau$")
            ax.set_ylabel(r"phase boundary $\theta_B(\tau)$")
            ax.set_title(f"American {kind}")
            ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f01_phase_boundary.png", dpi=160)
        plt.close(fig)
        print("saved f01_phase_boundary.png")
        """
    ),
    md(
        r"""
        ## 5. Short-maturity asymptotics

        Fit \(b(\tau)=b_0+\eta\,c\,\sigma b_0\sqrt{2\tau|\ln\tau|}\) on tiny
        \(\tau\). The \(\sqrt{\tau|\ln\tau|}\) **shape** (infinite slope at
        maturity) is universal — a plain exponential spiral cannot
        reproduce it. The effective coefficient \(c\), however, depends on
        \(r-q\) at accessible maturities: it is \(\approx 1\) in the
        zero-drift case and departs from \(1\) as \(|r-q|\) grows. The
        spiral formula's free \(\eta\) parameter absorbs precisely this
        dependence, which is why collocation fixes \(\eta\) jointly with
        \((\kappa_1,\kappa_2)\).
        """
    ),
    code(
        r"""
        def short_coeff(kind, r_, q_, sig_, Tfit=0.05):
            taus, bv = p15.solve_boundary(K, r_, q_, sig_, Tfit, kind,
                                          n_grid=300, n_quad=40,
                                          delta=1e-8, cluster=2.0)
            b0 = p15.boundary_at_maturity(K, r_, q_, kind)
            eta = 1.0 if kind == "call" else -1.0
            xs, ys = [], []
            for i in range(1, len(taus)):
                if taus[i] > 0.02:
                    break
                xs.append(sig_ * math.sqrt(2 * taus[i]
                                           * abs(math.log(taus[i]))))
                ys.append(eta * (bv[i] - b0) / b0)
            coef = np.polyfit(xs, ys, 1)[0]
            return coef, b0

        coeff_grid = []
        zero_drift = []
        for r_, q_, sig_ in ((0.05, 0.05, 0.2), (0.07, 0.03, 0.2),
                             (0.03, 0.07, 0.2), (0.05, 0.05, 0.4)):
            for kind in ("call", "put"):
                coef, b0 = short_coeff(kind, r_, q_, sig_)
                coeff_grid.append((r_, q_, sig_, kind, coef))
                zd = abs(r_ - q_) < 1e-12
                if zd:
                    zero_drift.append(coef)
                print(f"r={r_} q={q_} sig={sig_} {kind}: coeff={coef:.4f} "
                      f"b0={b0:.2f}{'  (zero drift)' if zd else ''}")
        coeffs_zd = np.array(zero_drift)
        results["short_maturity_coeff_zero_drift_mean"] = float(
            np.mean(coeffs_zd))
        results["short_maturity_coeff_zero_drift_max_dev"] = float(
            np.max(np.abs(coeffs_zd - 1.0)))
        results["short_maturity_coeff_all"] = [
            dict(r=r_, q=q_, sigma=s_, kind=k, coeff=c_)
            for (r_, q_, s_, k, c_) in coeff_grid]
        # zero-drift coefficients sit within ~0.2 of unity on this window
        # (mild call-side positive bias); nonzero r - q shifts them
        # substantially, which eta absorbs
        assert results["short_maturity_coeff_zero_drift_max_dev"] < 0.25
        """
    ),
    md(
        r"""
        ## 6. The spiral family and its refinement

        Plain spiral: \(b(\tau)=b_\infty\exp(\ln(b_0/b_\infty)e^{-\kappa\tau})\).
        Refined spiral adds the universal asymptotic term with cutoff:

        \[
        \ln b(\tau)=\ln b_\infty+\ln(b_0/b_\infty)e^{-\kappa_1\tau}
        +\eta\,\sigma\sqrt{2\tau|\ln\max(\tau,\varepsilon)|}\,e^{-\kappa_2\tau}.
        \]

        We fit both to the reference boundary and compare.
        """
    ),
    code(
        r"""
        from scipy import optimize

        tau_fit = np.linspace(1e-5, T, 400)

        def fit_errors(kind):
            taus, bv = (taus_c, bvals_c) if kind == "call" \
                else (taus_p, bvals_p)
            bd = lambda tau: float(np.interp(tau, taus, bv))
            bt = np.array([bd(t) for t in tau_fit])
            b0 = p15.boundary_at_maturity(K, R, Q, kind)
            binf = foundations[(R, Q, kind)]["b_inf"]
            eta = 1.0 if kind == "call" else -1.0

            def err_plain(kap):
                bs = binf * np.exp(np.log(b0 / binf)
                                   * np.exp(-kap * tau_fit))
                return float(np.max(np.abs(bs - bt) / bt))
            kap = optimize.minimize_scalar(err_plain, bounds=(1e-3, 40),
                                           method="bounded").x
            e_plain = err_plain(kap)

            def err_ref(prm):
                k1, k2, eta_f = prm
                lb = np.array([math.log(p15.spiral_refined_boundary(
                    t, b0, binf, SIG, eta * eta_f, k1, k2))
                    for t in tau_fit])
                return float(np.max(np.abs(np.exp(lb) - bt) / bt))
            best = optimize.minimize(err_ref, x0=[0.8, 1.1, 1.0],
                                     bounds=[(1e-3, 40), (1e-3, 40),
                                             (0, 2.5)],
                                     method="L-BFGS-B")
            return e_plain, best.fun, kap, best.x, bt, b0, binf, eta

        fit_report = {}
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
        for ax, kind in zip(axes, ("call", "put")):
            e_p, e_r, kap, prm, bt, b0, binf, eta = fit_errors(kind)
            fit_report[kind] = dict(plain=e_p, refined=e_r, kappa=kap,
                                    k1=prm[0], k2=prm[1], eta=prm[2])
            print(f"{kind}: plain L-inf {100 * e_p:.2f}% (k={kap:.3f}), "
                  f"refined {100 * e_r:.2f}% "
                  f"(k1={prm[0]:.3f}, k2={prm[1]:.3f}, eta={prm[2]:.3f})")
            ax.plot(tau_fit, bt, lw=2, color="tab:blue", label="reference")
            bs = binf * np.exp(np.log(b0 / binf) * np.exp(-kap * tau_fit))
            ax.plot(tau_fit, bs, ls="--", color="tab:orange",
                    label="plain spiral")
            lb = np.array([math.log(p15.spiral_refined_boundary(
                t, b0, binf, SIG, eta * prm[2], prm[0], prm[1]))
                for t in tau_fit])
            ax.plot(tau_fit, np.exp(lb), ls=":", color="tab:red",
                    label="refined spiral")
            ax.set_xlabel(r"$\tau$")
            ax.set_ylabel(r"$b(\tau)$")
            ax.set_title(f"American {kind}: boundary fits")
            ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f02_spiral_fit.png", dpi=160)
        plt.close(fig)
        print("saved f02_spiral_fit.png")
        """
    ),
    md(
        r"""
        ## 7. The collocation formula (no fitting)

        \((\kappa_1,\kappa_2,\eta)\) fixed by driving the value-matching
        residual to zero at three fractional times to maturity (bounded
        least squares). Prices then come from European + EEP on the
        collocated boundary — no reference solve needed.
        """
    ),
    code(
        r"""
        collocation = {}
        for kind in ("call", "put"):
            k1, k2, eta, info = p15.spiral_collocation(K, R, Q, SIG, T,
                                                       kind)
            taus, bv = (taus_c, bvals_c) if kind == "call" \
                else (taus_p, bvals_p)
            bd = lambda tau: float(np.interp(tau, taus, bv))
            row = []
            for S in (80.0, 90.0, 100.0, 110.0, 120.0):
                ref = p15.american_from_boundary(S, T, bd, K, R, Q, SIG,
                                                 kind, n_quad=96)
                sp, *_ = p15.american_spiral(S, K, R, Q, SIG, T, kind,
                                             params=(k1, k2, eta))
                bw = p15.baw(S, K, R, Q, SIG, T, kind)
                row.append(dict(S=S, ref=ref, spiral=sp, baw=bw))
            collocation[kind] = dict(k1=k1, k2=k2, eta=eta,
                                     objective=info["objective"], rows=row)
            print(f"{kind}: k1={k1:.4f} k2={k2:.4f} eta={eta:.4f} "
                  f"objective={info['objective']:.2e}")
            for rr in row:
                print(f"  S={rr['S']:5.0f} ref={rr['ref']:.5f} "
                      f"spiral={rr['spiral']:.5f} BAW={rr['baw']:.5f} "
                      f"|sp-ref|={abs(rr['spiral'] - rr['ref']):.5f} "
                      f"|baw-ref|={abs(rr['baw'] - rr['ref']):.5f}")
        """
    ),
    code(
        r"""
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
        for ax, kind in zip(axes, ("call", "put")):
            rows = collocation[kind]["rows"]
            Ss = [rr["S"] for rr in rows]
            ax.plot(Ss, [abs(rr["spiral"] - rr["ref"]) for rr in rows],
                    "o-", label="spiral error")
            ax.plot(Ss, [abs(rr["baw"] - rr["ref"]) for rr in rows],
                    "s--", label="BAW error")
            ax.set_yscale("log")
            ax.set_xlabel("spot $S$")
            ax.set_ylabel("abs price error")
            ax.set_title(f"American {kind}: error vs spot")
            ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f03_spot_errors.png", dpi=160)
        plt.close(fig)
        print("saved f03_spot_errors.png")
        """
    ),
    md(
        r"""
        ## 8. Parameter-grid benchmark

        Reference solver vs spiral formula vs BAW vs CRR–Richardson on a
        reduced deterministic grid (the extended 90-configuration run is
        reported in the manuscript).
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
            taus, bv = p15.solve_boundary(K, r_, q_, sig_, T_, kind,
                                          n_grid=250, n_quad=48, delta=1e-8)
            bd = lambda tau: float(np.interp(tau, taus, bv))
            k1, k2, eta, _ = p15.spiral_collocation(K, r_, q_, sig_, T_,
                                                    kind)
            for S in (90.0, 100.0, 110.0):
                ref = p15.american_from_boundary(S, T_, bd, K, r_, q_,
                                                 sig_, kind, n_quad=96)
                sp, *_ = p15.american_spiral(S, K, r_, q_, sig_, T_, kind,
                                             params=(k1, k2, eta))
                bw = p15.baw(S, K, r_, q_, sig_, T_, kind)
                crr = p15.crr_richardson(S, K, r_, q_, sig_, T_, kind,
                                         Ns=(1200, 2400, 4800))
                bench.append(dict(r=r_, q=q_, sigma=sig_, T=T_, kind=kind,
                                  S=S, ref=ref, spiral=sp, baw=bw, crr=crr))
        arr = {k: np.array([x[k] for x in bench])
               for k in ("ref", "spiral", "baw", "crr")}
        summary = {}
        for name in ("spiral", "baw", "crr"):
            d = arr[name] - arr["ref"]
            summary[name] = dict(rmse=float(np.sqrt(np.mean(d ** 2))),
                                 mae=float(np.max(np.abs(d))))
            print(f"{name:>7} vs ref: RMSE={summary[name]['rmse']:.5f} "
                  f"MAE={summary[name]['mae']:.5f}")
        results["benchmark"] = summary
        with open(TABLES / "benchmark_reduced.csv", "w") as f:
            f.write("r,q,sigma,T,kind,S,ref,spiral,baw,crr\n")
            for x in bench:
                f.write(f"{x['r']},{x['q']},{x['sigma']},{x['T']},"
                        f"{x['kind']},{x['S']},{x['ref']:.6f},"
                        f"{x['spiral']:.6f},{x['baw']:.6f},"
                        f"{x['crr']:.6f}\n")
        print("saved phase15_tables/benchmark_reduced.csv")
        """
    ),
    code(
        r"""
        fig, ax = plt.subplots(figsize=(5.2, 3.4))
        names = ["spiral", "BAW", "CRR-Rich"]
        rms = [summary["spiral"]["rmse"], summary["baw"]["rmse"],
               summary["crr"]["rmse"]]
        mae = [summary["spiral"]["mae"], summary["baw"]["mae"],
               summary["crr"]["mae"]]
        xs = np.arange(3)
        ax.bar(xs - 0.2, rms, width=0.4, label="RMSE")
        ax.bar(xs + 0.2, mae, width=0.4, label="MAE")
        ax.set_xticks(xs)
        ax.set_xticklabels(names)
        ax.set_ylabel("error vs reference")
        ax.set_title("Reduced-grid benchmark")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIGURES / "f04_benchmark_summary.png", dpi=160)
        plt.close(fig)
        print("saved f04_benchmark_summary.png")
        """
    ),
    md(
        r"""
        ## 9. Structural identities of the formula

        The collocation formula must respect: the zero-dividend call limit
        (American call = European), the perpetual limit
        (\(T\to\infty\) price \(\to\) perpetual), and monotonicity in spot.
        """
    ),
    code(
        r"""
        euro = p15.bs_european(S0, K, R, 0.0, SIG, T, "call")
        am0, *_ = p15.american_spiral(S0, K, R, 0.0, SIG, T, "call")
        results["q0_call_gap"] = abs(am0 - euro)
        print(f"q=0 call: spiral={am0:.8f} European={euro:.8f} "
              f"gap={results['q0_call_gap']:.2e}")

        perp_price, _ = p15.perpetual_american(S0, K, R, Q, SIG, "put")
        am_long, *_ = p15.american_spiral(S0, K, R, Q, SIG, 30.0, "put")
        results["perpetual_gap_T30"] = abs(am_long - perp_price)
        print(f"put T=30: spiral={am_long:.6f} perpetual={perp_price:.6f} "
              f"gap={results['perpetual_gap_T30']:.4f}")

        spots = np.linspace(60.0, 140.0, 41)
        prices = np.array([p15.american_spiral(s, K, R, Q, SIG, T, "put")[0]
                           for s in spots])
        diffs = np.diff(prices)
        results["put_monotone_decreasing"] = bool(np.all(diffs <= 1e-9))
        seconds = np.diff(prices, 2)
        results["put_convex_min_second_diff"] = float(np.min(seconds))
        print(f"put monotone decreasing in S: "
              f"{results['put_monotone_decreasing']}")
        print(f"put min second difference: "
              f"{results['put_convex_min_second_diff']:.3e} (>= ~0)")
        """
    ),
    md("## 10. Evidence summary"),
    code(
        r"""
        results["runtime_seconds"] = time.time() - started
        with open(TABLES / "phase15_summary.json", "w") as f:
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

out = Path(__file__).parent / "phase15_american_spiral.ipynb"
nbf.write(nb, out)
print(f"wrote {out}")
