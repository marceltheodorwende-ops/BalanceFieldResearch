import unittest
from fractions import Fraction as F
from bfg_lab.certified_interior import assess_interior
from bfg_lab.network_transfer import catalogue


class InteriorTests(unittest.TestCase):
    def test_interior_network_witness(self):
        p=next(c['input'] for c in catalogue() if c['id']=='path3_3s_.8_intact')
        r=assess_interior(**p,max_boxes=1,max_candidates=0)
        self.assertEqual(r['status'],'compatible_witness')
        self.assertEqual(r['witness_source'],'numerical_proposal_exact_certificate')
        for i,row in enumerate(r['witness']['weights']):
            for j,w in enumerate(row):
                self.assertLessEqual(F(p['weight_lower'][i][j]),F(w))
                self.assertLessEqual(F(w),F(p['weight_upper'][i][j]))
        self.assertLessEqual(r['fit_evaluations'],256)

    def test_zero_budget_preserves_unresolved(self):
        p=next(c['input'] for c in catalogue() if c['condition']=='intact')
        r=assess_interior(**p,fit_evaluations=0,max_boxes=1,max_candidates=0)
        self.assertEqual(r['status'],'unresolved')

    def test_failed_fit_cannot_exclude_family(self):
        r=assess_interior([[0,0],[0,0]],[[0,2],[2,0]],[1,0],
            [[1,0],['.7','.3'],['.7','.3']],[0,1,2],[0,1],
            max_boxes=1,max_candidates=0,fit_evaluations=20)
        self.assertEqual(r['status'],'unresolved')
        self.assertLessEqual(r['fit_evaluations'],20)

    def test_invalid_fit_budget(self):
        for b in (-1,True):
            with self.assertRaises(ValueError):
                assess_interior([[0]],[[0]],[0],[[0]],[0],[0],fit_evaluations=b)

    def test_small_residual_without_certificate_is_not_accepted(self):
        p=next(c['input'] for c in catalogue() if c['id']=='path3_3s_.8_intact')
        r=assess_interior(**p,max_boxes=1,max_candidates=0,fit_terms=0)
        self.assertEqual(r['status'],'unresolved')
        self.assertEqual(r['fit_stop'],'small_numerical_residual')
        self.assertNotEqual(r['fit_certificate_status'],'compatible_witness')

    def test_joint_initial_state_and_weight_fit(self):
        from decimal import Decimal,localcontext
        with localcontext() as ctx:
            ctx.prec=70
            samples=[]
            for t in (0,1):
                d=Decimal('.93')*(-Decimal('1.74')*t).exp()/2
                samples.append([str(Decimal('.485')+d),str(Decimal('.485')-d)])
        r=assess_interior([[0,'.7'],['.7',0]],[[0,'1.3'],['1.3',0]],[1,0],
            samples,[0,1],[0,1],initial_error='.1',sensor_error='1e-6',max_boxes=1,max_candidates=0)
        self.assertEqual(r['status'],'compatible_witness')
        self.assertEqual(r['witness_source'],'numerical_proposal_exact_certificate')
        self.assertLessEqual(abs(F(r['witness']['initial'][0])-1),F('.1'))
