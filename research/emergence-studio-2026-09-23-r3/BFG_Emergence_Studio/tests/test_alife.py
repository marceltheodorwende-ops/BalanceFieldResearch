import numpy as np
from bfg_studio import (
    SelfOrganizationParameters,
    make_self_organizing_seed,
    simulate_self_organization,
    organization_metrics,
)

def test_self_organizing_seed_is_well_formed():
    p=SelfOrganizationParameters(node_count=16,persistent_rank=4)
    s=make_self_organizing_seed(seed=3,params=p)
    A=s.metadata["adjacency"]
    assert A.shape==(16,16)
    assert np.allclose(A,A.T)
    assert np.all(A>=0)
    assert np.allclose(np.diag(A),0)
    assert np.min(np.linalg.eigvalsh(s.Y)) >= -1e-9

def test_organization_metrics_bounded():
    p=SelfOrganizationParameters(node_count=16,persistent_rank=4)
    s=make_self_organizing_seed(seed=4,params=p)
    m=organization_metrics(s,p)
    assert 0 <= m["largest_component_fraction"] <= 1
    assert 0 <= m["viable_fraction"] <= 1
    assert 0 <= m["resource_entropy"] <= 1.0000001
    assert 0 <= m["maintenance_score"] <= 1.0000001

def test_self_organization_run_executes():
    p=SelfOrganizationParameters(node_count=14,persistent_rank=4)
    run=simulate_self_organization(seed=5,steps=3,params=p)
    assert len(run.states) >= 2
    assert len(run.steps) >= 1


def test_lineage_split_detection_on_reference_seed():
    from bfg_studio import cluster_lineage_events
    p=SelfOrganizationParameters(node_count=24,persistent_rank=6)
    run=simulate_self_organization(seed=1341550191,steps=18,params=p)
    events=cluster_lineage_events(run,p)
    assert any(e["event"]=="split_like" for e in events)
