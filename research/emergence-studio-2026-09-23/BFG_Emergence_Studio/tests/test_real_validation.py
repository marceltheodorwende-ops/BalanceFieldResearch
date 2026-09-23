import numpy as np
import pytest

from bfg_studio import (
    BFGState,
    CarrierSchema,
    ValidatedCarrierAdapter,
    HeldoutValidationPlan,
    plan_fingerprint,
    run_heldout_carrier_validation,
)

class FixedDummyCarrier(ValidatedCarrierAdapter):
    def map_measurement_to_state(self,measurement,*,generation=0):
        x=np.asarray(measurement,dtype=float)
        n=len(x)
        D=x.astype(complex)
        D=D/max(np.linalg.norm(D),1e-12)
        K=np.diag(np.linspace(-1.0,1.0,n)).astype(complex)
        Y=np.diag(np.linspace(0.1,0.4,n)).astype(complex)
        R=np.eye(n,dtype=complex)
        return BFGState(D=D,K=K,Y=Y,R_C=R,generation=generation)

    def advance(self,previous,step,policy):
        return previous

def make_carrier():
    schema=CarrierSchema(
        name="fixed-test",
        domain="unit-test",
        description="fixed held-out test carrier",
        measurement_mapping={
            "D":"normalized measurement",
            "K":"fixed diagonal",
            "Y":"fixed positive diagonal",
            "R_C":"identity",
        },
        invariant_parameters={"fixed":True},
    )
    return FixedDummyCarrier(schema)

def test_validation_plan_rejects_overlapping_splits():
    carrier=make_carrier()
    plan=HeldoutValidationPlan(
        domain="x",
        dataset_name="d",
        target_statement="prospective test",
        calibration_indices=(0,1),
        heldout_indices=(1,2),
        null_model_name="null",
        primary_metric="metric",
        success_criterion="criterion",
        mapping_fingerprint=carrier.mapping_fingerprint,
    )
    with pytest.raises(ValueError):
        plan.validate()

def test_heldout_validation_preserves_mapping_fingerprint():
    carrier=make_carrier()
    plan=HeldoutValidationPlan(
        domain="x",
        dataset_name="d",
        target_statement="fixed mapping on held-out data",
        calibration_indices=(0,1),
        heldout_indices=(2,3),
        null_model_name="constant",
        primary_metric="success fraction",
        success_criterion="declared before held-out evaluation",
        mapping_fingerprint=carrier.mapping_fingerprint,
    )
    measurements=[
        np.array([1.0,0.5,0.2]),
        np.array([0.9,0.4,0.3]),
        np.array([0.8,0.6,0.1]),
        np.array([0.7,0.2,0.4]),
    ]
    def bfg_metric(states,indices):
        return sum(states[i]["mapping_valid"] for i in indices)/len(indices)
    def null_metric(measurements,indices):
        return 0.5

    result=run_heldout_carrier_validation(
        carrier,measurements,plan,null_metric,bfg_metric
    )
    assert result["mapping_fingerprint"]==carrier.mapping_fingerprint
    assert result["mapping_audit"]["all_valid"]
    assert len(result["plan_fingerprint"])==64
    assert result["interpretation_guard"]["natural_realization_established"] is False
