# Reference trajectory monitor R1, 2026-09-15

Fixed before execution. Compare on the same 288 noisy histories as detection
catalogue V1: same seed, generation order, scenarios, noise and sensor sets.
Do not change V1's monitor or thresholds. This is a paired synthetic comparison,
not new held-out field data or evidence for BFG superiority.

Additional information: exact initial reference graph/weights and sampling
interval, plus a full-network initial calibration with the same bounded scalar
error as the later sensors. Only 2,4 or 8 selected sensors are needed after
calibration. Do not give the reference detector the changed graph, fault time,
fault type or any future sensor reading.

Predict each next reference state with the original heat operator. Propagate
initial componentwise uncertainty via |R|. Flag an observed residual only if
it exceeds propagated initial error plus declared sensor error plus 1e-10.
This is a deterministic error budget, not a trained threshold or statistical
confidence level. An alarm indicates reference inconsistency, not a fault cause.

Report baseline false alarms, pre-event alarms, detected/missed changes and
first detection delay as in V1. Also test a uniform initial state, where removing
an edge is unobservable under unforced diffusion even with all sensors.
Document exact-topology and calibration assumptions and their limitations.
