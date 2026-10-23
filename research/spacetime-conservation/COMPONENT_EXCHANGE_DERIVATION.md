# Component balance of the stable BFG pair: damping, compensation and transported charges

Date: 23 October 2026. BFG-only continuation under MANDATE.de.md.
Prerecorded checks: COMPONENT_EXCHANGE_PROTOCOL.md, including the scope-preserving transported-observable amendment.
Source: complete Dynamic Order, Parts I and II, unchanged pinned ambient update.
Domain: the autonomous full-persistence/simple-spectrum class in STABLE_PAIR_DERIVATION.md. No physical clock, spatial bath, stress operator or external evolution law is assumed.

## 1. Exact componentwise source balance

[SOURCE-DERIVED ON THIS DOMAIN]
In the retained ordered pair eigenframe Y_S=diag(y1,y2), y1<y2, write
K_S=p0 I+p1 sigma_x+p2 sigma_y+p3 sigma_z.
The normalized source channel factors are diagonal:
T_C,i=sqrt(alpha)/sqrt[alpha+(1-alpha)y_i^2],
T_B,i=sqrt(1-alpha)y_i/sqrt[alpha+(1-alpha)y_i^2].
Their squared entries sum to one for each i, and
h=sum_j T_j,1 T_j,2
 =[alpha+(1-alpha)y1 y2]/sqrt[(alpha+(1-alpha)y1^2)(alpha+(1-alpha)y2^2)].
As y1!=y2 and 0<alpha<1, Cauchy-Schwarz gives 0<h<1.

The ACTUAL pair event is therefore
(p0,p1,p2,p3)_+=(p0,h p1,h p2,p3),
Delta p=(0,-(1-h)p1,-(1-h)p2,0).
This is a finite event identity, not a differential approximation. The components have K/formation units; they have not been identified with physical energy or momentum.

The two transverse components rotate together under residual pair rephasing; the damping is independent of that basis choice. To make an individual transverse readout source-relational, one may use nonzero off-diagonal F (or separately justified reference data) to fix its phase.
For example the normalized off-diagonal part P1 F P2+P2 F P1 supplies sigma_x up to its declared normalization. On the stable class the spectral projectors and aligned F are retained, so that relational observable is fixed. This is a covariant source readout, not an assertion that an unanchored Pauli coordinate is a physical momentum.

For any FIXED Hermitian local A, tr(A K_S) is conserved for every K_S iff [A,Y_S]=0. The fixed-charge space is span_R{I,sigma_z}, of real dimension two. Thus four independent fixed linear pair charges are not supplied by this channel.

## 2. An exact eventwise dissipative operator identity

Because both source T_j are Hermitian and sum_j T_j^2=I,
Phi(K)-K = -(1/2) sum_j [T_j,[T_j,K]].
Proof: expand the double commutators; the sum is
sum_j(T_j^2 K+K T_j^2-2T_j K T_j)=2K-2Phi(K).

For Hermitian A,K and the Hilbert-Schmidt inner product,
tr[A(K-Phi(K))]=(1/2)sum_j <[T_j,A],[T_j,K]>_HS.
In particular
tr[K(K-Phi(K))]=(1/2)sum_j ||[T_j,K]||_HS^2 >=0.

[STANDARD QUADRATIC GRADIENT REPRESENTATION]
For the FROZEN event factors define the mathematical functional
D_(Y,alpha)(K)=(1/4)sum_j ||[T_j,K]||_HS^2.
Its Hilbert-Schmidt gradient is (1/2)sum_j[T_j,[T_j,K]], so the exact K event can be written K_+=K-grad D.
This identifies an eventwise convex dissipative structure. D has squared formation units. It is not physical energy, not a Lorentzian action, and not a stationary-action derivation of the whole BFG tuple. In actual source evolution Y and alpha change; a single fixed functional or continuous-time gradient flow is not established by this identity.

The local defect K_S-Phi(K_S) is traceless. When transverse components are nonzero its eigenvalues have opposite signs. Calling that matrix a nonnegative exported-energy operator would be an additional unjustified interpretation; stress components need not themselves be positive.

## 3. No independent-complement compensation for a fixed transverse charge

Let R denote ALL current source data other than K_SS: Y,F,W,P, K_EE, K_SE and K_ES, in the retained pair/complement splitting. This may include the pair's F,W,Y data; it excludes K_SS itself.
On full persistence the source factors are functions of Y and block diagonal. Therefore
K_EE,+=sum T_E K_EE T_E,
K_SE,+=sum T_S K_SE T_E,
and all other R updates are independent of K_SS.
No pair-diagonal perturbation is transferred into these complement/cross blocks. This is a source-algebra statement, not an assumed isolation from a physical environment.

Suppose a total candidate has the form
Q_A(Xi)=tr(A K_SS)+q(R),
where A is fixed under the retained frame transport and q is ANY single-valued function of R.
Compare two inputs with identical R but different K_SS. Their R_+ are identical. If Q_A is conserved for every such input, subtracting the two conservation equations gives
tr[A(Phi(Delta K_SS)-Delta K_SS)]=0 for every Hermitian Delta K_SS.
Hence Phi(A)=A, so [A,Y_S]=0.

[SCOPED OBSTRUCTION]
An independent-complement additive charge cannot repair either transverse fixed linear pair charge, and cannot turn four independent fixed linear pair components into four conserved totals. This applies even when q is nonlinear in the specified complementary data.
It is NOT a no-go for nonlinear local identifications, charges mixing pair and complement, state-dependent/transported A, or an explicitly enlarged history state. Those alternatives need separate definitions and derivations.

