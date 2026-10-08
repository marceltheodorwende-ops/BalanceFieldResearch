# Regular geometry-retaining delay chart (8 October 2026)

## Active step and completion rule
Construct two genuinely evolving signed observables from the canonical BFG, prove a regular local closed transition, derive its event acceleration, and establish exactly what is missing for a physical pendulum. Complete only with exact rank witness, domain/counter-limit checks, independent Ambient and derivative/inversion controls, publication and register/ledger verification. No empirical fitting is justified before the physical instrument/clock is selected.

## Sources, types and premises
Sole active source: Dynamic Order, SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Sections 84.1–84.4 equations (124)–(138) define the update; section 89 equations (161)–(162) distinguish factor closure from a physical generator. Sections 62–64 give the regular differential chain; sections 68.1,69.2–69.3,70.1/70.4 require independently prepared observables and seconds. Dependencies P39/P41/P43.

Restrict to a two-dimensional full-persistence carrier P=I, 0<Y<I, F positive with simple eigenvalues f,2f and [F,Y]=0, f>0. K is any Hermitian matrix and W any density matrix. Label the eigenprojectors E1,E2 by the distinct FORMATION eigenvalues f,2f, not by geometry ordering. Put y_i=tr(E_i Y). These labels and numbers are simultaneous-unitary invariant, even if the geometry order reverses. This is a declared preparation subfamily, not all matrix BFG. It has two free geometry directions. Formation and geometry are simultaneously diagonal; K need not commute. No force or mechanical trajectory is inserted.

Full persistence makes Q,Tsel,PG identities. C=(I+Y)^-1, B=I-C; the positive loads give
lc/f=1/(1+y1)+2/(1+y2), lb/f=y1^2/(1+y1)+2y2^2/(1+y2).
Set alpha=lb/(lc+lb), beta=1-alpha. From A†A and inheritance, in the natural input frame,
R_i(y)=[alpha(y)+beta(y)y_i^2]/(1+y_i)^2, F+=F, Y+=diag(R1,R2).
Thus the commuting preparation is preserved. R_i>0 and R_i<1 because 0<alpha,beta<1 and each channel factor lies strictly between 0 and 1. A has full column rank, witness survives, and the seed complement is empty: all these states continue nonterminal. The scalar contraction theorem is not used or extended.

## Construction and regularity proof
Let g(y)=y1-y2 and define the dimensionless delay observable
H(y)=(q,v)=(g(y),g(R(y))-g(y)).
It uses the known canonical update at the current prepared state, not a future observed target. Both components are signed. All loads are rational functions with strictly positive denominators, so R,H are smooth on (0,1)^2.

DH has first row (1,-1), second row grad(g composed R)-(1,-1). Consequently det DH=partial_1(g composed R)+partial_2(g composed R). At y0=(1/5,7/10), exact rational differentiation yields
 det DH(y0)=18076941875/236768239296 >0.
At the same point det DR=-321243859375/52720394616576 is nonzero as well: both geometry directions genuinely evolve, and this property persists on a sufficiently small neighborhood. The inverse function theorem therefore supplies an open neighborhood V of y0 on which H is a diffeomorphism onto its image. This is an existence theorem; the numerical box used below is not asserted to be a certified maximal inverse domain.

For every (q,v) in H(V) define y=H^-1(q,v). The COMPLETE nonlinear transition, not just its tangent, is
 q+=q+v,
 v+=g(R²(y))-g(R(y)),
 a_event=v+-v=g(R²(y))-2g(R(y))+g(y).
This proves exact local fiber closure under equation (161): H is injective on V and its successor is explicitly H(R(y)). K/W and the positive formation scale f do not affect this geometry factor. Transition output need not lie in H(V); repeated use requires overlapping invertible charts or checking entry into the same chart. No global invariant two-coordinate chart has been proved. At points where both charts are regular, the tangent in chart coordinates is DH(R(y)) DR(y) DH(y)^-1, with consistent labels. An invertible coordinate change preserves rank of DR; a chart alone is not a proof that DR is nonsingular everywhere.

## Conditional conditioning bound and failures
Let sigma0 be the least singular value of DH(y0)>0. On a convex ball contained in V where ||DH(y)-DH(y0)||_2<=sigma0/2, integrating the derivative along a segment gives
 ||H(u)-H(v)||_2 >= (sigma0/2)||u-v||_2.
