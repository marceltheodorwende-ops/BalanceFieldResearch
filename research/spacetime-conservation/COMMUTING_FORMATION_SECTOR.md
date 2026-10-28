# Runde59: dynamisch invarianter messbarer F-Sektor ohne interne Dekohärenzauswahl

Präregistrierung PROTOCOL.md, Commit d0733fef579e92cf769a6587bd0fce4febd627eb; Auswertung 2026-10-24. Ausschließlich gepinnte BFG-Quelle: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, durch audit.load_update geprüft.

## Konstruktives Ergebnis und Grenze

Die in [Runde58](WITNESS_INSTRUMENT_INFORMATION.md) erhaltene positive Alternative ist dynamisch konsistent: Präparationen mit [W,F]=0 bleiben unter gemeinsamer BFG-Retention kommutierend, auch durch nichtterminale Seedereignisse. Eine projektive Messung ganzer F-Spektralräume kann auf dieser eingeschränkten Familie informativ sein und den unbeobachteten Witness-Nachfolger unverändert lassen. Sie ist daher ein mathematisch zulässiger wiederholt messbarer Energiesektor unter der zusätzlichen Identifikation rho_Q=W,H proportionalF.

Die Quelle wählt diesen Sektor jedoch nicht durch Abbau vorhandener F-Kohärenz aus: sowohl die Frobeniusnorm des Kommutators als auch der Abstand zum spektral gepinchten Witness bleiben im geprüften Retentionszweig exakt erhalten. Das ist eine lokale Aussage über die benannte Witness-/F-Struktur, kein allgemeines Verbot von Dekohärenz durch zusätzliche Messkopplungen, andere Zustandsbrücken oder anfängliche Auswahlverluste.

## Exakte Identität aus demselben BFG-Update

Voraussetzungen wie Runde51: nichtterminales Ereignis, gemeinsame Retention der unterstützten positiven W,F, trW=1. In der nach dem ersten erfolgreichen Ereignis verfügbaren Q=I-Klasse gilt mit V=T4 Tsel

    V†V=P, VV†=S4,
    W_out=V W V†,
    F_out=V F V†+s Pi_seed,
    Pi_seed S4=0.

Ohne Seed setzt man s Pi_seed=0. Aus der Witness-Orthogonalität folgen

    W_out Pi_seed=Pi_seed W_out=0,
    [W_out,F_out]=V[W,F]V†.

Der Eingangskommutator ist auf P unterstützt; die Abbildung ist auf diesem Träger isometrisch. Somit

    ||[W_out,F_out]||_F²=||[W,F]||_F².

Dasselbe gilt für die nichtnull singulären Werte und damit für jede Schattennorm dieses Kommutators; zusätzliche Nullräume ändern sie nicht. Insbesondere ist [W,F]=0 ein invarianter Sektor, ein strikt positiver Kommutatorrest wird auf diesem Zweig nicht dissipiert.

Die Kommutatornorm hat die Formationseinheit von F (W dimensionslos) und ist nicht als physikalischer Impuls definiert. Eine nachträgliche Normierung durch wachsende trF könnte relative Werte verkleinern, ohne diese absolute Identität zu ändern; das wäre eine andere Größe.

## Spektrale Kohärenz und entartete F-Räume

Schreibe Pi_lambda(F) für den gesamten Eigenraum zum Wert lambda und

    D_F(W)=sum_lambda Pi_lambda(F) W Pi_lambda(F).

Es werden keine willkürlich gewählten Basislinien innerhalb entarteter Eigenräume gemessen. D_F(W)=W gilt genau bei [W,F]=0; Kohärenzen innerhalb desselben entarteten F-Blocks sind erlaubt und werden nicht entfernt.

Der Quellenfunktionalkalkül transportiert die alten F-Eigenräume mit V. Falls ein Seedwert mit einem alten Eigenwert kollidiert, wird der entsprechende Eigenraum um die orthogonale Seedrichtung erweitert. Da diese Richtung und ihre Kreuzterme in W_out exakt Witnessgewicht0 haben, bleibt trotzdem

    D_Fout(W_out)=V D_F(W) V†.

Daraus folgt als stärkeres spektrales Distanzkorollar

    ||W_out-D_Fout(W_out)||_F=||W-D_F(W)||_F.

Die nichtkommutierende Witness-Präparation nähert sich daher in dieser spektralen Dephasierungsdistanz nicht dem kommutierenden Sektor an. Das folgt algebraisch und hängt nicht von der numerischen Clusterwahl der Kontrollrechnung ab.

Die Aussagen gelten nicht automatisch für verlustbehaftete anfängliche Selektion: dort können Projektion und Witnesskonditionierung die Kommutator-/Kohärenzstruktur ändern. Auch die Quelle kann terminal enden; es wird kein Nachfolger erfunden.

## Informativ messbarer invarianter Sektor

Für festes F und seine Spektralprojektoren ist das Quellen-nachgeschaltete mathematische Instrument

    I_lambda(W)=V Pi_lambda W Pi_lambda V†,
    p_lambda=tr(W Pi_lambda).

