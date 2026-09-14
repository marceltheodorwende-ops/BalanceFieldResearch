# Paired synthetic comparison, 14 September 2026

## Protocol

Run `python -m bfg_lab.comparison` to reproduce `results/comparison.json` with
all candidate histories, input hashes and NumPy version. This is an exploratory
toy benchmark, not a preregistered or held-out physical prediction test.

24 paired cases: two load geometries (diagonal and mixed), capacity scale
0.75 or 1, retention 0.8 or 1, and perturbation -1e-6, 0 or +1e-6. Each case
runs all three rules from the exact same initial state for up to 12 transitions.
Perturbation simultaneously scales D and changes the first state component;
it is one perturbation direction, not an exhaustive robustness test.

Shared normalization, Gram closure, capacity transport and formation gate are
held fixed. The 72 runs are deterministic, not 72 independent random samples.
No error runs are silently dropped. The 12-step horizon censors survival time.

## Reference transport

The baseline `carried` retains the old transport on the retained carrier:
`Q = J* U`, `R_next = Q* R Q`, where U spans the new polar range.
Q has orthonormal columns. This is unchanged dynamics restricted and expressed
in new coordinates, not literal reuse of matrix entries across different spaces.
Compression can itself change the spectrum when a subspace is discarded.
The baseline requires Hermitian R: compression of a general normal operator
need not remain normal. Hermitian contractions stay Hermitian contractions.
It uses no newly chosen persistence projector; rho is unused by this baseline.

## Results

| Rule | Cases | Gate stopped | Reached 12 transitions |
| --- | ---: | ---: | ---: |
| Packet projector (M1) | 24 | 18 | 6 |
| Negative spectral projector (M2) | 24 | 12 | 12 |
| Carried transport | 24 | 12 | 12 |

No tested perturbation changes a stopping index. M2 does not outperform the
reference on budget-reaching count. Longer survival is not defined as better
physics or a predictive accuracy score here.

At zero perturbation with retention 0.8:

| Geometry / capacity scale | M1 transitions | M2 transitions | Carried transitions |
| --- | ---: | ---: | ---: |
| Diagonal / 0.75 | 2 | 2 | 2 |
| Diagonal / 1 | 3 | 4 | 4 |
| Mixed / 0.75 | 1 | 1 | 2 |
| Mixed / 1 | 1 | 2 | 4 |

For maintained capacities the mixed example keeps three directions with M2,
two with carried transport, while M1 stops after one transition. Preserving
more modes is partly an imposed consequence of M2's projector, not evidence
that its dynamics are more realistic. The full reason codes remain in the JSON.

## Source and assumption audit

Rechecked Structural Strong Form V2 sections 23-24 in the supplied text:
microscopic capacities and the master spectrum are not fully derived there;
construction of D_cov c, W_N and L_C is assigned to the research program.
This agrees with the [five-document source audit](SOURCE_AUDIT.md).

| Component | Evidence or status |
| --- | --- |
| Neutral split, metric projection, reciprocal weights, polar transport | Implemented paper building blocks; restricted numerical domain |
| Peripheral persistence definition | Proposed correction; see PERSISTENCE_PROPOSAL.md |
| Unit Euclidean packet normalization | Extra modeling choice; discards amplitude |
| Capacity retention factor | Imposed depletion, not derived dissipation |
| Y=(C+N)/(1+norm(D)) | Extra Gram closure; not the upstream construction |
| Packet / negative-spectrum / carried R | Three explicit alternative modeling choices |

This is not a renewed proof audit of every claim in all five papers. No new
physical prediction or superiority claim is supported by these runs. The next
scientific obligation is an independently justified transport and observable
mapping, followed by a frozen predictive test against data or a known system.
