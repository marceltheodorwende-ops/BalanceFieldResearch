"""Repeated source Y update and entrywise adjacency, BFG only."""
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
SEED=20261103

def exact_controls():
    y,a=s.symbols('y a',positive=True)
    second=2*((1-a)*(1-2*y)+3*a)/(1+y)**4
    assert s.cancel(s.diff(pair_audit.g(y,a),y,2)-second)==0
    rows=[]; references=[]
    for epsilon in (s.Rational(1,40),s.Rational(1,80),s.Rational(1,160)):
        initial=s.eye(3)/4+epsilon*s.Matrix([[0,1,0],[1,0,1],[0,1,0]])
        current=initial; f=s.diag(1,2,3); sequence=[]
        for event in range(3):
            c=(s.eye(3)+current).inv()
            lc=s.trace(f*c); lb=s.trace(f*current*current*c)
            alpha=s.cancel(lb/(lc+lb))
            nxt=(alpha*s.eye(3)+(1-alpha)*current*current)*c*c
            nxt=nxt.applyfunc(s.cancel)
            assert nxt[0,2]>0 and nxt[0,1]>0 and nxt[1,2]>0
            assert nxt*initial-initial*nxt==s.zeros(3)
            lower=min(nxt[i,i]-sum(abs(nxt[i,j]) for j in range(3) if j!=i) for i in range(3))
            upper=max(nxt[i,i]+sum(abs(nxt[i,j]) for j in range(3) if j!=i) for i in range(3))
            assert lower>0 and upper<s.Rational(1,2) and lower>=2*upper*upper
            rows.append(dict(epsilon=str(epsilon),event=event+1,endpoint_entry=str(nxt[0,2]),
                             endpoint_float=float(nxt[0,2]),class_lower_bound=float(lower),class_upper_bound=float(upper)))
            sequence.append(dict(y=np.array(nxt,dtype=float),alpha=float(alpha)))
            current=nxt
        references.append(sequence)
    return dict(fixed_alpha_second_derivative=str(second),exact_events=len(rows),cases=rows),references

def source_controls(update,references):
    rng=np.random.default_rng(SEED)
    maxima=dict(rational_load=0.,rational_alpha=0.,retained_spectral_frame=0.,gauge_load=0.)
    rows=[]; gauges=0
    for case,epsilon in enumerate((1/40,1/80,1/160)):
        y=np.eye(3)/4+epsilon*np.array([[0,1,0],[1,0,1],[0,1,0]])
        initial=y.copy(); _,basis=np.linalg.eigh(initial)
        f=np.diag([1.,2.,3.]); w=np.eye(3)/3
        k=np.array([[1.,1+1j,.2],[1-1j,-2.,-.3j],[.2,.3j,3.]])
        for event in range(3):
            out=pair_audit.source_aligned(update,k,f,w,y)
            exact=references[case][event]
            residual=float(np.linalg.norm(out['y']-exact['y']))
            spectral=basis.conj().T@out['y']@basis
            frame=float(np.linalg.norm(spectral-np.diag(np.diag(spectral))))
            maxima['rational_load']=max(maxima['rational_load'],residual)
            maxima['rational_alpha']=max(maxima['rational_alpha'],abs(float(out['alpha']-exact['alpha'])))
            maxima['retained_spectral_frame']=max(maxima['retained_spectral_frame'],frame)
            assert out['y'][0,2].real>0
            if event==0:
                g=audit.complex_unitary(rng,3); conjugate=lambda a:g@a@g.conj().T
                gout=pair_audit.source_aligned(update,conjugate(k),conjugate(f),conjugate(w),conjugate(y))
                maxima['gauge_load']=max(maxima['gauge_load'],float(np.linalg.norm(gout['y']-conjugate(out['y'])))); gauges+=1
            rows.append(dict(epsilon=epsilon,event=event+1,source_endpoint=float(out['y'][0,2].real),
                             source_maximum=float(np.linalg.eigvalsh(out['y'])[-1]),rational_residual=residual,
                             current_graph_edges_above_audit_tolerance=int(sum(abs(out['y'][i,j])>TOL for i in range(3) for j in range(i+1,3)))))
            k,f,w,y=out['k'],out['f'],out['w'],out['y']
    assert max(maxima.values())<TOL
    return dict(source_events=len(rows),additional_gauge_source_calls=gauges,
                full_source_calls=len(rows)+gauges,maximum_residuals=maxima,cases=rows)

def run():
    update=audit.load_update(); exact,references=exact_controls()
    return dict(scope='Three-node formation graph under repeated autonomous C events; exact finite-horizon convexity',
                source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=SEED,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=exact,full_source=source_controls(update,references),
                status='PASS for persistent created Y edge on stated family; physical geometry/Einstein OPEN')

if __name__=='__main__':
    result=run()
    (HERE/'adjacency_evolution_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
