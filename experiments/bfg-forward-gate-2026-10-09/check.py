"""P57 math/code controls only; import update without data evaluation.
PYTHONPATH=experiments/real-eeg-covariance-2026-10-07 python experiments/bfg-forward-gate-2026-10-09/check.py
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
from experiment import update
t,q=sp.symbols('t q',positive=True);h=t*q
u=[t+h,t-h];c=[1/(1+x) for x in u];b=[x*y for x,y in zip(u,c)]
m=t*t+h*h*(1-t)/(1+t);al=m/(1+m);ev=[al*x*x+(1-al)*y*y for x,y in zip(c,b)]
A=sp.cancel(sum(ev)/2);V=sp.cancel((ev[0]-ev[1])/2);G2=sp.cancel((al*c[0]*c[1]+(1-al)*b[0]*b[1])**2/(ev[0]*ev[1]))
E=(1+t)**3+q*q*(1-2*t*t-t**3)+q**4*t*t
N=(1+t)*(1-t*t+q*q*(t*t-2*t))
assert sp.cancel(V/(A*q)-N/E)==0
rhs=t*(q**4*(2+2*t-t*t)+q*q*(1-t*t)+2*(1+t)**2)/((1+q*q)*E)
assert sp.cancel(1/(1+q*q)-V/(A*q)-rhs)==0
fa=sp.lambdify((t,q),A,'numpy');fv=sp.lambdify((t,q),V,'numpy');fg=sp.lambdify((t,q),G2,'numpy')
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2)
Q=1/np.sqrt(2);L=(1+Q)/2;rng=np.random.default_rng(57);errors=[];margins=[]
for _ in range(60):
    tt=rng.uniform(.08,.5);qq=rng.uniform(.02,.99);s=rng.uniform(.02,5);phi=rng.uniform(-np.pi,np.pi);r=tt*qq/np.sqrt(1+.04*s*s)
    Y=tt*I+r*(np.cos(phi)*S[0]+np.sin(phi)*S[1]);J=s*S[2];W=I/2+.2*S[0];Z=Y+.1j*(Y@J-J@Y)
    out=update(J,1.7*I,W,Z,I);assert out['terminal'] is None
    vv=out['v'];yn=vv@out['y']@vv.conj().T;jn=vv@out['k']@vv.conj().T
    tn=np.trace(yn).real/2;rn=np.sqrt(np.trace((yn-tn*I)@(yn-tn*I)).real/2);sn=np.sqrt(np.trace(jn@jn).real/2);qn=rn*np.sqrt(1+.04*sn*sn)/tn
    expected=[fa(tt,qq),fv(tt,qq),s*np.sqrt(fg(tt,qq))];errors.append(float(max(abs(np.array([tn,rn,sn])-expected))))
    assert 0<tn<tt and 0<sn<s and 0<qn<=Q+1e-10
    assert tn*(1+qn)<1 and tn*(1-qn)>0
    margins.append(float(1-tn*(1+qn)))
assert max(errors)<1e-10
# Canceled rational formulas avoid subtracting nearly equal tiny a+/a-.
ma=sp.lambdify((t,q),A,'mpmath');mv=sp.lambdify((t,q),V,'mpmath');mg=sp.lambdify((t,q),G2,'mpmath')
def trajectory(dps):
    mp.mp.dps=dps;tt=mp.mpf('.4');qq=mp.mpf('.8');s=mp.mpf('4');eta=mp.mpf('.1');cost=mp.mpf(0);minrel=mp.mpf(1)
    t0=tt;t1=None;Qm=1/mp.sqrt(2);Lm=(1+Qm)/2
    for k in range(50):
        assert 0<qq<1 and tt*(1+qq)<1 and s<=5
        cost+=2*eta*s*tt*qq/mp.sqrt(1+4*eta*eta*s*s)
        tn=ma(tt,qq);rn=mv(tt,qq);sn=s*mp.sqrt(mg(tt,qq));qn=rn*mp.sqrt(1+4*eta*eta*sn*sn)/tn
        assert 0<qn<=Qm and 0<sn<s and 0<tn<tt
        if k>=1:assert tn<=Lm*tt
        if t1 is None:t1=tn
        minrel=min(minrel,1-qn);tt,qq,s=tn,qn,sn
    assert cost<=t0+t1/(1-Lm)
    return {'events':50,'final_q':str(qq),'final_s':str(s),'log10_final_t':str(mp.log10(tt)),'sum_input_norm':str(cost),'min_relative_margin':str(minrel)}
lo=trajectory(60);hi=trajectory(100)
assert abs(mp.mpf(lo['final_q'])-mp.mpf(hi['final_q']))<mp.mpf('1e-45')
assert abs(mp.mpf(lo['final_s'])-mp.mpf(hi['final_s']))<mp.mpf('1e-45')
# Preserve the previously admitted, but not forward-admitted, large-s case.
mp.mp.dps=80;tt=mp.mpf('.5');qq=mp.mpf('.8');ss=mp.mpf(100)
tn=ma(tt,qq);sn=ss*mp.sqrt(mg(tt,qq));qn=mv(tt,qq)*mp.sqrt(1+mp.mpf('.04')*sn*sn)/tn
outside_margin=tn*(1-qn);assert outside_margin<0
res={'symbolic_checks':2,'ambient_cases':60,'max_ambient_endpoint_error':max(errors),'min_sample_upper_gate_margin':min(margins),'certified_Q':Q,'certified_lambda':L,'trajectory_100_digits':hi,'precision_comparison_q_error':str(abs(mp.mpf(lo['final_q'])-mp.mpf(hi['final_q']))),'preserved_outside_domain_next_lower_margin':str(outside_margin),'kind':'synthetic math/code only','holdout_accessed':False,'physical_force_derived':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
