import unittest
import numpy as np
from bfg_lab.formation import transport_capacities, formation_gate, prepare_candidate


class FormationTests(unittest.TestCase):
    def test_support_compression_excludes_artificial_zero_modes(self):
        j = np.zeros((4, 2)); j[0, 0] = 1
        result = transport_capacities(j, np.diag([3., 9.]), np.eye(2), np.eye(2))
        self.assertEqual(result['formation'].shape, (1, 1))
        np.testing.assert_allclose(result['formation'], [[-1.]])
        self.assertTrue(formation_gate(result['formation'], [1, 1], .5)['passed'])

    def test_isometric_mixed_transport(self):
        j = np.vstack([np.eye(2), np.eye(2)])/np.sqrt(2)
        result = transport_capacities(j, np.diag([4., 1.]), np.eye(2), np.eye(2))
        np.testing.assert_allclose(np.linalg.eigvalsh(result['formation']), [-2., 1.])
        for key in ['difference','coherence','neutral']:
            self.assertGreaterEqual(np.linalg.eigvalsh(result[key]).min(), 0.)

    def test_gate_failure_reasons(self):
        cases = [(np.eye(2), [1,1], .5, 'nonnegative_minimum'),
                 (-np.eye(2), [1,1], .5, 'nonisolated_minimum'),
                 (np.diag([-1.,2.]), [0,1], .5, 'no_dual_support'),
                 (np.diag([-1.,2.]), [1,1], 0., 'no_persistence_gap'),
                 (np.diag([-1e-12,2.]), [1,1], .5, 'minimum_within_tolerance')]
        for k, loads, gap, reason in cases:
            result = formation_gate(k, loads, gap)
            self.assertFalse(result['passed'])
            self.assertIn(reason, result['reasons'])

    def test_invalid_input_is_not_terminal_physics(self):
        with self.assertRaises(ValueError):
            transport_capacities(np.ones((4,2)), np.eye(2), np.eye(2), np.eye(2))
        with self.assertRaises(ValueError):
            formation_gate(np.eye(2), [np.nan,1], .5)

    def test_end_to_end_pass_and_reject(self):
        args = (np.eye(2), np.array([1.,1.]), np.diag([1.,.5]))
        passed = prepare_candidate(*args, 3*np.eye(2), np.eye(2), np.eye(2))
        self.assertEqual(passed['status'], 'formation_admitted')
        self.assertEqual(passed['transport']['formation'].shape, (1,1))
        rejected = prepare_candidate(*args, np.eye(2), np.eye(2), np.eye(2))
        self.assertEqual(rejected['status'], 'formation_rejected')
        self.assertIn('nonnegative_minimum', rejected['gate']['reasons'])

    def test_no_witness_and_full_witness(self):
        for r, expected in [(np.eye(2)*.5, 'no_dual_support'), (np.eye(2), 'nonisolated_minimum')]:
            result = prepare_candidate(np.eye(2), np.ones(2), r, 3*np.eye(2), np.eye(2), np.eye(2))
            self.assertEqual(result['status'], 'formation_rejected')
            self.assertIn(expected, result['gate']['reasons'])

    def test_unitary_change_of_coordinates(self):
        rng = np.random.default_rng(42)
        q,_ = np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
        j = np.vstack([np.eye(3),np.eye(3)])/np.sqrt(2)
        d=np.diag([5.,3.,1.]); c=np.eye(3)
        a=transport_capacities(j,d,c,c)
        b=transport_capacities(j,q@d@q.conj().T,c,c)
        np.testing.assert_allclose(np.linalg.eigvalsh(a['formation']),np.linalg.eigvalsh(b['formation']),atol=1e-12)
