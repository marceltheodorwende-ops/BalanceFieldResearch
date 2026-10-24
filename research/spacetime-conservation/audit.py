"""BFG-only finite conservation and determinant-carrier controls.

Run from any directory: python research/spacetime-conservation/audit.py
Imports the existing source update without executing empirical entry points.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import sys
from fractions import Fraction as R
from pathlib import Path

import numpy as np
import scipy
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "experiments/real-eeg-covariance-2026-10-07/experiment.py"
EXPECTED_SOURCE_BLOB = "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498"
TOL = 1e-10
SEED = 20261023

def source_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def load_update():
    blob = source_blob(SOURCE)
    if blob != EXPECTED_SOURCE_BLOB:
        raise RuntimeError("Pinned source update changed; review before reusing these certificates")
    spec = importlib.util.spec_from_file_location("bfg_pinned_kernel", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.update

def hermitian_function(y, function):
    eig, vec = np.linalg.eigh(y)
    return (vec * function(eig)) @ vec.conj().T

def aligned(k, f, y):
    """Independent formula from the paper's full-persistence algebra."""
    eye = np.eye(len(y))
    c = np.linalg.inv(eye + y)
    b = y @ c
    lc = np.trace(f @ c).real
    lb = np.trace(f @ y @ y @ c).real
    alpha = lb / (lc + lb)
    m = alpha * c @ c + (1 - alpha) * b @ b
    invsqrt = hermitian_function(m, lambda eig: 1 / np.sqrt(eig))
    tc = np.sqrt(alpha) * c @ invsqrt
    tb = np.sqrt(1 - alpha) * b @ invsqrt
    kp = tc @ k @ tc + tb @ k @ tb
    return dict(k=kp, y=m, tc=tc, tb=tb, alpha=alpha)

def pauli():
    return [np.eye(2), np.array([[0., 1.], [1., 0.]]),
            np.array([[0., -1j], [1j, 0.]]), np.diag([1., -1.])]

def coordinates(x):
    return np.array([np.trace(s @ x).real / 2 for s in pauli()])

def qdet(x):
    z = coordinates(x)
    return float(z[0] ** 2 - z[1:] @ z[1:])

def exact_certificates():
    lc = R(4, 5) + R(2, 3)
    lb = R(1, 20) + R(1, 6)
    alpha = lb / (lc + lb)
    yi, yj = R(1, 4), R(1, 2)
    q2 = (alpha + (1-alpha)*yi*yj)**2 / (
        (alpha+(1-alpha)*yi**2)*(alpha+(1-alpha)*yj**2))
    assert (lc, lb, alpha, q2) == (R(22,15), R(13,60), R(13,101), R(1152,1295))
    assert 1-q2 == R(143,1295) > 0
    a, lam = R(16,135), R(224,675)
    assert lam**2-a**2 == R(43776,455625) > 0
    assert lam/a == R(14,5)
    # Exact determinant on the declared REAL Hermitian coordinate space.
    x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
    x = sp.Matrix([[x0+x3, x1-sp.I*x2], [x1+sp.I*x2, x0-x3]])
    determinant = sp.expand(x.det())
    expected = x0*x0-x1*x1-x2*x2-x3*x3
    assert sp.expand(determinant-expected) == 0
    hessian = sp.hessian(determinant, [x0,x1,x2,x3])
    assert hessian == sp.diag(2,-2,-2,-2)
    # Exact pinching defect on noncommuting F,K (no floating tolerances).
    q = sp.sqrt(sp.Rational(q2.numerator,q2.denominator))
    f = sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]])
    k = sp.Matrix([[0,1],[1,0]])
    kp = sp.Matrix([[0,q],[q,0]])
    assert sp.simplify(sp.trace(f*kp)-q) == 0
    assert sp.trace(f*k) == 1 and sp.simplify(q*q-sp.Rational(1152,1295)) == 0
    return dict(load_C=str(lc), load_B=str(lb), alpha=str(alpha),
                h12_squared=str(q2), null_cone_defect=str(1-q2),
                tangent_null_defect=str(lam*lam-a*a), temporal_spatial_ratio=str(lam/a),
                determinant=str(determinant), determinant_hessian=hessian.tolist())

def complex_unitary(rng, n):
    z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    return np.linalg.qr(z)[0]

def pos(rng, n):
    z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    return z @ z.conj().T + .2*np.eye(n)

