# P56: positive kernel endpoints are incompatible with infinite prepared viability

## Active statement and completion rule
Following P55, remove analyticity from the positive-endpoint investigation.
For the P54 family, fixed finite eta!=0, strict gate at every event and infinitely
many events imply s_k ->0. Consequently no invariant amplitude curve, analytic
or nonanalytic, can support an infinite admissible tail with s_k ->s*>0.
This does not exclude nonanalytic zero-endpoint curves or different policies.
Completion: general proof, boundary and alternative-model audit, independent
symbolic and Ambient controls, verified publication and register/ledger status.

## Assumptions and sources
Only Dynamic Order (8October2026,144pages, SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba).
Sections83(121)–(123),84(124)–(138),85 and PartI62–64 define types, quotient,
event and interior differential chain. Dependencies P47 radial norm theorem
and P53/P54 exact Pauli factor. Section88.3(157) supplies the infinite viability
quantifier; section89(161)–(162) separates closure, flow and physical clocks.
H=C2,P=I,F=fI,f>0,W=I/2+w.sigma with 0<|w|<=1/2,w perpendicular j;
Y=tI+y.sigma,J=K/kappa=j.sigma,y perpendicular j,r=|y|>0,s=|j|>0.
Preparation D=eta*i[Y,J] is an explicit extra policy before the unchanged event.
All t,r,s,eta dimensionless; kappa converts kernel units. No physical units or
measured calibration are inferred. The witness supplies relative phase phi.

Let h=r*sqrt(1+4eta²s²), q=h/t in(0,1), with t+h<1. Use P55's exact
A,V,G: t+=A(t,h),r+=V(t,h)>0,s+=sG(t,h),phi+=phi+atan(2eta s).
Thus the exact relative-anisotropy equation is

    q+/q = [V(t,tq)/(A(t,tq)*q)] * sqrt(1+4eta²(sG(t,tq))²).       (1)

## Proof without graph regularity
1. P54 gives 0<G<1, hence s decreases to some s*>=0. P47 applied to
the PREPARED geometry bounds A<=||Y+||<= (t+h)/2<t. Thus t decreases to
L>=0. This is not the autonomous estimate 2^-k for this input model.
2. Suppose s*>0. Then G_k=s_(k+1)/s_k ->1. If L>0, compactness of
0<=h<=min(t,1-t), L<=t<=t0<1 and the strict channel correlation condition
implies h_k ->0: on every h>=epsilon subregion G has maximum strictly below1.
The formulas extend continuously to u-=0 or u+=1 when t>=L>0; these are
limits for the argument, not claimed admitted endpoints. At h=0, A=f_scalar(t)
=2t²/[(1+t)²(1+t²)]<t for0<t<1 (section88.1(154)). Taking limits in
t_(k+1)=A(t_k,h_k) yields L=f_scalar(L), contradiction. Therefore L=0.
3. As t->0, uniformly in q in[0,1], G(t,tq)->g(q)=1/sqrt(1+q²+q⁴).
Because G_k->1, compactness gives q_k->0. The canceled rational expression
V/(Aq) extends continuously to (t,q)=(0,0) with value1. These are algebraic
limits, not an application of an interior derivative theorem at zero loads.
4. Equation(1) now yields q_(k+1)/q_k ->sqrt(1+4eta²s*²)>1. For some
epsilon>0 and all sufficiently large k, q_(k+1)>=(1+epsilon)q_k. Positive
q_k can then neither tend to0 nor stay below1 indefinitely. Contradiction.
Thus s*=0. QED. No analyticity, differentiability or graph existence was used.

Conditional corollary: a nonanalytic invariant graph with an infinite admissible
tail must have zero kernel endpoint; a positive endpoint cannot repair P55.
This closes the positive-endpoint investigation, NOT the invariant-curve parent
requirement. No claim that all initial states continue infinitely is made.

## Alternative constructions, boundaries, and physical force
For eta=0 step4 gives ratio1, so this proof does not decide that branch; phase
is then stationary. For r=0, the scalar geometry branch has G=1 and any constant
s>0, an explicit counterexample if positive anisotropy is omitted. Its phase
is undefined. A trajectory exiting the prepared gate is outside the infinite
viability premise, and gate exit need not be a canonical terminal outcome.
Variable eta_k, additional input, nonorthogonal kernels, non-scalar formation,
seeding or nonreplicated carriers require their own equations and are not ruled
out. No positive load reserve, physical energy decay rate, or full-state
contraction follows from s->0. There is no numerical stability claim near the
boundary: phase is poorly conditioned and double precision loses tiny geometry.

The phase increment alone still supplies no force. With a declared seconds
clock H>0, event angular secants are atan(2eta s_k)/H; rescaling H by c changes
rates by1/c and second secants by1/c² while preserving every event above.
If physical angle is additionally phi, fixed eta makes all increments have
one sign, so this direct identification cannot produce ordinary libration
turning points (absent wrap artifacts). A phase-to-angle readout could behave
differently but requires full closure and independent selection; no sine torque,
inertia, damping constant, or physical energy is derived here.

## Whole-source compatibility search supporting this step
83–85/PartI62–64: quotient, exact channel correlation and differential domains;
86(146)–(150): balanced loads, formation/witness accounting and spectral
distinctions do not select eta or an amplitude graph; on full persistence the
neutral F/W roles do not add evolving amplitude information. 87/Theorem6:
finite autonomous seed capacity does not authorize a seed in this fixed P=I
family. 88.1: scalar boundary equation used above; 88.2(155)–(156): constant
scalar input has a positive fixed point but is a DIFFERENT preparation, not
a counterexample to this theorem. 88.3: static gate is not forward viability;
88.4: mediator ODE is not the discrete generator. 89: clock/closure remain
independent. 90(163)–(164): normalized full-persistence tensor replication
preserves loads,A,V,G and commutes with commutator preparation. Restriction
back to the replicated subfamily gives(1), so that lift does not avoid the
positive-endpoint contradiction. Nonreplicated directions may do so but need
a specified return map and physical bridge. No physical fractality asserted.

## Verification rule and actual scope
Seven exact symbolic checks for limiting formulas, joint-limit denominators,
scalar boundary, and channel
correlation; 40 independent Ambient updates with relative-anisotropy comparison.
Numerical tolerance fixed at1e-10 on interior t in[.2,.7],s in[.1,.8],
h in[.02,.7min(t,1-t)],eta=.1. Synthetic mathematics/code only. An80-digit
boundary-limit check independently checks the contradiction multiplier at
s*=.3; it is not an orbit or invented physical observation. No real-data
experiment is needed for this exact viability implication. Holdout closed.

Status: proved under named extra policy and infinite strict-gate assumptions.
Next necessary dependency: construct or disprove a zero-kernel-endpoint
nonanalytic invariant amplitude curve with a certified forward gate, before
its two-dimensional generator/clock/force selection. This remains OPEN.
