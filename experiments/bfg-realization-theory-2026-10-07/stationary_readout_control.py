"""Synthetic control for the inherited-formation readout obstruction."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'real-eeg-covariance-2026-10-07'))
from experiment import update
from reference_carrier import prepare,readout
rng=np.random.default_rng(20261007)
errors=[]
for _ in range(100):
    theta,w=rng.normal(size=2)
    F,J,A,B=prepare(theta,w)
    result=update(-np.eye(3),F,F/np.trace(F),.5*F/np.trace(F),np.eye(3))
    assert result['terminal'] is None
    V=result['v']
    instruments=[V.conj().T@O@V for O in [J,A,B]]
    errors.extend(abs(np.array(readout(result['f'],*instruments))-[theta,w]))
assert max(errors)<1e-12
print('100 ambient updates; maximum inherited-readout residual',max(errors))
