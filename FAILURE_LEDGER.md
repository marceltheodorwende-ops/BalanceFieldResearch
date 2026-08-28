# BFG Failure Ledger

## Balance–Field Framework (BFG)

The BFG Failure Ledger records negative, null, contradictory, inconclusive, restricted, and falsifying outcomes within the **Balance–Field Framework (BFG)**.

Its purpose is not to collect mistakes for their own sake.

Its purpose is to preserve scientific constraints.

A failed BFG test must not disappear merely because a later interpretation is more attractive.

A negative result must not be reclassified as support after the result is known.

The governing rule is:

> **Failure is evidence about the boundary of a claim.**

---

# 1. Core Failure Principle

The Balance-Field Standard requires preservation of negative results.

The basic rule is:

**negative result → failure-ledger constraint**

and:

**failure ≠ reinterpretation as support**

A failed test may:

* weaken a claim,
* restrict its scope,
* reject a particular mechanism,
* invalidate an operationalization,
* force a new preregistration,
* expose a redescription-only result,
* or falsify the declared claim.

It must not be silently removed from the research record.

---

# 2. Relation to the Claim Register

Every failure record should refer to a corresponding claim in:

**`CLAIM_REGISTER.md`**

using its `claim_id`.

Example:

**claim_id: BFG-CR-004**

may refer to the neutral-mediation claim.

A failure record does not automatically falsify the entire Balance–Field Framework.

Failure should be localized to the smallest claim that actually failed.

For example:

**mediator ablation fails**

does not automatically mean:

**all BFG mathematics is false**

Instead, it means that the specific mediator claim for the tested carrier has failed or been weakened.

---

# 3. Failure Localization Principle

BFG failures are role-specific.

A failed gate should identify which layer has failed.

Possible failure locations include:

| Gate                 | Failure consequence                                         |
| -------------------- | ----------------------------------------------------------- |
| Profile Gate         | difference profile is circular or endpoint-dependent        |
| Polarity Gate        | P1 and P2 are redundant or ornamental                       |
| Mediator Gate        | N is not load-bearing                                       |
| Configuration Gate   | proposed closure configuration adds no measurable structure |
| Export Gate          | Eout is unnecessary for the tested mechanism                |
| Recursive Gate       | recursive closure adds no measurable value                  |
| Spectral Gate        | recursive dynamics are unstable or null-equivalent          |
| Differentiation Gate | bounded dynamics collapse differentiation                   |
| Transport Gate       | relevant distinctions are not preserved                     |
| Redescription Gate   | BFG adds vocabulary but no new constraint                   |
| Null-Model Gate      | matched alternative performs equally well or better         |
| No-Retuning Gate     | result requires post-hoc rule adjustment                    |
| Scaling Gate         | effect does not survive declared scale changes              |
| Replication Gate     | effect does not reproduce                                   |
| Audit Gate           | negative or residual outcomes were not preserved            |

Failure should weaken the corresponding layer rather than being converted into an unrestricted statement about the whole framework.

---

# 4. Failure Decision States

Each failure record should receive a decision state.

| Decision State                | Meaning                                                        |
| ----------------------------- | -------------------------------------------------------------- |
| **Negative**                  | declared diagnostic failed                                     |
| **Null-Equivalent**           | BFG performed no better than the matched null                  |
| **Restricted**                | claim survives only in a narrower domain or condition          |
| **Underdetermined**           | evidence is insufficient to distinguish competing explanations |
| **Operationalization Failed** | measurement or estimator does not validly test the claim       |
| **Ablation Failed**           | proposed BFG role is not load-bearing                          |
| **Retuning Violation**        | rules changed after outcome inspection                         |
| **Redescription-Only**        | no BFG-specific added value demonstrated                       |
| **Replication Failed**        | declared result did not reproduce                              |
| **Rejected**                  | claim failed its declared decision gate                        |
| **Falsified**                 | explicit preregistered falsification condition was met         |

---

# 5. Mandatory Failure Record

Every substantive failure entry should contain the following fields.

## BFG Failure Ledger Record

**failure_id:**
Unique identifier for the failure.

**claim_id:**
Corresponding claim from `CLAIM_REGISTER.md`.

**date:**
Date on which the result was classified.

**domain:**
Domain, carrier, dataset, simulation, or formal test in which the failure occurred.

**claim_state_before_test:**
Claim status before the result was known.

**failed_gate:**
The exact BFG gate that failed.

**result_summary:**
Short factual description of the observed result.

**primary_endpoint:**
Declared primary endpoint, where applicable.

**success_criterion:**
Criterion that would have counted as success.

**failure_criterion:**
Criterion that was declared as failure.

**null_model_result:**
Performance or result of the matched null model.

**ablation_result:**
Result of mediator, export, recursion, polarity, transport, or other declared ablation.

**retuning_status:**
Whether operators, thresholds, readouts, datasets, or decision criteria remained frozen.

**allowed_interpretation:**
What the result is allowed to support.

**forbidden_interpretation:**
What must not be inferred from the result.

**recovery_action:**
Permitted scientific response.

**transport_decision:**
Decision about whether the claim may remain in the core, be restricted, revised, preregistered again, quarantined, or rejected.

