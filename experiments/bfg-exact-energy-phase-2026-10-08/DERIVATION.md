# Conditional exact nonlinear closure and stability
Active BFG source: Dynamic Order, SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba, section 89 (factor and calibrated-clock conditions); section 88.2 is an explicitly input-coupled scalar model, not a derivation of gravity. Dependence: prior P33 energy-only closure counterexample and explicit driven-counter extension. No older paper is used as an active axiom source.

## Premises and types
Additional physical generator: theta_dot=w, w_dot=-a sin(theta)-b w, a>0 in s^-2, b>=0 in s^-1, theta dimensionless radians and w in s^-1. Parameters are calibrated externally. E=w^2/2+a(1-cos(theta)) is energy per inertia in s^-2; e=E/a is dimensionless. This mechanical assumption is NOT implied by the BFG scalar update. We construct a sufficient physical coordinate bridge, not a selection of the generator by BFG alone.

## Derivation
On |theta|<pi and 0<e<2, set q=2 sin(theta/2), p=w/sqrt(a). Then e=(q^2+p^2)/2. Define q=sqrt(2e) cos(phi), p=-sqrt(2e) sin(phi), phi modulo 2pi. The inverse is theta=2 arcsin(sqrt(e/2) cos(phi)), w=-sqrt(2ae) sin(phi). All inverses stay in the same well; no lost sign of velocity.
Let c=cos(theta/2)=sqrt(1-q^2/4)>0. Chain differentiation yields q_dot=sqrt(a)pc and p_dot=-sqrt(a)qc-bp, because sin(theta)=qc. Therefore e_dot=q q_dot+p p_dot=-b p^2=-2be sin^2(phi). For phi=atan2(-p,q), phi_dot=(p q_dot-q p_dot)/(q^2+p^2)=sqrt(a)c-b cos(phi) sin(phi). Thus the exact closed equations are

    e_dot = -2 b e sin(phi)^2
    phi_dot = sqrt(a) sqrt(1-e cos(phi)^2/2)-b cos(phi) sin(phi).

They retain the missing phase of P33. Equal e with different phase still gives different loss; no autonomous energy-only factor is asserted. The coordinate map is bijective to the punctured libration-energy well with phase on the circle, not on an unwrapped unique real line. Changing phi by 2pi leaves the observable invariant.

## Invariance and conditioning
Integration of the first equation gives e(t)=e(0) exp(-2b integral_0^t sin(phi(s))^2 ds), hence e(0)exp(-2bt)<=e(t)<=e(0)<2 for all finite t>=0. This proves positivity and a forward invariant domain, conditional on passive mechanics. At b=0 energy is exactly conserved. Rest e=0 is a separate equilibrium with no physical phase; implementation returns theta=w=0 exactly. At e=2 the chart is not guaranteed; rotations require a different chart and are rejected explicitly.
On e<=e_max<2, |d theta/dq|<=1/sqrt(1-e_max/2). Phase derivatives in (q,p) have norm 1/sqrt(2e), unbounded as e approaches zero: no uniform phase-noise robustness near rest. At rest use q,p or the explicit equilibrium branch. Separatrix sensitivity also diverges as e_max approaches 2. A sufficient condition for strictly increasing phase is sqrt(a)*sqrt(1-e(0)/2)>b/2. Without that condition phase is not a monotone clock. Physical seconds remain an independent calibration.

## Positive-coordinate numerical realization
For e>0 integrate ell=log(e): ell_dot=-2b sin(phi)^2, retaining the same phase equation with e=exp(ell). Finite-precision reconstructed e can eventually underflow on extremely long trajectories; this is not a new BFG terminal or a global floating-point guarantee. RK4 stages and final ell increments are nonpositive for b>=0, so every computed stage remains below the initial energy bound, provided arithmetic is finite. This is an invariant-domain argument, not a universal RK4 error bound. Accuracy is separately checked against an independent DOP853 solver and Cartesian RK4 at predeclared tolerances.

## BFG interface and non-derivability
The prepared mechanical state (e0,phi0), calibrated a,b and time per event are additional typed preparation/readout data. With explicit extended event counter n, use Pi(Xi,n)=H(Phi_(n h)(e0,phi0)). Updating n by one yields Pi Uhat=Phi_h Pi by the flow composition law. This satisfies the section-89 factor criterion for this declared extension. It does not say the original scalar y alone contains phase, or silently update inherited K,F, or alter the canonical Xi tuple. A different supplied force generator would also admit a comparable encoding, as the archived nonlinear force counterexamples show. Thus gravity, damping and seconds are not derived from this construction. Driven scalar geometry can coexist with it but supplies no additional physical forecast content without an independently identified coupling.

Status: exact closure and invariant-well bounds proved under stated mechanical assumptions; independent code controls and development equivalence checked. No BFG-only physical emergence, new confirmatory evidence, or superiority over equivalent mechanics.
