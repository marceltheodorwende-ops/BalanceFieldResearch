import unittest
import numpy as np
from bfg_lab.gram import rebuild


class GramTests(unittest.TestCase):
    def test_rectangular_known_result(self):
        r = rebuild([[1, 0], [0, 2], [0, 0]], np.diag([4, 9, 0]), [[1], [2]])
        np.testing.assert_allclose(r['h'], np.diag([4, 36]))
        np.testing.assert_allclose(r['y'], [[148]])
        np.testing.assert_allclose(r['c'], [[1/149]])

    def test_complex_adjoint(self):
        r = rebuild([[1j]], [[2]], [[3j]])
        np.testing.assert_allclose(r['y'], [[18]])

    def test_zero_weight_is_valid(self):
        r = rebuild(np.eye(2), np.zeros((2, 2)), np.eye(2))
        np.testing.assert_allclose(r['c'], np.eye(2))
        np.testing.assert_allclose(r['b'], 0)

    def test_unitary_carrier_change(self):
        b = np.array([[1, 2j], [3, 1]])
        w = np.diag([2, 3])
        l = np.array([[1, 1j], [0, 2]])
        u = np.array([[1, 1j], [1j, 1]])/np.sqrt(2)
        r, s = rebuild(b, w, l), rebuild(b, w, l @ u)
        for key in ('y', 'g', 'c', 'b', 'z'):
            np.testing.assert_allclose(s[key], u.conj().T @ r[key] @ u, atol=1e-12)

    def test_rejects_invalid_weight(self):
        for w in (np.diag([1, -1]), [[1, 1], [0, 1]], [[np.nan, 0], [0, 1]]):
            with self.assertRaises(ValueError):
                rebuild(np.eye(2), w, np.eye(2))

    def test_rejects_domains_and_tolerance(self):
        with self.assertRaises(ValueError):
            rebuild(np.ones((2, 3)), np.eye(2), np.eye(2))
        with self.assertRaises(ValueError):
            rebuild([[1]], [[1]], [[1]], tol=-1)

    def test_roundoff_policy_is_visible(self):
        r = rebuild([[1]], [[-1e-12]], [[1]])
        self.assertEqual(r['clipped_weight_eigenvalues'], 1)
        np.testing.assert_allclose(r['y'], 0)


if __name__ == '__main__':
    unittest.main()
