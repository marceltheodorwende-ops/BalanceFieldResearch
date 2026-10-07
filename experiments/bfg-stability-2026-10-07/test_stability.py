import unittest
import numpy as np
class Bounds(unittest.TestCase):
    def test_log_norm_bound(self):
        for a,b in [(4.,.2),(1.,2.),(40.,.001)]:
            L=(-b+np.sqrt(b*b+4*a))/2
            for theta in np.linspace(-np.pi,np.pi,101):
                J=np.array([[0,np.sqrt(a)],[-np.sqrt(a)*np.cos(theta),-b]])
                actual=np.linalg.eigvalsh((J+J.T)/2)[-1]
                self.assertLessEqual(actual,L+1e-12)
    def test_upright_instability(self):
        a,b=4.,.2
        roots=np.linalg.eigvals(np.array([[0,1],[a,-b]]))
        self.assertGreater(max(roots),0)
        self.assertAlmostEqual(max(roots),(-b+np.sqrt(b*b+4*a))/2)
if __name__=='__main__':unittest.main()
