# First BFG-only spacetime and conservation investigation

Date: 23 October 2026. Status: mathematical first round, not a physical Einstein derivation.
Authority and predeclared checks: [MANDATE.de.md](MANDATE.de.md), [PROTOCOL.md](PROTOCOL.md).
Active source: *Dynamic Order*, 8 October 2026, Parts I and II, source hash in SOURCE_MANIFEST.json. No external physical theory is used as a BFG axiom.

## 1. Exact source sector and coordinate alignment

[SOURCE BFG] Write the finite source tuple as Xi=(K,F,W,Y,P), with K Hermitian, F positive formation, W positive trace one, Y positive load, and P an orthogonal carrier. II84 gives the ambient update, II85 its unitary quotient, II86 its balances, II89 its fiber criterion and extra clock, II91.1 its optional gravitational completion.

Assume a nonterminal autonomous event on full persistence:
P=I, 0<Y<I, F>0 and W>=0 with tr W=1.
Then Q=P_sel=P_G=I, no seed complement exists, and the successor has the same dimension.
Define C=(I+Y)^(-1), B=YC, positive scalar loads
Lambda_C=tr(FC), Lambda_B=tr(F Y^2 C),
alpha=Lambda_B/(Lambda_C+Lambda_B), beta=1-alpha,
M=alpha C^2+beta B^2 and
T_C=sqrt(alpha) C M^(-1/2), T_B=sqrt(beta) B M^(-1/2).

[BFG DERIVED under these assumptions] Align the successor SVD frame V back to the source frame. The complete update becomes
Y_+=M, K_+=Phi_Y(K)=T_C K T_C+T_B K T_B, F_+=F, W_+=W, P_+=I.
Indeed the ambient SVD has U=[sqrt(alpha)C;sqrt(beta)B] V Sigma^(-1), with M=V Sigma^2 V^dagger; R4 is V^dagger. This is a representative of the actual quotient event, not an altered rule. Every T is a positive self-adjoint function of Y and sum_j T_j^2=I. Alpha remains the source-derived function of F,Y.

## 2. A real conserved kernel scalar, and its limits

[BFG DERIVED] tr K_+=tr K on this full-persistence sector.
Proof: cyclic trace gives tr Phi_Y(K)=tr[K sum T_j^2]=tr K.
Formation stock tr F and tr W are also preserved here; they are different quantities.

In a Y eigenbasis, K_+,ij=h_ij K_ij, where
h_ij=(alpha+beta y_i y_j)/sqrt[(alpha+beta y_i^2)(alpha+beta y_j^2)].
Cauchy-Schwarz applied to (sqrt(alpha),sqrt(beta)y_i) gives
0<h_ij<=1, with equality iff y_i=y_j.
Hence tr K^2-tr K_+^2=sum_ij (1-h_ij^2)|K_ij|^2>=0,
with equality iff [Y,K]=0. This overlaps the repository's existing Schur-multiplier result; it is applied here to conservation candidates, not claimed as a new classification.

For a fixed Hermitian observable A carried through the frame alignment, tr(AK) is preserved for every Hermitian K in one event iff Phi_Y(A)=A iff [A,Y]=0.
Proof: Phi_Y is self-adjoint for the Hilbert-Schmidt pairing; then use the strict off-block factors above.
For simple Y, this fixed space has real dimension n. On the autonomous full-persistence trajectory, each Y_+ is a function of Y, so projectors of the initial Y continue to commute with later Y. Their block-trace charges are conserved when those initial projectors are retained as history data. This does not mean tr(Y_k K_k) is conserved while Y_k itself changes.

[OPEN PHYSICAL IDENTIFICATION] K is not a source-selected Hamiltonian in joules; tr K can have either sign and has formation units. Its conservation supplies no physical normalization, spatial flux or Lorentz transformation law. Other fixed-block weights are also conserved; the finite law has not selected their physical combination.

## 3. A weighted-energy candidate fails conservation AND scalar fiber closure

