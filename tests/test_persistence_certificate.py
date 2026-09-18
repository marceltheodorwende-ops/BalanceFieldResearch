import unittest
from fractions import Fraction as F
from bfg_lab.persistence_certificate import verify


class PersistenceCertificateTests(unittest.TestCase):
    def test_oblique_projector(self):
        x = verify([[1,1],[0,'1/2']], [[1,-2],[0,1]], 1, [[1]], [[1]])
        self.assertEqual(x['spectral_projector'], [[1,2],[0,0]])

    def test_defective_stable_block_is_allowed(self):
        x = verify([['1/2',1],[0,'1/2']], [[1,0],[0,1]], 0, [], [[2,0],[0,20]])
        self.assertEqual(x['spectral_projector'], [[0,0],[0,0]])

    def test_peripheral_rotation(self):
        x = verify([[0,-1],[1,0]], [[1,0],[0,1]], 2, [[1,0],[0,1]], [])
        self.assertEqual(x['persistent_dimension'], 2)

    def test_peripheral_jordan_rejected(self):
        with self.assertRaises(ValueError):
            verify([[1,1],[0,1]], [[1,0],[0,1]], 2, [[1,0],[0,1]], [])

    def test_exact_near_unit_stable(self):
        q=F(10**40-1,10**40)
        x=verify([[q]], [[1]], 0, [], [[1]])
        self.assertEqual(x['persistent_dimension'], 0)
        with self.assertRaises(ValueError):
            verify([[q]], [[1]], 1, [[1]], [])

    def test_ill_conditioned_basis(self):
        a=10**30
        x=verify([[1,-a],[0,0]], [[1,a],[0,1]], 1, [[1]], [[1]])
        self.assertEqual(x['spectral_projector'], [[1,-a],[0,0]])

    def test_bad_certificates(self):
        for r,s,p,m,n in [([[2]],[[1]],0,[],[[1]]),
                           ([[1]],[[0]],1,[[1]],[]),
                           ([[1]],[[1]],1,[[-1]],[]),
                           ([[1,1],[0,0]],[[1,0],[0,1]],1,[[1]],[[1]])]:
            with self.assertRaises(ValueError): verify(r,s,p,m,n)

    def test_float_and_bad_shapes_rejected(self):
        with self.assertRaises(ValueError): verify([[1.]],[[1]],1,[[1]],[])
        with self.assertRaises(ValueError): verify([[1]],[[1]],1,[],[])


if __name__ == '__main__': unittest.main()
