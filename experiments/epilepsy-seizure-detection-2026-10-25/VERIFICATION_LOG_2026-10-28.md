# EP01 verification log — 28 October 2026

Status: non-empirical implementation verification only. This is not a protocol
freeze, data acquisition, detector evaluation, or clinical result.

## Scope

All currently versioned `check_*.py` controls were executed once from this
package directory with Python 3.12 and the pinned `numpy==2.3.5` environment.
The package-relative working directory is required because several controls
intentionally load their adjacent, pinned audit inputs by relative path.

## Command and result

```text
for checker in check_*.py; do python "$checker"; done
```

All 19 checkers reported `status: PASS`:

- annotation import and reconciliation;
- availability, cohort, patient and manifest/montage controls;
- BFG boundary, causal-stream, channel, EDF-header and timing controls;
- contract, event-spacing, recording-time and scoring controls; and
- full-header-inventory, numbered-annotation and timely-endpoint controls.

The runner's synthetic full-inventory control again made zero real network
requests. A first aggregate invocation from the repository root failed before
any checker assertion because `check_annotation_import.py` correctly could not
find its package-relative `development_header_audit.json`; rerunning from this
directory produced the results above. This is a working-directory requirement,
not evidence about EEG data or clinical performance.

## Unchanged limits

The real 565-record header inventory remains `PREPARED_NOT_STARTED` pending a
supported finite job lifecycle. No EDF waveform, external holdout data, or
external labels were opened. No seizure detector, threshold, performance,
clinical utility, physiological law, or new BFG derivation follows from these
software controls.