**notes:**
Additional audit information.

---

# 6. Standard Failure Record Template

Copy this block for every new failure:

---

## Failure Record: BFG-F-XXXX

**failure_id:** BFG-F-XXXX

**claim_id:** BFG-CR-XXX

**date:** YYYY-MM-DD

**domain:**
To be declared.

**claim_state_before_test:**
To be declared.

**failed_gate:**
To be declared.

### Result Summary

To be completed with the observed result only.

Do not reinterpret the result inside this field.

### Primary Endpoint

To be declared before confirmatory testing.

### Success Criterion

To be declared before confirmatory testing.

### Failure Criterion

To be declared before confirmatory testing.

### Null-Model Result

To be completed.

### Ablation Result

To be completed.

### Retuning Status

Choose one:

* Frozen / no retuning
* Exploratory
* Retuning violation
* Not applicable

### Allowed Interpretation

State the narrowest scientifically justified interpretation.

### Forbidden Interpretation

State explicitly what the result does not establish.

### Recovery Action

Choose or describe:

* no action required,
* restrict claim,
* revise operationalization,
* preregister new test,
* reject mechanism,
* reject claim,
* retain as unresolved,
* independent replication required.

### Transport Decision

Choose one:

* Accept
* Restricted
* Open
* Revise
* Preregister
* Quarantine
* Reject
* Falsified

### Notes

Additional provenance, code version, data reference, commit, or audit note.

---

# 7. No Post-Hoc Rescue Rule

A failed test must not be rescued by changing its meaning after the result is known.

The following sequence is not admissible:

**prediction fails**

→ **definition changes**

→ **threshold changes**

→ **different endpoint is selected**

→ **result is reported as support**

If the original test fails and a modified hypothesis becomes scientifically interesting, the new hypothesis must be treated as a **new exploratory claim**.

It requires a new claim record and, for confirmatory use, a new preregistration.

The failed original claim remains in this ledger.

---

# 8. No-Retuning Failure

A no-retuning failure occurs when the declared test grammar changes after the target evidence has been inspected.

Relevant components include:

* preprocessing,
* operational definitions,
* windows,
* operators,
* thresholds,
* null models,
* ablations,
* exclusion rules,
* datasets,
* readouts,
* success criteria.

A confirmatory claim that violates the freeze becomes:

**exploratory only**

unless independently tested again under newly frozen rules.

The original retuning violation must remain documented.

---

# 9. Mediator Failure

A mediator failure occurs when the proposed neutral mediator `N` is not demonstrably load-bearing.

Relevant tests include:

**N → 0**

mediator shuffling,

mediator replacement,

or comparison with a matched direct model:

**P1 — P2**

versus:

**P1 — N — P2**

If mediator removal or replacement produces no relevant loss, the correct interpretation is:

**the proposed N-mediated mechanism is weakened for this carrier**

not:

**the mediator worked in a different invisible way**

unless a new independent hypothesis is preregistered and tested.

---

# 10. Export Failure

A regulated-export claim should predict a consequence when the relevant export channel is blocked.

The primary ablation is:

**Eout → 0**

A failure occurs when removal of the proposed export channel produces none of the declared consequences in:

* burden,
* instability,
* drift,
* overload,
* fragmentation,
* transition,
* or persistence.

The correct response is to weaken or reject the tested export mechanism.

A generic system output should not be relabeled as BFG export after the original export hypothesis fails.

---

# 11. Recursive Closure Failure

A recursive-closure claim may fail when:

* RC does not remain bounded,
* the declared spectral condition is violated,
* recursive performance is null-equivalent,
* raw recursion performs equally well,
* a simpler controller reproduces the effect,
* or the proposed recursion destroys relevant differentiation.

A bounded result is not automatically successful.

The following combination must be avoided:

**bounded dynamics + collapsed differentiation = successful closure**

If the system is bounded but differentiation collapses, the non-collapse gate has failed.

---

# 12. Differentiation Failure

A non-collapse failure occurs when the declared differentiation condition is not satisfied.

For the participation-ratio realization:

**Dd ≤ Dmin**

constitutes failure of the declared differentiation gate.

This may occur even if:

**sup ‖RCⁿs‖ < ∞**

is satisfied.

Therefore:

**boundedness ≠ non-collapse**

---

# 13. Redescription Failure

A BFG reconstruction fails the added-value test when it merely renames an already-existing mechanism.

Examples include:

**existing interaction → mediation**

**existing stability → closure**

**existing output → export**

**existing attractor → BFG attractor**

If the BFG mapping adds no measurable constraint, prediction, failure condition, ablation sensitivity, or transferable structure, classify the result as:

**Redescription-Only**

This is not a hidden success state.

It is a scientific constraint on the BFG-specific claim.

---

# 14. Null-Model Failure

A BFG-specific claim is weakened when an appropriately matched alternative performs equally well or better.

Examples may include:

* direct dyadic models,
* aggregate models,
* shuffled controls,
* randomized relation models,
* capacity-matched controllers,
* domain-specific baseline models,
* simpler stability models.

