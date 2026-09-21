# Reale RLC-Messungen: Schaltungsrekonstruktion und BFG-Zuordnungsgrenze

Stand: 21. September 2026. Explorative Auswertung realer Impedanzdaten, keine Bestätigung der BFG und kein Test eines bereits operationalisierten CTC-Übergangs.

## Daten und Provenienz

Quelle: Michael A. Danzer, Christian Plank und Tom Rüther, **Impedance data for various electrochemical and electrical systems**, Version 1.0.0, [Zenodo, DOI 10.5281/zenodo.10794584](https://doi.org/10.5281/zenodo.10794584), Universität Bayreuth. Lizenz laut Zenodo-API: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Die Datei [rlc_circuit.json](rlc_circuit.json) ist unverändert übernommen. Analysecode und Ergebnisse sind eigene Ergänzungen; keine Zustimmung der Datenersteller zur BFG-Interpretation wird behauptet.

Die dokumentierte Schaltung besteht aus einem Kondensator parallel zu einer verlustbehafteten Spule. Die Metadaten nennen C=2,2 µF, L=5 mH, R=9,7 mOhm, nominelle Fabrikwertabweichungen bis +/-10 %, galvanostatische Messung mit 30 mA und Biologic VMP300. Diese Fabrikwertangabe ist keine Messfehlergrenze der einzelnen Impedanzpunkte.

Die Datei enthält 81 Frequenzen von 99,968163 bis 10002,226 Hz und komplexe Impedanzen. MD5 0d8f9939685d435c7475aed873a6ba99 stimmt mit dem Zenodo-Dateieintrag überein. SHA-256: 5ba93aeef5570f8eaf13bf84e0d2b3bb5221f2d208ce365c9088b62873ef5cbd. Verwendet wurden die numerischen Felder z_real und z_imag, nicht die gerundeten komplexen Zeichenketten.

Die Datei ist ein verarbeitetes Frequenzspektrum, kein Datensatz vollständiger Strom-/Spannungszeitverläufe, wiederholter Präparationen oder beobachteter Reclosure-Übergänge. Die technische Exportzeit im Dateikopf ist kein unabhängig verifiziertes Messdatum.

## Gewöhnliches Vergleichsmodell

Mit omega=2 pi f folgt aus der Parallelschaltung:

    Z(omega) = 1 / [1/(R+i omega L) + i omega C]
             = (R+i omega L)/(1+i omega C(R+i omega L)).

R,L,C sind positiv. Dieses Modell stammt aus gewöhnlicher Schaltungstheorie. Die Buchstaben C und L bezeichnen hier elektrische Bauteilwerte, nicht automatisch die gleich benannten BFG-Operatoren.

Auswertungsverfahren: Frequenzen aufsteigend sortiert, gerade nullbasierte Indizes als 41 Fitpunkte, ungerade als 40 Interpolationskontrollpunkte. Minimiert wurde die Summe der relativen komplexen quadratischen Residuen, mit identischem Gewicht pro Frequenz. Das ist keine aus Messunsicherheiten hergeleitete Likelihood. Ein gedämpftes Gauss-Newton-Verfahren in logarithmischen positiven Parametern wurde von drei verschiedenen Startwerten ausgeführt. Keine zusätzlichen Schaltungselemente wurden nachträglich eingeführt.

Der Datensatz war vor dieser Aufteilung bereits eingesehen. Der Vergleich ist daher explorativ und weder ein blinder Test noch eine unabhängige Replikation. Die Kontrollfrequenzen prüfen Interpolation innerhalb desselben Sweeps, keine neue Messung und keine Extrapolation.

## Ergebnisse

| Größe | Ergebnis |
|---|---:|
| R im Fit | 9,53528 Ohm |
| L im Fit | 4,84889 mH |
| C im Fit | 2,18313 µF |
| Relativer komplexer RMS-Fehler, Fitpunkte | 1,5926 % |
| Relativer komplexer RMS-Fehler, Interpolationskontrolle | 1,5958 % |
| Größter relativer komplexer Fehler, Interpolationskontrolle | 4,2743 % |
| Komplexer RMS-Fehler, Interpolationskontrolle | 1,90883 Ohm |

Die Prozentgröße ist sqrt(mean(|Z_model−Z_data|²/|Z_data|²)), keine statistische Konfidenz und keine Angabe zur BFG-Gültigkeit. Die vollständigen Zahlen stehen in [RESULTS.json](RESULTS.json).

**Dokumentationsdiskrepanz:** Der nominelle Widerstand 0,0097 Ohm passt in dieser Topologie nicht zu den Daten; der nominelle Parametersatz ergibt über alle Punkte etwa 107,4 % relativen komplexen RMS-Fehler. Bereits bei der kleinsten Frequenz liegt Re(Z) bei 9,49367 Ohm. Der angepasste Widerstand liegt nahe 9,7 Ohm statt 9,7 Milliohm. Möglich sind ein Einheitenfehler in der Beschreibung oder nicht vollständig beschriebene Verluste. Ohne unabhängige Bauteilmessung oder Auskunft der Ersteller wird die Ursache nicht entschieden und die Quelle nicht korrigiert.

Dass L und C nahe den angegebenen Werten liegen und das Modell die Kurve gut annähert, liefert einen brauchbaren konventionellen Ausgangsvergleich. Die verbleibenden Residuen lassen sich ohne punktweise Fehlergrenzen nicht abschließend als Rauschen oder Modellfehler klassifizieren.

## BFG-Zuordnung: konkrete Grenze statt nachträglicher Anpassung

1. Die komplexe, frequenzabhängige und dimensionsbehaftete Impedanz Z ist nicht unmittelbar ein positiver selbstadjungierter dimensionsloser Gramoperator Y. Ihr Imaginärteil wechselt im Spektrum das Vorzeichen. Eine willkürliche Normierung ihres Betrags und die Definition Y=1/s−1 würden die gewünschte Resolventenform konstruieren, nicht unabhängig testen.
2. Die gemessene Antwort bestimmt weder die BFG-Kapazitäten noch den aktiven BFG-Vektor und den Paketgewinn q unabhängig. Eine Interpretation der Frequenzpunkte als aufeinanderfolgende Reclosure-Stufen wäre eine neue, unbegründete Annahme.
3. Besonders deutlich ist die Persistenzgrenze bei direkter Identifikation der BFG-Rekursion mit der freien Schaltungsdynamik. Für x=(v_C,i_L) und ohne äußeren Strom gilt

       x_dot=A x,
       A=[[0,-1/C],[1/L,-R/L]].

   Das charakteristische Polynom ist lambda²+(R/L)lambda+1/(LC). Bei R,L,C>0 haben beide Wurzeln strikt negativen Realteil. Mit den Fitwerten sind sie ungefähr −983,245 +/- 9669,522 i pro Sekunde. Für jede feste positive Abtastzeit besitzt exp(A delta_t) daher ausschließlich Eigenwerte mit Betrag kleiner eins. Sein peripherer persistenter Rieszraum ist leer.
4. Unter dieser direkten dynamischen Zuordnung ist somit kein nichttrivialer persistenter CTC-SA-Sektor vorhanden. Eine dauernde sinusförmige Fremdanregung ist keine nichtabklingende Eigenmode der freien Schaltung. Eine Erweiterung um die Quelle oder andere Zustandsräume wäre ein neues Modell mit zusätzlichem Nachweisbedarf. Auch die zweidimensionale Zustandsdarstellung liefert keine nichtterminale Folge des SA-Modells mit seiner ausdrücklich gesetzten Dimensionsgrenze.

**Urteil:** Geeignet als reale Kontrolle einer Schaltungsrekonstruktion und als negativer Eignungstest der direkten dynamischen BFG-Zuordnung. Nicht geeignet, um mit diesen Daten allein zwischen g=q, q² und q/2 zu entscheiden. Dieser Befund widerlegt nicht sämtliche möglichen BFG-Realisierungen; er schließt die hier geprüfte unmittelbare Interpretation aus.

Die vorherige Empfehlung eines RLC-Einstiegs war eine Kandidatenauswahl. Die nun ausgeführte Prüfung begrenzt diese Empfehlung ausdrücklich: Ein guter RLC-Fit darf nicht als Fortschritt bei der empirischen Auswahl des BFG-Load-Gesetzes gezählt werden.

## Verifikation und Reproduktion

Abhängigkeit: Python 3 und NumPy (ausgeführt mit NumPy 2.3.5).

    python research/rlc-realization-2026-09-21/analyze.py

Geprüft wurden Dateihash, endliche/eindeutige Frequenzwerte, Konsistenz von Frequenz und Kreisfrequenz, Betrag und Phase der Impedanz, äquivalente Kirchhoff-Admittanzform und DC-Grenzwert. Drei Optimierungsstarts konvergieren auf denselben Parametersatz. Ein separates synthetisches Spektrum mit bekannten R,L,C wird numerisch zurückgewonnen. Diese synthetische Kontrolle validiert das Rechenverfahren, nicht die BFG oder die physikalische Vollständigkeit der Topologie. Die Stabilitätsaussage folgt zusätzlich analytisch aus dem charakteristischen Polynom. Ausführung erfolgreich, Exitstatus 0; kein Gesamttestlauf der unveränderten BFG-Implementierung.

Auditkriterien der drei BFG-Vorlagen: Daten und Deutung getrennt, Einheitenkonflikt erhalten, Vergleichsmodell explizit, negatives Eignungsergebnis nicht entfernt. Kein Kontakt mit den Datenerstellern und keine Veröffentlichung in deren Namen.

## Konsequenz für den nächsten Kandidaten

Vor einem weiteren Fit muss ein Kandidat drei Dinge anbieten: eine physikalisch begründete Zustandszuordnung, einen unabhängig belegten persistenten Sektor oder eine begründete andere Rekursionsabbildung sowie tatsächlich beobachtete Übergänge, aus denen alter Paketgewinn und neuer Load getrennt bestimmbar sind. Ein weiterer gewöhnlicher Input-Output-Datensatz allein löst diese Anforderungen nicht.
