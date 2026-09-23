# BFG Emergence Studio

A working experimental software prototype based on Marcel Theodor Wende's
Balance–Field Framework (BFG), especially the Canonical Universal Reclosure
Architecture and the Canonical Reclosure / Structural Novelty theorem.

## Purpose

This is a domain-agnostic computational laboratory for asking:

- Which structures persist?
- Which structures reclose into a successor?
- When is the successor merely inherited structure?
- When does a strict spectral novelty witness fire?
- When does formation fail?
- Can we search for initial structures that generate long-lived, novel closure trajectories?
- Can different carrier models plug into the same reclosure grammar?

## Implemented BFG core

- `C=(I+Y)^(-1)`, `B=Y(I+Y)^(-1)`
- graph metric `G=I+Y`
- numerical finite-dimensional bounded non-decay / peripheral persistence sector
- graph-metric persistent projector
- reciprocal endogenous order
- cross-fed packet
- canonical polar partial isometry
- reclosed formation operator
- simple-negative-mode formation gate
- inherited-support spectral novelty
- commutator diagnostics on the compatible support stratum

The next positive geometry is a **carrier adapter**. This is deliberate:
the universal BFG paper gives the Gram rebuild in carrier-dependent form.
The included `ReferenceGramCarrier` is an executable research/demo carrier,
not a claim that every natural system uses that specific reconstruction.

## Install and run

```bash
cd BFG_Emergence_Studio
pip install -e .
python -m bfg_studio demo --steps 12 --seed 7
python -m bfg_studio control --steps 6 --seed 7
python -m bfg_studio search --trials 150 --steps 8 --seed 7
```

## What the commands do

- `demo`: noncommuting random seed, generative multi-level reclosure
- `control`: commuting inheritance control
- `search`: inverse search for seed structures with long-lived novelty
- `alife`: self-organization on an adaptive carrier
- `alife-search`: inverse search for self-organizing seeds
- `population`: dimension change, fission, independent child units
- `evolution`: heritable variation and selection
- `environment`: evolution under changing external conditions
- `learning`: within-lifetime learning, memory, recall, and memory-disabled control
- `self-model`: recursive world/self readout, prospective self-prediction, and causal action selection
- `perspective`: Level-29 multiplicity/unity closure into a persistent organizational standpoint
- `identity`: Level-30 temporal continuity through bounded historical/present-self mediation
- `benchmark`: frozen cross-layer reference benchmark suite
- `robustness`: randomized algebraic, tolerance, and carrier-sensitivity audit
- `checkpoint`: hash-verified save/load/resume of a BFG state
- `sweep`: parallel seed sweeps for self-organization, population, or evolution
- `hardening`: benchmark + robustness + recursive-stability + checkpoint audit in one command
- `enso-prepare`: development-only ENSO/Pacific-SST readiness preflight
- `enso-validate`: prospective ENSO confirmation using external future data + one-time permit
- `portfolio`: audit all active empirical carriers without opening held-out data
- `cross-domain`: compare development-only BFG invariant coordinates across READY carriers
- `stability-audit`: audit the finite-dimensional recursive power-boundedness theorem hypotheses
- `math-audit`: audit the integrated BFG mathematical closure layer
- `transfer-audit`: send all allowed real development/calibration states through the common finite master runtime
- `formation-analysis`: analyze formation-depth normalization, neutral-load contraction, tolerance sensitivity, and the terminal surface
- `small-load-audit`: verify the multidimensional quadratic successor-load theorem and sufficient depth bounds

Each run can write CSV/JSON and trajectory plots.

## Carrier adapters

Subclass `CarrierAdapter` to map the same BFG core onto:

- materials / lattices
- reaction networks / protocell models
- adaptive graphs
- agent systems
- field discretizations
- other mathematical carriers

That is the intended path toward genuinely cross-domain software.

## Scientific scope

A successful software run is not empirical evidence that a natural system
realizes BFG. The current BFG papers explicitly separate mathematical closure
from natural realization. See `SCIENTIFIC_SCOPE.md`.


## Self-organization / Artificial Life

The master build includes a concrete `SelfOrganizingNetworkCarrier`.

Run one self-organization experiment:

```bash
python -m bfg_studio alife --nodes 24 --rank 6 --steps 18 --seed 11
```

Search for long-lived self-organizing seeds:

```bash
python -m bfg_studio alife-search --nodes 24 --rank 6 --steps 18 --trials 60 --top 5
```

The carrier reports:

- persistent BFG reclosure generations
- spectral novelty
- resource maintenance
- connected structural clusters
- largest-cluster fraction
- graph connectivity
- multi-cluster states
- cluster ancestry and `split_like` lineage events

`split_like` is deliberately narrower than "reproduction": it means one
predecessor cluster has substantial node-overlap with two or more successor
clusters. The current node population is fixed, so this is structural fission,
not biological reproduction.

The self-organization rules are carrier-specific research rules. They do not
replace or modify the generic BFG reclosure core.


## Independent population dynamics

The master build now contains a population layer in which a self-organizing
BFG structure can become more than a multi-cluster state.

A **fission** is recorded only when:
1. at least two disconnected successor components are independently viable;
2. the parent unit terminates as one identity;
3. each child receives its own `BFGState`, unit ID, state dimension, age, and
   subsequent reclosure trajectory.

Run the population experiment:

```bash
python -m bfg_studio population \
  --nodes 24 --rank 6 --generations 28 \
  --seed 1341550191 \
  --node-birth-threshold 1.10
```

The reference seed currently produces one controlled fission:
`U0 -> U1 (17 nodes) + U2 (5 nodes)` at generation 17. The two remaining
one-node fragments are below the viability floor and are recorded as loss.

The same population layer supports **dimension-changing carrier dynamics**:
high-resource nodes can allocate part of their resource into a new node,
while persistently depleted nodes can be removed. For example:

```bash
python -m bfg_studio population \
  --nodes 20 --rank 5 --generations 20 \
  --seed 7 --node-birth-threshold 0.70
```

In the included reference run the carrier grows from 20 to 30 nodes through
ten node-birth events while remaining BFG-admissible for all 20 tested steps.

These are software-level self-organization and population experiments. They
are not presented as an empirical model of biological reproduction.


## Heritable evolution and selection

The master build now supports a software-level evolutionary layer on top of
independent BFG population units.

Heritable carrier traits currently include:

- formation drive
- geometric neighbor scale
- resource adaptation rate
- topology adaptation rate
- export cost
- node-birth threshold
- fission threshold

