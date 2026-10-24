# Runde53: Präparationsaffinität und Grenze strikter Teilträgerenergie

Präregistrierung: PROTOCOL.md, Commit d014fa31557ca5413e48b0d6390c588e8280a096; Auswertung 2026-10-24. BFG-Quelle unverändert: vollständiges Dynamic-Order-Manuskript 8. Oktober 2026, Parts I/II, Quellencommit 457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498; audit.load_update prüft seine gepinnte Identität.

## Status des Prüfkriteriums

BFG liefert die Witness-Formationspaarung und ihren internen Transport aus [Runde51](WITNESS_FORMATION_ENERGY.md) und [Runde52](WITNESS_FORMATION_LOCALIZATION.md). Die statistische Identifikation rho_Q=W ist eine dort benannte Quantenbrücke, keine hier nachgewiesene physikalische Tatsache. Unter dieser zusätzlichen Interpretation gilt folgendes operationales Kriterium: Bei festem F, festem Effektcover und fester Messvorschrift soll eine lokale Erwartung affin von der statistischen Präparation W abhängen. Das ist Standardmathematik einer zustandsunabhängigen linearen Observablenablesung; es wird nicht rückwirkend als neues BFG-Gesetz eingesetzt. Wenn W stattdessen ein ontischer Zustand mit nichtstatistischer Mischung ist oder das Instrument mit W variiert, trifft diese Ausschlussklasse nicht ohne Weiteres zu.

## Bedingte Auswahl zwischen den beiden Kandidaten

Für R_F=sqrt(F) W sqrt(F) ist

    q_F(E,W)=tr[E R_F]=tr[W H_E],
    H_E=sqrt(F) E sqrt(F).

Damit ist die Ablesung affin in W, positiv für E>=0 und bei Sum E_a=I gilt Sum H_a=F. Im gemeinsamen aktiven Träger ersetzt P die Identität. H_E hängt von F und E ab, nicht von W. Für mitbewegte E'_a=V E_a V† liefert derselbe Quellenfunktionalkalkül H'_a=V H_a V†; der orthogonale Seed hat keinen Beitrag. Dies nutzt dieselben Retentionsbedingungen wie Runde52, nicht eine beliebige anfängliche Rangverlustselektion.

Für R_W=sqrt(W) F sqrt(W) ist die lokale Paarung nicht allgemein affin. Exakt:

    F=diag(1,3), E=diag(1,0),
    W±=(I±sigma_x)/2, W0=(W++W-)/2=I/2.
    q_W(E,W+)=q_W(E,W-)=1,
    q_W(E,W0)=1/2.

Die gemittelte lokale Energie wäre1, die Ablesung der gemischten Präparation ist aber1/2. Dagegen liefert q_F in allen drei Fällen1/2. Die globale Energie tr(WF)=2 bleibt bei allen drei Zuständen affin und gleich; das Gegenbeispiel betrifft ausschließlich die lokale Vorschrift. Alle drei W sind zulässige positive normierte Witness-Zustände, einschließlich reiner Präparationen.

Das zusätzliche Kriterium bevorzugt also R_F gegenüber R_W für eine feste lineare Energieablesung. Es beweist keine Eindeutigkeit unter allen denkbaren positiven affinen Lokalisierungsvorschriften und bestimmt noch kein physikalisches Effektcover oder Messinstrument.

## Exakter Satz zur strikten orthogonalen Lokalität

Seien Pi_a orthogonale Projektoren mit Sum Pi_a=I und F>=0. Gesucht seien feste positive Observablen H_a mit

    H_a=Pi_a H_a Pi_a,   Sum H_a=F.

Solche Observablen existieren genau dann, wenn [F,Pi_a]=0 für jedes a. In diesem Fall sind sie eindeutig H_a=Pi_a F Pi_a.

