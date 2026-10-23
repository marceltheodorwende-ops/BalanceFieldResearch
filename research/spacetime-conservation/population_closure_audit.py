"""Source-derived population chains, coherence obstruction and exact memory."""
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
SEED=20261101

def diagonal(k): return np.diag(np.diag(k))
def off(k): return k-diagonal(k)
def phi(k,ts): return sum((t@k@t for t in ts),np.zeros_like(k,dtype=complex))
def weights(ts): return sum((np.abs(t)**2 for t in ts),np.zeros(ts[0].shape))
def event(update,k,f,w,y,v):
    model=audit.aligned(k,f,y)
    ts=[v.conj().T@model[key]@v for key in ('tc','tb')]
    out=pair_audit.source_aligned(update,k,f,w,y)
    return out,ts,weights(ts)

def exact_checks():
    h=s.symbols('h',real=True)
    r=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
    def transformed(k,basis):
        y=basis*k*basis.T
        y=s.Matrix([[y[0,0],h*y[0,1]],[h*y[1,0],y[1,1]]])
        return s.simplify(basis.T*y*basis)
    x=s.Matrix([[0,1],[1,0]]); z=s.diag(1,-1)
    coupling=s.simplify(transformed(x,r)[0,0])
    assert s.simplify(coupling-s.Rational(168,625)*(1-h))==0
    generated=s.simplify(transformed(s.diag(2,1),r)[0,1])
    assert s.simplify(generated-coupling/2)==0
    f=r*s.diag(1,2)*r.T
    alpha=pair_audit.alpha_exact([s.Rational(1,5),s.Rational(3,10)],[f[0,0],f[1,1]])
    def exact_h2(a):
        yi,yj=s.Rational(1,5),s.Rational(3,10)
        return s.cancel((a+(1-a)*yi*yj)**2/((a+(1-a)*yi**2)*(a+(1-a)*yj**2)))
    unbiased=s.Matrix([[1,-1],[1,1]])/s.sqrt(2)
    assert s.simplify(transformed(z,unbiased)-h*z)==s.zeros(2)
    assert transformed(x,unbiased)[0,0]==0
    sy=s.Matrix([[0,-s.I],[s.I,0]])
    assert s.simplify(transformed(sy,unbiased)[0,0])==0
    for sign in (1,-1):
        k=s.eye(2)+sign*x/2
        assert k.det()>0
        ku=s.diag(2,1)+sign*x/5+sign*3*sy/10
        assert ku.det()>0
    return dict(tilted_F=[[str(value) for value in row] for row in f.tolist()],tilted_alpha=str(alpha),tilted_h_squared=str(exact_h2(alpha)),
                population_coherence_coupling=str(coupling),generated_coherence=str(generated),
                tilted_population_fiber_gap=str(coupling),
                unbiased_h_squared=str(exact_h2(s.Rational(8,133))),
                unbiased_closure='Phi_F(sigma_z)=h sigma_z; offdiagonal Hermitian directions have zero diagonal')

def witness_controls(update):
    r=np.array([[.6,-.8],[.8,.6]]); y0=np.diag([.2,.3]); f=r@np.diag([1.,2.])@r.T; w=np.eye(2)/2
    x=audit.pauli()[1]; sy=audit.pauli()[2]
    rows=[]; successor=[]
    for sign in (1,-1):
        kf=np.eye(2)+sign*x/2; k=r@kf@r.T
        out,ts,p=event(update,k,f,w,y0,r)
        q=np.diag(r.T@out['k']@r).real
        a=audit.aligned(k,f,y0)['alpha']
        h=(a+(1-a)*.2*.3)/np.sqrt((a+(1-a)*.2**2)*(a+(1-a)*.3**2))
        coupling=168/625*(1-h)
        expected=np.array([1+sign*coupling/2,1-sign*coupling/2])
        assert np.linalg.norm(q-expected)<TOL
        successor.append(q)
        rows.append(dict(sign=sign,input_population=[1.,1.],coherence_magnitude=.5,
                         successor_population=q.tolist(),markov_prediction=(p@np.ones(2)).tolist()))
    assert np.linalg.norm(successor[0]-successor[1])>1e-5
    # A diagonal preparation generates coherence and a two-event memory correction.
    k=r@np.diag([2.,1.])@r.T; y=y0.copy(); formation=f.copy(); witness=w.copy()
    markov=np.array([2.,1.]); couplings=[]; memory=[]
    for step in range(2):
        model=audit.aligned(k,formation,y); a=model['alpha']; ys=np.diag(y).real
        h=(a+(1-a)*ys[0]*ys[1])/np.sqrt((a+(1-a)*ys[0]**2)*(a+(1-a)*ys[1]**2))
        couplings.append(168/625*(1-h))
        out,ts,p=event(update,k,formation,witness,y,r); markov=p@markov
        actual=np.diag(r.T@out['k']@r).real
        memory.append(dict(event=step+1,actual=actual.tolist(),repeated_markov=markov.tolist()))
        k,formation,witness,y=out['k'],out['f'],out['w'],out['y']
    defect=actual-markov; expected=np.array([1.,-1.])*couplings[0]*couplings[1]/2
    assert np.linalg.norm(defect-expected)<TOL and np.linalg.norm(defect)>1e-9
    # Noncommuting but unbiased F nodes have genuine population closure for all K.
    u=np.array([[1.,-1.],[1.,1.]])/np.sqrt(2); uf=u@np.diag([1.,2.])@u.T
    histories=[]; max_closed=0.
    for sign in (1,-1):
        kf=np.diag([2.,1.])+sign*x/5+sign*.3*sy
        k=u@kf@u.T; formation=uf.copy(); witness=w.copy(); y=y0.copy(); history=[]
        for step in range(2):
            before=np.diag(u.T@k@u).real
            out,ts,p=event(update,k,formation,witness,y,u)
            after=np.diag(u.T@out['k']@u).real
            residual=float(np.linalg.norm(after-p@before)); assert residual<TOL
            max_closed=max(max_closed,residual); history.append(after.tolist())
            k,formation,witness,y=out['k'],out['f'],out['w'],out['y']
        histories.append(history)
    assert np.linalg.norm(np.array(histories[0])-np.array(histories[1]))<TOL
    return dict(full_source_calls=8,tilted_fiber_examples=rows,tilted_fiber_successor_gap=(successor[0]-successor[1]).tolist(),
                diagonal_preparation_history=memory,two_event_memory_defect=defect.tolist(),
                two_event_predicted_memory=expected.tolist(),unbiased_population_histories=histories,
                unbiased_maximum_markov_residual=max_closed)

