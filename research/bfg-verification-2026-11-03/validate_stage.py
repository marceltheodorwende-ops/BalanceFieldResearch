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
origin=json.loads((root/'origin_bridge/results.json').read_text(encoding='utf-8'))
assert origin['status']=='PASS' and origin['primitive_identity_found_in_reviewed_origin_source']
assert origin['rank_one_protection_and_unnormalized_stationarity_unique_witness']
assert not origin['original_to_operator_representation_theorem_established']
assert not origin['new_physical_rule_adopted'] and not origin['event_rule_modified']
origin_sources=json.loads((root/'origin_bridge/SOURCES.json').read_text(encoding='utf-8'))
assert len(origin_sources['original_extractions'])==8
report['origin_representation_audit']='PASS; primitive identity/persistence credited; conditional stationary-witness theorem; origin representation remains unresolved'
profile=json.loads((root/'profile_identity/results.json').read_text(encoding='utf-8'))
assert profile['status']=='PASS'
assert profile['sharp_pure_fixture']['squared_Frobenius_distance']=='18/25'
assert not profile['historical_premise_enforcing_bridge_established']
assert not profile['new_physical_rule_adopted'] and not profile['event_rule_modified']
report['profile_identity_bridge']='PASS; exact equivalent alignment criteria and sharp gap bound; historical enforcing premise unresolved'
origin_subset=json.loads((root/'origin_subset/results.json').read_text(encoding='utf-8'))
assert origin_subset['status']=='PASS' and origin_subset['origin_subset_consistent']
assert origin_subset['exact_common_transport_identity'] and origin_subset['exact_seed_separation_identity']
assert [x['dimension'] for x in origin_subset['implementation_checks']]==[1,2]
assert not origin_subset['fundamental_origin_identification_derived']
assert not origin_subset['conditional_origin_rule_installed']
assert not origin_subset['new_physical_rule_adopted'] and not origin_subset['event_rule_modified']
report['origin_subset']='PASS; conditional root restriction consistent; transport/seed separation proved and checked; forcing origin premise unresolved'
initial_persistence=json.loads((root/'initial_persistence/results.json').read_text(encoding='utf-8'))
assert initial_persistence['status']=='PASS' and initial_persistence['containing_projectors_classified']
assert initial_persistence['example_minimal_ranks']==[1,2]
assert not initial_persistence['origin_support_criterion_derived_from_original_premises']
assert not initial_persistence['new_origin_support_rule_installed']
assert not initial_persistence['new_physical_rule_adopted'] and not initial_persistence['event_rule_modified']
report['initial_persistence']='PASS; containing and neutral-invariant minimal supports distinguished; same-input P dependence checked; origin criterion unresolved'
no_choice=json.loads((root/'origin_no_choice/results.json').read_text(encoding='utf-8'))
assert no_choice['status']=='PASS' and no_choice['support_ranks']==[1,2,3]
assert not no_choice['enumerated_packet_uniquely_selects_origin_support']
assert not no_choice['historical_all_axioms_independence_theorem']
assert not no_choice['new_origin_rule_installed']
assert not no_choice['new_physical_rule_adopted'] and not no_choice['event_rule_modified']
report['origin_no_choice']='PASS; stronger-packet relative support nonuniqueness and source no-tie-break boundary; full historical origin theorem not established'
joint=json.loads((root/'joint_initialization/results.json').read_text(encoding='utf-8'))
assert joint['status']=='PASS' and joint['noncommuting_kernel_fixture']
assert joint['fixed_raw_R_two_Ys_same_protected_line']
assert not joint['unique_joint_initializer_derived']
assert not joint['new_identification_or_origin_law_adopted'] and not joint['event_rule_modified']
report['joint_initialization']='PASS; exact joint positive-sector persistence criterion and conditional mode matching; neutral/raw-recursion origin premises unresolved'
raw=json.loads((root/'raw_recursion/results.json').read_text(encoding='utf-8'))
assert raw['status']=='PASS' and raw['raw_composition_defined_conditionally']
assert raw['neural_interface_reconstruction_given_complete_instantaneous_data']
assert not raw['unique_fundamental_initial_R_derived']
assert not raw['new_physical_rule_adopted'] and not raw['event_rule_modified']
raw_sources=json.loads((root/'raw_recursion/SOURCES.json').read_text(encoding='utf-8'))
assert len(raw_sources['newly_located_original_pdfs'])==3
report['raw_recursion']='PASS; original primitive-factor composition and conditional neural reconstruction credited; unique origin factors unresolved'
dependency=json.loads((root/'dependency_closure/results.json').read_text(encoding='utf-8'))
assert dependency['status']=='PASS' and dependency['node_count']==38
assert dependency['rule_count']==16 and dependency['scenario_count']==8
assert dependency['complete_event_closed_from_supplied_input']
assert not dependency['unique_origin_closed_from_reviewed_formation_packet']
assert not dependency['full_historical_impossibility_or_independence_theorem']
assert not dependency['new_physical_rule_adopted'] and not dependency['event_rule_modified']
report['dependency_closure']='PASS; guarded source-linked dependency ledger consolidated; complete event closed, unique origin not established from reviewed smaller packet'
plugin=json.loads((root/'plugin_synthesis/results.json').read_text(encoding='utf-8'))
assert plugin['status']=='PASS' and plugin['plugin_reference_inventory']==20
assert plugin['indexed_parts']==1728 and plugin['information_functional_complete_probe_rank']==4
assert plugin['field_derived_feedback_identity'] and plugin['triangle_triples_checked']==343
assert plugin['quotient_counterexample']['discounted_distance']=='1/5'
assert not plugin['unique_fundamental_initializer_derived']
assert not plugin['new_physical_rule_adopted'] and not plugin['event_rule_modified']
plugin_sources=json.loads((root/'plugin_synthesis/SOURCES.json').read_text(encoding='utf-8'))
assert len(plugin_sources['references'])==20
report['plugin_synthesis']='PASS; actual BFG-Engine corpus indexed; conditional scalar/operator bridges and quotient correction checked; unique origin not established'
local_info=json.loads((root/'local_information/results.json').read_text(encoding='utf-8'))
assert local_info['status']=='PASS' and len(local_info['exact_reconstruction_cases'])==6
assert all(x['exact_measurement_rank']==x['dimension']**2 for x in local_info['exact_reconstruction_cases'])
assert not local_info['source_origin_functional_values_derived']
assert not local_info['unique_fundamental_initializer_derived']
assert not local_info['new_physical_rule_adopted'] and not local_info['event_rule_modified']
report['local_information']='PASS; arbitrarily local conditional reconstruction and exact-balance implication; real/domain and conditioning limits checked'
origin_info=json.loads((root/'origin_information_domain/results.json').read_text(encoding='utf-8'))
assert origin_info['status']=='PASS' and origin_info['quadratic_measurement_rank']==4
assert origin_info['incompatible_count_augmented_rank']==5
assert origin_info['exact_fresh_minimum_projector_span_rank']==1
assert not origin_info['actual_origin_similarity_and_representation_derived']
assert not origin_info['unique_fundamental_initial_operator_derived']
assert not origin_info['new_physical_rule_adopted'] and not origin_info['event_rule_modified']
report['origin_information_domain']='PASS; source count formula verified, candidate quadratic bridge tested, exact-minimum versus perturbation domain distinguished'
bridge=json.loads((root/'configuration_hilbert_bridge/results.json').read_text(encoding='utf-8'))
assert bridge['status']=='PASS' and bridge['worked_packet']['configuration_dimension']==5
assert bridge['worked_packet']['unitary_transition'] and bridge['worked_packet']['full_count_quadratic_preserved']
assert bridge['positive_fixed_Gram_information_compatibility_fixture']
assert not bridge['source_origin_configuration_packet_derived']
assert not bridge['unique_fundamental_initializer_derived']
assert not bridge['new_physical_rule_adopted'] and not bridge['event_rule_modified']
report['configuration_hilbert_bridge']='PASS; explicit finite conditional representation and transition lift; Gram, quotient and operator-role compatibility limits checked'
future=json.loads((root/'future_identifiability/results.json').read_text(encoding='utf-8'))
assert future['status']=='PASS' and future['exhaustive_finite_models']==3984
assert future['independent_ordered_pair_checks']==62688
assert future['minimal_observable_model_unique_given_complete_behavior']
assert not future['full_balance_count_future_fixes_microscopic_model']
assert not future['tested_observations_equal_full_source_canonical_datum']
assert not future['new_physical_rule_adopted'] and not future['event_rule_modified']
report['future_identifiability']='PASS; finite predictive quotient exact and minimal; tested balance/count packet leaves underlying models nonunique'
canonical=json.loads((root/'joint_canonical_data/results.json').read_text(encoding='utf-8'))
assert canonical['status']=='PASS' and canonical['simultaneous_coordinate_change']['equivalent']
assert not canonical['same_individual_spectra_different_alignment']['equivalent']
assert canonical['nonzero_but_singular_intertwiner_space']['intertwiner_dimension']==1
assert not canonical['nonzero_but_singular_intertwiner_space']['equivalent']
assert not canonical['source_origin_joint_values_derived']
assert not canonical['new_physical_rule_adopted'] and not canonical['event_rule_modified']
report['joint_canonical_data']='PASS; exact joint-coordinate equivalence and alignment effects checked; input class distinguished from behavioral quotient and origin selection'
symmetry=json.loads((root/'source_symmetry/results.json').read_text(encoding='utf-8'))
assert symmetry['status']=='PASS' and symmetry['noncommuting_unique_class_fixture']
assert symmetry['commutant_dimensions']==dict(K=2,K_double=2,capacities=1,capacities_double=4)
assert [row['exact_rank'] for row in symmetry['event_checks']]==[1,2,2]
assert symmetry['matrix_covariance_theorem_not_applied_to_quotient_rules']
assert not symmetry['unique_source_initializer_derived']
assert not symmetry['full_historical_independence_theorem']
assert not symmetry['new_physical_rule_adopted'] and not symmetry['event_rule_modified']
report['source_symmetry']='PASS; matrix and quotient covariance distinguished; original capacity symmetry and exact event consequences checked; source constitutive initializer unresolved'
effective=json.loads((root/'effective_response/results.json').read_text(encoding='utf-8'))
assert effective['status']=='PASS' and effective['exact_response_inverse']
assert len(effective['quadratic_fixtures'])==5
assert [x['minimal_neutral_dimension'] for x in effective['quadratic_fixtures']]==[2,2,1,1,0]
assert effective['single_ground_probe_insufficient'] and effective['nested_Gram_realization_checks']==2
assert not effective['source_capacity_to_effective_response_derived']
assert not effective['physical_channel_uniqueness_required_for_finite_event']
assert not effective['new_physical_rule_adopted'] and not effective['event_rule_modified']
report['effective_response']='PASS; minimized assessment exactly identifies Y; minimal factor equivalence and role-sensitive source audit checked; source constitutive response unresolved'
functional=json.loads((root/'functional_hessian/results.json').read_text(encoding='utf-8'))
assert functional['status']=='PASS' and len(functional['nonlinear_local_reduction'])==2
assert functional['source_Lyapunov_specialization']['flat_source_direction']
assert functional['resolvent_derivative_identities'] and functional['residual_Gram_identity']
assert functional['positive_potential_negative_Hessian']=='-1/4'
assert not functional['accepted_source_functional_to_initial_E_derived']
assert not functional['local_Hessian_equals_full_nonlinear_law']
assert not functional['source_Gram_rule_replaced']
assert not functional['new_physical_rule_adopted'] and not functional['event_rule_modified']
report['functional_hessian']='PASS; conditional nonlinear Schur Hessian and source functional limits checked; no unsourced identification of local curvature with exact initial Y'
quotient=json.loads((root/'admissible_quotient/results.json').read_text(encoding='utf-8'))
assert quotient['status']=='PASS' and quotient['joint_unitary_classes_distinct']
assert quotient['flat_direction_survives_normalization_and_fixed_information']
assert [x['second_information_moment'] for x in quotient['normalized_fixed_information_family']]==['17/4','9/2']
assert quotient['quotient_positive_control']==[['1','0'],['0','4']]
assert quotient['quotient_singular_control']==[['1','0'],['0','0']]
assert not quotient['source_selects_initial_reduced_response']
assert not quotient['all_plugin_dynamics_and_origin_axioms_realized']
assert not quotient['equivalence_identified_with_full_nine_role_state']
assert not quotient['new_physical_rule_adopted'] and not quotient['event_rule_modified']
report['admissible_quotient']='PASS; residual-rank quotient criterion and normalized fixed-information nongauge flat family checked; complete source-domain initializer remains unresolved'
roles=json.loads((root/'role_information/results.json').read_text(encoding='utf-8'))
assert roles['status']=='PASS' and roles['exact_moment_reconstruction_cases']==48
assert roles['degenerate_eigenspace_unitary_certificate']
assert roles['two_mode_mean_information_fixes_pure_class']
assert roles['mixed_density_counterexample']['purity_a']=='1/3'
assert roles['mixed_density_counterexample']['purity_b']=='25/72'
assert not roles['source_fixes_those_moment_values']
assert not roles['complete_state_moments_alone_fix_initial_Y']
assert not roles['moments_determine_mixed_density_joint_class']
assert not roles['full_historical_independence_theorem']
assert not roles['new_physical_rule_adopted'] and not roles['event_rule_modified']
report['role_information']='PASS; complete pure-state moment diagnostic and conditional two-mode closure; mixed-state and source-response limits retained; role preservation separated from origin selection'
compatibility=json.loads((root/'recursion_compatibility/results.json').read_text(encoding='utf-8'))
assert compatibility['status']=='PASS' and compatibility['date']=='2026-11-04'
assert compatibility['phase_flip_control']['both_fixed'] and compatibility['phase_flip_control']['neutral_not_fixed']
assert compatibility['nonselfadjoint_control']['exact_event_rank']==2
assert compatibility['nonselfadjoint_control']['conjugate_eigenvalues']==['1','-9/25']
assert compatibility['sharp_commuting_bound_verified'] and compatibility['zero_load_boundary_verified']
assert not compatibility['canonical_comparison']['older_zero_cost']
assert not compatibility['source_neutral_identification_adopted']
assert not compatibility['raw_selfadjointness_assumed_universally']
assert not compatibility['new_physical_rule_adopted'] and not compatibility['event_rule_modified']
report['latest_followup_date']='2026-11-04'
report['recursion_compatibility']='PASS; dual fixed-point compatibility and sharp conditional cost/load bound; nonselfadjoint bounded exception and positive finite event checked; origin identifications remain unadopted'
initial_y=json.loads((root/'initial_y_closure/results.json').read_text(encoding='utf-8'))
assert initial_y['status']=='PASS' and initial_y['candidate_formula_computation_complete']
assert initial_y['source_status']=='EXISTING PROPOSAL; NOT ADOPTED'
assert [(x['mixed_clause'],x['metric_clause']) for x in initial_y['independent_clause_controls']]==[(True,True),(False,True),(True,False)]
assert initial_y['whole_carrier_selection_criterion_verified']
assert initial_y['rank_one_input']['alpha']=='625/9841'
assert initial_y['existing_scalar_boundary']['implementation_terminal']=='selection'
assert not initial_y['original_source_implication_of_mixed_and_metric_clauses_established']
assert not initial_y['proposal_adopted'] and not initial_y['new_physical_rule_adopted']
assert not initial_y['event_rule_modified']
report['initial_y_closure']='PASS; existing candidate computed exactly with strict domain and event checks; two source identifications remain proposed, not historically derived or adopted'
capacity_gram=json.loads((root/'capacity_gram/results.json').read_text(encoding='utf-8'))
assert capacity_gram['status']=='PASS' and capacity_gram['source_unitary_covariance']
assert all(x['same_Y'] for x in capacity_gram['neutral_coordinate_controls'])
assert [(x['capacity_rank'],x['Gamma_rank'],x['Y_rank']) for x in capacity_gram['rank_controls']]==[(0,0,0),(1,1,1),(2,2,2)]
assert capacity_gram['literal_composition_control']['coherence_rank']==1
assert capacity_gram['literal_composition_control']['target_rank']==2
assert capacity_gram['derivative_control']['same_point_constant_field_derivative_rank']==0
assert capacity_gram['derivative_control']['derivative_rank']==2
assert not capacity_gram['target_identity_derived_from_original_sources']
assert not capacity_gram['source_Dcov_typing_and_capacity_identification_resolved']
assert not capacity_gram['proposed_blocks_adopted'] and not capacity_gram['new_physical_rule_adopted']
assert not capacity_gram['event_rule_modified']
report['capacity_gram']='PASS; neutral-coordinate invariant target and rank checks; explicit source B_C relation retained; finite composition distinguished from field derivative; source implication unresolved'
engine_equation=json.loads((root/'engine_gram_equation/results.json').read_text(encoding='utf-8'))
assert engine_equation['status']=='PASS' and engine_equation['endomorphism_covariant_derivative_verified']
assert engine_equation['gauge_pullback_identity_verified'] and engine_equation['nonorthonormal_frame_identity_verified']
assert [x['nonnegative_weight_exists'] for x in engine_equation['inverse_Gram_cases']]==[True,True,True,True,False,True]
assert [x['positive_definite_weight_exists'] for x in engine_equation['inverse_Gram_cases']]==[True,True,True,True,False,False]
assert not engine_equation['metric_completion_is_source_derivation']
assert not engine_equation['full_initial_Y_derived_from_original_assumptions']
assert not engine_equation['reference_runtime_modified']
assert not engine_equation['new_physical_rule_adopted'] and not engine_equation['event_rule_modified']
engine_sources=json.loads((root/'engine_gram_equation/SOURCES.json').read_text(encoding='utf-8'))
assert engine_sources['plugin']['reference_count']==20
assert engine_sources['runtime_static_trace']['ast_parse']=='PASS'
report['engine_gram_equation']='PASS; BFG-Engine source inventory verified; typed gauge/coordinate independent equation and exact inverse-Gram feasibility proved and checked; constructed weight not adopted as source law'
(root/'STAGE_CHECK.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
manifest={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts}
(root/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
