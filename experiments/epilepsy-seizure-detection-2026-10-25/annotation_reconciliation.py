"""Offline hash-bound numbering reconciliation; source bytes never overwritten."""
from pathlib import Path
import hashlib
import re
from development_manifest import development_entry, parse_checksums, PINS


def boundary_subset(data):
    """Strict audited WFDB metadata/reset/boundary subset, not a general codec."""
    pos=0
    def word():
        nonlocal pos
        if pos+2>len(data):raise ValueError('Truncated annotation word')
        value=int.from_bytes(data[pos:pos+2],'little');pos+=2
        return value>>10,value&1023
    def skip():
        nonlocal pos
        if pos+4>len(data):raise ValueError('Truncated SKIP payload')
        high=int.from_bytes(data[pos:pos+2],'little');low=int.from_bytes(data[pos+2:pos+4],'little');pos+=4
        value=(high<<16)|low
        return value-2**32 if value>=2**31 else value
    if word()!=(22,0):raise ValueError('Expected initial metadata NOTE')
    kind,size=word()
    if kind!=63 or pos+size+(size%2)>len(data):raise ValueError('Invalid metadata AUX')
    note=data[pos:pos+size];pos+=size
    if size%2:
        if data[pos]!=0:raise ValueError('Nonzero AUX padding')
        pos+=1
    match=re.fullmatch(rb'## time resolution: ([1-9][0-9]*)',note)
    if match is None:raise ValueError('Unsupported sampling metadata')
    fs=int(match[1])
    if word()!=(59,0) or skip()!=-1 or word()!=(0,1):raise ValueError('Unsupported metadata reset')
    samples=[];total=0
    while True:
        kind,delta=word()
        if kind==delta==0:
            if pos!=len(data) or not samples or len(samples)%2:raise ValueError('Invalid terminator/boundary count')
            break
        while kind==59:
            if delta!=0:raise ValueError('Invalid SKIP interval')
            value=skip()
            if value<0:raise ValueError('Negative boundary increment')
            total+=value;kind,delta=word()
        expected=32 if len(samples)%2==0 else 33
        if kind!=expected:raise ValueError('Unsupported code or nonalternating boundaries')
        total+=delta
        if samples and (total<samples[-1] or (kind==33 and total==samples[-1])):
            raise ValueError('Unordered or empty event')
        samples.append(total)
    return fs,samples


def reconcile_block(lines, binary, approved_changes):
    """lines start with filename; approvals are(pair1, Start/End, old_index)."""
    fs,samples=boundary_subset(binary)
    if len(lines)<4:raise ValueError('Incomplete source block')
    count=re.fullmatch(r'Number of Seizures in File: (\d+)\s*',lines[3])
    if count is None or int(count[1])*2!=len(samples):raise ValueError('Binary/source event count differs')
    approved=set(approved_changes)
    if len(approved)!=len(approved_changes):raise ValueError('Duplicate approval')
    changes=set();result=list(lines)
    for i,sample in enumerate(samples):
        pair=i//2+1;kind='Start' if i%2==0 else 'End';at=4+i
        if at>=len(lines):raise ValueError('Missing source boundary')
        m=re.fullmatch(r'Seizure (\d+) '+kind+r' Time:[ \t]+(\d+) seconds\s*',lines[at])
        if m is None or int(m[2])*fs!=sample:raise ValueError('Source/binary numerical boundary differs')
        old=int(m[1])
        if old!=pair:
            change=(pair,kind,old)
            if change not in approved:raise ValueError('Unapproved numbering discrepancy')
            changes.add(change);a,b=m.span(1);result[at]=lines[at][:a]+str(pair)+lines[at][b:]
    if changes!=approved:raise ValueError('Unused or stale approval')
    return result,len(changes),fs


def reconcile_summary(source, case, record_path, binary, approved_changes):
    row=development_entry(record_path)
    if row['case']!=case:raise ValueError('Source/record case mismatch')
    root=Path(__file__).resolve().parent
    raw=(root/'source_metadata/CHB_SHA256SUMS.txt').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=PINS['CHB_SHA256SUMS.txt']:raise ValueError('Master hash mismatch')
    pins=parse_checksums(raw)
    if hashlib.sha256(source).hexdigest()!=pins.get(case+'/'+case+'-summary.txt') or hashlib.sha256(binary).hexdigest()!=pins.get(record_path+'.seizures'):
        raise ValueError('Original source/annotation hash mismatch')
    text=source.decode('ascii');lines=text.splitlines(keepends=True)
    target='File Name: '+record_path.split('/')[1]
    starts=[i for i,line in enumerate(lines) if line.strip()==target]
    if len(starts)!=1:raise ValueError('Source record identity not unique')
    start=starts[0];end=next((i for i in range(start+1,len(lines)) if lines[i].startswith('File Name: ')),len(lines))
    # Keep empty lines/positions intact externally; only pass nonempty block lines.
    positions=[i for i in range(start,end) if lines[i].strip()]
    compact=[lines[i] for i in positions];compact[0]=compact[0].removeprefix('File Name: ')
    changed,n,fs=reconcile_block(compact,binary,approved_changes)
    sampling=re.search(r'^Data Sampling Rate: (\d+) Hz\s*$',text,re.M)
    if sampling is None or int(sampling[1])!=fs:raise ValueError('Source/annotation rate mismatch')
    for i in range(1,len(positions)):
        lines[positions[i]]=changed[i]
    derived=''.join(lines).encode('ascii')
    return derived,dict(source_sha256=hashlib.sha256(source).hexdigest(),binary_sha256=hashlib.sha256(binary).hexdigest(),derived_sha256=hashlib.sha256(derived).hexdigest(),changed_identity_tokens=n,numerical_boundaries_unchanged=True,originals_overwritten=False)
