"""Seeded finite-dimensional consistency audit for the 29 September BFG preprint.

Uses independent direct quadratic minimization and spectral identities as oracles.
This does not execute the full BFG successor or test physical emergence.
"""
import json
import platform

import numpy as np


SEED = 20260929
TRIALS = 10_000
CONTROLS = 1_000
TOL = 1e-9


def main():
    rng = np.random.default_rng(SEED)
    maxima = {}
    minima = {}
    counts = dict(complex_consistency=0, level0_tangent=0,
                  noncommuting_novelty=0, formation_gate_pass=0,
                  formation_gate_terminal=0, commuting_controls=0,
                  scalar_load_controls=0)
    failures = []
    novelty = []

    def residual(label, value, trial, tolerance=TOL):
        value = float(value)
        maxima[label] = max(maxima.get(label, 0.0), value)
        if not np.isfinite(value) or value > tolerance:
            failures.append(dict(trial=trial, check=label, observed=value,
                                 tolerance=tolerance))

    def lower_bound(label, value, trial, tolerance=TOL):
        value = float(value)
        minima[label] = min(minima.get(label, value), value)
        if not np.isfinite(value) or value < -tolerance:
            failures.append(dict(trial=trial, check=label, observed=value,
                                 lower_bound=-tolerance))

    for trial in range(TRIALS):
        n = int(rng.integers(2, 9))
        ident = np.eye(n)
        # §3.2 plus older architecture: complex positive load, graph metric,
        # G-orthogonal persistence, reciprocal packet, polar and Gram checks.
        A = (rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))) / np.sqrt(2*n)
        Y = A.conj().T @ A
        G = ident + Y
        C = np.linalg.solve(G, ident)
        B = Y @ C
        Z = (ident-Y) @ C
        residual('neutral_partition', np.linalg.norm(C+B-ident, 2), trial)
        residual('contrast_to_resolvent', max(np.linalg.norm(C-(ident+Z)/2, 2),
                                             np.linalg.norm(B-(ident-Z)/2, 2)), trial)
        r = int(rng.integers(1, n+1))
        W = rng.normal(size=(n, r)) + 1j*rng.normal(size=(n, r))
        P = W @ np.linalg.solve(W.conj().T@G@W, W.conj().T@G)
        residual('graph_projector_idempotence', np.linalg.norm(P@P-P, 2), trial)
        residual('graph_projector_adjoint', np.linalg.norm(P.conj().T@G-G@P, 2), trial)
        D = rng.normal(size=n) + 1j*rng.normal(size=n)
        dk = P@C@D
        du = P@B@D
        graph_norm = lambda z: float(np.vdot(z, G@z).real)
        lk, lu = graph_norm(dk), graph_norm(du)
        total = lk+lu
        if min(lk, lu) <= 1e-14:
            failures.append(dict(trial=trial, check='positive_persistent_loads',
                                 observed=min(lk, lu)))
            continue
        wk, wu = lu/total, lk/total
        residual('reciprocal_balance', abs(wk*lk-wu*lu), trial)
        residual('reciprocal_simplex', abs(wk+wu-1), trial)
        gain_squared = (wk*lk+wu*lu)/graph_norm(D)
        maxima['crossfed_gain'] = max(maxima.get('crossfed_gain', 0.0),
                                      float(np.sqrt(gain_squared)))
        lower_bound('nonexpansion_margin', .5-gain_squared, trial)
        packet = np.r_[np.sqrt(wk)*dk, np.sqrt(wu)*du]
        compact = np.r_[np.sqrt(wk)*P@(ident+Z)@D/2,
                        np.sqrt(wu)*P@(ident-Z)@D/2]
        residual('compact_expanded_packet', np.linalg.norm(packet-compact), trial)
        F = np.vstack((np.sqrt(wk)*P@C, np.sqrt(wu)*P@B))
        U, s, Vh = np.linalg.svd(F, full_matrices=False)
        rank = int(np.sum(s > 1e-10*s[0]))
        J = U[:, :rank] @ Vh[:rank, :]
        support = Vh[:rank, :].conj().T @ Vh[:rank, :]
        residual('polar_support', np.linalg.norm(J.conj().T@J-support, 2), trial)
        R = rng.normal(size=(2*n, 2*n)) + 1j*rng.normal(size=(2*n, 2*n))
        capacity = R.conj().T@R
        compressed = J.conj().T@capacity@J
        lower_bound('compressed_capacity_min_eig',
                    np.linalg.eigvalsh((compressed+compressed.conj().T)/2).min(), trial)
        T = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        V = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        neutral_metric = V.conj().T@V + ident
        load = T.conj().T@neutral_metric@T
        Lnext = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        rebuilt = Lnext.conj().T@load@Lnext
        lower_bound('rebuilt_gram_min_eig',
                    np.linalg.eigvalsh((rebuilt+rebuilt.conj().T)/2).min(), trial)
        counts['complex_consistency'] += 1

        # The new Appendix C: formed Level-0 branch and direct neutral minimization.
        O, _ = np.linalg.qr(rng.normal(size=(n, n)))
        a = float(rng.uniform(.5, 2))
        K = (O*np.r_[-a, rng.uniform(.2, 3, size=n-1)])@O.T
        delta = np.sqrt(a)*O[:, 0]
        H = K+a*ident+2*np.outer(delta, delta)
        grad = K@delta + (delta@delta)*delta
        residual('level0_stationarity', np.linalg.norm(grad), trial)
        lower_bound('formed_hessian_min_eig', np.linalg.eigvalsh(H).min(), trial)
        x = rng.normal(size=n)*.2
        f = lambda v: .5*v@K@v+.25*(v@v)**2
        remainder = f(delta+x)-f(delta)-.5*x@H@x
        exact_remainder = (delta@x)*(x@x)+.25*(x@x)**2
        residual('quartic_taylor_identity', abs(remainder-exact_remainder), trial)
        Rm = rng.normal(size=(n, n))
        M = Rm.T@Rm+.5*ident
        L = rng.normal(size=(n, n))/np.sqrt(n)
        source = rng.normal(size=n)
        eta = np.linalg.solve(L.T@H@L+M, L.T@H@source)
        physical_cost = (.5*(source-L@eta)@H@(source-L@eta)
                         +.5*eta@M@eta)
        eh, Uh = np.linalg.eigh(H)
        em, Um = np.linalg.eigh(M)
        Sh = (Uh*np.sqrt(eh))@Uh.T
        Sm = (Um*np.sqrt(em))@Um.T
        Astar = Sh@L@np.linalg.inv(Sm)
        d, nu = Sh@source, Sm@eta
        whitened_cost = .5*np.linalg.norm(d-Astar@nu)**2+.5*np.linalg.norm(nu)**2
        Ystar = Astar@Astar.T
        gram_cost = .5*d@np.linalg.solve(ident+Ystar, d)
        residual('hessian_whitening', abs(physical_cost-whitened_cost), trial)
        residual('neutral_gram_minimum', abs(physical_cost-gram_cost), trial)
        residual('neutral_stationarity',
                 np.linalg.norm((L.T@H@L+M)@eta-L.T@H@source), trial)
        counts['level0_tangent'] += 1

        # New paper Theorem 1: independently compare spectral moments with the
        # entrywise defect, including the formation gate as a diagnostic.
        y = rng.uniform(0, 3, size=n)
        alpha, beta = rng.uniform(.3, 3, size=2)
        eig = np.r_[-rng.uniform(.2, 2), rng.uniform(.2, 3, size=n-1)]
        Uq, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)))
        Kp = (Uq*eig)@Uq.conj().T
        den = np.outer(alpha+beta*y*y, alpha+beta*y*y)
        chi = (alpha+beta*np.outer(y, y))/np.sqrt(den)
        Knext = chi*Kp
        defect = alpha*beta*(y[:, None]-y[None, :])**2/den
        residual('schur_defect_identity', np.max(np.abs(1-chi*chi-defect)), trial)
        spectral_loss = float((np.trace(Kp@Kp)-np.trace(Knext@Knext)).real)
        predicted_loss = float(np.sum(defect*np.abs(Kp)**2))
        residual('novelty_moment_identity', abs(spectral_loss-predicted_loss), trial)
        if spectral_loss <= 1e-11:
            failures.append(dict(trial=trial, check='strict_internal_novelty',
                                 observed=spectral_loss))
        counts['noncommuting_novelty'] += 1
        eig_next = np.linalg.eigvalsh((Knext+Knext.conj().T)/2)
        if eig_next[0] < 0 and eig_next[1]-eig_next[0] > 1e-10:
            counts['formation_gate_pass'] += 1
            novelty.append(float(np.linalg.norm(np.sort(eig_next)-np.sort(eig))
                                 /np.linalg.norm(eig)))
        else:
            counts['formation_gate_terminal'] += 1
        if trial < CONTROLS:
            diagonal = np.diag(eig)
            residual('commuting_inheritance', np.linalg.norm(chi*diagonal-diagonal), trial)
            counts['commuting_controls'] += 1
        if trial < 100:
            scalar = np.full(n, rng.uniform(0, 3))
            chi0 = (alpha+beta*np.outer(scalar, scalar))/np.sqrt(
                np.outer(alpha+beta*scalar*scalar, alpha+beta*scalar*scalar))
            residual('scalar_load_inheritance', np.linalg.norm(chi0*Kp-Kp), trial)
            counts['scalar_load_controls'] += 1

    result = dict(seed=SEED, dimensions=[2, 8], trials=TRIALS,
                  controls=CONTROLS, tolerance_abs=TOL, counts=counts,
                  max_abs_residual=maxima, minimum_eigenvalues_and_margins=minima,
                  spectral_novelty_successful_cases=dict(
                      minimum=min(novelty) if novelty else None,
                      median=float(np.median(novelty)) if novelty else None,
                      maximum=max(novelty) if novelty else None),
                  failure_count=len(failures), failures=failures[:10],
                  numpy_version=np.__version__, python_version=platform.python_version(),
                  scope=('Adapted internal finite-dimensional consistency audit; '
                         'the Schur stratum is not a full canonical five-object successor, '
                         'and no natural-carrier or irreducible-emergence test is run.'))
    print(json.dumps(result, indent=2, allow_nan=False))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
