import json
from pathlib import Path
import unittest
import numpy as np
from finite_closure import State, advance, persistent_projectors, NumericalAmbiguity, gram_factors


def seed():
    d = np.array([1., 1.])/np.sqrt(2)
    return State(np.outer(d, d), np.array([[-2., .5], [.5, 1.]]),
                 np.diag([.3, 1.7]), np.eye(2))


class FiniteClosureTests(unittest.TestCase):
    def test_exact_scalar_update(self):
        s = State(np.ones((1, 1)), -np.ones((1, 1)), np.ones((1, 1)), np.ones((1, 1)))
        out = advance(s).state
        np.testing.assert_allclose(out.Y, [[.25]], atol=1e-14)
        np.testing.assert_allclose(out.K, [[-1]], atol=1e-14)
        np.testing.assert_allclose(out.rho, [[1]], atol=1e-14)
        np.testing.assert_allclose(out.R, [[np.exp(-1j)]], atol=1e-14)

    def test_nonnormal_input_completes_one_step(self):
        s = State(np.ones((2, 2)), np.diag([-2., 1.]), np.eye(2),
                  np.array([[1., -.5], [0., .5]]))
        out = advance(s)
        self.assertIsNotNone(out.state)
        self.assertEqual(out.state.K.shape, (1, 1))
        self.assertGreater(out.diagnostics['projector_difference'], .5)

    def test_growing_recursion_rejected(self):
        s = seed(); s.R = np.diag([1., 2.])
        with self.assertRaisesRegex(ValueError, 'growing'):
            advance(s)

    def test_peripheral_jordan_rejected(self):
        with self.assertRaises(NumericalAmbiguity):
            persistent_projectors(np.array([[1., 1.], [0., 1.]], complex), np.eye(2))

    def test_stable_jordan_is_allowed(self):
        r = np.array([[1., 0., 0.], [0., .5, 1.], [0., 0., .5]], complex)
        e, p, rank = persistent_projectors(r, np.eye(3))
        self.assertEqual(rank, 1)
        np.testing.assert_allclose(e, np.diag([1, 0, 0]), atol=1e-12)
        np.testing.assert_allclose(e, p, atol=1e-12)

    def test_nonnormal_spectral_and_metric_projectors(self):
        r = np.array([[1., -.5], [0., .5]], complex)
        e, p, rank = persistent_projectors(r, np.eye(2))
        self.assertEqual(rank, 1)
        np.testing.assert_allclose(e, [[1, -1], [0, 0]], atol=1e-12)
        np.testing.assert_allclose(p, [[1, 0], [0, 0]], atol=1e-12)
        self.assertGreater(np.linalg.norm(p@r-r@p), .1)

    def test_near_unit_is_inconclusive(self):
        with self.assertRaises(NumericalAmbiguity):
            persistent_projectors(np.diag([1., 1.-5e-9]).astype(complex), np.eye(2))

    def test_empty_support_and_absorbing_terminal(self):
        s = seed(); s.R = .5*np.eye(2)
        self.assertIsNone(advance(s).state)
        self.assertIsNone(advance(None).state)

    def test_nonhermitian_input_not_silently_repaired(self):
        s = seed(); s.K[0, 1] += .1
        with self.assertRaisesRegex(ValueError, 'Hermitian'):
            advance(s)

    def test_degenerate_formation_inconclusive(self):
        s = seed(); s.K = -np.eye(2)
        with self.assertRaises(NumericalAmbiguity):
            advance(s)

    def test_positive_formation_terminates(self):
        s = seed(); s.K = np.eye(2)
        self.assertIsNone(advance(s).state)

    def test_profile_phase_is_absent(self):
        s = seed(); d = np.array([1., 1.])/np.sqrt(2)
        d = np.exp(.731j)*d
        t = State(np.outer(d, d.conj()), s.K, s.Y, s.R)
        a, b = advance(s).state, advance(t).state
        np.testing.assert_allclose(np.linalg.eigvalsh(a.K), np.linalg.eigvalsh(b.K), atol=1e-12)
        np.testing.assert_allclose(np.trace(a.rho), np.trace(b.rho), atol=1e-12)

    def test_repeated_steps_preserve_category_or_report_numerical_ambiguity(self):
        s = seed()
        completed = 0
        for _ in range(20):
            try:
                out = advance(s)
            except NumericalAmbiguity as error:
                self.assertGreaterEqual(completed, 3)
                self.assertIn('near zero', str(error))
                return
            self.assertIsNotNone(out.state); s = out.state; completed += 1
            self.assertGreater(np.linalg.eigvalsh(s.Y).min(), 0)
            np.testing.assert_allclose(s.R.conj().T@s.R, np.eye(len(s.R)), atol=1e-11)
            self.assertEqual(np.count_nonzero(np.linalg.eigvalsh(s.rho)>1e-9), 1)
            self.assertFalse(out.diagnostics['real_polarity_claimed'])

    def test_declared_factor_gauge_reconstructs_the_load(self):
        s = advance(seed()).state; f = gram_factors(s.Y)
        np.testing.assert_allclose(f['B_C'], f['D_K']@f['F'], atol=1e-12)
        h = f['B_C'].conj().T@f['W_N']@f['B_C']
        np.testing.assert_allclose(f['L_C'].conj().T@h@f['L_C'], s.Y, atol=1e-12)

    def test_unitary_coordinate_equivalence(self):
        rng = np.random.default_rng(20260923)
        for _ in range(24):
            s = seed(); q, _ = np.linalg.qr(rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))
            t = State(*(q@a@q.conj().T for a in (s.rho, s.K, s.Y, s.R)))
            for _ in range(3):
                x, y = advance(s), advance(t)
                self.assertIsNotNone(x.state); self.assertIsNotNone(y.state)
                s, t = x.state, y.state
                np.testing.assert_allclose(np.linalg.eigvalsh(s.K), np.linalg.eigvalsh(t.K), atol=1e-10)
                np.testing.assert_allclose(np.linalg.eigvalsh(s.Y), np.linalg.eigvalsh(t.Y), atol=1e-10)
                self.assertAlmostEqual(x.diagnostics['alpha'], y.diagnostics['alpha'], places=10)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FiniteClosureTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    payload = {'tests_run': result.testsRun, 'failures': len(result.failures),
               'errors': len(result.errors), 'passed': result.wasSuccessful(),
               'scope': 'Finite conditional model; no empirical or uniquely forced BFG closure claim'}
    (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    raise SystemExit(0 if result.wasSuccessful() else 1)
