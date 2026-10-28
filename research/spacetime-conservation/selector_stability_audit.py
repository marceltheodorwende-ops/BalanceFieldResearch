"""Gap-dependent stability and degeneracy limit of a spectral pair selector."""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import audit
import pair_audit

def projector(y):
    vals,vectors=np.linalg.eigh(y); v=vectors[:,:2]
    return v@v.conj().T,vals

def symbolic():
    t=sp.symbols('t',positive=True); angle=sp.pi/12; c=sp.cos(angle); s=sp.sin(angle)
    R=sp.Matrix([[1,0,0],[0,c,-s],[0,s,c]]); Y=sp.diag(sp.Rational(1,10),sp.Rational(1,10)+t,sp.Rational(1,10)+2*t)
    E=sp.simplify(R*Y*R.T-Y); P=sp.diag(1,1,0); D=sp.simplify(R*P*R.T-P)
    assert sp.simplify(sp.trace(E*E)-2*t*t*s*s)==0
    assert sp.simplify(sp.trace(D*D)-2*s*s)==0
    assert sp.simplify(E.det())==0
    assert sp.simplify(sp.trace(E))==0
    assert sp.simplify(D)!=sp.zeros(3)
    return dict(angle='pi/12',input_operator_norm='t*sin(pi/12)',projector_frobenius_norm='sqrt(2)*sin(pi/12)',relative_input_error='sin(pi/12) < 1/2',selector_bound='2*epsilon/(gap-epsilon)',isotropic_obstruction='all-unitary covariance forces scalar identity; rank-two orthogonal projector impossible at fully isotropic n=3 state')

def perturbations():
    rng=np.random.default_rng(20261123); rows=[]
    for n in (3,4):
        u=audit.complex_unitary(rng,n); vals=np.array([.06,.08,.12] if n==3 else [.06,.08,.12,.16]); y=(u*vals)@u.conj().T
        p,_=projector(y); gap=vals[2]-vals[1]
        for fraction in (.01,.1,.25):
            x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); e=x+x.conj().T; e*=fraction*gap/np.linalg.norm(e,2)
            q,_=projector(y+e); eps=np.linalg.norm(e,2); observed=np.linalg.norm(p-q); bound=2*eps/(gap-eps)
            assert eps<gap/2 and observed<=bound+1e-12
            rows.append(dict(n=n,error_gap_ratio=fraction,projector_difference=float(observed),proved_bound=float(bound)))
    return rows

def source():
    update=audit.load_update(); rng=np.random.default_rng(20261124); theta=np.pi/12; c=np.cos(theta); s=np.sin(theta)
    R=np.array([[1,0,0],[0,c,-s],[0,s,c]]); p=np.diag([1.,1.,0.]); rp=R@p@R.T
    f=np.eye(3); w=np.eye(3)/3; k=np.eye(3)/3; calls=0; pr=0.; yr=0.; gr=0.; rows=[]
    for index,t in enumerate((.01,.005,.0025)):
        y=np.diag([.1,.1+t,.1+2*t]); ry=R@y@R.T
        base=pair_audit.source_aligned(update,k,f,w,y); rotated=pair_audit.source_aligned(update,k,f,w,ry); calls+=2
        pb,values=projector(base['y']); pq,rotated_values=projector(rotated['y']); gap=values[2]-values[1]
        pr=max(pr,float(np.linalg.norm(pb-p)),float(np.linalg.norm(pq-rp)))
        yr=max(yr,float(np.linalg.norm(rotated['y']-R@base['y']@R.T)))
        in_error=np.linalg.norm(ry-y,2); out_error=np.linalg.norm(rotated['y']-base['y'],2)
        distance=np.linalg.norm(pb-pq); exact=np.sqrt(2)*s
        assert abs(in_error-t*s)<1e-10 and abs(out_error-gap*s)<1e-10 and abs(distance-exact)<1e-10
        assert distance<=2*in_error/(t-in_error)+1e-12
        if index in (0,2):
            g=audit.complex_unitary(rng,3); conj=lambda z:g@z@g.conj().T
            gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
            gp,_=projector(gout['y']); gr=max(gr,float(np.linalg.norm(gout['y']-conj(base['y']))),float(np.linalg.norm(gp-conj(p))))
        rows.append(dict(t=t,input_gap=t,input_error=float(in_error),source_output_gap=float(gap),source_output_error=float(out_error),source_projector_distance=float(distance),predicted_constant_distance=float(exact),gap_shrunk=bool(gap<t)))
    assert calls==8 and max(pr,yr,gr)<1e-10 and all(x['gap_shrunk'] for x in rows)
    return dict(calls=calls,projector_residual=pr,load_covariance_residual=yr,gauge_residual=gr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seeds=[20261123,20261124],symbolic=symbolic(),hermitian_perturbation_controls=perturbations(),source=source(),scope='Gap-relative selector stability and no uniform absolute continuity at fully isotropic triple degeneracy. No chosen physical transport or impossibility for richer nonsymmetric state data.')
    Path(__file__).with_name('selector_stability_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
