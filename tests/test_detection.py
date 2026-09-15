import unittest
from bfg_lab.detection import run


class DetectionTests(unittest.TestCase):
    def test_complete_catalogue_and_accounting(self):
        result=run()
        self.assertEqual(len(result['runs']),288)
        self.assertEqual(len(result['summary']),12)
        for row in result['summary']:
            self.assertEqual(row['runs'],24)
            self.assertEqual(row['runs'],row['abstained']+row['pre_event_alarm']+row['detected']+row['no_alarm'])
        for row in result['runs']:
            self.assertEqual(len(row['statuses']),20)
            if row['sensors']<8:
                self.assertEqual(row['outcome'],'abstained')
                self.assertIsNone(row['delay'])
            if row['delay'] is not None:
                self.assertEqual(row['delay'],row['first_alarm']-7)
                self.assertGreaterEqual(row['delay'],0)
        groups={}
        for row in result['runs']:
            groups.setdefault((row['family'],row['weight'],row['initial'],row['noise'],row['sensors']),[]).append(row)
        for rows in groups.values():
            self.assertEqual(len({r['prefix_hash'] for r in rows}),1)
            self.assertTrue(all(r['statuses'][:6]==rows[0]['statuses'][:6] for r in rows))
