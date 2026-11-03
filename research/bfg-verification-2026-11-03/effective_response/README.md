# Identifying the effective neutral response

This is a continuation of the existing BFG research stage, not a new paper or a proposed physical law. A focused source check has not established a derivation of the initial neutral response from the original three capacity operators. The new mathematical result makes the remaining obligation smaller and testable: in the specified quadratic sector it suffices to determine the **minimized source assessment**, without uniquely identifying every neutral channel factor.

The [source symmetry analysis](../source_symmetry/README.md) distinguished matrix-valued and quotient-valued initialization. The earlier [interface classification](../foundation_audit/INTERFACE_IDENTIFICATION.md) classified strictly positive joint quadratic assessments. Both remain valid. Here we classify their effective responses and the irrelevant factor freedom, without equating the finite five-object state with every role in the original nine-role field coordinate.

## 1. What the checked sources already determine

| Source and inspected location | Existing relation | Its input obligation |
|---|---|---|
| April 17, 2025 BFG, section 7.2, printed page 19 | I_B=d(Phi I)/dt and its product rule | Given scalar trajectories or their dynamics; this identity supplies no source-neutral matrix response by itself. |
| Neutral Interface, May 21, 2026, sections 3-5 | Primitive operator roles and Phi[s,N]=<s,E I s>/<s,B N s> | Requires the listed operators and admissible states. The neutral interface operator N is not automatically the September capacity aleph or the response C_N(Y). |
| Compact Recursive Stability, sections 4-5 | I_B=A+B I_B and I_B=A/(1-B) when 1-B is nonzero | Requires its affine coefficients. These scalar A,B are not the finite neutral channel or the quadratic mixed Hessian. |
| Level 0, sections 10.1-10.4, PDF pages 15-17 | Boundary-mediated coupling, conditional separability and an interface-completion score J_int | Requires the configuration decomposition, component functionals, weights and threshold. A threshold on this score does not provide a numerical quadratic source assessment. |
| Canonical Universal Reclosure, September 22, sections 3.1 and 4.1 | K=c+aleph-D_cap, then a separately introduced channel A and Y=A* A | The capacity combination supplies formation; exact neutral elimination supplies the response conditional on A. The inspected clauses do not compute A from those capacities. |
| Same September source, section 4.2, equations 17-18 | H_C=B_C* W_N B_C and Y_C=L_C* H_C L_C | Fixed role-bearing factors determine Y_C. Positivity of this factorization alone does not determine those factors. |

This is targeted reading of the named clauses, continuing the [earlier ten-document search](../foundation_audit/EXISTING_PREMISE_SEARCH.md) and the [global plugin synthesis](../plugin_synthesis/README.md). It is not a proof that no implication can be found elsewhere or derived from a larger formalized source system. The original April 2025 material is retained in this trace. Raw manuscripts and private filesystem locations are not republished.

The existing proposed L0-NC amendment remains proposed: its mixed-Hessian and metric clauses do fix a response in their stated sector. They are not used here as original axioms. No equality between differently named operator roles is inferred from shared words such as 'neutral', 'information' or 'coupling'.

## 2. The effective response is exactly the minimized assessment

Work on fixed finite source and neutral carriers, with reference inner products and a fixed positive definite Hermitian source Hessian H. In the already studied quadratic class write

    J(d,eta) = (||d-L eta||_H^2 + ||eta||_M^2)/2,    M>0.

The joint mixed block is B_mix=-HL and the neutral diagonal block is N_joint=M+L*HL. Exact minimization gives

    min_eta J(d,eta) = d* E d /2,
    E = H - HL (M+L*HL)^(-1) L*H,
    Y = H^(1/2) L M^(-1) L* H^(1/2),
    E = H^(1/2) (I+Y)^(-1) H^(1/2).

All operators must be expressed on the **same source carrier with its joint coordinate relations**; separate eigenvalue lists are insufficient.

**Proposition R1.** For fixed H>0, the map above is a bijection between all positive semidefinite loads Y and all Hermitian E satisfying 0<E<=H. Its inverse is

    Y = H^(1/2) E^(-1) H^(1/2) - I.

**Proof.** Set C=H^(-1/2) E H^(-1/2). The interval condition is exactly 0<C<=I. Its eigenvalues c obey 0<c<=1, so Y=C^(-1)-I is positive semidefinite. Conversely every Y>=0 has C=(I+Y)^(-1) in that interval and reconstructs E. These formulas are mutual inverses. The previous completion identity supplies the same E for any given L,M. QED.

This changes the logical target: a source law determining E is sufficient for Y, even when it does not choose a unique physical L, M or neutral carrier. Determining the mixed block and intrinsic neutral metric is one sufficient route, not the only possible route. This refines the stopping question in the earlier interface report; its classification is unchanged.

The response rank is also intrinsic:

    rank(Y) = rank(H-E).

Indeed H-E=H^(1/2) Y(I+Y)^(-1) H^(1/2); multiplication by the invertible factors preserves rank. If E=H then Y=0. This is a legitimate response boundary, although the finite event may subsequently fail its positive complementary-load gate.

