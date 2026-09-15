import unittest
import numpy as np
from bfg_lab.monitor import assess, experiment


class MonitorTests(unittest.TestCase):
    def test_partial_data_never_becomes_global_forecast(self):
        result=assess(np.ones((6,2)),8,model_assumed=True)
        self.assertEqual(result['status'],'insufficient_coverage')
        self.assertIsNone(result['forecast'])

    def test_assumption_is_explicit(self):
        data=np.array([[1.,0.],[.8,.2],[.7,.3]])
        self.assertEqual(assess(data,2)['status'],'model_unverified')
        self.assertIsNotNone(assess(data,2,model_assumed=True)['forecast'])

    def test_mass_forcing_detected_and_noise_respected(self):
        data=np.array([[1.,0.],[1.1,.1],[1.2,.2]])
        result=assess(data,2,model_assumed=True)
        self.assertEqual(result['status'],'assumption_violation')
        self.assertIn('mass_changed',result['reasons'])
        self.assertIsNone(result['forecast'])
        self.assertNotIn('mass_changed',assess(data,2,sample_error=.1)['reasons'])

    def test_noncontraction_and_acceleration(self):
        for norms,reason in [([1.,1.1,1.2],'disagreement_increased'),
                             ([1.,.9,.4],'decay_not_log_convex')]:
            data=np.array([[v,-v] for v in norms])
            self.assertIn(reason,assess(data,2,model_assumed=True)['reasons'])

    def test_scenarios_and_undetectable_change(self):
        rows=experiment()
        self.assertEqual(len(rows),8)
        by={(r['scenario'],r['coverage']):r for r in rows}
        self.assertEqual(by['steady','full']['after']['status'],'conditional_forecast')
        self.assertEqual(by['forcing','full']['after']['status'],'assumption_violation')
        self.assertEqual(by['speedup','full']['after']['status'],'assumption_violation')
        self.assertFalse(by['speedup','full']['earlier_interval_contains_target'])
        self.assertEqual(by['cut','full']['after']['status'],'conditional_forecast')
        # A cut need not violate monotonicity, conservation or log convexity.
        for r in rows:
            if r['coverage']=='partial':
                self.assertIsNone(r['after']['forecast'])

    def test_invalid_input_and_zero_signal(self):
        for data in (np.ones((1,2)),np.array([[0.,np.nan],[1.,0.]])):
            with self.assertRaises(ValueError):
                assess(data,2)
        self.assertEqual(assess(np.ones((3,2)),2,model_assumed=True)['status'],'unresolved_initial_signal')
