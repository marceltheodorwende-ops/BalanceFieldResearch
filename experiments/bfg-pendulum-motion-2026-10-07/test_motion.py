import math,unittest
import numpy as np
from scipy.linalg import expm
from motion import prepare,readout,one_step,event_clock,scalar,Y0,log_phi,stable_clock_step

class Controls(unittest.TestCase):
    def test_actual_ambient_state(self):
        from experiment import update
        rng=np.random.default_rng(20261007)
        for _ in range(100):
            theta,w=rng.normal(size=2)
            F,K=prepare(theta,w,20.,.1)
            result=update(np.array([[K]]),np.array([[F]]),np.ones((1,1)),np.array([[Y0]]),np.ones((1,1)))
            self.assertIsNone(result['terminal'])
            self.assertAlmostEqual(result['f'][0,0],F,places=12)
            self.assertAlmostEqual(result['k'][0,0],K,places=12)
            self.assertAlmostEqual(result['y'][0,0],scalar(Y0),places=12)
            expected=expm(np.array([[0.,1.],[-20.,-.1]])*.1)@np.array([theta,w])
            predicted=readout(result['f'][0,0],result['k'][0,0],event_clock(result['y'][0,0]),20.,.1,.1)
            np.testing.assert_allclose(predicted,expected,atol=1e-12)
    def test_reconstruction(self):
        F,K=prepare(np.array([.3,-.2]),np.array([-.4,.7]),20.,.1)
        theta,w=readout(F,K,0,20.,.1,.1)
        np.testing.assert_allclose(theta,[.3,-.2],atol=1e-14)
        np.testing.assert_allclose(w,[-.4,.7],atol=1e-14)
    def test_matrix_exponential(self):
        for a,b,dt in [(20.,.1,.1),(10.,0.,.2),(40.,.5,.05)]:
            pred=np.array(one_step(.3,-.4,a,b,dt))
            expected=expm(np.array([[0.,1.],[-a,-b]])*dt)@np.array([.3,-.4])
            np.testing.assert_allclose(pred,expected,atol=1e-13)
    def test_clock(self):
        y=Y0
        for event in range(7):
            self.assertAlmostEqual(event_clock(y),event,places=12)
            y=scalar(y)
    def test_stable_coordinate(self):
        x=log_phi(Y0)
        for _ in range(600):x=stable_clock_step(x)
        self.assertAlmostEqual(math.log2(-x/(-log_phi(Y0))),600.,places=12)
    def test_critical_gate(self):
        with self.assertRaises(ValueError):prepare(.1,.1,1.,2.)

if __name__=='__main__':unittest.main()