Hence the inverse is Lipschitz there with bound 2/sigma0. Continuity provides some such ball; no numerical radius is certified here. This is local readout conditioning, not dynamical attraction or forecast stability. At the tested center cond_2(DH)=55.42: appreciable amplification remains.

At y1=y2=t the difference R1-R2=0, and its differential is a scalar multiple of dy1-dy2 (the common alpha derivative cancels). Thus det DH=0 there. The preparation and canonical update remain admissible and nonterminal; the readout is singular. This explicitly prevents a global regularity claim or an interpretation of chart failure as canonical termination. Approaching such a stratum can destroy the inverse bound. Formation degeneracy f=2f is impossible for f>0; equal-formation preparations would require a different label convention. Threshold crossing, seeds, noncommuting F/Y and inputs are outside this proof.

## Physical-force audit and alternatives
Declare, additionally, theta=A q and omega_secant=A v/h with A!=0 and h>0. A is an angle conversion and h is seconds per event; neither is selected by the canonical equations. The exact law becomes
 theta+=theta+h omega_secant,
 omega_secant+=omega_secant+(A/h²)[g(R²(y))-2g(R(y))+g(y)] h.
The bracket times A/h² is a well-defined CLOSED acceleration for this discrete chart. It is BFG-derived event acceleration conditional on the preparation/readout, not a Newtonian torque, sine force, inertia, or continuous instantaneous angular velocity. In particular no interpolating flow has been constructed. Seconds rescaling h->c h changes velocities by 1/c and accelerations by 1/c² while leaving the canonical orbit intact. This supplies a concrete remaining calibration nonuniqueness.

For a genuine sine pendulum with instantaneous omega and a>0, b>=0, Taylor expansion of its independent smooth flow gives theta(h)=theta0+h omega0+(h²/2)(-a sin theta0-b omega0)+O(h³). The exact first line above lacks that curvature term. At omega0=0 and 0<theta0<pi, curvature is nonzero for sufficiently small h. Thus treating this secant observable as instantaneous velocity does not automatically identify the sine-flow transition. This comparison does not assert that this chart contains every such mechanical state; it exhibits the additional compatibility obligation, not a universal impossibility.

Other smooth g define different delay maps and accelerations; they are allowed by the same internal update. Even the constants A,h are freely declared until instrument and clock measurements constrain them. Closure and regular rank therefore supply two internal observable directions without uniquely selecting a physical force. Adding an external sine flow to a decoder would again be an external bridge, not this derivation.

## Whole-paper compatibility search supporting this step
The search covered selection/gauge, differential/SVD chain, metric load balance, formation/loss/seed, entropy/diversity, historical witness, finite seed capacity, scalar driven branch, viability/transverse conditions, factor/clock, tensor transitions and physical measurement sections throughout the active text. Canonical equations and factor/differential conditions above support the chart. On this preparation formation stock is constant, seeds absent and witness history lossless; these balances do not calibrate angle or seconds. Entropy and spectral summaries are alternatives but require their own invertible readout check. Constant-input scalar and matrix lifts would change the candidate and are not silently invoked. Section 90's full-persistence lift preserves these geometry/load observables; it cannot supply an independent seconds/force selection merely by label replication. No physical fractality is claimed.

## Controls and actual status
Run: PYTHONPATH=<repository>/experiments/real-eeg-covariance-2026-10-07 python check.py (locally /workspace/bfg-eeg supplies the same Ambient implementation). Dependencies numpy, scipy, sympy. Exact rational rank witness and exact collision rank loss; 40 synthetic nearby cases independently compared with full Ambient SVD update; central differences of symbolic derivative; local numerical inverse checks. Predetermined thresholds: Ambient <1e-10, derivative <1e-7, inverse <1e-8. First symbolic evaluation unnecessarily expanded a full rational determinant and was stopped; substituting the rational point before taking the determinant gives the same intended exact witness efficiently. No failed physical result or data removed.

Status: local regular two-observable INTERNAL factor constructed and proved under explicit preparation. Synthetic controls passed; no measured pendulum prediction, physical force emergence, calibrated seconds, inertia or intervention claimed. Next necessary obligation: independently justified physical observable/clock selection and generator compatibility (including the secant-versus-instantaneous distinction), before a permitted development evaluation. The larger physical question remains OPEN.
