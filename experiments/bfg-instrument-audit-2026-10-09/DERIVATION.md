# P65 — Real-development instrument audit and observable/clock closure

## Active claim, assumptions and completion
Audit the permitted attempt-1 instruments and processing to determine whether
P64's state/phase/event-clock measurement prerequisites are supplied. Derive
an explicit conditional two-channel observable, its rank and acceleration
closure; prove concrete calibration/nonidentifiability limits. Complete with
fresh provenance-verified development audit, independent algebra controls,
publication and verified register/ledgers. This is one instrumentation and
bridge investigation, not a fitted new pendulum model or confirmation.

Sole mathematical source: Dynamic Order,8October2026,144pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Sources: PartI22–23(87)–(91),62–64,73.1;83(121)–(123),84–85(124)–(143),
86(144)–(150),87(152),88.3(157)–(158),88.4(159),89(161)–(162),
90(163)–(164). Dependencies P60–P64; retain the additional commutator
preparation and exact selected nonlinear quotient family. A measurement
bridge remains an extra hypothesis; the original paper is unchanged.

Empirical primary source: EnzeXu/Damped_Pendulum_Dataset, commit
cbf82673641ecd65e902ad5c38a048387649a2a0. Read only README.md,
process.py,column_names.py,pendulum_length.json and the 15 explicitly allowed
cleaned_data/len{1..5}_cond{1..3}_1.csv. No dataset clone/archive and no
attempt-2/3 file was read. Metadata and code are source evidence, not
instructions to run their unrestricted all-file processor. Source blobs and
fresh derived audit are recorded in source_evidence.json/source_manifest.json
and audit.json. The source repository is Apache2.0; the four metadata/code
excerpts are retained as audit evidence, with author/repository provenance.

## What is actually provided
The pinned README describes PASCO's Wireless Rotary Motion Sensor PS-3220,
angle and angular velocity, nominal0.01-second sampling, five pendulum lengths
and air/small-baffle/large-baffle conditions. column_names.py identifies
raw units Time(s),Angle(rad),Angular Velocity(rad/s). The length values are
0.236,0.330,0.426,0.518,0.607 meters. These are reported physical metadata,
not inferred BFG constants. The previously archived manufacturer-resolution
audit remains unchanged; its illustrative uncertainty envelope is not a
calibration certificate and is not newly claimed here.

process.py renames the three channels, retains raw time5<=time<65seconds,
subtracts5seconds, then formats time to2decimals and angle/velocity to3.
It copies the angular-velocity channel; the exact sensor/software velocity
estimator and its covariance with angle are not specified by this script.
The angle peak detector consumes the complete record, resolves equal maxima
with a seeded random middle choice, and constructs is_peak. It is a processed
noncausal annotation, not an independent BFG event detector. Do not use a
future-dependent peak flag as an independently calibrated prediction-time
clock. We did not run this script or alter its source.

Fresh audit of all15 allowed files verifies the pinned Git blob for each,
6000 rows per file, time0.00 through59.99, successive one-centisecond ticks,
and the four columns time,angle,angular_velocity,is_peak. Both measured
channels have three printed decimal places throughout. This is90,000
development rows, reused development evidence, not new independent data.
SHA256 and independent byte-level Git hashes are computed locally by audit.py.
CSV formatting implies a conditional half-last-digit rounding bound0.0005
on each printed channel, relative to its preformatted value. It does NOT
bound sensor error, bias, angular-velocity processing, timebase accuracy,
quantization correlations or unobserved true state.

In the materials actually inspected there is no supplied BFG K/Y/witness
measurement, prepared commutator input, event label, N(x), physical c for
one BFG update, uncertainty certificate or direct calibrated torque/inertia
channel. This is a scoped source/schema finding, not a claim that no further
documentation could exist. Device time in seconds IS available as reported;
it does not identify how many canonical BFG events occurred per second.
Ordinary extrema and mechanical phase estimates are derived coordinates
whose identification with BFG relative phase requires a separate bridge.

