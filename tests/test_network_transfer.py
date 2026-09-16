import unittest
from fractions import Fraction as F
from bfg_lab.network_transfer import catalogue


class TransferInputsTests(unittest.TestCase):
    def test_closed_forms_against_independent_matrix_evolution(self):
        import numpy as np
        from bfg_lab.diffusion import heat_operator
        for c in catalogue():
            if c['condition']!='intact': continue
            p=c['input']; n=len(p['initial'])
            a=np.array([[float(c['weight']) if v else 0 for v in row] for row in p['weight_lower']])
            for k,t in enumerate(p['times'][1:],1):
                op,_=heat_operator(a,float(t)); predicted=op@np.array(p['initial'],dtype=float)
                for j,i in enumerate(p['sensors']):
                    actual=float(F(p['samples'][k][j])-F('1e-7')*(1 if (k+i)%2 else -1))
                    self.assertAlmostEqual(actual,predicted[i],places=13)

    def test_fixed_catalogue_and_initial_readings(self):
        cases=catalogue()
        self.assertEqual(len(cases),20)
        self.assertEqual(len({c['id'] for c in cases}),20)
        for c in cases:
            p=c['input']
            for j,i in enumerate(p['sensors']):
                self.assertLess(abs(F(p['samples'][0][j])-F(p['initial'][i])),F(p['sensor_error']))

    def test_noise_removed_modal_mass_is_preserved(self):
        for c in catalogue():
            p=c['input']
            if len(p['sensors'])!=len(p['initial']): continue
            for k,row in enumerate(p['samples']):
                total=sum(F(v)-F('1e-7')*(1 if (k+i)%2 else -1) for i,v in enumerate(row))
                self.assertLess(abs(total-sum(map(F,p['initial']))),F('1e-75'))