### Exact source witness inside the invariant class
Y=diag(1/5,1/4,3/10),
F=[[1,1/2,0],[1/2,1,0],[0,0,1]],
W=I3/3, P=I3,
K_plus/minus=I3 plus/minus (sigma_x direct-sum 0).
Both input kernels are positive semidefinite and are admissible full-persistence kernels. Their R data coincide. F fixes the transverse reference, so the sign difference is not removed by a common source gauge preserving the remaining tuple.

The exact source alpha is 119/1993 and h^2=9048258/9159761.
The pair components are initially (1,+/-1,0,0) and subsequently (1,+/-h,0,0).
All complementary successor data are identical in the two cases.
The required compensator increments would be +(1-h) and -(1-h), with h approximately 0.9938947961370511. A single q(R_+)-q(R) cannot equal both. This proves the obstruction with the actual source, without fitting a cancellation term.

## 4. Inspecting the source analysis branches does not supply the missing charge

The normalized local analysis isometry V=[T_C;T_B] comes from the same source ambient analysis, with V^dagger V=I.
One can CONSTRUCT the joint block matrix L(K)=V K V^dagger. It satisfies
V^dagger L(K) V=K,
and summing its diagonal branch blocks gives Phi(K).
Its 2x2 branch marginal is
B_ab(K)=tr(T_a K T_b)=tr(T_b T_a K).
Because T_a T_b are diagonal in the pair Y frame, B_ab depends only on the two diagonal K entries. It cannot distinguish the exact +/-sigma_x witness, although their transverse deficits are opposite.

Thus a branch-only charge, added to the independent complementary data of section 3, also cannot compensate that fixed transverse charge for both witness states.
The JOINT matrix L(K) does distinguish the inputs; the source analysis has a mathematically available correlation structure. That does not derive physical interaction stress.

Important typing: L(K)=V K V^dagger is a derived mathematical lift, NOT the source ambient K direct-sum K used to define K_+=V^dagger(K direct-sum K)V, and NOT a persistent extra variable already in Xi. Replacing one by the other would change the model. Selecting arbitrary joint compensators solely to cancel a defect would repeat the forbidden backward-construction shortcut.

## 5. Invertible as a linear map, not as a positive-cone automorphism

All component multipliers are nonzero, so Phi is invertible as a real linear map on Herm(C^2):
(p0,p1,p2,p3) maps backward to (p0,p1/h,p2/h,p3).
This attenuation is not a proof of algebraic information loss when the channel factors are known.

But take the positive, determinant-null OUTPUT X=I+sigma_x. Its unique inverse is I+sigma_x/h, with determinant
1-1/h^2 = -111503/9048258 <0
for the exact witness; its smallest eigenvalue is 1-1/h<0.
Therefore the inverse is not positive on the entire positive cone. The actual event is not a Lorentz/conformal cone automorphism. This is a standard order-theoretic property of this fixed event, not a universal rejection of every physical completion or calibrated inverse readout.

## 6. Transported observables: a valid formal escape, with its cost

The fixed-charge obstruction must not be overstated.
In the retained pair frame define the derived trajectory record
H_0=1, H_(k+1)=h_k H_k.
Then H_k>0 for every finite number of exact events, and
(p0,k, p1,k/H_k, p2,k/H_k, p3,k)
is constant along the full-persistence trajectory.
Equivalently choose dual observables A_(k+1)=Phi_k^(-1)(A_k); the adjoint/self-adjoint pairing gives conservation.

This is a mathematically valid history-dependent readout constructed from the SAME source channel, without modifying the kernel. It does not single out a physical momentum: it requires an initial reference and accumulated inverse attenuation, and the source has not selected its units, clock, spatial translations, stress interpretation or uniqueness.
Any invertible linear event admits analogous inverse-transported coordinates. Their existence alone does not produce a Noether law.

One can also pull back the initial determinant form to a history-dependent quadratic form
q_H(p)=p0^2-p1^2/H^2-p2^2/H^2-p3^2.
The event together with H_+=hH preserves this form. This is an algebraic transported metric on a trajectory-augmented carrier, not a metric on independently derived spacetime, a new source field equation, or a repair of the earlier fixed-metric null-cone test.
No uniform infinite-time numerical conditioning or finite-precision nonunderflow of H is claimed.

## 7. Fresh checks and scope

component_exchange_audit.py verifies the exact algebraic witness, component map, double commutator, pairing, branch equality and inverse-cone determinant.
It then tests 12 mixed complex preparations across two successive events each (24 paired events, 48 complete source calls), with nonzero cross-block source kernels, using the unchanged source pin and predeclared tolerance 1e-10.
Maximum normalized residual is below 4e-15 across component, double-commutator, pairing, complement independence, source-analysis lift, branch marginal and dual-history-charge controls.
No inputs, coefficients, source tolerance or original source code were changed. The original finite-precision rank limitation remains documented by the first audit.

## 8. Updated scientific dependency

Now known: the stable current-state pair factor has an exact dissipative component balance; independent current complementary data and the pure analysis-branch marginal cannot supply a compensating fixed transverse charge. Formal four-charge conservation is possible with inverse-transported observables/history, but is not a source-selected physical law.

Next distinguish the remaining candidates BEFORE claiming a full energy-impulse current:
- a source-derived relational observable/clock/translation rule that selects the transported readout, rather than choosing it to make charges constant;
- a genuinely source-defined joint interaction functional with variations that yield both coupling and current;
- explicit current transition rules outside full persistence, including selection/seed/terminal accounting.

There is no derived spatial locality or common physical action here. The component obstruction narrows the simple additive interpretation; the transported-observable construction shows precisely why it cannot be called a universal impossibility theorem. Einstein dynamics remains open.

