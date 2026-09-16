# Exact pair protocol

Engineering plan fixed before this extension's test run. Apply the three owner
audit documents anchored by SHA-256 in ../../docs/BOUNDARY_PROTOCOL.md: separate claims,
preserve negatives, fixed inputs, one purpose per artifact, explicit limitations.
This is known-case engineering, not independent scientific preregistration.

Scope: an additional fallback only for two nodes, exactly known initial state,
zero sensor error, both sensors and exactly two observation times (zero and t>0).
Keep existing APIs and historical results unchanged. No tolerance inflation.

Endpoint: resolve the two remaining catalogue cases with analytic certificates.
Controls: reversed sensor order, out-of-box logarithmic weight, inconsistent
mass, partial sensors/noisy inputs, exhausted log bounds and multiple times.
Failure: wrong exclusion, witness outside the box, rounded log presented as
exact, or a result outside the declared analytic scope.

Use exact rational lower/upper bounds on -log(r)/(2t), from the integrated
geometric series. Default 64 terms, cap 256. Return an explicit symbolic witness
only if its entire weight enclosure is inside the original box. Otherwise retain
unresolved unless positivity or a disjoint weight enclosure proves exclusion.
Replay the original 39-case catalogue; distinguish software tests from research
case outcomes. No empirical BFG or cross-domain conclusion is admissible.
