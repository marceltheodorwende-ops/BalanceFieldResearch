import unittest
import numpy as np
from bfg_lab.minimal import seed, simulate, advance


class MinimalTests(unittest.TestCase):
    def test_analytic_stop(self):
        result = simulate(seed(), steps=8, retention=.8)
        self.assertEqual(result['status'], 'formation_rejected')
        self.assertEqual(result['transitions'], 2)
        np.testing.assert_allclose([r['gate']['minimum'] for r in result['history']], [-1, -.4, .08], atol=1e-12)

    def test_budget_is_not_proof_of_infinite_survival(self):
        result = simulate(seed(), steps=12)
        self.assertEqual(result['status'], 'step_limit')
        self.assertEqual(result['transitions'], 12)

    def test_next_state_invariants_and_no_mutation(self):
        state = seed()
        original = {k:v.copy() for k,v in state.items()}
        nxt, report = advance(state, retention=.8)
        self.assertTrue(report['gate']['passed'])
        self.assertEqual(nxt['y'].shape, (1,1))
        self.assertAlmostEqual(np.linalg.norm(nxt['d']), 1)
        for key in ('y','difference','coherence','neutral'):
            self.assertGreaterEqual(np.linalg.eigvalsh(nxt[key]).min(), -1e-12)
        np.testing.assert_allclose(nxt['r'].conj().T@nxt['r'], nxt['r']@nxt['r'].conj().T)
        for key in state:
            np.testing.assert_array_equal(state[key], original[key])

    def test_perturbations_away_from_boundary(self):
        for epsilon in (-1e-6, 0, 1e-6):
            s = seed()
            s['difference'] *= 1+epsilon
            s['d'][0] += epsilon
            self.assertEqual(simulate(s, steps=8, retention=.8)['transitions'], 2)

    def test_invalid_parameters(self):
        for retention in (-.1, 1.1, np.nan):
            with self.assertRaises(ValueError):
                simulate(seed(), retention=retention)
        with self.assertRaises(ValueError):
            simulate(seed(), steps=-1)
        with self.assertRaises(ValueError):
            advance(seed(), rho=1)
