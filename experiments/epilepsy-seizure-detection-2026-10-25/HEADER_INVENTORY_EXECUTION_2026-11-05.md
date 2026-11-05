# EP01 development-header inventory — executed transport-blocked run

5 November 2026. This is an execution receipt for the sole EP01
development-only header inventory. It is not a seizure-detector result,
clinical claim, confirmation protocol, or BFG derivation.

## Fixed scope and local input check

The existing runner was invoked once with its fixed 565-record CHB-MIT
development manifest (449 train, 116 validation), four workers, an externally
enforced 30-minute limit, and header-only access. Before the actual request
phase, it exposed a preparation defect: `load_records` requires every allowed
case's original `*-summary.txt`, while the package retained only the already
exposed `chb01` summary. The first invocation therefore stopped locally at the
missing `chb02-summary.txt`; it made no header request.

For the authorized rerun, the 18 missing *development-only* summaries and the
previously audited `chb09_08.edf.seizures` companion were fetched singly from
the pinned CHB-MIT 1.0.0 URLs, each verified against the pre-existing original
`SHA256SUMS.txt`. The companion was 70 bytes and SHA-256
`d6a387c5eaf9033896bce18672914ffe78448c17c723d6a952f221dcfef04af1`.
No archive, internal-test object, Siena object, EDF waveform, or signal sample
was requested. These temporary local annotation inputs were removed immediately
after the run and are not committed or published.

## Actual result

The rerun reached the header phase and wrote 565 per-record local receipts.
All 565 exact development paths were attempted once. Every request stopped at
the existing no-redirect control with the same error:
`ValueError: Unexpected redirect; stop metadata acquisition`.

| Field | Value |
|---|---:|
| expected / attempted files | 565 / 565 |
| eligible / metadata-ineligible / failed | 0 / 0 / 565 |
| all files attempted | true |
| successfully joined seconds | 0 |
| full cohort recorded seconds | null |
| waveform access enabled | false |
| clinical result | false |

The failed receipts were retained locally for aggregate verification. They
contain the path, failure class and message; no EEG samples were read. This is
a transport/access outcome, not evidence about seizures, annotations, channel
quality, BFG, or any detector.

## Consequence

The full-header gate remains **BLOCKED**. Redirect following must not be added
as an after-the-fact workaround: a distinct source-access configuration would
need to specify endpoint, redirect policy, identity controls and independent
review before another finite run. Missing or failed records must remain in the
complete accounting; none may be dropped, inferred, or converted into a
non-seizure observation. No repeat of the same request configuration is
authorized by this receipt.