At fission, each child receives the parent's trait vector and then undergoes
bounded stochastic mutation. The child is subsequently rebuilt with its own
inherited/mutated carrier parameters, so the variation affects later BFG
reclosure rather than existing only as metadata.

A finite carrying capacity creates differential survival. Selection uses an
explicitly carrier-level organization score derived from maintenance,
viability, resource entropy, connectivity, age, and recent structural novelty.

Example:

```bash
python -m bfg_studio evolution \
  --nodes 24 --rank 6 --generations 32 \
  --seed 1341550191 \
  --node-birth-threshold 1.05 \
  --mutation-rate 1.0 \
  --mutation-sigma 0.05 \
  --carrying-capacity 1
```

The included reference run produces:
- one parent fission into two independent children,
- two inherited but mutated trait vectors,
- one capacity-limited selection event,
- continued BFG reclosure of the surviving child.

Reports include population size, mean fitness, lineage depth, trait means and
variances, mutation events, selection events, and a lineage plot.

This is a software evolution analogue. The heritable trait vector and
selection score are carrier-model choices, not universal BFG theorems.


## Changing environments and adaptation

The master build now includes an explicit environmental-evolution layer.

An environment can change:
- resource supply,
- structural disturbance,
- carrying capacity,
- the preferred values of heritable carrier traits.

Environmental forcing acts on the carrier **before** the next BFG reclosure,
so it can alter later formation and persistence. Selection then acts on a
combination of intrinsic organization and environment/trait match.

Built-in programs:
- `shift`: one auditable regime change,
- `seasonal`: repeated alternating environmental phases.

Example:

```bash
python -m bfg_studio environment \
  --program shift \
  --generations 60 \
  --shift-generation 24 \
  --founders 12 \
  --founder-sigma 0.18 \
  --seed 1341550191
```

The included reference run starts with standing heritable variation. Under the
new environment at generation 24, environmental carrying capacity falls from
8 to 4. In that selection round the mean trait/environment match rises from
approximately `0.364` to `0.424`. Later fission/mutation events continue under
the changed environment.

Reports distinguish:
- old-environment match before the shift,
- new-environment match before selection,
- new-environment match after selection,
- immediate selection gain,
- final match,
- net adaptation from the new-environment baseline,
- maintenance and population response.

This distinction prevents a misleading comparison of match values computed
against different environmental targets.


## Within-lifetime learning and memory

This layer is positioned after environmental adaptation and before later
self-model / perspective stages, matching the BFG ordering:

`Action -> Learning -> Memory -> Self-Model`.

The implementation keeps three levels separate:

1. **Genotype / inherited carrier traits** — changed only by evolutionary mutation.
2. **Plastic policy** — changed within one lifetime through bounded experience-dependent learning.
3. **Memory closure** — contextual witnesses that can be recovered after separated recursive cycles.

The software operationalizes the BFG learning relation

`s(t+1) = f(s(t), M(t), a(t), r(t))`

and the policy deformation

`pi(t+1) = pi(t) + Delta pi(t)`

with an explicit maximum policy-step norm. A policy change therefore cannot
jump arbitrarily across carrier space.

Memory is not implemented as a passive log. Each memory slot contains:

- a sensed environmental cue,
- the best stabilized policy associated with that cue,
- the experienced scalar outcome,
- memory strength,
- creation/update/retrieval times.

A **witness recovery** is counted only when a previously encountered context
disappears and later returns after a declared temporal gap, and the same
memory trace is still recoverable.

The memory export channel implements BFG-style:

`compression -> abstraction -> forgetting`

by merging highly similar traces and removing weak/surplus traces when the
bounded memory capacity is exceeded.

The learning carrier also uses a bounded two-candidate experience test. From
the same pre-transition state it evaluates:

- the current/recalled stabilized policy,
- one small exploratory alternative,

under the same environmental disturbance realization. Only the better
BFG-admissible transition is committed. A memory-disabled control uses the
same environment but no retained policy or memory witness.

Run:

```bash
python -m bfg_studio learning \
  --generations 60 \
  --seed 1341550191 \
  --exploration-sigma 0.035 \
  --retrieval-blend 0.92
```

In the included reference run:

- all 61 committed BFG reclosures pass,
- two recurring contextual memory traces are formed,
- four temporally separated witness recoveries occur at generations
  20, 30, 40, and 50,
- 17 bounded policy updates occur,
- mean reward is higher than the memory-disabled control by about `+0.00947`,
- reward gain exactly at witness-recovery generations is about `+0.01224`,
- mean post-recall reward gain is about `+0.01007`.

These values are software-carrier results, not empirical neuroscience claims.
The generic BFG core is unchanged; learning/memory remains a downstream
carrier realization whose defining tests are adaptive plasticity and
recoverable witness persistence.


## Self-model closure

The master build now extends the cognitive carrier from memory to a declared
self-model closure. The implementation follows the BFG ordering in which
memory precedes self-model closure.

The software keeps the two poles explicit:

- `W`: a world readout from the current environmental carrier;
- `Os`: an organism readout containing resource state, maintenance,
  retained/export fractions, plastic-policy magnitude, and memory load.

They are not collapsed into one vector. A separate mediated readout is formed:

`Self = Cl_NSelf(W, Os)`

and the software checks a nonzero bounded world/self corridor.

The self-model adds a causal forward map:

`F_self(W_t, W_hat_{t+1}, Os_t, pi_t) -> (Os_hat_{t+1}, r_hat_{t+1})`

where the organism's own next-state prediction is learned online from committed
transitions only. Unchosen candidate futures are never used as training targets.

A self-model action is permitted only after:
- enough prospective observations exist,
- recent prediction error is competitive with a persistence baseline,
- the self-reference graph is reachable,
- recursive self-dynamics remain bounded near criticality.

Self-reference reachability is operationalized as a closed causal path:
persistent organism readout -> internal predictor -> policy-mediated action ->
later organism readout.

The explicit closure diagnostics are:
- world coherence,
- organism coherence,
- world/self separation corridor,
- mediated cross-coupling,
- self-reference reachability,
- bounded recurrent spectral radius,
- export of non-integrable self-predictions.

Run:

```bash
python -m bfg_studio self-model \
  --generations 80 \
  --seed 1341550191 \
  --min-observations 12 \
  --candidates 5 \
  --candidate-sigma 0.035 \
  --rho-max 1.04
```

In the included reference run:
- all `81/81` committed BFG reclosures pass,
- self-reference reachability is present for about `83.95%` of recorded steps,
- self-model closure passes on `68` steps,
- the model makes `61` self-model-based action decisions,
- `57` of those decisions differ from the unmodified current/recalled action,
- the final recurrent self radius is about `0.99433`,
- mean prospective self-state error is about `0.01272`,
- the persistence baseline error is about `0.01277`,
- self-prediction beats the persistence baseline on about `47.83%` of eligible steps,
- the self-model branch has a mean reward advantage of about `+0.00470`
  over the self-model-ablated control.

