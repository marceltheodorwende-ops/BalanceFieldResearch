# Transport amendment before empirical evaluation

7 October 2026. Run 37674587952 passed all six numerical checks, then failed
with a connection timeout downloading PhysioNet files; evaluation was skipped.
No empirical prediction result was inspected or used to alter the protocol.

The downloader now tries the public AWS mirror documented by PhysioNet,
https://physionet-open.s3.amazonaws.com/eegmmidb/1.0.0/, with the canonical
PhysioNet endpoint as fallback. Files must match the official SHA256SUMS.txt.
The manifest records the download endpoint; incomplete/mismatched files are not
accepted. Verified raw files are cached by GitHub Actions but not committed.
Connection timeouts are bounded and concurrency reduced to eight workers.
The workflow explicitly uses Bash pipefail so failed tests stop publication.

These are transport and execution changes. Subject splits, channels, model,
preprocessing, comparators, endpoints and success criteria remain unchanged.
No empirical results exist from the failed run.
