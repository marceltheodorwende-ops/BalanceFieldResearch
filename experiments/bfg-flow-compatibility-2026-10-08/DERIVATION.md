# Continuous-flow compatibility of the canonical geometry-delay candidate

8 October 2026. Sole active source: Dynamic Order, SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.

## Single investigation and completion rule
Audit the P44 two-observable candidate against the endpoint-flow obligation. Prove the scope of an orientation obstruction, derive the state-dependent-clock modification, check counterexamples and coordinate signs, and independently verify derivatives and a full nonlinear mechanical comparator. Publish evidence and register/ledger status. No empirical fit before this interface audit; no new experiment, download or holdout access.

## Source and assumptions
Dynamic Order section84 equations(124)–(138), sections62–64 regular differential chain, section9 quotient/gauge, section89 equations(161)–(162) factor and clock, sections68.1/70.4 physical clock. P39/P41/P44 provide the canonical geometry factor, not an ODE. The proof below uses standard chain rule, variational equation, matrix determinant lemma and continuity, explicitly derived here; it is an additional compatibility argument, not an ODE stated in the paper.

Keep exactly P44's preparation: two-dimensional full persistence, 0<Y<I, positive commuting formation with eigenvalues f,2f; labels set by formation projectors; arbitrary K and density W. With p=1/3,
lc=p/(1+x)+(1-p)/(1+y), lb=p x²/(1+x)+(1-p)y²/(1+y), alpha=lb/(lc+lb),
R_i=(alpha+(1-alpha)y_i²)/(1+y_i)².
This canonical map and its rational derivative are smooth and nonterminal on (0,1)². No input or lifted extra variable is added.

At z0=(1/5,7/10), P44 already established det DR(z0)=-321243859375/52720394616576<0. This determinant itself is NOT a new discovery. The new investigation derives its implications for continuous physical-time realization and checks possible clock/coordinate loopholes.

## Fixed-duration flow orientation theorem
Let F be a C1 autonomous vector field on an open planar domain, with a flow defined for the requisite time h>0 and a neighborhood of each initial state. Its derivative M(t)=D phi_t(z) satisfies M'=DF(phi_t(z)) M, M(0)=I. Since the fundamental matrix is invertible, Jacobi's determinant formula gives
 (det M)'=tr(DF(phi_t(z))) det M,
 det D phi_h(z)=exp(integral_0^h div F(phi_t(z)) dt)>0.
This requires neither linearization, small amplitude nor a sine law. For the supplied full sine generator F(theta,w)=(w,-a sin theta-bw), div F=-b and the determinant equals exp(-bh)>0, including b=0. These mechanical parameters remain extra premises.

Suppose a single C1 physical readout Pi is regular (det DPi never zero) on a CONNECTED open set D containing z0 and R(z0), and Pi(R(z))=phi_h(Pi(z)) in a neighborhood of z0. Pi need only be locally invertible everywhere; global injectivity is unnecessary for this derivative argument. Differentiating gives
 DPi(Rz) DR(z)=D phi_h(Pi(z)) DPi(z),
 det DR(z)=det Dphi_h(Pi(z)) det DPi(z)/det DPi(Rz).
Continuity and connectedness force det DPi to have one sign throughout D. The right side is positive; the canonical determinant at z0 is negative, contradiction. By continuity the source determinant stays negative on some neighborhood. Thus no such regular SAME connected two-dimensional readout realizes this candidate there as a fixed-duration autonomous flow. This is a precise obstruction to this preparation/bridge class, NOT to all BFG carriers, nonregular factors, larger embeddings, disconnected charts or altered physical hypotheses.

The restriction is important: an arbitrary regular readout on disconnected source and destination neighborhoods can have opposite determinant signs and evade this argument. Physical preparation must justify the domain, not silently assume it connected or equate such an evasion with a global mechanical instrument.

## Why the positive delay-chart determinant is no repair
P44's H=(g,g composed R-g), g=x-y, has det DH(z0)>0, while det DH(Rz0)<0 in the independent check. The formal coordinate transition DH(Rz0) DR(z0) DH(z0)^-1 has positive determinant. This is algebraically consistent: H reverses orientation between the two locations. Any continuous path in (0,1)² between them crosses det DH=0 by the intermediate value theorem. Consequently H cannot serve as a single regular physical readout on a connected domain containing both. The earlier local inverse theorem remains valid near z0; it never proved a global regular bridge. No earlier result is deleted or relabeled as false.

