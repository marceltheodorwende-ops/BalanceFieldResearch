# Verifikation am 18.9.2026

- `python -m unittest discover -s tests -p test_persistence_certificate.py -v`:
  8 Tests bestanden, Exit 0.
- `python -m unittest discover -s tests -q`: 123 Tests bestanden in 10.526 s,
  Exit 0.
- SHA-256 aller fünf Originalpaper gegen papers/manifest.json: unverändert.

Neue Fälle: oblique Projektion mit unabhängig bekanntem Ergebnis;
stabiler defekter Block; periphere Rotation; Ablehnung eines peripheren
Jordanblocks mit der gelieferten Metrik; exakte Klassifikation von
1-10^-40; schlecht konditionierte rationale Basis; ungültige Metriken,
Zerlegungen und Eingabeformen; Ablehnung von Fließkommaeingaben.

Diese Prüfungen belegen den begrenzten Zertifikatsbaustein, weder eine
vollständige Zertifikatssuche noch die universelle BFG-Rekonstruktion.
