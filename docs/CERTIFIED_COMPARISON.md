# Vergleich der zertifizierten Verfahren – 15. September 2026

## Ergebnis bei unveränderten Eingaben

39 bereits vorhandene synthetische Fälle aus `test_certified.py` und
`test_certified_search.py` werden erneut ausgewertet. Messwerte, Messfehler,
Parametergrenzen und Reihenbudget sind innerhalb des Hauptvergleichs identisch.
Die Suche verwendet maximal Tiefe 20. Die Budgets 31 und 255 wurden vor dem
ersten Vergleichslauf festgelegt. Dies ist eine Wiederholung bekannter
Regressionsfälle, kein unabhängiger Leistungsnachweis an neuen Daten.

| Verfahren | Gemeinsamer Parametersatz bestätigt | Ganze Familie ausgeschlossen | Ungeklärt |
| --- | ---: | ---: | ---: |
| Ursprüngliche Mittelpunktprüfung | 3 | 1 | 35 |
| Verfeinerung, maximal 31 Boxen | 7 | 2 | 30 |
| Verfeinerung, maximal 255 Boxen | 13 | 3 | 23 |

Bei 255 Boxen werden **12 der 35 zuvor offenen Fälle zusätzlich geklärt**:
zehn durch einen gemeinsamen Zeugen und zwei durch Ausschluss der gesamten
Familie. Bereits vorhandene Zertifikate bleiben inhaltlich erhalten.
Keiner der als gesund erzeugten Gitter- oder Unsicherheitsfälle wird ausgeschlossen.

| Fallgruppe | Anzahl | Vorher offen | Bei 255 Boxen offen | Erklärung |
| --- | ---: | ---: | ---: | --- |
| Fehler-Eckpunkte der Kalibrierung und Messung | 24 | 24 | 20 | Vier Zeugen gefunden; die übrigen sind mit bekannten Erzeugungsparametern separat zertifizierbar. |
| Gewichtsgitter einschließlich Randpunkten | 7 | 6 | 1 | Gewicht 2 benötigt mehr Suchboxen. |
| Unterschiedliche Gewichte an zwei Messzeiten | 2 | 2 | 0 | Jede Zeit allein kann passen; die gemeinsame Familie wird ausgeschlossen. |
| Unsicherer Anfangszustand, einzelner Knoten | 1 | 1 | 0 | Passender Anfangszustand 1/4 gefunden. |
| Exakte Beobachtung (0.7, 0.3) | 1 | 1 | 1 | Analytisch kompatibel, endliche Intervallprüfung liefert keinen exakten Zeugen. |
| Exaktes Gleichgewicht bei endlicher Zeit 100 | 1 | 1 | 1 | Analytisch inkompatibel; aktuelle Reihenhülle reicht nicht aus. |
| Mittelpunkt-, Konstanz- und Ausschlusskontrollen | 3 | 0 | 0 | Zertifikate unverändert. |

## Gezielte Diagnose der 23 Restfälle

Diese Zusatzprüfungen wurden nach Sichtung des Hauptvergleichs gewählt und
werden ausdrücklich **nicht** in dessen Erfolgszahlen eingerechnet.

* **20 Fehler-Eckpunkte:** Die bekannten synthetischen Erzeugungsgewichte und
  Anfangszustände liegen in der ursprünglichen Familie. Bei festem Kandidaten,
  unveränderten Messungen und Messfehlern sowie 64 Reihentermen bestätigt die
  rationale Prüfung jeden dieser Zeugen. Die Fälle sind damit nachweislich
  kompatibel. Das offene Suchergebnis belegt eine Grenze der Kandidatensuche
  und ihrer Zertifizierung, keine fehlende Kompatibilität. Welcher Anteil allein
  auf Reihenbudget, Tiefenlimit oder Kandidatenwahl entfällt, wurde nicht isoliert.
  Die Erzeugungsparameter stehen einem realen Detektor nicht als Orakel bereit.
* **Gewicht 2:** Nur das Boxenbudget wurde auf 1023 angehoben. Nach 501 besuchten
  Boxen wird ein Zeuge bestätigt. Hier reicht nachweislich mehr Suchbudget.
