"""Deterministic stress audit for the official BFG finite update candidate.

This is an internal mathematical/numerical stress test, not empirical validation.
It exercises the current Selection-first living candidate and reports exact terminal
reasons separately from numerical ambiguity.
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
    UniversalOperatorState,
    bfg_universal_state_update,
)


def dagger(a):
    return np.asarray(a).conj().T


def random_unitary(rng, n):
    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    # deterministic phase normalization of QR columns
    d = np.diag(r)
    phase = np.ones_like(d)
    nz = np.abs(d) > 0
    phase[nz] = d[nz] / np.abs(d[nz])
    return q * phase.conj()


def random_psd(rng, n, floor=0.0):
    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    a = dagger(z) @ z / n
    if floor:
        a = a + floor*np.eye(n)
    return (a + dagger(a))/2


def random_state(rng, n, persistent_rank):
    u = random_unitary(rng, n)
    z = u[:, :persistent_rank]
    p = z @ dagger(z)

    # Selected/exported neutral sectors both occur in the ensemble.
    v = random_unitary(rng, n)
    yvals = np.exp(rng.uniform(np.log(0.08), np.log(3.5), size=n))
    y = v @ np.diag(yvals) @ dagger(v)

    rho_w_local = random_psd(rng, persistent_rank, floor=0.1)
    rho_w_local = rho_w_local / np.trace(rho_w_local).real
    rho_w = z @ rho_w_local @ dagger(z)

    # Full positive formation density; Selection transport determines what survives.
    rho_f = random_psd(rng, n, floor=0.05)

    # Generic Hermitian capacities. K is biased negative with nondegenerate structure
    # so emergent simple-negative seeds are common but not guaranteed.
    w = random_unitary(rng, n)
    dvals = np.linspace(1.6, 2.8, n) + rng.uniform(-0.05, 0.05, size=n)
    dcap = w @ np.diag(dvals) @ dagger(w)
    coherence = 0.45*np.eye(n) + 0.05*random_psd(rng, n)
    emergence = 0.45*np.eye(n) + 0.05*random_psd(rng, n)

    stable_vals = rng.uniform(0.05, 0.75, size=n-persistent_rank)
    r_c = u @ np.diag(np.r_[np.ones(persistent_rank), stable_vals]) @ dagger(u)

    return UniversalOperatorState(
        D_cap=dcap,
        coherence=coherence,
        emergence=emergence,
        formation_density=rho_f,
        witness=rho_w,
        Y=y,
        R_C=r_c,
        P_per=p,
    )


def run_batch(seed=20260925, cases=1000, max_steps=8):
    rng = np.random.default_rng(seed)
    reasons = {}
    semantics = {}
    success_steps = []
    export_events = 0
    persistent_rank_decreases = 0
    persistent_rank_increases = 0
    witness_loss_events = 0
    max_power_norm = 0.0

    for _ in range(cases):
        n = int(rng.integers(3, 7))
        p = int(rng.integers(1, min(3, n) + 1))
        state = random_state(rng, n, p)
        successful = 0
        final_reason = "max_steps"
        final_semantics = "step_limit"

        for _step in range(max_steps):
            out = bfg_universal_state_update(
                state,
                tol=1e-12,
                boundary_tol=1e-10,
            )

            if out.diagnostics.get("source_export_rank", 0) > 0:
                export_events += 1

            before = int(out.diagnostics.get("persistent_rank_before", 0))
            after_sel = int(out.diagnostics.get("persistent_rank_after_selection", 0))
            after = int(out.diagnostics.get("persistent_rank_after_reclosure", 0))

            if after_sel < before:
                witness_loss_events += 1
            if after < before:
                persistent_rank_decreases += 1
            elif after > before:
                persistent_rank_increases += 1

            if out.terminal:
                final_reason = out.reason
                final_semantics = out.diagnostics.get(
                    "runtime_stop_semantics", "runtime_stop_unclassified"
                )
                break

            successful += 1
            state = out.state

            for k in (1, 2, 5, 10):
                max_power_norm = max(
                    max_power_norm,
                    float(np.linalg.norm(np.linalg.matrix_power(state.R_C, k), 2)),
                )
        else:
            final_reason = "max_steps"
            final_semantics = "step_limit"

        reasons[final_reason] = reasons.get(final_reason, 0) + 1
        semantics[final_semantics] = semantics.get(final_semantics, 0) + 1
        success_steps.append(successful)

    return {
        "seed": seed,
        "cases": cases,
        "max_steps": max_steps,
        "terminal_or_boundary_counts": reasons,
        "runtime_stop_semantics_counts": semantics,
        "mean_successful_steps": float(np.mean(success_steps)),
        "min_successful_steps": int(np.min(success_steps)),
        "max_successful_steps": int(np.max(success_steps)),
        "export_events": int(export_events),
        "persistent_rank_decreases": int(persistent_rank_decreases),
        "persistent_rank_increases": int(persistent_rank_increases),
        "witness_loss_events": int(witness_loss_events),
        "max_observed_recursive_power_norm": float(max_power_norm),
        "status_note": (
            "Internal deterministic finite mathematical stress test only. "
            "Counts depend on the declared synthetic seed ensemble and are not "
            "empirical evidence. Numerical ambiguity is not exact terminality."
        ),
    }


if __name__ == "__main__":
    result = run_batch()
    out = Path(__file__).with_name("NEUTRAL_CONTRAST_STRESS_RESULTS.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
