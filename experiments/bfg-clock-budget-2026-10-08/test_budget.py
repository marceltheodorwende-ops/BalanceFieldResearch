import unittest
import numpy as np
from scipy.integrate import solve_ivp
from budget import clock_bounds

def flow(x,t,a,b):
    if t==0:return np.array(x)
    return solve_ivp(lambda _,z:[z[1],-a*np.sin(z[0])-b*z[1]],(0,t),x,method='DOP853',rtol=1e-12,atol=1e-14).y[:,-1]
class Controls(unittest.TestCase):
    def test_clock_bound_independent_flow(self):
        for x in [(0,0),(.5,-.2),(3.,.2),(4.,3.)]:
            for b in [0,.3]:
                h=6.4;eps=.01;nom=flow(x,h,4,b)
                angle,velocity=clock_bounds(x[0],x[1],4,b,h,eps)
                for sign in [-1,1]:
                    delta=abs(flow(x,h*(1+sign*eps),4,b)-nom)
                    self.assertLessEqual(delta[0],angle+1e-10)
                    self.assertLessEqual(delta[1],velocity+1e-10)
    def test_time_rescaling_nonidentifiability(self):
        c=1.03;a=4;b=.2;x=[.5,-.3];t=1.6
        physical=flow(x,c*t,a,b)
        observed=flow([x[0],c*x[1]],t,c*c*a,c*b)
        np.testing.assert_allclose(observed,[physical[0],c*physical[1]],atol=1e-10)
    def test_invalid_backward_range(self):
        with self.assertRaises(ValueError):clock_bounds(.3,0,4,.2,1,1.1)
if __name__=='__main__':unittest.main()
