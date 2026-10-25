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
