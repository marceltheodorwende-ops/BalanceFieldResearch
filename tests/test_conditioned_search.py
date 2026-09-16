import unittest
from bfg_lab.network_transfer import catalogue
from bfg_lab.certified_interior import assess_interior


class ConditionedTests(unittest.TestCase):
    def test_all_complete_graph_cases_certified(self):
        for c in catalogue():
            if c['graph']!='complete4' or c['condition']!='intact': continue
            with self.subTest(case=c['id']):
                r=assess_interior(**c['input'],max_boxes=1,max_candidates=0,fit_rcond=1e-8)
                self.assertEqual(r['status'],'compatible_witness')
                self.assertEqual(r['fit_rcond'],1e-8)
                self.assertLessEqual(r['fit_evaluations'],256)

    def test_default_remains_stalled_on_old_regression(self):
        p=next(c['input'] for c in catalogue() if c['id']=='complete4_4s_.8_intact')
        r=assess_interior(**p,max_boxes=1,max_candidates=0)
        self.assertEqual(r['status'],'unresolved')

    def test_small_residual_still_requires_certificate(self):
        p=next(c['input'] for c in catalogue() if c['id']=='complete4_4s_.8_intact')
        r=assess_interior(**p,max_boxes=1,max_candidates=0,fit_rcond=1e-8,fit_terms=0)
        self.assertEqual(r['status'],'unresolved')
        self.assertEqual(r['fit_stop'],'small_numerical_residual')

    def test_invalid_cutoffs(self):
        for cutoff in (True,-1,1,float('nan'),'1e-8'):
            with self.assertRaises(ValueError):
                assess_interior([[0]],[[0]],[0],[[0]],[0],[0],fit_rcond=cutoff)

    def test_json_cli_accepts_numeric_cutoff(self):
        import json,subprocess,sys,uuid
        from pathlib import Path
        root=Path(__file__).resolve().parents[1]
        output=root/('cli-test-'+uuid.uuid4().hex+'.json')
        try:
            process=subprocess.run([sys.executable,'-m','bfg_lab.certified_interior','--input',
                str(root/'research/conditioned-search-2026-09-16/example.json'),
                '--output',str(output)],cwd=root,capture_output=True,text=True)
            self.assertEqual(process.returncode,0,process.stderr)
            self.assertEqual(json.loads(output.read_text())['status'],'compatible_witness')
        finally:
            output.unlink(missing_ok=True)
