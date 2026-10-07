"""Explicit EEG bridge experiment; see frozen PROTOCOL.md before interpreting."""
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import sys
import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import scipy
from scipy.signal import butter, sosfilt

ROOT = Path(__file__).resolve().parent
CHANNELS = ['FC3', 'FC4', 'C3', 'C4', 'CP3', 'CP4', 'Cz', 'Pz']
SEED = 20261007


def download(subject):
    out = []
    for run in (1, 2):
        name = f'S{subject:03d}R{run:02d}.edf'
        url = f'https://physionet.org/files/eegmmidb/1.0.0/S{subject:03d}/{name}'
        target = ROOT / 'raw' / name
        target.parent.mkdir(exist_ok=True)
        if not target.exists():
            for attempt in range(3):
                try:
                    with urllib.request.urlopen(url, timeout=120) as response:
                        data = response.read()
                    break
                except OSError:
                    if attempt == 2: raise
                    time.sleep(1)
            temp = target.with_suffix('.partial')
            temp.write_bytes(data)
            temp.replace(target)
        data = target.read_bytes()
        out.append(dict(subject=subject, run=run, file=name, url=url,
                        bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
    return out


def read_edf(path):
    """EDF/EDF+ reader for equal-rate selected channels; no annotation parsing."""
    data = path.read_bytes()
    head = data[:256]
    if len(head) != 256 or head[:8].strip() != b'0':
        raise ValueError('Not a supported EDF header')
    header_size = int(head[184:192]); records = int(head[236:244])
    duration = float(head[244:252]); ns = int(head[252:256])
    widths = [16, 80, 8, 8, 8, 8, 8, 80, 8, 32]
    fields = []; pos = 256
    for width in widths:
        fields.append([data[pos+i*width:pos+(i+1)*width].decode('ascii').strip()
                       for i in range(ns)])
        pos += width*ns
    if pos != header_size or records <= 0:
        raise ValueError('Unexpected EDF record/header dimensions')
    labels = [x.strip('.').lower() for x in fields[0]]
    indices = [labels.index(ch.lower()) for ch in CHANNELS]
    samples = np.array(fields[8], dtype=int)
    block = int(samples.sum())
    raw = np.frombuffer(data[header_size:], dtype='<i2')
    if len(raw) != records*block:
        raise ValueError('Truncated or unexpected EDF payload')
    raw = raw.reshape(records, block)
    offsets = np.r_[0, np.cumsum(samples)]
    channels = []; clipped = []; fs = []
    for idx in indices:
        values = raw[:, offsets[idx]:offsets[idx+1]].reshape(-1)
        pmin, pmax = float(fields[3][idx]), float(fields[4][idx])
        dmin, dmax = float(fields[5][idx]), float(fields[6][idx])
        unit = fields[2][idx]
        factor = {'uV': 1e-6, 'mV': 1e-3, 'V': 1.0}.get(unit)
        if factor is None or dmax <= dmin:
            raise ValueError(f'Unsupported calibration: {unit}')
        channels.append(((values.astype(float)-dmin)*(pmax-pmin)/(dmax-dmin)+pmin)*factor)
        clipped.append((values <= dmin) | (values >= dmax))
        fs.append(samples[idx]/duration)
    if not all(rate == 160 for rate in fs):
        raise ValueError(f'Unexpected sample rate {fs}')
    return np.array(channels), np.any(clipped, axis=0), 160


def features(subject, run):
    path = ROOT / 'raw' / f'S{subject:03d}R{run:02d}.edf'
    x, clipped, fs = read_edf(path)
    x -= x.mean(axis=0)
    bad = clipped | np.any(np.abs(x) > 500e-6, axis=0) | np.any(~np.isfinite(x), axis=0)
    filtered = sosfilt(butter(4, [1, 40], btype='bandpass', fs=fs, output='sos'), x, axis=1)
    out = []
    for start in range(4*fs, x.shape[1]-2*fs+1, 2*fs):
        z = filtered[:, start:start+2*fs]
        cov = np.cov(z)
        valid = not bad[start:start+2*fs].any() and np.isfinite(cov).all() and np.trace(cov)>0
        shrunk = .95*cov+.05*np.trace(cov)*np.eye(8)/8
        out.append((start/fs, valid, shrunk))
    return out


def polar(x, tol=1e-12):
    u, s, vh = np.linalg.svd(x, full_matrices=False)
    active = s > tol*max(1., float(s[0]) if len(s) else 0.)
    return u[:, active] @ vh[active], int(active.sum())


def update(k, f, w, y, p, tol=1e-12, frames=None):
    """Ambient paper update. Returns named terminal or complete successor."""
    n = len(y); identity = np.eye(n)
    eig, vectors = np.linalg.eigh(y)
    q = (vectors[:, eig < 1] @ vectors[:, eig < 1].conj().T)
    tsel, rank = polar(q@p, tol)
    if rank == 0: return {'terminal': 'T_sel0'}
    psel = tsel@tsel.conj().T
    fsel = tsel@f@tsel.conj().T
    wun = tsel@w@tsel.conj().T
    mass = float(np.trace(wun).real)
    if mass <= 0: return {'terminal': 'T_w1'}
    wsel = wun/mass
    pe, pv = np.linalg.eigh(psel)
    z = pv[:, pe > .5]
    g = identity+y
    pg = z@np.linalg.solve(z.conj().T@g@z, z.conj().T@g)
    c = np.linalg.solve(g, identity); b = identity-c
    lc = float(np.trace(g@pg@c@fsel@c@pg.conj().T).real)
    lb = float(np.trace(g@pg@b@fsel@b@pg.conj().T).real)
    if lc <= 0 or lb <= 0: return {'terminal': 'T_load'}
    alpha = lb/(lc+lb); beta = lc/(lc+lb)
    a = np.vstack([np.sqrt(alpha)*pg@c, np.sqrt(beta)*pg@b])
    if frames is None:
        u, s, vh = np.linalg.svd(a, full_matrices=False)
        active = s > tol*max(1., s[0]); u=u[:, active]; s=s[active]; v=vh[active].conj().T
    else:
        u, s, v = frames
        if np.linalg.norm(a-u@np.diag(s)@v.conj().T) > 1e-9:
            raise ValueError('Incompatible supplied SVD frames')
    if not len(s): raise ArithmeticError('Positive loads but zero analysis rank')
    yn = np.diag(s*s)
    kk = np.zeros((2*n,2*n), dtype=k.dtype); kk[:n,:n]=k; kk[n:,n:]=k
    kn = u.conj().T@kk@u
    t4, _ = polar(v.conj().T@psel, tol)
    s4 = t4@t4.conj().T
    m4 = float(np.trace(t4@wsel@t4.conj().T).real)
    if abs(m4-1) > 1e-8: raise ArithmeticError(f'R4 mass failure {m4}')
    wn = t4@wsel@t4.conj().T/m4
    fn = t4@fsel@t4.conj().T
    e = np.eye(len(s))-s4
    ee, ev = np.linalg.eigh(e); ze=ev[:, ee>.5]
    pn=s4.copy()
    if ze.shape[1]:
        he=ze.conj().T@kn@ze; se, sv=np.linalg.eigh(he)
        if se[0]>=0: return {'terminal':'T_seednone'}
        if len(se)>1 and abs(se[1]-se[0]) <= tol*max(1.,np.linalg.norm(he,2)):
            return {'terminal':'T_seeddeg'}
        seedv=ze@sv[:,0]; seedp=np.outer(seedv,seedv.conj())
        fn=fn-se[0]*seedp; pn=pn+seedp
    return dict(terminal=None, k=kn, f=fn, w=wn, y=yn, p=pn,
                u=u, s=s, v=v, a=a, psel=psel, t4=t4,
                msel=mass, m4=m4, lc=lc, lb=lb, alpha=alpha)


def predict(f, scale, geometry=None, tol=1e-12):
    result=update(-scale*np.eye(8), f, f/np.trace(f),
                  f/scale if geometry is None else geometry, np.eye(8), tol)
    if result['terminal']: return None, result
    return (scale*result['v']@result['y']@result['v'].conj().T).real, result


def write_csv(path, rows):
    if not rows: raise ValueError(f'No rows for {path}')
    with path.open('w', newline='') as file:
        writer=csv.DictWriter(file, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)


def loss(pred, target):
    return float(np.linalg.norm(pred-target)/np.linalg.norm(target)), float(
        np.linalg.norm(np.linalg.eigvalsh(pred)-np.linalg.eigvalsh(target))/np.linalg.norm(np.linalg.eigvalsh(target)))


def evaluate():
    outdir=ROOT/'results'; outdir.mkdir(exist_ok=True)
    tri=np.triu_indices(8); allwindows=[]; pairs=[]; qc=[]; manifests=[]
    for subject in range(1,110):
        for run in (1,2):
            try:
                windows=features(subject,run)
                data=(ROOT/'raw'/f'S{subject:03d}R{run:02d}.edf').read_bytes()
                manifests.append(dict(subject=subject,run=run,file=f'S{subject:03d}R{run:02d}.edf',
                    url=f'https://physionet.org/files/eegmmidb/1.0.0/S{subject:03d}/S{subject:03d}R{run:02d}.edf',
                    bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
                qc.append(dict(subject=subject,run=run,status='loaded',windows=len(windows),
                               valid=sum(v for _,v,_ in windows),error=''))
                for start,valid,f in windows:
                    row=dict(subject=subject,run=run,start_seconds=start,valid=int(valid),split='development' if subject<=40 else 'holdout')
                    row.update({f'F_{i}_{j}':float(f[i,j]) for i,j in zip(*tri)})
                    allwindows.append(row)
                for (time, valid, f),(_,nextvalid,target) in zip(windows,windows[1:]):
                    if valid and nextvalid: pairs.append((subject,run,time,f,target))
            except (ValueError,OSError) as error:
                qc.append(dict(subject=subject,run=run,status='excluded',windows=0,valid=0,error=str(error)))
    complete={s for s in range(1,110) if sum(q['subject']==s and q['status']=='loaded' and q['valid']>1 for q in qc)==2}
    if sum(s<=40 for s in complete)<30 or sum(s>40 for s in complete)<50:
        write_csv(outdir/'qc.csv',qc); raise ValueError('Insufficient complete subjects for frozen protocol')
    devwindows=[np.array([row[f'F_{i}_{j}'] for i,j in zip(*tri)]) for row in allwindows if row['subject']<=40 and row['valid']]
    def unpack(v):
        a=np.zeros((8,8)); a[tri]=v; a[(tri[1],tri[0])]=v; return a
    devmat=np.array([unpack(v) for v in devwindows])
    scale=float(np.percentile(np.linalg.eigvalsh(devmat),95)); geometry=devmat.mean(axis=0)/scale
    train=[pair for pair in pairs if pair[0]<=40]
    design=np.array([np.r_[f[tri]/scale,1.] for _,_,_,f,_ in train])
    targets=np.array([target[tri]/scale for _,_,_,_,target in train])
    ridge=np.eye(37)*1e-3*len(train); ridge[-1,-1]=0
    coef=np.linalg.solve(design.T@design+ridge,design.T@targets)
    fitted=dict(scale=scale,geometry=geometry.tolist(),linear_coefficients=coef.tolist(),
                development_pairs=len(train),development_windows=len(devwindows))
    (outdir/'development_parameters.json').write_text(json.dumps(fitted,indent=2)+'\n')
    rows=[]
    for subject,run,time,f,target in pairs:
        if subject<=40: continue
        linear=unpack(np.r_[f[tri]/scale,1.]@coef)*scale
        eig,vec=np.linalg.eigh(linear); linear=(vec*np.maximum(eig,0))@vec.T
        bfg,r=predict(f,scale); frozen,fr=predict(f,scale,geometry)
        common=bfg is not None and frozen is not None
        sensitivity={}
        for tol in (1e-10,1e-14):
            other,orr=predict(f,scale,tol=tol)
            sensitivity[f'rank_{tol}']=len(orr['s']) if other is not None else -1
            sensitivity[f'terminal_{tol}']=orr['terminal'] or ''
        for model,pred,res in [('persistence',f,{}),('linear',linear,{}),('bfg',bfg,r),('frozen_geometry',frozen,fr)]:
            l,sl=loss(pred,target) if pred is not None else ('','')
            row=dict(subject=subject,run=run,start_seconds=time,model=model,common=int(common),
                terminal=res.get('terminal') or '',relative_frobenius=l,relative_spectrum=sl,
                dimension=len(res['s']) if pred is not None and 's' in res else 8,
                msel=res.get('msel',''),m4=res.get('m4',''))
            row.update(sensitivity); rows.append(row)
    write_csv(outdir/'windows.csv',allwindows); write_csv(outdir/'pairs.csv',rows)
    write_csv(outdir/'qc.csv',qc); write_csv(outdir/'data_manifest.csv',manifests)
    subjectrows=[]
    for scope in ('all','common'):
        for subject in range(41,110):
            for model in ('persistence','linear','bfg','frozen_geometry'):
                means=[]; spectra=[]; count=0
                for run in (1,2):
                    selected=[r for r in rows if r['subject']==subject and r['run']==run and r['model']==model
                              and r['relative_frobenius']!='' and (scope=='all' or r['common'])]
                    if selected:
                        means.append(np.mean([r['relative_frobenius'] for r in selected])); spectra.append(np.mean([r['relative_spectrum'] for r in selected])); count+=len(selected)
                if means: subjectrows.append(dict(subject=subject,model=model,scope=scope,runs=len(means),pairs=count,
                    relative_frobenius=float(np.mean(means)),relative_spectrum=float(np.mean(spectra))))
    write_csv(outdir/'subjects.csv',subjectrows)
    common_subjects=sorted({r['subject'] for r in subjectrows if r['scope']=='common' and r['model']=='bfg'})
    if len(common_subjects)<50: raise ValueError('Insufficient held-out subjects with common nonterminal pairs')
    matrix=np.array([[next(r['relative_frobenius'] for r in subjectrows if r['scope']=='common' and r['subject']==subject and r['model']==model)
                     for model in ('bfg','persistence','linear','frozen_geometry')] for subject in common_subjects])
    rng=np.random.default_rng(SEED); boot=matrix[rng.integers(0,len(matrix),size=(10000,len(matrix)))].mean(axis=1)
    summary=dict(seed=SEED,bootstrap_replicates=10000,heldout_subjects=len(matrix),eligible_holdout_pairs=len(rows)//4,
                 common_pairs=sum(r['common'] for r in rows)//4,models={},comparisons={},conditions={})
    for idx,model in enumerate(('bfg','persistence','linear','frozen_geometry')):
        mrows=[r for r in rows if r['model']==model]
        terminal=sum(bool(r['terminal']) for r in mrows)
        summary['models'][model]=dict(mean_relative_frobenius_common=float(matrix[:,idx].mean()),
            ci95=np.percentile(boot[:,idx],[2.5,97.5]).tolist(),terminal_pairs=terminal,coverage=1-terminal/len(mrows),
            all_available_subject_mean=float(np.mean([r['relative_frobenius'] for r in subjectrows if r['model']==model and r['scope']=='all'])))
        for run,label in ((1,'eyes_open'),(2,'eyes_closed')):
            runmeans=[np.mean([r['relative_frobenius'] for r in mrows if r['subject']==s and r['run']==run and r['common']])
                      for s in common_subjects if any(r['subject']==s and r['run']==run and r['common'] for r in mrows)]
            summary['conditions'].setdefault(label,{})[model]=float(np.mean(runmeans))
        if idx:
            delta=boot[:,0]-boot[:,idx]
            summary['comparisons'][model]=dict(bfg_minus_comparator=float((matrix[:,0]-matrix[:,idx]).mean()),
                ci95=np.percentile(delta,[2.5,97.5]).tolist())
    summary['rank_sensitivity_changed_pairs']=sum(
        r['model']=='bfg' and (r['rank_1e-10']!=r['rank_1e-14'] or r['terminal_1e-10']!=r['terminal_1e-14']) for r in rows)
    summary['practical_success']=bool(summary['models']['bfg']['coverage']>=.95 and all(v['ci95'][1]<0 for v in summary['comparisons'].values()))
    summary['environment']=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform())
    (outdir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('action',choices=['download','evaluate'])
    parser.add_argument('--first',type=int,default=1); parser.add_argument('--last',type=int,default=109)
    args=parser.parse_args()
    if args.action=='download':
        with ThreadPoolExecutor(max_workers=16) as pool:
            for rows in pool.map(download,range(args.first,args.last+1)):
                print('downloaded',rows[0]['subject'],flush=True)
    else: evaluate()


if __name__=='__main__': main()