Auf der gesamten kommutierenden Präparationsfamilie gilt

    sum_lambda I_lambda(W)=V W V†=W_out.

Bei p_lambda>0 ist der bedingte Eingangszustand W_lambda=Pi_lambda W Pi_lambda/p_lambda. Er ist positiv, normiert, F-kommutierend und auf dem entsprechenden F-Wert unterstützt. Die BFG-Retention transportiert ihn in den alten F-Ausgangswert lambda; Seedrichtungen liefern kein neues Witnessgewicht. Die schon in Runde51 erhaltene Witness-gewichtete F-Spektralverteilung gibt die unveränderten p_lambda einschließlich entarteter/collidierter Werte. Bei weiteren nichtterminalen Retentionsereignissen bleibt diese Struktur erhalten.

Damit ist wiederholte Messung derselben F-Energie mathematisch konsistent: nach einer selektiven Auslese lambda bleibt derselbe Wert bei erneuter Auslese erhalten. Unbeobachtet bleibt das kommutierende Gemisch unverändert. Eine einzelne selektive Messung verändert im Allgemeinen den bekannten Gemischzustand zu W_lambda; universelle Zustandsunverändertheit jedes einzelnen Outcomes wird nicht behauptet.

Das widerspricht dem Rang1-Instrumentsatz aus Runde58 nicht: dort wurde Gleichheit des Gesamtkanals auf ALLEN Witness-Präparationen gefordert. Hier stimmt das Spektralinstrument nur auf dem kommutierenden Sektor mit der Quelle überein. Es ist keine neue universelle Instrumentzerlegung des ursprünglichen Witnesskanals.

Die so erhaltenen Energiegewichte und Werte bleiben auf diesem geschlossenen Zweig konstant. Daraus folgen weder physikalische Übergangsraten noch Emission/Absorption, Arbeitskopplung oder ein räumlicher Energiestrom. Eine solche Interaktionsdynamik müsste gesondert aus einer begründeten Brücke hervorgehen.

## Exakte und frische Originalkontrollen

[COMMUTING_FORMATION_SECTOR_CHECKS.md](COMMUTING_FORMATION_SECTOR_CHECKS.md) enthält vollständigen Code und Rohdaten. Symbolisch: F=diag(1,3), W=[[1/2,1/4],[1/4,1/2]] ergibt exakt ||[W,F]||_F²=1/2.

Ein frischer lokaler Lauf mit6 Originalereignissen PASS ohne Fehlvorlauf/Korrektur. Rationaler Seedhintergrund:

    P=diag(1,1,0), F=diag(1,.42,0), K=-diag(1,2,3),
    Y=[[.25,0,.1],[0,.5,.1],[.1,.1,.5]].

Verglichen wurden ein kommutierender Witness diag(.6,.4,0), ein Witness mit gleichen Diagonalen und Kohärenzen W12=.1i,W21=-.1i sowie dessen komplexe simultane Eichversion (Seed20261109), je2 vollständige Ereignisse. Die erste Seedreclosure erweitert den aktiven Träger auf Rang3; die zweite volle Persistenz bewahrt die Ergebnisse.

- Kommutierender Fall: Kommutatornorm² numerisch ungefähr1e-31, Messinstrument-Abweichung vom Quellen-Witness maximal1.90e-15.
- Kohärenter Fall: Kommutatornorm²0.006728 bleibt über beide Ereignisse erhalten; Messinstrument-Abweichung0.1414213562 bleibt ungleich0.
- Maximaler Kommutatortransportrest4.11e-16; komplexer Eichrest der Norm²6.94e-18.
- Witness-gewichtete F-Momente1..3 stimmen vor/nach jedem Ereignis bis1.23e-15 überein.

Numerische Spektralräume wurden mit Clustertoleranz1e-9 als ganze Blöcke behandelt. Diese Toleranz zertifiziert keine nahezu entarteten Fälle; die exakten Spektral-/Seedkollisionsaussagen folgen aus der algebraischen Identität. Die numerischen Werte sind Implementierungsevidenz, kein Ersatz für den allgemeinen Beweis.

## Nächste konkrete Abhängigkeit

Es gibt jetzt eine positiv beschriebene, quellenstabile Präparations-/Messklasse. Offen ist, ob eine unabhängig begründete physikalische Präparation gerade diese Klasse auswählt, wie Messapparat/Interaktion sie realisiert und ob eine zusätzliche räumliche/Uhr-/Generatorbrücke daraus Energie und Impuls macht. Das unveränderte Retentionsupdate liefert in der geprüften Witness-/F-Struktur keinen Mechanismus, der beliebige kohärente Präparationen automatisch in diese Klasse führt.

Nur Forschungsdokumentation; ursprüngliche Manuskripte, Grundgleichungen, Lizenzen und empirische Ergebnisse unverändert, keine Audit-/Workflowänderung und kein neuer Remote-CI-Pass.
