import unittest,numpy as np
from shared_calibration import frequency_coefficient,fit_shared,G

class Controls(unittest.TestCase):
    def test_point_mass(self):
        self.assertAlmostEqual(frequency_coefficient(.5,0),2*G)
    def test_rotor_inertia(self):
        m,L,I=2.,.5,.03
        expected=m*G*L/(m*L*L+I)
        self.assertAlmostEqual(frequency_coefficient(L,I/m),expected)
    def test_known_shared_ratio(self):
        records=[]
        for i,L in enumerate([.236,.426,.607]):
            x=np.array([[1.,0.],[0.,1.],[1.,1.],[-1.,1.]])
            a=G*L/(L*L+.002);b=.01*(i+1)
            records.append(dict(name=str(i),length=L,x=x,target=a*x[:,0]+b*x[:,1]))
        ratio,params=fit_shared(records)
        self.assertAlmostEqual(ratio,.002,places=9)
        for i,(_,a,b) in enumerate(params):self.assertAlmostEqual(b,.01*(i+1),places=8)

if __name__=='__main__':unittest.main()
