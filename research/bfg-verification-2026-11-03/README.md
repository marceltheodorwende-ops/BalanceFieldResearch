# BFG verification and RC feasibility — 3 November 2026

Research stage for **The Balance Field Gleichung: Finite Dynamics and Physical Correspondence in RC Models**, DOI [10.5281/zenodo.23897937](https://doi.org/10.5281/zenodo.23897937). [Published paper](../../papers/finite-dynamics-rc-models-2026-11-02/README.md).

The latest [source symmetry analysis](source_symmetry/README.md) distinguishes a unique matrix initializer from a unique joint state class. K-only covariant matrix rules are spectrally restricted, while a unique quotient class can be noncommuting. The original three capacity operators retain joint information lost in K. Exact commutant and event checks establish these conditional results without selecting a new physical initialization law.

The subsequent [effective response analysis](effective_response/README.md) proves that, for a fixed positive source Hessian H, determining the minimized source assessment E is equivalent to determining Y. A unique microscopic channel is unnecessary for the supplied finite event: minimal Gram factors are equivalent up to neutral coordinates. Five exact fixtures and a focused source check including April 2025 distinguish this reduced obligation from still-unproved constitutive identifications.

The [functional Hessian audit](functional_hessian/README.md) then tests actual BFG assessment candidates. It proves a conditional nonlinear Schur-reduction criterion, distinguishes tangent curvature from the exact finite completion, and checks a flat direction of the displayed neutral-interface Lyapunov cost. The September source explicitly preserves its master Gram rather than replacing it with a level-specific Hessian. A source-derived joint assessment fixing initial E remains unresolved.

The next [admissible quotient analysis](admissible_quotient/README.md) uses the BFG-Engine stability sources to test whether normalization or coordinate equivalence removes the flatness. It proves the residual-rank criterion for positive quotient curvature and supplies an exact normalized, fixed-information family with different joint invariants and zero displayed Lyapunov cost. This is a counterexample to the enumerated stability packet's automatic curvature claim, not to every historical BFG axiom or the specified finite event.

The [role information analysis](role_information/README.md) gives a complete finite moment diagnostic for a pure state relative to one Hermitian information operator. In the source's conditional two-mode branch, normalization and known mean information suffice for that class. Forty-eight exact reconstruction fixtures passed. Identity continuity does not itself select an initial value, and even complete primitive state moments do not determine a neutral response without a source bridge. Mixed densities require additional information.

On **4 November 2026**, the [recursion compatibility audit](recursion_compatibility/README.md) derives an exact test for simultaneously identifying older normalized/conjugate fixed points with a retained neutral response. Under the explicit canonical comparison, the older cost obeys a sharp lower bound in the mean load; zero cost forces a zero-load direction. Exact phase and nonselfadjoint exceptions delimit the theorem, and one fresh preserved event passes with positive loads. None of the comparison identifications is adopted as an origin law.

The [direct initial-Y closure check](initial_y_closure/README.md), also dated **4 November 2026**, evaluates the existing explicit formula Y=(H_*^(-1/2) aleph_0 H_*^(-1/2))^2, traces its two source-neutral identifications to their still-proposed L0-NC status, and proves the full-selection criterion -H_*<aleph_0<H_*. The existing two-dimensional fixture succeeds and the scalar Y=1 boundary terminates as expected. The candidate computation is complete conditionally; its derivation from the earlier assumptions remains unestablished. The proposal is not adopted.

The [capacity-Gram follow-up](capacity_gram/README.md) reduces the candidate response to the invariant condition B M^(-1) B*=aleph_0 H^(-1) aleph_0. A screen of 75 deduplicated extractions and targeted source reading retains the existing B_C=D_cov c relation. A rank test rules out one literal finite-composition identification for the proposal's example; a positive-field control shows why differentiation is different and needs field-derivative data. The source implication of the target identity remains open; no proposed rule is adopted.

The requested [BFG-Engine equation synthesis](engine_gram_equation/README.md) verifies all 20 bundled source fingerprints, traces the candidate runtime without modifying it, and works out the invariant equality T^dagger W_N T=aleph_0 H^(-1) aleph_0. Gauge and nonorthonormal-coordinate covariance are checked. A finite theorem gives exact kernel conditions and an explicit positive-weight completion, with six algebraic controls. This completes the equation's formulation and solvability analysis; reverse construction of its weight is not a source derivation of initial Y.

The [explicit completion check](engine_gram_equation/COMPLETION_CHECK.md) fixes the requested endpoint: a source-derived unique initial Y, allowing factor freedoms that leave Y unchanged. Coordinate formulation and conditional metric completion are already complete subtasks. The original-Y source implication remains open, with a direct positive-weight freedom control. Further work is restricted to that implication; unrelated theory or empirical goals are not added to the acceptance conditions.

## Results of the first milestone

- An indexed register of 48 numbered statements, with original statement text, available adjacent proofs, labels and PDF pages. Seven central dependencies received a focused analytic review; the remaining rows are explicitly pending detailed adversarial review. Definitions and limitations are indexed but are not treated as positive theorems.
- A written scalar proof gives the stronger scalar-only bound `y_k < 2^(-1-2^(k-1))` for k>=1 and 0<y0<1. Five symbolic identities and 816 exact rational steps passed. No priority claim or proof-assistant certificate is made.
- The published finite-event control implementation was freshly replayed: 120 random cases, 40 high-precision cases and nine rational cases passed. This is a replay of existing code, not an independent reimplementation.
- A new synthetic three-node RC pilot explores component mismatch and finite measurement resolution in 1,000 tolerance cases. Its classical null and designed BFG clock are observationally identical in the ideal common mode, so this pilot cannot independently confirm a BFG natural law.
- A prospective protocol records hardware-readiness gates, finite event resolution and the inability of the assumed millivolt detector to resolve the predicted nanovolt thermal scale.
- Proof-assistant verification and actual hardware work remain incomplete. No laboratory data are included.

## Files

| File | Purpose |
|---|---|
| [claims.json](claims.json), [claims.csv](claims.csv) | Indexed claims and review status |
| [PROOF_AUDIT.md](PROOF_AUDIT.md) | Central dependency audit and unresolved rank issues |
| [SCALAR_PROOF.md](SCALAR_PROOF.md) | Analytic scalar proof, assumptions and boundary controls |
| [scalar_controls.py](scalar_controls.py), [scalar_results.json](scalar_results.json) | Exact symbolic and rational checks |
| [baseline/](baseline/) | Preserved published implementation and fresh execution results |
| [rc_pilot.py](rc_pilot.py), [rc_pilot_results.json](rc_pilot_results.json) | Synthetic feasibility study |
| [synthetic_fixed_time_trace.csv](synthetic_fixed_time_trace.csv) | Explicitly synthetic acquisition trace |
| [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) | Prospective protocol and discrimination boundary |
| [FORMALIZATION_PLAN.md](FORMALIZATION_PLAN.md) | Formal proof acceptance criteria; not completed |
| [SOURCE.json](SOURCE.json), [reference_main.tex](reference_main.tex) | Frozen source reference and hashes |

## Reproduce

Use Python 3.12, NumPy 2.5.4, SymPy 1.14.0 and mpmath 1.3.0. Matplotlib 3.11.2 is also needed to import the preserved baseline script. Run from this folder:

```sh
python scalar_controls.py
python rc_pilot.py
python -c "import runpy; m=runpy.run_path('baseline/extended_controls.py'); m['run']()"
```

The last command intentionally replays checks without regenerating manuscript figures. Exact rational iteration can be slower than floating point because numerator and denominator sizes grow rapidly. Output paths are relative to each script, not the current working directory.

## Status and next steps

### Joint canonical data and exact coordinate-equivalence certificates

[The joint canonical-state analysis](joint_canonical_data/README.md) brings in all five stored finite roles and proves an exact simultaneous-unitary criterion via invertible intertwiners and their determinant polynomial. It distinguishes coordinate copies from equal-individual-spectrum states with different K/Y alignment. Mixed traces and exact successor spectra expose an operational difference, while a separate example has inequivalent stored inputs but the same reduced successor. The stored class is not silently equated with the source's full behavioral quotient or nine-role state. Exact algebraic certificates and preserved-helper controls passed; no origin values or physical laws are invented.

### Complete-future observable identifiability

[The future-identifiability analysis](future_identifiability/README.md) computes the exact coarsest predictive congruence for a supplied finite transition and observable family. Its minimal observable model is unique given the full behavior set, while balance/count histories alone permit different underlying models and hidden copies. The exact algorithm passes 3,984 symbolic models and 62,688 independent state-pair checks; these are not full BFG-admissibility or physical tests. The source's full canonical datum is explicitly not equated with the reduced observation packet. Count information is transported through the quotient instead of being reset to its new cardinality. No new origin rule is adopted.

### Constructive finite configuration-to-Hilbert bridge

[The configuration-Hilbert construction](configuration_hilbert_bridge/README.md) builds an explicit count-preserving representation and exact linear lift of a supplied finite invariant configuration transition. The worked five-label packet preserves information and recursion. Further exact checks distinguish classical multiplication from full-operator uniqueness, class quotient from dynamic congruence, and generic similarity from a positive Gram. A positive-kernel information-compatibility criterion is proved, and singleton zero-information factorization limits are identified. This completes a conditional representation builder, not a unique physical-origin initializer or a new law.

### Source origin information and profile-domain check

[The origin-information audit](origin_information_domain/README.md) directly verifies Level-0 Section 14's log similarity-class count and distinguishes it from the later quadratic information functional. A finite candidate bridge fails an exact quadratic identity; a positive control reconstructs log(2)I. An exact finite-count/open-connected bridge would be isotropic. The fresh minimum set supplies only one projector, while nearby profiles have a strictly positive, quantified quartic excess. Comparison data, a compatible representation and a broader admissible profile domain remain explicit source obligations. All new exact controls passed; no rule is installed.

### Local admissible information reconstruction

[The local-information analysis](local_information/README.md) proves an explicit n^2-profile reconstruction arbitrarily close to a formed direction in the finite complex Hermitian sector. Six exact n=2,3,4 cases pass. Real-only and restricted boundedness domains leave identifiable operator directions missing. An open neighborhood of exact balance forces E J=B_op N in the stated Hermitian sector, whereas a finite balance band leaves a family. Exact error-amplification bounds distinguish local uniqueness from numerical robustness. Functional values and full dynamic accessibility remain source obligations; no new physical rule is installed.

### BFG-Engine plugin synthesis and source quotient correction

[The plugin synthesis](plugin_synthesis/README.md) uses the requested installed BFG-Engine skill and all 20 indexed bundled references for global source/topic coverage, with focused mathematical inspection. It credits the field-derived scalar A/B closure and proves the finite information-functional span criterion for reconstructing the information operator. A full-core admissibility family still leaves transverse recursion unspecified. Direct visual checks of the foundational FW history formulas expose an exact quotient-distance mismatch; an erratum gives the 1/5 counterexample and two coherent metric continuations. All new exact controls passed. This is not a full proof audit of 1,728 indexed parts, and neither a new physical law nor a unique origin initializer is claimed.

### Consolidated origin-to-event dependency checkpoint

[The dependency closure audit](dependency_closure/README.md) unifies the earlier findings into a source-linked premise ledger and guarded inference graph: 38 nodes, 16 rules, 9 source records and 8 premise packets. It separates the complete finite event's sufficiency from a unique original initializer, preserves the conditional Gram derivation, and tests two guarded circular attempts and six unlicensed shortcuts. The complete supplied state closes; the smaller reviewed formation packet does not yet supply the interface, origin persistence and witness representation. This is dependency bookkeeping and a bounded source conclusion, not a full historical impossibility theorem or formal proof-assistant certification.

### Original raw-recursion definition located

[The raw-recursion source audit](raw_recursion/README.md) directly checks the May 14 original cognitive PDF, including visual verification of pages 3 and 5, plus the original core/consolidated sources. R is genuinely defined as the composition of primitive coupling and feedback maps; their origin values are not derived in that axiom. The existing neural interface equation conditionally reconstructs feedback when its other instantaneous data are supplied. Exact controls distinguish scalar feedback from an operator prescription, and original inverse-neutral normalization from later conjugate mediation. No new primitive, initializer or physical rule is adopted.

### Joint neutral-interface and recursive-origin constraints

[The joint initialization analysis](joint_initialization/README.md) proves an exact positive-sector kernel criterion linking a specified neutral recursion operator and raw recursion to the protected formed line. It keeps N_R distinct from C_N(Y) unless an additional identification is explicitly assumed. Under that comparison identification a common formed mode obeys y=r-1, with a conditional surviving interval 1<r<2; even fixed raw R need not determine transverse Y. Exact noncommuting and quadratic-interface compatibility controls passed. No new identification, raw-recursion prescription or origin rule is adopted.

### No-choice origin checkpoint

[The no-choice audit](origin_no_choice/README.md) checks the original recovery/no-tie-break clauses and distinguishes them from a smallest-rank axiom. Three parameter-free covariant support assignments preserve the same fresh formation on a scalar-neutral stratum while satisfying the enumerated scale, commutation and boundedness requirements. Exact arguments and unchanged-event controls yield distinct successor dimensions and spectra. No-choice forbids an unjustified preference; it does not supply a missing origin criterion or invalidate deterministic evolution from supplied initial data. The next distinct obligation is the initial neutral interface and its joint relation to origin recursion.

### Initial persistent-support classification

[The initial-persistence audit](initial_persistence/README.md) classifies every orthogonal support containing the fresh formed line as P=Pi+Q on an orthogonal complement. The least such support is Pi; the least Y-invariant containing support is instead the cyclic span of the formed vector under Y and can be larger. Neither origin criterion is silently adopted. Exact invariants and unchanged-event controls with the same K, formation, witness and Y show different seed stock and successor kernel traces for the two support choices. Preservation and bounded recursion do not determine the full origin support under that stated packet.

### Fresh-origin subset and later two-density separation

[The origin-subset analysis](origin_subset/README.md) proves that a root-only identification of witness and normalized fresh formation is consistent with the existing state category. Common nonzero transport preserves the equality without seeding; an orthogonal formation seed breaks it, with an exact separation formula. Two unchanged-event checks begin from the actual fresh quartic minimum: an isotropic coupling gives a one-dimensional unseeded output, while a noncommuting coupling gives a two-dimensional seeded output with distinct formation and witness. The subset is not forced by no ancestry alone, and no boundary rule is installed.

### Exact formed-profile / identity bridge criterion

[The profile-identity audit](profile_identity/README.md) constructs the unique formed-line projector and characterizes exactly when a positive trace-one inherited witness equals it: same support, zero transverse mass, minimum quadratic formation value, or finite order domination by the fresh formation density. A gap-controlled Frobenius error bound has a sharp exact fixture. The reviewed source passages do not establish the enforcing origin premise; general witness stationarity, commutation, overlap and covariance are insufficient. No new initializer or law is adopted.

### Original identity and persistence checked

[The origin representation audit](origin_bridge/README.md) traces eight original extractions, including March/April 2025 and the June origin chain. Primitive identity and persistence are already present; what remains unproved is their unique representation as the first finite witness and protected ground line. An analytic theorem derives the unique witness from a rank-one protected sector and unnormalized stationarity. Exact controls distinguish these premises from mere normalized stationarity, spectral criticality or the conjugate-product grammar. Existing declared successor rules remain credited; no new origin rule is adopted.

### Formation-derived initial data

[The formation initializer audit](formation_initialization/README.md) derives the unique phase-free fresh formation density from the existing simple-negative quartic minimum. It proves the witness formula conditional on support on that same line and exhibits why the general witness type and static formation do not alone determine identity or persistence. Existing successor promotion is credited without silently extending its domain to origin. Exact symbolic controls passed; the complete initializer, including Y, remains unresolved.

### Initial-data contract reconciled

[The original initial data versus the complete finite state](initial_state_audit/README.md) shows that Y0 is already an explicit state input in the September and November finite kernel. No extra L/M is needed once the complete typed five-tuple is supplied. The exact event's uniqueness and an initializer-fiber induction distinguish different initial states from different representations of the same state. Fresh checks passed. A separate numerical-policy witness shows that the preserved helper can label a strictly positive small load as a tolerance stop; it is not evidence of exact terminality. No model rule, baseline code or paper was changed.

### Coupling independence: all three requested steps

[Dependency sorting, uniform consequences and dependence witnesses](coupling_independence/README.md) now distinguish an unknown initial interface from a changed event law. The 48-statement register is classified by dependence without upgrading prior proof-review status. For the fixed finite event, completion/absorption, finite budgets and convergence of every infinite successful orbit do not require a uniquely derived initial coupling. A common absolute-event load envelope follows for fixed initial dimension. Exact and bounded implementation checks show that the selected outcome, final carrier dimension, seed count, formation stock and limiting K can nevertheless differ across initial interfaces. Four 90-digit load trajectories passed the recorded bounds. No physical rule or paper is changed.

### Follow-up: foundation-to-event derivation audit

[Open the derivation audit](foundation_audit/README.md) and its [status ledger](foundation_audit/DERIVATION_STATUS.md). Six historical text extractions, including the April 2025 sources, were traced separately from the November event definitions. An exact, parameter-free successor witness shows nonuniqueness relative to an explicitly listed structural packet: the same input yields loads 8/45 and 8/53. The stronger exact Gram identification excludes the witness, so the result does not refute the defined event. Source-local checks also expose the limits of a monotone-descent balance argument and the telescoping process-time definition. All controls passed. No new physical law, paper or experimental claim was introduced. Earlier September G/S/R findings are credited.

Reproduce this follow-up with `python foundation_audit/verify_foundations.py` (SymPy required). See its source manifest for extraction hashes and the explicit limit on any claim about all historical axioms.

**Existing derivation reconciled with the program:** the [19-step crosswalk](foundation_audit/DERIVATION_PROGRAM_CROSSWALK.md) confirms the prior BFG-internal conditional Gram derivation and its correct active-target coordinates. The 8/45-versus-8/53 witness fails the full same-completion premise and does not refute that derivation. Exact complex rectangular-channel, selector, weight, seed and capacity-transport checks passed. Run `python foundation_audit/verify_crosswalk.py`. Source versions are pinned, and remaining role/ordering obligations are separated from already derived algebra. No program rule or published PDF is changed.

**Next premise check completed:** the [interface classification](foundation_audit/INTERFACE_IDENTIFICATION.md) distinguishes true coordinate normalization from inequivalent quadratic completions of the same formed Hessian. Positive joint forms are uniquely parameterized by a coupling L and intrinsic neutral metric M; the source Hessian alone does not determine them. Exact fixtures and coordinate-invariance checks passed. Run `python foundation_audit/verify_interface.py`. The proposed L0-NC restriction remains explicitly proposed, with no new law adopted.

**Existing-premise search:** a [targeted review of ten original documents](foundation_audit/EXISTING_PREMISE_SEARCH.md), including recovered V3, distinguishes the existing rule for reciprocal weights from the upstream source-neutral coupling. No earlier complete interface-fixing implication was established in that bounded review; the concrete condition located is the explicitly proposed L0-NC restriction. Exact witnesses show why zero fitted coefficients, source-scale normalization and reciprocal balance alone do not close that gap. Run `python foundation_audit/verify_premise_candidates.py`. This preserves the already established conditional finite program.

This stage found no contradiction in the focused central finite-model proof chain. It does not certify all 48 statements, establish historical uniqueness of the model, or validate a universal physical law. Next: execute the scalar proof-assistant pilot; certify ambiguous rank decisions; complete adversarial reviews of the other claims; identify a physically discriminating prediction before presenting hardware as a natural-law test.

The original publication remains unchanged. This dated research stage is an internal AI-assisted analytic/computational review, not external peer review. No background scheduler was created. Repository-wide rights remain in force for new materials; the original publication retains its existing file-specific published terms.