Consider exactly
Y_a=diag(1/4,1/2), Y_b=(3/8)I,
F=[[1,1/2],[1/2,1]], W=I/2, P=I, K=[[0,1],[1,0]].
Both are admissible full-persistence inputs. F has eigenvalues 1/2,3/2.
They have identical proposed scalar readouts
Pi=(n,tr K,tr F,tr W,tr Y,E_F), E_F=tr(FK):
Pi_a=Pi_b=(2,0,2,1,3/4,1).

For Y_a, Lambda_C=22/15, Lambda_B=13/60, alpha=13/101 and
h_12^2=1152/1295, 0<h_12<1.
Thus E_F,+,a=sqrt(1152/1295), whereas for scalar Y_b all h_ij=1 and E_F,+,b=1.
This is an exact algebraic counterexample, not a floating discrepancy.

[REFUTED IN THIS CANDIDATE CLASS] E_F is not universally conserved; Pi is not an autonomous closed physical state under the II89 fiber criterion. Adding n and these trace summaries does not repair it. This does not refute closure on the complete tuple or every possible richer projection.
The general defect is
E_F,+-E_F=tr[(Phi_Y(F)-F)K].
In particular conservation for all K requires [F,Y]=0. Keeping noncommuting formation/load alignment can therefore be necessary.

## 4. The full-persistence charge cannot be globalized silently

Protocol C3 first specifies P=diag(1,0), Y=I/2, F=W=P, K=-I.
Here analysis rank is one, so K_+=(-1), tr K changes from -2 to -1 and there is no seed complement. The protocol's initial expectation of a nonempty complement for this particular input was incorrect; the rank argument identifies that before new numerical execution. Both the original test and this correction are retained.

For a separate seeded case C3b, set v=(sqrt(3)/2,1/2), P=vv^dagger, F=W=P, Y=diag(1/4,1/2), K=diag(-1,-2).
Selection has no loss. Each analysis channel has range in span(v), and its two source rows are independent because y_1!=y_2 and both v coordinates are nonzero. Thus analysis rank is two.
Since <v,Kv>=-5/4, the complete inherited kernel is K_+=-(5/4)I_2, with trace -5/2 instead of -3. The one-dimensional complement has a simple negative eigenvalue -5/4 and seeds formation stock 5/4.
Consequently F stock changes from 1 to 9/4, consistent with II86 and zero selection loss.

[REFUTED IN THIS EXTENSION] tr K is not a conservation law across all admissible carrier/rank/seed events. A global physical charge would require the complete accounting of these events, not extrapolation from P=I.

## 4a. A source-computed signed kernel flux for general nonterminal events

Split the actual analysis isometry U into source-space blocks U_C,U_B, each n by r, and define D=U_C U_C^dagger+U_B U_B^dagger. No new source variable or physical law is needed to compute D. Since K_+=U^dagger(K direct-sum K)U, cyclic trace gives
tr K_+-tr K=tr[K(D-I)], D>=0, tr D=r.
This is valid for every nonterminal source event, including rank change and seeding. Seed formation changes F, not this formula for K_+.

Define the source-computed signed outflow J_K=tr[K(I-D)]. Then tr K_+-tr K=-J_K. The trajectory identity
tr K_N+sum_(k<N) J_K,k=tr K_0
is exact through arbitrary sequences of nonterminal events. It is a history balance, not a state-only invariant of Xi, a positive reservoir, or a spatial four-current. The terminal output has no canonical successor K and is outside this identity unless a separate export convention is supplied.

In full persistence D=I. In C3, D=diag(1,0); in C3b D=2P and J_K=-1/2. The latter D has eigenvalue 2, so D need not be <=I and the signed flux need not be nonnegative. This gives a concrete accounting term that a future physical bridge must interpret rather than suppress.

## 5. What contraction says about scalar energy

[STANDARD MATHEMATICS APPLIED TO BFG] On the selected scalar branch f(y)=2y^2/[(1+y)^2(1+y^2)] with 0<y<1, f(y)<y and f^k(y)->0. If H(y) is invariant, H(f(y))=H(y), and extends continuously to 0, then H(y)=H(0). Proof: iterate and take the limit.
This excludes nonconstant continuous-at-the-limit conserved energies depending only on y, with the other scalar-branch constants fixed. It does not exclude constants depending on inherited F,K, singular readouts, histories or additional variables.
For the declared driven contraction F_d(y)=f(y+d) on [0,1/4], 0<d<3/4, every continuous invariant on that interval is constant by convergence to y_d*. This uses the extra input assumption, not the autonomous law.
A continuous finite-valued state clock N cannot obey N(F_d(y))-N(y)=1 throughout this interval: at y_d* the equation is 0=1. A clock singular at the limit or an explicit event history is an extra choice.