def random_controls(update):
    rng = np.random.default_rng(SEED)
    maxima = dict(aligned_kernel=0., aligned_load=0., inherited_formation=0.,
                  inherited_witness=0., trace_kernel=0., trace_formation=0.,
                  channel_unital=0., gauge_kernel=0., gauge_load=0.,
                  gauge_formation=0., charge_commutant=0.,
                  hs_dissipation_identity=0.)
    dimensions = []
    for n in (2,3,4,5):
        for case in range(8):
            u = complex_unitary(rng,n)
            y = (u*np.linspace(.15,.8,n)) @ u.conj().T
            f, w = pos(rng,n), pos(rng,n)
            w /= np.trace(w).real
            z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
            k = (z+z.conj().T)/2
            r = update(k,f,w,y,np.eye(n))
            assert r["terminal"] is None and len(r["y"]) == n
            v = r["v"]
            back = lambda a: v @ a @ v.conj().T
            d = aligned(k,f,y)
            for key,val in (
                ("aligned_kernel", np.linalg.norm(back(r["k"])-d["k"])/max(1,np.linalg.norm(k))),
                ("aligned_load", np.linalg.norm(back(r["y"])-d["y"])),
                ("inherited_formation", np.linalg.norm(back(r["f"])-f)/max(1,np.linalg.norm(f))),
                ("inherited_witness", np.linalg.norm(back(r["w"])-w)),
                ("trace_kernel", abs(np.trace(r["k"])-np.trace(k))/max(1,np.linalg.norm(k))),
                ("trace_formation", abs(np.trace(r["f"])-np.trace(f))/max(1,np.linalg.norm(f))),
                ("channel_unital", np.linalg.norm(d["tc"]@d["tc"]+d["tb"]@d["tb"]-np.eye(n))),
            ):
                maxima[key] = max(maxima[key],float(val))
            # A is transported as a FIXED source observable, not replaced by Y_+.
            conserved = np.trace(y @ d["k"])-np.trace(y @ k)
            maxima["charge_commutant"] = max(maxima["charge_commutant"],float(abs(conserved))/max(1,np.linalg.norm(k)))
            eig,evec = np.linalg.eigh(y)
            kb = evec.conj().T @ k @ evec
            alpha = d["alpha"]
            weights = np.sqrt(alpha+(1-alpha)*eig*eig)
            hij = (alpha+(1-alpha)*np.outer(eig,eig))/np.outer(weights,weights)
            expected_loss = np.sum((1-hij*hij)*np.abs(kb)**2).real
            actual_loss = np.trace(k@k).real-np.trace(d["k"]@d["k"]).real
            assert actual_loss >= -TOL
            maxima["hs_dissipation_identity"] = max(maxima["hs_dissipation_identity"],
                float(abs(actual_loss-expected_loss))/max(1,np.linalg.norm(k)**2))
            if case < 3:
                g = complex_unitary(rng,n)
                conj = lambda a: g @ a @ g.conj().T
                s = update(conj(k),conj(f),conj(w),conj(y),np.eye(n))
                assert s["terminal"] is None
                sb = lambda a: s["v"] @ a @ s["v"].conj().T
                for label,original,shifted in (
                    ("gauge_kernel",back(r["k"]),sb(s["k"])),
                    ("gauge_load",back(r["y"]),sb(s["y"])),
                    ("gauge_formation",back(r["f"]),sb(s["f"]))):
                    error=np.linalg.norm(shifted-conj(original))/max(1,np.linalg.norm(original))
                    maxima[label]=max(maxima[label],float(error))
            dimensions.append(n)
    assert max(maxima.values()) < TOL
    return dict(preparations=len(dimensions), dimensions=[2,3,4,5],
                gauge_controls=12, maximum_residuals=maxima)

