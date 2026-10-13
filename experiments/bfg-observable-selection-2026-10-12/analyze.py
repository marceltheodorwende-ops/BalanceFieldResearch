"""Frozen P78 angle-only necessary tests; attempt-1 whitelist only.
Run: python analyze.py --data-dir PATH. No downloads/holdout access.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--data-dir', type=Path, required=True)
args = parser.parse_args()
here = Path(__file__).resolve().parent
manifest = json.loads((here/'source_manifest.json').read_text())
allowed = {f'len{l}_cond{c}_1.csv' for l in range(1, 6) for c in range(1, 4)}
assert {Path(item['path']).name for item in manifest} == allowed
a = 16/135
results, audit = [], []


def best_reversal(q):
    n = len(q)
    pmin, pmax, smin, smax = [0]*n, [0]*n, [n-1]*n, [n-1]*n
    for i in range(1, n):
        pmin[i] = i if q[i] < q[pmin[i-1]] else pmin[i-1]
        pmax[i] = i if q[i] > q[pmax[i-1]] else pmax[i-1]
    for i in range(n-2, -1, -1):
        smin[i] = i if q[i] <= q[smin[i+1]] else smin[i+1]
        smax[i] = i if q[i] >= q[smax[i+1]] else smax[i+1]
    best = (-float('inf'), None, None)
    for j in range(1, n-1):
        i, k = pmin[j-1], smin[j+1]
        score = min(q[j]-q[i], q[j]-q[k])
        if score > best[0]:
            best = (score, 'peak', [i, j, k])
        i, k = pmax[j-1], smax[j+1]
        score = min(q[i]-q[j], q[k]-q[j])
        if score > best[0]:
            best = (score, 'trough', [i, j, k])
    return best


for item in manifest:
    name = Path(item['path']).name
    assert name in allowed and name.endswith('_1.csv')
    raw = (args.data_dir/name).read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert blob == item['git_blob_sha'], (name, 'source hash mismatch')
    rows = list(csv.DictReader(raw.decode().splitlines()))
    assert len(rows) == 6000
    q = np.array([float(row['angle']) for row in rows])
    t = np.array([float(row['time']) for row in rows])
    assert np.all(np.isfinite(q)) and np.all(np.isfinite(t)) and np.all(np.diff(t)>0)
    score, kind, triple = best_reversal(q)
    residual = q[1:]-a*q[:-1]
    imin, imax = int(np.argmin(residual)), int(np.argmax(residual))
    spread = float(residual[imax]-residual[imin])
    audit.append(dict(file=name, git_blob_sha=blob, sha256=hashlib.sha256(raw).hexdigest(),
                      rows=len(rows), source_commit=item['source_commit']))
    previous = {}
    for N in [2000, 4000]:
        for extra in [0., .0005, .002, .01]:
            error = np.pi/N+.0005+extra
            margin = float(score-2*error)
            fixed_margin = float(spread-2*(1+a)*error)
            if N in previous:
                assert margin <= previous[N]+1e-14
            previous[N] = margin
            results.append(dict(file=name, N=N, extra_angle_error=extra,
                                error_radius=float(error), reversal_kind=kind,
                                reversal_indices=triple, reversal_angles=[rows[i]['angle'] for i in triple],
                                reversal_score=float(score), reversal_margin=margin,
                                affine_positive_contraction_rejected=bool(margin>1e-9),
                                fixed_a_residual_min_index=imin, fixed_a_residual_max_index=imax,
                                fixed_a_residual_spread=spread, fixed_a_margin=fixed_margin,
                                fixed_a_rejected=bool(fixed_margin>1e-9)))
summary = dict(kind='reused_development_necessary_interface_test', files=len(audit),
               rows=sum(x['rows'] for x in audit), scenarios=len(results),
               affine_rejections=sum(x['affine_positive_contraction_rejected'] for x in results),
               fixed_a_rejections=sum(x['fixed_a_rejected'] for x in results),
               minimum_reversal_margin=min(x['reversal_margin'] for x in results),
               maximum_reversal_margin=max(x['reversal_margin'] for x in results),
               independent_confirmation=False, physical_calibration=False,
               canonical_event_alignment_assumed=True, holdout_accessed=False)
for name, value in [('record_results.json', results), ('data_audit.json', audit), ('summary.json', summary)]:
    (here/name).write_text(json.dumps(value, indent=2)+'\n')
print(json.dumps(summary, indent=2))
