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

---

## Blind Partition, Temporal Alignment & Calibration Protocol

### Purpose

This section freezes the data-partition and temporal-alignment logic before numerical BFG estimator construction and before confirmatory target evaluation.

The purpose is to prevent:

- temporal leakage,
- challenge-arm leakage,
- threshold chasing,
- outcome-driven window selection,
- post-hoc synchronization,
- and reuse of held-out data for model construction.

This section freezes the protocol.

It does not yet execute the partition.

---

## Data Access Classes

Four data-access classes are defined.

### Class A — Metadata Only

Permitted before numerical operationalization:

- filenames,
- archive structure,
- sensor metadata,
- channel names,
- units,
- sampling rates,
- timestamp format,
- measurement reliability metadata,
- turbine metadata,
- documented carrier-condition labels.

No signal-value optimization is permitted.

---

### Class B — Normal Calibration A

A subset of externally documented Normal Operation data will be used for:

- estimator construction,
- dimensional checks,
- numerical implementation,
- synchronization verification,
- feature-definition development within already frozen functional families,
- and model fitting where required.

Target challenge-arm data must not enter Calibration A.

---

### Class C — Normal Calibration B

A second independent Normal Operation subset will be used only for:

- selecting among already declared candidate estimator implementations,
- estimating calibration reference values,
- estimating I0,
- setting preregistered tolerances,
- setting frozen decision thresholds,
- and rejecting unstable implementations.

Calibration B must not be repeatedly reused after threshold freeze.

---

### Class D — Locked Confirmatory Evaluation

The following data are locked from estimator construction and threshold selection:

1. held-out Normal Operation,
2. collective pitch-system mechanical failure,
3. aerodynamic imbalance,
4. rotor icing.

These data may be evaluated only after the numerical operationalization, null models, endpoints, thresholds, and decision rules have been frozen.

---

# Primary Normal-Operation Partition

Normal Operation will be partitioned into:

**50% — Calibration A**

**25% — Calibration B**

**25% — Positive Holdout**

The split must be performed using temporal acquisition groups rather than individual randomly shuffled samples.

The purpose is to prevent autocorrelation leakage.

---

## Atomic Partition Unit

The preferred atomic partition unit is:

**one externally identifiable uninterrupted acquisition session or one native HDF5 acquisition group.**

Acquisition units are ordered chronologically using timestamps only.

Signal values must not be used to determine partition membership.

Where multiple acquisition units occur within one continuous recording day, they may be grouped into a single temporal block before partitioning.

---

## Partition Allocation Rule

After chronological ordering of eligible Normal Operation acquisition units:

- the earliest approximately 50% of total eligible duration becomes Calibration A,
- the next approximately 25% becomes Calibration B,
- the final approximately 25% becomes Positive Holdout.

Allocation is based on cumulative eligible duration rather than number of files.

No unit may be reassigned because of its observed BFG score, Φ value, fault-like appearance, spectral structure, or model performance.

---

## Partition Fallback Rule

If the native file structure does not provide enough independent acquisition units for a 50/25/25 grouped split:

1. recordings will first be divided into chronologically ordered contiguous super-blocks,
2. super-block boundaries will be based on time only,
3. the same 50/25/25 duration rule will then be applied.

The fallback rule must not depend on signal values.

If an adequate temporally separated split cannot be constructed, confirmatory BFG-TEST-001 must be suspended rather than rescued by random sample-level splitting.

---

# Temporal Leakage Guard

A temporal guard interval is required at every boundary between:

- Calibration A and Calibration B,
- Calibration B and Positive Holdout.

The guard interval is:

**10 minutes**

or:

**five times the longest primary analysis scale**

whichever is larger.

All samples inside the guard interval are excluded from confirmatory analysis.

They must not be reassigned to another partition.

---

# Challenge-Arm Lock

All three externally defined challenge arms are:

**100% confirmatory held-out data**

during estimator construction.

Challenge-arm signal values must not be used to:

