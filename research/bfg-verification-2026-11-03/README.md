# BFG verification and RC feasibility — 3 November 2026

Research stage for **The Balance Field Gleichung: Finite Dynamics and Physical Correspondence in RC Models**, DOI [10.5281/zenodo.23897937](https://doi.org/10.5281/zenodo.23897937). [Published paper](../../papers/finite-dynamics-rc-models-2026-11-02/README.md).

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
