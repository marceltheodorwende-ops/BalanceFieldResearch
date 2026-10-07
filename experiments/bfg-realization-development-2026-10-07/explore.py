"""Development-only diagnostic; no holdout downloader or confirmatory claims."""
import csv, hashlib, json, math, re, statistics, sys
from pathlib import Path

LENGTHS = [.236, .330, .426, .518, .607]

def allowed(name):
    return re.fullmatch(r'len[1-5]_cond[1-3]_1.csv', name) is not None

def scalar(y):
    if not 0 < y < 1:
        return None
    return 2*y*y / ((1+y)**2*(1+y*y))

def energy(theta, length):
    return 9.799*length*2*math.sin(theta/2)**2

def pairs(rows, length):
    peaks = [r for r in rows if r['is_peak'] == '1']
    result, rejected = [], 0
    for p, q in zip(peaks, peaks[1:]):
        t, u, a, b, w, v = [float(x) for x in (p['time'], q['time'], p['angle'], q['angle'], p['angular_velocity'], q['angular_velocity'])]
        if not all(map(math.isfinite, [t,u,a,b,w,v])) or u <= t or a*b >= 0 or min(abs(a),abs(b)) < .01:
            rejected += 1
            continue
        e, z = energy(a,length), energy(b,length)
        result.append(dict(time=t,dt=u-t,angle=a,next_angle=b,velocity=w,next_velocity=v,E=e,target=z,kinetic_fraction=(length*w)**2/(2*e)))
    return result, rejected, len(peaks)

def loss(xs, model):
    ys = [(model(p),p['target']) for p in xs]
    good = [(a,b) for a,b in ys if a is not None]
    return (math.sqrt(sum((a-b)**2 for a,b in good)/sum(b*b for _,b in good)) if good else None),len(good)/len(xs)

def write_csv(path, rows):
    if not rows: raise ValueError('empty output')
    with path.open('w', newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)

def main(root):
    root=Path(root); out=root/'results';out.mkdir(exist_ok=True)
    observed={x.name for x in (root/'data').glob('*.csv')}
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if observed != expected: raise ValueError('development-only allowlist mismatch; no holdout permitted')
    manifest=json.loads((root/'source_manifest.json').read_text()); datasets=[]; provenance=[]
    for entry in manifest:
        name=Path(entry['path']).name
        if not allowed(name): raise ValueError('holdout forbidden')
        raw=(root/'data'/name).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if blob != entry['git_blob_sha']: raise ValueError('source bytes differ: '+name)
        provenance.append({**entry,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
        rows=list(csv.DictReader(raw.decode().splitlines()))
        if set(rows[0]) != {'time','angle','angular_velocity','is_peak'}: raise ValueError('schema')
        if any(r['is_peak'] not in {'0','1'} for r in rows): raise ValueError('peak annotation')
        length=LENGTHS[int(name[3])-1]; ps,rejected,np=pairs(rows,length)
        datasets.append((name,ps,rejected,np))
    s=1.1*max(max(p['E'],p['target']) for _,ps,_,_ in datasets for p in ps)
    recordings=[]; allpairs=[]; stresses=[]
    for name,ps,rejected,np in datasets:
        if len(ps)<5: raise ValueError('insufficient development pairs '+name)
        # Development descriptive rivals, fitted and scored on the same pairs.
        a=max(0,min(1,sum(p['E']*p['target'] for p in ps)/sum(p['E']**2 for p in ps)))
        low=[p for p in ps if max(abs(p['angle']),abs(p['next_angle']))<=.2]
        rec=dict(recording=name,pairs=len(ps),rejected_pairs=rejected,annotated_peaks=np,
                 persistence_error=loss(ps,lambda p:p['E'])[0],
                 fitted_decay_error=loss(ps,lambda p:a*p['E'])[0],fitted_a=a,
                 bfg_error=loss(ps,lambda p:s*scalar(p['E']/s))[0],
                 low_amplitude_pairs=len(low),mean_dt=statistics.mean(p['dt'] for p in ps),
                 median_kinetic_fraction=statistics.median(p['kinetic_fraction'] for p in ps))
        recordings.append(rec)
        for factor in [.1,.5,1,2,10]:
            scale=s*factor
            def predictor(p):
                value=scalar(p['E']/scale)
                return None if value is None else scale*value
            error,coverage=loss(ps,predictor)
            stresses.append(dict(recording=name,scale_factor=factor,error_on_valid=error,coverage=coverage))
        for p in ps:
            pred=s*scalar(p['E']/s)
            allpairs.append(dict(recording=name,**p,bfg_prediction=pred,persistence_prediction=p['E'],fitted_decay_prediction=a*p['E'],bfg_ratio=pred/p['E'],observed_ratio=p['target']/p['E']))
    low=[p for p in allpairs if max(abs(p['angle']),abs(p['next_angle']))<=.2]
    summary=dict(stage='exploratory; development only; in-sample rival fit',recordings=len(recordings),pairs=len(allpairs),holdout_files_accessed=0,scale_J_per_kg=s,
                 mean_record_errors={k:statistics.mean(r[k] for r in recordings) for k in ['bfg_error','persistence_error','fitted_decay_error']},
                 low_amplitude_pairs=len(low),low_amplitude_median_observed_ratio=statistics.median(p['observed_ratio'] for p in low) if low else None,
                 low_amplitude_median_bfg_ratio=statistics.median(p['bfg_ratio'] for p in low) if low else None,
                 median_kinetic_fraction=statistics.median(p['kinetic_fraction'] for p in allpairs),
                 rejected_pairs=sum(r['rejected_pairs'] for r in recordings),
                 confirmatory_ready=False,limitations=['Carrier map and clock are added hypotheses','No causal intervention identification','Peak annotations use future samples','Rival is fit and scored in-sample','No population uncertainty or holdout inference'])
    write_csv(out/'pairs.csv',allpairs);write_csv(out/'recordings.csv',recordings);write_csv(out/'scale_stress.csv',stresses)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main(sys.argv[1] if len(sys.argv)>1 else '.')
