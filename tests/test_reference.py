import unittest
import numpy as np
from bfg_lab.reference import assess_reference, run
from bfg_lab.diffusion import adjacency, heat_operator


class ReferenceTests(unittest.TestCase):
    def test_exact_known_trajectory_and_alarm(self):
        r=np.array([[.8,.2],[.2,.8]])
        data=np.array([[1.],[.8],[.68]])
        self.assertEqual(assess_reference(r,[1.,0.],data,[0])['status'],'no_observed_conflict')
        data[-1,0]+=.1
        result=assess_reference(r,[1.,0.],data,[0])
        self.assertEqual(result['first_alarm'],2)

    def test_bounded_calibration_and_sensor_noise(self):
        r=np.array([[.8,.2],[.2,.8]])
        x=np.array([1.,0.]); samples=[]
        for _ in range(5):
            samples.append(x.copy()); x=r@x
        noise=np.array([[.01,-.01],[-.01,.01],[.01,.01],[-.01,-.01],[.01,-.01]])
        result=assess_reference(r,[1.01,-.01],np.array(samples)+noise,[0,1],initial_error=.01,sensor_error=.01)
        self.assertIsNone(result['first_alarm'])

    def test_uniform_state_hides_edge_failure(self):
        a=adjacency('path',8,1.); r,_=heat_operator(a,.2)
        a[3,4]=a[4,3]=0.; changed,_=heat_operator(a,.2)
        x=np.ones(8)/8; samples=[x.copy()]
        for _ in range(20):
            x=changed@x; samples.append(x.copy())
        self.assertIsNone(assess_reference(r,np.ones(8)/8,samples,list(range(8)))['first_alarm'])

    def test_invalid_sensor_identity(self):
        with self.assertRaises(ValueError):
            assess_reference(np.eye(2),[1,0],[[1,0]],[0,0])

    def test_no_future_data_changes_earlier_diagnostics(self):
        r=np.array([[.8,.2],[.2,.8]])
        prefix=[[1.],[.8],[.68]]
        short=assess_reference(r,[1.,0.],prefix,[0])
        extended=assess_reference(r,[1.,0.],prefix+[[9.]],[0])
        self.assertEqual(short['history'],extended['history'][:3])
        self.assertEqual(extended['first_alarm'],3)

    def test_catalogue_accounting(self):
        result=run()
        self.assertEqual(len(result['runs']),288)
        for row in result['summary']:
            self.assertEqual(row['runs'],24)
            self.assertEqual(row['runs'],row['pre_event_alarm']+row['detected']+row['no_alarm'])
        self.assertTrue(all(r['full_initial_calibration'] for r in result['runs']))
