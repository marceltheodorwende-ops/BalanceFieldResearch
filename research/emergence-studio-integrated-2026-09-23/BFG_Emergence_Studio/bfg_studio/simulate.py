from .types import NumericalPolicy, RunRecord
from .core import canonical_reclosure

def simulate(initial, carrier, steps=10, policy=None):
    policy = policy or NumericalPolicy()
    states=[initial]; records=[]; current=initial
    for _ in range(int(steps)):
        if current.terminal: break
        out=canonical_reclosure(current, policy)
        records.append(out)
        current=carrier.advance(current, out, policy)
        states.append(current)
        if current.terminal: break
    return RunRecord(states=states, steps=records)
