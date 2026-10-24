"""Invariant spectral-pair class and complementary-moment controls, BFG only."""
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
SEED=20261025

def f(y): return 2*y*y/((1+y)**2*(1+y*y))
def r(y): return y*y/(1+y*y)

def polynomial_certificate():
    x=s.symbols("x",positive=True)
    alpha=s.symbols("alpha",real=True)
    derivative=2*((1-alpha)*x-alpha)/(1+x)**3
    assert s.cancel(s.diff(pair_audit.g(x,alpha),x)-derivative)==0
    p=4+4*x+12*x*x+6*x**3+12*x**4-8*x**5+4*x**6-15*x**7
    lower=4+4*x+12*x*x+6*x**3+s.Rational(49,8)*x**4+4*x**6
    remainder=x**4*(s.Rational(1,2)-x)*(8+15*(x*x+x/2+s.Rational(1,4)))
    assert s.expand(p-lower-remainder)==0
    denom=(1+x)**4*(1+x*x)**2*(1+2*x*x)**2*(1+4*x**4)
    assert s.cancel(f(2*x*x)-2*f(x)**2-8*x**5*p/denom)==0
    assert all(c>0 for c in s.Poly(lower,x).coeffs())
    return dict(identity="f(2x^2)-2f(x)^2=8x^5 P(x)/D(x)",
                P=str(p),positive_lower_polynomial=str(lower),
                nonnegative_remainder=str(remainder),D=str(denom),
                domain="0<x<=1/2",fixed_alpha_derivative=str(derivative),
                conclusion="strictly positive on the declared domain")

def exact_classes():
    rows=[]
    for n in (2,3,4,5):
        for case in range(4):
            ys=[s.Rational(1,5)+s.Rational(case,1000)+s.Rational(i,10*(n-1)) for i in range(n)]
            weights=[1+s.Rational(i+case,n+1) for i in range(n)]
            for event in range(3):
                m,M=min(ys),max(ys)
                assert 0<m<=M<=s.Rational(1,2) and m>=2*M*M
                alpha=pair_audit.alpha_exact(ys,weights)
                assert r(m)<=alpha<=r(M)<m
                bound=2*(m-M*M)/((1+M*M)*(1+M)**3)
                gaps=[ys[i+1]-ys[i] for i in range(n-1)]
                nxt=[s.cancel(pair_audit.g(y,alpha)) for y in ys]
                nm,nM=min(nxt),max(nxt)
                assert nxt==sorted(nxt) and len(set(nxt))==n
                assert f(m)<=nm<=nM<=f(M)
                assert nm>2*nM*nM
                assert all(nxt[i+1]-nxt[i]>=bound*gaps[i] for i in range(n-1))
                rows.append(dict(n=n,case=case,event=event+1,
                                 current_minimum=float(m),current_maximum=float(M),
                                 alpha=float(alpha),gap_multiplier_lower_bound=float(bound),
                                 successor_minimum=float(nm),successor_maximum=float(nM),
                                 successor_class_margin=float(nm-2*nM*nM)))
                ys=nxt
    return dict(preparations=16,exact_events=len(rows),cases=rows)

def exact_moment_witness():
    pair=[s.Rational(1,5),s.Rational(9,40)]
    ea=[s.Rational(1,4),s.Rational(3,10)]
    eb=[s.Rational(13,50),s.Rational(29,100)]
    assert sum(ea)==sum(eb)==s.Rational(11,20)
    ya,yb=pair+ea,pair+eb
    assert min(ya)>2*max(ya)**2 and min(yb)>2*max(yb)**2
    aa=pair_audit.alpha_exact(ya,[1]*4)
    ab=pair_audit.alpha_exact(yb,[1]*4)
    gap=s.cancel(pair_audit.g(pair[0],aa)-pair_audit.g(pair[0],ab))
    assert aa!=ab and gap!=0
    return dict(pair=list(map(str,pair)),complement_a=list(map(str,ea)),
                complement_b=list(map(str,eb)),complement_m0="2",complement_m1="11/20",
                alphas=[str(aa),str(ab)],first_pair_successor_gap=str(gap),
                gap_float=float(gap))

def source_moment_check(update,cert):
    sx=audit.pauli()[1]
    k=np.zeros((4,4)); k[:2,:2]=sx
    y0=np.diag([.2,.225,.25,.3])
    y1=np.diag([.2,.225,.26,.29])
    a=pair_audit.source_aligned(update,k,np.eye(4),np.eye(4)/4,y0)
    b=pair_audit.source_aligned(update,k,np.eye(4),np.eye(4)/4,y1)
    gap=float((a["y"][0,0]-b["y"][0,0]).real)
    assert abs(gap-cert["gap_float"])<TOL
    assert abs(gap)>1e-8
    return dict(source_successor_gap=gap,exact_comparison_residual=abs(gap-cert["gap_float"]))

