"""Exact rational identifiability audit of allowed chb01 montage metadata."""
from fractions import Fraction as F
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
STANDARD=('FP1','F3','C3','P3','O1','F7','T7','P7','FZ','CZ','PZ',
          'FP2','F4','C4','P4','O2','F8','T8','P8')
BIPOLAR18=('FP1-F7','F7-T7','T7-P7','P7-O1','FP1-F3','F3-C3','C3-P3','P3-O1',
           'FP2-F4','F4-C4','C4-P4','P4-O2','FP2-F8','F8-T8','T8-P8','P8-O2','FZ-CZ','CZ-PZ')

def rank(matrix):
    a=[list(map(F,row)) for row in matrix];i=0
    for j in range(len(a[0])):
        pivot=next((k for k in range(i,len(a)) if a[k][j]),None)
        if pivot is None: continue
        a[i],a[pivot]=a[pivot],a[i]
        q=a[i][j];a[i]=[x/q for x in a[i]]
        for k in range(len(a)):
            if k!=i:
                q=a[k][j];a[k]=[x-q*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a): break
    return i

def audit():
    header=(ROOT/'source_metadata/chb01-summary.txt').read_text().split('File Name:')[0]
    labels=re.findall(r'^Channel [0-9]+: ([A-Z0-9]+-[A-Z0-9]+)\s*$',header,re.M)
    nodes=sorted(set(v for label in labels for v in label.split('-')))
    def row(label):
        a,b=label.split('-');return [F(int(n==a)-int(n==b)) for n in nodes]
    B=[row(l) for l in labels]
    L=[[F(int(n==target))-F(int(n in STANDARD),19) for n in nodes] for target in STANDARD]
    w=[F(int(n in ('FZ','CZ','PZ'))) for n in nodes]
    measured=[sum(a*b for a,b in zip(r,w)) for r in B]
    target=[sum(a*b for a,b in zip(r,w)) for r in L]
    # Independent graph-component calculation controls exact elimination rank.
    edges=[label.split('-') for label in labels];unseen=set(nodes);components=[]
    while unseen:
        first=min(unseen);unseen.remove(first);component={first}
        while True:
            new={v for a,b in edges if a in component or b in component for v in (a,b)}-component
            if not new:break
            component|=new;unseen-=new
        components.append(sorted(component))
    components.sort()
    assert len(labels)==23 and len(nodes)==21
    assert rank(B)==len(nodes)-len(components)==19
    assert not any(measured) and any(target)
    assert rank(B+L)==20
    assert all(label in labels for label in BIPOLAR18)
    assert row('P7-T7')==[-v for v in row('T7-P7')]
    assert labels.count('T8-P8')==2
    return dict(source='source_metadata/chb01-summary.txt',bipolar_rows=len(labels),electrode_nodes=len(nodes),
        exact_incidence_rank=rank(B),components=components,common_average_target_rank=rank(L),
        stacked_rank=rank(B+L),common_average_identifiable=False,
        kernel_witness=dict(nonzero_electrodes=['FZ','CZ','PZ'],measurement_zero=True,
            target_values={n:str(v) for n,v in zip(STANDARD,target)}),
        candidate_bipolar18=list(BIPOLAR18),candidate_rank=rank([row(l) for l in BIPOLAR18]),
        duplicate='T8-P8 occurs twice',reversal='P7-T7 is minus T7-P7',
        generalization='chb01 metadata only; no header/unit or other-record montage verification',empirical_performance=False)

if __name__=='__main__':
    result=audit();(ROOT/'montage_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
