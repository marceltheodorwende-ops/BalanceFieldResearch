# Audit und Verifikation

Die drei Auditquellen und SHA-256 stehen im unveränderten
[Quellenregister](../prediction-audit-2026-09-18/sources.json).

- Complete Edition: Claim-State und Redescription-Prüfung. Bedingte Sätze,
  Korrekturvorschlag, numerische Umsetzung und Naturbehauptung bleiben getrennt.
- Workflow Master: begrenzter Prüfgegenstand, Voraussetzungen und Negativbefunde
  dokumentiert; keine alten Resultate umklassifiziert.
- Context Recovery: Quellenhierarchie eingehalten; V2 §24 als offene Aufgabe
  gelesen, V4-Kompaktschreibweise nicht als fehlende Funktionsdefinition ersetzt.

Abnahme: vollständige Lösung aller sieben Punkte **nicht erreicht**. Insbesondere
werden keine frei gewählten F_B,F_W,F_L,F_R als interne Ableitung eingeführt.
Die neuen Resultate schließen den bedingten Matrix-Rebuild und formulieren
nachprüfbare Sätze für Teilklassen. Es handelt sich um KI-gestützte Herleitungen,
keine unabhängige Begutachtung oder formale Proof-Assistant-Verifikation.

Sieben gezielte neue Tests prüfen einen rechteckigen analytischen Referenzfall,
komplexe Adjungierte, Nullgewicht, unitäre Kovarianz, ungültige Gewichte,
inkompatible Domänen/Toleranzen und die sichtbare Rundungspolitik. Der erste
gezielte Lauf bestand alle sieben Tests. Erwartungswerte stammen aus separater
Handrechnung bzw. Basiswechsel-Invarianz. Keine empirischen Tests.

Ausführung: `python -m unittest discover -s tests -p test_gram.py -v`.
Gesamtsuite und Originalhashprüfung werden im separaten Verifikationsprotokoll
dieser Stufe festgehalten. Kein Testlauf wird als Schließung der offenen
Rekonstruktionsfunktionen oder als Naturbestätigung ausgegeben.
