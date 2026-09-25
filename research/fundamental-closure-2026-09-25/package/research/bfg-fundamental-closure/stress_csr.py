"""Deterministic stress audit for the BFG CSR research candidate.

This is not an empirical validation script. It probes numerical/category behavior of
the current finite completion rules.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from bfg_lab.fundamental_closure import (
    QuotientState,
    canonical_self_reclosure_step,
)


def dagger(a):
    return np.asarray(a).conj().T


def random_unitary(rng, n):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, _ = np.linalg.qr(z)
    return q


def random_state(rng, n, persistent_rank):
    def h(scale=1.0):
        z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        return scale*(z + dagger(z))/2

    D = 2.0*np.eye(n) + 0.2*h()
    C = 0.5*np.eye(n) + 0.1*h()
    A = 0.3*np.eye(n) + 0.1*h()
    d = rng.normal(size=n) + 1j*rng.normal(size=n)

    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    Y = dagger(z) @ z / n + 0.1*np.eye(n)

    U = random_unitary(rng, n)
    vals = np.r_[np.ones(persistent_rank), rng.uniform(0.05, 0.8, n-persistent_rank)]
    R = U @ np.diag(vals) @ dagger(U)
    P = U[:, :persistent_rank] @ dagger(U[:, :persistent_rank])

    return QuotientState(
        D_cap=D,
        coherence=C,
        emergence=A,
        d=d,
        Y=Y,
        R_C=R,
        P_per=P,
    )


def run_batch(seed=20260925, cases=1000, max_steps=10):
    rng = np.random.default_rng(seed)
    reasons = {}
    success_steps = []
    persistence_rank_increases = 0
    max_power_norm = 0.0

    for _ in range(cases):
        n = int(rng.integers(3, 7))
        p = int(rng.integers(1, min(3, n) + 1))
        state = random_state(rng, n, p)
        old_rank = int(np.linalg.matrix_rank(state.P_per, tol=1e-9))
        successful = 0
        reason = "max_steps"

        for _step in range(max_steps):
            out = canonical_self_reclosure_step(
                state,
                require_simple_negative_formation=False,
            )
            if out.terminal:
                reason = out.reason
                break

            successful += 1
            state = out.state
            new_rank = int(np.linalg.matrix_rank(state.P_per, tol=1e-9))
            if new_rank > old_rank:
                persistence_rank_increases += 1
            old_rank = new_rank

            for k in (1, 2, 5, 10):
                max_power_norm = max(
                    max_power_norm,
                    float(np.linalg.norm(np.linalg.matrix_power(state.R_C, k), 2)),
                )

        reasons[reason] = reasons.get(reason, 0) + 1
        success_steps.append(successful)

    return {
        "seed": seed,
        "cases": cases,
        "max_steps": max_steps,
        "terminal_or_boundary_counts": reasons,
        "mean_successful_steps": float(np.mean(success_steps)),
        "min_successful_steps": int(np.min(success_steps)),
        "max_successful_steps": int(np.max(success_steps)),
        "persistent_rank_increases": persistence_rank_increases,
        "max_observed_recursive_power_norm": max_power_norm,
        "runtime_stop_semantics_counts": {
            "numerical_unresolved": int(
                sum(v for k, v in reasons.items() if "ambiguity" in k)
            ),
            "exact_terminal_or_no_choice_failure": int(
                sum(v for k, v in reasons.items()
                    if "ambiguity" not in k and k != "max_steps")
            ),
            "step_limit": int(reasons.get("max_steps", 0)),
        },
        "status_note": (
            "Internal deterministic finite mathematical stress test only. "
            "Counts depend on the declared synthetic seed ensemble and are not "
            "empirical evidence. Numerical ambiguity is not exact terminality."
        ),
        "interpretation": {
            "numerical_rank_ambiguity": (
                "A nonzero analysis map fell below the declared floating rank "
                "threshold. This is numerical ambiguity, not exact mathematical "
                "termination."
            ),
            "dual_load_numerical_ambiguity": (
                "A positive legacy rank-one dual load fell below floating "
                "resolution. This is numerical ambiguity, not exact terminality."
            ),
            "rank_increase": (
                "Inherited-only CSR is designed not to fabricate persistence; "
                "therefore exact persistent rank increase is absent. R4 supports "
                "new persistent strata separately, so this is a restriction of CSR."
            ),
        },
    }


if __name__ == "__main__":
    result = run_batch()
    out = Path(__file__).with_name("CSR_STRESS_RESULTS.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
