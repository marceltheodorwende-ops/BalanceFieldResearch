# BFG spacetime and conservation investigation

This is the BFG-only research packet authorized by Marcel Theodor Wende on 23 October 2026. Start with the [binding German mandate](MANDATE.de.md) and [checked status](STATUS.md).

**Result:** finite conservation identities and counterexamples are established in stated sectors. A standard Hermitian-two-mode determinant construction supplies an algebraic Lorentz carrier, but physical dimensional selection, transport, clock, stress, action and Einstein dynamics remain OPEN.

## Contents
- [MANDATE.de.md](MANDATE.de.md): binding scope, source hierarchy and completion rules; committed first.
- [PROTOCOL.md](PROTOCOL.md): predeclared candidates, bounds and transparent amendments.
- [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json): pinned manuscript and original kernel.
- [DERIVATION.md](DERIVATION.md): proofs, exact witnesses and their limits.
- [STATUS.md](STATUS.md): German claim/evidence ledger and next dependency.
- [audit.py](audit.py), [test_audit.py](test_audit.py), [results.json](results.json): executable finite controls.
- [REVIEW.md](REVIEW.md): verification scope and retained failures.

## Two-mode/environment continuation

[Exact pair-selection limits and environment-assisted factor](PAIR_DERIVATION.md), with [preregistered checks](PAIR_PROTOCOL.md) and [new source controls](pair_results.json). A pure pair and pair-plus-alpha fail autonomous closure; a complementary formation-weighted spectral measure supplies a sufficient closed factor on the full-persistence history domain. No physical clock/current or Einstein completion is claimed.

Run the additional controls with:
    python research/spacetime-conservation/pair_audit.py

## Stable current-state pair selection

[Invariant spectral class and derivative correction](STABLE_PAIR_DERIVATION.md), [protocol](STABLE_PAIR_PROTOCOL.md), [fresh results](stable_pair_results.json). On the stated full-persistence class, the two-smallest selector is retained and the environment-assisted factor needs no extra pair-history label. Complementary mass and first moment still do not close it. Physical selection/clock/current remain open.

Additional controls:
    python research/spacetime-conservation/stable_pair_audit.py

## Component balance and compensation limits

[Exact component balance and scoped compensation theorem](COMPONENT_EXCHANGE_DERIVATION.md), [protocol](COMPONENT_EXCHANGE_PROTOCOL.md), [fresh controls](component_exchange_results.json). Independent complementary source data and the branch marginal do not compensate fixed transverse pair charges. Inverse-transported history observables give formal conserved coordinates, without selecting a physical current.

Additional controls:
    python research/spacetime-conservation/component_exchange_audit.py

## Reproduce
Use Python 3.12 and the adjacent requirements.txt. From the repository root:
    python -m pip install -r research/spacetime-conservation/requirements.txt
    python research/spacetime-conservation/audit.py
    cd research/spacetime-conservation
    python -m unittest -v test_audit

The audit imports the unchanged source update, checks its exact Git blob, and never calls the empirical data evaluator. It writes only this packet's results.json. On Windows, use a checkout retaining the source's LF bytes (for example git -c core.autocrlf=false clone ...); a byte mismatch intentionally stops rather than silently changing the pin. Upstream source changes require an explicit new source review.

The six-event trajectory reaches a recorded numerical rank cutoff at event six; only five completed events are claimed. Other bounded controls pass. Numerical controls do not replace the proofs and do not establish physical emergence.

This research branch starts from the active manuscript branch, not the older main. Original manuscripts, kernel, licenses and empirical artifacts remain unchanged.


## State-clock constructions and ambiguity

[Positive durations, scalar unit-tick coordinate and limits](CLOCK_DERIVATION.md), [protocol](CLOCK_PROTOCOL.md), [fresh results](clock_results.json). The same source trajectories admit both summable and nonsummable positive mathematical durations. An exact scalar Abel coordinate exists, with explicit optional asymptotic normalization; physical calibration and spatial flow remain open.

Additional controls:
    python research/spacetime-conservation/clock_audit.py

## Relational frame and quotient coordinates

[Formation/Witness reference frames and closed invariant coordinates](RELATIONAL_FRAME_DERIVATION.md), [protocol](RELATIONAL_FRAME_PROTOCOL.md), [fresh results](relational_frame_results.json). Nonzero pair reference coherence supplies a persistent covariant Pauli frame; its kernel coordinates are gauge invariant. The alternative Witness chart, overlap rotation and symmetric-state obstruction are explicit. Internal frame transport is not yet spatial propagation.

Additional controls:
    python research/spacetime-conservation/relational_frame_audit.py

## Eventual stable-class entry and collision limits

[Global positive-persistence envelope and finite C-entry theorem](EVENTUAL_CLASS_DERIVATION.md), [protocol](EVENTUAL_CLASS_PROTOCOL.md), [fresh results](eventual_class_results.json). Every autonomous full-persistence state with F>0 and 0<Y<I eventually reaches C. Initially simple eigenvalues can nevertheless collide across the two-mode selection boundary. A trace-increase counterexample limits the trace-log clock to its original domain.

Additional controls:
    python research/spacetime-conservation/eventual_class_audit.py

## Retained-data tie resolution and equal-load charges