This is a software self-model realization, not a claim of consciousness.
The universal BFG layer treats self-model and later cognitive labels as
downstream realization hypotheses; the software therefore reports the
invariant structural tests separately from any interpretation.


## Perspective closure

The master build now implements BFG Level 29 directly after Self-Model Closure.

The declared BFG structure is:

`P1 = multiple self-representations`

`P2 = unified standpoint`

`NP = perspectival integration`

with

`Persp = Cl_NP(Sself_1, ..., Sself_n)`.

The software keeps five simultaneously inspectable self-representations:

- body/resource self,
- memory self,
- action/policy self,
- predictive self,
- world-relative self.

They are embedded into a shared seven-coordinate carrier, but are **not**
arithmetically summed. Neutral mediation assigns endogenous compatibility /
continuity weights, produces a bounded candidate center, and recursively
transports the previous standpoint:

`Persp(t+1) = Cl_NP(Persp(t), Sself_1(t+1), ..., Sself_n(t+1))`.

The operational `Here(t)` is the persistent perspective standpoint. It is an
organizational coordinate, not a physical position.

Closure requires the BFG multiplicity/unity corridor:

`epsilon_P < d_NP(multiplicity, unity) < L_P`

together with coherent active representations, bounded recursive persistence,
and a nonzero persistent standpoint.

Four explicit Level-29 failure surfaces are implemented and tested:

- perspectival fragmentation,
- representational collapse,
- over-unification / homogenization,
- recursive instability.

Non-integrable self-representations are not silently forced into the center.
They are exported through a declared `perspective_export` event, implementing
the BFG excess channel `E_Persp_excess -> Gamma_Persp`.

Perspective is causally downstream of the Self-Model. When closure is active,
candidate actions are scored primarily by the existing Self-Model prediction
and weakly by compatibility with the persistent standpoint. The default
perspective action weight is deliberately only `0.05`, so Level 29 organizes
lower closures rather than overwriting them.

Run:

```bash
python -m bfg_studio perspective \
  --generations 96 \
  --seed 1341550191 \
  --alpha 0.985 \
  --epsilon 0.035 \
  --max-distance 0.62 \
  --export-threshold 0.46 \
  --action-weight 0.05
```

In the included reference run:

- all `97/97` committed BFG reclosures pass,
- all 97 tested perspective states remain inside the declared closure corridor,
- mean standpoint persistence is about `0.99599`,
- recursive perspective radius is `0.985`,
- five self-representation channels remain differentiated,
- mean representation diversity is about `0.20731`,
- mean multiplicity/unity distance is reduced to about `0.26158`,
- the ablated branch has a larger mean distance of about `0.37711`,
- diversity is essentially preserved (`~0.20743` in the ablated branch),
- two non-integrable memory-self traces are explicitly exported,
- 85 decisions are made with active Perspective Closure,
- 83 of those alter the unmodified lower-closure action,
- mean reward difference versus the perspective-ablated branch is small but
  positive in this reference run (`~+0.00035`).

The main Level-29 result is therefore not reward maximization. It is:

**greater unity of standpoint without collapse of self-representational diversity.**

This module is a software realization of perspective closure. It does not by
itself establish consciousness, phenomenal awareness, or subjective experience.
Those are later and separately testable BFG closure claims.


## Identity closure

The master build implements BFG Level 30 directly after Perspective Closure.

The declared source structure is:

`P1 = historical self`

`P2 = present self`

`NId = identity mediation`

with

`Id = Cl_NId(Selfpast, Selfnow)`

and the recursive form

`Id(t+1) = Cl_NId(Id(t), Self(t+1))`.

Identity is therefore not strict sameness. It is also not unrestricted change.
The operational closure condition is the BFG temporal corridor:

`epsilon_Id < d_NId(Selfpast, Selfnow) < L_Id`.

The current Perspective standpoint is the present-self carrier. The recursively
retained Identity state is the historical-self carrier.

The module measures two quantities simultaneously:

- **persistent self-index** — similarity of the recursive Identity witness to
  the initially established self-index;
- **transverse adaptation** — change orthogonal to that persistent index.

This realizes the stronger universal BFG identity signature:
a persistent self-index remains while transverse carrier degrees adapt.

Identity failure surfaces are implemented explicitly:

- fragmentation: temporal distance exceeds `L_Id`,
- rigidity: temporal distance approaches the lower bound,
- recursive instability: the Identity recurrence leaves the bounded corridor.

The Level-30 export channel is also explicit. If an individual historical
coordinate becomes obsolete or non-integrable, that historical residual is
exported rather than forcing the present self to remain identical to it.
This implements the source requirement that identity uses **selective
continuity**.

Run:

```bash
python -m bfg_studio identity \
  --generations 120 \
  --seed 1341550191 \
  --alpha 0.965 \
  --epsilon 0.0015 \
  --max-distance 0.14 \
  --export-threshold 0.16 \
  --min-index-similarity 0.80
```

In the included reference run:

- all `121/121` lower Perspective/BFG reclosures pass,
- after initialization, `142/142` Identity Closure steps pass,
- mean historical/present distance is about `0.08083`,
- mean Identity trajectory step is about `0.00328`,
- raw Perspective step is about `0.00349`,
- temporal mediation therefore reduces trajectory change by about `0.000216`
  per step on average,
- mean persistent self-index similarity is about `0.92309`,
- minimum self-index similarity remains about `0.83945`,
- mean transverse adaptation remains nonzero at about `0.05295`,
- one obsolete historical continuity component is explicitly exported,
- recursive Identity radius is `0.965`,
- there are no fragmentation, rigidity, recursion, or norm failures.

The ablated control consumes the exact same Perspective trajectory but replaces
historical identity with the current standpoint every step. It cannot claim
Identity Closure and has lower mean self-index similarity (`~0.88993`).

Identity remains distinct from narrative identity. Level 30 stabilizes
continuity of the self across change; it does not yet construct biography,
future-oriented personal narrative, or autobiographical meaning.

## Theory feature freeze

The theory-facing feature stack is now frozen through **Identity Closure**.

The frozen chain is:

`Canonical BFG Reclosure -> Self-Organization -> Population -> Evolution ->
Environmental Adaptation -> Learning -> Memory -> Self-Model -> Perspective ->
Identity`.

