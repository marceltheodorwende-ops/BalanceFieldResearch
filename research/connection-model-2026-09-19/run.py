"""Run from repository root; prints bounded M3 demonstration, no empirical data."""
import sys
from pathlib import Path
import json
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from bfg_lab.connection_model import advance,seed

general=dict(connection=np.array([[0.,-1.,.3],[1.,0.,-.7],[-.3,.7,0.]]),
             coherence=np.diag([1.,2.,4.]),difference=np.diag([8.,9.,12.]),
             neutral=np.eye(3),d=np.array([1.,2.,1.]))
out={}
for label,state,steps in [('analytic',seed(),4),('noncommuting',general,3)]:
    rows=[]
    for k in range(steps):
        state,report=advance(state)
        rows.append(dict(step=k+1,**report))
        if state is None: break
    out[label]=rows
print(json.dumps(out,indent=2))
