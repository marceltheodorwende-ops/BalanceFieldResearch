# BFG relational composition and the shared balance state

Mathematical supplement prepared for Marcel Theodor Wende, 30 September 2026. The paper and reproducibility package are in English.

- [Download the derivation with 32 editable equations (DOCX)](BFG_Relational_Composition_and_Balance_State_2026-09-30.docx)
- [Download the reproducibility package (ZIP)](BFG_Relational_Composition_Reproducibility_Package_2026-09-30.zip)

## Result and scope

Under three explicitly stated additional relational rules (R1: linear closure under local endpoint operators; R2: an invariant relation metric; R3: matched neutral intertwining with isotropic quadratic costs), the construction yields a four-dimensional complex relation space and a normalized Bell-form direction. It starts from the complex local carrier already used in the BFG carrier paper.

The existing real G0 continuation selects and preserves this direction in the declared real Hermitian relation sector. The supplement also identifies the global-phase zero mode in the real Hessian on the full complex relation space; it does not claim a positive Hessian or a complete G0 continuation on that full space.

R1–R3 are proposed BFG constitutive additions, not established deductions from the historical Level-0 axioms. The geometric correlation combination is 2√2, but interpreting it as counted CHSH outcomes still requires additional measurement assumptions. This is not an independent derivation of the Born rule or empirical validation of BFG.

## Reproduce the calculations

Extract the ZIP and run:

```bash
python3 verify_relational.py
```

The verification requires Python and NumPy. It checks exact finite matrix identities, 96 source and endpoint-frame variants, and five G0 steps per variant (480 steps in total). The recorded maximum numerical residual is 4.263256414560601e-14.

The ZIP contains:

- `verify_relational.py`
- `source/g0_model.py` (unchanged real G0 implementation)
- `results.json`
- `build_report.py`
- `README.txt`

The report builder additionally requires python-docx, lxml, and Pandoc. The English paper was rendered and all eight pages were visually checked before publication. All 32 native editable equations match the previous version, apart from a translated explanatory phrase. The verification script, G0 implementation, and recorded numerical results are unchanged. The report builder now generates the English paper.

This English edition replaces the German files previously published in this folder. The earlier edition remains available in Git history.
