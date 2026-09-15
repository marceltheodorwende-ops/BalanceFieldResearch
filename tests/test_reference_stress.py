import unittest
from bfg_lab.reference_stress import run


class ReferenceStressTests(unittest.TestCase):
    def test_design_and_valid_reference_controls(self):
        result=run(); rows=result['runs']
        self.assertEqual(len(rows),144)
        controls=[r for r in rows if not r['cut'] and r['reference_scale']==1 and r['calibration']!='understated']
        self.assertEqual(len(controls),16)
        self.assertTrue(all(r['first_alarm'] is None for r in controls))
        invisible=[r for r in rows if r['cut'] and not r['probe'] and r['reference_scale']==1 and r['calibration']=='unbiased']
        self.assertEqual(len(invisible),4)
        self.assertTrue(all(r['first_alarm'] is None for r in invisible))
        self.assertEqual(sum(r['runs'] for r in result['summary']),144)
        for row in result['summary']:
            self.assertEqual(row['runs'],row['alarms']+row['no_alarm'])
        paired={}
        for row in rows:
            paired.setdefault((row['family'],row['weight'],row['probe'],row['cut']),set()).add(row['samples_hash'])
        self.assertTrue(all(len(hashes)==1 for hashes in paired.values()))
