# P69 — Instrument selection, weak force closure and uncertainty

Sole mathematics source: Dynamic Order,8October2026,144pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba,
freshly checked. PartI22–23(87)–(91),62–64,73.1; PartII83(121)–(123),
84–85(124)–(143),86(144)–(150),87(152),88(153)–(159),89(161)–(162),
90(163)–(164),AppendixA. Full-paper accompanying search covers nonlinear
ambient and differential/gauge chain, weighted load/stock/spectral/witness/seed
balances, scalar/driven inputs, mediator, viable/transverse certificates and
factors/clocks/typed lifts. None independently identifies sensor angle with a
canonical phase, or a device tick with a reclosure event.

DependenciesP65/P66/P68. P68 proved a concrete sine acceleration and position
dependent damping using an imposed arcsine readout and clock on a selected
canonical return. It also gave exact event equality including F DT in its tangent;
we retain that equality and do NOT substitute a device sample for a BFG event.
Here the explicit EXTRA bridge hypothesis identifies Q,W,tau with direct
reported sensor channels. Raw source/provenance already audited in P65; actual
SI instrument uncertainty/preparation/event correspondence remains uncalibrated.
P68 equations become Q'=W,W'=-kappa sin Q-Gamma0 cos(Q/2)W. Both the force
and physical identification remain category(c)/(b), not an internally selected law.

## Weak closure, exact derivation and shared physical premise
Let b(Q)=cos(Q/2) for P68 or b=1 for viscous/mixed rivals, beta>=0. Assume
 Q'=W, W'=-kappa sin Q-gamma b(Q)W-beta |W|W.             (1)
For any C1 test function phi vanishing at a,b, integration by parts gives
 integral_a^b W phi' dt
 =kappa integral_a^b sin Q phi dt
  +gamma integral_a^b b(Q)W phi dt
  +beta integral_a^b |W|W phi dt.                        (2)
No acceleration finite differences are required. The zero boundary terms are
essential. Conditional closure for a dense collection of compactly supported
tests is distributional closure (and classical for continuous RHS); finitely
many fitted moments alone do not establish the full ODE or its canonical factor.
An exactly orthogonal untested residual is a concrete counterexample to that
inference: for any finite span of tests choose a nonzero smooth residual in its
orthogonal complement. Existing free between-event/observable ambiguities persist.

For a hypothesized identical bob of mass m with length L and constant pivot
inertia I0, torque=-m g L sin Q and I=mL^2+I0 imply
kappa(L)=g L/(L^2+lambda),lambda=I0/m. This is an EXTRA mechanical assumption
from the old shared-calibration package, not BFG or independently measured m,I0.
Dataset length/g values are reported external metadata; g is not a new BFG
prediction. m and I0 cannot be separated from lambda without independent mass
or inertia data. kappa has s^-2 units, gamma s^-1,beta dimensionless with radians
dimensionless,lambda m^2; angle and time channels retain their reported units.
Changing time calibration by a constant a changes kappa by a^-2,gamma by a^-1;
finite prediction scores do not remove the P68 unobserved event-clock freedom.

## Kinematic bound and its stated physical reach
For exact true Q'=W on a width h window, samples spaced dt, errors bounded
epsQ,epsW and exact true sample times, the measured residual satisfies
 |Qm(b)-Qm(a)-Trap(Wm)|<=2epsQ+h epsW+h dt^2 M2/12,      (3)
where M2 bounds true |W''|. The first two terms follow from the triangle
inequality and nonnegative trapezoid weights summing to h; the last is the
composite trapezoid remainder. Printed rounding .0005 bounds rounding only;
using it as total true-state uncertainty is a separately falsifiable assumption.
No certificate for timing error, filtering, bias or sensor response is available.

For (1), E=W^2/2+kappa(1-cos Q) has
 E'=-gamma b(Q)W^2-beta |W|^3.                          (4)
For b=cos(Q/2), restrict the principal chart |Q|<pi with E0<2kappa; energy
nonincrease proves forward chart invariance, b>0 and |W|<=vmax=sqrt(2E0).
For b=1, energy nonincrease holds without that chart restriction, though we use
the same corridor for comparability. At an uncertain window start, bound E0 by
(|Wm|+epsW)^2/2+kappa max_{|e|<=epsQ}(1-cos(Qm+e)).
Evaluate both endpoints and any intervening odd-pi maximum. If the interval
does not lie in the principal chart or E0>=2kappa, mark the certificate
unavailable rather than silently assert it.

Put bmax=1,dmax=1/2 for clock_cos; dmax=0 for other rivals.
 Amax=kappa+gamma vmax+beta vmax^2 bounds |W'|.
