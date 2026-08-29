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

---

## Supplementary SCADA Measurement Layer

### Purpose

A supplementary public SCADA dataset from the Aventa AV-7 research turbine family is registered before BFG role mapping in order to improve direct observability of the turbine control state.

This supplementary source is not introduced after target-result inspection.

It is registered during the preregistration stage.

---

### Supplementary Dataset

Dataset:

**Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA**

Zenodo version:

**v2**

DOI:

**10.5281/zenodo.15700928**

Coverage:

**2022-01-01 to 2023-07-20**

Sampling frequency:

**1 Hz**

Primary public file:

`Aventa_AV7_IET_OST_SCADA.csv`

MD5:

`0434ccfb5a05f91225796063942538f5`

---

### Carrier-Identity Boundary

The supplementary dataset documents an Aventa AV-7 research turbine at the Taggenberg site.

It is treated as a supplementary measurement layer for the same Aventa carrier family.

Exact record-level identity and timestamp alignment with the primary ETH Zurich SHM / SCADA fault archives must be verified before the two data sources are merged.

No cross-dataset merge is authorized until:

- timestamp compatibility is checked,
- turbine identity compatibility is checked,
- signal meaning is checked,
- unit compatibility is checked,
- and overlapping periods are documented.

---

### Supplementary SCADA Channels

The externally documented 1 Hz SCADA channels include:

- RotorSpeed
- GeneratorSpeed
- GeneratorTemperature
- WindSpeed
- PowerOutput
- offsetWindDirection
- SpeiseSpannung
- PitchDeg
- StatusAnlage
- MaxWindHeute
- Datetime

No BFG role is assigned by the presence of a channel alone.

---

### Direct Pitch-Angle Measurement

The supplementary metadata defines:

`PitchDeg`

as:

**Pitch angle in degrees**

with IEC-oriented channel name:

`WROT.BlPthAngVal`

The metadata describes the signal as derived from a:

**Balluff linear magnetostrictive sensor postprocessed to degrees**

and marks it as a reliable measurement.

This makes PitchDeg eligible as a directly measured control-state candidate.

It does not yet establish:

**N = PitchDeg**

or:

**N = pitch system**

The mediator role remains unfrozen.

---

### Rotor-Speed Measurement

The supplementary metadata defines:

`RotorSpeed`

as rotor speed in RPM.

The channel is marked as a reliable measurement.

RotorSpeed is eligible as a measured dynamical carrier variable.

No BFG role is assigned yet.

---

### Generator-Speed Measurement Boundary

The supplementary metadata defines:

`GeneratorSpeed`

as generator speed in RPM.

However, the metadata marks this channel as:

**Reliable Measurement = FALSE**

and notes that the signal is derived from a 0–10 V generator signal rather than an exact measurement.

Therefore GeneratorSpeed may not be used as a primary confirmatory BFG variable unless its uncertainty or measurement limitation is explicitly handled in the preregistration.

---

### Power-Output Measurement Boundary

The supplementary metadata defines:

`PowerOutput`

as converter active power in kW.

The channel is marked as reliable in the metadata, while the notes state that the inverter 0–10 V measurement is not completely accurate.

PowerOutput remains eligible, but its measurement limitation must be carried into any later uncertainty model.

---

### Wind and Orientation Measurements

The supplementary metadata defines:

`WindSpeed`

as wind speed in m/s

and:

`offsetWindDirection`

as wind direction relative to the nacelle in degrees.

These measurements are eligible as external forcing / alignment candidates.

They are not automatically:

- P1,
- Eexp,
- N,
- or any other BFG role.

---

### Supplementary-Data Firewall

The supplementary dataset may currently be inspected only for:

- metadata,
- channel names,
- physical units,
- sampling frequency,
- sensor description,
- measurement reliability,
- date coverage,
- turbine architecture,
- and timestamp format.

The following remain prohibited until the later freeze:

- comparing PitchDeg between fault and normal periods,
- selecting PitchDeg because it separates labels,
- choosing thresholds from fault data,
- selecting time windows from visible anomaly peaks,
- defining N from target-dependent behavior,
- defining Φ from outcome separation,
- or optimizing any BFG role mapping using fault labels.