- define P1, P2, or N,
- choose Eexp or Ebind formulas,
- construct I,
- determine I0,
- select RC,
- define the attractor,
- select spectral bands,
- choose normalization,
- choose thresholds,
- tune εcomm,
- tune δN,
- select features,
- or determine success criteria.

Challenge metadata may be inspected.

Challenge signal outcomes may not.

---

# Primary Temporal Representation

The primary analysis uses native-rate signals inside common time windows.

Raw structural signals will not be collapsed to 1 Hz merely to match SCADA.

Instead:

**features are computed at the native sampling rate of each measurement family and are subsequently aligned at the window level.**

This preserves high-frequency structural information.

---

## Primary Window

The primary confirmatory analysis window is:

**60 seconds**

Primary windows are:

- non-overlapping,
- timestamp-defined,
- and independent of observed signal behavior.

A window must not be shifted to capture a visible anomaly or maximize condition separation.

---

# Predeclared Scale Family

For the Trinity–Order scale-compatibility component, the temporal scale family is:

**λ1 = 30 seconds**

**λ2 = 60 seconds**

**λ3 = 120 seconds**

The 60-second representation is the primary reporting scale.

The 30-second and 120-second representations are scale-transfer tests.

These scales must not be changed after challenge-arm inspection.

---

## Nested Scale Construction

Scale representations will be constructed from common timestamp boundaries such that, where data coverage permits:

- four 30-second windows correspond to one 120-second master block,
- two 60-second windows correspond to the same 120-second master block.

This nesting is used to compare scale-dependent Trinity–Order readouts without changing the underlying time interval.

The master block, not an individual subwindow, is the unit used to prevent cross-partition leakage.

---

# Window Completeness Rule

A window is eligible for the primary confirmatory analysis only when each required channel for the relevant estimator has:

**at least 90% expected sample coverage**

within that window.

Windows below this coverage threshold are excluded according to the frozen rule.

They must not be repaired selectively according to condition label.

---

# Missing-Data Rule

The primary confirmatory analysis uses:

**no outcome-dependent imputation.**

Missing values are not filled using challenge-arm information.

No interpolation across long gaps is permitted.

If a numerical estimator requires complete samples, the corresponding window is excluded under the preregistered coverage rule.

Any later imputation-based sensitivity analysis must be labeled secondary or exploratory unless separately frozen before confirmatory evaluation.

---

# Native-Rate Processing Rule

The following principle is frozen:

**feature extraction first, cross-family alignment second.**

Each measurement family is processed at its native declared sampling rate.

The primary analysis does not downsample 200 Hz structural data directly to 1 Hz raw measurements.

Any required filtering is applied only within a frozen estimator specification developed using Calibration A.

---

# Anti-Aliasing Boundary

No raw downsampling requiring anti-alias filtering is part of the primary temporal representation at this stage.

If a later estimator requires explicit downsampling:

- the filter family,
- cutoff rule,
- order,
- edge treatment,
- and target sampling rate

must be frozen before confirmatory evaluation.

No filter may be selected because it improves challenge-arm separation.

---

# Timestamp Alignment

All signals are aligned using recorded timestamps.

The following are not permitted:

- visual manual shifting,
- condition-specific lag correction,
- fault-specific time offsets,
- or maximizing alignment separately for each challenge arm.

Timezone information must be taken from source metadata where available.

An undocumented timezone must not be guessed.

Any conversion must be recorded in the Data Manifest.

---

# Primary–Supplementary Dataset Merge Gate

The supplementary 1 Hz SCADA dataset containing PitchDeg must not be merged automatically with the primary ETH Zurich SHM / SCADA dataset.

Before merge, the following must be verified:

1. exact physical turbine identity,
2. compatible site / turbine metadata,
3. overlapping measurement period,
4. compatible timestamp reference,
5. compatible signal definitions,
6. compatible units,
7. and record-level temporal correspondence.

The verification must be documented without using challenge-condition BFG outcomes.

---

## Supplementary Merge Pass

If exact carrier identity and temporal compatibility are established:

**PitchDeg may remain the direct measured candidate component of N**