Beweis (Standardmatrixalgebra): Die Summe von strikt unterstützten H_a hat keine Offdiagonalblöcke Pi_a F Pi_b für a!=b. Somit ist F blockdiagonal. Umgekehrt summieren sich die positiven Kompressionen eines blockdiagonalen F zu F; Multiplikation der Summenidentität von links und rechts mit Pi_a zeigt die Eindeutigkeit. Der notwendige Blockdiagonalschritt braucht nicht einmal Positivität. Eine Forderung Sum tr(W H_a)=tr(WF) für alle positiven normierten W ist äquivalent zu Sum H_a=F, da solche Zustände Hermitesche Operatoren trennen.

Dagegen ist H_a=sqrt(F)Pi_a sqrt(F) stets positiv, affin und additiv, aber im Allgemeinen nicht strikt auf Pi_a unterstützt. Konkreter voller BFG-Zustand:

    F=2I+sigma_x, Pi_1=diag(1,0), Pi_2=I-Pi_1.
    H_1=[[1+sqrt(3)/2,1/2],[1/2,1-sqrt(3)/2]].

Der untere Diagonaleintrag ist positiv und ungleich null, obwohl Pi_1 ihn ausschließt. Für W±=(I±sigma_x)/2 sind beide lokalen Witnessblöcke identisch (je Diagonalgewicht1/2), während tr(W+ F)=3 und tr(W- F)=1. Eine additive Zuordnung, die für festes F nur die jeweiligen diagonal lokalen Witnessblöcke liest, kann beide Gesamtwerte nicht unterscheiden. R_F tut dies durch seine kohärenzsensitive, räumlich noch nicht interpretierte Ablesung: q_1(W+)=3/2, q_1(W-)=1/2.

Dies schließt nur strikt getrennte orthogonale Blockenergien für alle Präparationen bei kohärentem F aus. Wechselwirkungs-/Bindungsbeiträge, überlappende Effekte, kohärente lokale Algebren oder eingeschränkte Präparationen sind damit nicht ausgeschlossen. Der Satz ist keine allgemeine Widerlegung lokaler physikalischer Energie. Er zeigt genau, welche zusätzlich gewählte Lokalitätsdefinition nicht mit vollständiger additiver F-Energie vereinbar ist.

## Frische Prüfung und nächster Schritt

[PREPARATION_LOCALITY_CHECKS.md](PREPARATION_LOCALITY_CHECKS.md) enthält vollständigen Reproduktionscode und Rohdaten. Symbolisch wurden Mischungswerte, explizites H_1 und Kohärenzenergien geprüft. Fünf vorab festgelegte Originalereignisse mit K=-I, Y=diag(0.2,0.3), P=I waren alle nichtterminal: drei Mischungspräparationen bei F=diag(1,3), zwei Kohärenzpräparationen bei F=2I+sigma_x. Ein Lauf, PASS, keine Fehlvorläufe. Erwartungs- und mitbewegte Observablentransportreste in diesen Fällen numerisch0; dies ist keine Genauigkeitsgarantie außerhalb dieser Stichprobe. Die allgemeinen Aussagen folgen aus den exakten Rechnungen.

Als nächstes muss eine unabhängig begründete BFG-interne Präparations-/Messbrücke festlegen, ob W tatsächlich statistische Zustände bezeichnet und welche Effekte physikalische Regionen bzw. zugängliche lokale Algebren sind. Bei kohärentem F müssen eventuell nichtlokale Bindungs-/Wechselwirkungsbeiträge ausdrücklich mitgeführt werden; sie werden hier nicht erfunden. Erst danach ist ein räumlicher Fluss mit physikalischer Uhr, Impuls- und Translationsgeneratorrolle prüfbar. Ein mitbewegtes algebraisches Cover allein ist weiterhin keine Raumzeit.

Nur Forschungsdokumentation; keine Änderung an Manuskript, Grundgleichungen, empirischen Ergebnissen, Audit oder Workflow. Lokaler PASS ist kein neuer Remote-CI-Pass.