This freeze means new engineering work should improve validation, robustness,
benchmarking, carrier interfaces, reproducibility, persistence, performance,
and real-domain testing before adding further named closure levels.

Higher labels such as Consciousness Closure, Phenomenal Unity, Selfhood, and
Narrative Identity remain outside the frozen implemented stack. The source
corpus treats those as additional downstream realization hypotheses; they are
not silently inferred from successful Identity Closure.


## Validation and hardening

After the theory feature freeze at Identity Closure, development shifts to
validation and engineering quality rather than adding new named closure levels.

The master build now contains a fixed cross-layer benchmark suite:

```bash
python -m bfg_studio benchmark
```

The suite covers nine frozen targets:

1. canonical reclosure / novelty vs commuting inheritance,
2. self-organization,
3. population fission,
4. inheritance / mutation,
5. environmental selection,
6. learning / witness memory,
7. self-model closure,
8. perspective multiplicity–unity closure,
9. identity continuity through change.

The randomized robustness suite is separate:

```bash
python -m bfg_studio robustness \
  --trials 200 \
  --commuting 40 \
  --noncommuting 40 \
  --workers 4
```

It checks:
- exact neutral partition numerically across randomized PSD loads,
- positivity and graph-metric conditions,
- reciprocal endogenous balance,
- polar support identities,
- commuting no-novelty controls,
- noncommuting formation/novelty behavior,
- classification stability under a 100× numerical-tolerance span,
- self-organization survival under ±5% carrier perturbations,
- rejection of invalid negative neutral geometry.

Numerical tolerances remain implementation precision. They are not added as
free BFG generator parameters.

The combined audit is:

```bash
python -m bfg_studio hardening \
  --trials 200 \
  --workers 4
```

The current included hardening run passes:
- all 9/9 reference benchmarks,
- 200/200 randomized algebraic property trials,
- 40/40 commuting inheritance controls,
- noncommuting reclosure success fraction `0.825`,
- novelty fraction `1.0` among those successful noncommuting trials,
- stable classification across the tolerance sweep,
- `1.0` survival fraction across the declared ±5% carrier perturbation grid,
- hash-verified checkpoint save -> load -> resume.

The noncommuting success fraction is intentionally not forced to `1.0`:
random seeds that do not satisfy formation admissibility are allowed to fail
rather than having the gate weakened.

## Persistent experiment state and provenance

The master build now fingerprints its Python source tree and writes provenance
manifests containing:

- source SHA-256 fingerprint,
- experiment type,
- declared seed,
- parameters,
- Python / NumPy / SciPy environment,
- theory-freeze boundary.

A finite-dimensional BFG state can be saved, hash-verified, loaded, and
continued without pickle:

```bash
python -m bfg_studio checkpoint \
  --seed 17 \
  --pre-steps 2 \
  --post-steps 2
```

Higher-level experiments write immutable audit ledgers containing summaries,
events, frames, and source fingerprints. The core `BFGState` checkpoint is
currently the exact mid-run resumable primitive.

## Parallel experiment sweeps

Repeated seed studies can run concurrently:

```bash
python -m bfg_studio sweep \
  --mode evolution \
  --runs 20 \
  --horizon 20 \
  --workers 4
```

Supported batch modes are `alife`, `population`, and `evolution`. Each sweep
writes a provenance ledger so parallel exploration remains auditable.

## Carrier SDK

Real-domain carriers now use a stable `ValidatedCarrierAdapter` contract.

Every carrier must declare one fixed measurement mapping for:

- `D`,
- `K`,
- positive-semidefinite `Y`,
- `R_C`.

The declaration receives a SHA-256 mapping fingerprint. The SDK checks shape
consistency, finiteness, Hermiticity, positivity of `Y`, and nonzero state.

`no_retuning_comparison(...)` verifies that the mapping fingerprint remains
unchanged for the entire comparison dataset.

See:

- `CARRIER_SDK_SCHEMA.json`
- `examples/external_carrier_template.py`
- `REAL_DOMAIN_VALIDATION_PROTOCOL.md`

## First real-domain benchmark boundary

No empirical dataset is bundled and labeled as a validated BFG carrier yet.

This is deliberate. The first real-domain benchmark must freeze, before
held-out evaluation:

- domain and prospective target statement,
- measurement-to-BFG carrier mapping,
- calibration indices,
- held-out indices,
- matched null model,
- primary metric,
- success criterion.

The software implements this as `HeldoutValidationPlan` plus
`run_heldout_carrier_validation(...)`.

A successful held-out benchmark supports only its declared domain statement;
it does not automatically establish universal empirical realization.



## Annual sunspots — refreshed readiness-first carrier

The active annual-sunspot carrier now follows the same readiness-first empirical
policy as the Mauna Loa CO2 carrier.

The active development record is the complete bundled annual series
1700–2008.

The new prospective held-out target is:

`2009–2025`

and its target metrics are not bundled or evaluated by the refresh.

The active carrier uses 12-year causal delay windows with graph-aligned `K`, `Y`,
and `R_C`. It compares equal-complexity adaptive correction families:

- BFG feature selected from six frozen closure/neutral quantities;
- matched-null feature selected from six frozen ordinary window statistics.

The same readiness gate used for CO2 is applied:

- at least 2/3 rolling temporal fold wins,
- positive mean RMSE improvement,
- worst fold no worse than -2%,
- at least 95% canonical reclosure success.

Current development-only preflight:

- status: `READY_FOR_VALIDATION`
- fold wins: `3/3`
- Fold 1 improvement: about `+4.773%`
- Fold 2 improvement: about `+1.567%`
- Fold 3 improvement: about `+0.469%`
- mean fold improvement: about `+2.270%`
- worst fold: about `+0.469%`
- minimum fold reclosure success: `100%`
- full-development BFG RMSE: `14.786536`
- full-development matched-null RMSE: `14.821988`
- full-development relative improvement: about `+0.239%`
- full-development canonical reclosure: `100%`
- novelty among successful development reclosures: `100%`

Prepare / refresh:

```bash
python -m bfg_studio sunspot-prepare \
  --lag 12 \
  --out outputs/real_sunspots
```

Future confirmation is deliberately separate and requires both an external
2009–2025 annual data file and a one-time portfolio permit:

```bash
python -m bfg_studio sunspot-validate \
  --prepared outputs/real_sunspots \
  --data <future-annual-sunspot.csv> \
  --permit validation/permits/annual-sunspots.json
```

No future Sunspot confirmation permit is generated automatically.

See:

- `outputs/real_sunspots/SUNSPOT_PREFLIGHT_RESULT.md`
- `outputs/real_sunspots/sunspot_preflight.json`
- `outputs/real_sunspots/sunspot_validation_plan.json`

