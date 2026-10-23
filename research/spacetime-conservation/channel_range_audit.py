"""Exact and approximate channel range on a declared internal path graph."""
from __future__ import annotations
import json
import platform
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit
import mode_graph_audit

HERE=Path(__file__).resolve().parent
TOL=1e-10
SEED=20261102

def path_y(n,epsilon):
    return np.eye(n)/4+epsilon*(np.eye(n,k=1)+np.eye(n,k=-1))

def reduced_operators(f,y):
    alpha=audit.aligned(np.eye(len(y)),f,y)['alpha']; beta=1-alpha
    d=alpha*np.eye(len(y))+beta*y@y
    inv=audit.hermitian_function(d,lambda z:1/np.sqrt(z))
    return alpha,d,np.sqrt(alpha)*inv,np.sqrt(beta)*y@inv

def exact_checks():
    a,b,z=s.symbols('a b z',positive=True)
    tc=s.sqrt(a)/s.sqrt(a+b*z*z)
    derivative=s.sqrt(a)*b*(2*b*z*z-a)/(a+b*z*z)**s.Rational(5,2)
    assert s.simplify(s.diff(tc,z,2)-derivative)==0
    y=s.eye(3)/4+s.Rational(1,40)*s.Matrix([[0,1,0],[1,0,1],[0,1,0]])
    f=s.diag(1,2,3); c=(s.eye(3)+y).inv()
    lc=s.trace(f*c); lb=s.trace(f*y*y*c); alpha=s.cancel(lb/(lc+lb)); beta=1-alpha
    m=s.Rational(1,4)-s.sqrt(2)/40; M=s.Rational(1,4)+s.sqrt(2)/40
    assert s.simplify(2*m*m-M*M)>0 and s.simplify(M*M-alpha/beta)>0
    assert s.simplify(2*m*m-M*M-(102-60*s.sqrt(2))/1600)==0
    fun_c=lambda q:s.sqrt(alpha)/s.sqrt(alpha+beta*q*q)
    fun_b=lambda q:s.sqrt(beta)*q/s.sqrt(alpha+beta*q*q)
    ec=(fun_c(m)+fun_c(M)-2*fun_c(s.Rational(1,4)))/4
    eb=(fun_b(m)+fun_b(M)-2*fun_b(s.Rational(1,4)))/4
    transition=ec*ec+eb*eb
    coefficients=[s.binomial(2*j,j)/4**j for j in range(5)]
    assert all(0<value<=1 for value in coefficients)
    return dict(alpha=str(alpha),minimum_eigenvalue=str(m),maximum_eigenvalue=str(M),
                convexity_gap=str(s.simplify(2*m*m-M*M)),convexity_proof='alpha/beta <= M^2 < 2m^2',
                endpoint_C_50digits=str(s.N(ec,50)),endpoint_B_50digits=str(s.N(eb,50)),
                endpoint_transition_50digits=str(s.N(transition,50)),
                endpoint_C_float=float(ec.evalf()),endpoint_transition_float=float(transition.evalf()),
                binomial_coefficients=list(map(str,coefficients)))

def polynomial_checks(y,alpha,d,tc,tb):
    ds=np.linalg.eigvalsh(d); center=float((ds[0]+ds[-1])/2)
    radius=float((ds[-1]-ds[0])/(ds[-1]+ds[0])); assert 0<=radius<1
    h=np.eye(len(y))-d/center; power=np.eye(len(y)); series=np.zeros_like(y)
    rows=[]
    for N in range(3):
        series+=float(s.binomial(2*N,N)/4**N)*power
        inverse=series/np.sqrt(center)
        ca=np.sqrt(alpha)*inverse; ba=np.sqrt(1-alpha)*y@inverse
        cb=np.sqrt(alpha/center)*radius**(N+1)/(1-radius)
        bb=np.sqrt((1-alpha)/center)*np.linalg.norm(y,2)*radius**(N+1)/(1-radius)
        ce=float(np.linalg.norm(tc-ca,2)); be=float(np.linalg.norm(tb-ba,2))
        assert ce<=cb+TOL and be<=bb+TOL
        distance=np.abs(np.arange(len(y))[:,None]-np.arange(len(y))[None,:])
        cfar=ca[distance>2*N]; bfar=ba[distance>2*N+1]
        forbidden=max(float(np.max(np.abs(cfar))) if cfar.size else 0.,float(np.max(np.abs(bfar))) if bfar.size else 0.)
        assert forbidden<TOL
        rows.append(dict(degree=N,C_error=ce,C_bound=cb,B_error=be,B_bound=bb,
                         polynomial_outside_band_maximum=forbidden))
        power=power@h
    return dict(center=center,radius=radius,approximations=rows)

