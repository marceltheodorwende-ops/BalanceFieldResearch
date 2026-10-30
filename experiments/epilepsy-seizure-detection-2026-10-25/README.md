# EP01: seizure detection data and scoring contract

OPEN preparatory work; no confirmatory freeze or empirical seizure result.
Read DATA_AND_SCORING_AUDIT.md. Reproduce controls with Python 3.12,
`pip install -r requirements.txt` then `python check_contract.py`.
Full waveform access is denied pending the acquisition/preprocessing contract;
the separate development-only metadata probe reads validated EDF-header ranges.
The old negative EEG covariance experiment and open/deferred P81 are preserved.
Upstream scoring code is MIT-licensed; copied old provenance table retains its PhysioNet ODC-By attribution, not a new repository-wide license.

TIMELY_ENDPOINT.md and timely.py add a complementary fresh-activation endpoint
with original event denominators, latency, non-seizure false activations and alarm occupancy.
Run `python check_timely.py` for20 named groups and12,288 exhaustive synthetic oracle cases.
This endpoint supplements, and does not replace, pinned SzCORE scoring.

development_manifest.py builds the pinned source-based565-file development allowlist
(449 train,116 validation); no waveform downloader is enabled.
montage_audit.py proves a common-average identifiability limit for the first allowed
development montage. Run `python check_manifest_montage.py` for19 control groups.
See MANIFEST_AND_MONTAGE_CONTRACT.md for provenance, exposure and remaining gates.

Read BFG_ASSUMPTION_AUDIT.md for the no-invented-laws audit against the directly
hash-verified Dynamic Order PDF. `python check_bfg_boundary.py` checks unchanged
canonical equations on synthetic matrices only; it is not a seizure detector or
an empirically selected EEG preparation. BFG_SOURCE_REVIEW.json records the source.

edf_header.py provides a separately guarded development-header-only probe; full
waveform access stays closed. EDF_HEADER_CONTRACT.md documents the first real
header's units/rate and unresolved duplicate label. `python check_edf_header.py`
runs19 synthetic parser/range/access control groups without network access.

CHANNEL_POLICY.md documents a fixed17-channel instrument candidate that omits
both duplicate T8-P8 copies. `python check_channel_policy.py` runs16 control
groups, including exact ideal row-space equivalence and a noisy-data counterexample.
It is not a frozen montage, trained detector or BFG physiological identification.

STREAMING_CONTRACT.md and causal_stream.py add a one-record causal execution
primitive with explicit availability/coverage masks and no gap filling or file-state carryover.
`python check_causal_stream.py` runs15 groups including90 independent oracle cases.
Scientific filter coefficients, QC and clinical decision rules remain unfrozen.

Development metadata checkpoint: [HEADER_COVERAGE.md](HEADER_COVERAGE.md) records 19 first-per-case header outcomes, including eight preserved parser failures. No seizure performance result.

The 28 October 2026 non-empirical control run is recorded in
[VERIFICATION_LOG_2026-10-28.md](VERIFICATION_LOG_2026-10-28.md): all 19
versioned checkers passed from the package directory, with zero real network
requests from the full-inventory synthetic control. It is not a detector result
or a confirmatory freeze.

[COMPARATOR_TUNING_CONTRACT.md](COMPARATOR_TUNING_CONTRACT.md) fixes the
equal-information, equal-budget and validation-only threshold rules required
for future simple, established, modern and spatial-network comparisons. It
selects neither an algorithm nor a BFG measurement map.
