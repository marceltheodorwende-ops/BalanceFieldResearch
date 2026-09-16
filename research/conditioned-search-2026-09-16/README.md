# Conditioned search — 2026-09-16

[Diagnosis data](diagnosis.json) · [Protocol](protocol.md) · [Results](results.json)
· [Method](method.md) · [BFG audit](audit.md)

| Same 20 network cases | Previous interior solver | Cutoff 1e-8 |
| --- | ---: | ---: |
| Compatible witness | 8 | 12 |
| Entire family excluded | 8 | 8 |
| Unresolved | 4 | 0 |

All four formerly unresolved complete4 histories now have exact rational
witness certificates, including single-sensor cases. The prior 39-case
catalogue retains every status. This resolves these two known catalogues;
it is not a complete solver or a general performance guarantee.

## Diagnosis

At the midpoint, complete4 finite-difference Jacobians contain relative
singular values around 1e-10, alongside values near 1 and 0.5. The old default
least-squares cutoff retains these tiny numerical directions. Corresponding
unprojected steps range from roughly 45 million to 250 million in coordinates
bounded to [0,1]. Projection then clips the step heavily. Path3 has no comparable
spectral gap: its smallest relative value is at least 0.061 in this catalogue.

There is an analytic reason for insensitive directions: with equal hub edges
and an impulse at the hub, the other three nodes have equal states. Changing
edges between those equal-state nodes does not affect their heat flux. Treating
finite-difference residue in these directions as reliable sensitivity is harmful.
This is a local mechanism; no global identifiability theorem is asserted.

## Reproduce

```sh
python -m bfg_lab.conditioning_diagnosis
python -m bfg_lab.conditioned_evaluation
python -m bfg_lab.certified_interior --input research/conditioned-search-2026-09-16/example.json
```

The new option is `fit_rcond=1e-8`. Default `None` retains the old search behavior.
103 publication tests pass, including five new regression tests covering all
four complete4 cases, old-default reproduction, invalid cutoffs and refusal to
accept a small residual without a sufficient exact certificate, and the JSON CLI.
The first CLI check exposed a configuration parsing issue: the exact-decimal
JSON reader turned the numerical cutoff into a string. The CLI now converts
only this solver option to float; measurement strings stay exact.

Both sides use the same 256-call numerical budget, 31 boxes, depth 12, 27
boundary candidates and 64 certification terms. Measurement errors and physical
bounds are unchanged. The two catalogues' hashes and protocol hash are recorded.
Old stages retain the negative findings that motivated this correction.

Next validation should use newly designed, nonuniform and less symmetric graphs
with the option fixed in advance. The cutoff is not established as universally
appropriate, and successful fitting does not identify the unique true graph.