## 6. Two internal-metric obstructions, precisely scoped

[STANDARD MATHEMATICS] If G=I+Y>0, an injective pullback E^dagger G E is positive. It cannot have Lorentz signature. This addresses a direct identification/pullback of internal Gram geometry, not all emergent event-space constructions.

[BFG SYMMETRY + STANDARD MATHEMATICS] At a fully isotropic n>1 state K=kI, F=fI (f>0), W=I/n, Y=yI, P=I, any Hermitian internal metric assigned naturally under all simultaneous U(n) conjugations commutes with every unitary. It is cI. An internal natural rank-one time projector is likewise impossible: invariant projectors are 0 or I.
The proof concerns operators on the SAME internal H. It does not prohibit a Lorentz form on a different real representation space. It is therefore essential to test that alternative rather than turn this obstruction into a universal no-go.

## 7. Constructive BFG-internal alternative: the Hermitian two-mode carrier

[STANDARD MATHEMATICS APPLIED TO AN ADMISSIBLE n=2 BFG SECTOR]
Let V_evt=Herm(C^2), a real four-dimensional observable/variation space.
With Pauli coordinates X=x0 I+x1 sigma_x+x2 sigma_y+x3 sigma_z,
q(X)=det X=x0^2-x1^2-x2^2-x3^2.
Its polarized form has inertia (1+,3-); reversing overall sign gives the alternative convention. The future cone x0>=|x| is exactly X>=0.
This produces an algebraic Lorentz carrier from two complex internal modes without converting positive G into an indefinite metric.

For A in SL(2,C), det(AXA^dagger)=det X; for unitary source changes, X->UXU^dagger fixes x0 and rotates the spatial Pauli directions. These are standard determinant identities. The source's unitary coordinate covariance alone does NOT generate all physical boosts, physical translations or an event manifold.
An n-dimensional internal space has n^2 real Hermitian directions; only n=2 gives four by this construction. Neither finite rank nonincrease nor the tensor-lift theorem selects n=2 universally. A source-selected two-mode sector, locality and a clock remain necessary. Pauli components change under the source unitary gauge: the four coordinates are a covariant carrier, not four invariant physical observables on the quotient. Observable spatial directions need relational reference data. At a fully isotropic n>2 state, the same stabilizer argument in section 6 also prevents a natural internal rank-two projector; the two-mode selector cannot be assumed globally unique.

The aligned full-persistence kernel channel is positive and trace preserving, so it maps this future cone into itself and leaves x0 fixed. This is a genuine algebraic causal-cone property in the declared carrier. It is not yet a propagation-speed or physical-causality theorem.

For the Y_a,F pair of section 3, Phi_Y acts in Pauli coordinates by
(x0,x1,x2,x3)->(x0,h_12 x1,h_12 x2,x3).
Thus there are two unchanged components and two damped components. A fixed four-component identification with energy-momentum fails componentwise conservation on this closed tuple.
For X=I+sigma_x, q(X)=0 but
q(Phi_Y(X))=1-h_12^2=143/1295>0.
[REFUTED IN THIS IDENTIFICATION] This BFG event is not a Lorentz or conformal Lorentz frame transformation for the unmodified determinant form. A frame transformation must preserve the null cone.
This does not refute Lorentz-covariant dissipative physics with additional matter/environment fields, nor a different source-derived metric. No such fields or retuned metric have been added here.

## 8. Endogenous Y dynamics also needs a bridge