---

### Mediator-Observability Status

The mediator is now classified as:

**DIRECTLY OBSERVABLE CANDIDATE AVAILABLE — ROLE NOT YET FROZEN**

This status means that the carrier contains a direct physical control-state measurement that may later be evaluated as part of N.

It does not mean that the BFG mediator hypothesis has been confirmed.

---

### Current Supplementary-Layer Decision

**Supplementary SCADA source registered.**

**Direct pitch-angle measurement identified.**

**No cross-dataset merge performed.**

**No BFG role mapping completed.**

**No target-result inspection authorized.**

**No positive or negative BFG result evaluated.**

---

## Candidate Role Mapping v0.1 — Functional Freeze

### Purpose

This section freezes the primary functional BFG role mapping for the Aventa AV-7 carrier before target-result inspection.

The mapping is based on:

- externally documented turbine architecture,
- physical signal function,
- sensor metadata,
- dimensional role,
- and the declared BFG grammar.

It is not based on:

- fault-versus-normal separation,
- classification accuracy,
- anomaly magnitude,
- feature importance,
- observed Φ values,
- or preferred BFG outcomes.

---

### Functional Carrier Path

The primary physical carrier path is defined as:

**External aerodynamic forcing
→ collective pitch-mediated aerodynamic coupling
→ rotor/drivetrain dynamical response
→ electrical power export**

This physical sequence is used only to define candidate BFG roles.

It is not itself evidence that BFG is correct.

---

## Primary BFG Role Mapping

### P1 — External Aerodynamic Forcing State

**Functional definition**

P1 represents the externally imposed aerodynamic forcing acting on the turbine.

Primary raw measurement family:

**WindSpeed**

Secondary contextual measurement:

**offsetWindDirection / nacelle-relative wind orientation**

where available and temporally compatible.

Primary P1 identity:

**external wind forcing**

P1 is not defined by fault labels.

P1 is not selected according to classification performance.

---

### P2 — Rotor / Drivetrain Dynamical Response State

**Functional definition**

P2 represents the internal rotor/drivetrain response generated under aerodynamic forcing and turbine regulation.

Primary raw measurement:

**RotorSpeed**

Primary P2 identity:

**rotational response of the turbine rotor/drivetrain**

RotorSpeed is selected from the physical carrier architecture before target inspection.

PowerOutput is not used as the primary P2 variable.

GeneratorSpeed is not used as the primary P2 variable.

---

### P1–P2 Complementarity Boundary

The functional polarity is therefore:

**P1 = external aerodynamic forcing**

versus

**P2 = internal rotational response**

The polarity is not interpreted as antagonism in a semantic sense.

It is a physically distinguishable input–response relation whose admissibility may be mediated by the turbine control architecture.

The BFG claim requires that the relation remain non-collapsed and non-fragmented under the declared operational definitions.

---

### N — Collective Pitch Mediation State

The primary mediator candidate is:

**collective pitch regulation**

Direct measured control-state candidate:

**PitchDeg**

However:

**N is not defined as identical to PitchDeg.**

PitchDeg is a directly measured physical component of the candidate mediator state.

The BFG mediator role refers to the functional regulation of the relation between external aerodynamic forcing and rotor/drivetrain response.

The later operational N estimator must therefore test whether pitch-mediated information adds functional explanatory or stabilizing value beyond direct P1–P2 coupling.

---

### Mediator Functional Requirement

The primary mediator hypothesis is:

**Collective pitch regulation contributes load-bearing information or regulation to the relation between P1 and P2.**

This hypothesis receives support only if the frozen full model outperforms:

- a direct P1–P2 model,
- a no-N model,
- an N-shuffled model,
- and a matched N-replacement model

according to the later preregistered primary endpoint.

The presence of PitchDeg alone is not evidence for mediation.

---

### Direct-Mediator Alignment Failure Rule

Use of PitchDeg as the primary direct mediator measurement requires verified temporal and carrier compatibility between the supplementary SCADA source and the primary fault dataset.

