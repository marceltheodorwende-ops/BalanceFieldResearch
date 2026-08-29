# BFG-TEST-001 — Preregistration

## Trinity–Order Positive/Negative Carrier Challenge

**Test ID:** BFG-TEST-001

**Primary Claim ID:** BFG-CR-026 — Trinity–Order Compatibility Bridge

**Linked Claims:**

- BFG-CR-004 — Neutral Mediation
- BFG-CR-008 — Recursive Boundedness
- BFG-CR-010 — BFG Order Parameter Φ
- BFG-CR-011 — Domain Order Parameter
- BFG-CR-015 — Differentiation / Non-Collapse
- BFG-CR-017 — Cross-Domain Invariant Candidate
- BFG-CR-019 — Distinguishability-Preserving Transport
- BFG-CR-020 — No-Retuning Transfer

**Preregistration Status:** DRAFT — NOT FROZEN

**Confirmatory Status:** NOT YET ACTIVE

**Carrier Status:** SELECTED — NOT YET OPERATIONALLY FROZEN

**Order Parameter Status:** UNOPERATIONALIZED

**Primary Endpoint Status:** NOT YET FROZEN

**Null Models Status:** NOT YET FROZEN

**Ablation Status:** NOT YET FROZEN

**No-Retuning Status:** NOT YET FROZEN

---

## Scientific Boundary

No confirmatory test execution may begin while this preregistration remains marked:

**DRAFT — NOT FROZEN**

Any analysis performed before completion and freeze of the preregistration must be classified as exploratory.

Positive, negative, null-equivalent, restricted, and inconclusive outcomes are all admissible outcomes of BFG-TEST-001.

The protocol must not be modified after target-result inspection in order to recover a preferred outcome.

---

## Carrier Selection & Independence Boundary

### Primary External Carrier

The primary measured-data carrier for BFG-TEST-001 is:

**Aventa AV-7 ETH Zurich Research Wind Turbine SCADA and high frequency Structural Health Monitoring (SHM) data**

Dataset version:

**Zenodo v6**

DOI:

**10.5281/zenodo.8229750**

Dataset creators:

- Eleni Chatzi
- Imad Abdallah
- Martin Hofsäß
- Oliver Bischoff
- Sarah Barber
- Yuriy Marykovskiy

The dataset was produced independently of the Balance–Field Framework.

Its operating-condition labels were defined externally and were not constructed from BFG variables, BFG scores, the Order Parameter Φ, or the outcome of BFG-TEST-001.

---

### Externally Defined Carrier Conditions

The primary dataset contains four externally documented operating conditions:

1. **Normal operation for system identification**
2. **Aerodynamic imbalance on one blade**
3. **Rotor icing event**
4. **Failure of the flexible coupling of the linear drive of the collective pitch system**

These labels are treated as external carrier metadata.

They must not be redefined after BFG results are observed.

---

### Positive-Candidate Arm

The externally documented:

**Normal operation for system identification**

condition is designated as the:

**Positive-Candidate Arm**

for BFG-TEST-001.

This designation does not mean that the arm is assumed to produce a positive BFG result.

A candidate-positive BFG result will be declared only if the frozen Trinity–Order protocol later satisfies its preregistered positive criteria.

If the Normal Operation arm fails those criteria, the failure must be retained.

---

### Challenge Arms

The following externally defined conditions are designated as independent challenge arms:

**Challenge Arm 1 — Collective Pitch-System Mechanical Failure**

Failure of the flexible coupling of the linear drive of the collective pitch system.

**Challenge Arm 2 — Aerodynamic Imbalance**

Aerodynamic imbalance on one blade.

**Challenge Arm 3 — Rotor Icing**

Rotor icing event.

These challenge arms are not assumed to produce the same BFG failure signature.

Mechanistic BFG predictions for each arm must be declared before target evaluation.

---

### Candidate Mediator-Perturbation Boundary

The collective pitch-system mechanical failure is reserved as a:

**Candidate Natural Mediator-Perturbation Condition**

because it affects a documented control subsystem of the turbine.

This designation does not yet identify:

**N = pitch system**

and does not yet establish the collective pitch mechanism as the BFG neutral mediator.

The operational definition of N must be frozen separately.

The mediator hypothesis remains open until:

- P1 and P2 are operationally defined,
- N is operationally defined,
- a matched dyadic or non-mediated alternative is declared,
- mediator-related readouts are frozen,
- and the preregistered mediator-loss criterion is evaluated.

---

### Independence Boundary

The carrier is admissible for the first external BFG challenge because:

