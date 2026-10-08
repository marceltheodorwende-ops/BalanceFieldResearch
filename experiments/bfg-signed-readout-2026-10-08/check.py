"""Independent controls for a proposed signed coherence readout."""
import sys,json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'bfg-matrix-tangent-2026-10-08'))
sys.path.insert(0,str(ROOT/'real-eeg-covariance-2026-10-07'))
from control import natural
from experiment import update

def gamma(Y,F):
    _,R,alpha=natural(np.eye(2),F,Y);y=np.diag(Y);c=1/(1+y);b=1-c
    return float((alpha*c[0]*c[1]+(1-alpha)*b[0]*b[1])/np.sqrt(R[0,0]*R[1,1]))

def main(out):
    F=np.array([[1.,.3],[.3,2.]]);K=np.array([[0.,1.+.4j],[1.-.4j,0.]])
    Ys=[np.diag([.2,.7]),np.diag([.3,.8])];z=K[0,1]*F[1,0]
    gs=[gamma(Y,F) for Y in Ys];successors=[g*z for g in gs]
    gap=float(abs(successors[0]-successors[1]));assert gap>1e-3
    residuals=[]
    for Y,g in zip(Ys,gs):
        r=update(K,F,np.eye(2)/2,Y,np.eye(2));assert r['terminal'] is None
        Kn=r['v']@r['k']@r['v'].conj().T
        residuals.append(float(abs(Kn[0,1]*F[1,0]-g*z)))
    # Direct mechanical comparison is a counterexample/control, no empirical claim.
    a,b,h=3.,.1,.1
    sol=solve_ivp(lambda _,x:[x[1],-a*np.sin(x[0])-b*x[1]],(0,h),[.3,0.],method='DOP853',rtol=1e-12,atol=1e-14)
    assert sol.success and abs(sol.y[1,-1])>.01
    assert max(residuals)<1e-10 and all(0<g<=1 for g in gs)
    result=dict(kind='synthetic proof/code controls only',initial_signed_pair=[float(z.real),float(z.imag)],geometry_cases=[[.2,.7],[.3,.8]],gamma=gs,successor_pair_gap=gap,max_ambient_residual=max(residuals),direct_pendulum_control=dict(a=a,b=b,h=h,initial_angle=.3,initial_velocity=0.,physical_final_velocity=float(sol.y[1,-1]),coherence_radial_final_velocity=0.),holdout_accessed=False)
    Path(out).mkdir(parents=True,exist_ok=True);Path(out,'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'results')
