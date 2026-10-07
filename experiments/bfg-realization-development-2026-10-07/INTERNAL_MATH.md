# Internal mathematics: scale-independent feasibility restriction

Post-development analysis. All measurement evidence here is attempt 1.
No test files were opened. This strengthens diagnosis, not positive prediction.

For the scalar branch and linear energy readout E=s*y, one-step retention is

    r(y)=f(y)/y=2*y/((1+y)^2*(1+y^2)), 0<y<1.

Since (1+y)^2>=4*y, r(y)<=1/(2*(1+y^2))<1/2.
A sharper global bound follows from differentiating:
the sign of r'(y) is the sign of 1-y-y^2-3*y^3.
This polynomial decreases strictly on (0,1) and has exactly one root y_star.
Hence the global maximum is at y_star=0.46939642456999464, with
r_max=0.35629806077953297 (numerical approximations to an exact algebraic bound).

Consequences: no choice of positive reference scale s can make this scalar
linear-energy bridge retain more than approximately 35.63% per admissible step.
All 1,364 development transitions retained more than 50%. Thus the failure
is structural for this bridge, not merely a badly chosen scale.
This is finite development evidence coupled to a mathematical bound;
no new statistical confirmation is claimed. Terminating inputs do not evade
the bound while supplying a valid prediction.

## Routes that require new derivation

A nonlinear readout E=s*y^p changes retention to r(y)^p. It can evade the
linear-readout bound, but selecting p from these observations is a new
exploratory measurement hypothesis, not a derivation of physical energy.
Its behavior and regularity at zero must be audited. Smooth readouts with
zero derivative at zero also require more care than the regular-coordinate
theorem; no universal impossibility for all readouts is claimed.

A state-dependent clock can formally force scalar decay to match an exponential:
tau(y)=-log(r(y))/k for k>0 gives E_next=E*exp(-k*tau(y)).
This is an algebraic identity, not an independently calibrated physical clock.
Such a clock must be tested against measured event intervals, not chosen from
target energies; otherwise the construction is unfalsifiable.

A richer carrier retaining angle and velocity may avoid the information loss,
but operators K,F,W,Y,P, their physical projection and intervention action
still need a supported construction. Merely inserting a fitted physical
oscillator into those matrices would not establish that its laws follow from BFG.

Next work: audit these possible routes symbolically and on development data,
retain failed mappings, and reject paths requiring uncalibrated freedoms.
Confirmation remains sealed until a complete defensible realization is frozen.

