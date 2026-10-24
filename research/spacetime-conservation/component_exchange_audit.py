"""Source-derived pair-component identities and scoped compensation obstructions."""
from __future__ import annotations
import json
import platform
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

HERE=Path(__file__).resolve().parent
TOL=1e-10
SEED=20261026

def comm(a,b):return a@b-b@a

def factors(y,alpha):
    c=np.linalg.inv(np.eye(2)+y); b=y@c
    m=alpha*c@c+(1-alpha)*b@b
    im=audit.hermitian_function(m,lambda x:1/np.sqrt(x))
    return [np.sqrt(alpha)*c@im,np.sqrt(1-alpha)*b@im]

def phi(k,ts):return sum(t@k@t for t in ts)
def branch_matrix(k,ts):
    return np.array([[np.trace(a@k@b) for b in ts] for a in ts])

def exact_witness():
    ys=[s.Rational(1,5),s.Rational(1,4),s.Rational(3,10)]
    alpha=pair_audit.alpha_exact(ys,[1,1,1])
    assert alpha==s.Rational(119,1993)
    tc=[s.sqrt(alpha/(alpha+(1-alpha)*y*y)) for y in ys[:2]]
    tb=[s.sqrt((1-alpha)*y*y/(alpha+(1-alpha)*y*y)) for y in ys[:2]]
    ts=[s.diag(*tc),s.diag(*tb)]
    h=s.simplify(tc[0]*tc[1]+tb[0]*tb[1])
    h2=s.simplify(h*h)
    assert h2==s.Rational(9048258,9159761)
    assert 0<h2<1
    sx=s.Matrix([[0,1],[1,0]]); eye=s.eye(2)
    plus,minus=eye+sx,eye-sx
    ph=lambda k:sum((t*k*t for t in ts),s.zeros(2))
    assert s.simplify(ph(plus)-(eye+h*sx))==s.zeros(2)
    assert s.simplify(ph(minus)-(eye-h*sx))==s.zeros(2)
    # Exact double-commutator and quadratic pairing for the positive witness.
    double=sum((t*(t*plus-plus*t)-(t*plus-plus*t)*t for t in ts),s.zeros(2))
    assert s.simplify(ph(plus)-plus+double/2)==s.zeros(2)
    cs=[t*plus-plus*t for t in ts]
    norm2=sum(s.trace(c.conjugate().T*c) for c in cs)
    assert s.simplify(s.trace(plus*(plus-ph(plus)))-norm2/2)==0
    v=ts[0].col_join(ts[1])
    assert s.simplify(v.conjugate().T*v-eye)==s.zeros(2)
    branch=lambda k:s.Matrix(2,2,lambda i,j:s.trace(ts[i]*k*ts[j]))
    assert s.simplify(branch(plus)-branch(minus))==s.zeros(2)
    inv=eye+sx/h
    invdet=s.simplify(inv.det())
    assert invdet==s.Rational(-111503,9048258)
    return dict(alpha=str(alpha),h_squared=str(h2),h=str(h),h_float=float(h),
                plus_components_before=[1,1,0,0],
                plus_components_after=["1",str(h),"0","0"],
                null_to_timelike_defect=str(1-h2),
                opposite_transverse_defect_difference=str(2*(1-h)),
                inverse_cone_determinant=str(invdet),
                branch_marginal_difference="zero matrix",
                double_commutator_identity="exactly zero",
                pairing_identity="exactly zero")

def exact_source_check(update,cert):
    eye=np.eye(3); sx=audit.pauli()[1]
    y=np.diag([.2,.25,.3]); f=eye.copy(); f[0,1]=f[1,0]=.5
    w=eye/3; perturb=np.zeros((3,3)); perturb[:2,:2]=sx
    a=pair_audit.source_aligned(update,eye+perturb,f,w,y)
    b=pair_audit.source_aligned(update,eye-perturb,f,w,y)
    ha=audit.coordinates(a["k"][:2,:2]); hb=audit.coordinates(b["k"][:2,:2])
    h=cert["h_float"]
    assert np.linalg.norm(ha-np.array([1,h,0,0]))<TOL
    assert np.linalg.norm(hb-np.array([1,-h,0,0]))<TOL
    outside_error=max(np.linalg.norm(a[key]-b[key]) for key in ("f","w","y"))
    outside_error=max(outside_error,abs(a["k"][2,2]-b["k"][2,2]),
                      np.linalg.norm(a["k"][:2,2]-b["k"][:2,2]))
    assert outside_error<TOL
    assert abs((ha[1]-hb[1])-2*h)<TOL
    return dict(plus_components=ha.tolist(),minus_components=hb.tolist(),
                outside_successor_difference=float(outside_error),
                incompatible_required_compensator_increments=[1-h,-(1-h)])

