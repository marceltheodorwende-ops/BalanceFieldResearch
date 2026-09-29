# Constructive synthetic emergence witness: fixed rule

This protocol defines a *new constructed example*, designed after the earlier negative pilot. It is not a preregistration of independent data and does not replace that pilot.

## Generator and intervention

For independently driven source signs `s1_t,s2_t ∈ {-1,+1}`, set `q_t=1+0.5*s1_t*s2_t`, `m_{t+1}=0.6*m_t+0.4*q_t`, and `h_{t+1}=0.4*h_t+0.6*gamma*m_t`. Initial states are `m_0=h_0=1`. `h` is a separately updated higher state. Both sources have absolute amplitude one; source innovations and trajectories are matched in every arm. This is a stipulated two-layer synthetic generator, **not** a realization of the complete canonical five-object BFG map.

Use 1,000 independent source sequences of 160 steps, Python `random.Random(20260929)`. At step 80, reset `h` to zero in every arm while preserving `m` and sources. For steps 80–109 compare `gamma=1` (full) with `gamma=0` (removed). In a third arm restore `gamma=1` for steps 110–129 after the same 30-step removal. Removal changes the generating `m→h` edge; it does not erase an already computed readout. Score `Q` as mean `h` at steps 120–129. Compare restored with continuously removed trajectories at that score, and full with removed at steps 100–109. No fitting or sampling-based significance test is needed for the deterministic bounds.

## Decision rule and named rival class

The constructed example passes only if every realization has source amplitude one, the full higher state stays within `[0.5,1.5]` outside the deliberately imposed reset transient, `Q_full-Q_removed>0.49`, `Q_restored-Q_removed>0.49`, and the mixed source contrast and temporal impulse determinant below exceed tolerances. Numerical tolerance for analytic equalities: `1e-12`.

At one time step, the mixed source contrast is `q(+,+)-q(+,-)-q(-,+)+q(-,-)=2`. An additive source model and a common-driver model with no source-interaction path have zero contrast under independent controlled assignments. A circularly shifted source under a single-time source assignment with its shifted history held fixed also has zero contrast. These are restricted controls, not all conceivable common-driver mechanisms.

The impulse of `q_t` on `h_{t+k}` has `g1=0`, `g2=0.24`, `g3=0.24`, `g4=0.1824`; `g2*g4-g3*g3=-0.013824`. A direct one-pole dyad of the declared class `h_{t+1}=lambda*h_t+c*q_{t-1}` has zero determinant. The rule requires `|mixed contrast|>1`, `|determinant|>0.01`, and exact reproduction of all four impulse values within `1e-12`; the restricted rivals fail at least one condition. A dyad with its own two-state memory can recode `m` and tie the full generator; it is reported as an equivalent representation, not defeated. No inference of unique physical mediation or universal emergence follows.
