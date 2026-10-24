"""Exact two-mode/environment-factor controls against the pinned full BFG update."""
from __future__ import annotations
import json
import platform
from pathlib import Path
import numpy as np
import sympy as s
import audit

HERE=Path(__file__).resolve().parent
TOL=1e-10
SEED=20261024

def b(y): return y*y/(1+y)
def h(y): return (1+y*y)/(1+y)
def alpha_exact(ys, weights):
    return s.cancel(sum(w*b(y) for y,w in zip(ys,weights))/
                    sum(w*h(y) for y,w in zip(ys,weights)))
def g(y,alpha): return (alpha+(1-alpha)*y*y)/(1+y)**2

def exact():
    # P1: a natural initial spectral pair is not instantaneously reselected invariantly.
    ys=list(map(s.Rational,["1/10","1/2","9/10"]))
    weights=list(map(s.Rational,[1,1,10]))
    alpha=alpha_exact(ys,weights)
    yp=[s.cancel(g(y,alpha)) for y in ys]
    assert yp[0]>yp[2]>yp[1]
    # P2: identical local pair block, distinct source environmental formation.
    ys2=list(map(s.Rational,["1/4","1/2","3/4"]))
    a1=alpha_exact(ys2,[1,1,1])
    a2=alpha_exact(ys2,[1,1,2])
    assert a1==s.Rational(113,541) and a2==s.Rational(361,1457)
    gap=s.cancel(g(ys2[0],a2)-g(ys2[0],a1))
    assert gap>0
    # P3: equal current alpha and pair block, but distinct next alpha.
    ys3=list(map(s.Rational,["1/4","1/2","2/3","3/4"]))
    a0=alpha_exact(ys3,[1]*4)
    d=[s.cancel(b(y)-a0*h(y)) for y in ys3]
    ws=[s.S(1),s.S(1),1+d[3],1-d[2]]
    assert min(ws)>0
    assert s.cancel(alpha_exact(ys3,ws)-a0)==0
    nextys=[s.cancel(g(y,a0)) for y in ys3]
    anext0=alpha_exact(nextys,[1]*4)
    anext1=alpha_exact(nextys,ws)
    nextgap=s.cancel(anext1-anext0)
    assert nextgap!=0
    secondgap=s.cancel(g(nextys[0],anext1)-g(nextys[0],anext0))
    assert secondgap!=0
    return dict(selector=dict(y=list(map(str,ys)),weights=list(map(str,weights)),
                             alpha=str(alpha),successors=list(map(str,yp)),
                             initial_pair=[0,1],instantaneous_next_pair=[1,2]),
                pair_fiber=dict(y=list(map(str,ys2)),alphas=[str(a1),str(a2)],
                                first_successor_y_gap=str(gap),gap_float=float(gap)),
                alpha_fiber=dict(y=list(map(str,ys3)),weights0=["1"]*4,
                                 weights1=list(map(str,ws)),initial_alpha=str(a0),
                                 common_successor_y=list(map(str,nextys)),
                                 next_alphas=[str(anext0),str(anext1)],
                                 next_alpha_gap=str(nextgap),
                                 next_alpha_gap_float=float(nextgap),
                                 second_pair_y_gap=str(secondgap),
                                 second_pair_y_gap_float=float(secondgap)))

def source_aligned(update,k,f,w,y):
    r=update(k,f,w,y,np.eye(len(y)))
    if r["terminal"] is not None:
        raise RuntimeError("Unexpected source terminal: "+str(r["terminal"]))
    v=r["v"]
    back=lambda x:v@x@v.conj().T
    return dict(k=back(r["k"]),f=back(r["f"]),w=back(r["w"]),y=back(r["y"]),
                alpha=r["alpha"])

def pair_step(k,f,y,env_y,env_weight):
    """Sufficient source-derived factor; global alpha computed, not fitted."""
    eye=np.eye(2)
    c=np.linalg.inv(eye+y); by=y@c
    load_c=np.trace(f@c).real+np.sum(env_weight/(1+env_y))
    load_b=np.trace(f@y@y@c).real+np.sum(env_weight*b(env_y))
    alpha=load_b/(load_c+load_b)
    m=alpha*c@c+(1-alpha)*by@by
    im=audit.hermitian_function(m,lambda x:1/np.sqrt(x))
    tc=np.sqrt(alpha)*c@im
    tb=np.sqrt(1-alpha)*by@im
    return dict(k=tc@k@tc+tb@k@tb,y=m,f=f,
                env_y=g(env_y,alpha),env_weight=env_weight,alpha=alpha)