def full_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(pair_projector=0.,pair_y=0.,pair_k=0.,global_alpha=0.,class_violation=0.,gap_bound_violation=0.)
    cases=[]; events=0
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n); z=u[:,:2]; ze=u[:,2:]
            y=(u*np.linspace(.2,.3,n))@u.conj().T
            f0=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            k=(raw+raw.conj().T)/2
            local=dict(k=z.conj().T@k@z,f=z.conj().T@f0@z,y=z.conj().T@y@z,
                       env_y=np.linspace(.2,.3,n)[2:],env_weight=np.diag(ze.conj().T@f0@ze).real)
            for event in range(3):
                vals,vec=np.linalg.eigh(y); m,M=vals[0],vals[-1]
                assert m>2*M*M-TOL and M<=.5+TOL
                proj=vec[:,:2]@vec[:,:2].conj().T
                maxima["pair_projector"]=max(maxima["pair_projector"],float(np.linalg.norm(proj-z@z.conj().T)))
                lower=2*(m-M*M)/((1+M*M)*(1+M)**3)
                oldgaps=np.diff(vals)
                ext=pair_audit.pair_step(**local)
                full=pair_audit.source_aligned(update,k,f0,w,y)
                newvals=np.linalg.eigvalsh(full["y"])
                newprojvec=np.linalg.eigh(full["y"])[1][:,:2]
                maxima["pair_projector"]=max(maxima["pair_projector"],float(np.linalg.norm(newprojvec@newprojvec.conj().T-z@z.conj().T)))
                maxima["pair_k"]=max(maxima["pair_k"],float(np.linalg.norm(ext["k"]-z.conj().T@full["k"]@z)/max(1,np.linalg.norm(k))))
                maxima["pair_y"]=max(maxima["pair_y"],float(np.linalg.norm(ext["y"]-z.conj().T@full["y"]@z)))
                maxima["global_alpha"]=max(maxima["global_alpha"],float(abs(ext["alpha"]-full["alpha"])))
                violation=max(0.,float(2*newvals[-1]**2-newvals[0]))
                gap_violation=max(0.,float(np.max(lower*oldgaps-np.diff(newvals))))
                maxima["class_violation"]=max(maxima["class_violation"],violation)
                maxima["gap_bound_violation"]=max(maxima["gap_bound_violation"],gap_violation)
                cases.append(dict(n=n,case=case,event=event+1,
                                  source_min=float(newvals[0]),source_max=float(newvals[-1]),
                                  successor_class_margin=float(newvals[0]-2*newvals[-1]**2),
                                  minimum_gap=float(np.diff(newvals).min()),
                                  predicted_gap_lower_bound=float(lower*oldgaps.min())))
                k,f0,w,y=full["k"],full["f"],full["w"],full["y"]
                local={key:ext[key] for key in ("k","f","y","env_y","env_weight")}
                events+=1
    assert max(maxima.values())<TOL
    return dict(preparations=12,source_events=events,events_per_preparation=3,
                maximum_residuals=maxima,cases=cases)

def derivative_regressions(update):
    x=s.symbols("x",positive=True)
    fp=s.diff(f(x),x)
    rows=[]
    eye,sx,_,_=audit.pauli(); direction=eye+sx
    step=1e-5
    for value in (s.Rational(1,4),s.Rational(1,3),s.Rational(1,2)):
        a=s.cancel(2*value*(1-value)/((1+value*value)*(1+value)**3))
        lam=s.cancel(fp.subs(x,value))
        expected=float(lam)*eye+float(a)*sx
        y=float(value)*eye
        plus=pair_audit.source_aligned(update,np.zeros((2,2)),eye,eye/2,y+step*direction)["y"]
        minus=pair_audit.source_aligned(update,np.zeros((2,2)),eye,eye/2,y-step*direction)["y"]
        error=float(np.linalg.norm((plus-minus)/(2*step)-expected))
        assert error<1e-7
        rows.append(dict(y=str(value),traceless_derivative=str(a),scalar_derivative=str(lam),
                         finite_difference_step=step,norm_error=error))
    return rows


def run():
    update=audit.load_update()
    witness=exact_moment_witness()
    return dict(scope="Invariant full-persistence spectral class; no physical sector selection",
                seed=SEED,tolerance=TOL,source_blob=audit.EXPECTED_SOURCE_BLOB,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                polynomial=polynomial_certificate(),exact_class=exact_classes(),
                derivative_regressions=derivative_regressions(update),
                moment_witness=witness,source_moment=source_moment_check(update,witness),
                full_source=full_controls(update),
                status="PASS: class and finite selection/factor controls; physical current and clock remain OPEN")

if __name__=="__main__":
    result=run()
    (HERE/"stable_pair_results.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in ("exact_class","full_source")} |
                     dict(exact_class={k:v for k,v in result["exact_class"].items() if k!="cases"},
                          full_source={k:v for k,v in result["full_source"].items() if k!="cases"}),indent=2))