## A two-channel bridge, not an equation-counting shortcut
On P63's fixed family let x_dot_lambda=v(x)<0 and phi_dot_lambda=omega(x).
On a selected compact interior patch additionally assume v,omega are C1
and an amplitude map A>0 is C2. These smoothness assumptions exceed P63's
general locally Lipschitz conclusion and must be justified for any physical
use. Choose an independently calibrated constant event duration c>0seconds,
and declare a candidate physical angle

 Q(x,phi)=A(x)cos(phi),
 V(x,phi)=[v A' cos(phi)-A omega sin(phi)]/c.             (1)

The first is a new physical observable hypothesis; the second is its EXACT
derivative along the declared nonlinear BFG interpolation, not an independently
fitted velocity channel. Time tau=c*lambda. A measured velocity is a noisy
instrument output for V only if that observation model is validated.
Angle/radian is dimensionless; V has inverse-seconds units. A need not equal
the canonical geometry anisotropy or physical energy amplitude.

Put B=v A', C=A omega. Differentiating(1) gives the exact observation rank:

 det D(Q,V) =[(A B'-A' B)sin(phi)cos(phi)
              -A' C cos²(phi)-A C' sin²(phi)]/c.         (2)

If this is nonzero on a specified patch, the inverse function theorem
identifies x,phi locally from IDEAL Q,V for the FIXED A,v,omega,c and
chosen branch. Two printed channels alone do not ensure(2), identify those
functions/parameters, or provide a global inverse on the phase cylinder.
At a zero determinant the regular local inversion fails. For example a
constant A and constant omega make both Q,V independent of x: rank<=1.
If A is constant but omega varies, the determinant is
-A²omega' sin²(phi)/c and still degenerates at phase extrema. These are
conditional observation counterexamples; no claim that constant omega
reproduces P62's canonical phase increment is made.

The induced acceleration follows by applying v*d_x+omega*d_phi again:

 R(x,phi)=[(v² A''+v v' A'-A omega²)cos(phi)
           -(2v A' omega+v A omega')sin(phi)]/c².         (3)

On an invertible patch G=(Q,V), the explicit local normal form is
Q_dot_tau=V, V_dot_tau=R(G^-1(Q,V)). This is a conditional nonlinear
observable closure derived by the chain rule from P63's actual generator
and the declared observable, without embedding a mechanical solution.
It neither selects A/the interpolation/c nor turns R into a sine force.
A torque J_phys*R additionally requires calibrated inertia and the
mechanical-angle/torque identification. Without the extra smoothness,
only an a.e. version of(3) is available and no smooth mechanical force
law has been established. No unsupported regularity is repaired by fitting.

## Physical seconds do not fix the event duration: constructive counterexample
Let any finite distinct physical times tau_i with printed angle q_i and
velocity w_i be given. For ANY c>0 and any admissible u0>=0 set
u_i=u0+tau_i/c and x_i=N^-1(u_i). These states are on the admitted P63
trajectory in the Abel coordinate. Piecewise cubic Hermite interpolation
H(u) can match H(u_i)=q_i, H'(u_i)=c*w_i exactly for every i.
Choose instead the observable Q_H=H(N(x)), independent of phi. Its
physical derivative is H'(N(x))/c, so both measured channels match at
every sample for ANY c. This continuous C1 observational construction is
an explicitly arbitrary readout, not a BFG-internal derivation or a
two-dimensional pendulum realization: the pair (Q_H,V_H) has rank<=1
in (x,phi), and its force is unspecified between knots. Smooth Hermite
interpolation can also be constructed for finitely many prescribed jets;
no physical selection follows from a good fit alone.

Thus timestamps plus finite angle/velocity do not uniquely calibrate c
without restricting and independently justifying the preparation/observable.
This counterexample uses actual supplied channel types and does not invent
missing physical constants. It is a counterexample to unconstrained
calibration identification, not evidence that calibrated restricted models
cannot be identified. Requiring (2) removes this rank-one shortcut but
does not by itself select the full rank-two bridge.

## Uncertainty and sampling limitations
Define robustness here as local inversion sensitivity on a fixed patch
with specified A,v,omega,c and a convex neighborhood in observation space
contained in its image. If sigma_min(DG)>=gamma>0 throughout the corresponding
inverse domain, ||D G^-1||<=1/gamma. Integration on that convex observation
neighborhood yields state error<=measurement error/gamma. This requires a
real measurement-error bound and an appropriate norm/unit scaling between
angle and velocity; neither a printed decimal nor nonzero determinant
alone supplies gamma or calibrated error. c and parameter uncertainty need
additional propagation. No full-state Lyapunov or global prediction claim.

The0.01second grid is not P64's uniform-u grid unless c,N and state mapping
are independently supplied. Assigning one device sample to one BFG event
would be a declared c=0.01second hypothesis, not a discovered calibration.
No nominal Nyquist rate in seconds proves the assumed bandwidth in u.
P64's finite-node bump continues to leave angular accelerations ambiguous
under finitely many intermediate phase/derivative observations. Numerical
differentiation of quantized channels cannot create independent force data.
Adding length/condition metadata may constrain a future shared mechanical
bridge, but cannot silently turn an externally imposed sine oscillator into
an internal force derivation. All older positive/negative development fits
and their uncertainty remain archived; no new forecast score is reported.

## Full-source audit and compatible other carriers
PartI22–23/73.1 and89 requires exactly the identified observable/clock
missing from the schema; (1)–(3) supplies a conditional typed interface.
83–85 gives quotient covariance and gate restrictions,62–64 the complete
endogenous tangent,86 the cross-load/formation/witness/entropy balances.
Those balances do not add sensor channels or an SI event clock.87 does not
license hidden seed/resource growth.88.1's scalar model is not the entire
BFG;88.2's fixed-input clock obstruction remains,88.3 supplies viability
requirements and88.4's mediator equations are additional models. None
selects this instrument's A,c or true force from the observed schema.

On90's full-persistence tensor family L_m, define Q_m=Q composed with
normalized base readouts and V_m likewise. The full lifted endpoint returns
to the same (Q,V), observation rank and acceleration closure in base
coordinates, by(164); stock/witness are preserved and ranks multiply.
It supplies neither new measured channels nor independent time calibration.
Seed-degenerate/nonreplicated transitions remain outside this lift. No
physical fractality or improvement by repeated time aggregation is claimed.

## Closure and next necessary dependency
Audit.py independently checks every allowed source blob/row/schema/grid and
format; check.py checks(2)–(3) symbolically and the clock/readout Hermite
counterexample numerically for two incompatible event durations. Synthetic
controls are separate from the real-development schema audit. No processor
execution, model fitting, remote empirical workflow or second experiment.

Observed: all15 independently recomputed Git hashes match the pinned
manifest; all15 fresh SHA256 values also match archived development
provenance. Four metadata/code blobs verify independently, all90,000 rows
pass schema/grid/format checks. Four symbolic observable/rank/acceleration
identities pass; two synthetic Hermite clocks match the same samples to
<=2.78e-17 against a frozen1e-12 tolerance. These differing clock values
are counterexample choices, not proposed physical calibrations. All archived
empirical model results remain unchanged. Source license is retained in
SOURCE_LICENSE.txt. Reproduce with python audit.py DATA_DIR and python
check.py; DATA_DIR must contain exactly the15 allowed files and their
bytes must match source_manifest.json. No network fetch is performed by
either script. The clean-source excerpts in source_evidence.json are
evidence only and must not be run on the full dataset.

COMPLETED: primary-source instrument/processing audit, fresh allowed-file
verification, conditional rank-two observable/acceleration closure, and
concrete unconstrained clock-identification counterexample. BLOCKED WITHIN
THE INSPECTED EVIDENCE: adopting P64's phase/state/event-clock measurement
rule as already physically calibrated. The overarching physical problem
remains OPEN. Next necessary solvable dependency: derive and assess a
restricted physically justified observation/preparation family (including
its rank, shared parameters and instrument error), retaining nonlinear
mechanical rivals and the exact BFG factor conditions. No holdout access.