* **Exakte Beobachtung (0.7, 0.3):** Für zwei Knoten gilt bei x(0)=(1,0)
  `x_1(t)=(1+exp(-2wt))/2`. Bei t=1 erfüllt
  `w=-ln(0.4)/2`, ungefähr 0.458145366, die Beobachtung exakt und liegt in [0,2].
  Das ist ein analytischer Zeuge; die gerundete Dezimalzahl ist kein exakter
  Ersatz. Bei Messfehler null kann eine Hülle positiver Breite niemals innerhalb
  des verlangten Einzelpunkts liegen. Weitere Bisektionen garantieren daher
  kein maschinelles Zertifikat. Im Lauf bleiben zwei Blätter bei Tiefe 20 offen.
* **Zeit 100, festes Gewicht 1:** Hier ist
  `x_1(100)=1/2+exp(-200)/2 > 1/2`. Die exakt verlangte Beobachtung (1/2,1/2)
  bei Messfehler null ist mathematisch unmöglich. Eine Erhöhung von 2 auf 128
  Reihenterme beseitigt zwar den unzureichenden Reihenansatz als Abbruchgrund,
  doch die Hülle bleibt zu grob: weiterhin `unresolved`. Ein genaueres
  numerisches Verfahren oder eine symbolische Zweiknotenprüfung wäre nötig.

Die Annahme exakter Messwerte ist für diese letzten beiden Regressionen
absichtlich streng. Eine nachträgliche Vergrößerung des Messfehlers würde die
Fragestellung verändern und wurde deshalb nicht als Reparatur verwendet.

## Nächster begründeter Entwicklungsschritt

Zuerst Randkandidaten und die durch die Messung bei t=0 erlaubten Anfangszustände
gezielt prüfen, anschließend jeden Kandidaten mit den bestehenden strengen
Schranken zertifizieren. Das adressiert die größte verbleibende Gruppe ohne
pauschal den gesamten Suchbaum zu vergrößern. Der Vergleich zeigt die Priorität;
eine Verbesserung dadurch ist noch nicht implementiert oder nachgewiesen.
Für die exakten Zweiknotenfälle ist eine gesonderte analytische Behandlung sinnvoll.

Ein kompatibler Zeuge identifiziert den wahren Graphen nicht eindeutig. Bei
konstantem Anfangszustand liefern beispielsweise sämtliche erlaubten Gewichte
dieselbe konstante Trajektorie. Zusätzliche Anregung kann für Identifikation
erforderlich sein; kein aktuelles offenes Ergebnis wird pauschal so erklärt.

## Reproduktion und Reichweite

```sh
python -m bfg_lab.certified_comparison
python -m unittest discover -s tests -p test_certified_comparison.py -v
```

`results/certified_comparison.json` enthält alle Eingaben, deren gemeinsamen
SHA-256, Quellen, Einstellungen, Ergebnisse pro Fall und getrennte Diagnosen.
Die Eingaben folgen den ursprünglichen Decimal-Rechnungen (90 bzw. 60 Stellen).
Die Ausgabe verdichtet Zertifikate; vollständige Zertifikate lassen sich mit
`assess_family` bzw. `refine_family` aus den enthaltenen Eingaben erneut erzeugen.

Die publizierte Suite besteht mit **73 Tests**. Drei neue Tests prüfen die
Fallbilanz, erhaltene Zertifikate, fehlende Ausschlüsse gesunder Fälle und die
Zulässigkeit der diagnostischen Zeugen in den ursprünglichen Grenzen.

Die älteren 144 Netz-Stressläufe verwenden einen anderen, einzelnen
Referenzoperator und speichern Messdaten-Hashes statt vollständiger Eingaben.
Sie wurden in diesem Vergleich nicht erneut ausgewertet. Eine Übertragung auf
Graphfamilien benötigt ein eigenes vorab festgelegtes Unsicherheitsprotokoll;
die bisherigen Fehlalarmbefunde bleiben bestehen. Originalpapiere und historische
Ergebnisse wurden nicht verändert. Dies ist kein empirischer BFG-Nachweis.
