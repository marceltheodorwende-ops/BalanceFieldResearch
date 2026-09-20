# Verifikation der CTC-Referenz

Datum: 20.09.2026. Basis-Commit: d94489f4848336fb257e6513178a035459b6c09c.

## Änderung und Akzeptanzkriterien

- Eigenes Modul `bfg_lab.ctc_sa`; keine Änderung historischer Produktionsmodule oder Gates.
- Exakter rationaler Witnessraum aus überprüfter gelieferter Zerlegung; metrischer Projektor separat berechnet.
- Expliziter SA-Zustand mit abgeleitetem R_C und frischem skalarem Gram-Rebuild.
- Dokumentierte Folge 5→4→3→2→⊥; zweidimensionaler Stopp als zusätzliche CTC-Regel.
- Ungültige Daten/numerische Auflösungsfehler bleiben von mathematischer Terminalität getrennt.
- Beispielrechnung und negative Fälle werden als neue Forschungsstufe erhalten.

## Frische Ausführungsbefunde

1. Vor Implementierung scheiterte die neue Testsammlung erwartungsgemäß mit `ModuleNotFoundError: bfg_lab.ctc_sa` (Exit 1).
2. `python -m unittest discover -s tests -p test_ctc_sa.py -v`: 14 Tests bestanden, Exit 0.
3. `python -m bfg_lab.ctc_sa`: drei erfolgreiche Übergänge und expliziter Dimensionsstopp, Exit 0; Ausgabe in `example.json`.
4. `python -m unittest discover -s tests -v`: **143 Tests bestanden**, Laufzeit 16.937 s, Exit 0.

Die drei eta- und Energiewerte wurden gegen die im mathematischen Audit unabhängig berechneten rationalen Werte verglichen. Die Toleranzprüfungen sind keine exakte Zertifizierung der gesamten SA-Matrixrechnung.

## Grenzen

Das Modul verwendet für SA-Eigenwertberechnungen NumPy und TOL=1e-10. Sehr kleine eta oder Komponenten und nahezu degenerierte Eigenwerte können numerisch unauflösbar sein. Die exakte Projektor-Schnittstelle arbeitet mit gelieferten rationalen Zertifikaten und entdeckt nicht automatisch Spektralzerlegungen. Sie verwendet die vorhandenen internen Bruchmatrix-Hilfsfunktionen des Zertifikatsmoduls; die gemeinsame Regression wurde ausgeführt.

Keine empirische Bestätigung der BFG, kein universeller Schließungsnachweis und keine Implementierung einer unendlichdimensionalen Dynamik. Die historischen Testzahlen und Forschungsstufen bleiben unverändert; 143 bezeichnet ausschließlich diesen neuen Gesamtlauf.
