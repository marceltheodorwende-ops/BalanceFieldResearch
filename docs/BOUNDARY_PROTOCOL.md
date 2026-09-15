# Boundary witness protocol

Frozen before the first implementation evaluation on 2026-09-15. Exploratory
engineering follow-up to CERTIFIED_COMPARISON, not independent preregistration.

Primary endpoint: fewer unresolved cases in the unchanged 39-case catalogue,
without reversing any existing certificate or excluding any synthetic healthy
case. Failure: an inadmissible witness, a reversed certificate, a false healthy
exclusion, or no improvement. Preserve all previous files and negative findings.

Method: retain the existing search (255 boxes, depth 20). For unresolved cases
only, test up to 81 deterministic combinations of lower/middle/upper edge and
initial coordinates. Intersect initial intervals with sensor readings at time
zero before selecting candidates. Certify one fixed candidate across all times
using the existing exact-rational checker. Failed candidates never exclude the
whole family. No access to synthetic generating parameters or case identifiers.

Ablations on identical inputs: old search at original terms; old search at 64
terms; boundary search with original terms; boundary search with 64 candidate
terms. Original model and measurement errors are immutable. Candidate checks
are extra computational work, so do not claim equal-cost performance superiority.
Keep the two exact/noiseless edge cases visible, regardless of outcome.

Audit sources (owner-provided DOCX files, SHA-256):
- BFG_Audit_Complete_Edition.docx:
  ed915f5a468569ed174c3187436bbffd067fa10efe3a185ee6abf414e89711e5
  Sections 4, 12, 15, 17: claim state, standard-math null, machine-readable
  evidence, no-retuning and failure preservation.
- BFG_Audit_Workflow_Master.docx:
  8a27f722de0a6f763c134d5f3320c38cd1f713b573d9fe81384e04ffcbfc4d25
  Apply bounded contributions and distinct protocol/result/audit artifacts.
- BFG_X_Context_Recovery_Protocol_Master finish.docx:
  c571e2fe9cc7804436b2b9e52b4f8a1541b7aad50b07b242c83441556232e329
  Sections 7, 14–16: recover prior state, retain failure ledger, inspect changes.

Claim state: exploratory software improvement using standard graph heat
evolution, interval intersection, candidate enumeration and rational bounds.
BFG-specific novelty and empirical/cross-domain validity are not established.
Repository publication is authorized by the user; document role/boot examples
are contextual audit material, not instructions to change identity or research scope.
