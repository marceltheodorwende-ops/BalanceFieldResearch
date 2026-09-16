# Prospective small-network check

Fixed before execution. New cases for an unchanged solver, designed by the same
developer; not independent validation. Audit sources: the three DOCX files and
hashes registered in ../../docs/BOUNDARY_PROTOCOL.md. Preserve all prior stages.

20 cases: path with 3 nodes and complete graph with 4 nodes; true uniform
weights 0.8 and 1.2; full sensors or node 0 only; impulse at node 0; intact or
node 0 isolated before t=0 (16 cases). Four constant-state controls use state
0.25 at every node, isolated node 0, both graphs and sensor sets. These are
intentionally observationally indistinguishable from intact constant states.

Every declared healthy edge independently ranges from 0.7 to 1.3; absent edges
are fixed zero. Times 0, 0.25, 1; exact calibration; sensor bound 1e-6. Add
deterministic alternating +/-1e-7 reading offsets by time and node. Independent
closed-form modal solutions generate observations with Decimal precision 80.
The large difference between rounding precision and sensor allowance is a
numerical safeguard, not a separate machine-checked rounding theorem.

Unchanged assess_exact_pair: 31 boxes, depth 12, 27 boundary candidates,
24 original terms, 64 candidate terms, 64 log terms. No tuning after results.
Baseline: assess_family with the same physical inputs and 24 terms.
Primary safety endpoint: zero healthy-family exclusions on intact cases and
constant controls. Secondary descriptive endpoints: witness/exclusion/unresolved
counts by graph, sensors and condition; search effort. No minimum fault-detection
rate is assumed. Unresolved outcomes are retained, never counted as detections.

Failure: any exclusion of these known compatible inputs, invalid candidate,
changed threshold/input during evaluation, or a claim that constant-state cut
controls must reveal topology. No solver repair is included in this stage.
