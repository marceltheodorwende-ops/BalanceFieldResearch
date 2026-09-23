import json
from pathlib import Path
import pytest

from bfg_studio import (
    ValidationPortfolio,
    BlindHeldoutGuard,
    CONFIRMATION_ACK,
    STATUS_READY,
    STATUS_REJECTED,
)

def make_ready_portfolio(tmp_path):
    prepared=tmp_path/"outputs"/"carrier"
    prepared.mkdir(parents=True)
    (prepared/"ready.json").write_text('{"ready":true}')
    (prepared/"frozen.json").write_text('{"frozen":true}')
    (prepared/"plan.json").write_text('{"plan":true}')

    registry={
        "empirical_benchmarks":[{
            "id":"test-carrier",
            "name":"Test Carrier",
            "domain":"test domain",
            "status":"READY_FOR_VALIDATION",
            "mapping_fingerprint":"a"*64,
            "plan_fingerprint":"b"*64,
            "heldout_metrics_evaluated":False,
            "prepared_dir":"outputs/carrier",
            "readiness_token":"outputs/carrier/ready.json",
            "frozen_model":"outputs/carrier/frozen.json",
            "validation_plan":"outputs/carrier/plan.json",
            "result_artifact":None,
            "retuning_after_heldout":False,
        }]
    }
    reg=tmp_path/"EMPIRICAL_BENCHMARK_REGISTRY.json"
    reg.write_text(json.dumps(registry))
    return ValidationPortfolio(project_root=tmp_path,registry_path=reg)

def test_ready_portfolio_audits_without_opening_heldout(tmp_path):
    portfolio=make_ready_portfolio(tmp_path)
    assert portfolio.get("test-carrier").status==STATUS_READY
    audit=portfolio.audit()
    assert audit["valid"]
    assert audit["carrier_count"]==1

def test_seal_detects_artifact_drift(tmp_path):
    portfolio=make_ready_portfolio(tmp_path)
    guard=BlindHeldoutGuard(portfolio)
    guard.build_seal("test-carrier")
    assert guard.audit_seal("test-carrier")["valid"]

    (tmp_path/"outputs/carrier/plan.json").write_text('{"plan":"changed"}')
    audit=guard.audit_seal("test-carrier")
    assert not audit["valid"]
    assert not audit["checks"]["validation_plan_unchanged"]

def test_confirmation_permit_is_explicit_and_one_time(tmp_path):
    portfolio=make_ready_portfolio(tmp_path)
    guard=BlindHeldoutGuard(portfolio)
    guard.build_seal("test-carrier")

    with pytest.raises(ValueError):
        guard.issue_confirmation_permit("test-carrier","yes")

    permit=guard.issue_confirmation_permit(
        "test-carrier",CONFIRMATION_ACK
    )
    assert guard.validate_confirmation_permit(
        "test-carrier",permit
    )["valid"]

    consumed=guard.consume_confirmation_permit(
        "test-carrier",permit
    )
    assert consumed["consumed"]
    with pytest.raises(RuntimeError):
        guard.validate_confirmation_permit("test-carrier",permit)

def test_terminal_portfolio_result_cannot_transition_back(tmp_path):
    portfolio=make_ready_portfolio(tmp_path)
    entry=portfolio.record_confirmatory_result(
        "test-carrier",
        passed=False,
        result_artifact="outputs/carrier/result.json",
        metrics={"score":0.0},
    )
    assert entry.status==STATUS_REJECTED

    refreshed=ValidationPortfolio(
        project_root=tmp_path,
        registry_path=tmp_path/"EMPIRICAL_BENCHMARK_REGISTRY.json",
    )
    with pytest.raises(RuntimeError):
        refreshed.record_confirmatory_result(
            "test-carrier",
            passed=True,
            result_artifact="outputs/carrier/other.json",
        )


def test_portfolio_report_exposes_guard_status(tmp_path):
    from bfg_studio import write_portfolio_report
    portfolio=make_ready_portfolio(tmp_path)
    guard=BlindHeldoutGuard(portfolio)
    guard.build_seal("test-carrier")
    files=write_portfolio_report(portfolio,tmp_path/"validation-report")
    payload=json.loads(Path(files["json"]).read_text())
    assert payload["confirmation_guard"]["test-carrier"]["valid"] is True
