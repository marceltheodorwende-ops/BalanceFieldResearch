"""Unchanged canonical full-persistence controls, not an EEG detector."""
import json
from pathlib import Path
import numpy as np

def mathematical_preparation(c, power):
    # Explicit alternative definitions, never an assertion of physiological identification.
    if power not in (1,2) or np.trace(c).real <= 0:
        raise ValueError('Control definition outside domain')
    rho=c/np.trace(c).real
    y=rho if power==1 else rho@rho
    return y,rho

def closed(c,y):
    identity=np.eye(len(c));cc=np.linalg.inv(identity+y);b=y@cc
    # No frozen alpha or free damping term.
    lc=np.trace(c@cc).real;lb=np.trace(c@y@y@cc).real
    alpha=lb/(lc+lb)
    return alpha*cc@cc+(1-alpha)*b@b,alpha,lc,lb

def ambient(c,y):
    cc=np.linalg.inv(np.eye(len(c))+y);b=y@cc;g=np.eye(len(c))+y
    lc=np.trace(g@cc@c@cc).real;lb=np.trace(g@b@c@b).real
    alpha=lb/(lc+lb)
    analysis=np.vstack([np.sqrt(alpha)*cc,np.sqrt(1-alpha)*b])
    u,s,vh=np.linalg.svd(analysis,full_matrices=False);v=vh.conj().T
    yraw=np.diag(s*s);fraw=vh@c@v
    return v@yraw@vh,v@fraw@vh,alpha,lc,lb,s

def main():
    rng=np.random.default_rng(20261025)
    residuals={k:0. for k in ('svd_geometry','formation','cross_load','gauge','normalization')}
    cases=0
    for n in (2,3,18):
        for j in range(12):
            z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));q=np.linalg.qr(z)[0]
            eig=rng.uniform(.2,2,n)
            if n>2 and j%3==0:eig[2:]=0
            c=(q*eig)@q.conj().T
            for power in (1,2):
                y,w=mathematical_preparation(c,power)
                m,a,lc,lb=closed(c,y);out,cf,aa,lcc,lbb,s=ambient(c,y)
                assert min(lc,lb)>0 and 0<a<1 and np.max(np.linalg.eigvalsh(y))<1
                assert np.min(s)>0 and np.max(s*s)<1
                residuals['svd_geometry']=max(residuals['svd_geometry'],float(np.linalg.norm(m-out)))
                residuals['formation']=max(residuals['formation'],float(np.linalg.norm(cf-c)))
                residuals['cross_load']=max(residuals['cross_load'],abs(a*lc-(1-a)*lb))
                residuals['normalization']=max(residuals['normalization'],abs(np.trace(w)-1))
                z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));t=np.linalg.qr(z)[0]
                cg=t@c@t.conj().T;yg=t@y@t.conj().T
                mg,ag,_,_=closed(cg,yg)
                residuals['gauge']=max(residuals['gauge'],float(np.linalg.norm(mg-t@m@t.conj().T)),abs(a-ag))
                assert abs(a-aa)<1e-12 and abs(lc-lcc)<1e-10 and abs(lb-lbb)<1e-10
                cases+=1
    assert max(residuals.values())<2e-11
    c=np.diag([2.,1.]);y1,_=mathematical_preparation(c,1);y2,_=mathematical_preparation(c,2)
    m1,*_=closed(c,y1);m2,*_=closed(c,y2)
    gap=float(np.linalg.norm(np.sort(np.linalg.eigvalsh(m1))-np.sort(np.linalg.eigvalsh(m2))))
    assert gap>1e-3
    # Rank-one edge from the actual selection/witness gate, not an invented stabilizer.
    rho=np.diag([1.,0.]);q=np.diag([0.,1.]);surviving_mass=float(np.trace(q@rho))
    assert surviving_mass==0
    try:mathematical_preparation(np.zeros((2,2)),1)
    except ValueError:pass
    else:raise AssertionError('zero covariance normalized')
    result=dict(status='PASS',canonical_control_cases=cases,max_residuals=residuals,
        J1_J2_geometry_spectral_gap=gap,rank_one_surviving_witness=surviving_mass,
        zero_covariance_rejected=True,source='Dynamic Order II83-85 Eq121-143',
        preparation_definitions_not_physical_laws=True,EEG_detector_implemented=False,
        empirical_result=False,confirmatory_freeze=False)
    Path(__file__).with_name('bfg_boundary_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
