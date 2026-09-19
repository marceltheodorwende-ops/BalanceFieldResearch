import unittest
import numpy as np
from bfg_lab.connection_model import operators, advance, seed


class ConnectionModelTests(unittest.TestCase):
    def test_analytic_operators(self):
        o=operators(seed())
        np.testing.assert_allclose(o['b_c'], [[0,-1],[-1,0]])
        np.testing.assert_allclose(o['y'], np.eye(2))
        np.testing.assert_allclose(o['r'], [[0,-1],[1,0]])

    def test_four_step_analytic_norm(self):
        s=seed()
        for k in range(1,5):
            s,r=advance(s)
            self.assertEqual(r['status'],'formation_admitted')
            self.assertEqual(r['next_dimension'],2)
            self.assertAlmostEqual(np.linalg.norm(s['d']),np.sqrt(2)/4**k)
            np.testing.assert_allclose(operators(s)['y'],np.eye(2),atol=1e-12)

    def test_zero_commutator_rejects_dual_support(self):
        s=seed(); s['coherence']=np.eye(2)
        n,r=advance(s)
        self.assertIsNone(n)
        self.assertIn('no_dual_support',r['gate']['reasons'])

    def test_terminal_and_bad_connection(self):
        self.assertEqual(advance(None),(None,{'status':'terminal'}))
        s=seed(); s['connection']=np.eye(2)
        with self.assertRaises(ValueError): operators(s)

    def test_input_not_mutated(self):
        s=seed(); old={k:v.copy() for k,v in s.items()}
        advance(s)
        for k in s: np.testing.assert_array_equal(s[k],old[k])

    def test_covariance_and_general_invariants(self):
        s=dict(connection=np.array([[0.,-1.,.3],[1.,0.,-.7],[-.3,.7,0.]]),
               coherence=np.diag([1.,2.,4.]),difference=np.diag([8.,9.,12.]),
               neutral=np.eye(3),d=np.array([1.,2.,1.]))
        n,r=advance(s)
        self.assertIsNotNone(n)
        self.assertGreater(r['g1_discrepancy'], 1)
        self.assertGreater(r['derivative_discrepancy'], 1)
        o=operators(n)
        np.testing.assert_allclose(o['r'].conj().T@o['r'],np.eye(len(n['d'])),atol=1e-12)
        self.assertGreaterEqual(np.linalg.eigvalsh(o['y']).min(),-1e-12)
        # Nontrivial basis permutation: compare basis-independent next spectra and norms.
        q=np.eye(3)[:,[2,0,1]]
        ss={k:q.T@v@q for k,v in s.items() if k!='d'}; ss['d']=q.T@s['d']
        nn,rr=advance(ss)
        np.testing.assert_allclose(np.linalg.eigvalsh(operators(nn)['y']),np.linalg.eigvalsh(o['y']),atol=1e-11)
        self.assertAlmostEqual(np.linalg.norm(nn['d']),np.linalg.norm(n['d']))
        self.assertAlmostEqual(r['g1_discrepancy'],rr['g1_discrepancy'])


if __name__=='__main__': unittest.main()