## Validation readiness gate

External carriers now use a two-stage reporting flow:

`exploration -> readiness preflight -> frozen held-out validation`

Exploratory variants may be iterated on calibration data without creating a
separate headline failure entry for every discarded design. Confirmatory
held-out results remain immutable once opened.

See `VALIDATION_REPORTING_POLICY.md`.

## Mauna Loa CO2 carrier — sealed preflight

The second external carrier uses the bundled weekly Mauna Loa atmospheric CO2
measurements and converts calibration data to monthly means.

Calibration ends at `1990-12-31`.

The held-out block begins at `1991-01-01` and remains **unevaluated**.

The carrier uses 24-month causal delay windows and graph-aligned `K`, `Y`, and
`R_C`. Forecasting compares two equal-coefficient adaptive correction families:

- BFG: the feature is selected from six frozen BFG closure/neutral quantities.
- matched null: the feature is selected from six frozen ordinary window
  statistics.

Three expanding-window calibration folds are used as a readiness gate.

Current result:

- status: `READY_FOR_VALIDATION`
- temporal fold wins: `2/3`
- mean relative RMSE improvement: about `+0.591%`
- worst fold relative difference: about `-1.408%`
- minimum fold reclosure fraction: `100%`
- full-calibration BFG RMSE: `0.406321`
- full-calibration matched-null RMSE: `0.406874`
- full-calibration relative improvement: about `+0.136%`

A readiness token was created because the frozen preflight rule passed.

**No 1991–2001 held-out target metric has been evaluated.**

Commands:

```bash
python -m bfg_studio co2-prepare \
  --calibration-end 1990-12-31 \
  --heldout-start 1991-01-01 \
  --out outputs/real_co2
```

The separate confirmatory command exists but should be considered an explicit
unsealing operation:

```bash
python -m bfg_studio co2-validate \
  --prepared outputs/real_co2
```

Once that command is run, its frozen result must be retained.


## Validation Portfolio Manager

All empirical carriers are now governed by one central portfolio instead of
being managed as unrelated scripts.

Canonical statuses are:

`EXPLORATORY`
→ `NOT_YET_VALIDATED`
→ `READY_FOR_VALIDATION`
→ `CONFIRMED | REJECTED`

`CONFIRMED` and `REJECTED` are terminal for a frozen mapping / plan. A terminal
result cannot transition back to readiness or exploration.

The current portfolio contains:

- `annual-sunspots` — `READY_FOR_VALIDATION`, prospective 2009–2025 metrics sealed;
- `mauna-loa-co2` — `READY_FOR_VALIDATION`, held-out metrics still sealed.

Audit the portfolio without touching held-out target data:

```bash
python -m bfg_studio portfolio
```

The report is written to:

- `validation/portfolio_status.json`
- `validation/PORTFOLIO_STATUS.md`

## Blind-heldout guard

A readiness token alone can no longer open a confirmatory dataset.

A READY carrier must first be cryptographically sealed:

```bash
python -m bfg_studio portfolio-seal --id mauna-loa-co2
```

The seal binds:

- carrier id and READY status,
- mapping fingerprint,
- validation-plan fingerprint,
- readiness-token hash,
- frozen-model hash,
- validation-plan file hash,
- current BFG source-tree fingerprint.

If any of those change, the seal audit fails.

Opening held-out data requires a separate explicit one-time permit:

```bash
python -m bfg_studio portfolio-permit \
  --id mauna-loa-co2 \
  --ack "CONFIRM HELDOUT OPENING"
```

Merely creating the permit still does not evaluate held-out targets. The permit
is consumed only when the confirmatory evaluation begins.

The CO2 confirmatory command now requires that permit explicitly:

```bash
python -m bfg_studio co2-validate \
  --prepared outputs/real_co2 \
  --permit validation/permits/mauna-loa-co2.json
```

The permit is single-use. Once consumed, the confirmatory block is considered
opened and its result must be retained.

In the current master **no CO2 confirmation permit has been issued**.


## ENSO / Pacific SST carrier

The master build now contains a third independent external carrier based on
NOAA Pacific Ocean monthly average sea-surface temperature from 1950–2010.

The carrier works on **monthly SST anomaly** rather than raw temperature.
Month-of-year climatology is estimated from the current development interval
only, preventing future seasonal information from leaking backward during
rolling preflight.

The forecast geometry is:

`climatological zero anomaly <-> previous-month anomaly persistence`

with one BFG internal feature controlling the adaptive mixture. The matched
null receives the exact same two-coefficient mixture family but may select
only one ordinary anomaly-window statistic.

Development-only preflight:

- Fold 1: `+3.210%`
- Fold 2: `+0.101%`
- Fold 3: `-0.471%`
- wins: `2/3`
- mean relative improvement: `+0.947%`
- worst fold: `-0.471%`
- minimum fold reclosure: `100%`

Full 1950–2010 development fit:

- selected BFG feature: `formation_rayleigh`
- selected matched-null feature: `recent_level`
- BFG anomaly RMSE: `0.430348 °C`
- matched-null anomaly RMSE: `0.430848 °C`
- relative improvement: `+0.116%`
- canonical reclosure: `100%`
- novelty among successful reclosures: `100%`

Therefore the active carrier status is:

`READY_FOR_VALIDATION`

The prospective held-out period is monthly `2011-01` through `2025-12`.
Those targets are not bundled and are not evaluated by preparation.

```bash
python -m bfg_studio enso-prepare \
  --lag 24 \
  --out outputs/real_enso
```

Future confirmation, if intentionally opened later:

```bash
python -m bfg_studio enso-validate \
  --prepared outputs/real_enso \
  --data <future-enso-monthly.csv> \
  --permit validation/permits/enso-pacific-sst.json
```

## First cross-domain BFG invariant analysis

With Sunspots, CO2 and ENSO simultaneously `READY_FOR_VALIDATION`, the master
build now compares their **development/calibration states only** on common
BFG internal coordinates.

```bash
python -m bfg_studio cross-domain \
  --out outputs/cross_domain
```

Current sample counts:

- Annual Sunspots: `297`
- Mauna Loa CO2 calibration: `370`
- ENSO Pacific SST: `708`

All `1,375 / 1,375` development/calibration states pass canonical reclosure,
and spectral novelty is present on every successful reclosure in this
comparison.

Shared q10–q90 carrier-coordinate corridors currently exist for:

- neutral retention:
  approximately `0.87178 – 0.92428`
- cross-fed gain:
  approximately `0.05396 – 0.09440`
