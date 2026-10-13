"""Frozen P79 full-record alternating certificates; attempt-1 whitelist only."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np


def alternating_chain(q, threshold):
    if len(q)<2:
        return list(range(len(q)))
    low, high, direction, start = 0, 0, 0, None
    for i in range(1, len(q)):
        if q[i]-q[low] > threshold:
            chain, direction, extreme, start = [low], 1, i, i+1
            break
        if q[high]-q[i] > threshold:
            chain, direction, extreme, start = [high], -1, i, i+1
            break
        if q[i] < q[low]:
            low = i
        if q[i] > q[high]:
            high = i
    if not direction:
        return [0]
    for i in range(start, len(q)):
        if direction>0:
            if q[i] >= q[extreme]:
                extreme = i
            elif q[extreme]-q[i] > threshold:
                chain.append(extreme)
                direction, extreme = -1, i
        else:
            if q[i] <= q[extreme]:
                extreme = i
            elif q[i]-q[extreme] > threshold:
                chain.append(extreme)
                direction, extreme = 1, i
    chain.append(extreme)
    return chain


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    manifest = json.loads((here/'source_manifest.json').read_text())
    allowed = {f'len{l}_cond{c}_1.csv' for l in range(1, 6) for c in range(1, 4)}
    assert {Path(item['path']).name for item in manifest} == allowed
    audit, results = [], []
    loga = np.log(16/135)
    for item in manifest:
        name = Path(item['path']).name
        assert name in allowed
        raw = (args.data_dir/name).read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert blob == item['git_blob_sha'], name
        rows = list(csv.DictReader(raw.decode().splitlines()))
        assert len(rows)==6000
        q = np.array([float(row['angle']) for row in rows])
        t = np.array([float(row['time']) for row in rows])
        assert np.all(np.isfinite(q)) and np.all(np.isfinite(t)) and np.all(np.diff(t)>0)
        audit.append(dict(file=name,rows=len(rows),git_blob_sha=blob,
                          sha256=hashlib.sha256(raw).hexdigest(),source_commit=item['source_commit']))
        for N in [2000, 4000]:
            for extra in [0., .0005, .002, .01]:
                error = np.pi/N+.0005+extra
                chain = alternating_chain(q, 2*error+1e-9)
                diffs = np.diff(q[chain])
                assert all(chain[i]<chain[i+1] for i in range(len(chain)-1))
                assert np.all(np.abs(diffs)>2*error+1e-9)
                assert np.all(diffs[1:]*diffs[:-1]<0)
                candidates = []
                for i,j in zip(chain,chain[1:]):
                    numerator = abs(q[j]-q[i])-2*error
                    conservative = (np.log(numerator)-i*loga)/np.log(10)
                    exact_rows = conservative-np.log1p(-np.exp((j-i)*loga))/np.log(10)
                    candidates.append((float(exact_rows), float(conservative), i, j))
                strongest = max(candidates) if candidates else (None,None,None,None)
                results.append(dict(file=name,N=N,extra_angle_error=extra,error_radius=float(error),
                                    chain_indices=chain,chain_angles=[rows[i]['angle'] for i in chain],
                                    certified_chain_length=len(chain),
                                    polynomial_degree_lower_bound=max(0,len(chain)-1),
                                    rational_degree_sum_lower_bound=max(0,len(chain)-1),
                                    minimum_chain_margin=float(min(np.abs(diffs)-2*error)) if len(diffs) else None,
                                    log10_LR_lower_bound_one_event_per_row=strongest[0],
                                    log10_LR_lower_bound_forward_skips=strongest[1],
                                    sensitivity_edge=list(strongest[2:]),
                                    sensitivity_edge_angles=[rows[i]['angle'] for i in strongest[2:]] if candidates else []))
    bounds = [r['polynomial_degree_lower_bound'] for r in results]
    costs = [r['log10_LR_lower_bound_one_event_per_row'] for r in results if r['log10_LR_lower_bound_one_event_per_row'] is not None]
    summary = dict(kind='conditional_reused_development_complexity_certificates',files=len(audit),
                   rows=sum(r['rows'] for r in audit),scenarios=len(results),
                   minimum_certified_polynomial_degree=min(bounds),
                   maximum_certified_polynomial_degree=max(bounds),
                   minimum_log10_LR_cost_specific_a=min(costs),maximum_log10_LR_cost_specific_a=max(costs),
                   optimal_chains_claimed=False,model_fitted=False,independent_confirmation=False,
                   physical_calibration=False,holdout_accessed=False)
    for name,value in [('record_results.json',results),('data_audit.json',audit),('summary.json',summary)]:
        (here/name).write_text(json.dumps(value,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
