# Relational two-mode frame and a closed gauge-invariant coordinate factor

23 October 2026. BFG-only continuation. Preregistered checks: [RELATIONAL_FRAME_PROTOCOL.md](RELATIONAL_FRAME_PROTOCOL.md).
Source: pinned complete Dynamic Order, Parts I/II, same full ambient update and unitary quotient. The constructions below are derived mathematical readouts on a stated source domain, not new dynamics or physical space.

## 1. Reference domain and definition

Use the source-invariant class C of STABLE_PAIR_DERIVATION.md with simple spectrum. Let P1,P2 denote its two lowest Y-eigenprojectors, S=P1+P2 and Z=P1-P2.
These projectors are unchanged in aligned full-persistence representatives. Formation F and Witness W are likewise unchanged there.
Define
F_perp=P1 F P2+P2 F P1,
a_F=sqrt[tr(F_perp²)/2].
On the declared chart a_F>0 set
E0=S, E1=F_perp/a_F, E2=-i Z E1, E3=Z.

The chart condition means that formation supplies a nonzero relative phase reference between the selected eigenlines. It is not the assumption that F commutes with Y; indeed that would remove this reference.
F has formation units, so a_F has the same units and each E_mu is dimensionless. No sum of F and dimensionless W is introduced.

## 2. Exact Pauli structure, covariance and persistence

In any pair eigenbasis F_perp=[[0,z],[conjugate(z),0]], a_F=|z|. Thus E1²=S, Z²=S and ZE1=-E1Z. E2 is Hermitian and
E_i E_j=delta_ij S+i epsilon_ijk E_k,
tr(E_mu E_nu)=2 delta_mu_nu.
This is the Pauli algebra on the selected pair; the matrices vanish on its complement. The ordering P1 before P2 fixes the declared sign of E3.

Under a simultaneous source unitary G, every projector and F_perp transforms by conjugation, a_F is invariant, and E_mu transforms to G E_mu G†.
Under an actual source event with successor coordinate matrix V,
E_mu,+ = V† E_mu V,
a_F,+=a_F.
Proof: the invariant-class theorem retains P1,P2, and the full-persistence source update retains F in the aligned frame. Therefore every expression in the definition is retained. This also proves that a_F>0 is an invariant chart condition; it cannot disappear at a finite exact event on this class.

The coordinate scalars
p_mu=tr(E_mu K)/2
are invariant under simultaneous source unitaries. This addresses the earlier gauge qualification: raw Pauli components need a reference, and nonzero formation coherence supplies an explicit internal reference on this chart.
It does not select a physical position system or a measured momentum direction.

## 3. Closed real-coordinate factor on the unitary quotient

For any selected Hermitian block A_S, write a_mu=tr(E_mu A)/2.
It reconstructs A_S=sum_mu a_mu E_mu. Thus the four K coordinates retain the entire local Hermitian kernel, rather than compressing away its reference-relative phase.

In this frame,
Y_S=y0 E0+y3 E3, y0=(y1+y2)/2, y3=(y1-y2)/2,
F_S=f0 E0+a_F E1+f3 E3,
W_S=sum_mu w_mu E_mu.
In particular f1=a_F>0 and f2=0 are built into the chosen chart.
Together with the complementary formation-weighted spectral measure mu_E, the tuple
R=(p0,p1,p2,p3; y1,y2; f0,a_F,f3; w0,w1,w2,w3; mu_E)
is a closed real-coordinate representation of the previous pair/environment factor, after removing its internal U(2) coordinate freedom.

For explicit closure put f_11=f0+f3 and f_22=f0-f3. The source loads are
L_C=sum_(i=1,2) f_ii/(1+y_i)+integral (1+y)^-1 dmu_E,
L_B=sum_(i=1,2) f_ii y_i²/(1+y_i)+integral y²/(1+y) dmu_E,
alpha=L_B/(L_C+L_B), beta=1-alpha.
The successor is
y_i,+=g_alpha(y_i),
mu_E,+=(g_alpha)_* mu_E,
p_+=(p0,h p1,h p2,p3),
h=(alpha+beta y1 y2)/sqrt[(alpha+beta y1²)(alpha+beta y2²)],
while f0,a_F,f3 and all w_mu remain constant.
All entries on the right are in R. This is an explicit II89 closure proof by reconstruction and the existing exact factor theorem, not a numerical inference. The measure is retained; the previously refuted low-moment replacements are not reinstated.

For distinct y1,y2, 0<h<1. Relationalizing the coordinates therefore does not turn the two damped components into conserved charges. Their source units remain formation units, not established joules or physical momentum.