Knowing the minimized quadratic functional on the entire source determines E by polarization, hence determines Y. Knowing its value on one formed ground line generally does not. For H=diag(4,3), E_a=diag(2,1) and E_b=diag(2,2) give the same ground-line value d*E d at d=e_1, but yield respectively Y_a=diag(1,2) and Y_b=diag(1,1/2). Neither pointwise agreement nor separate scalar balance supplies the missing transverse response. The [local information analysis](../local_information/README.md) already explains the distinction between a complete quadratic probe family and one direction; the actual admissible source domain must still be justified.

## 3. Every positive load has a minimal quadratic realization

**Proposition R2.** For fixed H>0 and any Y>=0 of rank r, a realization of the preceding type exists with neutral dimension r. No smaller neutral dimension is possible. Among minimal whitened realizations, the channel factor is unique up to a unitary change of neutral coordinates, with the source frame fixed.

**Proof.** Factor Y=A* A with A mapping the source into C^r and having range C^r; an eigenvalue factor gives such A, including the zero-dimensional carrier when r=0. Choose M=I and L=H^(-1/2) A*. Then the displayed response is exactly Y and the joint form is strictly positive because it is an invertible completed-square congruence of diag(H,M). Any factor through an m-dimensional neutral carrier has rank Y<=m, proving minimality.

If A_1* A_1=A_2* A_2=Y, define U(A_1 x)=A_2 x. Equal Grams imply equal kernels and equal inner products of all images, so this is well-defined and isometric. In the minimal case both ranges are the entire neutral carriers, making U unitary and A_2=U A_1. Over real carriers the same proof gives an orthogonal U. For general M, whiten the neutral coordinate: A=M^(-1/2)L*H^(1/2). QED.

Nonminimal realizations can add uncoupled positive neutral degrees of freedom without changing E or Y. Such degrees cannot be reconstructed from this response alone. If a fuller BFG model assigns them additional roles or dynamics, they may matter there; the finite event's dependence only on its supplied five objects does not erase those roles from the foundational framework.

Thus 'the microscopic channel has not been uniquely derived' is stronger than the obstruction we actually need to resolve. Conversely, factor nonuniqueness by itself is not evidence for multiple finite-event laws: identical Y gives identical neutral input to the specified event when its other inputs agree.

## 4. Why the positive Gram formulas alone do not close the source bridge

For the source's weighted factorization,

    Y_C = L_C* B_C* W_N B_C L_C = A_eff* A_eff,
    A_eff = W_N^(1/2) B_C L_C,       W_N>=0.

When these factors are already fixed in their required roles, the expression determines Y_C exactly. If they are left free, every positive semidefinite Y can be represented, for example by W_N=I, B_C=I and L_C=A for a Gram factor A of Y. This is an algebraic realization test, not a physical assignment of those roles. It proves that the **bare positive-factor grammar** restricts the sign but not the numerical load. Additional source constraints on the factors may restrict the class and must be checked explicitly.

The original capacities c, aleph, D_cap cannot be replaced silently by W_N, B_C, L_C. In particular, the source-neutral elimination, weighted Gram rebuild and scalar information-order feedback are conditional constructions with different inputs. Their valid algebra is preserved by this distinction.

## 5. Exact checks with the same original capacities

Retain the previous milestone's positive capacities

    c=I, aleph=[[2,1],[1,2]], D_cap=[[5,1],[1,2]], K=diag(-2,1).

The real quartic formed-state Hessian is H=diag(4,3). The two **diagnostic**, not adopted, loads from that milestone produce

    Y_1=aleph/4,
    E_1=[[96/35, -8 sqrt(3)/35],[-8 sqrt(3)/35,72/35]],

    Y_2=(aleph/4)^2,
    E_2=[[1344/425,-128 sqrt(3)/425],[-128 sqrt(3)/425,1008/425]].

Both satisfy 0<E_i<H and admit strictly positive joint assessments with that same H. Their different E values identify the actual constitutive freedom left by the enumerated formation-plus-positive-completion packet. This is not a claim that both satisfy every historical BFG requirement. A source implication fixing E would distinguish or exclude them without needing to choose a preferred Gram factor.

The [exact script](check_response.py) verifies five fixtures, including rank two, real rank one, complex rank one and zero response. It checks the forward and inverse formulas, rank identity, joint congruence, nonorthogonal neutral-coordinate invariance and invisible uncoupled padding. Two full-rank fixtures also have explicit minimal-factor equivalence certificates and nested weighted-Gram realizations. The ground-line insufficiency example is exact. These are algebraic controls supporting the written general proofs, not empirical observations or a proof-assistant certificate. Results are in [results.json](results.json).

## 6. Remaining source obligation

The next source task is now precise: identify an accepted BFG functional and admissible variation domain that determine E on the formed source carrier, or an equivalent invariant specification of Y jointly with the original capacities. For a smooth nonlinear functional, an appropriate local Hessian could be a route **if** its carrier, evaluation point, admissible variations and relation to this neutral-eliminated assessment are already justified. Taking an unrelated score's Hessian and calling it E would add a new constitutive identification.

No such implication was established in the clauses checked here. The result narrows the needed derivation rather than asserting that it is impossible. It also avoids demanding unnecessary uniqueness of physical channel factors. The complete finite event remains conditional on its supplied initial state; the original paper and baseline implementation are unchanged.

Source hashes, exact anchors and prior provenance are in [SOURCES.json](SOURCES.json). Reproduce from the research-stage folder:

```sh
python effective_response/check_response.py
python validate_stage.py
```
