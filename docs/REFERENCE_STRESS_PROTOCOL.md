# Reference uncertainty and known excitation R2, 2026-09-15

Specified before running the catalogue. Keep R1 detector and thresholds fixed.
Synthetic sensitivity check, not field validation or external preregistration.

Eight nodes; path/cycle; true edge weights 0.5/1.0. Reference weights are
0.9,1.0,1.1 times the true weights. dt=0.2; 20 samples after initialization.
Physical condition: intact network or middle edge (3,4) removed before sample 0.
Initial condition: uniform 1/8, or uniform plus a known +0.5 impulse at node 0.
The initial impulse is part of the reference initial state, not an unmodeled
later forcing. No hardware intervention is performed.

Use full ongoing observation to isolate reference error from sensor coverage.
Reading noise and initial calibration noise are independent uniform [-0.001,
0.001], RNG seed 20260917. Reuse each graph's noises across paired cases.
Calibration cases: unbiased with declared error 0.001; +0.02 bias at node 0
with honest bound 0.021; same bias with understated bound 0.001.
Thus 2 families x 2 weights x 3 reference scales x 3 calibration cases x
2 excitation settings x 2 physical conditions = 144 runs.

Report healthy-network alarms separately from detected cuts and missed cuts;
report first alarm step. An alarm caused by wrong reference parameters or an
understated calibration bound is expected model inconsistency, not proof of a
physical fault. Excited versus unexcited cases are paired but are different
physical trajectories. Do not tune impulse size, noise budget or thresholds
after inspection. No fault localization claim.
