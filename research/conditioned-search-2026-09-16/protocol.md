# Conditioned numerical search protocol

Exploratory repair following diagnosis, fixed before the repaired evaluation.
Audit sources: the three DOCX files/hash register in ../../docs/BOUNDARY_PROTOCOL.md.
Retain historical records and original default behavior.

Diagnosis: complete4 midpoint Jacobians have relative singular values around
1e-10 in insensitive directions and raw steps around 4e7 to 3e8. Path3 has a
clear nonzero spectrum. For equal hub edges and an impulse at the hub, the three
other nodes remain equal: their internal edges have no effect on the trajectory.
The extremely small numerical singular values must not be treated as accurately
measured sensitivities. This is a local diagnosis, not general identification.

Repair: optional relative SVD cutoff fit_rcond=1e-8 in the existing least-squares
step. Chosen from the observed spectral gap, before evaluating the fix. No
change to measurement errors, physical intervals, trajectory certifier or
acceptance criterion. Default None preserves the old method for reproduction.

Compare None versus 1e-8 on the same 20 inputs, 31 boxes, depth 12, 27 candidates,
256 numerical evaluations and 64 certificate terms. Replay 39 older cases.
Success: fewer unresolved complete4 cases without reversing old certificates.
Failure: false exclusions, inadmissible witnesses, dependence on relaxed sensor
bounds, or no decision gain. Preserve residual unresolved cases without retuning.
No universal solver, unique graph identification or empirical BFG claim.
