"""Boundary/regression tests derived from the mathematical claims, not fitted data."""
import unittest
import numpy as np
import audit

class BFGConservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.update = staticmethod(audit.load_update())

    def test_commuting_formation_preserves_weighted_kernel(self):
        f=np.diag([1.,3.]); y=np.diag([.25,.5]); w=np.eye(2)/2
        k=np.array([[2.,1.+2j],[1.-2j,-1.]])
        r=self.update(k,f,w,y,np.eye(2))
        self.assertIsNone(r["terminal"])
        self.assertAlmostEqual(np.trace(r["f"]@r["k"]).real,-1.,places=12)

    def test_no_commutation_assumption_for_trace_charge(self):
        sx=audit.pauli()[1]
        f=np.array([[1.,.5],[.5,1.]])
        k=np.array([[2.,1.],[1.,-1.]])
        r=self.update(k,f,np.eye(2)/2,np.diag([.25,.5]),np.eye(2))
        self.assertIsNone(r["terminal"])
        self.assertAlmostEqual(np.trace(r["k"]).real,1.,places=12)
        self.assertGreater(abs(np.trace(r["f"]@r["k"]).real-np.trace(f@k).real),.05)

    def test_seeded_two_step_signed_history_balance(self):
        v=np.array([np.sqrt(3)/2,.5]); p=np.outer(v,v)
        state=(np.diag([-1.,-2.]),p,p,np.diag([.25,.5]),p)
        flux=0.
        for _ in range(2):
            k,f,w,y,p=state
            r=self.update(k,f,w,y,p)
            self.assertIsNone(r["terminal"])
            n=len(y); uc=r["u"][:n]; ub=r["u"][n:]
            d=uc@uc.conj().T+ub@ub.conj().T
            flux+=np.trace(k@(np.eye(n)-d)).real
            state=(r["k"],r["f"],r["w"],r["y"],r["p"])
        self.assertAlmostEqual(flux,-.5,places=11)
        self.assertAlmostEqual(np.trace(state[0]).real+flux,-3.,places=11)

    def test_terminal_not_assigned_a_successor_charge(self):
        r=self.update(np.eye(2),np.eye(2),np.eye(2)/2,2*np.eye(2),np.eye(2))
        self.assertEqual(r["terminal"],"T_sel0")
        self.assertNotIn("k",r)

    def test_raw_gram_congruence_stays_positive(self):
        g=np.diag([1.25,1.5]); e=np.array([[1.,2.],[-1.,1.]])
        self.assertGreater(np.linalg.eigvalsh(e.T@g@e).min(),0.)

    def test_isotropic_internal_rank_one_choice_breaks_covariance(self):
        # An explicit stabilizer of the isotropic input moves a proposed time line.
        p=np.diag([1.,0.,0.]); swap=np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,1.]])
        self.assertGreater(np.linalg.norm(swap@p@swap.T-p),1.)
        for x in [np.eye(3),.5*np.eye(3),np.eye(3)/3]:
            np.testing.assert_allclose(swap@x@swap.T,x,atol=0.,rtol=0.)

    def test_lorentz_carrier_is_not_an_eventwise_four_charge(self):
        eye,sx,_,_=audit.pauli()
        f=np.array([[1.,.5],[.5,1.]])
        r=self.update(eye+sx,f,eye/2,np.diag([.25,.5]),eye)
        self.assertIsNone(r["terminal"])
        aligned=r["v"]@r["k"]@r["v"].conj().T
        x=audit.coordinates(aligned)
        self.assertAlmostEqual(x[0],1.,places=12)
        self.assertAlmostEqual(x[1],np.sqrt(1152/1295),places=12)
        self.assertGreater(audit.qdet(aligned),.1)

if __name__ == "__main__":
    unittest.main(verbosity=2)

