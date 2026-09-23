from bfg_studio import run_github_math_integration_audit

def test_github_math_integration_audit_passes():
    result=run_github_math_integration_audit()
    assert result["audit_passed"]
    assert all(result["checks"].values())
    assert result["claim_register"]["g1"].startswith("conditional")
    assert result["claim_register"]["finite_reduced_master_closure"].startswith("CLOSED")
    assert result["claim_register"]["bounded_infinite_entry_class"].startswith("CLOSED")
    assert result["claim_register"]["historical_internal_uniqueness"].startswith("not required")
