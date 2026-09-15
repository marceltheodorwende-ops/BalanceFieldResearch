import unittest
from bfg_lab.certified_boundary import assess_boundary


class BoundaryTests(unittest.TestCase):
    def test_exact_endpoint_initial_witness(self):
        r=assess_boundary([[0]],[[0]],[0],[[1]],[0],[0],initial_error=1,max_boxes=1)
        self.assertEqual(r['status'],'compatible_witness')
        self.assertEqual(r['witness']['initial'],['1'])

    def test_candidate_rejection_is_not_family_exclusion(self):
        r=assess_boundary([[0,0],[0,0]],[[0,2],[2,0]],[1,0],
                          [[1,0],['.7','.3']],[0,1],[0,1],max_boxes=1)
        self.assertEqual(r['status'],'unresolved')
        self.assertGreater(r['candidate_checks'],0)

    def test_zero_candidate_budget_preserves_unresolved(self):
        r=assess_boundary([[0]],[[0]],[0],[[1]],[0],[0],initial_error=1,
                          max_boxes=1,max_candidates=0)
        self.assertEqual(r['status'],'unresolved')

    def test_partial_sensor_and_unobserved_initial_coordinate(self):
        r=assess_boundary([[0,0],[0,0]],[[0,0],[0,0]],[0,0],[[1],[1]],
                          [0,1],[1],initial_error=1,max_boxes=1)
        self.assertEqual(r['status'],'compatible_witness')
        self.assertEqual(r['witness']['initial'][1],'1')

    def test_invalid_budget(self):
        for opts in ({'max_candidates':True},{'max_candidates':-1},{'candidate_terms':129}):
            with self.assertRaises(ValueError):
                assess_boundary([[0]],[[0]],[0],[[0]],[0],[0],**opts)

    def test_one_candidate_must_fit_every_time(self):
        r=assess_boundary([[0]],[[0]],[0],[[1],[0]],[0,1],[0],
                          initial_error=1,max_boxes=1)
        self.assertEqual(r['status'],'unresolved')
        self.assertEqual(r['candidate_checks'],1)