A null-model failure must not be dismissed merely because the alternative lacks BFG terminology.

Functional equivalence counts.

---

# 15. Cross-Domain Transfer Failure

A cross-domain claim fails its stronger transfer condition when frozen BFG rules do not transport successfully.

Failure includes:

* changing Φ estimators after viewing the new domain,
* changing thresholds,
* changing RC definitions,
* changing failure criteria,
* selecting a different endpoint after inspection,
* excluding inconvenient carriers without a predeclared rule.

A failed frozen transfer may still motivate new research.

It does not count as successful no-retuning transfer.

---

# 16. Replication Failure

A strong empirical BFG claim should survive independent repetition appropriate to the strength of the original claim.

If a declared result does not reproduce, the failure must be recorded.

Possible decision states include:

* Restricted
* Underdetermined
* Replication Failed
* Rejected

The original positive result should not be silently deleted.

Both the original result and the replication failure belong to the scientific record.

---

# 17. Preregistration Boundary

Exploratory research remains valuable.

However:

**no preregistration → exploratory only**

for claims that require confirmatory status.

Before confirmatory evidence is used, the test should declare:

* hypothesis,
* domain,
* primary endpoint,
* secondary endpoints,
* operational readouts,
* dimensions,
* null model,
* ablation plan,
* no-retuning freeze,
* success criterion,
* failure criterion,
* allowed interpretation,
* forbidden interpretation,
* transport decision after result.

A negative result under a frozen preregistration becomes a meaningful failure-ledger constraint.

---

# 18. Allowed Recovery Actions

Failure does not prohibit further research.

It constrains how further research may proceed.

Admissible recovery actions include:

### Restrict the claim

Reduce the scope to the domain or condition that remains supported.

### Revise the operationalization

Only when the original result remains recorded as failed or inconclusive.

The revised operationalization becomes a new test.

### Introduce a new hypothesis

A new hypothesis receives a new claim record.

It does not replace the historical failed claim.

### Preregister a new experiment

A scientifically motivated modification may be tested again under frozen conditions.

### Reject the mechanism

If the proposed causal role is not supported, remove it from the corresponding claim.

### Reject the claim

If the declared falsification condition has been met, mark the claim accordingly.

---

# 19. Forbidden Recovery Actions

The following are not admissible responses to a failed confirmatory test:

* deleting the negative result,
* changing the endpoint after inspection and calling it the original prediction,
* changing thresholds without disclosure,
* replacing the null model after it performs too well,
* introducing a new mediator after mediator ablation fails and treating it as the same test,
* redefining Φ to restore the desired classification,
* calling a null-equivalent result confirmation,
* describing failed transfer as universal support,
* converting simulation success into empirical validation,
* using ontology to rescue an operational failure.

---

# 20. Failure and the BFG Core

The purpose of this ledger is not to make every failure global.

BFG uses **localized downgrade logic**.

Example:

**N fails in carrier d1**

means:

**the declared N mechanism is unsupported in carrier d1**

unless the original claim explicitly stated a universal condition whose falsification criterion has been met.

Likewise:

**2:3 loses to a matched ratio alternative**

should weaken or reject the corresponding 2:3 selection claim.

It does not automatically invalidate unrelated definitions of recursive closure or the order parameter Φ.

---

# 21. Failure Severity

Failure records may be classified by severity.

## Level F1 — Operational Warning

A measurement or implementation issue prevents a clean conclusion.

## Level F2 — Underdetermined

The result cannot distinguish BFG from the relevant alternative.

## Level F3 — Mechanism Failure

A declared load-bearing BFG role fails its ablation.

## Level F4 — Claim Rejection

The declared claim fails its decision criterion.

## Level F5 — Strong Falsification

A preregistered falsification condition for the stated scope is directly satisfied.

Severity refers to the affected claim scope.

It does not automatically propagate to the entire framework.

---

# 22. Current Ledger Status

At repository initialization, no failure should be invented merely to populate the ledger.

Historical negative results from existing BFG work may be imported only when their source, claim, result, and interpretation boundary are documented.

Current repository-level status:

**No new repository-specific failure records entered yet.**

This statement does not mean that the BFG corpus contains no negative or null results.

It means only that historical results have not yet been formally migrated into this repository ledger.

---

# 23. Failure Record Index

| Failure ID | Claim ID | Domain | Failed Gate | Decision                          | Date |
| ---------- | -------- | ------ | ----------- | --------------------------------- | ---- |
| —          | —        | —      | —           | No repository-specific record yet | —    |

This table should be updated whenever a formal failure record is added.

---

# 24. Minimum Scientific Rule

Every confirmatory BFG test should answer two questions before execution:

> **What result would count as support?**

and:

> **What result would make us weaken or reject the claim?**

If the second question has no answer, the test is not yet falsification-ready.

---

# 25. Guiding Principle

> **A negative result is not damage to the research record. Hiding or reinterpreting it is.**

The BFG Failure Ledger exists to ensure that unsuccessful predictions, null equivalence, failed mechanisms, retuning violations, and replication failures remain active constraints on future BFG development.

The objective is not to protect the framework from failure.

The objective is to make failure scientifically informative.