def complex_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(stochastic=0.,symmetry=0.,population_with_coherence=0.,diffusive_current=0.,
                current_decomposition=0.,two_event_memory=0.,gauge_population=0.)
    largest_markov_error=0.; largest_obstruction=0.; rows=[]; gauges=0
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n); y=(u*np.linspace(.2,.3,n))@u.conj().T
            f=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            _,v=np.linalg.eigh(f)
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=(raw+raw.conj().T)/2
            previous=None
            for step in range(2):
                kf=v.conj().T@k@v; d=diagonal(kf); o=off(kf)
                out,ts,p=event(update,k,f,w,y,v)
                next_k=v.conj().T@out['k']@v; q=np.diag(kf).real; qnext=np.diag(next_k).real
                coherent=np.diag(phi(o,ts)).real
                maxima['stochastic']=max(maxima['stochastic'],float(np.linalg.norm(p.sum(axis=0)-1)),float(np.linalg.norm(p.sum(axis=1)-1)))
                maxima['symmetry']=max(maxima['symmetry'],float(np.linalg.norm(p-p.T)))
                assert np.min(p)>=0
                maxima['population_with_coherence']=max(maxima['population_with_coherence'],float(np.linalg.norm(qnext-p@q-coherent)))
                jd=mode_graph_audit.channel_flux(d,ts,np.eye(n))
                jo=mode_graph_audit.channel_flux(o,ts,np.eye(n))
                jk=mode_graph_audit.channel_flux(kf,ts,np.eye(n))
                maxima['diffusive_current']=max(maxima['diffusive_current'],float(np.linalg.norm(jd-p*(q[:,None]-q[None,:]))))
                maxima['current_decomposition']=max(maxima['current_decomposition'],float(np.linalg.norm(jk-jd-jo)))
                error=float(np.linalg.norm(qnext-p@q)); largest_markov_error=max(largest_markov_error,error)
                obstruction=0.
                for i in range(n):
                    e=np.zeros((n,n)); e[i,i]=1
                    obstruction+=np.linalg.norm(off(phi(e,ts)))**2
                largest_obstruction=max(largest_obstruction,float(np.sqrt(obstruction)))
                if previous is not None:
                    d0,o0,ts0=previous
                    memory=diagonal(phi(off(phi(d0,ts0)),ts))+diagonal(phi(off(phi(o0,ts0)),ts))
                    predicted=diagonal(phi(d,ts))+memory
                    maxima['two_event_memory']=max(maxima['two_event_memory'],float(np.linalg.norm(diagonal(next_k)-predicted)))
                if case==0 and step==0:
                    g=audit.complex_unitary(rng,n); conjugate=lambda a:g@a@g.conj().T
                    gout=pair_audit.source_aligned(update,conjugate(k),conjugate(f),conjugate(w),conjugate(y))
                    gv=g@v; gq=np.diag(gv.conj().T@gout['k']@gv).real
                    maxima['gauge_population']=max(maxima['gauge_population'],float(np.linalg.norm(gq-qnext))); gauges+=1
                rows.append(dict(n=n,case=case,event=step+1,markov_only_population_error=error,
                                 diagonal_algebra_leakage=float(np.sqrt(obstruction))))
                previous=(d,o,ts)
                k,f,w,y=out['k'],out['f'],out['w'],out['y']
    assert max(maxima.values())<TOL and largest_markov_error>1e-5 and largest_obstruction>1e-5
    return dict(preparations=12,source_events=len(rows),additional_gauge_source_calls=gauges,
                full_source_calls=len(rows)+gauges,maximum_residuals=maxima,
                maximum_markov_only_error=largest_markov_error,maximum_diagonal_algebra_leakage=largest_obstruction,cases=rows)

def run():
    update=audit.load_update()
    return dict(scope='Formation-node population projection and exact coherence memory; no physical space identification',
                source_blob=audit.EXPECTED_SOURCE_BLOB,seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=exact_checks(),witnesses=witness_controls(update),full_source=complex_controls(update),
                status='PASS for conditional population closure and memory; generic population-only factor refuted')

if __name__=='__main__':
    result=run()
    (HERE/'population_closure_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
