"""Weak-splitting frozen-channel limit versus actual finite geometry drift."""
import json
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

TOL=1e-10

def run():
    e,y,a,b,c=s.symbols('e y a b c',real=True,positive=True)
    theta_a=s.atan((1/y+c*e)*(y+e*a)); theta_b=s.atan((1/y+c*e)*(y+e*b))
    linear=s.simplify(s.diff(theta_a-theta_b,e).subs(e,0))
    assert s.simplify(linear-(a-b)/(2*y))==0
    coefficient=s.simplify(-linear**2/2)
    assert s.simplify(coefficient+(a-b)**2/(8*y*y))==0
    update=audit.load_update(); rng=np.random.default_rng(20261107)
    calls=0; max_unitary=0.; max_gauge=0.; rows=[]
    y0=.25; fy=2*y0*y0/((1+y0)**2*(1+y0*y0))
    for n in (2,3,4):
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); a=(z+z.conj().T)/2; a/=np.linalg.norm(a,2)
        values,u=np.linalg.eigh(a)
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); f=z@z.conj().T+np.eye(n)
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=z@z.conj().T; k/=np.trace(k)
        w=np.eye(n)/n; comm=a@k-k@a; generator=-(a@comm-comm@a)/(8*y0*y0)
        ks=u.conj().T@k@u; target=u@(np.exp(-.1*(values[:,None]-values[None,:])**2/(8*y0*y0))*ks)@u.conj().T
        errors=[]; frozen_errors=[]; dimension_rows=[]
        for epsilon in (.01,.005,.0025,.00125):
            load=y0*np.eye(n)+epsilon*a
            aligned=audit.aligned(k,f,load); alpha=float(aligned['alpha'])
            theta=np.arctan(np.sqrt((1-alpha)/alpha)*(y0+epsilon*values))
            unitary=(u*np.exp(1j*theta))@u.conj().T
            mixed=(unitary@k@unitary.conj().T+unitary.conj().T@k@unitary)/2
            out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
            max_unitary=max(max_unitary,float(np.linalg.norm(out['k']-mixed)))
            error=float(np.linalg.norm((out['k']-k)/epsilon**2-generator)); errors.append(error)
            h=np.cos(theta[:,None]-theta[None,:]); count=int(np.floor(.1/epsilon**2))
            frozen=u@((h**count)*ks)@u.conj().T
            frozen_error=float(np.linalg.norm(frozen-target)); frozen_errors.append(frozen_error)
            jump=float(np.linalg.norm(out['y']-load)); jump_limit=np.sqrt(n)*abs(fy-y0)
            if epsilon==.01:
                g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1
                max_gauge=max(max_gauge,float(np.linalg.norm(gout['k']-conj(out['k']))))
            dimension_rows.append(dict(epsilon=epsilon,scaled_kernel_error=error,frozen_comparison_iterations=count,frozen_limit_error=frozen_error,geometry_jump=jump,geometry_jump_limit=jump_limit))
        assert errors[-1]<.02 and (errors[0]<=1e-10 or errors[-1]<.6*errors[0])
        assert frozen_errors[-1]<.02 and (frozen_errors[0]<=1e-10 or frozen_errors[-1]<.6*frozen_errors[0])
        assert abs(dimension_rows[-1]['geometry_jump']-dimension_rows[-1]['geometry_jump_limit'])<.01
        rows.append(dict(n=n,cases=dimension_rows))
    assert calls==15 and max(max_unitary,max_gauge)<TOL
    return dict(status='PASS: frozen diffusive channel limit; full fixed-y Euler scaling obstructed',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261107,full_source_calls=calls,symbolic_angle_difference_derivative=str(linear),symbolic_second_coefficient=str(coefficient),scalar_successor=str(s.Rational(32,425)),maximum_random_unitary_residual=max_unitary,maximum_gauge_residual=max_gauge,cases=rows,physical_time='OPEN; frozen powers are not autonomous source trajectories')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('weak_splitting_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
