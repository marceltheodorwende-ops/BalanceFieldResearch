import numpy as np
import pytest

from bfg_studio import (
    BFGState,
    NumericalPolicy,
    ProvenanceManifest,
    save_bfg_checkpoint,
    load_bfg_checkpoint,
    CarrierSchema,
    ValidatedCarrierAdapter,
    validate_state_contract,
    no_retuning_comparison,
    make_commuting_control_state,
)

def test_checkpoint_roundtrip(tmp_path):
    state=make_commuting_control_state(dim=5,persistent_rank=3,seed=12)
    state.metadata["nested"]={"array":np.array([1.0,2.0])}
    manifest=ProvenanceManifest.build(
        experiment="test_checkpoint",seed=12,parameters={"x":1}
    )
    save_bfg_checkpoint(state,tmp_path,"s",manifest=manifest,extra={"hello":"world"})
    loaded,m,extra=load_bfg_checkpoint(tmp_path,"s")
    assert loaded.generation==state.generation
    assert np.allclose(loaded.D,state.D)
    assert np.allclose(loaded.K,state.K)
    assert np.allclose(loaded.Y,state.Y)
    assert np.allclose(loaded.R_C,state.R_C)
    assert np.allclose(loaded.metadata["nested"]["array"],np.array([1.0,2.0]))
    assert extra["hello"]=="world"
    assert m["source_fingerprint"]

def test_checkpoint_hash_detects_corruption(tmp_path):
    state=make_commuting_control_state(dim=4,persistent_rank=2,seed=3)
    save_bfg_checkpoint(state,tmp_path,"s")
    arrays=tmp_path/"s_arrays.npz"
    data=bytearray(arrays.read_bytes())
    data[-1]=(data[-1]+1)%255
    arrays.write_bytes(bytes(data))
    with pytest.raises(ValueError):
        load_bfg_checkpoint(tmp_path,"s",verify_hash=True)

def test_state_contract_accepts_valid_state():
    state=make_commuting_control_state(dim=5,persistent_rank=3,seed=12)
    report=validate_state_contract(state)
    assert report.valid
    assert all(report.checks.values())

class DummyCarrier(ValidatedCarrierAdapter):
    def map_measurement_to_state(self,measurement,*,generation=0):
        n=3
        D=np.asarray(measurement,dtype=complex)
        K=np.diag([-1.0,0.5,1.0]).astype(complex)
        Y=np.diag([0.1,0.2,0.3]).astype(complex)
        R=np.eye(n,dtype=complex)
        return BFGState(D=D,K=K,Y=Y,R_C=R,generation=generation)

    def advance(self,previous,step,policy):
        return previous

def test_carrier_sdk_fixed_mapping_contract():
    schema=CarrierSchema(
        name="dummy",
        domain="test",
        description="test mapping",
        measurement_mapping={
            "D":"measurement",
            "K":"fixed diagonal",
            "Y":"fixed positive diagonal",
            "R_C":"identity",
        },
        invariant_parameters={"a":1},
    )
    carrier=DummyCarrier(schema)
    audit=no_retuning_comparison(
        carrier,
        [np.array([1,0,0]),np.array([0,1,0])],
    )
    assert audit["all_valid"]
    assert len(audit["mapping_fingerprint"])==64