- the data were not generated for BFG,
- the operating-condition labels predate BFG-TEST-001,
- the fault classes were not selected from BFG output,
- the Positive-Candidate Arm was not created by BFG optimization,
- and the carrier contains both normal and independently documented disturbed states.

BFG-TEST-001 must not redefine the external carrier labels after outcome inspection.

---

### Carrier Interpretation Boundary

The carrier selection alone does not establish:

- that the turbine implements a BFG trinity,
- that the collective pitch system is N,
- that Normal Operation satisfies Φ ≈ 1,
- that any fault state is a BFG failure state,
- that Φ is already operationalized,
- or that the Trinity–Order Compatibility Bridge has empirical support.

Those statements remain untested.

---

### Data-Use Boundary

No target-result inspection is permitted to determine:

- P1,
- P2,
- N,
- Eexp,
- Ebind,
- I,
- I0,
- ΩΦ,
- the Φ regime or corridor,
- εcomm,
- the primary endpoint,
- null-model thresholds,
- or success/failure thresholds.

Those quantities must be defined and frozen in later preregistration stages.

Metadata inspection for the purpose of understanding signal names, dimensions, sensor locations, sampling rates, and documented turbine operation is permitted.

Exploratory outcome-driven signal selection is not confirmatory.

---

### Current Carrier Decision

**Carrier selected.**

**Operational mapping not yet frozen.**

**No BFG result has yet been evaluated.**

**No positive or negative result has yet been registered.**

---

## Signal Inventory & Blind Feature Eligibility

### Purpose

This stage defines the admissible measured signal families for BFG-TEST-001 before any BFG role mapping, Order Parameter construction, endpoint optimization, or target-result inspection.

The purpose is to prevent outcome-driven variable selection.

No signal listed in this section is yet assigned to:

- P1,
- P2,
- N,
- K,
- C,
- A,
- Eout,
- Eexp,
- Ebind,
- I,
- I0,
- ΩΦ,
- RC,
- Ad,
- Dd,
- or εcomm.

Those mappings remain open.

---

### Metadata-Only Inspection Boundary

At this preregistration stage, the following forms of inspection are permitted:

- sensor names,
- sensor type,
- physical units,
- sensor location,
- sampling frequency,
- turbine architecture,
- documented control architecture,
- archive structure,
- file names,
- metadata schemas,
- documented operating-condition labels,
- and documented sensor orientation.

The following are not permitted for confirmatory variable selection at this stage:

- comparing Normal Operation with challenge-arm distributions,
- viewing fault-versus-normal feature plots,
- selecting sensors because they separate the labels,
- computing predictive accuracy against the carrier labels,
- using feature importance based on the target labels,
- choosing time windows because they maximize condition separation,
- choosing BFG roles because they produce a preferred Φ regime,
- or changing signal eligibility after target-result inspection.

If outcome-driven inspection occurs before freeze, it must be recorded as a protocol deviation and the affected analysis must be classified as exploratory.

---

### Dataset-Declared Measurement Architecture

The primary Aventa AV-7 carrier contains the following externally documented measurement families.

#### 1. Structural Acceleration Signals

The turbine is instrumented with:

**11 accelerometers**

distributed across:

- the tower,
- the nacelle main frame,
- the main bearing,
- and the generator.

Declared sampling frequency:

**200 Hz**

These measurements are structurally admissible candidate inputs for later recursive, dynamic, persistence, differentiation, and mediation analyses.

No BFG role is assigned to them yet.

---

#### 2. Tower Strain Signals

The dataset contains:

**2 full-bridge strain gauges**

installed at the concrete tower base.

The documented orientations are:

- fore-aft strain,
- side-side strain.

The strain measurements may be converted to bending moments according to the carrier metadata and domain mechanics.

Declared sampling frequency:

**200 Hz**

No BFG role is assigned to these channels yet.

---

#### 3. Environmental Signals

The dataset includes measurements of:

- temperature,
- humidity

at the tower base.

Declared sampling frequency:

**1 Hz**

These channels are eligible as environmental or contextual variables.

They must not automatically be treated as BFG order variables.

---

#### 4. SCADA Operational Signals

The externally documented SCADA measurement family contains:

- wind speed,
- nacelle yaw orientation,
- rotor RPM,
- power output,
- turbine status.

Declared sampling frequency:

**10 Hz**

These measurements are eligible as operational carrier variables.

No BFG role is assigned to them yet.

---

### Pitch-System Measurement Boundary

The Aventa AV-7 is externally documented as using:

**variable-speed and collective variable-pitch control.**

However, the Zenodo v6 dataset description used for BFG-TEST-001 does not itself list a direct pitch-angle measurement channel among the declared SCADA signals.

Therefore:

**a direct pitch-angle signal must not be assumed to exist unless it is confirmed in the dataset metadata files.**

