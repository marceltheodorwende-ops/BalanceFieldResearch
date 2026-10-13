# P78 — Observable restriction, nonlinear sine obstruction and clock alias separation

## Contract and source search

P77 proved a local exact factor p(U_d Xi)=a p(Xi),a=16/135, using two gauge-invariant evolving directions of the full canonical matrix update. It then represented an external sine flow using Pi_j=h_j^-1(S p). Here ask what follows if the physical chart is independently restricted rather than allowed to contain the target flow. PROTOCOL.md freezes the hypotheses and development checks. The physical parent question remains open whichever way this restricted bridge tests.

Sole source: Dynamic Order,8October2026,144pages,SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Part I22–23(87–91), II89(161–162) require fiber and endpoint-flow compatibility and an extra calibrated clock. II83–85(121–143)/AppendixA172–187 provide the endogenous matrix update; the P77 p construction retains its geometry/K transport. The affine physical chart and recorded-event alignment used below are EXTRA testable hypotheses, not source axioms. No new kernel/input policy is silently introduced.

Supporting whole-paper search: gauge quotient requires observable invariance, already met by p. Formation/witness stock and entropy balances II86 supply no instrument gain/clock/force selection. Finite autonomous seed capacity II87 supplies no missing independent sampling clock. II88.2(155) is the declared input needed by this carrier; II88.3 viability/transverse bounds control domains rather than selecting angle. The independent mediator II88.4 is external dynamics and cannot serve as a derived clock. II90 tensor transfer is analyzed below on its actual image; it does not create new observations or cure a failed bridge. The whole active source is searched in support of this one interface package, not separate projects.

## 1. Exact consequences of a fixed affine physical chart

Assume on the P77 neighborhood an EXTRA rank-two chart z=z*+S p, with constant invertible S including declared unit conversions, and constant positive duration tau. Then z+=z*+a(z-z*) EXACTLY for all states in that neighborhood. Since p is a submersion, its image contains a neighborhood of0. Therefore any purported physical continuous flow closing this chart must have return map equal to this affine homothety on an open physical neighborhood, not merely the matching tangent aI.

For an angle-only affine readout theta=b+l p, independently fixed l,b, theta_k=b+a^k(theta_0-b). It is monotone, constant only if l p0=0. The conclusion holds for every0<a<1, arbitrary offset and sign/gain of l, and every forward subsequence of event indices. There is no assertion that recorded .01s rows are canonical events; that alignment is an explicit hypothesis under test. Changes of readout, variable a, moving labels or input policies fall outside this result.

With reported angles q_k and true theta_k in[q_k-epsilon,q_k+epsilon], an ordered triple i<j<k cannot have q_j-q_i>2epsilon and q_j-q_k>2epsilon if the true sequence is monotone: its middle value would be strictly larger than both ends. The analogous trough is also impossible. Define

R_peak=max_j min(q_j-min_{i<j}q_i, q_j-min_{k>j}q_k),
R_trough=max_j min(max_{i<j}q_i-q_j, max_{k>j}q_k-q_j),
R=max(R_peak,R_trough).

R>2epsilon is a rigorous necessary-compatibility rejection for the entire fixed-positive-contraction affine class. This is an exact maximum over ordered triples, computed by prefix/suffix extrema. Ties can be broken by earliest index for reproducibility. Passing it is NOT sufficient for a geometric sequence or globally feasible interval trajectory. For any two admissible perturbations each difference changes by at most2epsilon, which proves the stated deterministic robustness. No dynamical noise/accuracy is inferred.

For the narrower fixed a=16/135 bridge, r_k=q_{k+1}-a q_k must equal c=(1-a)b up to radius(1+a)epsilon. Thus max r-min r>2(1+a)epsilon rejects every constant offset b. Common intersection is only necessary because errors in adjacent pairs share endpoints; it is not a sufficient fit or independent set of observations.

## 2. Even resonance does not make the full sine return affine

Supply EXTRA the damped sine system theta'=v, v'=-gamma v-kappa sin(theta), gamma>0,kappa>gamma^2/4. Put omega=sqrt(kappa-gamma^2/4), T=2pi j/omega,j>=1, rho=exp(-gamma T/2). Its linear return is rho I. Examine initial (theta,v)=(epsilon,-gamma epsilon/2). Write theta(t)=exp(-gamma t/2)u(t). Then

u''+omega^2 u=(kappa/6)exp(-gamma t)u^3+O(u^5), u(0)=epsilon,u'(0)=0.

Smooth dependence of this analytic ODE at fixed finite T gives u=epsilon cos(omega t)+epsilon^3 w(t)+O(epsilon^5), with zero initial w,w'. Variation of constants gives

theta(T)=rho epsilon+C epsilon^3+O(epsilon^5),
C=-rho kappa/(6omega) I,
I=integral_0^T exp(-gamma s) sin(omega s) cos^3(omega s) ds.

Differentiate cos^4(omega s) and integrate by parts:

I=[1-exp(-gamma T)-gamma integral_0^T exp(-gamma s)cos^4(omega s)ds]/(4omega)>0.

Strict positivity holds because cos^4<1 on a set of positive measure and gamma>0. Therefore C<0. An exact explicit expression, useful for independent checks, is

I=(1-exp(-gamma T))/(4omega) * [5/8-gamma^2/(2(gamma^2+4omega^2))-gamma^2/(8(gamma^2+16omega^2))].

