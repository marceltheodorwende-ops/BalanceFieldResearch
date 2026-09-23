from __future__ import annotations

from .types import NumericalPolicy, RunRecord
from .core import canonical_reclosure


def simulate(
    initial,
    carrier=None,
    steps=10,
    policy=None,
    *,
    runtime="auto",
    tau=1.0,
):
    """
    Unified simulation entry point.

    runtime="auto":
      - no carrier -> active reduced finite master runtime
      - explicit carrier -> carrier-specific legacy/research lane

    runtime="finite":
      force the reduced finite master runtime.

    runtime="carrier":
      require an explicit carrier and use canonical_reclosure + carrier.advance.

    Carrier-specific biological/empirical lanes remain explicit by design; they
    are adapters/models around the master mathematics rather than silent
    replacements for the finite core.
    """
    policy=policy or NumericalPolicy()
    if runtime not in {"auto","finite","carrier"}:
        raise ValueError("runtime must be auto, finite, or carrier")

    use_finite=(runtime=="finite") or (
        runtime=="auto" and carrier is None
    )
    if use_finite:
        from .finite_closure import run_reduced_runtime
        return run_reduced_runtime(
            initial,
            steps=int(steps),
            tau=float(tau),
            policy=policy,
        )

    if carrier is None:
        raise ValueError(
            "carrier runtime requires an explicit carrier adapter"
        )

    states=[initial]
    records=[]
    current=initial
    for _ in range(int(steps)):
        if current.terminal:
            break
        out=canonical_reclosure(current,policy)
        records.append(out)
        current=carrier.advance(current,out,policy)
        states.append(current)
        if current.terminal:
            break
    return RunRecord(states=states,steps=records)