The collective pitch-system failure condition remains an externally documented disturbance class.

It does not by itself provide a measured N variable.

The later mediator operationalization must therefore distinguish between:

- a directly measured mediator candidate,
- a mechanically inferred mediator candidate,
- and a latent functional mediator construction.

These alternatives must not be interchanged after target-result inspection.

---

### Dataset File Manifest

The selected Zenodo v6 record contains four primary carrier archives.

#### Normal Operation

File:

`aventa_normal_operation_for_system_identification.zip`

Approximate size:

**6.8 GB**

MD5:

`407114000b3c39a92e3a0cd8d73cc5af`

---

#### Collective Pitch-System Failure

File:

`aventa_failure_flexible_coupling_of_collective_pitch_drive.zip`

Approximate size:

**17.6 GB**

MD5:

`87a74879cbefabbc649ebca0c4003113`

---

#### Aerodynamic Imbalance

File:

`aventa_blade_aerodynamic_imbalance.zip`

Approximate size:

**17.1 GB**

MD5:

`1a1fa895fbf3536a0dad4ff1e818390c`

---

#### Rotor Icing

File:

`aventa_rotor_icing.zip`

Approximate size:

**7.7 GB**

MD5:

`87e8a2654cf524b72f5859f5c6c53089`

---

### Metadata Files Expected Inside the Carrier Archives

According to the external carrier record, each use-case archive contains metadata including:

- `Aventa-AV-7.json`
- `Aventa-AV-7.yaml`
- `Aventa_sensors.json`
- `Aventa_Sensors_Specs.xlsx`
- `IEAontology_schema.yaml`
- `sensors_schema.json`

and time-series measurements in:

**HDF5 format**

The metadata files may be inspected before signal-role mapping.

The target time-series outcomes must not be used to optimize the role mapping.

---

### Blind Signal Eligibility Rule

A signal or signal family is eligible for later confirmatory BFG operationalization only if its eligibility can be justified from:

1. external carrier metadata,
2. physical turbine architecture,
3. documented control or structural function,
4. dimensional compatibility,
5. or a preregistered mathematical transformation.

Eligibility must not be justified by the fact that the signal happens to distinguish Normal Operation from a challenge condition.

---

### Role-Mapping Firewall

The following rule is mandatory:

**Sensor availability does not imply BFG role identity.**

In particular:

- wind speed is not automatically Eexp,
- power output is not automatically Ebind,
- rotor RPM is not automatically I,
- turbine status is not automatically I0,
- the pitch-control subsystem is not automatically N,
- structural acceleration is not automatically C,
- and strain is not automatically Dd.

Every later mapping requires a separate functional and dimensional justification.

---

### Order Parameter Firewall

The BFG Order Parameter remains:

Φ = (Eexp · I) ÷ (Ebind · I0)

At this stage:

**Eexp = NOT YET FROZEN**

**Ebind = NOT YET FROZEN**

**I = NOT YET FROZEN**

**I0 = NOT YET FROZEN**

Therefore:

**Φ = NOT YET OPERATIONALIZED FOR THIS CARRIER**

No observed value of Φ may yet be interpreted as:

- binding-dominated,
- balanced,
- expansion-dominated,
- healthy,
- faulty,
- or Trinity–Order admissible.

---

### Sampling-Rate Boundary

The carrier contains measurements at multiple sampling frequencies:

- structural acceleration and strain: 200 Hz,
- SCADA operational measurements: 10 Hz,
- temperature and humidity: 1 Hz.

A common temporal representation will therefore be required for joint BFG analysis.

The following are not yet frozen:

- analysis-window duration,
- overlap,
- resampling rule,
- downsampling rule,
- anti-alias filtering,
- aggregation statistic,
- temporal alignment tolerance,
- missing-data treatment,
- and synchronization policy.

These decisions must be made before confirmatory target evaluation.

---

### Feature-Construction Boundary

No derived feature family is yet frozen.

Possible future feature classes may include physically justified:

- temporal statistics,
- spectral quantities,
- cross-channel relations,
- recurrence quantities,
- phase relations,
- structural-response measures,
- or information-retention measures.

Their use is not authorized by this section.

Each feature class must be declared before confirmatory evaluation.

---

### Current Signal-Inventory Decision

**External sensor architecture identified.**

**Eligible raw signal families identified from metadata.**

**No BFG role mapping completed.**

**No Order Parameter operationalization completed.**

**No target-driven feature selection permitted.**

**No positive or negative BFG result has been evaluated.**

**Version:** 0.3-draft

**Date:** 2026-08-29

**Copyright © 2026 Marcel Theodor Wende**
