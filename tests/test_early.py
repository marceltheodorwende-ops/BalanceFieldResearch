import unittest
import numpy as np
from bfg_lab.early import bounds, run


class EarlyTests(unittest.TestCase):
    def test_single_mode_and_mixture(self):
        single=.8**5
        lo,hi=bounds(single,5,20)
        self.assertAlmostEqual(lo,.8**20)
        self.assertGreaterEqual(hi,lo)
        q=np.sqrt((.8**2+.4**2)/2)
        target=np.sqrt((.8**4+.4**4)/2)
        lo,hi=bounds(q,1,2)
        self.assertLess(lo,target)
        self.assertLess(target,hi)
        # The single-mode contraction q has the same first observation,
        # but second observation q^2 differs from the mixture.
        self.assertGreater(target-q*q,.05)

    def test_noise_enclosure_and_endpoints(self):
        self.assertEqual(bounds(0,5,20),(0.,0.))
        self.assertEqual(bounds(1,5,20),(1.,1.))
        for e in (-.01,0,.01):
            lo,hi=bounds(.6+e,5,20,error=.01)
            self.assertLessEqual(lo,.6**4+1e-15)
            self.assertGreaterEqual(hi,.6-1e-15)
        self.assertEqual(bounds(-.005,5,20,error=.01)[0],0.)

    def test_invalid_assumptions_are_not_silently_clipped(self):
        for args in [(1.1,5,20,0),(np.nan,5,20,0),(.5,0,20,0),(.5,5,4,0),(.5,5,20,-1)]:
            with self.assertRaises(ValueError):
                bounds(args[0],args[1],args[2],error=args[3])

    def test_new_network_protocol(self):
        result=run()
        self.assertEqual(len(result['runs']),80)
        self.assertLess(result['max_violation'],1e-10)
        self.assertLess(result['max_noisy_violation'],1e-10)
        self.assertLess(result['mean_width'],1)
