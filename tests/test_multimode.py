import unittest
import numpy as np
from bfg_lab.minimal import advance, simulate, multimode_seed, spectral_transport


class MultimodeTests(unittest.TestCase):
    def test_analytic_two_modes_survive(self):
        result = simulate(multimode_seed(), steps=12, transport_rule='negative_spectrum')
        self.assertEqual(result['status'], 'step_limit')
        self.assertEqual([h['persistent_rank_next'] for h in result['history']], [2]*12)
        for h in result['history']:
            np.testing.assert_allclose(h['gate']['eigenvalues'], [-2., -1.], atol=1e-12)

    def test_analytic_depletion_rank_loss(self):
        result = simulate(multimode_seed(), retention=.8, transport_rule='negative_spectrum')
        self.assertEqual(result['transitions'], 4)
        self.assertEqual([h['persistent_rank_next'] for h in result['history'][:-1]], [2,1,1,0])
        self.assertEqual(result['history'][-1]['gate']['reasons'], ['no_dual_support'])
        np.testing.assert_allclose([h['gate']['minimum'] for h in result['history'][:-1]], [-2,-1.2,-.56,-.048], atol=1e-12)

    def test_complex_coordinate_invariance(self):
        s = multimode_seed()
        reference = simulate(s, retention=.8, transport_rule='negative_spectrum')
        rng = np.random.default_rng(913)
        for _ in range(12):
            q,_ = np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
            rotated = {k:q@v if k=='d' else q@v@q.conj().T for k,v in s.items()}
            result = simulate(rotated, retention=.8, transport_rule='negative_spectrum')
            self.assertEqual(result['transitions'], reference['transitions'])
            for a,b in zip(result['history'][:-1], reference['history'][:-1]):
                self.assertEqual(a['persistent_rank_next'], b['persistent_rank_next'])
                np.testing.assert_allclose(a['gate']['eigenvalues'], b['gate']['eigenvalues'], atol=1e-11)

    def test_threshold_sensitivity_is_explicit(self):
        k = np.diag([-1., -5e-9, 0., 1.])
        for tol, expected in [(1e-12,2),(1e-10,2),(1e-8,1)]:
            r, audit = spectral_transport(k, rho=.5, tol=tol)
            self.assertEqual(audit['persistent_rank_next'], expected)
            np.testing.assert_allclose(r.conj().T@r, r@r.conj().T)
            np.testing.assert_allclose(np.linalg.eigvalsh(r), [.5]*(4-expected)+[1.]*expected)
        with self.assertRaises(ValueError):
            spectral_transport(k, tol=0)

    def test_initial_perturbations(self):
        for eps in [-1e-6,1e-6]:
            s=multimode_seed(); s['difference'] *= 1+eps; s['d'][0] += eps
            self.assertEqual(simulate(s, retention=.8, transport_rule='negative_spectrum')['transitions'],4)

    def test_invalid_rule(self):
        with self.assertRaises(ValueError):
            advance(multimode_seed(), transport_rule='unknown')

    def test_noncommuting_load_and_capacities(self):
        s=multimode_seed()
        s['y']=np.array([[2.,.2,0.],[.2,1.,.1],[0.,.1,1.]])
        s['coherence']=np.array([[1.,.1,0.],[.1,1.,0.],[0.,0.,1.]])
        for _ in range(4):
            nxt, report=advance(s, transport_rule='negative_spectrum')
            self.assertIsNotNone(nxt)
            # The two split branches jointly span three directions here.
            # Lifted K is negative definite on their support in W direct-sum W.
            self.assertEqual(report['persistent_rank_next'],3)
            for key in ('y','difference','coherence','neutral'):
                np.testing.assert_allclose(nxt[key],nxt[key].conj().T,atol=1e-12)
                self.assertGreaterEqual(np.linalg.eigvalsh(nxt[key]).min(),-1e-12)
            np.testing.assert_allclose(np.linalg.eigvalsh(nxt['r']),[1.,1.,1.],atol=1e-12)
            s=nxt
