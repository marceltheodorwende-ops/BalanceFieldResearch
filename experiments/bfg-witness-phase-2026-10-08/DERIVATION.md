# P54 — Witness-referenced phase and exact closure audit

8 October 2026. P53 next dependency: a coherence-retaining observable phase and two-variable nonlinear closure. Result: an internal gauge-invariant phase is constructed and its exact event/tangent derived; the tested phase/kernel pair fails local closure. The complete factor has four coordinates. Physical pendulum, force, seconds and invariant two-dimensional realization remain OPEN.

## Claim and completion criteria

Use H=C², P=I, F=fI (fixed f>0), K=kappa J (fixed positive unit scale), Y=tI+y·sigma, J=j·sigma, y·j=0. Keep P53's explicitly EXTRA preparation D=eta i[Y,K]/kappa, fixed real eta; apply the unchanged canonical event to Z=Y+D. Replace the scalar witness by W=I/2+w·sigma with fixed |w|=a, 0<a<=1/2, w·j=0. This is a declared initial state family of the existing witness type, not a new external vector or modified update. Require r=|y|>0,s=|j|>0 and 0<t-h<t+h<1 where h=r sqrt(1+4eta²s²).

Investigated claim: witness inheritance supplies an observable phase; establish algebraic family preservation, complete factor closure, regular tangent, and test whether the pair(phi,s) alone closes. Completion requires proof, exact fiber counterexample if needed, independent Ambient/gauge controls, boundary/units checks, and verified publication/register/ledger. None of these criteria substitutes for physical calibration.

## Source scope and supporting search

This proof uses ONLY Dynamic Order: §83 types/quotient(123); §84 selection/loads/SVD/R4/seed(124)–(140); §85 Theorems2–3; §§62–64 within PartI regular derivatives; §86 balance/stock/witness distinctions; §88 driven input/viability(155)–(157); §89 closure/clock(161)–(162); §90 typed full-persistence lift(163)–(164). The PDF is the unchanged144-page artifact with SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. The latest mandate's sole-source restriction suffices; no premise needs the older paper. P53's algebra is a prior derived dependency, reproduced here where needed.

The supporting search across the full active text included gauge/polar/SVD differentials, weighted load and formation-loss-seed accounting, historical witness balance, spectral diversity/entropy, scalar and explicit input models, viability/transverse certificates, factors/clocks and tensor transitions. Full persistence makes R4 a unitary identification and witness inheritance lossless. Here it carries a directional reference; its scalar mass/entropy alone cannot carry the relative phase. Seed capacity adds no variable on empty complement. Formation balances do not select eta or seconds. The typed normalized lift preserves traces/weights and commutes with this commutator preparation, since [Y⊗I,J⊗I]=[Y,J]⊗I. It replicates this same factor and adds no independent physical phase or dimensional calibration. No unsupported fractality/level bridge is inferred.

## Exact reference and phase construction

On full persistence, natural-frame W+=V W_successor V†=W, by equation(138) and T4=V†. F+=fI, P+=I. P53's exact natural-frame endpoint is

z=y-2eta y×j, |z|=h,

u±=t±h, c±=(1+u±)^-1, b±=u±c±,

Lc=f(c++c-), Lb=f(u+²c++u-²c-), alpha=Lb/(Lc+Lb), beta=1-alpha,

a±=alpha c±²+beta b±²,

t+=(a++a-)/2, v+=(a+-a-)/2,

y+=(v+/h)z, j+=gamma j,

gamma=(alpha c+c-+beta b+b-)/sqrt(a+a-).

All these follow from A†A=alpha C²+beta B² and offdiagonal J in the Z eigenbasis; {z·sigma,J}=0 yields CJC=c+c-J,BJB=b+b-J. Full R4 inheritance then preserves w. Consequently y+·j+=w+·j+=0 and |w+|=a. Current event is nonterminal: positive loads, rank2 and empty complement. The next prepared gate remains compulsory; P53's failure for large s applies unchanged because W does not enter loads on full P.

Define quotient-invariant circular observables

X=(w·y)/(ar), Zphi=j·(w×y)/(sar), X²+Zphi²=1,

phi=atan2(Zphi,X) modulo2pi.

Both are common-unitary invariants; traces of Pauli products and their signed commutator recover the dot/triple products. They refer to the existing W,J,Y states, not to a coordinate axis. If w points along x and j along z in any representative, y has planar angle phi. Then z rotates y by atan(2eta s) about j.

### Positive geometry splitting, no hidden pi flip

Let m=Lb/Lc=t²+h²(1-t)/(1+t). Define A(u)=(m+u²)/[(1+m)(1+u)²]. Algebra gives

A(u+)-A(u-)=4h [t-t³-h²(2-t)] /[(1+m)(1+u+)²(1+u-)²].

For t<=1/2, h<t implies the bracket>t(1-2t)>=0 (strict at t=1/2 through h<t). For t>=1/2, h<1-t implies bracket>2(1-t)(2t-1)>=0. Thus v+>0 everywhere on this strict family. This sharpens P53's generic split-sign boundary discussion: v+=0 cannot occur here in the interior. There is no extra pi jump.

Cauchy–Schwarz on (sqrt(alpha)c±,sqrt(beta)b±) gives 0<gamma<1 for h>0. Therefore

phi+=phi+atan(2eta s) mod2pi,

(t,r,s,phi)+=(t+,v+,gamma s,phi+atan(2eta s)).

