# BFG Fundamental Closure — preserved package and review

Author of the supplied BFG research: Marcel Theodor Wende. Intake: 25 September 2026.

This stage preserves all **44 files** from the supplied `BFG_Emergence_Studio.zip`, byte for byte, in [package](package/README.md). Despite its archive name, this is a self-contained Fundamental Closure package, not a replacement for the earlier Emergence Studio master.

The [review](review/REVIEW.md) records fresh verification and a search of the author's two local BFG collections. [Source findings](review/SOURCE_SEARCH.md) distinguish useful historical support from remaining derivation obligations. The original package's integration instructions refer here to the **package root**; they have not been applied to overwrite the repository root.

Run the supplied tests from `package` with `python -m pytest tests -q` in an environment containing pytest, NumPy and SciPy. The review harness runs the supplied consistency and stress functions without replacing their historical JSON reports. Original bytes are identified in [the manifest](review/PACKAGE_MANIFEST.json).

This stage does not change earlier Studio stages or the EEG experiment protocol. Mathematical definitions, conditional results, numerical verification and empirical validation remain distinct.
