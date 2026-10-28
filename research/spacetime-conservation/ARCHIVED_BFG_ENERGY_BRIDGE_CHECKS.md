# Archivvergleich – frische Kontrollen

**Runde 81, 26. Oktober 2026**

## Quellenidentität (lokal)

- `BFG_Unified_V4_Compact_Canonical_Universal_Reclosure_2026-09-12.pdf` — SHA-256 `cc1083760ba0f9ce87a7c822fc1837f24e84425bf3ad12e2e776c1f2eb141fb2`
- `BFG_Endogenous_Dual_Order_Strong_Universal_Canonical_Closure_Whitepaper_2026-09-08.pdf` — SHA-256 `d88d6b83035bd4a7e8c872aba69ba1456b8f4615d16fbd5ccbbdaf69d2b84b52`
- `manuscript_text.txt` (BFG-Preprint, 21. September 2026) — SHA-256 `9cb12d42cd19297d6b068ebd120ebd35fecc6511712ef0e42b4b072dd1ece630`

Die Archivdateien wurden nur gelesen, nicht geändert. Die extrahierten Aussagen sind: strukturelle Lasten sind keine joulewertige Energie; neutrale Anteile brauchen für Energie eine Carrier-Readoutkarte; ein atomarer Carrier-Hamiltonian wird nicht durch BFG erzeugt; und Rekursionstiefe ist nicht physikalische Zeit.

## Ausführung

```powershell
C:\Users\getyo\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe research/spacetime-conservation/bfg_archive_energy_bridge_check.py
```

Ergebnis:

```text
PASS: archived neutral fractions sum to one and are scale invariant
PASS: same BFG data admit distinct sector-compatible energy operators
r_N=268/375; b_N=107/375; E_H1=16/25; E_H2=48/25
```

Die Rechnung verwendet ausschließlich rationale Arithmetik. Sie demonstriert Unterbestimmtheit eines physikalischen \(H\) innerhalb der gemeinsamen Zwei-Sektor-Symmetrie; sie ist keine Behauptung über reale Energieeinheiten.
