import unittest
from fractions import Fraction
from bfg_lab.certified_comparison import run


class ComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=run()

    def test_catalogue_accounting_and_no_reversed_certificates(self):
        r=self.report
        self.assertEqual(len(r['cases']),39)
        self.assertEqual(len({c['id'] for c in r['cases']}),39)
        for method,counts in r['counts'].items():
            self.assertEqual(sum(counts.values()),39)
        for row in r['rows']:
            if row['baseline']['status']!='unresolved':
                self.assertEqual(row['baseline']['status'],row['search_255']['status'])
            if row['search_31']['status']!='unresolved':
                self.assertEqual(row['search_31']['status'],row['search_255']['status'])

    def test_synthetic_healthy_cases_not_excluded(self):
        for row in self.report['rows']:
            if row['id'].startswith(('corner_','grid_')):
                for method in ('baseline','search_31','search_255'):
                    self.assertNotEqual(row[method]['status'],'healthy_family_excluded')

    def test_diagnostic_witnesses_respect_original_family(self):
        cases={c['id']:c['input'] for c in self.report['cases']}
        witnesses=[d for d in self.report['diagnostics'] if d['kind']=='synthetic_generating_witness']
        self.assertTrue(witnesses)
        for d in witnesses:
            self.assertEqual(d['result']['status'],'compatible_witness')
            p=cases[d['id']]
            for i,x in enumerate(d['initial']):
                self.assertLessEqual(abs(Fraction(x)-Fraction(p['initial'][i])),Fraction(p['initial_error']))
                for j,w in enumerate(d['weights'][i]):
                    self.assertLessEqual(Fraction(p['weight_lower'][i][j]),Fraction(w))
                    self.assertLessEqual(Fraction(w),Fraction(p['weight_upper'][i][j]))