def witnesses(update):
    eye,sx,sy,sz = pauli()
    f=np.array([[1.,.5],[.5,1.]])
    ya=np.diag([.25,.5]); yb=.375*eye
    a=update(sx,f,eye/2,ya,eye); b=update(sx,f,eye/2,yb,eye)
    assert a["terminal"] is None and b["terminal"] is None
    readout=lambda y: np.array([2,np.trace(sx).real,np.trace(f).real,1,np.trace(y).real,np.trace(f@sx).real])
    assert np.array_equal(readout(ya),readout(yb))
    ea=np.trace(a["f"]@a["k"]).real
    eb=np.trace(b["f"]@b["k"]).real
    h=np.sqrt(1152/1295)
    assert abs(ea-h)<TOL and abs(eb-1)<TOL and eb-ea>.05
    p=np.diag([1.,0.])
    c=update(-eye,p,p,.5*eye,p)
    assert c["terminal"] is None and len(c["y"])==1
    assert abs(np.trace(c["k"]).real+1)<TOL
    v=np.array([np.sqrt(3)/2,.5]); p=np.outer(v,v)
    s=update(np.diag([-1.,-2.]),p,p,ya,p)
    assert s["terminal"] is None and len(s["y"])==2
    assert np.linalg.norm(s["k"]+1.25*eye)<TOL
    assert abs(np.trace(s["f"]).real-2.25)<TOL
    # Actual complete source update on a positive determinant-null kernel.
    null=eye+sx
    out=update(null,f,eye/2,ya,eye)
    assert out["terminal"] is None
    aligned_null=out["v"]@out["k"]@out["v"].conj().T
    defect=qdet(aligned_null)
    assert abs(qdet(null))<TOL and abs(defect-143/1295)<TOL and defect>.1
    return dict(fiber_input=readout(ya).tolist(), energy_weighted_outputs=[float(ea),float(eb)],
                fiber_successor_gap=float(eb-ea), rank_drop_trace=[-2.,float(np.trace(c["k"]).real)],
                seeded_trace=[-3.,float(np.trace(s["k"]).real)],
                seeded_formation=[1.,float(np.trace(s["f"]).real)],
                null_input=float(qdet(null)), null_output=float(defect),
                pauli_channel=[1.,float(h),float(h),1.])

def cone_and_metric_controls(update):
    rng=np.random.default_rng(SEED+1)
    eye=np.eye(2); f=np.array([[1.,.5],[.5,1.]]); y=np.diag([.25,.5])
    max_det_error=0.; max_unitary_error=0.; max_sl_error=0.
    min_output_eigenvalue=float("inf")
    for _ in range(16):
        x=pos(rng,2)
        q=qdet(x); determinant=np.linalg.det(x).real
        max_det_error=max(max_det_error,abs(q-determinant)/max(1,abs(determinant)))
        r=update(x,f,eye/2,y,eye)
        assert r["terminal"] is None
        min_output_eigenvalue=min(min_output_eigenvalue,float(np.linalg.eigvalsh(r["k"]).min()))
        u=complex_unitary(rng,2)
        max_unitary_error=max(max_unitary_error,abs(qdet(u@x@u.conj().T)-q)/max(1,abs(q)))
        # det A=1; this is a mathematical comparison, NOT a source boost law.
        a=np.diag([np.exp(.2),np.exp(-.2)])
        max_sl_error=max(max_sl_error,abs(qdet(a@x@a.conj().T)-q)/max(1,abs(q)))
    assert min_output_eigenvalue>0 and max(max_det_error,max_unitary_error,max_sl_error)<TOL
    pullback_min=[]
    for n in (2,3,4,5):
        g=np.eye(n)+pos(rng,n)
        e=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        assert abs(np.linalg.det(e))>1e-12
        pullback_min.append(float(np.linalg.eigvalsh(e.conj().T@g@e).min()))
    assert min(pullback_min)>0
    return dict(positive_cone_controls=16, determinant_residual=float(max_det_error),
                unitary_residual=float(max_unitary_error), sl2_comparison_residual=float(max_sl_error),
                minimum_output_eigenvalue=min_output_eigenvalue,
                positive_pullback_dimensions=[2,3,4,5], minimum_pullback_eigenvalues=pullback_min)

def derivative_control(update):
    eye,sx,_,_=pauli(); e=eye+sx
    lam=224/675; a=16/135
    expected=lam*eye+a*sx
    y=.5*eye
    def source_m(z):
        r=update(np.zeros((2,2)),eye,eye/2,z,eye)
        assert r["terminal"] is None
        return r["v"]@r["y"]@r["v"].conj().T
    errors=[]
    for h in (1e-4,1e-5,1e-6):
        actual=(source_m(y+h*e)-source_m(y-h*e))/(2*h)
        errors.append(dict(h=h,norm_error=float(np.linalg.norm(actual-expected)),
                           determinant=float(qdet(actual))))
    assert min(row["norm_error"] for row in errors)<1e-7
    return dict(analytic_temporal=lam,analytic_spatial=a,
                analytic_determinant=43776/455625,central_differences=errors)

def scalar_controls():
    def f(y): return 2*y*y/((1+y)**2*(1+y*y))
    ratios=[]
    for y in [R(i,20) for i in range(1,20)]:
        assert 0<f(y)<y
        ratios.append(str(f(y)/y))
    # Fixed-point clock contradiction is exact and independent of root finding.
    # Verify the declared driven equilibrium numerically only as a corroboration.
    from scipy.optimize import brentq
    d=.15
    fixed=brentq(lambda y:f(y+d)-y,0,.25)
    assert abs(f(fixed+d)-fixed)<1e-12
    return dict(exact_scalar_rational_cases=19,
                driven_input=d,driven_fixed_point=float(fixed),
                clock_identity_at_fixed_point="N(y*)-N(y*)=0, not 1",
                invariant_theorem_boundary="continuous at attracting limit; other invariants fixed")

