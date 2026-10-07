import unittest
import numpy as np
from energy_input import f,inverse,feedback
class Controls(unittest.TestCase):
    def test_inverse_reference(self):
        # exact rational control: f(1/2)=8/45
        self.assertAlmostEqual(inverse(8/45),.5,places=12)
    def test_causal_feedback_identity(self):
        for y in [.0001,.01,.1,.125]:
            for r in [.8,.95,1.]:
                d=feedback(y,r);self.assertGreater(d,0);self.assertLess(d,.75)
                self.assertAlmostEqual(f(y+d),r*y,places=12)
    def test_log_scalar_positive(self):
        logy=np.log(.1)
        for _ in range(64):logy=np.log(2)+2*logy-2*np.logaddexp(0,logy)-np.logaddexp(0,2*logy)
        self.assertTrue(np.isfinite(logy));self.assertLess(logy,-1000)
    def test_inverse_gate(self):
        for y in [0,.25,.3]:
            with self.assertRaises(ValueError):inverse(y)
if __name__=='__main__':unittest.main()