- reciprocal `omega_keep`:
  approximately `0.00218 – 0.00857`
- recursive spectral radius:
  numerically `~1`

The q10–q90 `spectral_mismatch` intervals do **not** share a common
three-domain intersection. This is retained as an important domain-dependent
distinction rather than forced into a universal corridor.

These are exploratory shared **development-coordinate corridors**, not proof
of universal natural BFG invariants. No active held-out target is touched by
the cross-domain command.


## Finite-dimensional recursive stability theorem

The master now includes a theorem-level finite-dimensional recursive
stability layer in `BFG_RECURSIVE_STABILITY_THEOREM.md`.

The exact matrix theorem used is:

\[
R_C \text{ is power bounded}
\iff
\sigma(R_C)\subseteq\overline{\mathbb D}
\text{ and every }|\lambda|=1\text{ eigenvalue is semisimple}.
\]

This closes an important gap in the shorthand condition `rho(R_C) ≈ 1`:
spectral radius one alone is insufficient because a defective unit-circle
Jordan block grows polynomially.

For the canonical protected-witness split

\[
H=W\oplus E_s,
\]

with unit-modulus diagonalizable persistence on `W` and

\[
\rho(R_C|_{E_s})<1,
\]

power-bounded recursive persistence follows exactly. An adapted
positive-definite Lyapunov metric exists that is isometric on the persistent
sector and strictly contractive on the stable complement.

The theorem is finite-dimensional and conditional on its stated hypotheses.
It does not claim that every possible carrier automatically satisfies them,
and it does not establish the corresponding infinite-dimensional result.

Numerical theorem-hypothesis audit:

```bash
python -m bfg_studio stability-audit \
  --horizon 64 \
  --out outputs/stability
```

The audit includes explicit controls:

- semisimple unit-circle recursion: accepted,
- unit-circle Jordan block: rejected,
- supercritical eigenvalue: rejected.
- small outward perturbation from the unit circle: rejected,
- tangential unit-circle perturbation: accepted.

The mathematical proof is independent of the numerical audit.


## Integrated mathematical closure layer

The current master contains a single integrated mathematical closure layer.
Exact identities, conditional compatibility results and explicit finite runtime
laws are placed directly in their corresponding theorem, audit and runtime
components.

Integrated into the exact theorem/audit layer:

- exact real-rational nonnormal persistence certificates for a **supplied**
  invariant split and supplied Lyapunov/isometry metrics;
- finite Gram rebuilding from explicitly supplied `B_C`, `W_N`, `L_C`;
- exact retained-channel Gram-energy decomposition.

Integrated into the conditional/model layer:

- G1 load inheritance as a conditional compatibility result / additional
  postulate, not a universal core axiom;
- M3 connection closure as a complete finite upstream model under explicit
  extra connection assumptions.

Integrated as architecture guards:

- finite local derivative jets do not determine unrestricted field evolution
  without an additional evolution law;
- an isometry into a Hilbert space does not by itself guarantee admissibility
  of an unbounded Gram-form restriction.

Run:

```bash
python -m bfg_studio math-audit \
  --out outputs/math_audit
```

See `INTEGRATED_CLOSURE_ARCHITECTURE.md` and
`MATHEMATICAL_CLOSURE_LEDGER.md`.

The 23-September finite-closure theorem is now adopted as the **binding
finite master runtime profile**. Within that declared reduced category, next-state
reconstruction and finite iteration are no longer open runtime obligations.

The implementation uses an explicit intrinsic-Gram successor law, square-root
factor gauge and unitary successor transport. These are architecture laws of the
master runtime, not parameters inferred after the fact from validation targets.


## Finite master closure profile

The master runtime now closes the reduced finite state

\[
S=(\rho,K,Y,R)
\]

with \(\rho\) nonzero positive rank one, \(K=K^\dagger\),
\(Y>0\), and power-bounded \(R\).

The adopted successor laws are:

\[
C=(I+Y)^{-1},\qquad B=Y(I+Y)^{-1},
\]

\[
\alpha=\frac{\ell_u}{\ell_k+\ell_u},\qquad
\beta=\frac{\ell_k}{\ell_k+\ell_u},
\]

\[
A=
\begin{bmatrix}
\sqrt{\alpha}\,PC\\
\sqrt{\beta}\,PB
\end{bmatrix},
\]

followed on the active support by

\[
K_+=J^\dagger(K\oplus K)J,
\qquad
Y_+=A^\dagger A,
\]

\[
\rho_+=(-\lambda_0)\Pi_0,
\qquad
R_+=e^{i\tau K_+}.
\]

The simple-negative-mode gate sends failures to absorbing \(\bot\).

Because \(K_+\) is Hermitian, \(R_+\) is unitary. Therefore every
nonterminal successor is power bounded by construction.

The master also fixes the successor Gram-factor gauge:

\[
B_{C,+}=Y_+^{1/2},\qquad
W_{N,+}=I,\qquad
L_{C,+}=I.
\]

Consequently, for the declared finite runtime category the update is
single-valued, total after adjoining \(\bot\), and exactly iterable for every
finite number of steps.

A restricted bounded infinite-dimensional input class with isolated finite
peripheral Riesz range reduces to this finite profile after one admissible
step.

Code: `bfg_studio/finite_closure.py`.


### Runtime dispatch

The reduced finite profile is now a first-class runtime path, not only a
side module.

`simulate(...)` dispatches as follows:

- no explicit carrier → reduced finite master runtime;
- explicit carrier → carrier-specific research/application lane.

The `demo` and `control` CLI commands use the finite master runtime by
default and retain `--runtime legacy` only as an explicit compatibility
option.

This removes the previous gap between adopting the finite profile in the
documentation and actually routing the principal generic runtime through it.


## Master Runtime Transfer Audit

The three active real-domain carriers are now connected to the same closed
finite master runtime.

The transfer path is:

\[
\text{measurement}
\to
BFGState
\to
\rho=\frac{|D\rangle\langle D|}{\langle D|D\rangle}
\to
ReducedClosureState
\to
\mathcal U_{\rm master}.
\]

No carrier-specific successor law is used after this adapter.

Run:

```bash
python -m bfg_studio transfer-audit \
  --horizon 4 \
  --out outputs/runtime_transfer
```

Current development/calibration-only result:

- states processed: `1,375 / 1,375`
- uncaught exceptions: `0`
- successful first master transfer: `1,375 / 1,375`
- maximum successor unitarity residual:
  approximately `7.03e-16`
- maximum successor Gram-rebuild residual: `0`

