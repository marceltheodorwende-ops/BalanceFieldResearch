import unittest
from decimal import Decimal, localcontext
from bfg_lab.certified import assess_family


class CertifiedTests(unittest.TestCase):
    def test_constant_exact_witness(self):
        r=assess_family([[0,'.9'],['.9',0]],[[0,'1.1'],['1.1',0]],
                        ['.5','.5'],[['.5','.5'],['.5','.5']],[0,1],[0,1])
        self.assertEqual(r['status'],'compatible_witness')

    def test_interior_parameter_not_rejected(self):
        r=assess_family([[0,'.9'],['.9',0]],[[0,'1.1'],['1.1',0]],
                        [1,0],[[1,0],['.56766764','.43233236']],[0,1],[0,1],sensor_error='.000001')
        self.assertEqual(r['status'],'compatible_witness')

    def test_whole_family_excluded(self):
        r=assess_family([[0,'.9'],['.9',0]],[[0,'1.1'],['1.1',0]],
                        [1,0],[[1,0],[3,0]],[0,1],[0,1],sensor_error='.001')
        self.assertEqual(r['status'],'healthy_family_excluded')
        self.assertIn('certificate',r)

    def test_outer_overlap_is_not_a_witness(self):
        r=assess_family([[0,0],[0,0]],[[0,2],[2,0]],
                        [1,0],[[1,0],['.7','.3']],[0,1],[0,1])
        self.assertEqual(r['status'],'unresolved')

    def test_insufficient_series_budget_abstains(self):
        r=assess_family([[0,1],[1,0]],[[0,1],[1,0]],
                        [1,0],[[1,0],['.5','.5']],[0,100],[0,1],terms=2)
        self.assertEqual(r['status'],'unresolved')

    def test_invalid_box(self):
        with self.assertRaises(ValueError):
            assess_family([[0,2],[2,0]],[[0,1],[1,0]],[1,0],[[1,0]],[0],[0,1])

    def test_healthy_weight_and_error_corners(self):
        with localcontext() as ctx:
            ctx.prec=90
            for weight in (Decimal('.9'),Decimal('1'),Decimal('1.1')):
                for e0 in (Decimal('-.001'),Decimal('.001')):
                    for e1 in (Decimal('-.001'),Decimal('.001')):
                        for noise in (Decimal('-.0001'),Decimal('.0001')):
                            x0=Decimal(1)+e0; x1=e1
                            samples=[]
                            for t in (Decimal(0),Decimal('.1'),Decimal(1),Decimal(3)):
                                diff=(x0-x1)*(-2*weight*t).exp()/2
                                mean=(x0+x1)/2
                                samples.append([str(mean+diff+noise),str(mean-diff-noise)])
                            r=assess_family([[0,'.9'],['.9',0]],[[0,'1.1'],['1.1',0]],
                                            [1,0],samples,[0,'.1',1,3],[0,1],
                                            initial_error='.001',sensor_error='.000100000000000000000000000001')
                            self.assertNotEqual(r['status'],'healthy_family_excluded')

    def test_timewise_compatibility_does_not_produce_common_witness(self):
        r=assess_family([[0,'.9'],['.9',0]],[[0,'1.1'],['1.1',0]],
                        [1,0],[[1,0],['.582649444','.417350556'],['.506138670','.493861330']],
                        [0,1,2],[0,1],sensor_error='.000000001')
        self.assertNotEqual(r['status'],'compatible_witness')

    def test_partial_sensor_exact_witness_and_initial_conflict(self):
        args=([[0,0],[0,0]],[[0,0],[0,0]],[1,0])
        self.assertEqual(assess_family(*args,[[1],[1]],[0,1],[0])['status'],'compatible_witness')
        self.assertEqual(assess_family(*args,[[2]],[0],[0])['status'],'healthy_family_excluded')

    def test_three_node_independent_modal_solution(self):
        with localcontext() as ctx:
            ctx.prec=80
            one=Decimal(1); e=(-one).exp(); e3=(-3*one).exp()
            target=[one/3+e/2+e3/6,one/3-e3/3,one/3-e/2+e3/6]
            a=[[0,1,0],[1,0,1],[0,1,0]]
            r=assess_family(a,a,[1,0,0],[[1,0,0],[str(v) for v in target]],
                            [0,1],[0,1,2],sensor_error='1e-20',terms=64)
            self.assertEqual(r['status'],'compatible_witness')
