import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from closure import observe,advance,ChartExit,spectral_observe,spectral_advance
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'real-eeg-covariance-2026-10-07'))
sys.path.insert(0,str(ROOT/'bfg-matrix-tangent-2026-10-08'))
from experiment import update
from control import natural

def residual(a,b):return max(float(np.max(abs(np.asarray(x)-np.asarray(y)))) for x,y in zip(a,b))

def main(out):
    rng=np.random.default_rng(202610081);errors=[];gauge=[];spectral_errors=[];swaps=0
    for _ in range(100):
        y=np.sort(rng.uniform(.08,.85,2));Y=np.diag(y)
        z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));K=(z+z.conj().T)/2
        z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));F=z@z.conj().T+.2*np.eye(2);W=np.eye(2)/2
        initial=observe(K,F,Y);predicted=advance(initial)
        r=update(K,F,W,Y,np.eye(2));assert r['terminal'] is None
        actual=observe(r['k'],r['f'],r['y']);errors.append(residual(predicted,actual))
        spectral_errors.append(residual(spectral_advance(spectral_observe(K,F,Y)),spectral_observe(r['k'],r['f'],r['y'])))
        _,naturalY,_=natural(K,F,Y);swaps+=int(naturalY[0,0].real>naturalY[1,1].real)
        Q=np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)))[0]
        transform=lambda X:Q@X@Q.conj().T
        gauge.append(residual(initial,observe(transform(K),transform(F),transform(Y))))
    # Same geometry spectrum, different formation weights: spectrum-only factor fails.
    Y=np.diag([.2,.7]);K=np.diag([1.,0.]);Fa=np.diag([.8,.2]);Fb=np.diag([.2,.8])
    _,Ya,_=natural(K,Fa,Y);_,Yb,_=natural(K,Fb,Y)
    eigen_only_failure=float(np.linalg.norm(np.sort(np.linalg.eigvalsh(Ya))-np.sort(np.linalg.eigvalsh(Yb))))
    assert eigen_only_failure>1e-3
    # Same weighted geometry AND same tr(FK); different coherence changes tr(FK)+.
    F=np.array([[1.,.3],[.3,1.]]);Ka=np.diag([1.,0.]);Kb=np.array([[.4,1.],[1.,0.]])
    assert abs(np.trace(F@Ka)-np.trace(F@Kb))<1e-12
    Kan,_,_=natural(Ka,F,Y);Kbn,_,_=natural(Kb,F,Y)
    kernel_failure=float(abs(np.trace(F@Kan)-np.trace(F@Kbn)));assert kernel_failure>1e-3
    # An admissible canonical event can exit this particular readout chart.
    def gap(weight):
        _,R,_=natural(Ka,np.diag([weight,1-weight]),Y);return float((R[1,1]-R[0,0]).real)
    weight=brentq(gap,1e-6,1-1e-6,xtol=1e-14);Fc=np.diag([weight,1-weight])
    r=update(Ka,Fc,np.eye(2)/2,Y,np.eye(2));assert r['terminal'] is None
    try:advance(observe(Ka,Fc,Y))
    except ChartExit:collision_gate=True
    else:raise AssertionError('collision gate missing')
    collision_residual=residual(spectral_advance(spectral_observe(Ka,Fc,Y)),spectral_observe(r['k'],r['f'],r['y']))
    assert max(errors+gauge+spectral_errors+[collision_residual])<1e-10
    result=dict(kind='synthetic mathematical/code controls; no empirical evaluation',ambient_factor_cases=100,unitary_gauge_cases=100,max_factor_residual=max(errors),max_gauge_residual=max(gauge),output_order_swaps=swaps,max_spectral_factor_residual=max(spectral_errors),collision_safe_factor_residual=collision_residual,eigenvalue_only_counterexample_successor_gap=eigen_only_failure,aggregate_kernel_counterexample_successor_gap=kernel_failure,collision_formation_weight=weight,collision_canonical_terminal=r['terminal'],collision_chart_gate=collision_gate,holdout_accessed=False)
    Path(out).mkdir(parents=True,exist_ok=True);Path(out,'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'results')