This is the COMPLETE four-coordinate quotient for fixed a,f and declared eta/kappa. Proof of completeness: nonzero orthogonal w,j determine an oriented frame (w/a,j/s,(w×j)/(as)); y is determined by r and its circular phase in that frame. Common SO(3), hence unitary, equivalence removes the frame. Equal four coordinates yield equal successor coordinates, current terminality and next prepared gate. The angular phase is retained instead of quotiented away as in P53's scalarW case. Eta sign becomes observable in this declared phase reference.

## Tangent and failed two-variable closure

Use local coordinates(t,h,s,phi); (t,r,s,phi)->(t,h,s,phi) is a smooth change on r,s>0. Then

dphi+=dphi+[2eta/(1+4eta²s²)]ds,

ds+=gamma ds+s(gamma_t dt+gamma_h dh).

The geometry derivatives are P53's exact rational channel chain; gamma is independent of s when t,h are held fixed. In the two tangent directions dphi and ds at fixed(t,h), the endpoint(phi+,s+) has determinant gamma>0. These are two observable evolving directions when eta!=0,h>0; this regular tangent does not itself prove an autonomous pair.

For Pi=(phi,s), varying h at fixed(t,s,phi) is a fiber direction. An exact symbolic calculation at t=9/20,h=3/25 proves

partial_h gamma²=-212767859808/180776990897 !=0.

Since gamma>0 and s>0, partial_h s+=s partial_h gamma!=0. Hence D(Pi U) does not vanish on ker DPi. By the chain rule no local C1 map T with Pi U=T Pi exists on a full neighborhood of this point. Numerically, at t=.45,s=.3, fixedphi, h=.12 versus .2 gives s+ gap .019859813832745897, while phase+ agrees. Both are strictly admitted states. This is failure of this pair on the declared family, not a universal obstruction to other pairs or invariant restrictions. Invertible recalibration of(phi,s) preserves its fibers and cannot fix this failure.

## Force, energy and clock consequences actually checked

The derived angular increment depends on the declared eta and s; eta=0 gives zero increment, eta and -eta give opposite increments with the SAME geometry/kernel attenuation. Both policies are Hermitian, covariant and admissible on the same gate. The canonical law therefore does not uniquely select angular orientation, a restoring sine law, mechanical inertia or friction. Treating phi as physical pendulum angle would require a bridge: its increment has fixed sign for fixed nonzero eta,s, whereas a librating pendulum angle reverses direction. Phi may instead be a phase variable, but a separate angle/velocity readout and full closure remain necessary. No mechanical sine is inserted into this readout.

Dimensionless kernel attenuation is proved: s+²=gamma²s². Conditional energy hypothesis E2=E0 s², E0>0 with joule units supplied externally, yields E2+=gamma²E2. Equally admissible E4=E0 s^4 yields E4+=gamma^4 E4. The canonical update and gate select neither observable nor E0; both decrease for h>0. Thus an energy monotonicity construction does not derive physical joules or potential. No energy observation is fabricated.

For any additional constant duration H>0 seconds, the event phase-rate readout is nu_H=atan(2eta s)/H. Taking H and cH gives the SAME event trajectory but rates scaled1/c; consecutive-rate acceleration scaled1/c². Equation(162) permits both until independent clock calibration. This explicitly proves absence of an identified frequency/acceleration scale from this event law. These are secants, not a continuous generator. Exact flow compatibility remains a separate obligation.

## Domains, boundaries and stability scope

W is positive trace1 for0<a<=1/2, including pure witness at a=1/2; full selection retains mass1. At a=0 the reference disappears and P53's phase invisibility returns. At r=0 phase is undefined; at s=0 the oriented axis is undefined and preparation vanishes. At eta=0 phase is fixed. u=0/1 boundaries are outside the strict family; rank/terminal behavior must follow canonical rules there. Circular phi needs local charts; avoid branch-cut artifacts by comparing exp(i phi). No global phase chart or infinite forward viability is claimed.

The two observable tangent rows give local smooth dependence, not global dynamical stability. Condition numbers of the phase extraction grow as a,r,s vanish; compact regular margins are needed for any uniform error bound. Synthetic controls only check the stated finite samples; they are not physical robustness evidence. P53's large-s next-domain counterexample prohibits an unconditional persistence guarantee.

## Independent control and next dependency

check.py independently computes60 canonical Ambient SVD endpoints and compares the phase law, natural-frame witness inheritance and arbitrary common-unitary gauge transformations. Maximum errors: phase4.94e-15, gauge1.85e-14, witness6.67e-16. Separate SymPy derivative is exact, not a finite-difference proof. Pair counterexample and all machine values are preserved in controls.json. Fixed seed54 and sample ranges/tolerances are executable. Import update only from the archived experiments/real-eeg-covariance-2026-10-07/experiment.py; do not execute its evaluate(). Run command is in check.py. No measured data, holdout download/access, empirical workflow or new automation.

P54 completes the observable-phase construction and pair-closure investigation with their actual statuses. The physical2D pendulum/force problem remains OPEN. Next necessary single dependency: a declared one-dimensional invariant amplitude curve in(t,r,s), satisfying (T(s+),R(s+))=(t+,r+) with s+=gamma s and forward prepared gate, so that adding this retained phase could give a two-dimensional factor; or a demonstrably closed alternative. A mere fitted curve or frozen hidden amplitude does not meet this obligation. Only after invariant closure can exact clock/generator and physical selection be tested.