under the already frozen functional-role mapping.

---

## Supplementary Merge Failure

If exact identity or temporal compatibility cannot be established:

**the supplementary dataset must not be merged into the primary confirmatory carrier.**

In that case:

**the direct-PitchDeg N component is suspended for BFG-TEST-001.**

A replacement direct-N signal must not be introduced after target-result inspection.

A reconstructed or latent N construction would require a separate preregistered test or an explicitly exploratory extension.

---

# Calibration-Only Alignment Exception

If the two datasets are confirmed to represent the same physical turbine and overlapping period but exhibit an unresolved constant clock offset, a single global offset may be estimated using:

**Calibration A only**

and shared non-target operational signals.

The offset must then be frozen before:

- Calibration B threshold setting,
- Positive Holdout inspection,
- or any Challenge Arm inspection.

A separate offset must not be fitted for each operating condition.

If a stable global alignment cannot be obtained, the supplementary merge fails.

---

# Calibration A Permissions

After this partition protocol is executed, Calibration A may be inspected for:

- numerical estimator feasibility,
- channel quality,
- dimensional consistency,
- measurement-scale behavior,
- synchronization,
- numerical stability,
- and development of the already declared BFG functional estimator families.

Calibration A may not be used to redefine the external carrier labels.

---

# Calibration B Permissions

Calibration B may be used to:

- compare only preregistered candidate implementations developed from Calibration A,
- set I0,
- establish the Normal Operation reference distribution,
- set the Φ corridor,
- set εcomm tolerance,
- set mediator-loss thresholds,
- set recursive-stability thresholds,
- and freeze the final primary endpoint.

Once these quantities are frozen:

**Calibration B becomes closed for further tuning.**

---

# Positive Holdout Boundary

The final 25% Normal Operation partition is:

**Positive Holdout**

It is not used for construction or tuning.

Its purpose is to test whether the frozen BFG representation recognizes externally documented normal persistent operation without having been optimized directly on those records.

Failure on Positive Holdout must be retained.

---

# Positive Evidence Boundary

A candidate-positive result must not be defined only as:

**challenge arms score worse than Normal Operation.**

Positive evidence also requires the frozen model to satisfy its own preregistered admissibility criteria on unseen Positive Holdout data.

Thus BFG-TEST-001 contains both:

**positive recovery**

and:

**negative / perturbation discrimination**

within one frozen protocol.

---

# Challenge Evaluation Order

After full preregistration freeze, the confirmatory evaluation order is:

**Stage 1 — Positive Holdout**

then:

**Stage 2 — Collective Pitch-System Mechanical Failure**

then:

**Stage 3 — Aerodynamic Imbalance**

then:

**Stage 4 — Rotor Icing**

All stages use the same frozen operator and thresholds.

Results from an earlier stage must not be used to retune a later stage.

---

# No-Retuning Partition Rule

After partition execution:

- partition membership is immutable,
- excluded guard intervals remain excluded,
- held-out records remain held out,
- thresholds cannot be refitted on held-out outcomes,
- and failed windows cannot be selectively removed because they harm the BFG result.

Any deviation requires:

1. explicit documentation,
2. loss of confirmatory status for the affected analysis,
3. and classification as exploratory unless a new preregistration is created.

---

# Data-Access Audit Record

Before confirmatory execution, the following must be recorded:

- dataset DOI and version,
- original filename,
- original checksum,
- local SHA-256,
- download date,
- acquisition-unit identifiers,
- partition membership,
- exclusion reason where applicable,
- guard-band membership,
- temporal scale,
- timestamp convention,
- and preprocessing configuration hash.

This record will later become part of the BFG-TEST-001 Data Manifest.

---

# Current Partition Decision

**Blind partition protocol frozen.**

**Normal Operation split = 50% Calibration A / 25% Calibration B / 25% Positive Holdout.**

**Challenge arms = 100% held out during estimator construction.**

**Primary window = 60 seconds.**

**Scale family = 30 / 60 / 120 seconds.**

**Temporal guard = 10 minutes or five times the maximum analysis scale, whichever is larger.**

