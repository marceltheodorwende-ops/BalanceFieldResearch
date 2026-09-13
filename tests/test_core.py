import unittest
import numpy as np
from bfg_lab.core import neutral, persistent_basis, metric_projector, split


class CoreTests(unittest.TestCase):
    def test_known_diagonal_responses(self):
        c, b, z = neutral(np.diag([0., 1., 3.]))
        np.testing.assert_allclose(np.diag(c), [1, .5, .25])
        np.testing.assert_allclose(np.diag(b), [0, .5, .75])
        np.testing.assert_allclose(np.diag(z), [1, 0, -.5])

    def test_persistence_counterexample(self):
        # Both vectors meet the paper's nondecay test, but their span includes decay.
        r = np.diag([1., .5])
        v1, v2 = np.array([1., 0.]), np.array([1., 1.])
        self.assertEqual(np.linalg.matrix_rank(np.stack([v1, v2])), 2)
        self.assertGreater(np.linalg.norm(np.linalg.matrix_power(r, 50) @ v2), .9)
        self.assertLess(np.linalg.norm(np.linalg.matrix_power(r, 50) @ (v2-v1)), 1e-12)
        w = persistent_basis(r)
        np.testing.assert_allclose(w @ w.conj().T, np.diag([1., 0.]))

    def test_metric_projection(self):
        g = np.array([[2., .4], [.4, 1.]])
        w = np.array([[1.], [1.]])
        p = metric_projector(w, g)
        np.testing.assert_allclose(p @ p, p)
        np.testing.assert_allclose(p.conj().T @ g, g @ p)
        np.testing.assert_allclose(metric_projector(w * 3, g), p)

    def test_zero_support(self):
        self.assertEqual(split(np.zeros((2, 2)), np.ones(2), np.eye(2))["status"], "no_dual_support")
        self.assertEqual(persistent_basis(np.eye(2)*.9).shape, (2, 0))

    def test_invalid_inputs(self):
        for y in [np.diag([-1., 1.]), np.array([[1., 2.], [0., 1.]])]:
            with self.assertRaises(ValueError):
                neutral(y)
        for r in [np.eye(2)*1.1, np.array([[1., 1.], [0., 1.]])]:
            with self.assertRaises(ValueError):
                persistent_basis(r)

    def test_seeded_complex_invariants(self):
        rng = np.random.default_rng(20260913)
        for n in range(2, 9):
            for _ in range(15):
                a = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
                y = a.conj().T @ a / n
                d = rng.normal(size=n) + 1j*rng.normal(size=n)
                w = (rng.normal(size=(n, max(1,n//2))) +
                     1j*rng.normal(size=(n, max(1,n//2))))
                result = split(y, d, w)
                self.assertEqual(result["status"], "ok")
                np.testing.assert_allclose(result["analysis"], result["compact"], atol=1e-12)
                self.assertLessEqual(result["gain"], 1/np.sqrt(2) + 1e-12)
                lk, lu = result["loads"]
                wk, wu = result["weights"]
                self.assertAlmostEqual(wk*lk, wu*lu)
                j = result["polar"]
                support = j.conj().T @ j
                np.testing.assert_allclose(support @ support, support, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
