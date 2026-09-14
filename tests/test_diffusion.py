import unittest
import numpy as np
from bfg_lab.diffusion import heat_operator, adjacency, evaluate, run


class DiffusionTests(unittest.TestCase):
    def test_two_node_analytic_heat_kernel(self):
        r, lap=heat_operator(np.array([[0.,1.],[1.,0.]]),.2)
        decay=np.exp(-.4)
        np.testing.assert_allclose(r,[[.5*(1+decay),.5*(1-decay)],
                                    [.5*(1-decay),.5*(1+decay)]],atol=1e-13)
        np.testing.assert_allclose(lap,[[1,-1],[-1,1]])

    def test_identical_readouts_do_not_identify_recovery(self):
        x=np.array([1.,0.,0.,0.])
        a=evaluate(adjacency('path',4,1.),x)
        b=evaluate(adjacency('star',4,1.),x)
        np.testing.assert_allclose(a['loads'],b['loads'],atol=1e-12)
        np.testing.assert_allclose(a['weights'],b['weights'],atol=1e-12)
        self.assertAlmostEqual(a['gain'],b['gain'])
        self.assertGreater(abs(a['observed_ratio']-b['observed_ratio']),.01)

    def test_full_fixed_protocol(self):
        result=run()
        self.assertEqual(len(result['runs']),72)
        self.assertLess(result['max_prediction_error'],1e-10)
        self.assertLess(result['max_bound_violation'],1e-10)
        self.assertLess(result['max_mass_error'],1e-10)
        self.assertLess(result['max_load_error'],1e-10)

    def test_invalid_graph_and_constant_target(self):
        for a in (np.array([[0.,1.],[0.,0.]]),np.array([[0.,-1.],[-1.,0.]])):
            with self.assertRaises(ValueError):
                heat_operator(a,.2)
        with self.assertRaises(ValueError):
            evaluate(adjacency('path',4,1.),np.ones(4))

    def test_unresolved_timescale_is_not_extra_persistence(self):
        with self.assertRaises(ValueError):
            evaluate(adjacency('path',4,1.),np.array([1.,0.,0.,0.]),dt=1e-12)
