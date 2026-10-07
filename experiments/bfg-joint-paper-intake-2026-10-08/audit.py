"""Fresh synthetic controls for both user-authorized BFG papers."""
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'real-eeg-covariance-2026-10-07'))
sys.path.insert(0,str(ROOT/'bfg-pendulum-motion-2026-10-07'))
from experiment import update
from motion import event_clock

def scalar(y):return 2*y*y/((1+y)**2*(1+y*y))
def main():
    rng=np.random.default_rng(20261008);support=[];mass=[];balance=[];stock=[];later=[]
    for _ in range(40):
        n=3;z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));u=np.linalg.qr(z)[0];Y=u@np.diag([.2,.6,1.4])@u.conj().T
        v=rng.normal(size=n)+1j*rng.normal(size=n);v/=np.linalg.norm(v);P=np.outer(v,v.conj())
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));F=z@z.conj().T+.1*np.eye(n)
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));W=z@z.conj().T;W/=np.trace(W);K=-np.eye(n)
        r=update(K,F,W,Y,P);assert r['terminal'] is None
        assert len(r['y'])<=n and np.min(np.linalg.eigvalsh(r['y']))>0 and np.max(np.linalg.eigvalsh(r['y']))<1
        support.append(float(np.linalg.norm(r['t4'].conj().T@r['t4']-r['psel'])));mass.append(abs(r['m4']-1));balance.append(abs(r['alpha']*r['lc']-(1-r['alpha'])*r['lb']))
        # Here rank(QP)=rank(P)=1, so the source support is P; K=-I seeds exactly unit stock.
        fsel=np.trace(P@F).real;seed=np.trace(r['f']).real-fsel
        E=np.eye(len(r['y']))-r['t4']@r['t4'].conj().T
        expected_seed=1. if np.trace(E).real>.5 else 0.
        stock.append(abs((np.trace(r['f']).real-np.trace(F).real)-(expected_seed-(np.trace(F).real-fsel))))
        s=update(r['k'],r['f'],r['w'],r['y'],r['p']);assert s['terminal'] is None;later.append(abs(s['msel']-1))
    assert max(support+mass+balance+stock+later)<1e-10
    d=.15;fixed=brentq(lambda y:scalar(y+d)-y,0,.25,xtol=1e-14);ys=np.linspace(0,.84,100)
    for _ in range(60):ys=scalar(ys+d)
    driven_error=float(np.max(abs(ys-fixed)));assert driven_error<1e-12
    grid=np.linspace(0,1,10001);derivative=4*grid*(1-grid**3)/((1+grid)**3*(1+grid*grid)**2);assert np.max(derivative)<=16/27+1e-12
    Y=np.diag([.2,.6]);K=np.array([[-1.,.2],[.2,-2.]]);F=np.array([[2.,.1],[.1,1.]]);W=np.eye(2)/2;P=np.eye(2);base=update(K,F,W,Y,P)
    m=3;I=np.eye(m);tau=I/m
    lifted=update(np.kron(K,I),np.kron(F,tau),np.kron(W,tau),np.kron(Y,I),np.kron(P,I),frames=(np.kron(base['u'],I),np.repeat(base['s'],m),np.kron(base['v'],I)))
    lift_error=max(float(np.linalg.norm(lifted[key]-np.kron(base[key],tau if key in ['f','w'] else I))) for key in ['k','f','w','y','p']);assert lift_error<1e-10
    v=np.array([1.,1.])/np.sqrt(2);P=np.outer(v,v);base_seed=update(-np.eye(2),P,P,np.diag([.2,.7]),P);assert base_seed['terminal'] is None
    replicated=update(-np.eye(4),np.kron(P,np.eye(2)/2),np.kron(P,np.eye(2)/2),np.kron(np.diag([.2,.7]),np.eye(2)),np.kron(P,np.eye(2)));assert replicated['terminal']=='T_seeddeg'
    clock_increment=float(event_clock(scalar(.25+d))-event_clock(.25));assert abs(clock_increment-1)>.01
    result=dict(stage='synthetic mathematical controls only; no empirical data',matrix_controls=40,max_R4_support_residual=max(support),max_R4_mass_residual=max(mass),max_weighted_balance_residual=max(balance),max_formation_balance_residual=max(stock),max_later_mass_residual=max(later),driven_input=d,driven_fixed_point=fixed,driven_60_step_error=driven_error,max_sampled_scalar_derivative=float(np.max(derivative)),theoretical_contraction_bound=16/27,tensor_lift_residual=lift_error,replicated_seed_terminal=replicated['terminal'],old_clock_increment_under_driven_step=clock_increment,full_differential_chain_audited=False)
    Path('control_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