At Y=yI, F=I, P=I in n=2, differentiate the ACTUAL aligned Y update M(Y), including alpha(Y):
DM_y(E)=a E+(lambda-a)(tr E/2)I,
a=2y(1-y)/[(1+y^2)(1+y)^3], lambda=f'(y).
At y=1/2, a=16/135 and lambda=224/675.
Proof: dalpha=(2y/(1+y^2)^2)(tr E/2); the correct fixed-alpha derivative is 2[(1-alpha)y-alpha]/(1+y)^3. At scalar Y it gives aE, and the scalar-sector derivative must be f'(y). Substitution gives the stated trace correction.

Correction, 23 October 2026: the earlier printed general expression for a omitted the beta factor on y. The numerical audit already used the correct special value 16/135 at y=1/2. The general formula above is corrected; the original checked point values and determinant defect are unchanged. STABLE_PAIR_DERIVATION.md and stable_pair_audit.py add a symbolic derivative identity and full-source checks at three scalar points.
The null tangent E=I+sigma_x is sent to lambda I+a sigma_x, with
q(DM(E))=lambda^2-a^2=43776/455625>0.
The temporal/spatial scale ratio lambda/a=14/5 is not one. The determinant form alone therefore does not make the canonical Y step a Lorentz/conformal transformation. This is a derivative at a scalar state, not a stationary physical vacuum or a proof against every Lorentzian dynamics. A state-dependent conformal metric would be an additional selection problem and is not fitted here.

## 9. Two mathematically valid shortcuts that do not derive physics

For any scalar observable M of any deterministic update U, define a reservoir by
r_+=r-[M(U Xi)-M(Xi)].
Then r+M is conserved by definition. Positivity, finite resources, physical coupling and units do not follow. On the explicit seeded case, identifying M=tr F would require drawing 5/4 formation units from such a reservoir; its existence is not a source theorem.

On a fixed real coordinate stratum, the multiplier action
S=sum_k lambda_k dot [x_(k+1)-U(x_k)]
has multiplier equations enforcing any U whatsoever. Variation in x adds adjoint equations for lambda; lambda=0 lifts every source trajectory. This proves formal action encodability, not a selected physical action, positive energy or a Noether stress tensor. Across rank/terminal changes even this chart needs separate typing.

These observations distinguish useful bookkeeping/variational representations from the missing physical selection. They are not impossibility theorems.

## 10. Joint conclusion and next exact dependency

Already derived here: a sectorial conserved tr K; characterization of fixed linear K charges; counterexamples to globalizing tr K and to conserving/closing E_F; a concrete four-real-dimensional determinant carrier with a future-cone property; exact null-cone defects for two canonical dynamics candidates.
None supplies a source-selected physical T_mu_nu, a local translation/diffeomorphism symmetry, a physical action with metric variation, or an Einstein limit. Global scalar trace conservation is not local covariant conservation. A covariantly conserved stress also would not imply a general global energy without suitable symmetry/boundary data.

The next constructive BFG question is now narrower:
Can the FULL BFG source select a two-mode local event/observable sector (rather than choosing n=2 externally), define its inter-event spatial transport and clock, and map source variations to a conserved total four-current including exchange at selection/seed events?
A valid candidate must specify domain/codomain, units and quotient covariance BEFORE evaluating a desired Einstein equation, satisfy II89 fiber closure (or explicitly retain necessary history), account for the demonstrated defects, and derive its symmetry/action rather than import them.

No unique such selector, spatial current or source action has been identified in the inspected source. This first round ends with those OPEN dependencies, not a fitted Lorentz sign, invented reservoir, or claim of completed gravity. A future proposal may overcome these scoped obstructions and must be tested against the same witnesses.



Runde 24: [Uniformes unteres Paar-Gedächtnis](LOWER_PAIR_MEMORY_DERIVATION.md) beweist am relativen Rand summierbare untere Aufspaltung und einen allzeitlich beschränkten lokalen Kerneldefekt. Die exakte positive-Last-Einzelschrittschranke wird von der noch offenen Quellen-Summierbarkeit getrennt.


Runde 25: [Positive-Last-Lyapunov-Übertragung](LOWER_PAIR_LIFT_DERIVATION.md) schließt die untere Summierbarkeitslücke in der ausgewiesenen n=4-Familie. Uniforme lokale Kernel-Gedächtnisschranke für die volle Quelle; Auswahl, Transport und physikalischer Viererstrom weiterhin offen.
