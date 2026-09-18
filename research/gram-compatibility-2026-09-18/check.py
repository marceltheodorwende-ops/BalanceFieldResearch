"""Run from repository root: python research/gram-compatibility-2026-09-18/check.py"""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import numpy as np
from bfg_lab.formation import prepare_candidate
from bfg_lab.gram import rebuild

i = np.eye(2)
s = np.array([[0., 1.], [1., 0.]])
r = prepare_candidate(i, np.array([1., 0.]), np.diag([1., .5]), 3*i, i, i)
u = np.array([[1.], [0.], [1.], [0.]])/np.sqrt(2)
p = u @ u.T
b2 = np.kron(i, s)
yg1 = u.T @ np.eye(4) @ u
bnext = u.T @ b2 @ u
yrec = rebuild(bnext, [[1]], [[1]])['y']
e = (np.eye(4)-p) @ b2 @ u
assert r['gate']['passed']
assert np.allclose(r['transport']['basis'] @ r['transport']['basis'].conj().T, p)
np.testing.assert_allclose(yg1, [[1]])
np.testing.assert_allclose(yrec, [[0]], atol=1e-14)
np.testing.assert_allclose(yg1-yrec, e.T @ e)
# Compatible control: constant derivative I preserves the same support.
b2_control = np.eye(4)
bc = u.T @ b2_control @ u
np.testing.assert_allclose(rebuild(bc, [[1]], [[1]])['y'], yg1)
print(json.dumps({'gate': r['gate'], 'g1_load': float(yg1[0,0]),
                  'reconstructed_load': float(yrec[0,0].real),
                  'leakage_norm_squared': float((e.T @ e)[0,0]),
                  'compatible_control': 'passed'}, indent=2))
