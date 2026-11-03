"""Validate recorded research artifacts; does not rerun expensive controls."""
from pathlib import Path
import json,hashlib,csv,re
root=Path(__file__).resolve().parent
claims=json.loads((root/'claims.json').read_text(encoding='utf-8'))
assert len(claims)==48
assert len({row['id'] for row in claims})==48
assert all(row['number'] and row['page'] for row in claims)
assert sum(row['review_status'].startswith('Focused') for row in claims)==7
assert all(row['source_statement_latex'] for row in claims)
assert all(row['source_proof_latex'] for row in claims if row['review_status'].startswith('Focused'))
results={name:json.loads((root/name).read_text(encoding='utf-8')) for name in ['scalar_results.json','rc_pilot_results.json','baseline/extended_verification.json']}
assert all(value['status']=='PASS' for value in results.values())
assert results['scalar_results.json']['exact_steps']==816
assert results['rc_pilot_results.json']['hardware_run'] is False
assert results['rc_pilot_results.json']['tolerance_cases']==1000
with (root/'synthetic_fixed_time_trace.csv').open(encoding='utf-8') as stream:
    trace=list(csv.DictReader(stream))
assert len(trace)==501
assert trace[0]['time_seconds']=='0.0' and trace[-1]['time_seconds']=='5.0'
source=json.loads((root/'SOURCE.json').read_text(encoding='utf-8'))
assert hashlib.sha256((root/'reference_main.tex').read_bytes()).hexdigest()==source['source_sha256']
for path in root.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        if target.startswith(('https://','../../papers/','../../completion-boundary-2026-09-29/','../../level0-neutral-capacity-source-law-2026-09-30/')):continue
        assert (path.parent/target).exists(),(path,target)
report={'status':'PASS','date':'2026-11-03','claim_entries':len(claims),'focused_analytic_reviews':7,'other_entries_detailed_review':'PENDING','exact_scalar_steps':816,'synthetic_trace_rows':len(trace),'baseline_replay':'PASS','formal_proof_assistant':'NOT EXECUTED','hardware':'NOT EXECUTED','published_pdf_modified':False,'scope':'Artifact consistency and recorded controls; not external review or a proof of every manuscript claim'}
foundation=json.loads((root/'foundation_audit/results.json').read_text(encoding='utf-8'))
assert foundation['status']=='PASS' and not foundation['new_physical_rules_adopted']
report['foundation_audit']='PASS; relative nonuniqueness, not a full historical independence theorem'
(root/'STAGE_CHECK.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
manifest={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts}
(root/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
