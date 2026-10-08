import json
from pathlib import Path
import sympy as s
import numpy as np
from experiment import update
Y=s.diag(s.Rational(1,5),s.Rational(7,10));F=s.diag(1,2);I=s.eye(2);eta=s.Rational(1,10)
vals=[];errs=[];eigs=[]
for J in [s.zeros(2),s.Matrix([[0,s.Rational(1,5)],[s.Rational(1,5),0]])]:
 Z=Y+eta*s.I*(Y*J-J*Y);C=(I+Z).inv();B=Z*C
 lc=s.trace(F*C);lb=s.trace(F*Z*Z*C);a=lb/(lc+lb);R=s.simplify(a*C*C+(1-a)*B*B)
 q=s.trace(F*Y)/s.trace(F);p=s.trace(F*J)/s.trace(F);qn=s.factor(s.trace(F*R)/s.trace(F));vals.append([str(q),str(p),str(qn)])
 z=np.array(Z,complex);j=np.array(J,complex);f=np.array(F,float);rr=np.array(R,complex)
 assert min(np.linalg.eigvalsh(z))>0 and max(np.linalg.eigvalsh(z))<1
 out=update(j,f,np.eye(2)/2,z,np.eye(2));assert out['terminal'] is None
 back=out['v']@out['y']@out['v'].conj().T;errs.append(float(np.max(abs(back-rr))));eigs.append(np.linalg.eigvalsh(z).tolist())
gap=s.factor(s.Rational(vals[1][2])-s.Rational(vals[0][2]));assert gap!=0 and vals[0][:2]==vals[1][:2]
# Rank2 input directions deltaY=I and deltaJ=I give identity readout Jacobian.
assert s.trace(F*I)/s.trace(F)==1
# Exact infinitesimal fiber witness at nonzero transverse amplitude.
t=s.symbols('t',real=True);J=s.Matrix([[0,t],[t,0]]);Z=Y+eta*s.I*(Y*J-J*Y);C=(I+Z).inv();B=Z*C
lc=s.trace(F*C);lb=s.trace(F*Z*Z*C);a=lb/(lc+lb);qn=s.factor(s.trace(F*(a*C*C+(1-a)*B*B))/s.trace(F))
der=s.factor(s.diff(qn,t).subs(t,s.Rational(1,5)));assert der!=0
fn=s.lambdify(t,qn,'numpy');eps=1e-5;fd=(fn(.2+eps)-fn(.2-eps))/(2*eps);error=abs(fd-float(der));assert error<1e-9
res=dict(fiber_derivative_difference_error=float(error),exact_readouts=vals,exact_successor_gap=str(gap),successor_gap=float(gap),exact_fiber_derivative=str(der),fiber_derivative=float(der),prepared_eigenvalues=eigs,max_ambient_error=max(errs),readout_rank=2,kind='synthetic mathematics/code controls',force_derived=False,holdout_accessed=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
