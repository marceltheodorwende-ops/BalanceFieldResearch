# Runde72: Mess-/Konditionierungstyp und Grenze der physikalischen Energiezuordnung

Präregistrierung PROTOCOL.md, Commit413728e291d06db773ab7d9a81a4196c2fb8358e; Auswertung25. Oktober2026. Auf ausdrückliche Nutzeranweisung werden vorhandene BFG-Mess- und Konditionierungsregeln benutzt, keine physikalischen Gesetze ergänzt. Vollständige Quelle Dynamic Order8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370; PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498 vor Import geprüft.

## Ergebnis vorweg

Aus der vorhandenen Konditionierungsstruktur lässt sich innerhalb eines klar angegebenen Erwartungswerttyps der GEWICHTETE lokale Readout begründen: Wenn W als Zustandsdichte und F als dasselbe feste Observable benutzt werden, ist die unbedingte Erwartung sum_a p_a e_a=tr(WF). Die rohe lokale Paarung q_a=p_a e_a ist im geprüften F-kommutierenden Labelmodell der additive Beitrag dazu.

Die ungewichtete Summe bedingter Erwartungen sum_a e_a ist nicht dieselbe unbedingte Messgröße. Sie hängt schon bei unverändertem Zustand von der bloßen Labelgruppierung ab und lässt sich im Allgemeinen nicht als Erwartung eines festen Observablen auf der Witnessfamilie darstellen. Ihre konservative Verzweigungsbilanz aus Runde71 genügt deshalb nicht, sie als unbedingte physikalische Gesamtenergie auszuweisen.

Damit ist aber noch KEINER der Bilanztypen als physikalische Energie aus dem kanonischen BFG allein bewiesen. Die Quelle legt die notwendige physikalische Zustands-/Hamiltonian-/Apparatebrücke ausdrücklich nicht fest. Die konditionale mathematische Typentscheidung wird nicht mit dieser fehlenden physikalischen Identifikation verwechselt.

## Was die Quelle zur Messung sagt

I6/Gleichung21 definiert normalisierten Witness nach Selektion; I6 bezeichnet m_sel ausdrücklich noch nicht als physikalische Bornwahrscheinlichkeit. I26/Gleichungen97–99 (PDF30) verlangt eine Quantenbrücke mit Hilbertraum, Zustandsdichte, Observablenalgebra und Hamiltonian. Die beiden dort genannten Kandidaten rho_Q=W und rho_Q=F/trF sind ausdrücklich keine Theoreme des endlichen Updates.

I27 (PDF31) zeigt an einem festen Effekt verschiedene Vorhersagen der beiden Zustandsbrücken. I28 (PDF32) unterscheidet einen festen Transportoperator als CP-Operation von der endogen zustandsabhängigen Familie; eine Instrumentidentifikation benötigt unabhängige Konditionierungsdaten.

I41.1/41.2 und II91.5/Gleichung170 verlangen vor Messauswertung festgelegte Präparation, Brücke, Apparatur, Einheiten/Kalibrierung und prüfbare Holdout-Vorhersagen. Passende interne Dimensionen oder Erhaltung allein genügen dort ausdrücklich nicht. Diese offenen Anforderungen werden hier nicht durch neue Gesetze ausgefüllt.

## Mathematische Typentscheidung bei festem Observable

Seien F fest und die scharfen Labelprojektoren E_a orthogonal mit SummeI. Im hier geprüften Sektor gilt [E_a,F]=0 und p_a=tr(E_a W)>0. Die vorhandene Normalisierungsrechnung gibt

    W_a=E_a W E_a/p_a,
    e_a=tr(W_a F),
    q_a=p_a e_a=tr(E_a W E_a F).

Weil das Cover F reduziert,

    sum_a q_a=tr(WF).

Dies ist zunächst Matrixalgebra. Wird W zusätzlich als physikalische Zustandsdichte und F als kalibriertes Observable identifiziert, sind p_a die zugehörigen Labelgewichte und e_a bedingte Erwartungswerte. Dann ergibt ihre gewichtete Summe die unbedingte Erwartung desselben Observablen. Die Gleichung setzt weder einen Hamiltonian noch eine Uhr ein.