**Minimum required sample coverage = 90%.**

**Native-rate feature extraction precedes cross-family alignment.**

**Supplementary PitchDeg merge remains conditional on exact carrier and timestamp verification.**

**No confirmatory target evaluation has yet occurred.**

---

## Data Acquisition, Integrity & Manifest Freeze

### Purpose

This section freezes the acquisition, integrity-verification, raw-data preservation, and provenance rules for BFG-TEST-001 before numerical BFG analysis begins.

Data acquisition itself does not constitute target-result inspection.

Downloaded challenge archives must remain outcome-blind until the confirmatory protocol authorizes their evaluation.

---

## Primary External Dataset

Dataset:

**Aventa AV-7 ETH Zurich Research Wind Turbine SCADA and high frequency Structural Health Monitoring (SHM) data**

Version:

**v6**

DOI:

**10.5281/zenodo.8229750**

The following four upstream archives are the authoritative primary carrier files.

### Normal Operation

Filename:

`aventa_normal_operation_for_system_identification.zip`

Published size:

**6.8 GB**

Published MD5:

`407114000b3c39a92e3a0cd8d73cc5af`

Role:

**Normal Operation source / future Calibration A, Calibration B, and Positive Holdout**

---

### Collective Pitch-System Mechanical Failure

Filename:

`aventa_failure_flexible_coupling_of_collective_pitch_drive.zip`

Published size:

**17.6 GB**

Published MD5:

`87a74879cbefabbc649ebca0c4003113`

Role:

**Locked Challenge Arm 1**

---

### Aerodynamic Imbalance

Filename:

`aventa_blade_aerodynamic_imbalance.zip`

Published size:

**17.1 GB**

Published MD5:

`1a1fa895fbf3536a0dad4ff1e818390c`

Role:

**Locked Challenge Arm 2**

---

### Rotor Icing

Filename:

`aventa_rotor_icing.zip`

Published size:

**7.7 GB**

Published MD5:

`87e8a2654cf524b72f5859f5c6c53089`

Role:

**Locked Challenge Arm 3**

---

## Supplementary SCADA Dataset

Dataset:

**Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA**

Version:

**v2**

DOI:

**10.5281/zenodo.15700928**

Primary time-series file:

`Aventa_AV7_IET_OST_SCADA.csv`

Published size:

**3.1 GB**

Published MD5:

`0434ccfb5a05f91225796063942538f5`

Associated metadata files:

`Aventa_AV_7_IET_OST_WT_metadata.json`

Published MD5:

`53869da8ceea9e4fe7fa8441637f91a1`

`SCADA_Channels_Metadata.csv`

Published MD5:

`470954defe72e3df328c4ce06190e3eb`

`turbine_status_mapping.json`

Published MD5:

`79847877526bb28018f072a0ba39b1ec`

The supplementary source remains subject to the previously frozen merge gate.

Acquisition does not authorize cross-dataset merging.

---

## Raw-Data Immutability Rule

Every upstream file must be preserved byte-for-byte after download.

The original files must not be:

- renamed without provenance recording,
- recompressed,
- edited,
- converted,
- normalized,
- truncated,
- repaired,
- or overwritten.

All transformed data must be written to a separate processed-data location.

The raw source is immutable.

---

## Integrity Verification

Two integrity layers are required.

### Layer 1 — Upstream MD5

The locally downloaded file must reproduce the MD5 published by Zenodo.

A mismatch means:

**ACQUISITION INTEGRITY FAILURE**

The affected file must not be used.

The file must be downloaded again from the authoritative record.

### Layer 2 — Local SHA-256

After a successful MD5 check, a SHA-256 hash will be computed locally for every acquired source file.

The SHA-256 becomes the BFG-TEST-001 local provenance fingerprint.

Both values must be retained:

- upstream MD5,
- local SHA-256.

---

## Raw Challenge Seal

The three Challenge Arm archives may be:

- downloaded,
- byte-counted,
- checksummed,
- and inventoried.

They must not yet be used for:

