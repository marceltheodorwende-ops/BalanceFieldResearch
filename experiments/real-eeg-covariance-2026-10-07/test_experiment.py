import tempfile
import unittest
from unittest.mock import patch
import hashlib
import experiment
from pathlib import Path
import numpy as np
from experiment import update, read_edf, predict


class Controls(unittest.TestCase):
    def test_measurements_require_official_checksum(self):
        payload=b'known measurement bytes'
        sha=hashlib.sha256(payload).hexdigest()
        with tempfile.TemporaryDirectory() as temp, patch.object(experiment,'ROOT',Path(temp)):
            raw=Path(temp)/'raw';raw.mkdir()
            (raw/'SOURCE_SHA256SUMS.txt').write_text(sha+'  S001/S001R01.edf\n'+sha+'  S001/S001R02.edf\n')
            with patch.object(experiment,'retrieve',return_value=(payload,'official mirror')):
                rows=experiment.download(1)
                self.assertEqual(len(rows),2)
                self.assertTrue(all(row['sha256']==sha for row in rows))
            (raw/'S001R01.edf').write_bytes(b'corrupt')
            with patch.object(experiment,'retrieve',return_value=(b'wrong bytes','official mirror')):
                with self.assertRaisesRegex(ValueError,'checksum mismatch'):experiment.download(1)

    def test_scalar_independent_formula_and_neutral_directions(self):
        for y in np.linspace(.001,.999,1000):
            r=update(np.array([[-.7]]),np.array([[2.]]),np.ones((1,1)),np.array([[y]]),np.ones((1,1)))
            expected=2*y*y/((1+y)**2*(1+y*y))
            self.assertIsNone(r['terminal'])
            self.assertAlmostEqual(r['y'][0,0],expected,places=13)
            self.assertTrue(0<r['y'][0,0]<y)
            self.assertAlmostEqual(r['k'][0,0],-.7)
            self.assertAlmostEqual(r['f'][0,0],2.)

    def test_terminal_gates(self):
        eye=np.eye(2)
        self.assertEqual(update(-eye,eye,eye/2,eye,eye)['terminal'],'T_sel0')
        self.assertEqual(update(-eye,eye,eye/2,np.zeros((2,2)),eye)['terminal'],'T_load')
        self.assertEqual(update(-eye,eye,np.diag([0.,1.]),np.diag([.5,2.]),eye)['terminal'],'T_w1')

    def test_seed_complement_branches(self):
        v=np.array([1.,1.])/np.sqrt(2);p=np.outer(v,v);y=np.diag([.2,.7])
        positive=update(np.eye(2),p,p,y,p)
        self.assertEqual(positive['terminal'],'T_seednone')
        negative=update(-np.eye(2),p,p,y,p)
        self.assertIsNone(negative['terminal'])
        self.assertAlmostEqual(np.trace(negative['p']),2)
        p4=np.zeros((4,4));p4[:2,:2]=p;p4[2:,2:]=p
        degenerate=update(-np.eye(4),p4,p4/2,np.diag([.2,.7,.3,.8]),p4)
        self.assertEqual(degenerate['terminal'],'T_seeddeg')

    def test_diagonal_readout_independent_channels(self):
        values=np.linspace(.1,.8,8);f=np.diag(values);scale=1.
        # P=I gives PG=I. Formation-derived loads couple scalar channels.
        lc=np.sum(values/(1+values));lb=np.sum(values**3/(1+values))
        alpha=lb/(lc+lb);beta=lc/(lc+lb)
        expected=(alpha+beta*values**2)/(1+values)**2
        pred,result=predict(f,scale)
        self.assertIsNone(result['terminal'])
        np.testing.assert_allclose(pred,np.diag(expected),rtol=1e-12,atol=1e-12)

    def test_complex_unitary_covariance_and_invariants(self):
        rng=np.random.default_rng(20261007)
        for n in (2,3,4,8):
            for _ in range(10):
                a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
                f=a@a.conj().T; w=f/np.trace(f)
                y=np.diag(np.linspace(.1,.9,n)); p=np.eye(n); k=-np.eye(n)
                r=update(k,f,w,y,p)
                l,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
                conjugate=lambda a:l.conj().T@a@l
                left=np.zeros((2*n,2*n),complex);left[:n,:n]=l.conj().T;left[n:,n:]=l.conj().T
                rr=update(*[conjugate(a) for a in (k,f,w,y,p)],frames=(left@r['u'],r['s'],l.conj().T@r['v']))
                for key in ('k','f','w','y','p'):
                    np.testing.assert_allclose(r[key],rr[key],rtol=1e-10,atol=1e-10)
                np.testing.assert_allclose(r['t4'].conj().T@r['t4'],r['psel'],atol=1e-10)
                np.testing.assert_allclose(r['p']@r['p'],r['p'],atol=1e-10)
                self.assertAlmostEqual(np.trace(r['w']).real,1)
                self.assertAlmostEqual(r['m4'],1)
                self.assertTrue(np.all(np.linalg.eigvalsh(r['y'])>0))
                self.assertTrue(np.all(np.linalg.eigvalsh(r['y'])<1))
                self.assertLessEqual(len(r['y']),n)

    def test_known_edf_calibration_and_truncation(self):
        labels=['FC3','FC4','C3','C4','CP3','CP4','Cz','Pz'];ns=8
        field=lambda value,width:str(value).ljust(width).encode('ascii')
        fixed=(field(0,8)+field('test',80)+field('test',80)+field('01.01.26',8)+field('00.00.00',8)
               +field(256+256*ns,8)+field('',44)+field(1,8)+field(1,8)+field(ns,4))
        values=[labels,['']*ns,['uV']*ns,[-100]*ns,[100]*ns,[-1000]*ns,[1000]*ns,['']*ns,[160]*ns,['']*ns]
        header=fixed+b''.join(b''.join(field(v,width) for v in vals) for vals,width in zip(values,[16,80,8,8,8,8,8,80,8,32]))
        digital=np.tile(np.arange(160,dtype='<i2'),(ns,1)).tobytes()
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'known.edf';path.write_bytes(header+digital)
            x,clipped,fs=read_edf(path)
            self.assertEqual(fs,160);self.assertFalse(clipped.any())
            np.testing.assert_allclose(x[0],np.arange(160)*1e-7,atol=1e-18)
            path.write_bytes(header+digital[:-2])
            with self.assertRaises(ValueError):read_edf(path)


if __name__=='__main__':unittest.main()
