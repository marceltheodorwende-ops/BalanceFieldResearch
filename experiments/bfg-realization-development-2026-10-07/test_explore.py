import math, unittest
from explore import allowed, scalar, energy, pairs

class Controls(unittest.TestCase):
    def test_sealed_holdout(self):
        for l in range(1,6):
            for c in range(1,4):
                self.assertTrue(allowed(f'len{l}_cond{c}_1.csv'))
                for a in [2,3]: self.assertFalse(allowed(f'len{l}_cond{c}_{a}.csv'))
        self.assertFalse(allowed('../len1_cond1_1.csv'))
    def test_known_scalar(self):
        self.assertAlmostEqual(scalar(.5),8/45)
        self.assertIsNone(scalar(1));self.assertIsNone(scalar(0))
    def test_contraction(self):
        for i in range(1,1000):
            y=i/1000
            self.assertGreater(scalar(y),0);self.assertLess(scalar(y),y)
    def test_energy_symmetry_and_calibration(self):
        self.assertAlmostEqual(energy(math.pi,.236),2*9.799*.236)
        self.assertEqual(energy(-.2,.236),energy(.2,.236))
    def test_nonconsecutive_rejection(self):
        rows=[dict(time=str(i),angle=str(a),angular_velocity='0',is_peak='1') for i,a in enumerate([.1,.1,-.1])]
        ps,rejected,_=pairs(rows,.236)
        self.assertEqual(len(ps),1);self.assertEqual(rejected,1);self.assertEqual(ps[0]['time'],1)

if __name__=='__main__': unittest.main()
