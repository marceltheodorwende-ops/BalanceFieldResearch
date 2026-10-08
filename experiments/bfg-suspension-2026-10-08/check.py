"""Conditional suspension/readout controls, no real measurements or force fitting."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import root
s=sp.symbols('s',real=True)
cs=sp.symbols('c0:6');poly=sum(cs[i]*s**i for i in range(6))
q0,q1,v0,v1,a0,a1=sp.symbols('q0 q1 v0 v1 a0 a1')
target=[q0,v0,a0,q1,v1,a1]
conditions=[sp.diff(poly,s,k).subs(s,t)-v for t,k,v in zip([0,0,0,1,1,1],[0,1,2,0,1,2],target)]
coeff=sp.solve(conditions,cs)
Q=sp.expand(poly.subs(coeff));bump=s**3*(1-s)**3*(s-sp.Rational(1,2))**2
for t in [0,1]:
    for k in range(3):assert sp.diff(bump,s,k).subs(s,t)==0
assert bump.subs(s,sp.Rational(1,2))==0 and sp.diff(bump,s).subs(s,sp.Rational(1,2))==0
assert sp.diff(bump,s,2).subs(s,sp.Rational(1,2))==sp.Rational(1,32)
for t,k,v in zip([0,0,0,1,1,1],[0,1,2,0,1,2],target):assert sp.simplify(sp.diff(Q,s,k).subs(s,t)-v)==0
qfun=sp.lambdify((s,q0,q1,v0,v1,a0,a1),[Q,sp.diff(Q,s),sp.diff(Q,s,2)],'numpy')
bfun=sp.lambdify(s,[bump,sp.diff(bump,s),sp.diff(bump,s,2)],'numpy')
def R(y):
    y=np.asarray(y,float);p=np.array([1/3,2/3]);lc=np.sum(p/(1+y));lb=np.sum(p*y*y/(1+y));alpha=lb/(lc+lb)
    return (alpha+(1-alpha)*y*y)/(1+y)**2

def data(y):
    yn=R(y);ynn=R(yn);q=y[0]-y[1];qn=yn[0]-yn[1];qnn=ynn[0]-ynn[1]
    return q,qn,qn-q,qnn-qn,0.,0.

def read(y,phase,lam=0.):return np.asarray(qfun(phase,*data(y)),float)+lam*np.asarray(bfun(phase),float)
z=np.array([.2,.7]);endpoint=[]
for u in [z,z+np.array([.001,-.001]),R(z)]:
    d=data(u);endpoint.append(float(np.max(abs(read(u,0)-np.array([d[0],d[2],0.])))))
    endpoint.append(float(np.max(abs(read(u,1)-read(R(u),0)))))
assert max(endpoint)<1e-12
r0=read(z,.5,0);r1=read(z,.5,1)
assert np.max(abs(r0[:2]-r1[:2]))<1e-14 and abs(r1[2]-r0[2]-1/32)<1e-14
# Same-model local fiber witness: vary phase and adjust prepared geometry.
target_pair=r0[:2]
sol=root(lambda yy:read(yy,.51)[:2]-target_pair,z,tol=1e-11)
assert sol.success and np.all(sol.x>0) and np.all(sol.x<1)
other=read(sol.x,.51)
assert np.max(abs(other[:2]-target_pair))<1e-10
assert abs(other[2]-r0[2])>1e-4
# Independently verify kinematic derivatives by finite differences.
eps=1e-5
fd1=(read(z,.5+eps)[0]-read(z,.5-eps)[0])/(2*eps)
fd2=(read(z,.5+eps)[1]-read(z,.5-eps)[1])/(2*eps)
assert abs(fd1-r0[1])<1e-8 and abs(fd2-r0[2])<1e-8
# Exact differential obstruction to a planar acceleration factor.
x,y=sp.symbols('x y',positive=True)
pw=sp.Rational(1,3)
lc=pw/(1+x)+(1-pw)/(1+y);lb=pw*x*x/(1+x)+(1-pw)*y*y/(1+y);al=lb/(lc+lb)
rs=sp.Matrix([(al+(1-al)*u*u)/(1+u)**2 for u in [x,y]])
jrs=rs.jacobian([x,y]);ez=sp.Matrix([sp.Rational(1,5),sp.Rational(7,10)])
zsub=dict(zip([x,y],ez));ez1=rs.subs(zsub);ez2=rs.subs(dict(zip([x,y],ez1)))
J0=jrs.subs(zsub);J1=jrs.subs(dict(zip([x,y],ez1)))
L=sp.Matrix([[1,-1]]);grad0=L;grad1=L*J0;grad2=L*J1*J0
D=sp.Matrix.vstack(grad0,grad1,grad1-grad0,grad2-grad1,sp.zeros(1,2),sp.zeros(1,2))
ed=sp.Matrix([(L*ez)[0],(L*ez1)[0],(L*(ez1-ez))[0],(L*(ez2-ez1))[0],0,0]);params=[q0,q1,v0,v1,a0,a1];esub=dict(zip(params,ed));rows=[]
for k in range(3):
    expr=sp.diff(Q,s,k).subs(s,sp.Rational(1,2))
    coef=sp.Matrix([[sp.diff(expr,v) for v in params]])
    dphase=sp.diff(Q,s,k+1).subs(s,sp.Rational(1,2)).subs(esub)
    rows.append((coef*D).row_join(sp.Matrix([[dphase]])))
triple_det=sp.factor(sp.Matrix.vstack(*rows).det())
assert triple_det!=0
state=np.r_[z,.5];ee=1e-6
def allobs(u):return read(u[:2],u[2])
numtriple=np.column_stack([(allobs(state+ee*np.eye(3)[i])-allobs(state-ee*np.eye(3)[i]))/(2*ee) for i in range(3)])
triple_error=abs(np.linalg.det(numtriple)-float(triple_det));assert triple_error<1e-7


from experiment import update
tensor_errors=[]
for m in [2,3]:
    Y=np.kron(np.diag(z),np.eye(m));F=np.kron(np.diag([1.,2.]),np.eye(m)/m);W=np.eye(2*m)/(2*m);K=np.kron(np.array([[1.,.2j],[-.2j,-1.]]),np.eye(m))
    out=update(K,F,W,Y,np.eye(2*m));assert out['terminal'] is None
    natural=out['v']@out['y']@out['v'].conj().T
    tensor_errors.append(float(np.max(abs(natural-np.kron(np.diag(R(z)),np.eye(m))))))
assert max(tensor_errors)<1e-10
result=dict(triple_determinant_difference_residual=float(triple_error),exact_acceleration_fiber_rank_determinant=str(triple_det),acceleration_fiber_rank_determinant=float(triple_det),tensor_multiplicities=[2,3],max_tensor_geometry_residual=max(tensor_errors),kind='synthetic mathematics/code controls only',exact_bump_acceleration_gap='1/32',max_seam_jet_residual=max(endpoint),same_sampled_readout_midpoint=r0[:2].tolist(),base_midpoint_acceleration=float(r0[2]),alternative_midpoint_acceleration=float(r1[2]),within_model_fiber_witness=dict(first_geometry=z.tolist(),first_phase=.5,second_geometry=sol.x.tolist(),second_phase=.51,observable_residual=float(np.max(abs(other[:2]-target_pair))),acceleration_gap=float(other[2]-r0[2])),kinematic_difference_residuals=[float(abs(fd1-r0[1])),float(abs(fd2-r0[2]))],declared_extra_phase=True,seconds_calibrated=False,planar_factor_closed=False,physical_force_derived=False,holdout_accessed=False)
Path(__file__).with_name('results').joinpath('controls.json').write_text(json.dumps(result,indent=2)+'\n')
Path(__file__).with_name('results').joinpath('quintic.txt').write_text(str(Q)+'\n')
print(json.dumps(result,indent=2))
