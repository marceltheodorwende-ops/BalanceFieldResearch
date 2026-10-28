"""Frozen BFG channel interpolation: scoped obstruction and alternatives."""
import json
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

TOL=1e-10

def run():
    update=audit.load_update(); rng=np.random.default_rng(20261106)
    ys=[s.Rational(3,20),s.Rational(1,5),s.Rational(4,15)]
    fs=[s.Integer(1),s.Integer(1),s.Rational(57,92)]
    alpha=pair_audit.alpha_exact(ys,fs); assert alpha==s.Rational(1,26)
    a=7/(5*s.sqrt(2)); b=s.Rational(24,25)
    half=s.Matrix([[1,s.sqrt(a),s.sqrt(b)],[s.sqrt(a),1,s.sqrt(a)],[s.sqrt(b),s.sqrt(a),1]])
    determinant=s.simplify(half.det())
    certificate=(1-s.sqrt(b))*(1+s.sqrt(b)-2*a)
    assert s.simplify(determinant-certificate)==0
    assert 49**2>20**2*6 and determinant.evalf()<0
    y=np.diag([float(v) for v in ys]); f=np.diag([float(v) for v in fs]); w=np.eye(3)/3; k=np.ones((3,3))/3
    h=np.array([[1,float(a),float(b)],[float(a),1,float(a)],[float(b),float(a),1]])
    out=pair_audit.source_aligned(update,k,f,w,y); calls=1
    source_residual=float(np.linalg.norm(out['k']-h/3)); gauge_residual=0.; endpoint_residual=0.; min_psd=1.
    half_min=float(np.linalg.eigvalsh(np.sqrt(h))[0]); assert half_min < -1e-7
    witness_theta=np.arctan(5*np.array([float(v) for v in ys]))
    delta=witness_theta[:,None]-witness_theta[None,:]
    convex=(1+h)/2; angular=np.cos(delta/2)
    separation=float(np.linalg.norm(convex-angular)); assert separation>1e-6
    convex_semigroup=float(np.linalg.norm(convex*convex-h))
    angular_semigroup=float(np.linalg.norm(angular*angular-h))
    assert convex_semigroup>1e-6 and angular_semigroup>1e-6
    for n in (3,4,5):
        for case in range(4):
            u=audit.complex_unitary(rng,n); vals=np.linspace(.2,.3,n)
            y=(u*vals)@u.conj().T
            z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); f=z@z.conj().T+np.eye(n)
            w=np.eye(n)/n; z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=z@z.conj().T; k/=np.trace(k)
            aligned=audit.aligned(k,f,y); al=float(aligned['alpha'])
            theta=np.arctan(np.sqrt((1-al)/al)*vals); delta=theta[:,None]-theta[None,:]; h=np.cos(delta)
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
            predicted=u@(h*(u.conj().T@k@u))@u.conj().T
            source_residual=max(source_residual,float(np.linalg.norm(out['k']-predicted)))
            for t in (.25,.5,.75):
                for intermediate in ((1-t)*np.ones((n,n))+t*h,np.cos(t*delta)):
                    min_psd=min(min_psd,float(np.linalg.eigvalsh(intermediate)[0]))
                    assert np.linalg.eigvalsh(intermediate)[0]>=-TOL
            endpoint_residual=max(endpoint_residual,float(np.linalg.norm(np.cos(delta)-h)))
            if case==0:
                g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                gauge_residual=max(gauge_residual,float(np.linalg.norm(gout['k']-conj(out['k']))))
    assert calls==16 and max(source_residual,gauge_residual,endpoint_residual)<TOL
    return dict(status='PASS: entrywise-power candidate refuted by exact witness; two nonunique CP interpolations established',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261106,full_source_calls=calls,exact_alpha=str(alpha),half_power_determinant=str(determinant),half_power_determinant_float=float(determinant),half_power_minimum_eigenvalue=half_min,half_time_interpolation_difference=separation,convex_half_composition_defect=convex_semigroup,angular_half_composition_defect=angular_semigroup,maximum_source_residual=source_residual,maximum_gauge_residual=gauge_residual,minimum_alternative_gram_eigenvalue=min_psd,physical_clock='OPEN; frozen kernel channels only')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('interpolation_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