- plotting,
- descriptive outcome statistics,
- BFG estimator construction,
- feature selection,
- threshold selection,
- spectral-band selection,
- Φ construction,
- mediator optimization,
- or model tuning.

Reading archive filenames and metadata structures remains permitted.

Signal-value evaluation remains locked.

---

## Normal-Operation Access Boundary

The Normal Operation archive may initially be inspected only for:

- archive structure,
- metadata,
- acquisition-unit identifiers,
- timestamps,
- duration,
- sampling metadata,
- and information required to execute the already frozen temporal partition.

Signal-value analysis begins only after partition membership has been assigned.

After partitioning:

- Calibration A may be opened under its declared permissions,
- Calibration B remains restricted to its declared calibration function,
- Positive Holdout remains locked.

---

## Supplementary SCADA Access Boundary

The supplementary metadata files may be inspected immediately.

The large supplementary SCADA time series may initially be inspected only for:

- timestamp coverage,
- timestamp format,
- channel presence,
- physical units,
- missing timestamp structure,
- and exact carrier-alignment verification.

Target-dependent BFG interpretation is prohibited.

The PitchDeg signal must not be evaluated against fault labels before the merge and operationalization gates are frozen.

---

## Data Manifest Requirement

Every acquired file must receive a Data Manifest entry containing at minimum:

`dataset_id`

`dataset_version`

`doi`

`source_role`

`original_filename`

`published_size`

`upstream_md5`

`local_md5`

`local_sha256`

`integrity_status`

`download_date`

`raw_path`

`processing_status`

`partition_status`

`access_class`

`notes`

No file lacking a successful integrity record may enter confirmatory processing.

---

## Processing Separation

The local data workspace must contain logically distinct locations for:

`raw`

`metadata`

`processed`

`manifests`

`logs`

Raw files are never modified in place.

Processed outputs must be reproducible from:

**raw input + frozen configuration + versioned code**

---

## Data Redistribution Boundary

The authoritative public scientific repositories remain the external source of the raw carrier data.

BFG-TEST-001 does not require the large upstream carrier files to be committed to the BalanceFieldResearch Git repository.

The Git repository should contain:

- provenance records,
- checksums,
- manifests,
- frozen configurations,
- analysis code,
- null-model code,
- result summaries,
- and reproducibility documentation.

Raw upstream data remain externally sourced unless redistribution rights and repository policy are separately verified.

---

## Acquisition Failure Gate

Data acquisition is classified as failed or incomplete if:

- an upstream MD5 cannot be reproduced,
- an archive is corrupted,
- an authoritative source file cannot be identified,
- dataset version cannot be verified,
- essential metadata are missing,
- or provenance cannot be reconstructed.

Such a failure is a data-layer failure.

It is not a positive or negative empirical BFG result.

---

## Current Data Decision

**Authoritative upstream datasets identified.**

**Dataset versions frozen.**

**Authoritative filenames frozen.**

**Published MD5 fingerprints frozen.**

**Raw-data immutability rule frozen.**

**Local SHA-256 requirement frozen.**

**Challenge signal-value inspection remains locked.**

**No BFG outcome has yet been evaluated.**

---

## Remote Data Access Amendment

### Purpose

This amendment replaces the requirement for a complete local mirror of the large Aventa carrier archives with a remote-access and blockwise-processing strategy.

The scientific purpose is unchanged.

The amendment is introduced before confirmatory target-result inspection and therefore does not constitute outcome-driven retuning.

---

## Authoritative Raw-Data Location

The authoritative raw carrier data remain hosted at their original Zenodo records.

A complete local copy of all large carrier archives is not required for BFG-TEST-001.

The authoritative external records remain:

Primary carrier:

**Aventa AV-7 ETH Zurich Research Wind Turbine SCADA and high frequency Structural Health Monitoring data**

Version:

**v6**

DOI:

**10.5281/zenodo.8229750**

Supplementary SCADA source:

**Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA**

Version:

**v2**

DOI:

**10.5281/zenodo.15700928**

---

