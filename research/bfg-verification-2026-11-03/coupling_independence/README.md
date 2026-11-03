# Coupling independence of the fixed finite BFG event

3 November 2026. Three requested steps: dependency sorting, coupling-uniform consequences, and concrete dependence witnesses. This is a follow-up in the existing verification stage; no new paper or physical rule is introduced.

## 1. What is varied and what is held fixed

The event is exactly Section 12 of DOI 10.5281/zenodo.23897937, including the same neutral response, selection, density loads, reciprocal weights, ambient analysis, intrinsic-Gram output, polar transport and seed/terminal policy. We vary the **initial** source-neutral interface. We do not change it afresh at every event or substitute an alternative successor rule.

For fixed positive formed Hessian H, a neutral metric M>0 and channel L generate `Y0=H^(1/2)L M^-1 L*H^(1/2)>=0`. Whenever this and the supplied other coordinates form a typed finite input, the published event theorems apply. The classification below is about this input family, not all possible historical or physical BFG realizations. It does not derive the unique source preparation of K, densities or P from the earliest axioms.

## 2. Dependency sorting

[dependence_register.csv](dependence_register.csv) classifies all 48 indexed manuscript statements by their relationship to this initial-coupling question. It does not upgrade the previous detailed-review status of other statements. Definitions are not counted as independent dynamical theorems.

| Result | What survives variation of the initial coupling | What is still assumed or can change |
|---|---|---|
| 13.1 Ambient invariants | Every successful output is typed, has 0<Y+<I and does not increase carrier dimension | Success is not guaranteed for every initial coupling; the complete event is fixed |
| 13.2 Accounting | The same formation balance and witness accounting identity | Actual survival mass and seed contribution can differ |
| 14.1 Schur novelty | The equivalence involving commutation remains true on its specified compatible support | Whether a given state commutes, and its exact Schur factors, can differ |
| 26.1 Later lossless selection | Applies after every successful first event, regardless of how the initial load was obtained | The first event may fail; later seed gates can still fail before completion |
| 26.2 Completion/absorption | Every input in dimension n0 terminates or reaches full persistence within at most n0 attempts | Which alternative occurs, its time and resulting carrier dimension can depend on coupling |
| 26.3 Finite budgets | At most n0-1 seeds; same formation upper bound if initial K and rhoF are fixed | Actual seed count, formation stock and first witness loss can differ |
| 26.4 Load collapse | Any full-persistence input with 0<Y<I has the same stated uniform envelope and load limit zero | Individual trajectories, mode ratios and threshold-crossing times can differ |
| 26.5 Kernel convergence | Every infinite successful trajectory has a convergent formation kernel after its finite prefix | Neither a common K-infinity nor a coupling-independent convergence rate is established |
| 26.6 Renewal limitation | No infinite seeding, unbounded carrier growth or positive load floor on an infinite successful orbit | This remains a conclusion about the closed finite event; extra forcing is not silently allowed |
| Geometric construction | Conditional existence theorem for its specified four-mode family and added metric remains available | Not every arbitrary initial interface lies in that family or satisfies its regularity margins |
| RC sector | Its separately stated circuit results do not require a unique initial BFG coupling | They are not consequences of coupling independence or a validation of a universal BFG law |

## 3. Coupling-uniform theorem

**Proposition C1 (uniform over initial interfaces, for the fixed event).** Fix an initial finite dimension n0>=1 and the Section 12 event. For every typed initial state produced by an interface in the family above, either the orbit terminates within n0 event attempts, or it reaches full persistence after m<=n0 attempts and succeeds at every subsequent finite attempt. Across each successful orbit there are at most n0-1 seeds. If K0 and rhoF0 are shared across the family, the same upper formation budget `tr(rhoF0)+(n0-1)||K0||` holds for every member.

For every infinite successful orbit, write X_k for the state after k attempts. For k>=n0+2 its maximal load obeys the **common absolute-index envelope**

`||Y_k|| <= (1/2)(4/5)^(2^(k-n0-2))`.

Each such orbit has a convergent K in a compatible fixed-carrier gauge after completion and tends to a boundary state with Y=0. This does not assert that different interfaces yield the same K limit, density values or final carrier dimension.