def full_controls(update):
    rng=np.random.default_rng(SEED)
    sx,sy=audit.pauli()[1:3]
    maxima=dict(pauli_map=0.,double_commutator=0.,pairing=0.,
                complement_successor=0.,isometry=0.,lift_recovery=0.,
                partial_trace=0.,branch_insensitivity=0.,inverse_map=0.,history_dual_charges=0.)
    min_damping=1.; min_inverse_negative=0.; rows=[]; offblock_inputs=[]
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n); z=u[:,:2]; ze=u[:,2:]
            y=(u*np.linspace(.2,.3,n))@u.conj().T
            f=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            k=(raw+raw.conj().T)/2
            offblock=dict(n=n,case=case,k=float(np.linalg.norm(z.conj().T@k@ze)),
                          f=float(np.linalg.norm(z.conj().T@f@ze)),
                          w=float(np.linalg.norm(z.conj().T@w@ze)))
            assert min(offblock[key] for key in ("k","f","w"))>1e-6
            offblock_inputs.append(offblock)
            initial_components=audit.coordinates(z.conj().T@k@z)
            history_h=1.
            for event in range(2):
                transverse=sx if case%2==0 else sy
                perturb=z@transverse@z.conj().T
                plus=pair_audit.source_aligned(update,k+perturb,f,w,y)
                minus=pair_audit.source_aligned(update,k-perturb,f,w,y)
                alpha=plus["alpha"]
                yp=z.conj().T@y@z
                ts=factors(yp,alpha)
                cp=z.conj().T@(k+perturb)@z
                actual=z.conj().T@plus["k"]@z
                expected=phi(cp,ts)
                norm=max(1,np.linalg.norm(cp))
                vals=np.diag(yp).real
                h=(alpha+(1-alpha)*vals[0]*vals[1])/np.sqrt(
                    (alpha+(1-alpha)*vals[0]**2)*(alpha+(1-alpha)*vals[1]**2))
                coords=audit.coordinates(cp); predicted=coords*np.array([1,h,h,1])
                maxima["pauli_map"]=max(maxima["pauli_map"],float(np.linalg.norm(audit.coordinates(actual)-predicted)/norm))
                double=sum(comm(t,comm(t,cp)) for t in ts)
                maxima["double_commutator"]=max(maxima["double_commutator"],float(np.linalg.norm(actual-cp+double/2)/norm))
                norm2=sum(np.linalg.norm(comm(t,cp))**2 for t in ts)
                pairing=np.trace(cp@(cp-actual)).real
                maxima["pairing"]=max(maxima["pairing"],float(abs(pairing-norm2/2)/max(1,norm**2)))
                outside=max(np.linalg.norm(plus[key]-minus[key]) for key in ("f","w","y"))
                outside=max(outside,np.linalg.norm(ze.conj().T@(plus["k"]-minus["k"])@ze),
                            np.linalg.norm(z.conj().T@(plus["k"]-minus["k"])@ze))
                maxima["complement_successor"]=max(maxima["complement_successor"],float(outside/max(1,np.linalg.norm(k))))
                v=np.vstack(ts); joint=v@cp@v.conj().T
                maxima["isometry"]=max(maxima["isometry"],float(np.linalg.norm(v.conj().T@v-np.eye(2))))
                maxima["lift_recovery"]=max(maxima["lift_recovery"],float(np.linalg.norm(v.conj().T@joint@v-cp)/norm))
                partial=joint[:2,:2]+joint[2:,2:]
                maxima["partial_trace"]=max(maxima["partial_trace"],float(np.linalg.norm(partial-actual)/norm))
                cm=z.conj().T@(k-perturb)@z
                maxima["branch_insensitivity"]=max(maxima["branch_insensitivity"],float(np.linalg.norm(branch_matrix(cp,ts)-branch_matrix(cm,ts))/norm))
                inverse=np.eye(2)+sx/h
                maxima["inverse_map"]=max(maxima["inverse_map"],float(np.linalg.norm(phi(inverse,ts)-(np.eye(2)+sx))))
                inverse_eigen=float(np.linalg.eigvalsh(inverse).min())
                assert inverse_eigen<0 and 0<h<1
                min_inverse_negative=min(min_inverse_negative,inverse_eigen)
                min_damping=min(min_damping,float(1-h))
                rows.append(dict(n=n,case=case,event=event+1,alpha=float(alpha),
                                 damping_factor=float(h),transverse_loss_fraction=float(1-h),
                                 inverse_minimum_eigenvalue=inverse_eigen,
                                 complement_difference=float(outside)))
                # Continue the true unperturbed source trajectory by linearity in K.
                k=(plus["k"]+minus["k"])/2
                history_h*=h
                dual=audit.coordinates(z.conj().T@k@z)/np.array([1.,history_h,history_h,1.])
                maxima["history_dual_charges"]=max(maxima["history_dual_charges"],float(np.linalg.norm(dual-initial_components)/max(1,np.linalg.norm(initial_components))))
                f,w,y=plus["f"],plus["w"],plus["y"]
    assert max(maxima.values())<TOL and min_damping>1e-8
    return dict(preparations=12,events_per_preparation=2,paired_events=len(rows),
                full_source_calls=2*len(rows),maximum_residuals=maxima,
                minimum_transverse_loss_fraction=min_damping,
                most_negative_inverse_eigenvalue=min_inverse_negative,
                offblock_inputs=offblock_inputs,cases=rows)

def run():
    update=audit.load_update()
    cert=exact_witness()
    return dict(scope="Stable full-persistence BFG pair; fixed linear local charges and independent complement compensation",
                seed=SEED,tolerance=TOL,source_blob=audit.EXPECTED_SOURCE_BLOB,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=cert,source_witness=exact_source_check(update,cert),
                full_source=full_controls(update),
                status="PASS for scoped identities/obstructions; nonlinear joint current and physical conservation OPEN")

if __name__=="__main__":
    result=run()
    (HERE/"component_exchange_results.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k!="full_source"} |
                     dict(full_source={k:v for k,v in result["full_source"].items() if k not in ("cases","offblock_inputs")}),indent=2))