An ad hoc two-event sampling also fails at this witness: det D(R²)(z0)=det DR(Rz0) det DR(z0)<0 (numerical independent control). This is not a proof about every later event aggregation and is not fractality. Choosing aggregation after seeing data would require a new frozen protocol; none is launched here.

## State-dependent clocks: exact formula and counterexample
For a C1 positive duration tau(z), define E(z)=phi_tau(z)(z). The chain rule gives
 DE=M+F(E(z)) grad tau(z)^T,
where M=D_z phi_t(z) evaluated at t=tau(z). Autonomy yields F(E(z))=M F(z), because translating the initial state along its flow translates the endpoint. Therefore the determinant lemma implies
 det DE=det M [1+grad tau(z) dot F(z)].
The factor is dimensionless: grad tau has seconds per coordinate and F coordinate per second. A fixed clock has factor1. A state-dependent clock satisfying 1+grad tau dot F>0 preserves local event ordering along trajectories and also preserves orientation. Under that additional transversality/ordering premise the same connected-readout obstruction holds. At a zero factor the endpoint map is singular. A negative factor reverses the ordering of nearby endpoints along the same flow.

POSITIVE durations alone do not imply positive factor. Exact counterexample: F=(1,0), tau(x,y)=2-2x on any domain x<1 containing the initial point. The unrestricted flow is translation; E=(2-x,y), tau(.25,y)=1.5>0 and det DE=-1. This is a mathematical clock loophole, not a measured clock, a BFG-derived physical bridge, or a pendulum force. It shows why the paper's positive clock condition cannot silently be strengthened to an orientation theorem without an ordering premise. Time along a single forward orbit still increases for each individually positive duration; the ordering condition compares nearby initial states.

## Physical selection and force-law scope
This step closes the particular P44 continuous-flow audit negatively under constant-duration or ordered state-dependent clock and regular connected physical readout. It rules out all C1 autonomous planar force laws in that bridge class, not just sine, but only on this specified canonical preparation near this witness. Calibration of h cannot fix its determinant sign. A nonordered clock, disconnected/critical instrument, additional states or another carrier could evade it and would need separately declared domains and physical evidence. A higher-dimensional canonical factor is not covered by this planar rank2 conjugacy argument.

No numerical energy, inertia, damping or gravity is inferred from internal loads. The event acceleration previously derived remains a discrete conditional quantity; its equality to an instantaneous mechanical force is not established. Next necessary dependency: select a physically motivated carrier/readout with a consistently regular event-to-event domain and a declared clock ordering rule, then verify its nonlinear generator compatibility. Retain this counterexample as a pre-fit gate instead of tuning angle/clock constants around it.

## Whole-paper search supporting this step
Search across the active paper covered quotient/gauge, spectral selection, regular differential chain, load/formation and historical witness balances, finite seeds, entropy/diversity, viability/transverse certificates, autonomous/driven scalar branches, factor/clock and typed tensor transitions. Sections84/89 and the differential chain directly support the endpoint audit. Positive loads and lossless full persistence guarantee canonical continuation but not physical orientation/clock ordering. Balance/entropy statements do not select a force. Scalar input would change the model. Section90's declared full-persistence tensor replication leaves this geometry factor unchanged; no resolution is inferred just from increasing labels. A lifted physical reduction with additional evolving directions would require a fresh proof. No physical fractality is invoked.

## Verification and robustness limits
Protocol before controls: exact rational source determinant negative; independently differentiated finite differences of R at steps1e-4,1e-5,1e-6, final max error<1e-8; source/destination chart signs explicitly checked; full nonlinear sine plus variational DOP853 control determinant residual<1e-10; exact positive-clock counterexample. Synthetic values a=3,b=.1,h=.1 only verify mathematics/code. They are not measured parameters or fitted development variants.

All checks pass. Finite differences independently agree to3.26e-11; Liouville mechanical residual3.34e-16. No general numerical domain radius certified. The theorem's sign margin persists on some neighborhood by continuity, not on an unspecified global perturbation range. Absolute dynamical/numerical/forecast stability is not claimed. Publication, register and both ledger entries must be verified before completion report.
