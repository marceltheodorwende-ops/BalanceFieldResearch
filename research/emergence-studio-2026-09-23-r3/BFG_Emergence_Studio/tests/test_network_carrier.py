from bfg_studio import (
    KarateInteractionCarrier,
    load_weighted_karate_graph,
    run_karate_network_audit,
)
from bfg_studio.carrier_sdk import validate_state_contract

def test_weighted_karate_snapshot_shape_and_mapping_contract():
    A=load_weighted_karate_graph()
    assert A.shape==(34,34)
    assert (A.T==A).all()
    assert int((A>0).sum()/2)==78

    carrier=KarateInteractionCarrier()
    measurements=carrier.measurements()
    assert len(measurements)==34
    for i,m in enumerate(measurements):
        state=carrier.map_measurement_to_state(m,generation=i)
        report=validate_state_contract(state)
        assert report.valid
        assert state.metadata["club_label_used"] is False

def test_real_relational_network_audit_preserves_negative_and_positive_results():
    result=run_karate_network_audit(recursive_horizon=4)
    assert result["heldout_metrics_evaluated"] is False
    assert result["confirmatory_plan_defined"] is False
    assert result["status"]=="EXPLORATORY_REAL_RELATIONAL_CARRIER"
    assert result["state_contract_valid"]==34
    assert result["first_step_successes"]==13
    assert result["first_step_failure_reasons"]=={
        "formation gate failed: no simple negative lowest eigenvalue":21
    }
    assert result["small_load"]["all_bounds_verified"]
    assert result["small_load"]["bound_passed"]==41
    assert result["permutation_equivariance"]["equivariant"]
    assert all(
        not row["shared_four_domain"]
        for row in result["four_domain_transform_corridors"]
    )
    assert all(
        not row["shared_four_domain"]
        for row in result["four_domain_formation_corridors"]
    )