A short recursive diagnostic horizon is also retained. Under the current
floating-point admissibility policy, the real-domain trajectories typically
complete two to three successful master reclosures before entering absorbing
`bottom`. The dominant terminal mechanism is vanishing dual persistent load;
a smaller subset reaches the declared numerical positive-load floor.

This is recorded as runtime behavior rather than hidden by retuning
tolerances.

Shared q10-q90 first-step transformation corridors currently exist for:

- reciprocal update weight `alpha`:
  approximately `0.002180 – 0.008567`
- normalized formation gap:
  approximately `1.26485 – 1.30354`
- neutral-load density ratio:
  approximately `0.024566 – 0.057264`
- `K` RMS transport ratio:
  approximately `0.795695 – 0.811047`

The normalized formation-depth q10-q90 intervals do not have a common
three-domain intersection. That difference is retained rather than
normalized away.

These are exploratory transformation coordinates. They do not open any
held-out target and do not constitute confirmatory evidence of a universal
natural law.


## Formation geometry, load contraction, and terminal surface

The master now contains a development/calibration-only analysis of the
observed 2–3 step recursive termination.

The analysis keeps the original formation-depth normalization and three
alternative dimensionless normalizations simultaneously. No candidate is
selected after seeing a held-out result.

The original quantity

\[
\frac{-\lambda_0(K_+)}{\|K\|_2}
\]

still has **no** common three-domain q10–q90 intersection.

Three other fixed normalizations do:

\[
\frac{-\lambda_0(K_+)}{\|K\|_{\rm RMS}}
\in
[1.327277,\;1.342006],
\]

\[
\frac{-\lambda_0(K_+)}{\gamma_{\rm formation}}
\in
[0.760588,\;0.790084],
\]

and

\[
\frac{-\lambda_0(K_+)}
     {\operatorname{tr}|K|/d}
\in
[1.365628,\;1.415870].
\]

All four candidates remain reported. The non-overlap of the original
spectral-norm coordinate is not erased.

### Recursive load contraction

Across successful master transitions, the pooled log-log load fit is
superlinear. More importantly, after the first carrier→master transition the
depth-specific exponents are

\[
p_2\approx1.9521,\qquad
p_3\approx1.9797.
\]

This is close to the exact scalar reduced-master recurrence

\[
y_+
=
\frac{2y^2}{(1+y)^2(1+y^2)}
\sim
2y^2
\qquad (y\to0^+).
\]

The present real-carrier trajectories therefore enter a near-quadratic
small-load contraction regime after the first master reclosure.

### Numerical versus structural termination

`atol` and `psd_tol` were jointly scaled by `0.1`, `1`, and `10`, while the
spectral/rank/gap tolerances were kept fixed.

Across all three scales:

- median successful recursive depth: `3`
- q10 successful depth: `2`
- q90 successful depth: `3`

The tighter `0.1×` floor allows a small tail to reach depth 4, while the
median remains unchanged.

Thus the correct interpretation is:

\[
\boxed{
\text{load contraction is structural, while the finite numerical }\bot
\text{ crossing depends on the admissibility floor.}
}
\]

At the default numerical policy, terminal causes are:

- dual persistent load below admissibility threshold: `1276`
- successor positive-load floor reached: `99`

This wording deliberately avoids calling the first event exact mathematical
vanishing.

Run:

```bash
python -m bfg_studio formation-analysis \
  --horizon 6 \
  --out outputs/formation_dynamics
```


## Current master quality gates

- `142/142` tests pass.
- hardening: `PASS`
- recursive stability audit: `PASS`
- integrated mathematical closure audit: `PASS`
- master runtime transfer audit: `PASS`
- formation-dynamics smoke gate: `PASS`
- relational-network audit: `PASS`
- formation-eligibility theorem audit: `PASS`
- formation-robustness theorem audit: `PASS`
- parent-formation-radius audit: `PASS`
- stratum-transition geometry audit: `PASS`
- portfolio audit: `PASS`
- source fingerprint: `9ed33c1e22e743dd88004ed147b447dfe7a0c832f25779196805b137726843b8`



## Fourth real carrier: relational interaction network

The master now includes a structurally different real carrier based on the
weighted Zachary karate-club interaction graph.

This is **not** another recurrence/time-series carrier. It is a fixed
observed weighted interaction network with 34 nodes and 78 edges.

The BFG mapping uses 34 node-centered heat-diffusion probes and does not use
the source dataset's later club/fission labels.

Current result:

- BFG state contract: `34/34`
- first simple-negative formation/master transfer: `13/34`
- formation-gate terminals: `21/34`
- successful recursive small-load certificates: `41/41`
- permutation-equivariance audit: `PASS`

The `13/34` result is intentionally retained. The formation drive was not
increased to force every node probe through the gate.

### Four-domain consequence

Once the relational carrier is added, none of the earlier q10-q90
transformation corridors shared by Sunspots, CO2 and ENSO remains shared
across all four domains.

The same is true for all four tested formation-depth normalizations.

Therefore the earlier overlaps are now interpreted as

\[
\boxed{\text{time-series-family shared corridors}}
\]

rather than universal cross-structure invariants.

In contrast, the multidimensional small-load theorem remains intact on the
relational carrier:

\[
\boxed{41/41}
\]

successful recursive network transitions satisfy its explicit bound.

This separates empirical carrier-family regularities from mathematical
master-runtime structure much more sharply.

The network carrier remains `EXPLORATORY`; it is not placed into the sealed
confirmatory portfolio until an independent prospective network target and
split are defined.

See `REAL_RELATIONAL_NETWORK_CARRIER.md`.


## Formation eligibility: exact active-spectrum criterion

The `13/34` relational formation split now has an exact mathematical
explanation.

With

\[
H=K\oplus K,
\qquad
A=U_r\Sigma_rV_r^\dagger,
\]

the active successor formation operator is

\[
K_+=U_r^\dagger H U_r.
\]

On the active right support define

\[
M=V_r^\dagger A^\dagger H A V_r,
\qquad
N=V_r^\dagger A^\dagger A V_r.
\]

Since

\[
M=\Sigma_rK_+\Sigma_r,
\qquad
N=\Sigma_r^2,
\]

the generalized eigenvalues of `(M,N)` are exactly the eigenvalues of
`K_+`.

Therefore formation is admissible exactly when the lowest generalized
eigenvalue is negative and simple under the already-declared formation-gate
tolerances.

The parent ground vector \(u_-\) also defines the transport witness

\[
\chi_-=
\frac{
\langle Au_-,(K\oplus K)Au_-\rangle
}{
\langle Au_-,Au_-\rangle
}.
\]

By the min-max principle,