Differentiating (1) along the flow yields
 W''=-kappa cos Q W-gamma[b'(Q)W^2+b(Q)W']-2beta|W|W',
 M2=kappa vmax+gamma[dmax vmax^2+Amax]+2beta vmax Amax.  (5)
The derivative of |W|W exists at zero and is2|W|; no false dry-friction
discontinuity is used. Thus (3) is a rigorous conditional bound for every
specified parameterized model, not an empirical assertion that its assumptions
are true. Failure certifies inconsistency of THAT combined instrument/ODE
hypothesis even with this conservative integration allowance. Holding the
initial energy envelope and M2 FIXED, the additive angle-budget deficit is
max(0,(|R|-h epsW-h dt^2 M2/12)/2-epsQ). Increasing uncertainty at the
initial state changes M2 and requires recomputing the certificate; this number
is not a minimum uncertainty for a repaired model or a measured device accuracy.
If the hypothesis has no valid corridor,
the criterion is not evaluated as a proof of failure.

For the ENTIRE clock_cos family in the frozen calibration bounds, take
kmax=g/L,kmin=g*L/(L^2+.02),gammamax=2sqrt(kmax),beta=0. If the uncertain
start satisfies Vmax+(|Wm|+epsW)^2/(2kmin)<2 and |Qm|+epsQ<pi, it has
a valid corridor for every allowed kappa. The velocity bound from kmax and
gammamax dominates (5) for every member, since all terms are nonnegative and
monotone in these parameters. Applying (3) with those bounds is a family-wide
conditional exclusion, independent of fitted lambda/gamma. It excludes only
this underdamped, shared-inertia, rounding-only direct sensor/time hypothesis.

For force moments, rounding alone gives the separate integral perturbation
allowance (for nonnegative sin^2 phi)
 2epsW+(h/2)[kappa epsQ+gamma(epsW+dmax*vmax epsQ)
                    +beta(2vmax epsW+epsW^2)].          (6)
This does not bound unvalidated continuous quadrature/timing/sensor effects.
Fine/coarse weak quadrature differences are implementation diagnostics only.

## Identifiability and stability before any development result
Weak damping columns must have positive norm and independent spans. For any
design A with singular value sigma_min>0, a bounded unweighted moment error
e gives parameter error<=||e||/sigma_min for the unconstrained linear inversion;
boundary-constrained fits need their active-set geometry too. Normalizing
columns diagnoses correlation, not physical-unit uncertainty. If |Q|<=A<pi,
 0<=1-cos(Q/2)<=Q^2/8<=A^2/8.
Hence the clock/viscous damping moment difference is at most
(A^2/8)integral |W phi|, and their discrimination degenerates with amplitude.
Do not infer sine-clock selection from nearly identical fitted residuals or
one good mean. beta terms add 15 degrees of freedom and remain in comparison.

The declared stability notion is energy decay/chart invariance of the extra
factor and step-refinement agreement for predictions, not universal BFG
stability. All forecast parameters are calibrated only at0–30 and held fixed
for a single autonomous30–59.99 path. Actual prediction uncertainty is not
certified without an apparatus budget; repeated development temporal splits
are not independent confirmation. Calibration weak quadrature is repeated
at .02 grid to expose numerical sensitivity, with no refit using later records.

## Other compatible levels and status
For full-persistence lift90(163)–(164), define normalized base projection Pi_m
by the P68 base readout. Pi_m(L_m Xi)=Pi(Xi), T_m(L_m Xi)=T(Xi), so
Pi_m(U L_m Xi)=flow_F^{T(Xi)}Pi(Xi), and differential on base directions
including F DT is unchanged. Formation stock/witness normalization are
preserved, ambient/persistent ranks multiply by m. Seed replication can terminate
at T_seeddeg; this calculation is confined to full persistence. Pulling a sensor
test back through this lift gives the SAME test, not new observations/accuracy.
It does not repair the physical clock or select sine. Temporal grouping is
ordinary flow composition, not a physical fractality certificate. Coupled levels
with new measured states/resources would need a separately declared input and
return projection. The independent scalar mediator has no such sensor interface
and cannot be substituted for the ambient generator by calling it a clock.

Status before development: weak/energy/kinematic/conditioning identities PROVED
under explicit assumptions; direct physical identification and shared-inertia
law ADDITIONAL HYPOTHESES. Data and controls only assess this limited hypothesis.
No nonlinear rival or passive sensor series is called a canonical intervention.
Physical force selection,SI event durations,absolute inertia,preparation and
actual interventions remain OPEN irrespective of temporal development scores.