**Proof.** Theorems 13.1 and 26.1-26.3 quantify over typed initial states and use no formula selecting the initial L or M. Their dimension/defect argument therefore applies to every family member without an interface-uniqueness premise. Terminated members require no infinite-time continuation claim. For an infinite member let m<=n0 be its completion time. Theorem 26.4 applied with j=k-m gives `||Y_k|| <= (1/2)(4/5)^(2^(j-2))` for j>=2. Since j>=k-n0 and the base lies in (0,1), this is bounded by the displayed common envelope. The positive Schur-product argument of Theorem 26.5 proves K convergence in the orbit's own compatible gauge. At Y=0 the B-load vanishes. The seed and formation budgets are the bounds in Theorem 26.3, with shared initial quantities when those are fixed. QED.

The absolute-index envelope is a direct quantified corollary of the existing paper. It is not an assertion of convergence over an unbounded initial dimension, a common carrier space across the family, a common physical clock or uniform kernel convergence speed.

**Corollary C2.** If the family is restricted at the initial state to P=I and 0<Y0<I, with nonzero positive formation and normalized positive witness, then every member continues indefinitely and has Y_k->0. No seed occurs. The full-persistence invariance removes the alternative terminal prefix in this subclass. No unique initial coupling is needed.

## 4. What actually changes: exact witnesses

### A. Absorption versus infinite continuation

Take K=diag(-1,2), its formed Hessian H=diag(2,3), M=H, P=I and rhoF=rhoW=diag(1,0). Compare L_a=I/2 with L_b=diag(2,1/2). Their loads are Y_a=I/4 and Y_b=diag(4,1/4). The first is in full persistence and continues forever by C2. In the second, the exact selector retains only the second direction, while the witness is entirely in the first: its retained mass is exactly zero and the branch terminates at the first selection gate. Thus initial coupling can determine **which branch of the theorem's dichotomy occurs**. The second input is a typed positive-load state before selection; it is not in C2's open-unit-load subclass. No theorem hypothesis has been silently removed.

### B. Final dimension and formation budget, even when both continue

Take K=diag(-2,-1), H=M=diag(4,1), P=rhoF=rhoW=diag(1,0). Compare Y_a=I/4 with Y_b=[[1/4,1/8],[1/8,1/4]]. Both lie strictly below I and are positive definite. The corresponding channels can be represented with the same H and M by L_a=I/2 and `L_b=H^(-1/2) sqrt(Y_b) H^(1/2)`.

The transverse ranks rank((I-P)Y P) are respectively 0 and 1. The first event therefore reduces to dimension one with full persistence and no seed. The second has two active dimensions. Its analysis has target rows supported on copies of the first source direction, so K+=-2I on the active target. Its one-dimensional emergent block has the simple negative eigenvalue -2, yielding one seed of trace 2 and full persistence in dimension two. Both continue indefinitely, but their final dimensions are 1 and 2, seed counts 0 and 1, and formation traces 1 and 3. The common bound is still respected; the second saturates the n0=2 formation-budget bound. This is a typed-event witness, not proof that every such initial P is generated by an earlier source-preparation law.

### C. Different limiting kernels with the same zero-load limit

Take K=[[0,1],[1,0]], whose formed Hessian is H=2I, set M=H, P=I and both densities to K's normalized negative-ground projector. Compare L_a=I/2 and L_b=diag(1/2,3/4), giving Y_a=I/4 and Y_b=diag(1/4,9/16). Both continue indefinitely. In the isotropic case every Schur factor is one, so K remains exactly its initial value and its off-diagonal limit is 1.

In the anisotropic case the first off-diagonal factor c0 satisfies 0<c0<1. All subsequent factors lie in (0,1], so the limiting off-diagonal entry is at most c0<1. The two K limits differ, even though both loads tend to zero. This infinite-time difference follows from the monotone product proof, not from extrapolating a finite simulation. Its exact first-factor square is recorded in results.json.

## 5. Verification and limits

Run `python coupling_independence/check_coupling_dependence.py` from the parent verification folder. It uses the existing NumPy/SymPy/mpmath/Matplotlib environment. Exact rational/symbolic checks establish the selector masses, transverse ranks, coupling representations and first Schur-factor bound. Fresh, well-separated binary64 calls to the preserved event() confirm the stated finite transitions; they are not certified rank algorithms. Four 90-digit full-support trajectories over 15 recorded states support the load bound, including singular formation densities. The analytic argument supplies the all-time conclusions.

No proof assistant, hardware experiment or new dynamical law was used. The published PDF and baseline event implementation are unchanged.
