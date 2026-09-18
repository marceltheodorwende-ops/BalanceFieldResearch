# Frische Verifikation

Datum: 18. September 2026; Python 3.12 in der lokalen Codex-Laufzeit.

| Prüfung | Ergebnis |
| --- | --- |
| `python -m unittest discover -s tests -p test_gram.py -v` | 7 Tests bestanden, Exit 0 |
| `python -m unittest discover -s tests -v` | 115 Tests bestanden, 10.946 s, Exit 0 |
| SHA-256 gegen `papers/manifest.json` | Alle fünf Originalquellen unverändert |

Die neue Suite prüft den bedingten Rebuild, nicht eine noch nicht spezifizierte
universelle Rekonstruktion. Die mathematischen Beweise im Begleittext sind
separat lesbar und nicht durch die Testzahl ersetzt. Die Implementierung bietet
keine Fehlerintervalle für allgemeine schlecht konditionierte Matrizen.