def path_controls(update,cert):
    rng=np.random.default_rng(SEED); rows=[]; gauges=0
    maxima=dict(operator_cancellation=0.,source_kernel=0.,source_population=0.,distance_bound_violation=0.,gauge_kernel=0.)
    for n in (3,4,5,6):
        for epsilon in (1/40,1/80,1/160):
            y=path_y(n,epsilon); f=np.diag(np.arange(1,n+1,dtype=float)); w=np.eye(n)/n
            k=np.zeros((n,n)); k[0,0]=1
            alpha,d,tc,tb=reduced_operators(f,y)
            model=audit.aligned(k,f,y); out=pair_audit.source_aligned(update,k,f,w,y)
            cancellation=max(np.linalg.norm(tc-model['tc']),np.linalg.norm(tb-model['tb']))
            p=np.abs(tc)**2+np.abs(tb)**2
            kernel=tc@k@tc+tb@k@tb
            maxima['operator_cancellation']=max(maxima['operator_cancellation'],float(cancellation))
            maxima['source_kernel']=max(maxima['source_kernel'],float(np.linalg.norm(out['k']-kernel)))
            maxima['source_population']=max(maxima['source_population'],float(np.linalg.norm(np.diag(out['k']).real-p[:,0])))
            approximation=polynomial_checks(y,alpha,d,tc,tb)
            c=approximation['center']; radius=approximation['radius']; M=np.linalg.eigvalsh(y)[-1]
            for i in range(n):
                for j in range(n):
                    distance=abs(i-j)
                    if distance>=2:
                        N=(distance-2)//2
                        bound=(alpha+(1-alpha)*M*M)/c*radius**(2*N+2)/(1-radius)**2
                        maxima['distance_bound_violation']=max(maxima['distance_bound_violation'],float(max(0.,p[i,j]-bound)))
            if n==3 and epsilon==1/40:
                assert abs(tc[2,0]-cert['endpoint_C_float'])<TOL
                assert abs(p[2,0]-cert['endpoint_transition_float'])<TOL
            if epsilon==1/40:
                g=audit.complex_unitary(rng,n); conjugate=lambda a:g@a@g.conj().T
                gout=pair_audit.source_aligned(update,conjugate(k),conjugate(f),conjugate(w),conjugate(y))
                maxima['gauge_kernel']=max(maxima['gauge_kernel'],float(np.linalg.norm(gout['k']-conjugate(out['k'])))); gauges+=1
            rows.append(dict(n=n,epsilon=epsilon,two_hop_transition=float(p[2,0]),
                             endpoint_transition=float(p[-1,0]),source_two_hop_population=float(out['k'][2,2].real),
                             minimum_transition=float(np.min(p)),polynomial=approximation))
    assert max(maxima.values())<TOL
    return dict(source_events=12,additional_gauge_source_calls=gauges,full_source_calls=12+gauges,
                maximum_residuals=maxima,cases=rows)

def disconnected_controls(update):
    rng=np.random.default_rng(SEED+1); rows=[]; maximum=0.
    for n in (4,5,6,7):
        y=np.zeros((n,n)); y[:2,:2]=path_y(2,1/40); y[2:,2:]=path_y(n-2,1/40)
        f=np.diag(np.arange(1,n+1,dtype=float)); w=np.eye(n)/n
        raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=(raw+raw.conj().T)/2
        alpha,d,tc,tb=reduced_operators(f,y); out=pair_audit.source_aligned(update,k,f,w,y)
        p=np.abs(tc)**2+np.abs(tb)**2; current=mode_graph_audit.channel_flux(k,[tc,tb],np.eye(n))
        residual=max(np.linalg.norm(p[:2,2:]),np.linalg.norm(current[:2,2:]),
                     abs(np.trace(out['k'][:2,:2]-k[:2,:2])),abs(np.trace(out['k'][2:,2:]-k[2:,2:])))
        assert residual<TOL and np.linalg.norm(k[:2,2:])>1e-3
        maximum=max(maximum,float(residual))
        rows.append(dict(n=n,cross_transition_norm=float(np.linalg.norm(p[:2,2:])),
                         cross_current_norm=float(np.linalg.norm(current[:2,2:])),maximum_stock_residual=float(residual)))
    return dict(full_source_calls=4,maximum_residual=maximum,cases=rows)

def run():
    update=audit.load_update(); cert=exact_checks()
    return dict(scope='Declared formation-node path and disconnected Y blocks; internal range only',
                source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=SEED,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=cert,path=path_controls(update,cert),disconnected=disconnected_controls(update),
                status='PASS for strict nearest-neighbor counterexample and approximate bounds; physical causality/space OPEN')

if __name__=='__main__':
    result=run()
    (HERE/'channel_range_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