def general_flux_controls(update):
    rng=np.random.default_rng(SEED+2)
    residuals=[]; trace_residuals=[]; records=[]
    for n in (2,3,4,5):
        for case in range(6):
            basis=complex_unitary(rng,n)
            rank=max(1,n//2)
            p=basis[:,:rank]@basis[:,:rank].conj().T
            ybasis=complex_unitary(rng,n)
            y=(ybasis*np.linspace(.15,.8,n))@ybasis.conj().T
            f=p@pos(rng,n)@p
            w=p/rank
            k=-pos(rng,n)
            r=update(k,f,w,y,p)
            record=dict(n=n,rank_p=rank,terminal=r["terminal"])
            if r["terminal"] is None:
                uc,ub=r["u"][:n,:],r["u"][n:,:]
                d=uc@uc.conj().T+ub@ub.conj().T
                delta=np.trace(r["k"]).real-np.trace(k).real
                predicted=np.trace(k@(d-np.eye(n))).real
                error=abs(delta-predicted)/max(1,np.linalg.norm(k))
                residuals.append(float(error))
                trace_residuals.append(float(abs(np.trace(d)-len(r["y"]))))
                record.update(successor_dimension=len(r["y"]),kernel_change=float(delta),
                              signed_outflow=float(-predicted),residual=float(error),
                              max_export_operator_eigenvalue=float(np.linalg.eigvalsh(d).max()))
            records.append(record)
    assert residuals and max(residuals)<TOL and max(trace_residuals)<TOL
    # A multi-event trace balance, with real source events and no added reservoir dynamics.
    n=3
    u=complex_unitary(rng,n); p=u[:,:2]@u[:,:2].conj().T
    y=.2*np.eye(n)+.4*np.diag([.1,.5,.9])
    state=(-pos(rng,n),p,p/2,y,p)
    initial=float(np.trace(state[0]).real); flux=0.; steps=0; trajectory_terminal=None
    numerical_stop=None
    for _ in range(6):
        k,f,w,y,p=state
        try:
            r=update(k,f,w,y,p)
        except ArithmeticError as error:
            numerical_stop=dict(event=steps+1,error=str(error),
                                maximum_load_eigenvalue=float(np.linalg.eigvalsh(y).max()))
            break
        if r["terminal"]:
            trajectory_terminal=r["terminal"]; break
        uc,ub=r["u"][:len(y),:],r["u"][len(y):,:]
        d=uc@uc.conj().T+ub@ub.conj().T
        flux+=float(np.trace(k@(np.eye(len(y))-d)).real)
        state=(r["k"],r["f"],r["w"],r["y"],r["p"])
        steps+=1
    assert steps>0
    final=float(np.trace(state[0]).real)
    trajectory_error=abs(final+flux-initial)
    assert trajectory_error<1e-10*max(1,abs(initial))
    return dict(preparations=24,nonterminal=len(residuals),
                terminal_count=24-len(residuals),max_balance_residual=max(residuals),
                max_isometry_trace_residual=max(trace_residuals),cases=records,
                trajectory=dict(nonterminal_steps=steps,terminal=trajectory_terminal,
                                numerical_stop=numerical_stop,
                                initial_trace=initial,final_trace=final,
                                cumulative_signed_flux=flux,residual=trajectory_error))


def run():
    update=load_update()
    result=dict(scope="finite mathematical controls only; no physical or Einstein completion",
                source_commit="457f23df6d9ccb15cf17916f3c3eac113b23c370",
                source_git_blob=EXPECTED_SOURCE_BLOB,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__),
                exact=exact_certificates(),
                full_update=random_controls(update),
                counterexamples=witnesses(update),
                complete_event_flux=general_flux_controls(update),
                geometry=cone_and_metric_controls(update),
                derivative=derivative_control(update),
                scalar=scalar_controls(),
                status="PARTIAL: finite assertions pass; six-event trajectory numerically stops at event 6; physical gates OPEN")
    return result

if __name__ == "__main__":
    data=run()
    # SymPy Integer entries become plain ints for a stable JSON certificate.
    text=json.dumps(data,indent=2,default=lambda x:int(x))+"\n"
    (HERE/"results.json").write_text(text,encoding="utf-8")
    print(text)

