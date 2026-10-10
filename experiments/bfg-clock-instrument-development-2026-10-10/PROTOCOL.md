# P69 — Direct instrument bridge and nonlinear clock-rival development

One active P68 dependency: test the restricted physical-selection hypothesis
Q=sensor angle, W=sensor angular velocity, tau=reported sensor seconds, against
its kinematic obligation and nonlinear force rivals. This is additional instrument
identification, not a BFG-internal force/clock derivation. P65's absent canonical
event/preparation identification is retained. Complete with derivation, independent
controls, real development comparison, all failures, publication and byte-verified
register/both ledgers. Protocol written before this package opens measurements.
All existing development data have been used before; no independent confirmation.

## Frozen data, comparison, stability and decision rules
Only the already pinned 15 len{1..5}_cond{1..3}_1.csv files. Require exact allowed
directory membership and SHA256/Git blobs from P65; reject other attempts before
opening any CSV. Source EnzeXu/Damped_Pendulum_Dataset commit
cbf82673641ecd65e902ad5c38a048387649a2a0. Read time,angle,angular_velocity only;
ignore is_peak (computed using the full record). No additional fetch or archive.
Fixed source lengths [.236,.330,.426,.518,.607] m and reported g=9.799 m/s^2.
Assume the historical EXTRA identical-bob/constant-pivot-inertia bridge
kappa(L)=g*L/(L^2+lambda); this is not independently established apparatus physics.
One shared lambda in [0,.02] m^2 and per-record nonnegative damping parameters.
No free angle offset, velocity gain, clock deformation or state smoothing.

Calibration 0<=time<=30; temporal development comparison 30<time<=59.99.
Nonoverlapping half-second weak windows; the window endpoint may be shared.
phi=sin^2(pi*(time-start)/.5), zero at both ends. Fit by equally weighted
record-normalized squared weak residuals (normalizer RMS(y) from calibration).
For each lambda eliminate damping by exact one-/two-column bounded least
squares; compare a 21-point lambda grid, both endpoints and bounded scalar
minimization at xatol1e-10. Gamma0 in [0,2sqrt(kappa)*(1-1e-10)] for all rivals;
a zero rate is retained and flagged as inherited P68 rank-degenerate boundary.

Models, frozen without development-response-dependent new terms:
  clock_cos: W'=-kappa sin Q-Gamma0 cos(Q/2)W (P68 conditional readout).
  viscous: W'=-kappa sin Q-Gamma0 W (nonlinear sine rival).
  mixed_drag: W'=-kappa sin Q-Gamma0 W-beta |W|W, beta>=0 (strong nonlinear rival).
Counts16,16,31 fitted coefficients respectively; known lengths/g, 30 observed
initial-state numbers, zero-angle and instrument/clock assumptions are additional.
These are equally specified models, not unexplained terms added to improve P68.

Kinematic selection: for each half-second window evaluate
R=Q(end)-Q(start)-trapezoid integral W. Under EXTRA rounding-only channel
errors epsQ=epsW=.0005, exact .01 grid timestamps, and a specified fitted
nonlinear ODE, bound |R|<=2epsQ+h epsW+h dt^2 sup|W''|/12. Derive sup|W''|
from that ODE's energy corridor and uncertain initial state, not from fitted
finite differences. A violated bound refutes that complete narrow instrument+
ODE hypothesis, not BFG universally or the sensor's actual accuracy. No certified
physical uncertainty budget exists. Force moments/quadrature discrepancies are
diagnostics rather than a substitute for a validated apparatus error model.
No timestamp rounding uncertainty silently invented or taken to vanish physically.

Also evaluate the clock_cos family-wide kinematic bound at kappa_max=g/L,
gamma_max=2sqrt(kappa_max),beta=0,dmax=.5. A common energy corridor exists
only if Vmax+(|Wm|+epsW)^2/(2*kappa_min)<2, where
kappa_min=g*L/(L^2+.02). That bound excludes every fitted lambda/rate in
the specified family if violated; it still assumes the rounding-only direct
sensor bridge and exact sample timestamps. Preserve unavailable certificates.

Dynamical stability: energy nonincrease and |Q|<pi under E(initial)<2kappa.
Numerical stability: compare all 45 autonomous forecast paths with RK4 steps
.005 and .0025 seconds, max angle difference<=1e-5 and velocity<=1e-4.
Failure is retained, not called a valid numerical result; at most one further
step halving, explicitly logged, is allowed. Independent DOP853/code controls.
Prediction robustness: quantify this integration disturbance only; no absolute
robustness to unknown real measurement error or preparation/clock changes.

From the observed state at time30 run ONE autonomous trajectory/model/record
without resetting from later observations. Report equally weighted per-record
angle/velocity RMSE and RMSE/persistence at horizons .1,.5,1,2,5,10,20,29.99s,
paired wins, medians/ranges, parameters/boundaries and within-record weak
conditioning. Baseline persistence holds the time30 state constant. These differ
from the older rolling .1s task; old scores are preserved, not relabeled.
Half-second force residual comparison and lambda profiles remain exploratory;
1%-loss profile width is a development sensitivity diagnostic, not a confidence
interval. No single favorable average establishes physical selection/superiority.

If direct instrument bounds fail, retain forecasts as diagnostics of this
uncalibrated hypothesis and report the physical bridge as failed in its stated
rounding-only form. Even a pass/small forecast error cannot calibrate BFG event
durations or establish canonical force selection. Next necessary dependency is
a justified instrument/preparation/event correspondence or a bounded declared
measurement model, not holdout access or uncontrolled observable changes.
