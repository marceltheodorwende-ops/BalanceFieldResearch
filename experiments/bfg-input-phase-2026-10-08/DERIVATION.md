# Explicit mechanical input and intervention bridge
Active source: Dynamic Order PDF SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Section88.2/Theorem7 supplies the declared scalar input model y+=f(y+d), not a mechanical torque. Section89 equations(161)–(162) require input-wise fiber closure and separately calibrated physical time. Dependence: P34 exact energy-phase coordinates and P30 explicit event-counter extension.

## 1. Declared additional physical assumptions
A fixed positive inertia I, fixed gravity rate a>0, viscous rate b>=0 and externally supplied torque tau(t) in N m give theta_dot=w, w_dot=-a sin(theta)-b w+v(t), v=tau/I in s^-2. This is a new physical bridge assumption, not a consequence of the autonomous canonical BFG operator. In the same |theta|<pi libration chart use q=2sin(theta/2), p=w/sqrt(a), e=(q²+p²)/2 and u=v/sqrt(a) in s^-1.

## 2. Exact forced differential chain
The chain rule gives q_dot=sqrt(a)p c and p_dot=-sqrt(a)q c-bp+u, c=sqrt(1-q²/4). Thus

    e_dot=-b p²+p u,
    phi_dot=sqrt(a)c-b cos(phi)sin(phi)-u cos(phi)/sqrt(2e),

where p=-sqrt(2e)sin(phi). Multiplying e_dot by a yields E_dot=-b w²+w v: external work and viscous loss. At rest the phase formula is undefined; q,p equations remain regular for |q|<2, including q=p=0. Hence phase is useful for unforced forecasts but q,p is the robust local input interface. Forced trajectories need not preserve e<2; stop this chart at its boundary or use the global theta,w flow. No passive-energy invariant is asserted under arbitrary forcing.

## 3. Exact impulse and work accounting
For an ideal torque impulse J=integral tau dt in kg m²/s, assume fixed angle across the impulse and viscous/gravity impulses vanish in the zero-duration idealization. Then j=J/I has units s^-1 and

    theta+=theta, w+=w+j,
    q+=q, p+=p+kappa, kappa=j/sqrt(a),
    e+=e-kappa sqrt(2e)sin(phi)+kappa²/2.

Recover phi+=atan2(-(p+kappa),q) modulo2pi unless the post-state is rest, where phase has no physical meaning. The total energy jump per inertia is E+-E=w j+j²/2. This is the work supplied by the impulse and may have either sign. In physical units the jump is w J+J²/(2I); no dimensionless BFG formation balance is identified with joules without an additional conversion.
The kick family composes J_j J_k=J_(j+k) and has inverse J_(-j). For the same known j it preserves the Euclidean difference between two theta,w states exactly: translations are nonexpansive. Uncertain impulse adds exactly delta j to velocity, and changes energy by (w+j)delta j+(delta j)²/2. This robustness is immediate-map robustness only; subsequent prediction remains sensitive to clock and force calibration.

## 4. Fiber obstruction and canonical-input distinction
Opposite nonzero velocities at theta=0 have equal energy. Applying the same nonzero j gives energy jumps differing by2wj. Thus energy alone is not a closed impulse observable, independently of the passive counterexample P33. The q,p map retains the missing sign.
In section88.2, d is dimensionless, positive and less than3/4. It is not the signed physical j in s^-1. A positive input can encode a signed torque through an additional centered/calibrated function, so positivity does not prove universal impossibility. But no such function is identified by the paper: two bridges j(d)=c(d-d0) and j(d)=-c(d-d0) have identical canonical y updates and opposite mechanical impulses. Physical orientation/calibration and measured torque are necessary to select a bridge. Geometry contraction16/27 is therefore not a mechanical input-response certificate.
With an explicitly prepared physical state z and counter n, declare U_(d,j)(Xi,z,n)=(U_d Xi, Phi_h(J_j z),n+1), using the supplied mechanical flow and h>0. Pi=z then satisfies equation(161) for every fixed specified d,j by construction. This is a typed extension, not a new component silently attributed to canonical Xi, not a force derived by readout, and not a closed physical factor of y alone. The arbitrary relation between d and j remains a falsifiable additional coupling hypothesis.

## 5. What a calibrated intervention would identify
An observed instantaneous pair obeys delta w=J/I. Known nonzero J and independently timed velocity units identify I=J/delta w under the impulse assumptions. Without known J, common rescaling I->cI, J->cJ leaves all kicks unchanged. No actual J measurements exist in the present passive CSVs; hypothetically applying a kick to measured states is not evidence of its physical occurrence.
For finite pulses the exact integral equation is delta w=-a integral sin(theta)dt-b integral w dt+c integral tau dt with c=1/I. Under independently calibrated torque and seconds, full column rank of these three integral regressors uniquely identifies (a,b,c); rank deficiency permits distinct parameter triples with the same observations. This follows directly from the nullspace criterion for a linear system. A pulse aligned with existing gravity/damping regressors fails to resolve inertia. The continuous/pulse observation and instrument calibration must be declared before an intervention experiment; no missing measurements are fabricated here.

Status: exact forced and kick laws, work and nonexpansiveness derived under additional mechanical assumptions; code/domain controls passed. BFG-to-torque selection, absolute inertia and causal intervention evidence remain unestablished. This package supplies their explicit interfaces and distinguishing conditions rather than claiming they have already been observed.
