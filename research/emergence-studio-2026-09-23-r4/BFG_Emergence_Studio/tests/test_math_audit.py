from bfg_studio import run_integrated_math_audit

def test_integrated_math_audit_passes():
    result=run_integrated_math_audit()
    assert result["audit_passed"]
    assert all(result["checks"].values())
    assert result["claim_register"]["g1"].startswith("conditional")
    assert result["claim_register"]["finite_reduced_master_closure"].startswith("CLOSED")
    assert result["claim_register"]["bounded_infinite_entry_class"].startswith("CLOSED")
    assert result["claim_register"]["historical_internal_uniqueness"].startswith("not required")