Unter bloßer Zusammenfassung mehrerer Detektorlabels addieren sich p_a und q_a; die neue bedingte Erwartung ist der gewichtete Mittelwert, nicht die Summe der alten bedingten Erwartungen. Ferner ist tr(WF) affin in W: Die Erwartung einer Mischung ist die entsprechend gemischte Erwartung. Diese Eigenschaften sind keine neu geforderten BFG-Grundgesetze, sondern folgen aus der angegebenen festen linearen Observable-/Konditionierungsstruktur.

Für nichtkommutierendes F/Cover ist die scharfe Zweigsumme tr(W sum_a E_a F E_a) und muss nicht tr(WF) sein. Frühere Selektions-/Instrumentgrenzen bleiben gültig. Die allgemein positive lokale Vorschrift sqrt(F) E_a sqrt(F) ist ebenfalls ein anderer Readouttyp; eine Instrument-/Ortsidentifikation darf nicht zwischen diesen Typen wechseln, ohne sie zu benennen. Diese Runde beweist keine universell eindeutige Lokalisation.

## Exakter Verfeinerungsgegenzeuge zum ungewichteten Typ

Verwende denselben uniformen Vierfachlift eines n2-Zustands mit F_base=diag(1,3), W_base=[[1/2,1/4],[1/4,1/2]]. Im gelifteten n8-Zustand gilt tr(WF)=1/2. Dieser Zustand und dieses Observable bleiben unverändert; nur die Labels werden in1,2 oder4 Gruppen zusammengefasst.

Die gewichtete Summe ist in allen drei Fällen1/2. Die ungewichtete bedingte Summe lautet dagegen

    1/2 bei einer Gruppe,
    1 bei zwei Gruppen,
    2 bei vier Gruppen.

Ein bloßer Wechsel der Detektorgruppierung vervierfacht also im letzten Fall die ausgewiesene ungewichtete Summe, ohne Zustand oder Observable zu ändern. Sie kann damit nicht der gruppierungsunabhängige unbedingte Erwartungswert desselben F sein. Ihre Levelkonservativität aus Runde71 bleibt richtig, bestimmt aber einen anderen mathematischen Readout.

Das widerlegt keine extensive Summe tatsächlich gleichzeitig existierender Subsystemenergien: Dafür müssten physikalische Subsysteme, deren lokale Energieobservablen und der gemeinsame Apparat bereits spezifiziert sein. Eine solche extensive Messstruktur ist nicht identisch mit der ungewichteten Addition von Mittelwerten auf exklusiv konditionierten Labels. Die deklarierte Punktwolke allein stellt diese Gleichsetzung nicht her.

## Exakter Präparationsmischungs-Gegenzeuge

Im festen Raum C2 tensorC2 sei F=diag(1,1,3,3), das Cover unterscheide die Indexpaare(0,2) und(1,3). Setze

    W_A=diag(4/5,1/50,1/10,2/25),
    W_B=diag(1/50,2/5,2/25,1/2),
    W_M=(W_A+W_B)/2.

Alle drei Witness sind strikt positiv und normiert; alle übrigen BFG-Daten sind gleich. Die gewichteten Erwartungen sind34/25,54/25 und44/25, also exakt affin.

Die ungewichteten Summen sind172/45,212/45 und88/25. Somit

    U(W_M)-(U(W_A)+U(W_B))/2=-56/75.

Kein einziges von W unabhängiges hermitesches H kann daher U(W)=tr(W H) auf dieser Familie darstellen, weil jede solche Darstellung affin wäre. Postselektierte bedingte Erwartungen sind dadurch nicht verboten; deren Quotientennichtlinearität ist gerade der andere Typ. Auch ein unabhängig klassisch konditioniertes Instrument oder anders spezifizierte Präparationsklasse wird nicht allgemein ausgeschlossen. Es wird nur verhindert, diese Typen als dasselbe unbedingte feste Observable auszugeben.