If that compatibility cannot be established:

**the direct-N confirmatory component of BFG-TEST-001 is classified as Operationalization Failed / Suspended.**

A different N variable must not be substituted after outcome inspection.

A latent or reconstructed mediator would require a separately declared preregistration or explicitly exploratory analysis.

---

### K — Stable Operating Configuration

K represents the joint carrier configuration formed by the declared roles.

At the functional level:

**K = configuration(P1, N, P2, Eout)**

The numerical state representation of K is not yet frozen.

No outcome-derived weights or features are authorized at this stage.

---

### C — Recursive Closure

C represents temporal recursive persistence of K.

The primary functional requirement is:

**the operating configuration must exhibit measurable return, retention, or bounded recursive continuation across time.**

The specific RC estimator is not yet frozen.

Recursive closure must later be compared with:

- no-memory,
- feed-forward,
- autoregressive,
- and simpler recurrence controls

where applicable.

---

### A — Operating Attractor

A represents a persistent operating regime associated with stable turbine operation.

The primary attractor reference may be estimated only from a predeclared Normal Operation calibration subset.

Challenge-arm data must not be used to construct the attractor.

The attractor estimator is not yet frozen.

---

### Eout / Γ — Regulated Export

The primary export candidate is:

**PowerOutput**

representing externally exported converter active power.

PowerOutput is reserved as the primary Eout measurement family.

It is not used as the primary P2 variable.

Its later uncertainty treatment must reflect the measurement limitations documented in the external metadata.

---

### SA — Selection Operator

A separate empirical SA claim is:

**NOT PART OF THE PRIMARY BFG-TEST-001 CONFIRMATORY CLAIM**

BFG-TEST-001 therefore does not claim to establish the full BFG selection architecture.

Any later SA interpretation requires a separate operational definition and test.

---

### TA — Admissible Transport

For BFG-TEST-001, TA is restricted to:

**within-carrier transport across preregistered temporal or scale representations.**

Cross-domain transport is not part of the primary BFG-TEST-001 confirmatory claim.

The exact scale representations and transport tolerance remain unfrozen.

---

### F — Falsification Gate

F will contain the later frozen decision criteria including:

- positive-support gate,
- negative gate,
- null-equivalence gate,
- mediator failure gate,
- Order Parameter failure gate,
- recursive-closure failure gate,
- non-collapse failure gate,
- scale-compatibility failure gate,
- and no-retuning violation.

The numerical thresholds are not yet frozen.

---

# Primary Order Parameter Role Mapping

The canonical BFG Order Parameter remains:

**Φ = (Eexp · I) ÷ (Ebind · I0)**

The formula itself is unchanged.

The following functional estimator families are now selected.

---

### Eexp — External Forcing / Differentiation Contribution

Primary functional source:

**P1 aerodynamic forcing**

Primary raw measurement family:

**WindSpeed**

Orientation information may later be incorporated only through a preregistered transformation.

Eexp must not use:

- PitchDeg,
- fault labels,
- PowerOutput,
- or challenge-arm classification information

in the primary confirmatory estimator.

Status:

**FUNCTIONAL FAMILY SELECTED — NUMERICAL ESTIMATOR NOT YET FROZEN**

---

### Ebind — Rotor Stabilization / Return Contribution

Primary functional source:

**P2 rotor/drivetrain response**

Primary raw measurement family:

**RotorSpeed**

Ebind will quantify a preregistered stabilization, bounded-return, or retention property of the P2 dynamics.

The exact estimator remains unfrozen.

Ebind must not directly use PitchDeg in the primary confirmatory Order Parameter estimator.

Status:

**FUNCTIONAL FAMILY SELECTED — NUMERICAL ESTIMATOR NOT YET FROZEN**

---

### I — Structured Closure Information

The primary I family will be derived from:

**structural SHM response**

using the independently measured acceleration and/or strain signal families of the primary dataset.

The intended function of I is to quantify structured information participating in persistent turbine response.

The later estimator may use preregistered quantities related to:

