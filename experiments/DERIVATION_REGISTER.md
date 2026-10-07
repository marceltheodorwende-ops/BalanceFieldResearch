# BFG derivation and proof register

Version 2026-10-07. Status refers to the stated hypotheses, not universal
physical emergence. Numerical controls corroborate calculations, not general
theorems. Every continuation must maintain this register.

| ID | Statement / obligation | Basis and additional assumptions | Current status | Evidence / next step |
|---|---|---|---|---|
| P01 | Scalar canonical update f(y) | Full selected 1D carrier, positive loads, no seed | Derived on this branch | movement tests compare 100 actual ambient updates |
| P02 | Clock N(f(y))=N(y)+1 | Constructed phi coordinate, fixed reference y0 | Derived, physically uncalibrated | NONLINEAR_OBSERVABLE.md and movement README |
| P03 | Linear-energy retention <=0.356299 | Physical E=s*y is an extra hypothesis | Conditional bound derived; candidate fails development feasibility | INTERNAL_MATH.md |
| P04 | Regular C1 energy bridge to exponential decay impossible near zero | h'(0) finite nonzero, physical g'(0) in (0,1) | Conditional obstruction derived | earlier EEG MATHEMATICAL_ASSESSMENT.md |
| P05 | Inverse-log readout yields geometric decay | Added H_p, free C and p | Derived representation; physical readout not independently justified | NONLINEAR_OBSERVABLE.md |
| P06 | Formation-only inherited readout is stationary | Full selection/rank, no seed; joint instrument inheritance | Conditional obstruction derived | STATIONARY_READOUT_OBSTRUCTION.md |
| P07 | Calibrated scalar projection reproduces linear pendulum motion | Added mechanical generator, physical clock and preparation | Exact conditional representation derived; emergence unproved | movement README, GENERALIZED_MOTION.md |
| P08 | Mass/inertia/torques uniquely identified from angular motion | Conventional mechanical torque model | Nonidentifiability demonstrated by common scaling | mechanical identification README |
| P09 | Physical energy unit and seconds fixed by BFG | No independently justified coupling supplied | Open physical requirement; exhibited calibration freedom | CONDITIONAL_PHYSICAL_EXPLANATION.md |
| P10 | Frequency and drag arise from BFG alone | Need constraints beyond fitted mechanical generator | Open derivation | Audit allowable BFG couplings and rival realizations |
| P11 | Instrument-aware latent state is measurable | PASCO resolution plus dataset processing | Exploratory evidence, incomplete uncertainty model | MEASUREMENT_AND_STABILITY.md |
| P12 | Baffle intervention corresponds to BFG operator action | Geometry/medium/inertia calibration needed | Conditional mechanical action; BFG action open | PHYSICAL_CLOSURE_AUDIT.md |
| P13 | Shared calibrated realization has independent predictive support | Fixed protocol, strong rivals, untouched observations | Not evaluated; holdout sealed | Freeze only after justified structure exists |

## Automatic execution rule

On each continuation choose the next dependency that can be addressed concretely.
Work on P09/P10/P12 by constructing restricted coupling candidates and testing
uniqueness, dimensional calibration, shared parameters and intervention constraints.
Use mathematical counterexamples to eliminate arbitrary choices before fitting.
For empirical checks use attempt-1 development data only and retain failures.

Do not mark P09/P10/P12 proved because P07 represents an already supplied
mechanical flow. Existing nonidentifiability arguments constrain the current
assumptions; they are not a universal impossibility theorem for every future BFG
extension. Any additional axioms or coupling principles must be separately named,
supported and tested. Update evidence and status after each substantive package.

## Additional shared-calibration evidence

P14: a(L)=gL/(L^2+I0/m) is derived conditional on a point bob and constant
pivot inertia. Shared ratio fits 15 development records with nearly unchanged
motion scores and fewer parameters; Action37689622515 verifies reproduction.
This constrains P10 using an added mechanical hypothesis, not a BFG-only proof.
P15: U_j=U^(2^j) implies U_(j+1)=U_j^2 and exact dyadic clock consistency.
This is derived temporal hierarchy, not observed physical fractality. Three
scalar controls pass. Fractal extensions are optional and require justification.