## Warum der gewichtete Typ noch keine physikalische Energie ist

Selbst bei mathematisch festem F fehlen zwei eigenständige Entscheidungen: Welche BFG-Größe ist die physikalische Zustandsdichte, und welches Observable ist der physikalische Energieoperator? Die Quelle lässt beides als Brücke offen.

Am eigenen I27-Beispiel F=diag(1,3),W=diag(3/4,1/4) geben die zwei vorhandenen Kandidaten schon für denselben F-Readout

    tr(WF)=3/2,
    tr((F/trF) F)=5/2.

Diese exakte Unterscheidung ist keine Behauptung H_phys=F; sie zeigt, dass die Quelle sogar vor einer Hamiltonian-Identifikation unterschiedliche statistische Readouts zulässt. Die bestehende BFG-Dynamik wählt diese Hypothesen nicht allein durch die Konditionierungsformel aus.

Auch der Formationsbestand trF bleibt eine exakte, teils konservative BFG-Buchführungsgröße. Er wird durch diese Mess-Typprüfung nicht mathematisch widerlegt, aber dadurch ebenso wenig als Joule-Energie kalibriert. Seine physikalische Messabbildung fehlt wie die der übrigen Kandidaten. Die frühere Generatorverträglichkeitsprüfung FORMATION_GENERATOR_COMPATIBILITY.md bleibt zusätzlich relevant; ein erhaltener F-Erwartungswert allein macht F nicht zum physikalischen Zeitgenerator.

## Frische Kontrollen und CI

[MEASUREMENT_ENERGY_BALANCE_TYPES_CHECKS.md](MEASUREMENT_ENERGY_BALANCE_TYPES_CHECKS.md) enthält vollständige Reproduktion und Rohdaten. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur mit fünf Originalereignissen: die drei n4-Präparationen, uniformer n8-Hierarchiezustand und komplexe Eichversion von W_A, Seed20261122.

Alle tatsächlichen Quellselektionen besitzen Masse1 und R4-ErfolgseffektI. Die verschiedenen Labelgewichte sind daher keine tatsächlichen selektierten BFG-Ereignisausgänge. Co-moving Labelabfragen bleiben nach dem Originalupdate gleich; die nichtlineare ungewichtete Mischungsabweichung stammt aus dem Readout, nicht aus einer behaupteten Nichtlinearität des hier festen Witnesskanals. Der Ausgangswitness erfüllt die Mischungsaffinität mit Rest6.21e-17. Maximaler Readouttransportrest4.45e-15, R4-Identitätseffektrest1.01e-15 und Eichreadoutrest3.11e-15. Toleranz1e-10; alle getesteten bedingten Massen sind strikt positiv, kleinste .1 bzw. .25, keine Nullmassen-Nachjustierung.

Runde71-CI am exakten Ergebnishead ist separat grün dokumentiert. Die neue eingebettete Reproduktion bleibt lokale Evidenz; Originaldynamik, Manuskripte, Lizenzen, empirische Ergebnisse, Audit-Dateien und Workflows unverändert.

## Präzise nächste Abhängigkeit

Unter der ausdrücklich hypothetischen Witness-/F-Observable-Interpretation ist der gewichtete lokale Typ für eine unbedingte Messung begründet; der ungewichtete Typ kann diesen Platz nicht allein wegen seiner Levelbilanz übernehmen. Eine physikalische Energieauswahl verlangt darüber hinaus die in I26/I41/II91.5 selbst geforderte feste Zustands-/Observable-/Apparate-/Kalibrierungsbrücke. Dafür liegt aus den hier verwendeten Quellen noch keine ausgesuchte vollständige Vorschrift vor.

Kein zusätzlicher Hamiltonian, keine Naturkonstante und kein Instrument wurden zur Zielerfüllung erfunden. Der verbleibende Unterschied ist nun eine präzise fehlende physikalische Identifikation, nicht ein durch Umbenennen oder eine günstig erhaltene Summe gelöstes mathematisches Problem. Dies ist kein allgemeines No-Go gegen eine spätere BFG-physikalische Brücke.
