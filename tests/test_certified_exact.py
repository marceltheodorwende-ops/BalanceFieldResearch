import unittest
from bfg_lab.certified_exact import assess_exact_pair


class ExactPairTests(unittest.TestCase):
    def case(self,lo=0,hi=2,samples=None,**kw):
        return assess_exact_pair([[0,lo],[lo,0]],[[0,hi],[hi,0]],[1,0],
            samples or [[1,0],['.7','.3']],[0,1],[0,1],max_boxes=1,**kw)

    def test_symbolic_log_witness(self):
        r=self.case()
        self.assertEqual(r['status'],'compatible_witness')
        self.assertEqual(r['symbolic_witness']['ratio'],'2/5')

    def test_finite_time_equilibrium_is_excluded(self):
        r=assess_exact_pair([[0,1],[1,0]],[[0,1],[1,0]],[1,0],
            [[1,0],['.5','.5']],[0,100],[0,1],terms=2)
        self.assertEqual(r['status'],'healthy_family_excluded')
        self.assertEqual(r['certificate']['rule'],'strict_positive_decay')

    def test_weight_outside_box(self):
        self.assertEqual(self.case(hi='.1')['status'],'healthy_family_excluded')

    def test_sensor_order(self):
        r=assess_exact_pair([[0,0],[0,0]],[[0,2],[2,0]],[1,0],
            [[0,1],['.3','.7']],[0,1],[1,0],max_boxes=1)
        self.assertEqual(r['status'],'compatible_witness')

    def test_mass_conflict(self):
        self.assertEqual(self.case(samples=[[1,0],['.7','.4']])['status'],'healthy_family_excluded')

    def test_low_log_budget_abstains(self):
        r=self.case(lo='.458',hi='.459',log_terms=1)
        self.assertEqual(r['status'],'unresolved')

    def test_out_of_scope_multiple_times(self):
        r=assess_exact_pair([[0,0],[0,0]],[[0,2],[2,0]],[1,0],
            [[1,0],['.7','.3'],['.7','.3']],[0,1,2],[0,1],max_boxes=1)
        self.assertEqual(r['status'],'unresolved')

    def test_noisy_input_not_symbolic(self):
        self.assertNotIn('symbolic_witness',self.case(sensor_error='.01'))

    def test_invalid_log_budget(self):
        for n in (0,True,257):
            with self.assertRaises(ValueError): self.case(log_terms=n)

    def test_partial_sensor_stays_outside_symbolic_scope(self):
        r=assess_exact_pair([[0,0],[0,0]],[[0,2],[2,0]],[1,0],
            [[1],['.7']],[0,1],[0],max_boxes=1)
        self.assertEqual(r['status'],'unresolved')