- contrast,
- integration,
- recurrence,
- closure contribution,
- invariant retention,

or a frozen subset of these components.

No component weights are yet authorized.

Fault labels must not enter I.

PitchDeg must not directly enter the primary I estimator.

Status:

**FUNCTIONAL FAMILY SELECTED — NUMERICAL ESTIMATOR NOT YET FROZEN**

---

### I0 — Structured-Information Reference Scale

I0 will be constructed from the same frozen I estimator used for I.

The reference scale may be estimated only from the predeclared Normal Operation calibration subset.

After calibration:

**I0 must remain fixed for all held-out Normal Operation and challenge-arm evaluations.**

Challenge-arm data must not determine I0.

Status:

**REFERENCE FAMILY SELECTED — VALUE NOT YET FROZEN**

---

## Primary Φ Anti-Circularity Firewall

The primary confirmatory Φ estimator must be:

**N-blind at the algebraic input level.**

Therefore the primary Φ construction must not directly include:

**PitchDeg**

or any other direct N measurement inside:

- Eexp,
- Ebind,
- I,
- or I0.

The purpose is to prevent mediator ablation from changing Φ merely because N was algebraically inserted into the Φ estimator.

N may influence Φ indirectly through real turbine dynamics.

That indirect influence is the quantity to be tested.

---

## Primary Measurement-Family Separation

For the primary confirmatory analysis, the measurement families are reserved as follows:

**WindSpeed → P1 / Eexp family**

**RotorSpeed → P2 / Ebind family**

**PitchDeg → N family**

**PowerOutput → Eout family**

**Structural acceleration / strain → I and I0 family**

This separation is intended to reduce circular reuse of the same signal across multiple BFG roles.

Alternative reuse requires explicit preregistration before target inspection.

---

## Label Firewall

The following external condition labels must not participate in construction of:

- P1,
- P2,
- N,
- Eexp,
- Ebind,
- I,
- I0,
- K,
- RC,
- Φ,
- or εcomm.

The labels may be used only after the relevant constructions have been frozen for confirmatory evaluation.

---

## Positive-Candidate Boundary

Normal Operation remains the:

**Positive-Candidate Arm**

but is not automatically classified as BFG-positive.

A positive result requires the later frozen positive-support gates to pass.

If held-out Normal Operation fails those gates, the result must be retained.

---

## Challenge-Arm Boundary

The three challenge conditions remain:

1. collective pitch-system mechanical failure,
2. aerodynamic imbalance,
3. rotor icing.

No challenge arm is assumed in advance to produce a specific numerical BFG signature.

Mechanistic directional predictions must be declared before confirmatory evaluation.

---

## Functional Freeze Decision

The following functional assignments are now frozen for BFG-TEST-001:

**P1 = external aerodynamic forcing**

**P2 = rotor/drivetrain dynamical response**

**N = collective pitch regulation**

**Eout = electrical power export**

**Eexp family = P1-derived external forcing**

**Ebind family = P2-derived stabilization / return**

**I family = structural SHM closure-information**

**I0 family = calibration reference of the same I estimator**

These assignments may not be replaced after target-result inspection while retaining confirmatory status.

---

## What Is Not Yet Frozen

The following remain open:

- temporal synchronization,
- dataset alignment,
- calibration split,
- held-out split,
- analysis-window duration,
- resampling,
- filtering,
- normalization,
- Eexp estimator,
- Ebind estimator,
- I estimator,
- I0 numerical value,
- RC estimator,
- attractor estimator,
- Φ corridor,
- εcomm,
- δN,
- primary endpoint,
- statistical model,
- null-model implementation,
- ablation implementation,
- success threshold,
- failure threshold,
- and stopping rules.

---

## Current Role-Mapping Decision

**Functional BFG role mapping selected and frozen.**

**Numerical operationalization not yet frozen.**

**Primary Φ estimator remains uncomputed.**

**No target labels have been authorized for model construction.**

**No positive or negative BFG result has been evaluated.**

**Version:** 0.5-draft

**Date:** 2026-08-29

**Copyright © 2026 Marcel Theodor Wende**
