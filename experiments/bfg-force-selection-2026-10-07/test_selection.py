import unittest
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
from selection import forecast
class Controls(unittest.TestCase):
    def test_linear_reference(self):
        x=np.array([.4]);w=np.array([-.2]);c=np.array([4.,0,0,.3]);h=np.array([6.4])
        p=forecast(x,w,c,h);q=expm(np.array([[0,1],[-4,-.3]])*6.4)@np.array([.4,-.2])
        np.testing.assert_allclose(np.array(p)[:,0],q,atol=1e-8)
    def test_independent_harmonic_solver(self):
        c=np.array([0.,3.,.4,.2]);x=np.array([.6]);w=np.array([.2]);h=np.array([6.4])
        p=forecast(x,w,c,h)
        def rhs(t,z):return [z[1],-3*np.sin(z[0])-.4*np.sin(2*z[0])-.2*z[1]]
        q=solve_ivp(rhs,(0,6.4),[.6,.2],method='DOP853',rtol=1e-12,atol=1e-14).y[:,-1]
        np.testing.assert_allclose(np.array(p)[:,0],q,atol=1e-8)
    def test_geometric_torque(self):
        theta=np.linspace(-3,3,101);m,g,L=2.,9.81,.5;h=1e-6
        V=lambda z:m*g*L*(1-np.cos(z))
        torque=-(V(theta+h)-V(theta-h))/(2*h)
        np.testing.assert_allclose(torque,-m*g*L*np.sin(theta),atol=3e-9)
if __name__=='__main__':unittest.main()
