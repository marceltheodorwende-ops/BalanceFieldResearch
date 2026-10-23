"""BFG state-clock constructions; no physical clock calibration."""
from __future__ import annotations
import json
import math
import platform
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

HERE=Path(__file__).resolve().parent
TOL=1e-10
SEED=20261027
N=48
Q=4/9

def f(y): return 2*y*y/((1+y)**2*(1+y*y))

def exact_checks():
    y=s.symbols('y', positive=True)
    # Both factors in the envelope are nonnegative on (0,1/2].
    assert s.cancel(s.Rational(4,9)-2*y/(1+y)**2-2*(1-2*y)*(2-y)/(9*(1+y)**2))==0
    assert s.cancel(f(y)/y-2*y/((1+y)**2*(1+y*y)))==0
    assert s.cancel(2*f(y)-(2*y)**2/((1+y)**2*(1+y*y)))==0
    witnesses=[dict(y=str(z),successor=str(s.cancel(f(z)))) for z in
               (s.Rational(1,5),s.Rational(1,4),s.Rational(3,10))]
    return dict(envelope='f(y)/y <= 2y/(1+y)^2 <= 4/9 on 0<y<=1/2',
                rational_scalar_witnesses=witnesses,
                load_duration_sum_bound='sum tr(Y_k)/n <= 9 M_0/5',
                scalar_clock='A(f(y))=2 A(y); tau=log_2 A')

def event_coordinate(y,steps=N):
    """Log-domain evaluation; no continuation of the source below its cutoff."""
    a=-math.log(2*y)
    for _ in range(steps):
        z=0.5*math.exp(-a)
        log_d=2*math.log1p(z)+math.log1p(z*z)
        a=2*a+log_d
    value=math.ldexp(a,-steps)
    return math.log2(value),value

def scalar_checks(update):
    rows=[]
    max_source=max_tick=max_perturbed=0.
    epsilon=1/(8*math.pi)
    for y in (.2,.25,.3):
        out=pair_audit.source_aligned(update,np.eye(2),np.eye(2),np.eye(2)/2,y*np.eye(2))
        residual=float(np.linalg.norm(out['y']-f(y)*np.eye(2)))
        t,a=event_coordinate(y); tp,ap=event_coordinate(f(y))
        pert=lambda z:z+epsilon*math.sin(2*math.pi*z)
        tick=abs(tp-t-1)
        pert_tick=abs(pert(tp)-pert(t)-1)
        max_source=max(max_source,residual); max_tick=max(max_tick,tick)
        max_perturbed=max(max_perturbed,pert_tick)
        assert residual<TOL and tick<TOL and pert_tick<TOL
        rows.append(dict(y=y,source_successor=f(y),source_residual=residual,
                         A_N=a,tau_N=t,A_successor_N=ap,unit_tick_residual=tick,
                         perturbed_tau_N=pert(t),perturbed_tick_residual=pert_tick,
                         nonuniqueness_difference=pert(t)-t))
    assert max(abs(z['nonuniqueness_difference']) for z in rows)>1e-3
    return dict(full_source_calls=3,log_recurrence_steps=N,
                analytic_A_truncation_bound=math.ldexp(2*math.log1p(.3)+math.log1p(.09),-N),
                truncation_bound_is_not_a_machine_roundoff_bound=True,
                epsilon=epsilon,phase_reparametrization_derivative_lower_bound=.75,
                max_source_residual=max_source,max_unit_tick_residual=max_tick,
                max_perturbed_tick_residual=max_perturbed,cases=rows)

def complex_checks(update):
    rng=np.random.default_rng(SEED)
    rows=[]; max_envelope=max_telescoping=0.; min_log=math.inf
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n)
            y=(u*np.linspace(.2,.3,n))@u.conj().T
            formation=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            k=(raw+raw.conj().T)/2
            initial_trace=float(np.trace(y).real)
            initial_max=float(np.linalg.eigvalsh(y)[-1])
            log_sum=load_sum=0.
            for event in range(2):
                current_trace=float(np.trace(y).real)
                current_max=float(np.linalg.eigvalsh(y)[-1])
                out=pair_audit.source_aligned(update,k,formation,w,y)
                next_trace=float(np.trace(out['y']).real)
                next_max=float(np.linalg.eigvalsh(out['y'])[-1])
                duration_load=current_trace/n
                duration_log=math.log(current_trace/next_trace)
                load_sum+=duration_load; log_sum+=duration_log
                violation=max(0.,next_max-Q*current_max)
                telescope=abs(log_sum-math.log(initial_trace/next_trace))
                assert violation<TOL and telescope<TOL
                assert duration_log>0 and duration_load>0
                assert load_sum<=initial_max/(1-Q)+TOL
                max_envelope=max(max_envelope,violation)
                max_telescoping=max(max_telescoping,telescope)
                min_log=min(min_log,duration_log)
                rows.append(dict(n=n,case=case,event=event+1,load_duration=duration_load,
                                 log_duration=duration_log,partial_load_sum=load_sum,
                                 infinite_load_sum_upper_bound=initial_max/(1-Q),
                                 partial_log_sum=log_sum,telescoping_residual=telescope,
                                 envelope_violation=violation))
                k,formation,w,y=out['k'],out['f'],out['w'],out['y']
    return dict(preparations=12,full_source_events=len(rows),maximum_envelope_violation=max_envelope,
                maximum_log_telescoping_residual=max_telescoping,minimum_log_duration=min_log,cases=rows)

def run():
    update=audit.load_update()
    return dict(scope='Full-persistence C and scalar y<=3/10; mathematical clocks only',
                source_blob=audit.EXPECTED_SOURCE_BLOB,seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=exact_checks(),scalar=scalar_checks(update),full_source=complex_checks(update),
                status='PASS for constructions and scoped ambiguity; physical clock/current/Einstein OPEN')

if __name__=='__main__':
    result=run()
    (HERE/'clock_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
