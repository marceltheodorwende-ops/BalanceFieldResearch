"""Matrix BFG controls only; no physical data or claimed interventions."""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'real-eeg-covariance-2026-10-07'))
from experiment import update

def natural(K,F,Y):
    n=len(Y);I=np.eye(n);C=np.linalg.inv(I+Y);B=I-C;G=I+Y
    lc=float(np.trace(G@C@F@C).real);lb=float(np.trace(G@B@F@B).real)
    if min(lc,lb)<=0:raise ValueError('positive loads required')
    alpha=lb/(lc+lb);beta=1-alpha;R=alpha*C@C+beta*B@B
    vals,vec=np.linalg.eigh(R)
    if min(vals)<=0:raise ValueError('positive full rank required')
    inverse=vec@np.diag(vals**-.5)@vec.conj().T
    Kn=inverse@(alpha*C@K@C+beta*B@K@B)@inverse
    return Kn,R,alpha

def main(out):
    rng=np.random.default_rng(1008);errors=[];phase=[];norms=[]
    for _ in range(30):
        n=3;Y=np.diag(rng.uniform(.1,.8,n))
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));K=(z+z.conj().T)/2
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));F=z@z.conj().T+np.eye(n);W=np.eye(n)/n
        kn,yn,alpha=natural(K,F,Y);r=update(K,F,W,Y,np.eye(n))
        assert r['terminal'] is None
        errors.append(max(np.linalg.norm(kn-r['v']@r['k']@r['v'].conj().T),np.linalg.norm(yn-r['v']@r['y']@r['v'].conj().T)))
        c=1/(1+np.diag(Y));b=1-c;ri=np.diag(yn)
        gamma=(alpha*np.outer(c,c)+(1-alpha)*np.outer(b,b))/np.sqrt(np.outer(ri,ri))
        errors.append(np.linalg.norm(kn-gamma*K));phase.append(float(np.max(abs(np.imag(kn/K)))))
        norms.append(float(np.linalg.norm(kn)/np.linalg.norm(K)))
        assert np.all(gamma>=0) and np.all(gamma<=1+1e-12)
    d=.15;f=lambda x:2*x*x/((1+x)**2*(1+x*x));y=brentq(lambda yy:f(yy+d)-yy,0,.25);x=y+d
    F=np.array([[2.,.2j],[-.2j,1.]])
    K=np.array([[1.,.3+.1j],[.3-.1j,-1.]])
    H=np.array([[.2,.1+.2j],[.1-.2j,-.4]])
    alpha_x=2*x/(1+x*x)**2
    s=2*x*(1-x)/((1+x*x)*(1+x)**3)
    t=(1-x)/(1+x)*alpha_x
    predicted=s*H+t*np.trace(F@H).real/np.trace(F).real*np.eye(2)
    steps=[]
    for eps in [1e-4,1e-5,1e-6]:
        kp,rp,_=natural(K,F,x*np.eye(2)+eps*H);km,rm,_=natural(K,F,x*np.eye(2)-eps*H)
        steps.append(dict(step=eps,geometry_derivative_residual=float(np.linalg.norm((rp-rm)/(2*eps)-predicted)),kernel_derivative_residual=float(np.linalg.norm((kp-km)/(2*eps)))))
    assert max(errors)<1e-10 and max(phase)<1e-10 and max(norms)<=1+1e-12
    assert steps[-1]['geometry_derivative_residual']<1e-7 and steps[-1]['kernel_derivative_residual']<1e-7
    result=dict(kind='synthetic independent matrix/math controls; no real-data evaluation',ambient_cases=30,max_ambient_or_formula_residual=max(errors),max_kernel_ratio_imaginary=max(phase),max_kernel_HS_ratio=max(norms),declared_isotropic_input=d,fixed_y=y,transverse_geometry_eigenvalue=s,weighted_trace_geometry_eigenvalue=s+t,finite_difference_checks=steps,full_matrix_contraction_claimed=False,holdout_accessed=False)
    Path(out).mkdir(exist_ok=True,parents=True);Path(out,'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'results')
