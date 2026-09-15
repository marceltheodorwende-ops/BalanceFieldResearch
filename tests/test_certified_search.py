import unittest
from decimal import Decimal, localcontext
from bfg_lab.certified import assess_family
from bfg_lab.certified_search import refine_family


class RefinementTests(unittest.TestCase):
    def problem(self, weights):
        with localcontext() as ctx:
            ctx.prec = 60
            samples = [['1', '0']]
            for t, w in enumerate(weights, 1):
                y = (1 + (-2*Decimal(str(w))*t).exp())/2
                samples.append([str(y), str(1-y)])
        return dict(weight_lower=[[0,0],[0,0]], weight_upper=[[0,2],[2,0]],
                    initial=[1,0], samples=samples, times=list(range(len(samples))),
                    sensors=[0,1], sensor_error='0.000001')

    def test_interior_witness_resolves_overlap(self):
        p = self.problem(['0.5'])
        self.assertEqual(assess_family(**p)['status'], 'unresolved')
        r = refine_family(**p)
        self.assertEqual(r['status'], 'compatible_witness')
        self.assertEqual(r['witness']['weights'][0][1], '1/2')

    def test_inconsistent_times_exclude_entire_family(self):
        p = self.problem(['0.9','1.1'])
        self.assertEqual(assess_family(**p)['status'], 'unresolved')
        r = refine_family(**p, max_boxes=1024)
        self.assertEqual(r['status'], 'healthy_family_excluded')
        # Terminal dyadic boxes form an exhaustive, nonoverlapping partition
        # up to shared boundaries, with one exclusion certificate per leaf.
        from fractions import Fraction
        self.assertEqual(sum(Fraction(1,2**len(e['path'])) for e in r['excluded_leaves']), 1)

    def test_budget_does_not_become_alarm(self):
        r = refine_family(**self.problem(['0.5']), max_boxes=1)
        self.assertEqual(r['status'], 'unresolved')
        self.assertEqual(len(r['pending_paths']), 2)

    def test_initial_uncertainty_search(self):
        r = refine_family([[0]], [[0]], ['0.5'], [['0.25']], [0], [0], initial_error='0.5')
        self.assertEqual(r['status'], 'compatible_witness')
        self.assertEqual(r['witness']['initial'], ['1/4'])

    def test_depth_and_series_limits_remain_unresolved(self):
        self.assertEqual(refine_family(**self.problem(['0.5']), max_depth=0)['status'], 'unresolved')
        p = self.problem(['0.5']); p['times'] = [0,100]
        self.assertEqual(refine_family(**p, terms=2)['status'], 'unresolved')

    def test_invalid_budgets(self):
        for opts in ({'max_boxes':0}, {'max_boxes':True}, {'max_depth':-1}):
            with self.assertRaises(ValueError):
                refine_family(**self.problem(['0.5']), **opts)

    def test_healthy_interior_grid_never_excluded(self):
        for w in ('0', '0.125', '0.5', '0.9', '1', '1.75', '2'):
            with self.subTest(w=w):
                self.assertNotEqual(refine_family(**self.problem([w]), max_boxes=31)['status'],
                                    'healthy_family_excluded')
