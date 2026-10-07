# Failure mode: inherited formation readout is stationary

The reference carrier preserves signed theta,w at preparation, but preparation
alone does not imply physical evolution.

For P=I, Q=I, full positive analysis rank and no complement seed, the square
right SVD frame V is unitary and R4 inherits F_plus=V_dagger F V.
If physical instruments are transported by the same frame,
O_plus=V_dagger O V, cyclicity of trace gives

    tr(O_plus F_plus)=tr(O F).

Thus every ratio of such inherited formation traces remains invariant.
In particular the reference-carrier angle and velocity readout stays fixed.
This is a conditional algebraic obstruction for this readout/transport choice,
not a theorem ruling out all BFG physical observables.

The reference candidate Y=0.5 F/tr(F), P=I, K=-I has full selection and positive
loads. Its ambient analysis has full rank and no complementary seed.
100 independent random preparations were passed through the actual existing
ambient implementation; maximum theta/w change was 3.552713678800501e-15.

Reproduction uses experiment.update from the preceding EEG implementation,
reference_carrier.prepare/readout, and inherited instruments V_dagger O V.
These are synthetic code controls, not physical data experiments.

Disposition: retain the successful encoding, reject inherited-F trace ratios
as moving physical observables for this preparation. A next candidate must
use changing internal geometry Y and/or a independently justified instrument
dynamics, with explicit closure and reference calibration. A coordinate change
alone cannot generate physical motion. No physical clock or arbitrary changing
instrument should be fitted just to reproduce target trajectories.
All reserved physical holdout remains sealed.
