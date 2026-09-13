import unittest
import numpy as np
from bfg_lab.__main__ import experiment


class NetworkTests(unittest.TestCase):
    def test_conservation_and_partition(self):
        for scenario in ('impulse','edge_failure','coupling_drift'):
            rows = experiment(scenario)
            self.assertEqual(len(rows), 81)
            for row in rows:
                self.assertAlmostEqual(sum(row['state']), 1.)
                self.assertAlmostEqual(row['retention']+row['complement'], 1.)
                self.assertEqual(row['witness_rank'], 1)
                self.assertEqual(row['status'], 'ok')
                self.assertLessEqual(row['dual_gain'], 1/np.sqrt(2))
            self.assertLess(rows[-1]['disagreement'], rows[0]['disagreement'])

    def test_failure_timing(self):
        baseline, failure = experiment('impulse'), experiment('edge_failure')
        self.assertEqual(baseline[:20], failure[:20])
        self.assertLess(failure[20]['spectral_gap'], baseline[20]['spectral_gap'])
        self.assertGreater(failure[-1]['disagreement'], baseline[-1]['disagreement'])