[Partial Y/F/W selector, closed factor and equal-load four-charge sector](LEX_SELECTOR_DERIVATION.md), [protocol](LEX_SELECTOR_PROTOCOL.md), [fresh results](lex_selector_results.json). Formation/Witness can resolve degenerate Y blocks and retain the chosen pair on C. Unresolved symmetry and discontinuity are explicit. Equal selected Y loads give four constant relational kernel coordinates in a reference-supported example; no physical spatial four-current is claimed.

Additional controls:
    python research/spacetime-conservation/lex_selector_audit.py

## Internal graph and source-channel continuity

[Mode graphs, failed phase-current candidates and exact channel current](MODE_GRAPH_DERIVATION.md), [protocol](MODE_GRAPH_PROTOCOL.md), [fresh results](mode_graph_results.json). Retained Y-mode stocks do not flow, though coherence magnitudes attenuate. The actual source channel yields an antisymmetric current with exact internal continuity on noncommuting formation nodes, including a nonzero exact witness. Spatial interpretation, reduced closure and physical energy-momentum remain open.

Additional controls:
    python research/spacetime-conservation/mode_graph_audit.py

## Population closure and coherence memory

[Formation-node populations, conditional classical sector and exact memory](POPULATION_CLOSURE_DERIVATION.md), [protocol](POPULATION_CLOSURE_PROTOCOL.md), [fresh results](population_closure_results.json). Generic populations/channel magnitudes do not close; source-generated coherences contribute. An unbiased two-mode sector has a closed population/load factor and nonzero flux. General finite-horizon coherence memory is explicit. Physical locality is still open.

Additional controls:
    python research/spacetime-conservation/population_closure_audit.py

## Channel range and controlled tails

[Internal-path two-hop transfer, norm tail bounds and disconnected blocks](CHANNEL_RANGE_DERIVATION.md), [protocol](CHANNEL_RANGE_PROTOCOL.md), [fresh results](channel_range_results.json). A nearest-neighbor Y matrix does not force a nearest-neighbor source channel. An exact witness has nonzero distance-two transfer; state-dependent finite-band approximation bounds are proved. This is not a physical Lorentz-causality test.

Additional controls:
    python research/spacetime-conservation/channel_range_audit.py

## Repeated adjacency evolution

[Persistent creation of an endpoint Y edge](ADJACENCY_EVOLUTION_DERIVATION.md), [protocol](ADJACENCY_EVOLUTION_PROTOCOL.md), [fresh results](adjacency_evolution_results.json). The declared three-node current-Y path becomes a triangle. A proof using the actual endogenous alpha schedule retains the new edge at every finite event, while spectral projectors stay fixed and weights shrink. Physical locality is not inferred from either support or fixed spectral algebra.

Additional controls:
    python research/spacetime-conservation/adjacency_evolution_audit.py


## Exact multi-event channel composition

[Fixed spectral-frame composition and effective population matrices](COMPOSITION_DERIVATION.md), [protocol](COMPOSITION_PROTOCOL.md), [fresh results](composition_results.json). A tensor-product Gram formula composes the actual channels without intermediate dephasing. Effective finite-horizon population matrices are symmetric and doubly stochastic, but generally differ from products of one-event population matrices. Physical space, clock and energy-momentum remain open.

Additional controls:
    python research/spacetime-conservation/composition_audit.py


## Controlled multi-event range in the initial graph

[Vector-Bernstein tail bound including coherent initial states](MULTIEVENT_RANGE_DERIVATION.md), [protocol](MULTIEVENT_RANGE_PROTOCOL.md), [fresh results](multievent_range_results.json). A polynomial approximation of the full Kraus vector controls total population beyond an initial-graph ball without changing the source. Bounds are conservative and depend on the actual geometry schedule; no physical speed or spatial calibration is inferred.

Additional controls:
    python research/spacetime-conservation/multievent_range_audit.py


## Frozen-channel continuous interpolation

[Exact entrywise-power obstruction and two positive alternatives](INTERPOLATION_DERIVATION.md), [protocol](INTERPOLATION_PROTOCOL.md), [fresh results](interpolation_results.json). A three-mode C-sector witness refutes positivity of the naive homogeneous fractional Schur-power path. Convex and angular Gram paths preserve positivity and endpoints but differ between events. Neither is selected as physical time or a continuous geometry equation.

Additional controls:
    python research/spacetime-conservation/interpolation_audit.py


## Weak splitting and joint scaling limit

[Exact random-unitary form, dissipative coefficient and finite geometry drift](WEAK_SPLITTING_DERIVATION.md), [protocol](WEAK_SPLITTING_PROTOCOL.md), [fresh results](weak_splitting_results.json). A nearly scalar load gives a double-commutator kernel coefficient and a frozen-channel comparison limit. The actual geometry retains a finite jump at fixed positive scalar load, obstructing that full-state Euler scaling. Frozen powers are not autonomous source trajectories.

Additional controls:
    python research/spacetime-conservation/weak_splitting_audit.py


## Joint small-load boundary chart

[Exact scale/shape equations and nontrivial boundary kernel channel](SMALL_LOAD_DERIVATION.md), [protocol](SMALL_LOAD_PROTOCOL.md), [fresh results](small_load_results.json). Formation-normalized relative load retains a closed boundary map as total load vanishes. A two-mode witness retains finite kernel change, while a scalar path to the same raw zero-load point has the identity channel. The relative chart is not a physical clock or a source call at zero load.

Additional controls:
    python research/spacetime-conservation/small_load_audit.py
