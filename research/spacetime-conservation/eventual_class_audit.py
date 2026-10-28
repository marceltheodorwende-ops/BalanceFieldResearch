"""Eventual spectral-class entry and degeneracy limits, BFG only."""
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
SEED=20261029

def f(y): return 2*y*y/((1+y)**2*(1+y*y))
def r(y): return y*y/(1+y*y)
def in_class(ys):
    m,M=min(ys),max(ys)
    return M<=s.Rational(1,2) and m>=2*M*M

def entry_bound(M,delta):
    k=0
    while (M/2**k)**2>delta/128: k+=1
    return k+1

def exact_checks():
    y,M,a,b,alpha=s.symbols('y M a b alpha',positive=True)
    g=pair_audit.g
    assert s.cancel(s.diff(g(y,r(M)),y)-2*(y-M*M)/((1+M*M)*(1+y)**3))==0
    assert s.cancel(M/2-r(M)-M*(1-M)**2/(2*(1+M*M)))==0
    assert s.cancel(s.Rational(1,2)-2*M/(1+M)**2-(1-M)**2/(2*(1+M)**2))==0
    h=(1+y*y)/(1+y)
    assert s.cancel(1-h-y*(1-y)/(1+y))==0
    assert s.cancel(h-s.Rational(1,2)-(2*(y-s.Rational(1,4))**2+s.Rational(7,8))/(2*(1+y)))==0
    collision=(a-b)*(a+b+2*a*b-2*alpha*(1+a)*(1+b))/((1+a)**2*(1+b)**2)
    assert s.cancel(g(a,alpha)-g(b,alpha)-collision)==0
    ys=[s.Rational(1,10),s.Rational(1,2),s.Rational(9,10)]
    target=s.Rational(59,209); t=s.symbols('t',positive=True)
    solutions=s.solve(pair_audit.alpha_exact(ys,[1,1,t])-target,t)
    assert len(solutions)==1 and solutions[0]>0
    weight=solutions[0]; nxt=[s.cancel(g(z,target)) for z in ys]
    assert nxt[0]==nxt[2] and nxt[1]<nxt[0] and in_class(nxt)
    assert weight>1  # F compressed to the colliding block resolves this particular tie.
    trace_y=[s.Rational(1,100),s.Rational(1,50),s.Rational(9,10)]
    trace_alpha=pair_audit.alpha_exact(trace_y,[1,1,100])
    trace_next=[s.cancel(g(z,trace_alpha)) for z in trace_y]
    trace_jump=s.cancel(sum(trace_next)-sum(trace_y))
    assert trace_jump>0 and max(trace_next)<max(trace_y)/2
    return dict(collision_input=list(map(str,ys)),collision_formation_weights=['1','1',str(weight)],
                collision_alpha=str(target),collision_successor=list(map(str,nxt)),
                collision_at_second_selection_boundary=True,collision_successor_in_C=True,
                formation_resolves_this_witness=True,
                trace_input=list(map(str,trace_y)),trace_weights=['1','1','100'],
                trace_alpha=str(trace_alpha),trace_successor=list(map(str,trace_next)),
                trace_increase=str(trace_jump),trace_increase_float=float(trace_jump))

def exact_orbits():
    cases=[]; events=0
    for n in (2,3,4,5):
        for case in range(3):
            ys=[s.Rational(1,50)+s.Rational(24*i,25*(n-1))+s.Rational(case,1000) for i in range(n)]
            weights=[s.Integer(10)**(case*i) for i in range(n)]
            delta=min(weights)/sum(weights); bound=entry_bound(max(ys),delta)
            history=[]
            assert not in_class(ys)
            for event in range(10):
                M=max(ys); alpha=pair_audit.alpha_exact(ys,weights)
                nxt=[s.cancel(pair_audit.g(z,alpha)) for z in ys]
                nm,nM=min(nxt),max(nxt)
                assert nM<=M/2 and alpha>=delta*M*M/4
                assert nm>=delta*M*M/16 and nM<=2*M*M
                entered=bool(in_class(nxt)); events+=1
                history.append(dict(event=event+1,maximum=float(nM),minimum=float(nm),entered_C=entered,
                                    distinct_eigenvalues=len(set(nxt))))
                ys=nxt
                if entered: break
            assert entered, 'Exact orbit did not enter C within predeclared ten-event cap'
            assert len(history)<=bound
            cases.append(dict(n=n,case=case,delta=str(delta),proved_entry_event_bound=bound,
                              first_entry_event=len(history),events=history))
    return dict(preparations=12,exact_events=events,cases=cases)

