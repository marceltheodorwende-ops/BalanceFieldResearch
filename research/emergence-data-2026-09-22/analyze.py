"""Recompute summaries of the author-supplied successful emergence cases."""
import csv
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
source = ROOT / 'bfg_emergence_mc.csv'
raw = source.read_bytes()
columns = 'spectral_novel commP commY ratio wk wu lamplus gapplus ampplus'.split()
with source.open(newline='', encoding='utf-8-sig') as handle:
    reader = csv.reader(handle)
    assert next(reader) == columns, 'Unexpected columns'
    rows = list(reader)
assert rows and all(len(row) == len(columns) for row in rows)
data = np.asarray(rows, dtype=float)
assert np.isfinite(data).all(), 'Nonfinite data'
x = dict(zip(columns, data.T))
observed = {
    'rows': len(data),
    'unique_numeric_rows': len(np.unique(data, axis=0)),
    'all_values_finite': bool(np.isfinite(data).all()),
    'stored_gate_passes': int(np.sum((x['lamplus'] < 0) & (x['gapplus'] > 0))),
    'positive_spectral_novelty_rows': int(np.sum(x['spectral_novel'] > 0)),
    'weight_sum_max_abs_error': float(np.max(np.abs(x['wk'] + x['wu'] - 1))),
    'amplitude_identity_max_abs_error': float(np.max(np.abs(x['ampplus'] - np.sqrt(np.maximum(0, -x['lamplus']))))),
    'spectral_novel_commP_pearson': float(np.corrcoef(x['spectral_novel'], x['commP'])[0, 1]),
    'column_statistics': {name: {'min': float(v.min()), 'median': float(np.median(v)), 'max': float(v.max())} for name, v in x.items()},
}
reconciliation = {
    'paper_reported_trials': 10000,
    'paper_reported_successes': 9993,
    'paper_reported_terminations': 7,
    'success_count_matches': observed['rows'] == 9993,
    'spectral_summary_matches_paper_rounding': [round(observed['column_statistics']['spectral_novel'][k], 4) for k in ('min', 'median', 'max')] == [0.0362, 0.2698, 0.8248],
    'correlation_matches_paper_rounding': round(observed['spectral_novel_commP_pearson'], 3) == 0.781,
    'failed_trials_present': False,
    'original_simulation_regenerated': False,
}
result = {'source': {'file': source.name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(), 'git_blob_sha1': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()}, 'observed': observed, 'paper_reconciliation': reconciliation}
target = ROOT / 'RESULTS.json'
target.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
