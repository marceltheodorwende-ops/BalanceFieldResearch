# Frozen protocol: component balance and compensation in the stable pair factor

Date: 23 October 2026. BFG-only continuation under MANDATE.de.md.
Research baseline: d925e3edcbb13f7e3a0575534adce00b001ec44b.
Use the unchanged source and invariant full-persistence/simple-spectrum class established in STABLE_PAIR_DERIVATION.md. No spatial bath, stress, clock or physical generator is added.

## Predeclared mathematical questions
E1. In the ordered Y-pair eigenframe derive the Pauli-component map of K_S and the exact defects of all four components. Identify which fixed linear local kernel charges can be conserved for every K_S.
E2. Derive or refute the source-operator identity Phi(K)-K=-1/2 sum_j[T_j,[T_j,K]] and its Hilbert-Schmidt pairing identity. If valid, identify its exact eventwise quadratic gradient representation; do not promote a frozen-event functional to physical energy/action or a global continuous flow.
E3. Test additive compensation by any function of the complementary CURRENT source data (including K_EE,K_SE,Y,F,W) independent of K_SS. Since the complete source update is block diagonal in its channel factors, compare two full inputs differing only in K_SS. Do not choose a compensator backward from the residual.
Exact witness: n=3, Y=diag(1/5,1/4,3/10), F=[[1,1/2,0],[1/2,1,0],[0,0,1]], W=I3/3, P=I3, K_plus/minus=I3 plus/minus sigma_x in the first pair. F fixes a transverse relational reference; no unanchored Pauli coordinate is claimed physical. Both states lie in the established source class.
E4. Inspect the two source analysis branches themselves: V=[T_C;T_B] is the source-normalized local analysis isometry. The constructed joint matrix V K_S V^dagger is a mathematical lift; trace its internal pair space to a 2x2 branch matrix. Test whether that branch-only object can distinguish the two transverse-sign witness inputs. Distinguish branch marginals, joint correlations, source-selected state variables and physical interaction stress.
E5. Test algebraic invertibility versus cone-preserving invertibility: h>0 makes the fixed-event pair map invertible as a real linear map, but does its inverse preserve the positive Hermitian cone? Use I+sigma_x as a fixed output test. This is a scoped order-isomorphism question, not a no-go for physical Lorentz covariance in every completion.

## Evidence and finite controls
Symbolic/rational algebra for the exact witness's alpha, h^2, determinant defects and corrected operator coefficients.
12 mixed complex source preparations: n=3,4,5,6, three each, simple Y spectrum in [1/5,3/10], random F>0 and normalized W, arbitrary Hermitian full K with off-block entries. Hold the currently stable pair frame and test two successive events. At each event compare full plus/minus source updates differing by an embedded transverse pair perturbation. Seed 20261026, tolerance 1e-10 for normalized identities and complement equality. Preserve all failures and source numerical boundaries. No source repair or tolerance fitting.
For each event independently check the Pauli map, double commutator, pairing identity, isometry and joint-lift recovery, branch-marginal insensitivity to a transverse perturbation, and inverse-cone failure. Nonzero exact defects, not count statistics, support the compensation obstruction.
No claim is made about nonlinear local charge identifications, charges mixing pair/complement data, explicitly historical inverse readouts, state-dependent transported charge operators or general selection/seed events.

Outputs: COMPONENT_EXCHANGE_DERIVATION.md, component_exchange_audit.py, component_exchange_results.json; update status, README and narrow CI. Keep all previous physical gates open unless actually established.

## Scope-preserving extension after the first component controls
Add E6 before a final new run: distinguish fixed-charge obstruction from transported observables. Because h>0, the event map is invertible as a real linear map. Test H_0=1, H_(k+1)=h_k H_k along each unperturbed source trajectory, and the exact constancy of (p0,p1/H_k,p2/H_k,p3) in the fixed retained pair frame. This is a derived HISTORY readout, not a source-selected physical four-momentum. It prevents the fixed-identification obstruction from being overstated as a no-go for every possible charge definition. Require normalized residual <1e-10 across the same two-event controls. No new state law or physical input is introduced.


