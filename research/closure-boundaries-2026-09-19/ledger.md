# Abschlussledger der automatischen internen Ableitungsrunde

## Sieben Pflichten

| Problem | Erreicht | Was weiterhin fehlt |
| --- | --- | --- |
| 1 State Update | Bedingter vollständiger Zustandsvertrag; erforderliche Kanaldaten präzisiert | Intern begründete Aktualisierung dieser Daten |
| 2 B_C,W_N,L_C | Nicht-Eindeutigkeit eingegrenzt; bedingte G1-Kompatibilität und Gegenfälle | Konkrete eindeutige Rekonstruktion mit ursprünglicher Bedeutung von D_cov c |
| 3 Gram-Rebuild | Getesteter Matrixbaustein für gelieferte Faktoren; verlustfreie Gram-Zerlegung | Autonome Erzeugung seiner Faktoren |
| 4 Rekursiver Transport | Voraussetzungen und Kompressionsrisiko gezeigt | Eindeutiges internes R_next mit Stabilitäts-/Persistenznachweis |
| 5 Universelle Iteration | Bedingter Induktionssatz | Nachweise der Voraussetzungen; weder universelle Realisierung noch Konvergenz bewiesen |
| 6 Nichtnormaler Fall | Exakter rationaler Zertifikatsprüfer; 123 Softwaretests im letzten Codelauf | Allgemeine Suche, weitere Eingabeklassen und Erzeugung von R_next |
| 7 Unendlichdimensional | Bedingte Formrealisierung und expliziter Domänengegenfall | Konkrete domänenerhaltende Gesamtiteration |

Keines der offenen universellen Probleme wird allein wegen der Softwaretests
oder der lokalen Gegenbeispiele als vollständig abgeschlossen gewertet.

## Grenze der eigenständigen Fortsetzung

Die nächsten zentralen Schritte benötigen ein explizites vorgelagertes Modell:
Definition von D_cov und seiner Entwicklung, Konstruktion von W_N und L_C,
Transformationsregel für die vollständigen Kanäle und R_next sowie zulässige
Domänen. Die fünf Quellen formulieren diese Konstruktion bislang als Aufgabe.
Die bisher geprüften vereinfachenden Schlusswege ersetzen sie nicht.

Eine zusätzliche Modellwahl könnte weiterentwickelt werden, wäre aber ein neuer
ausdrücklich hypothetischer Ansatz. Die automatische Ableitungsrunde wird deshalb
pausiert, statt denselben Quellenstand immer wieder als vermeintlichen Beweis zu
bearbeiten. Das ist keine Behauptung, es gebe weltweit keine weitere sinnvolle
Mathematik zu BFG; es ist die Grenze des derzeit spezifizierten internen Auftrags.

Wiederaufnahme: neue konkrete Quellendefinition oder ausdrücklich als solche
behandelte Modellannahmen liefern, daraus überprüfbare Rekonstruktions- und
Transportgesetze formulieren und gegen die dokumentierten Gegenfälle prüfen.

## Erhaltene Nachweise

- [Bedingte Herleitungen](../internal-closure-2026-09-18/README.md)
- [Lokale Nicht-Eindeutigkeit](../reconstruction-witness-2026-09-18/README.md)
- [G1-Vorschlag](../gram-inheritance-proposal-2026-09-18/README.md)
- [G1-Kompatibilitätsprüfung](../gram-compatibility-2026-09-18/README.md)
- [Mitgeführte Kanäle](../retained-channels-2026-09-18/README.md)
- [Exakte nichtnormale Zertifikate](../exact-nonnormal-2026-09-18/README.md)

Diese Abschlussentscheidung folgt dem Auditprinzip, Nichtableitbarkeit unter
den geprüften Voraussetzungen offen zu halten und keine neuen Axiome zu erfinden.
