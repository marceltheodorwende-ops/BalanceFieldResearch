import unittest
import numpy as np
from scipy.integrate import solve_ivp
from phase import encode,decode,rhs,forecast

class Controls(unittest.TestCase):
    def test_roundtrip(self):
        rng=np.random.default_rng(724)
        e=rng.uniform(1e-8,1.9,100);p=rng.uniform(-20,20,100)
        t,w=decode(e,p,3.);ee,pp=encode(t,w,3.)
        np.testing.assert_allclose(ee,e,atol=2e-15)
        tt,ww=decode(ee,pp,3.)
        np.testing.assert_allclose(tt,t,atol=2e-14)
        np.testing.assert_allclose(ww,w,atol=2e-14)
    def test_independent_flow(self):
        for a,b,t,w in [(3.,.04,.7,.2),(1.,0.,2.,.1),(4.,.5,1e-7,-2e-7)]:
            e,p=encode(t,w,a)
            cart=solve_ivp(lambda _,z:[z[1],-a*np.sin(z[0])-b*z[1]],(0,6.4),[t,w],method='DOP853',rtol=1e-11,atol=1e-13)
            polar=solve_ivp(lambda _,z:rhs(z[0],z[1],a,b),(0,6.4),[np.log(e),p],method='DOP853',rtol=1e-11,atol=1e-13)
            result=decode(np.exp(polar.y[0,-1]),polar.y[1,-1],a)
            np.testing.assert_allclose(result,cart.y[:,-1],rtol=0,atol=1e-8)
            np.testing.assert_allclose(forecast(t,w,a,b,6.4),cart.y[:,-1],rtol=0,atol=1e-5)
    def test_conservation(self):
        t,w=forecast(np.array([.8]),np.array([.2]),3.,0.,6.4)
        e,_=encode(t,w,3.);initial,_=encode(.8,.2,3.)
        np.testing.assert_allclose(e,initial,atol=2e-15)
    def test_rest_and_domains(self):
        np.testing.assert_array_equal(forecast(0.,0.,3.,.1,6.4),(0.,0.))
        for t,w in [(np.pi,0.),(0.,4.)]:
            with self.assertRaises(ValueError):encode(t,w,3.)
        with self.assertRaises(ValueError):forecast(0.,0.,3.,-.1,1.)

if __name__=='__main__':unittest.main()
