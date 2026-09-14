import unittest
import numpy as np
from bfg_lab.minimal import advance, multimode_seed, simulate
from bfg_lab.comparison import run


class ComparisonTests(unittest.TestCase):
    def test_carried_diagonal_transport(self):
        nxt, report=advance(multimode_seed(), transport_rule='carried')
        np.testing.assert_allclose(nxt['r'],np.eye(2),atol=1e-12)
        self.assertEqual(report['persistent_rank_next'],2)
        result=simulate(multimode_seed(), retention=.8, transport_rule='carried')
        self.assertEqual(result['transitions'],4)
        self.assertIn('nonnegative_minimum',result['history'][-1]['gate']['reasons'])

    def test_paired_reproducible_complete_design(self):
        a=run(); b=run()
        self.assertEqual(a,b)
        self.assertEqual(len(a['runs']),72)
        for i in range(0,72,3):
            group=a['runs'][i:i+3]
            self.assertEqual(len({r['case'] for r in group}),1)
            self.assertEqual(len({r['input_hash'] for r in group}),1)
            self.assertEqual({r['rule'] for r in group},{'packet','negative_spectrum','carried'})

    def test_carried_coordinate_invariance_and_domain(self):
        s=multimode_seed()
        rng=np.random.default_rng(41)
        q,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
        rotated={k:q@v if k=='d' else q@v@q.conj().T for k,v in s.items()}
        a=simulate(s,retention=.8,transport_rule='carried')
        b=simulate(rotated,retention=.8,transport_rule='carried')
        self.assertEqual(a['transitions'],b['transitions'])
        for x,y in zip(a['history'],b['history']):
            np.testing.assert_allclose(x['gate']['eigenvalues'],y['gate']['eigenvalues'],atol=1e-11)
        s['r']=np.diag([1.,1j,.5])
        with self.assertRaises(ValueError):
            advance(s,transport_rule='carried')
