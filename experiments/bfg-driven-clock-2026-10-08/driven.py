"""Explicitly augmented input model; event count is trajectory bookkeeping."""
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp

L=16/27

def f(x):return 2*x*x/((1+x)**2*(1+x*x))

@dataclass(frozen=True)
class AugmentedScalar:
    K: float
    F: float
    y: float
    event: int=0

def advance(state,d):
    if state.F<=0 or state.event<0 or not 0<=state.y<=.25 or not 0<d<.75:raise ValueError('declared invariant domain')
    return AugmentedScalar(state.K,state.F,float(f(state.y+d)),state.event+1)

def sensitivity_bound(initial_error,input_error,output_error,events):
    if min(initial_error,input_error,output_error,events)<0:raise ValueError('nonnegative bounds')
    return L**events*initial_error+(L*input_error+output_error)*(1-L**events)/(1-L)

def physical_projection(state,decode,step,a,b):
    # supplied flow and physical seconds are explicitly additional assumptions
    if step<=0 or a<=0 or b<0:raise ValueError('physical calibration domain')
    x=np.asarray(decode(state.F,state.K),dtype=float)
    t=state.event*step
    if t==0:return x
    solution=solve_ivp(lambda _,z:[z[1],-a*np.sin(z[0])-b*z[1]],(0,t),x,method='DOP853',rtol=1e-11,atol=1e-13)
    if not solution.success:raise RuntimeError(solution.message)
    return solution.y[:,-1]