## Remote Processing Rule

BFG-TEST-001 may access carrier data remotely using a cloud or hosted computation environment.

Permitted environments include reproducible Python-based hosted notebook or compute environments.

Remote processing must preserve the same preregistered:

- carrier identity,
- partition rules,
- temporal windows,
- access classes,
- challenge-arm lock,
- functional role mapping,
- no-retuning rules,
- and confirmatory decision structure.

The compute location may change.

The scientific rules may not.

---

## Blockwise Access Rule

Full carrier archives do not need to be permanently downloaded to the local research computer.

Only the data required for the currently authorized stage may be fetched or materialized.

Permitted block selection must be based only on:

- externally defined file identity,
- acquisition identifier,
- timestamp,
- preregistered temporal partition,
- declared analysis window,
- or deterministic record index.

Block selection must not be based on:

- observed Φ,
- fault severity,
- anomaly score,
- classification performance,
- visible signal pattern,
- mediator score,
- or preferred BFG outcome.

---

## Challenge-Arm Remote Seal

Remote access does not weaken the challenge-arm lock.

Before final operational freeze, Challenge Arm data may not be inspected for outcome-dependent signal behavior.

Challenge files or blocks may be:

- identified,
- referenced,
- checksummed where feasible,
- structurally inventoried,
- and prepared for later execution.

They must not yet be used for:

- estimator construction,
- threshold tuning,
- feature selection,
- fault-versus-normal plotting,
- Φ optimization,
- mediator optimization,
- or result interpretation.

---

## Remote Provenance Record

Every remotely accessed analysis block used in BFG-TEST-001 must later receive a provenance record containing, where applicable:

- dataset ID,
- dataset version,
- DOI,
- authoritative source record,
- original filename,
- upstream checksum,
- acquisition identifier,
- timestamp interval,
- record or byte range where available,
- local or cloud cache filename,
- local SHA-256 of the materialized block or derived artifact,
- processing script version,
- configuration hash,
- access date,
- and partition status.

---

## Integrity Boundary

The published upstream checksum remains the integrity anchor for the authoritative source file.

A complete locally recomputed checksum of a multi-gigabyte source archive is not required when the complete archive is not downloaded.

For every materialized local or cloud artifact used in analysis:

**a local SHA-256 must be recorded.**

Derived results must remain reproducible from:

**authoritative source + frozen selection rule + frozen configuration + versioned code**

---

## Local-Laptop Boundary

The local research computer is not required to store the complete external carrier dataset.

Large raw carrier files should not be committed to the BalanceFieldResearch repository.

The repository will instead contain compact reproducibility artifacts including:

- preregistration,
- source manifest,
- data dictionary,
- checksums for materialized artifacts,
- frozen configuration,
- analysis code,
- null-model code,
- result summaries,
- and audit records.

---

## Cloud-Environment Boundary

Use of a hosted computation environment does not itself provide scientific evidence.

The environment is treated only as execution infrastructure.

Package versions, script versions, random seeds where applicable, and configuration hashes must be recorded before confirmatory execution.

A change of cloud provider does not count as retuning if the frozen analytical rules and numerical implementation remain equivalent.

---

## Remote Access Failure Gate

Remote execution is classified as operationally failed or incomplete if:

- the authoritative source cannot be verified,
- requested records cannot be deterministically reproduced,
- timestamp or record selection cannot be reconstructed,
- required provenance is lost,
- or derived artifacts cannot be linked back to the authoritative carrier source.

Such a failure is an infrastructure or provenance failure.

It is not a positive or negative empirical BFG result.

---

## Amendment Decision

**Complete local raw-data mirroring is no longer required.**

**Authoritative Zenodo records remain the raw-data source of record.**

**Remote and blockwise processing is permitted.**

**Challenge-arm access restrictions remain unchanged.**

**No target-result inspection has yet occurred.**

**No BFG positive or negative empirical result has yet been evaluated.**

**Version:** 0.8-draft

**Date:** 2026-08-29

**Copyright © 2026 Marcel Theodor Wende**
