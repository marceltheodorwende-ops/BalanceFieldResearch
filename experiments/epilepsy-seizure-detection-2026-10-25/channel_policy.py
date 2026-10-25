"""Fixed instrument-coordinate candidate; no waveform reader or neural dynamics."""
from fractions import Fraction
import re
from edf_header import to_volts, UNITS
from montage_audit import BIPOLAR18

TARGET17=tuple(x for x in BIPOLAR18 if x!='T8-P8')
EDGE_PATH={'F8-T8':-1,'FP2-F8':-1,'FP2-F4':1,'F4-C4':1,
           'C4-P4':1,'P4-O2':1,'P8-O2':-1}

def normalize(label):
    return re.sub(r'\s*-\s*','-',label.strip()).upper()

def compile_map(metadata):
    """Direct unique labels first; reverse-only unique labels get sign -1.

    Direct duplicates reject; never repair using an arbitrary copy/reverse.
    Returns metadata eligibility only, not permission to access waveforms.
    """
    reasons=[];mapping=[];channels=metadata['channels']
    if metadata.get('discontinuous'):reasons.append('EDF+D requires unresolved discontinuous timing')
    if metadata.get('records',-1)<=0:reasons.append('unknown or nonpositive record count')
    if Fraction(metadata['record_seconds'])<=0:reasons.append('nonpositive record duration')
    for target in TARGET17:
        left,right=target.split('-');reverse=right+'-'+left
        direct=[c for c in channels if normalize(c['label'])==target]
        if len(direct)>1:
            reasons.append(target+':duplicate direct label');continue
        sign=1;matches=direct
        if not direct:
            sign=-1;matches=[c for c in channels if normalize(c['label'])==reverse]
        if len(matches)!=1:
            reasons.append(target+':missing or duplicate reverse label');continue
        c=matches[0]
        if c['unit'] not in UNITS or c.get('volts_per_digital_step') is None:
            reasons.append(target+':unknown voltage calibration');continue
        if Fraction(c['sampling_hz'])!=256:
            reasons.append(target+':unsupported sample rate');continue
        mapping.append(dict(target=target,source_index=c['index'],source_label=c['label'],sign=sign))
    indices=[x['source_index'] for x in mapping]
    if len(set(indices))!=len(indices):reasons.append('one source channel assigned multiple times')
    return dict(candidate='fixed17-bipolar-v1',eligible=not reasons,reasons=reasons,
                mapping=mapping,full_waveform_access_enabled=False)

def signed_volts(channel,digital,sign):
    if sign not in (-1,1):raise ValueError('Orientation must be plus or minus one')
    return sign*to_volts(channel,digital)

def incidence(labels,nodes):
    result=[]
    for label in labels:
        a,b=label.split('-');result.append([Fraction(int(n==a)-int(n==b)) for n in nodes])
    return result

def reconstruction():
    """R:17 to18, S:18 to17, for exact ideal bipolar incidence data only."""
    r=[]
    for label in BIPOLAR18:
        r.append([Fraction(EDGE_PATH.get(k,0)) for k in TARGET17] if label=='T8-P8'
                 else [Fraction(int(k==label)) for k in TARGET17])
    s=[[Fraction(int(k==label)) for k in BIPOLAR18] for label in TARGET17]
    return r,s
