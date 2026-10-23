# Paarfamilie außerhalb skalarer Last: Geschlossenheitsdefekt und native Ergänzung

## Quelle und präziser Kandidat

Ausschließlich derselbe gepinnte vollständige positive BFG-Persistenzsektor, Standardmathematik. Aus Runde 34 bleiben F=diag(1,2,4), W=[[1,0,0],[0,4,-1],[0,-1,4]]/9, J=i(|2><3|-|3><2|), K_plus/minus=I/3±J/12 und die beschriftete P_tau-Familie aus F+tau W erhalten. tau ist weiterhin zusätzliche mathematische Selektorwahl, kein Quellgesetz. Der originale Quellträger hat Rang drei.

Die vorgeschlagene Reduktion behält Y,F,W und sämtliche beschrifteten Kompressionen P_tau K P_tau. Sie vergisst nur die eine J-Richtung des Kernels im Beispiel. Die letzten Resultate zeigten ausdrücklich Geschlossenheit dieser Faser im skalaren Lastteilbereich. Jetzt wird ihre Erweiterung auf eine nichtskalare, vollständig zulässige Last geprüft.

## Identische reduzierte Eingänge und echte Quellkopplung

Setze für 0<e<=.02

Y=[[.1,e,0],[e,.1,0],[0,0,.15]].

Die Eigenwerte sind y_minus=.1-e,y_plus=.1+e,y_3=.15, mit Eigenvektoren (e_1-e_2)/sqrt(2),(e_1+e_2)/sqrt(2),e_3. Sie sind positiv und geordnet; m>=.08>2(.15)², also in C. Die Diagonalgewichte von F in diesem Rahmen sind 3/2,3/2,4. K_plus und K_minus sind positiv mit denselben Eigenwerten 1/4,1/3,5/12 und Spur eins.

Die beiden Zustände haben exakt dieselben Y,F,W und sämtliche initialen P_tau-Kompressionen, da P_tau J P_tau=0. Sie unterscheiden sich weder in der behaltenen Umgebung noch im aktuellen alpha. Ein Geschlossenheitsversagen kann daher nicht einer stillschweigend variierten Umgebung zugeschrieben werden.

## Exakter vollständiger Kernelkanal macht die Phase sichtbar

Seien h_minus und h_plus die exakten Schurfaktoren zwischen y_minus bzw. y_plus und y_3, berechnet mit demselben endogenen alpha. Definiere J_13=i(|1><3|-|3><1|), J_23=J. Aus Diagonalisierung des vollständigen Quellkanals folgt

Phi(J)=(h_plus-h_minus)J_13/2+(h_plus+h_minus)J_23/2,
K_plus/minus,+ = I/3 ± Phi(J)/12.

Es wird kein Ersatzkanal angenommen: Dies sind die exakten Kraus-/Schurkoeffizienten des vollen positiven Updates. F,W bleiben im ausgerichteten Sektor erhalten, Y_+ ist für beide Fasermitglieder gleich, also auch die beschriftete Projektorfamilie.

Für den reinen Witness-Projektor P_W ergibt sich die nichtverschwindende Ausgangstrennung

||P_W(K_plus,+-K_minus,+)P_W||_F=(h_plus-h_minus)/12.

Bei e=1/100 ist alpha=98101/5854501 und exakt

h_plus²-h_minus²=1642718953898217/43174166750550284>0.

Beide Faktoren sind positiv, daher ist die Trennung streng positiv. Näherungswert .00162040102819565. Damit liegen identische reduzierte Eingänge und verschiedene reduzierte Ausgänge vor: Ein deterministisches Update auf dieser Reduktion existiert auf einem Bereich, der beide Zustände enthält, nicht. Dies ist ein echtes Faser-Kriterium-Gegenbeispiel nach Abschnitt II89 für den angegebenen Kandidaten außerhalb skalarer Last. Es ist kein Widerspruch der vollständigen BFG-Dynamik und kein allgemeines Verbot anderer Reduktionen.

## Natürliche interne Ergänzung statt erfundener Reserve

Die fehlende Richtung lässt sich bereits aus den vorhandenen F-/W-Daten kovariant schreiben:

i[F,W]=(2/9)J.

Der zusätzliche reelle Skalar j=tr(i[F,W]K) unterscheidet die Faser: j(K_plus/minus)=±1/27. Gemeinsam mit den bisherigen Bilddaten erhöht er den exakten reell-linearen Rang von 8 auf 9 auf Herm(C³). Bei festgehaltener Spur entspricht dies dem Übergang von sieben sichtbaren auf alle acht affinen Kernelparameter.

Damit ist die Informationslücke im Beispiel mit nur einem zusätzlichen reellen Datum geschlossen. Die Ergänzung ist eine mathematische Beobachtungswahl aus vorhandenen BFG-Größen, kein neuer physikalischer Speicher oder Kopplungsterm. Sie ist nicht als Energie, Impuls oder konservierte Ladung identifiziert. Im vorliegenden Faserfall gilt sogar j_+=j(h_plus+h_minus)/2; der Skalar ist im Allgemeinen nicht erhalten.

Da nach Ergänzung der ganze Kernel rekonstruierbar ist und Y,F,W mitgeführt werden, ist die volle Quellfortsetzung in diesem festen Beispiel wieder bestimmbar. Dies ist eine vollständige Informationsergänzung, gerade keine neue vierdimensionale Reduktion. Minimal ist hier die Zahl eines zusätzlichen linearen Datums bei Beibehaltung der bisherigen Bilder; keine allgemeine Minimalitätsaussage für andere Koordinatensysteme wird behauptet.

## Frische Evidenz und Grenzen

PAIR_CLOSURE_PROTOCOL.md vor Auswertung auf GitHub publiziert. Exaktes rationales alpha/Schurfaktor-Zeichen, Kanalidentität, native Kommutatoridentität und Ränge 8/9 geprüft. Acht frische Original-Quellaufrufe: e=.005,.01,.02 jeweils mit K_plus und K_minus, plus zwei simultane komplexe Eichkontrollen bei e=.01. Initiale Bildergleichheit, Ausgangstrennung, volle K-Identität, F-/W-Erhaltung und gleiches Y_+ separat geprüft.

Kernelrest 3.022367231926356e-16, Rest der Ausgangstrennung 1.235990476633475e-17, Feldrest 7.483328527857331e-16, Eichrest 6.218062178924354e-16, initialer Faserrest 7.517135062566164e-19; vorab Schwelle 1e-10. Ausgangstrennungen .000805015771423544,.0016204010281956646,.003322579114163055 stimmen mit dem exakten Kanal überein. Positivität und C-Bedingung wurden kontrolliert; keine Niedrigrang-Grenztrajektorie behauptet. CI separat in CI_VALIDATION.md.

Der vorige skalare Geschlossenheitsbefund bleibt gültig und wird nicht rückwirkend umgedeutet. Die früheren speziellen Paar-Gedächtnissätze betreffen andere, ausdrücklich geschlossene Voraussetzungen und bleiben ebenfalls bestehen.

Nächste Abhängigkeit: echte geschlossene lokale Reduktion mit Quellenbegründung oder vollständige Mehrsektor-Bilanz einschließlich dieser Kohärenzen; dazu Bilanz über überlappende/wechselnde Sektoren und räumliche Beziehungen. Ein frei gewähltes Weglassen von Kommutatorinformation ist nicht als Energie-Impuls-Erhaltung zulässig. Allgemeine Trägerauswahl, räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen.