## 4. Witness chart and overlap rotation

If W_perp=P1 W P2+P2 W P1 is nonzero, its amplitude a_W and frame are defined by the same formulas. This provides a source-internal alternative, including when F_perp=0.
On the overlap a_F a_W>0 define
c+i s=tr(P1 F P2 W P1)/(a_F a_W).
The eigenline calculation gives c²+s²=1, and
E1_W=c E1_F+s E2_F,
E2_W=-s E1_F+c E2_F,
E3_W=E3_F.
The transverse coordinate pairs obey the same SO(2) matrix. Both references and their projectors are aligned constants, so c,s are constants along this full-persistence trajectory.

This is a fixed relational change of reference; it is not a physical boost, spatial velocity or evolving spacetime connection. The mathematical source gives both reference candidates. The present construction does not establish that the physical readout must privilege formation over Witness.
An atlas can retain both charts with the explicit overlap rotation. A rule that switches reference at a zero still needs its own continuity treatment; no globally smooth preferred frame is claimed.

## 5. Exact example and the degeneracy boundary

Take the preregistered n=3 data
Y=diag(1/5,1/4,3/10),
F_ii=1, F12=(3+4i)/10,
W_ii=1/3, W12=(1-2i)/30,
and selected K=[[2,1-2i],[1+2i,-1]], all remaining offblocks zero.
The selected F eigenvalues are 1±1/2 and those of W are 1/3±sqrt(5)/30; both complete matrices are positive.

Then a_F=1/2, a_W=sqrt(5)/30,
p_F=(1/2,-1,2,3/2),
p_W=(1/2,sqrt(5),0,3/2),
c=-1/sqrt(5), s=2/sqrt(5).
The source has alpha=119/1993 and h²=9048258/9159761, independently of the nonzero formation offdiagonal in this Y eigenbasis. Both reference descriptions yield the same attenuated operator and transverse magnitude.
Replacing F by I removes the formation chart but retains the Witness chart and its source-consistent component law.

There is a precise obstruction at genuinely symmetric data, not merely a failed normalization:
choose the full tuple K,F,W,Y diagonal with simple Y, and P=I. Relative phase unitaries exp(i theta)P1+P2+(I-S) stabilize the entire state.
Any covariantly assigned transverse operator must then be invariant under those phases. Its pair offdiagonal must vanish. But a Pauli transverse axis must anticommute with Z and square to S; these requirements are incompatible with a zero offdiagonal.
Thus there is no such natural transverse Pauli frame at this admissible state. This does not prohibit full-state references involving offblocks at other states, a K-based self-reference away from its zero, or a chart atlas.

The formation-based frame itself also has no continuous extension across F_perp=0: approach the same diagonal F using F12=epsilon and F12=i epsilon. Their normalized E1 limits differ, with tr[(E1_real-E1_imag)²]=4 for every positive epsilon. The exact checks retain epsilon=1/10 and 1/1000, but the argument is symbolic for every epsilon>0.
No numerical threshold is substituted for this proof. The audit's 1e-12 normalization guard only prevents reporting a frame below its numerical resolution.

## 6. Evidence and the spatial-transport boundary

Fresh controls use the unchanged source after its exact Git-blob check:
- 12 complex preparations, dimensions 3,4,5,6, two events each: 24 source events.
- Eight further simultaneous-unitary source controls.
- Two prescribed source examples, including the Witness fallback: 34 full source calls overall.
- Exact symbolic Pauli algebra, relative rotation, positive-reference witness and phase-boundary identities.

Largest recorded residuals: frame transport <4.3e-14, component update <5.5e-14, reference coordinates <1.5e-13, gauge components <5.2e-14. All satisfy the predeclared 1e-10 tolerance.
The first symbolic Hermiticity check used structural matrix equality and failed before source controls. Exact simplification of the matrix difference proved the same identity; no formula, input or acceptance threshold changed. Reference amplitudes were then simplified for readable output, followed by a fresh final run. No source code was modified.

This result closes an internal gauge-reference gap: the selected pair has explicitly invariant relational coordinates and persistent reference frames on nonempty source charts.
It supplies no inter-event displacement vector, separated event graph, translation generator, length calibration or local current through spatial boundaries. An aligned stationary frame is not evidence of spatial propagation.

The next mathematical scope question is whether broader full-persistence data enter the stable selection class, and how selection/seed changes affect these charts. A physical transport proposal must additionally specify event adjacency and displacement/current maps, and pass closure and covariance checks; these cannot be inferred by renaming the internal coordinates.
