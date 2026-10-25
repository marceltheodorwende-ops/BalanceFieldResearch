# EP01: seizure detection data and scoring contract

OPEN preparatory work; no confirmatory freeze or empirical seizure result.
Read DATA_AND_SCORING_AUDIT.md. Reproduce controls with Python 3.12,
`pip install -r requirements.txt` then `python check_contract.py`.
The code has no network calls and denies all waveform requests pending an exact development manifest.
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
