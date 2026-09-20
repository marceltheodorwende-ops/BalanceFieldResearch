import unittest
from fractions import Fraction as F
import numpy as np

from bfg_lab.ctc_sa import State, advance, operators, seed, projectors_from_certificate


class CTCSATests(unittest.TestCase):
    def test_exact_oblique_and_metric_projectors(self):
        result = projectors_from_certificate(
            [[1, '-1/2'], [0, '1/2']], [[1, 1], [0, 1]], 1,
            [[1]], [[1]], [[1, 0], [0, 1]])
        self.assertEqual(result['spectral_projector'], [[F(1), F(-1)], [F(0), F(0)]])
        self.assertEqual(result['metric_projector'], [[F(1), F(0)], [F(0), F(0)]])

    def test_metric_changes_projection_not_space(self):
        result = projectors_from_certificate(
            [[1, 0], [0, '1/2']], [[1, 0], [0, 1]], 1,
            [[1]], [[1]], [[2, 1], [1, 2]])
        self.assertEqual(result['metric_projector'], [[F(1), F(1, 2)], [F(0), F(0)]])

    def test_jordan_certificate_rejected(self):
        with self.assertRaises(ValueError):
            projectors_from_certificate([[1, 1], [0, 1]], [[1, 0], [0, 1]], 2,
                                        [[1, 0], [0, 1]], [], [[1, 0], [0, 1]])

    def test_no_peripheral_space_rejected(self):
        with self.assertRaises(ValueError):
            projectors_from_certificate([['1/2']], [[1]], 0, [], [[1]], [[1]])

    def test_empty_stable_space_allowed(self):
        r = projectors_from_certificate([[1]], [[1]], 1, [[1]], [], [[2]])
        self.assertEqual(r['metric_projector'], [[F(1)]])

    def test_indefinite_metric_rejected(self):
        with self.assertRaises(ValueError):
            projectors_from_certificate([[1]], [[1]], 1, [[1]], [], [[-1]])

    def test_documented_history_against_exact_fractions(self):
        s = seed()
        expected = [(F(1, 5), F(5, 6)), (F(25, 624), F(625, 23364)),
                    (F(324480000, 164268811201), F(3515200000000, 69326858847152401))]
        for dimension, (eta, energy) in zip([4, 3, 2], expected):
            s, result = advance(s)
            self.assertEqual(result['status'], 'advanced')
            self.assertEqual(len(s.d), dimension)
            self.assertAlmostEqual(s.eta, float(eta), places=13)
            self.assertAlmostEqual(result['energy_next'], float(energy), places=13)
            self.assertLess(result['energy_ratio'], .2)
        self.assertEqual(operators(s)['r'], 0)
        s, result = advance(s)
        self.assertIsNone(s)
        self.assertEqual(result['reason'], 'ctc_dimension_floor')
        self.assertEqual(advance(None), (None, {'status': 'terminal', 'reason': 'absorbing'}))

    def test_new_gram_not_inherited(self):
        s, result = advance(seed())
        np.testing.assert_allclose(operators(s)['y'], np.eye(4)/5)
        self.assertAlmostEqual(result['gram_inheritance_defect'], .8)

    def test_general_eta_and_nonuniform_vector(self):
        s = seed(4)
        s = State(s.difference, s.coherence, s.neutral, np.array([1., 2., 3., 4.]), 2.)
        n, report = advance(s)
        self.assertAlmostEqual(n.eta, float(F(56, 675)))
        self.assertLess(report['energy_ratio'], .2)

    def test_unitary_covariance(self):
        s = seed(3)
        q = np.array([[1, 1j, 0], [1j, 1, 0], [0, 0, np.sqrt(2)]])/np.sqrt(2)
        changed = State(*(q @ a @ q.conj().T for a in (s.difference, s.coherence, s.neutral)),
                        q @ s.d, s.eta)
        n, r = advance(s)
        nn, rr = advance(changed)
        self.assertAlmostEqual(n.eta, nn.eta)
        self.assertAlmostEqual(r['energy_next'], rr['energy_next'])
        np.testing.assert_allclose(np.linalg.eigvalsh(n.coherence), np.linalg.eigvalsh(nn.coherence))

    def test_invalid_class_cases(self):
        s = seed(3)
        cases = [State(s.difference,s.coherence,s.neutral,np.array([1.,0.,1.]),1.),
                 State(s.difference,s.coherence,s.neutral,s.d,0.),
                 State(s.difference,s.coherence,s.neutral,s.d,float('nan')),
                 State(np.diag([3.,1.,2.]),s.coherence,s.neutral,s.d,1.),
                 State(s.difference,np.diag([0.,2.,3.]),s.neutral,s.d,1.),
                 State(s.difference,np.eye(2),s.neutral,s.d,1.),
                 State(np.array([[3.,1.,0.],[0.,1.,0.],[0.,0.,1.]]),s.coherence,s.neutral,s.d,1.)]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                advance(case)

    def test_noncommuting_capacities_rejected(self):
        s=seed(3)
        neutral=s.neutral.copy(); neutral[0,1]=neutral[1,0]=.1
        with self.assertRaises(ValueError):
            advance(State(s.difference,s.coherence,neutral,s.d,1.))

    def test_input_unchanged(self):
        s=seed(); old=[a.copy() for a in (s.difference,s.coherence,s.neutral,s.d)]
        advance(s)
        for a,b in zip(old,(s.difference,s.coherence,s.neutral,s.d)):
            np.testing.assert_array_equal(a,b)

    def test_unresolvable_eta_is_not_mathematical_terminal(self):
        s=seed(3)
        with self.assertRaises(ValueError):
            advance(State(s.difference,s.coherence,s.neutral,s.d,1e-250))


if __name__ == '__main__':
    unittest.main()
