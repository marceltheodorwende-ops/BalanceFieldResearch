"""Bernstein-vector fixed-initial-graph range bounds for actual BFG events."""
import json
import math
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

TOL=1e-10

def vector(t,schedule):
    t=np.asarray(t,dtype=float)
    result=np.ones((1,t.size))
    for alpha in schedule:
        beta=1-alpha; den=np.sqrt(alpha+beta*t*t)
        result=np.concatenate((result*(np.sqrt(alpha)/den),result*(np.sqrt(beta)*t/den)),axis=0)
        t=(alpha+beta*t*t)/(1+t)**2
    return result

def symbolic():
    t=s.symbols('t',real=True); a=s.Function('a')(t); b=s.Function('b')(t)
    v=s.kronecker_product(s.Matrix([s.cos(a),s.sin(a)]),s.Matrix([s.cos(b),s.sin(b)]))
    residual=s.trigsimp((v.diff(t).T*v.diff(t))[0]-s.diff(a,t)**2-s.diff(b,t)**2)
    assert residual==0
    return str(residual)

def run():
    certificate=symbolic(); update=audit.load_update(); rng=np.random.default_rng(20261105)
    rows=[]; calls=0; source_residual=0.; gauge_residual=0.; worst_excess=0.
    for n in (6,10,14):
        y=np.eye(n)/4+(np.eye(n,k=1)+np.eye(n,k=-1))/40
        vals,u=np.linalg.eigh(y); m0=float(vals[0]); M0=float(vals[-1])
        lo,hi=m0,M0; derivative_bound=1.; lipschitz_squared=0.; schedule=[]
        f=np.diag(np.arange(1,n+1,dtype=float)); w=np.eye(n)/n
        point=np.zeros((n,n)); point[0,0]=1
        z=np.zeros(n,dtype=complex); z[:2]=[1,1j]; z/=np.linalg.norm(z)
        coherent=np.outer(z,z.conj()); initial=[point.copy(),coherent.copy()]; current=[point,coherent]
        supports=[0,1]
        for event in range(3):
            aligned=audit.aligned(current[0],f,y); alpha=float(aligned['alpha']); beta=1-alpha
            angle_bound=np.sqrt(alpha*beta)*derivative_bound/(alpha+beta*lo*lo)
            lipschitz_squared+=angle_bound**2
            slope_bound=2*(beta*hi-alpha)/(1+lo)**3
            assert slope_bound>0
            derivative_bound*=slope_bound
            lo=(alpha+beta*lo*lo)/(1+lo)**2
            hi=(alpha+beta*hi*hi)/(1+hi)**2
            schedule.append(alpha)
            exact_vectors=vector(vals,schedule)
            outputs=[]
            for index,k in enumerate(current):
                out=pair_audit.source_aligned(update,k,f,w,y); calls+=1; outputs.append(out)
                prediction=u@((exact_vectors.T@exact_vectors)*(u.conj().T@initial[index]@u))@u.conj().T
                source_residual=max(source_residual,float(np.linalg.norm(out['k']-prediction)))
            if event==0:
                g=audit.complex_unitary(rng,n); conjugate=lambda a:g@a@g.conj().T
                out=pair_audit.source_aligned(update,conjugate(current[1]),conjugate(f),conjugate(w),conjugate(y)); calls+=1
                gauge_residual=max(gauge_residual,float(np.linalg.norm(out['k']-conjugate(outputs[1]['k']))))
            for degree in (1,2,3):
                nodes=m0+(M0-m0)*np.arange(degree+1)/degree
                x=(vals-m0)/(M0-m0)
                weights=np.array([math.comb(degree,j)*x**j*(1-x)**(degree-j) for j in range(degree+1)])
                approximate=vector(nodes,schedule)@weights
                measured_error=float(np.linalg.norm(exact_vectors-approximate,axis=0).max())
                epsilon=math.sqrt(lipschitz_squared)*(M0-m0)/(2*math.sqrt(degree))
                bound=min(1.,epsilon**2)
                worst_excess=max(worst_excess,measured_error-epsilon)
                assert measured_error<=epsilon+TOL
                # Each component polynomial of degree d has no path entry beyond d.
                approximate_ops=[(u*component)@u.conj().T for component in approximate]
                far=np.abs(np.arange(n)[:,None]-np.arange(n)[None,:])>degree
                sparsity=max(float(abs(op[far]).max()) for op in approximate_ops)
                assert sparsity<TOL
                tails=[]
                for index,out in enumerate(outputs):
                    tail=float(np.diag(out['k']).real[supports[index]+degree+1:].sum())
                    tails.append(tail); worst_excess=max(worst_excess,tail-bound)
                    assert tail>=-TOL and tail<=bound+TOL
                rows.append(dict(n=n,event=event+1,degree=degree,lipschitz_bound=math.sqrt(lipschitz_squared),epsilon=epsilon,tail_bound=bound,measured_vector_error=measured_error,polynomial_far_residual=sparsity,source_tails=tails))
            current=[out['k'] for out in outputs]; f,w,y=outputs[0]['f'],outputs[0]['w'],outputs[0]['y']
    assert calls==21 and max(source_residual,gauge_residual,worst_excess)<TOL
    return dict(status='PASS for finite-horizon internal graph bound; physical locality OPEN',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261105,symbolic_tensor_norm_residual=certificate,full_source_calls=calls,maximum_source_residual=source_residual,maximum_gauge_residual=gauge_residual,maximum_bound_excess=worst_excess,cases=rows)

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('multievent_range_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
