import unittest
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk
from driven import AugmentedScalar,advance,f,L,sensitivity_bound,physical_projection
class Controls(unittest.TestCase):
    def test_variable_input_bound(self):
        rng=np.random.default_rng(20261008);y=.2;z=.1;rho=.02
        for n in range(1,101):
            d=.15+rng.uniform(-rho,rho);y=f(y+d);z=f(z+.15)
            self.assertLessEqual(abs(y-z),sensitivity_bound(.1,rho,0,n)+1e-14)
            self.assertGreaterEqual(y,f(.13));self.assertLess(y,.25)
    def test_additive_output_margin(self):
        dmin,dmax=.13,.17;margin=min(f(dmin),.25-f(.25+dmax));eta=margin/4
        y=.2
        for k in range(100):
            y=f(y+(dmin if k%2 else dmax))+(eta if k%3 else -eta)
            self.assertGreater(y,0);self.assertLess(y,.25)
    def test_counter_at_geometry_fixed_point(self):
        from scipy.optimize import brentq
        y=brentq(lambda y:f(y+.15)-y,0,.25)
        s=AugmentedScalar(.2,2.,y);t=advance(s,.15)
        self.assertAlmostEqual(s.y,t.y,places=12);self.assertEqual(t.event,1)
        self.assertEqual((s.K,s.F),(t.K,t.F))
    def test_nonlinear_flow_closure(self):
        decode=lambda F,K:np.array([.6,.2]);s=AugmentedScalar(.2,2.,.2,7);t=advance(s,.15)
        x=physical_projection(s,decode,.1,4,.2)
        target=solve_ivp(lambda _,z:[z[1],-4*np.sin(z[0])-.2*z[1]],(0,.1),x,method='DOP853',rtol=1e-12,atol=1e-14).y[:,-1]
        np.testing.assert_allclose(physical_projection(t,decode,.1,4,.2),target,atol=1e-9)
    def test_independent_period(self):
        amplitude=1.5;period=2*ellipk(np.sin(amplitude/2)**2)
        s=AugmentedScalar(0,2.,.2,1)
        x=physical_projection(s,lambda F,K:[amplitude,0],period,4,0)
        np.testing.assert_allclose(x,[amplitude,0],atol=1e-8)
if __name__=='__main__':unittest.main()
