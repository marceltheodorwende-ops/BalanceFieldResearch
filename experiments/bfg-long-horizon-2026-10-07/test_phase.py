import unittest,numpy as np
from scipy.special import ellipk
from scipy.linalg import expm
from phase_corrected import prepare_corrected,corrected_readout

class Controls(unittest.TestCase):
    def test_initial_state(self):
        theta=np.array([.2,-.3,0.]);w=np.array([-.5,.4,.6])
        F,K=prepare_corrected(theta,w,20.,.05)
        a,v=corrected_readout(F,K,0,20.,.05)
        np.testing.assert_allclose(a,theta,atol=1e-12);np.testing.assert_allclose(v,w,atol=1e-12)
    def test_independent_elliptic_period(self):
        for amplitude in [.1,.2,.4]:
            exact=4*ellipk(np.sin(amplitude/2)**2)/np.sqrt(20.)
            leading=2*np.pi/(np.sqrt(20.)*(1-amplitude**2/16))
            self.assertLess(abs(leading/exact-1),.004*amplitude**4)
    def test_linear_limit(self):
        theta,w=1e-6,-2e-6
        F,K=prepare_corrected(theta,w,20.,.05)
        predicted=corrected_readout(F,K,4,20.,.05)
        expected=expm(np.array([[0.,1.],[-20.,-.05]])*.4)@np.array([theta,w])
        np.testing.assert_allclose(predicted,expected,atol=1e-15)
    def test_domain_gate(self):
        with self.assertRaises(ValueError):prepare_corrected(np.array([1.2]),np.array([0.]),20.,.05)

if __name__=='__main__':unittest.main()
