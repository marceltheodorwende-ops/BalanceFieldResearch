# Fortschrittsledger: sieben Beweispflichten

Stand dieser Stufe: 18.9.2026, Fortsetzung von 2e680c2.
Dieses Ledger konsolidiert die bisherigen Stufen; historische Dateien bleiben erhalten.

| Pflicht | Nachgewiesen | Offen / nächste konkrete Pflicht |
| --- | --- | --- |
| 1 Vollständiger State Update | Bedingter Zustandsvertrag; komprimiertes c kann Ableitungskanäle verlieren | Geschlossene Aktualisierung aller erforderlichen Daten, nicht nur Y |
| 2 B_C,W_N,L_C | Lokale Nicht-Eindeutigkeit; G1-Kompatibilität unter Intertwining; Informationsverlust aus c' allein | Eindeutige vorgelagerte Funktionen oder begründet eingeschränkte Realisierung |
| 3 Gram-Rebuild | Implementiert für gelieferte Faktoren; jetzt exakte verlustfreie Kanalzerlegung | Faktoren aus dem Zustand gewinnen; gewichtete Kanäle korrekt behandeln |
| 4 Rekursiver Transport | Polarabbildung ist nicht automatisch R_next; Kompression kann Stabilität verlieren | Intern begründetes R_next und Erhaltung seiner zulässigen Klasse |
| 5 Universelle Iteration | Induktiver Satz bei wohldefiniertem U:S→S | Voraussetzungen 1,2,4 nachweisen; keine Konvergenz aus endlichem Lauf |
| 6 Nichtnormaler Fall | Endlicher potenzbeschränkter Spektralsatz; metrische vs. Rieszprojektion getrennt | Numerische Zertifizierung und Einbindung in vollständige Rekursion |
| 7 Unendlichdimensionale Realisierung | Bedingter Satz über abgeschlossene Gramformen | Dichte Domänen, Abschließbarkeit, Persistenz und Erhaltung unter Iteration |

## Nicht erneut als Lösung versuchen

- Positive Gram-Faktorisierung allein bestimmt keine vorgelagerte Rekonstruktion.
- G1 nicht ohne zusätzliche Begründung als Quellenaxiom behandeln.
- G1 nicht allgemein mit dem aus komprimiertem c rekonstruierten Gram gleichsetzen.
- Ein verlorenes B'=0 nicht durch Änderung von W' oder L' reparieren wollen.
- Delta=E†E nicht als vollständigen Ersatz für äußere dynamische Kanäle ausgeben.
- Softwaretests, exakte lokale Rechnungen und Naturbestätigung nicht vermischen.

## Nächste unabhängige Arbeit

Für die Rekonstruktion ist zu prüfen, welche Kanaldaten eine geschlossene
Ableitungsregel benötigt. Ein lokaler Fehlerterm genügt noch nicht. Parallel
im sachlichen Sinn unabhängig wäre ein exakter endlichdimensionaler Nachweis
der Persistenz für vorgegebene nichtnormale rationale Matrizen möglich;
dies wäre ein begrenzter Baustein, keine Lösung der vorgelagerten Dynamik.

Die Automatisierung wird noch nicht als abgeschlossen markiert: diese
konkreten unabhängigen Pflichten sind noch bearbeitbar. Eine zusätzliche
universelle Closure wird ohne Begründung nicht eingeführt.