def source_witnesses(update,e):
    eye2=np.eye(2); sx=audit.pauli()[1]
    y=np.diag([.25,.5,.75]); k=np.zeros((3,3)); k[:2,:2]=sx
    w=np.eye(3)/3
    states=[source_aligned(update,k,np.diag([1.,1.,v]),w,y) for v in (1.,2.)]
    gap=states[1]["y"][0,0].real-states[0]["y"][0,0].real
    assert abs(gap-e["pair_fiber"]["gap_float"])<TOL
    ys=np.array([.1,.5,.9])
    selector=source_aligned(update,k,np.diag([1.,1.,10.]),w,np.diag(ys))
    order=np.argsort(np.diag(selector["y"]).real).tolist()
    assert order[:2]==[1,2]
    ys3=np.array([.25,.5,2/3,.75])
    weights1=np.array([float(s.Rational(x)) for x in e["alpha_fiber"]["weights1"]])
    k=np.zeros((4,4)); k[:2,:2]=sx; w=np.eye(4)/4
    r0=source_aligned(update,k,np.eye(4),w,np.diag(ys3))
    r1=source_aligned(update,k,np.diag(weights1),w,np.diag(ys3))
    assert abs(r0["alpha"]-r1["alpha"])<TOL
    assert np.linalg.norm(r0["y"]-r1["y"])<TOL
    t0=source_aligned(update,r0["k"],r0["f"],r0["w"],r0["y"])
    t1=source_aligned(update,r1["k"],r1["f"],r1["w"],r1["y"])
    nextgap=t1["alpha"]-t0["alpha"]
    secondgap=t1["y"][0,0].real-t0["y"][0,0].real
    assert abs(nextgap-e["alpha_fiber"]["next_alpha_gap_float"])<TOL
    assert abs(secondgap-e["alpha_fiber"]["second_pair_y_gap_float"])<TOL
    assert abs(nextgap)>1e-8 and abs(secondgap)>1e-8
    return dict(selector_next_order=order,pair_successor_gap=float(gap),
                equal_alpha_first_step_residual=float(abs(r0["alpha"]-r1["alpha"])),
                next_alpha_gap=float(nextgap),second_pair_y_gap=float(secondgap))

def random_factor_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(pair_k=0.,pair_y=0.,pair_f=0.,pair_w=0.,environment_y=0.,
                environment_weights=0.,alpha=0.,pair_trace_k=0.,gauge_pair=0.)
    offblocks=[]; source_events=0; cases=[]; gauge_count=0
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n)
            z=u[:,:2]; ze=u[:,2:]
            y=(u*np.linspace(.2,.8,n))@u.conj().T
            f=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            kk=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            k=(kk+kk.conj().T)/2
            offblocks.append(dict(n=n,k=float(np.linalg.norm(z.conj().T@k@ze)),
                                  f=float(np.linalg.norm(z.conj().T@f@ze)),
                                  w=float(np.linalg.norm(z.conj().T@w@ze))))
            pair=dict(k=z.conj().T@k@z,f=z.conj().T@f@z,
                      y=z.conj().T@y@z,env_y=np.linspace(.2,.8,n)[2:],
                      env_weight=np.diag(ze.conj().T@f@ze).real)
            pair_w=z.conj().T@w@z
            if case==0:
                gu=audit.complex_unitary(rng,n); gz=gu@z
                conv=lambda a:gu@a@gu.conj().T
                direct=source_aligned(update,k,f,w,y)
                changed=source_aligned(update,conv(k),conv(f),conv(w),conv(y))
                err=np.linalg.norm(gz.conj().T@changed["k"]@gz-z.conj().T@direct["k"]@z)/max(1,np.linalg.norm(k))
                maxima["gauge_pair"]=max(maxima["gauge_pair"],float(err)); gauge_count+=1
            first_trace=np.trace(pair["k"]).real
            for event in range(3):
                local=pair_step(**pair)
                full=source_aligned(update,k,f,w,y); source_events+=1
                expected_k=z.conj().T@full["k"]@z
                expected_y=z.conj().T@full["y"]@z
                env_eigs=np.diag(ze.conj().T@full["y"]@ze).real
                env_weights=np.diag(ze.conj().T@full["f"]@ze).real
                errors=dict(
                    pair_k=np.linalg.norm(local["k"]-expected_k)/max(1,np.linalg.norm(k)),
                    pair_y=np.linalg.norm(local["y"]-expected_y),
                    pair_f=np.linalg.norm(local["f"]-z.conj().T@full["f"]@z)/max(1,np.linalg.norm(f)),
                    pair_w=np.linalg.norm(pair_w-z.conj().T@full["w"]@z),
                    environment_y=np.linalg.norm(local["env_y"]-env_eigs),
                    environment_weights=np.linalg.norm(local["env_weight"]-env_weights)/max(1,np.linalg.norm(f)),
                    alpha=abs(local["alpha"]-full["alpha"]),
                    pair_trace_k=abs(np.trace(local["k"]).real-first_trace)/max(1,np.linalg.norm(k)))
                for key,error in errors.items():maxima[key]=max(maxima[key],float(error))
                cases.append(dict(n=n,case=case,event=event+1,alpha=float(full["alpha"]),
                                  maximum_residual=float(max(errors.values()))))
                k,f,w,y=full["k"],full["f"],full["w"],full["y"]
                pair={key:local[key] for key in ("k","f","y","env_y","env_weight")}
    assert all(min(row[key] for row in offblocks)>1e-6 for key in ("k","f","w"))
    assert max(maxima.values())<TOL
    return dict(preparations=12,events_per_preparation=3,source_events=source_events,
                unitary_covariance_controls=gauge_count,maximum_residuals=maxima,
                offblock_norms=offblocks,cases=cases)

def run():
    update=audit.load_update()
    e=exact()
    return dict(scope="BFG-only autonomous full persistence; local pair plus source spectral environment",
                seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                pinned_source_blob=audit.EXPECTED_SOURCE_BLOB,
                exact=e,full_source_witnesses=source_witnesses(update,e),
                environment_factor=random_factor_controls(update),
                status="PASS for declared algebraic identities and finite source controls; physical spacetime/current OPEN")

if __name__=="__main__":
    data=run()
    text=json.dumps(data,indent=2)+"\n"
    (HERE/"pair_results.json").write_text(text,encoding="utf-8")
    print(json.dumps(dict(status=data["status"],source=data["pinned_source_blob"],
                         exact=data["exact"],witnesses=data["full_source_witnesses"],
                         controls={k:v for k,v in data["environment_factor"].items() if k not in ("cases","offblock_norms")}),indent=2))

