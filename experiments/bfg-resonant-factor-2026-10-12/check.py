"""Finite synthetic checks for P77; no data/network access. Run with Python 3,
NumPy, SciPy and mpmath. General existence is proved in DERIVATION.md.
Thresholds declared before execution: MP tails/closure 1e-20, SVD/gauge 1e-12,
expm 1e-12, nonlinear endpoint 2e-8, inverse residual 1e-9,
five-event gauge readouts and independent spectral calculation 1e-8.
"""
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.optimize import root

mp.mp.dps = 100
a = mp.mpf(16)/135
lam = mp.mpf(224)/675
d = mp.mpf(29)/90
ys = mp.mpf(8)/45
assert lam**2 < a < lam < mp.sqrt(a)
assert lam < mp.mpf(17)/50 < mp.sqrt(a)


def canonical_limit(s0, r0, n):
    """Exact scalar spectral calculus for a real 2x2 Pauli carrier.
    Returns fast radial component and K-channel transverse multiplier.
    Orientation is unchanged in the tested local domain.
    """
    s, r, eta_product = s0, r0, mp.mpf(1)
    for _ in range(n):
        xp, xm = s+d+r, s+d-r
        assert 0 < xm <= xp < 1
        lc = 1/(1+xp)+1/(1+xm)
        lb = xp*xp/(1+xp)+xm*xm/(1+xm)
        alpha = lb/(lc+lb)
        gp = (alpha+(1-alpha)*xp*xp)/(1+xp)**2
        gm = (alpha+(1-alpha)*xm*xm)/(1+xm)**2
        tcp = mp.sqrt(alpha/gp)/(1+xp)
        tcm = mp.sqrt(alpha/gm)/(1+xm)
        tbp = mp.sqrt((1-alpha)/gp)*xp/(1+xp)
        tbm = mp.sqrt((1-alpha)/gm)*xm/(1+xm)
        eta_product *= tcp*tcm+tbp*tbm
        s, r = (gp+gm)/2, (gp-gm)/2
    return r/a**n, eta_product


mp_tail = mp.mpf(0)
mp_closure = mp.mpf(0)
for offset in ['-.001', '0', '.001']:
    for radial in ['.0001', '.001', '.003']:
        s, r = ys+mp.mpf(offset), mp.mpf(radial)
        z60, k60 = canonical_limit(s, r, 60)
        z80, k80 = canonical_limit(s, r, 80)
        mp_tail = max(mp_tail, abs(z60-z80), abs(k60-k80))
        # Independent first-event loads, then compare shifted infinite limit.
        xp, xm = s+d+r, s+d-r
        alpha = (xp*xp/(1+xp)+xm*xm/(1+xm))/(
            (1+xp*xp)/(1+xp)+(1+xm*xm)/(1+xm))
        gp = (alpha+(1-alpha)*xp*xp)/(1+xp)**2
        gm = (alpha+(1-alpha)*xm*xm)/(1+xm)**2
        zp, _ = canonical_limit((gp+gm)/2, (gp-gm)/2, 80)
        mp_closure = max(mp_closure, abs(zp-a*z80))
assert mp_tail < mp.mpf('1e-20')
assert mp_closure < mp.mpf('1e-20')

sx = np.array([[0., 1.], [1., 0.]])
sz = np.diag([1., -1.])
ident = np.eye(2)


def ambient(Y, K, W):
    X = Y+float(d)*ident
    C = np.linalg.inv(ident+X)
    B = X@C
    alpha = np.trace(X@X@C).real/np.trace((ident+X@X)@C).real
    A = np.vstack((np.sqrt(alpha)*C, np.sqrt(1-alpha)*B))
    U, sigma, Vh = np.linalg.svd(A, full_matrices=False)
    V = Vh.conj().T
    Kraw = U.conj().T@np.block([[K, np.zeros_like(K)],
                               [np.zeros_like(K), K]])@U
    # Transform canonical SVD outputs back to smooth ambient frame.
    return V@np.diag(sigma*sigma)@V.conj().T, V@Kraw@Vh, W


