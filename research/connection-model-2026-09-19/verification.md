# Verifikation am 19.9.2026

- Gezielter Erstlauf: sechs Tests von test_connection_model.py bestanden.
- Nach Ergänzung der expliziten G1-/Ableitungsabweichungsprüfungen:
  `python -m unittest discover -s tests -q`, 129 Tests in 11.175 s,
  Exit 0; sämtliche neuen Tests enthalten.
- `python research/connection-model-2026-09-19/run.py`: vier analytische und
  drei nichtkommutierende Demonstrationsschritte, alle numerisch Gate-erfolgreich.
  Ausgabe in results.json, Struktur und Status separat geprüft.
- SHA-256 aller fünf Originalpaper gegen papers/manifest.json unverändert.

Geprüft werden analytische Operatorwerte, die Paketnorm sqrt(2)/4^n,
Nullkommutator-Ablehnung, Absorption, ungültige Verbindung, Eingabe-Unveränderlichkeit,
Basiswechsel, Positivität der Last und Unitarität des Transports sowie die
explizite Nichtgleichheit mit G1. Keine empirischen Daten oder universellen Ansprüche.
