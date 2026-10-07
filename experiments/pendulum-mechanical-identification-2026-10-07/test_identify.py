import unittest,numpy as np
from identify import forecast,fit,blocks

class Controls(unittest.TestCase):
    def test_free_motion(self):
        a,v=forecast(np.array([.2]),np.array([.3]),np.zeros(4),np.array([.1]))
        self.assertAlmostEqual(a[0],.23);self.assertAlmostEqual(v[0],.3)
    def test_viscous_decay(self):
        a,v=forecast(np.array([0.]),np.array([1.]),np.array([0.,2.,0.,0.]),np.array([.1]))
        self.assertAlmostEqual(v[0],np.exp(-.2),places=10)
    def test_identification(self):
        x=np.array([[1,0,0,0],[0,1,0,0],[1,1,0,0]],float)
        c,_=fit(x,np.array([2.,3.,5.]),[0,1])
        np.testing.assert_allclose(c,[2,3,0,0],atol=1e-12)
    def test_integral_constant_velocity(self):
        t=np.arange(21)*.01
        data=np.column_stack([t,np.zeros(21),np.ones(21)*2])
        s,e,x,y=blocks(data)
        np.testing.assert_allclose(x[:,1],.2,atol=1e-14)
        np.testing.assert_allclose(y,0)

if __name__=='__main__':unittest.main()
