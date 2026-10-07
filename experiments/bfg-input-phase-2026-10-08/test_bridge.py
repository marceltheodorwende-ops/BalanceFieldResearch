import unittest
import numpy as np
from bridge import kick,energy,chart,qp_rhs

class Controls(unittest.TestCase):
    def test_exact_work_and_inverse(self):
        rng=np.random.default_rng(910)
        theta=rng.uniform(-3,3,200);w=rng.uniform(-4,4,200);j=rng.uniform(-1,1,200);a=3.
        t,v=kick(theta,w,a,j)
        np.testing.assert_allclose(energy(t,v,a)-energy(theta,w,a),w*j+j*j/2,atol=1e-12,rtol=0)
        tt,vv=kick(t,v,a,-j)
        np.testing.assert_allclose(vv,w,atol=1e-12,rtol=0);np.testing.assert_array_equal(tt,theta)
    def test_chain_rule_for_torque(self):
        theta=.7;w=-.8;a=3.;b=.1;torque=.4
        q=2*np.sin(theta/2);p=w/np.sqrt(a)
        dq,dp=qp_rhs(q,p,a,b,torque/np.sqrt(a))
        self.assertAlmostEqual(dq,w*np.cos(theta/2))
        self.assertAlmostEqual(dp,(-a*np.sin(theta)-b*w+torque)/np.sqrt(a))
        self.assertAlmostEqual(q*dq+p*dp,-b*p*p+p*torque/np.sqrt(a))
    def test_rest_and_phase_singularity(self):
        e,phi,rest=chart(0.,0.,3.);self.assertTrue(rest)
        e,phi,rest=chart(*kick(0.,0.,3.,.2),3.)
        self.assertFalse(rest);self.assertAlmostEqual(e,.2**2/6)
        # Removing all kinetic energy can return exactly to undefined-phase rest.
        self.assertTrue(chart(*kick(0.,.2,3.,-.2),3.)[2])
    def test_signed_energy_counterexample(self):
        self.assertLess(energy(*kick(0.,1.,3.,-.1),3.),energy(0.,1.,3.))
        self.assertGreater(energy(*kick(0.,1.,3.,.1),3.),energy(0.,1.,3.))
    def test_invalid_and_rotation(self):
        with self.assertRaises(ValueError):kick(0.,0.,3.,np.nan)
        with self.assertRaises(ValueError):chart(np.pi,0.,3.)
        with self.assertRaises(ValueError):qp_rhs(2.,0.,3.,.1,0.)
        # Global kick remains defined when its energy lies outside local chart.
        t,w=kick(0.,0.,3.,10.)
        with self.assertRaises(ValueError):chart(t,w,3.)

if __name__=='__main__':unittest.main()

class ForceFactorControl(unittest.TestCase):
    def test_nonresonant_sylvester_has_no_tangent_factor(self):
        from scipy.linalg import expm
        a,b,h=3.,.1,.2
        M=expm(h*np.array([[0.,1.],[-a,-b]]));D=np.diag([1.,1.,.4])
        # Vectorizing B D - M B in column-major order yields this matrix.
        operator=np.kron(D.T,np.eye(2))-np.kron(np.eye(3),M)
        self.assertEqual(np.linalg.matrix_rank(operator),6)
        self.assertGreater(np.linalg.svd(operator,compute_uv=False)[-1],.001)
