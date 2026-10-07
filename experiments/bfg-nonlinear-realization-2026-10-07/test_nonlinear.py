import unittest,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.special import ellipk
from nonlinear import prepare,decode,flow,readout,energy
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'bfg-pendulum-motion-2026-10-07'))
sys.path.insert(0,str(ROOT/'real-eeg-covariance-2026-10-07'))
from motion import event_clock,Y0
from experiment import update
class Controls(unittest.TestCase):
    def test_actual_ambient_closure(self):
        for theta,w in [(0,0),(.3,-.4),(1.5,0),(4.,2.)]:
            F,K=prepare(theta,w)
            s=update(np.array([[K]]),np.array([[F]]),np.ones((1,1)),np.array([[Y0]]),np.ones((1,1)))
            self.assertIsNone(s['terminal'])
            p=readout(s['f'][0,0],s['k'][0,0],event_clock(s['y'][0,0]),4.,.2)
            np.testing.assert_allclose(p,flow([theta,w],.1,4.,.2),atol=1e-10)
    def test_composition(self):
        for alpha in [0,.5,1]:
            np.testing.assert_allclose(flow(flow([1.2,.4],.7,4.,.2,alpha),1.1,4.,.2,alpha),flow([1.2,.4],1.8,4.,.2,alpha),atol=1e-9)
    def test_independent_period(self):
        for amplitude in [.3,1.5,2.8]:
            T=4*ellipk(np.sin(amplitude/2)**2)/2
            np.testing.assert_allclose(flow([amplitude,0],T,4.,0),[amplitude,0],atol=1e-8)
    def test_linear_endpoint(self):
        M=np.array([[0,1],[-4,-.2]])
        np.testing.assert_allclose(flow([1.5,.2],3.,4.,.2,0),expm(M*3)@np.array([1.5,.2]),atol=1e-9)
    def test_energy_and_nonuniqueness(self):
        x=np.array([1.5,0.])
        for alpha in [0,.5,1]:
            self.assertLess(energy(flow(x,3.,4.,.2,alpha),4.,alpha),energy(x,4.,alpha))
            self.assertAlmostEqual(energy(flow(x,3.,4.,0,alpha),4.,alpha),energy(x,4.,alpha),places=8)
        self.assertGreater(np.linalg.norm(flow(x,1.,4.,0,0)-flow(x,1.,4.,0,1)),.1)
    def test_rest_encoding(self):
        F,K=prepare(0,0);self.assertEqual(F,1)
        np.testing.assert_allclose(readout(F,K,100,4,.2),[0,0],atol=1e-12)
        F,K=prepare(4.,2.);np.testing.assert_allclose(decode(F,K),[4.,2.],atol=1e-12)
if __name__=='__main__':unittest.main()
