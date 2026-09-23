# BFG Emergence Studio — Master Build Policy

This project is maintained as one continuously updated master build.

- No public version branches are used.
- New functionality is merged into the existing master codebase.
- The distributable artifact keeps the stable name `BFG_Emergence_Studio.zip`.
- Older downloadable builds are superseded by the newly generated master archive.
- Internal package metadata may contain a technical version placeholder required by Python packaging, but it is not used as the public project identity.

The project identity is simply:

**BFG Emergence Studio**


## Theory feature freeze

The current theory-facing stack is frozen through **Identity Closure**.
Further master-build development should prioritize benchmarks, robustness,
persistent experiment state, carrier interfaces, performance, and real-domain
validation before adding additional named closure levels.


## Validation portfolio continuity

The single master build also owns the empirical validation portfolio.

After any Python-source change, READY carrier seals must be refreshed before a
future confirmation opening. Refreshing a seal does not inspect held-out target
metrics and does not alter the frozen carrier mapping or plan.

Confirmation permits are never generated automatically during a master update.