rng = np.random.default_rng(77)
gauge_error = 0.
readout_gauge_error = 0.
spectral_error = 0.
for _ in range(30):
    Y = float(ys)*ident+.003*sx+.002*sz
    K = sz.copy()
    W = (ident+sx/2)/2
    raw = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
    V, _ = np.linalg.qr(raw)
    out = ambient(Y, K, W)
    gout = ambient(V@Y@V.conj().T, V@K@V.conj().T, V@W@V.conj().T)
    gauge_error = max(gauge_error, *(np.max(np.abs(gout[i]-V@out[i]@V.conj().T)) for i in range(3)))
    Yb, Kb, Wb = Y.copy(), K.copy(), W.copy()
    Yg, Kg, Wg = V@Y@V.conj().T, V@K@V.conj().T, V@W@V.conj().T
    for _ in range(5):
        Yb, Kb, Wb = ambient(Yb, Kb, Wb)
        Yg, Kg, Wg = ambient(Yg, Kg, Wg)
    Zb = (Yb-np.trace(Yb)*ident/2)/float(a)**5
    Zg = (Yg-np.trace(Yg)*ident/2)/float(a)**5
    pb = np.array([np.trace(Kb@Zb).real/2,
                   2*np.trace((Wb-ident/2)@Zb).real])
    pg = np.array([np.trace(Kg@Zg).real/2,
                   2*np.trace((Wg-ident/2)@Zg).real])
    readout_gauge_error = max(readout_gauge_error, np.max(np.abs(pb-pg)))
    radius = mp.sqrt(mp.mpf('.003')**2+mp.mpf('.002')**2)
    zr, eta = canonical_limit(ys, radius, 5)
    u = np.array([float(mp.mpf('.003')/radius), float(mp.mpf('.002')/radius)])
    expected_Z = float(zr)*(u[0]*sx+u[1]*sz)
    initial_k = np.array([0., 1.])
    parallel_k = np.dot(initial_k, u)*u
    expected_k = parallel_k+float(eta)*(initial_k-parallel_k)
    expected_K = expected_k[0]*sx+expected_k[1]*sz
    spectral_error = max(spectral_error, np.max(np.abs(Zb-expected_Z)),
                         np.max(np.abs(Kb-expected_K)))
assert gauge_error < 1e-12
assert readout_gauge_error < 1e-8
assert spectral_error < 1e-8

af = float(a)
tau = 1.  # Synthetic unit convention, NOT measured/calibrated seconds.
gamma = -2*np.log(af)/tau


def parameters(j):
    return (2*np.pi*j/tau)**2+gamma**2/4


def flow_scaled(u, scale, kappa, rival=False):
    # Rescaled integration avoids subtracting the carrier fixed point and avoids
    # very small physical amplitudes amplified by a^-n in h_N.
    def rhs(_, z):
        theta = scale*z[0]
        restoring = z[0]+scale**2*z[0]**3 if rival else (
            np.sin(theta)/scale if scale else z[0])
        return [z[1], -gamma*z[1]-kappa*restoring]
    sol = solve_ivp(rhs, [0, tau], u, method='DOP853', rtol=2e-12, atol=2e-14)
    assert sol.success and sol.t[-1] == tau
    return sol.y[:, -1]


def h(z, kappa, n=12, rival=False):
    u = np.asarray(z, dtype=float)
    scale = 1.
    for _ in range(n):
        u = flow_scaled(u, scale, kappa, rival)/af
        scale *= af
    return u


expm_error = 0.
endpoint_error = 0.
inverse_error = 0.
tail_error = 0.
cases = 0
for j, rival in [(1, False), (2, False), (1, True)]:
    kappa = parameters(j)
    A = np.array([[0., 1.], [-kappa, -gamma]])
    expm_error = max(expm_error, np.max(np.abs(expm(tau*A)-af*ident)))
    for z in ([.005, -.002], [-.008, .003], [.01, .005]):
        hz = h(z, kappa, rival=rival)
        psi = flow_scaled(z, 1., kappa, rival)
        endpoint_error = max(endpoint_error, np.max(np.abs(h(psi, kappa, rival=rival)-af*hz)))
        tail_error = max(tail_error, np.max(np.abs(hz-h(z, kappa, 16, rival))))
        # Pi=h^-1(p) is constructed numerically from independently given p.
        p = np.array([.003, -.002])
        solution = root(lambda v: h(v, kappa, rival=rival)-p, p, tol=1e-10)
        assert solution.success
        inverse_error = max(inverse_error, np.max(np.abs(h(solution.x, kappa, rival=rival)-p)))
        returned = flow_scaled(solution.x, 1., kappa, rival)
        endpoint_error = max(endpoint_error, np.max(np.abs(h(returned, kappa, rival=rival)-af*p)))
        cases += 1
assert expm_error < 1e-12
assert endpoint_error < 2e-8
assert inverse_error < 1e-9
assert tail_error < 2e-8
assert parameters(2) != parameters(1)
theta = .01
force_difference = -(parameters(2)-parameters(1))*np.sin(theta)
assert force_difference != 0.
result = dict(kind='synthetic_math_and_implementation_controls_only',
              precision_digits=mp.mp.dps, canonical_cases=9, gauge_cases=30,
              nonlinear_cases=cases, max_mp_tail=str(mp_tail),
              max_mp_closure=str(mp_closure), max_gauge_svd_error=gauge_error,
              max_five_event_readout_gauge_error=readout_gauge_error,
              max_independent_spectral_error=spectral_error,
              max_expm_error=expm_error, max_nonlinear_endpoint_error=endpoint_error,
              max_inverse_residual=inverse_error, max_flow_tail_difference=tail_error,
              same_clock_force_difference_at_synthetic_angle=force_difference,
              empirical_confirmation=False, physical_calibration=False,
              holdout_accessed=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