\[
\chi_-<0
\Longrightarrow
\lambda_{\min}(K_+)<0.
\]

This witness is sufficient in general, not necessary in arbitrary states.

Current first-step audit:

- states: `1,409`
- direct/generalized spectral agreement:
  maximum residual `~3.55e-15`
- Sunspots criterion/runtime agreement: `297/297`
- CO2 criterion/runtime agreement: `370/370`
- ENSO criterion/runtime agreement: `708/708`
- relational network criterion/runtime agreement: `34/34`

For the relational carrier, all `34/34` parent operators already possess a
negative ground mode and all `34/34` satisfy the simplicity-gap condition.
The split is therefore entirely in the transported active sign:

- successful `13/34`: \(\chi_-<0\)
- terminal `21/34`: \(\chi_->0\)

Observed network witness ranges are separated around zero:

\[
-0.55412\le\chi_-\le-0.01602
\]

for formation success, versus

\[
0.01983\le\chi_-\le0.13599
\]

for formation terminal states.

Thus the relevant formation statement is now

\[
\boxed{
\text{negative parent mode}
\not\Rightarrow
\text{formation};
\quad
\text{negative active packet mode}
\Rightarrow
\text{formation eligibility}.
}
\]

See `BFG_FORMATION_ELIGIBILITY_THEOREM.md`.


## Formation robustness and bifurcation margin

Formation is now quantitative rather than only binary.

For the active operator \(K_+\), define

\[
s=-\varepsilon_{\rm sign}-\lambda_0,
\qquad
g=(\lambda_1-\lambda_0)-\varepsilon_{\rm simple}.
\]

If the state is formation-eligible, its exact Hermitian operator-norm
distance to loss of formation is

\[
\boxed{
d_+
=
\min\left(s,\frac{g}{2}\right).
}
\]

If the state is terminal, the infimum distance to the eligible set is

\[
\boxed{
d_-
=
\max\left(
(-s)_+,\frac{(-g)_+}{2}
\right).
}
\]

This follows directly from Weyl eigenvalue perturbation bounds, and the
bounds are attained by perturbations aligned with the lowest eigenspaces.

Current audit:

- active gate states: `1,409`
- sub-boundary adversarial perturbations preserving status: `1,409/1,409`
- just-beyond-boundary perturbations changing status: `1,409/1,409`

For the relational carrier:

- nearest successful state to the bifurcation surface:
  `+0.0166927689`
- nearest terminal state:
  `-0.0183398303`
- 31/34 probes are sign-surface limited
- 3/34 are simplicity-surface limited

The three time-series carriers are much farther from the current active
formation boundary, with median margins around `0.76–0.81`.

The exact radius is currently a theorem in the active \(K_+\) operator norm.
It is not yet promoted to an identical radius in a norm of the parent
variables \((K,Y,R,\rho)\), because parent perturbations can rotate the
active packet subspace.

See `BFG_FORMATION_ROBUSTNESS_THEOREM.md`.


## Parent-state formation radius

The active formation margin is now transported backward to the parent state

\[
S=(\rho,K,Y,R).
\]

The correct result is **stratified**, not an unrestricted ambient-ball
theorem. Exact unit-circle persistence and exact packet rank are not open
properties: arbitrarily small ambient perturbations can change either one.

The declared parent product norm is

\[
\|\Delta S\|_\oplus
=
\max\{
\|\Delta K\|_2,\,
\|\Delta Y\|_2,\,
\|\Delta R\|_2,\,
\|\Delta\rho\|_1
\}.
\]

Inside a fixed persistent-rank / fixed-active-rank admissible stratum, the
master now propagates perturbation bounds through

\[
\Delta R
\to
\Delta P
\to
\Delta(C,B)
\to
\Delta(\lambda_{\rm keep},\lambda_{\rm up})
\to
\Delta A
\to
\Delta U_r
\to
\Delta K_+.
\]

The key sufficient endpoint is

\[
\|\Delta K_+\|_2
\le
E_F(\delta)
<
|\mathfrak m_F(K_+)|.
\]

Whenever this holds, formation status is preserved.

Current audit:

- positive conditional parent-radius certificates: `1409/1409`
- structured admissible regression controls: `43/43`
- all 43 controls preserve active rank and formation status
- all 43 observed active spectral shifts remain below the theorem bound

Median certified radii:

- Sunspots: `3.7351e-6`
- CO2: `2.4781e-6`
- ENSO: `2.0443e-6`
- relational network: `1.4095e-7`

The smaller network radius is consistent with its much closer formation
bifurcation geometry, but the parent bound is conservative and is not
claimed to be the exact parent-state distance.

See `BFG_PARENT_FORMATION_ROBUSTNESS_THEOREM.md`.


## Stratum-transition geometry

The master now records four formation-transition families in one explicit
bifurcation ledger:

\[
\boxed{
\text{sign},
\quad
\text{simplicity},
\quad
\text{persistent runtime rank},
\quad
\text{active runtime rank}.
}
\]

Exact algebraic rank and exact unit-circle persistence remain non-open under
arbitrary ambient perturbations. The positive rank-transition margins below
are therefore **finite-runtime operational margins** induced by the declared
numerical policy.

For normal-contraction \(R\),

\[
\tau_P=1-\texttt{peripheral\_tol}
\]

defines the persistent runtime surface. Singular-value stability gives a
certified operator radius preserving the persistent runtime count.

For the packet \(A\),

\[
\tau_A
=
\max(
\texttt{rank\_tol},
\texttt{rtol}\,\sigma_1(A)
)
\]

defines the active runtime surface. The sufficient packet radius is

\[
\boxed{
r_A
=
\frac{
\min(
\sigma_r-\tau_A,\,
\tau_A-\sigma_{r+1}
)
}{
1+\texttt{rtol}
}.
}
\]

Full native audit:

- `1,409/1,409` states have persistent runtime rank 4;
- `1,409/1,409` states have active runtime rank 4;
- nearest persistent transition is loss of persistence on `1,409/1,409`;
- nearest active transition is latent-mode activation on `1,409/1,409`.

The native active-rank margin is around \(10^{-10}\), much closer than the
formation and persistent surfaces in their own coordinates.

After transport into the common parent norm, all `1,409/1,409` states also
receive a positive **full runtime-stratum radius**. In all current real
carriers the limiting parent-level runtime surface is the active-rank
surface.

This stricter radius is much smaller than the conditional formation radius
because it additionally protects the runtime rank decision itself. It is a
numerical continuity scale, not a physical constant.

See `BFG_STRATUM_TRANSITION_GEOMETRY_THEOREM.md`.