def source_witnesses(update,cert):
    rows=[]
    for kind in ('collision','trace'):
        ys=np.array([float(s.Rational(z)) for z in cert[kind+'_input']])
        weights=np.array([float(s.Rational(z)) for z in cert[kind+'_formation_weights' if kind=='collision' else 'trace_weights']])
        expected=np.array([float(s.Rational(z)) for z in cert[kind+'_successor']])
        out=pair_audit.source_aligned(update,np.diag([1.,2.,3.]),np.diag(weights),np.eye(3)/3,np.diag(ys))
        residual=float(np.linalg.norm(out['y']-np.diag(expected)))
        assert residual<TOL
        eig=np.linalg.eigvalsh(out['y'])
        row=dict(kind=kind,matrix_residual=residual,successor_eigenvalues=eig.tolist())
        if kind=='collision':
            gap=float(eig[2]-eig[1]); assert abs(gap)<TOL
            row['numerical_second_boundary_gap']=gap
        else:
            jump=float(np.trace(out['y']).real-sum(ys))
            assert jump>1e-3 and abs(jump-cert['trace_increase_float'])<TOL
            row['trace_increase']=jump
        rows.append(row)
    return dict(full_source_calls=2,cases=rows)

def complex_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(half_envelope_violation=0.,alpha_lower_violation=0.,minimum_lower_violation=0.,quadratic_upper_violation=0.)
    rows=[]
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n); y=(u*np.linspace(.04,.96,n))@u.conj().T
            formation=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            delta=float(np.linalg.eigvalsh(formation)[0]/np.trace(formation).real)
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=(raw+raw.conj().T)/2
            for event in range(2):
                M=float(np.linalg.eigvalsh(y)[-1])
                out=pair_audit.source_aligned(update,k,formation,w,y)
                eig=np.linalg.eigvalsh(out['y']); nm,nM=float(eig[0]),float(eig[-1])
                values=dict(half_envelope_violation=max(0.,nM-M/2),
                            alpha_lower_violation=max(0.,delta*M*M/4-out['alpha']),
                            minimum_lower_violation=max(0.,delta*M*M/16-nm),
                            quadratic_upper_violation=max(0.,nM-2*M*M))
                for key,value in values.items(): maxima[key]=max(maxima[key],float(value))
                rows.append(dict(n=n,case=case,event=event+1,delta=delta,maximum_before=M,
                                 maximum_after=nM,minimum_after=nm,entered_C=nm>=2*nM*nM and nM<=.5))
                k,formation,w,y=out['k'],out['f'],out['w'],out['y']
    assert max(maxima.values())<TOL
    return dict(preparations=12,full_source_events=len(rows),maximum_bound_violations=maxima,cases=rows)

def run():
    update=audit.load_update(); cert=exact_checks()
    return dict(scope='Autonomous full persistence P=I, F>0, 0<Y<I; no general simple-spectrum guarantee',
                source_blob=audit.EXPECTED_SOURCE_BLOB,seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=cert,exact_orbits=exact_orbits(),source_witnesses=source_witnesses(update,cert),
                full_source=complex_controls(update),
                status='PASS for eventual C entry; universal Y-only two-smallest selector and global trace-log clock refuted')

if __name__=='__main__':
    result=run()
    (HERE/'eventual_class_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