Thus the FULL nonlinear sine return is not rho I on ANY neighborhood, even at even resonance. The rank-two affine z=S p bridge cannot realize that full law when rho=a. This strengthens a tangent-only test without contradicting P77: its h_j^-1 must supply a genuinely nonlinear physical chart. It also identifies a falsifiable cubic departure from affine return under separately controlled preparations, not an actual intervention carried out here. The restoring sine law was assumed in this comparison and is not derived from BFG.

Boundary controls: when gamma=0 the displayed position coefficient vanishes, but the velocity cubic correction at T is kappa T epsilon^3/16, so undamped sine still has a nontrivial return jet. It cannot match P77's a<1 in the first place. A separately supplied LINEAR oscillator with the same gamma,kappa has exact resonant return rho I; it is a valid counterexample to any claim that the affine chart excludes all oscillators. Conversely varying force-dependent readouts as in P77 recovers sine closure; this explicitly falls outside the independently affine restriction. No universal BFG obstruction is asserted.

## 3. What independently measured extra time can identify

In an independently fixed physical angle/velocity chart, an underdamped tangent generator has A=[[0,1],[-kappa,-gamma]]. A measured scalar return aI at duration tau determines gamma=-2log(a)/tau but permits aliases omega_j=2pi j/tau and kappa_j=omega_j^2+gamma^2/4. These are exact *linearized* aliases; the full sine maps are not equal at finite amplitude. Without a fixed chart, P77 can conjugate them separately, so measured timing alone does not identify a force.

At an additional independently calibrated duration s=r tau, the tangent return is

B_j(s)=exp(-gamma s/2)[cos(omega_j s)I+sin(omega_j s)/omega_j (A_j+gamma I/2)].

In particular its normalized half-trace is c_j=cos(2pi j r). If a separately justified frequency ceiling Omega limits aliases to j<=floor(Omega tau/(2pi)), then

Delta=min_{j!=k}|c_j-c_k|

gives a sufficient robust discrimination rule: deterministic normalized half-trace error eta<Delta/2 leaves disjoint candidate intervals. If Delta=0 the trace alone does not separate those aliases; the full measured matrix may still do so. No frequency ceiling, derivative measurement, time accuracy or phase error bound is inferred from passive samples. With uncertain r in a declared interval, replace each c_j by its full range; only disjoint expanded intervals certify separation. Widening uncertainties cannot strengthen the certificate.

For exact known irrational r, equality cos(2pi j r)=cos(2pi k r) would require(j-k)r or(j+k)r integer, impossible for distinct positive integers. It separates any fixed finite alias set. This is not a robust infinite-frequency claim: without a ceiling and finite errors arbitrarily near aliases are possible. Rational r can leave exact aliases (e.g.r=1/4,j1 andj3 have equal trace). Finite measurement precision cannot certify an exact irrational ratio.

An exact stronger tangent statement needs no assumed oscillator form: if constant real matrices A,B satisfy exp(tau1 A)=exp(tau1 B) and exp(tau2 A)=exp(tau2 B) with tau1/tau2 irrational, then A=B. The two common exponential matrices commute. Their integer powers give equality at every m tau1+n tau2, including negative integers because exponentials invert. This subgroup is dense, so continuity gives exp(tA)=exp(tB) for every real t; differentiating at0 yields A=B. This proves tangent-generator uniqueness, not a nonlinear force law from finite noisy data. Nonlinear generator reconstruction still requires an independently specified chart and sufficiently informative local trajectories/preparations; equal derivative data alone cannot distinguish sin(theta) from theta+theta^3.

## 4. Domain, units, information loss and levels

p,geometry,a are dimensionless; theta in radians, v in s^-1, gamma in s^-1,kappa in s^-2,tau/s in seconds only under additional calibration. Affine b,l are physical/instrument assumptions, not BFG energy or SI conversion. Quotient invariance is inherited from p, and full-persistence P77 domains have positive loads and no seed. The triple test discards velocity, time and hidden labels; this loss is deliberate for a necessary angle-only certificate. No measured acceleration, inertia, energy or causal input is reconstructed.

On II90's full-persistence tensor-lift image, P77's normalized trace p_m equals p exactly and its update remains a p. Therefore the affine return, monotonicity constraint, cubic sine obstruction and additional-clock conditions transfer unchanged on that image. Total formation/witness are preserved and ranks multiply; neither an independent clock nor a new instrument direction is created. Off-image states and seed branches require separate rules; replicated seed minima may yield T_seeddeg. No physical fractality is claimed.

## Actual status and next dependency

The affine consequences, cubic sine-return obstruction and exact/uncertain finite-alias conditions are PROVED UNDER explicitly stated additional hypotheses. Development outcomes in REPORT.md test only the frozen affine/event/instrument contract. Failure identifies the restricted readout/alignment as inadequate; it does not disprove arbitrary BFG, independent nonlinear bridges or P77's formal conjugate representations. It also cannot tell which part of the uncalibrated bridge fails in the actual apparatus.

Next necessary OPEN dependency: a force-independent nonlinear measurement/preparation law with calibrated event alignment and uncertainty, or a separately constrained alternative carrier/input policy. It must be specified from apparatus/physical principles independently of the desired flow and then tested on development data. Merely replacing the failed affine chart by P77's h_j^-1 reproduces the original physical nonselection. No missing calibration is invented or handed back as routine work.
