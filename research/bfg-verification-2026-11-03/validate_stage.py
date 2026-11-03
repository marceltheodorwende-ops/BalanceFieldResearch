"""Validate recorded research artifacts; does not rerun expensive controls."""
from pathlib import Path
import json,hashlib,csv,re,posixpath
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
        if target.startswith(('../../proof-chain-audit-2026-09-26/','../../fundamental-closure-2026-09-25/')):
            sources=json.loads((root/'foundation_audit/crosswalk_sources.json').read_text(encoding='utf-8'))
            repo_path=posixpath.normpath('research/bfg-verification-2026-11-03/'+path.relative_to(root).parent.as_posix()+'/'+target)
            known={row['path'] for row in sources['source_documents']}
            known.add('research/fundamental-closure-2026-09-25/review/SOURCE_SEARCH.md')
            assert repo_path in known,repo_path
            continue
        assert (path.parent/target).exists(),(path,target)
report={'status':'PASS','date':'2026-11-03','claim_entries':len(claims),'focused_analytic_reviews':7,'other_entries_detailed_review':'PENDING','exact_scalar_steps':816,'synthetic_trace_rows':len(trace),'baseline_replay':'PASS','formal_proof_assistant':'NOT EXECUTED','hardware':'NOT EXECUTED','published_pdf_modified':False,'scope':'Artifact consistency and recorded controls; not external review or a proof of every manuscript claim'}
foundation=json.loads((root/'foundation_audit/results.json').read_text(encoding='utf-8'))
assert foundation['status']=='PASS' and not foundation['new_physical_rules_adopted']
report['foundation_audit']='PASS; relative nonuniqueness, not a full historical independence theorem'
crosswalk=json.loads((root/'foundation_audit/crosswalk_results.json').read_text(encoding='utf-8'))
assert crosswalk['status']=='PASS' and not crosswalk['previous_countermodel']['refutes_conditional_derivation']
assert crosswalk['rectangular_complex_channel']['active_SVD_Gram_identity']
assert not crosswalk['new_physical_rules_adopted']
report['existing_derivation_crosswalk']='PASS; earlier conditional derivation retained, weaker-packet witness excluded by its full premises'
interface=json.loads((root/'foundation_audit/interface_results.json').read_text(encoding='utf-8'))
assert interface['status']=='PASS' and not interface['new_physical_rule_adopted']
assert interface['same_source_and_intrinsic_neutral_metric']['not_coordinate_equivalent_as_metric_channel_pairs']
assert not interface['proposed_L0_NC']['adopted_by_this_audit']
report['interface_identification']='PASS; quadratic-class classification and coordinate-invariance distinction; full historical necessity unresolved'
premise=json.loads((root/'foundation_audit/premise_candidate_results.json').read_text(encoding='utf-8'))
inventory=json.loads((root/'foundation_audit/premise_source_inventory.json').read_text(encoding='utf-8'))
assert premise['status']=='PASS' and not premise['new_physical_rules_adopted']
assert not premise['original_Gram_rule_changed'] and not premise['L0_NC_adopted']
assert len(inventory['sources'])==10 and all(r['status']=='EXTRACTED' for r in inventory['sources'])
report['existing_premise_search']='Ten original documents screened; exact relative witnesses PASS; no universal absence theorem claimed'
dependence=json.loads((root/'coupling_independence/results.json').read_text(encoding='utf-8'))
register=json.loads((root/'coupling_independence/dependence_register.json').read_text(encoding='utf-8'))
assert dependence['status']=='PASS' and dependence['fixed_event_rule'] and not dependence['new_law_adopted']
assert len(register)==48 and {r['id'] for r in register}=={r['id'] for r in claims}
assert dependence['carrier_and_seed_pair']['eventual_dimensions']==[1,2]
assert dependence['kernel_limit_pair']['first_Schur_factor_squared_exact']=='132496/155221'
report['coupling_independence']='Three steps completed: dependency register, conditional uniform theorem and exact dependence witnesses; controls PASS'
initial=json.loads((root/'initial_state_audit/results.json').read_text(encoding='utf-8'))
assert initial['status']=='PASS' and initial['same_Y_interface_representation']['successors_agree']
assert not initial['omit_Y_witness']['same_complete_state']
assert not initial['event_rule_modified'] and not initial['new_fundamental_input_added']
report['initial_state_contract']='PASS; complete finite state already contains Y, initializer reconstruction remains distinct; numeric policy witness recorded'
formation=json.loads((root/'formation_initialization/results.json').read_text(encoding='utf-8'))
assert formation['status']=='PASS' and formation['witness_unique_given_same_rank_one_support']
assert not formation['complete_initializer_derived'] and not formation['new_physical_rule_adopted']
assert not formation['event_rule_modified']
report['formation_initialization']='PASS; fresh ground-state density derived; origin witness and persistence conditional; complete initializer unresolved'
(root/'STAGE_CHECK.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
manifest={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts}
(root/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
