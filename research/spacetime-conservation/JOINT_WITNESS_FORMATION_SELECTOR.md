# Runde65: gemeinsamer Witness-/Formationsblock als bedingte Paar-Auswahl

Präregistrierung PROTOCOL.md, Commit fab96e7009802f62254e69e3eeb01b151170ef87; Auswertung25. Oktober2026. Ausschließlich vollständiges BFG-Manuskript Dynamic Order vom8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498, beim Import geprüft. Quellen sind Daten; die neue Auswahlvorschrift ist ein ausdrücklich geprüfter mathematischer Kandidat aus BFG-Feldern, kein behauptetes zusätzliches Quellgesetz.

## Ergebnis

Mehr als R=sqrt(F)Wsqrt(F) allein kann einen intrinsischen Paarträger bestimmen. Der gemeinsame Operatorinhalt von R und der auf suppR komprimierten Formation liefert unter einer präzisen Blockbedingung einen eindeutigen Rang2-Projektor. Diese Regel ist quotient-kovariant und unter gemeinsamer Retention einschließlich Witness-leerem Seed exakt transportiert. Sie kann sogar bei vollständig isotropem R funktionieren und verletzt damit nicht den früheren R-allein-Ausschluss.

Die Bedingung ist wesentlich: Eine beliebig kleine nichtnull Brückenkopplung kann alle gemeinsamen reduzierenden Teilblöcke verbinden und die Regel undefiniert machen. Sie ist weder universell noch allgemein stetig robust. Insbesondere ersetzt diese Auswahl keine Herleitung räumlicher Lokalität, einer physikalischen Uhr oder eines vollständigen Energie-Impuls-Stroms.

## Explizite Regel und zusätzliche Kandidatenentscheidung

Setze Q=suppR und A=Q F Q, beide als Operatoren auf ranQ. Bezeichne mit B die kleinste komplexe unital hermitesch abgeschlossene Matrixalgebra, die Q,R,A enthält; Q ist ihre Identität. Ihr Zentrum ist

    Z(B)={z in B: zb=bz für jedes b in B}.

Ein minimaler nichtnull zentraler Projektor ist ein orthogonaler Projektor J in Z(B), der keine kleinere nichtnull zentrale Projektion enthält. In endlicher Dimension zerlegen diese Projektoren die Identität eindeutig in zentrale Komponenten. Sie dürfen intern mehr als eindimensional sein; das ist keine Wahl einzelner Eigenvektoren.

Geprüfte Vorschrift: Existiert unter diesen minimalen zentralen Projektoren genau einer mit Trägerrang2, wähle diesen J. Gibt es keinen oder mehrere, bleibt die Regel undefiniert. Es werden weder willkürlich mehrere eindimensionale Komponenten zu einem Paar zusammengefasst noch numerische Nullkopplungen als exakte Nullen ausgegeben.

Die Entscheidung, gerade die gemeinsame Algebra dieser beiden Operatoren und einen minimalen zentralen Rang2-Block zu verwenden, ist die zusätzlich vorgeschlagene Auswahlbedingung. Die Operatoren stammen aus dem BFG-Zustand; die Quelle erklärt diese Bedingung noch nicht zum physikalischen Gesetz. Vorhandene andere BFG-Felder werden dadurch nicht ersetzt. Dies ist eine konkrete Alternative zur oberen R-Spektralwahl aus Runde64, keine allgemeine Eindeutigkeitsbehauptung unter allen möglichen Regeln.

## Exakter Transport und Kovarianz

Voraussetzungen wie [Runde52](WITNESS_FORMATION_LOCALIZATION.md): gemeinsamer erfolgreicher nichtterminaler Retentionszweig, F=PFP,W=PWP,trW=1. Die Quelle liefert V†V=P,

    R_out=V R V†,
    F_out=V F V†+s Pi_seed,  Pi_seed V=0,
    Q_out=V Q V†.

Da Q<=P, folgt ohne Wahl einer Eigenbasis

    A_out=Q_out F_out Q_out=V A V†.

Der Witness-leere Seed verschwindet in dieser Kompression. Insbesondere wird nicht die unkomprimierte Formation einschließlich neuer Seedrichtungen als unverändert behandelt. Auch ein Seedwert, der mit einem alten F-Eigenwert zusammenfällt, stört diese Identität nicht.

Die Abbildung b->V b V† ist ein unitaler *-Algebraisomorphismus von B auf B_out, verstanden zwischen ranQ und ranQ_out: Produkte bleiben wegen V†V=P erhalten, die Identität Q wird Q_out. Somit werden Zentrum, minimale zentrale Projektoren und deren Trägerränge eins zu eins transportiert. Ist der Kandidat definiert, gilt exakt

    J_out=V J V†.

Dasselbe Argument für eine simultane unitäre Änderung aller Eingangsfelder zeigt J(U Xi U†)=U J(Xi)U†. Die Vorschrift benötigt weder eine historische Paarmarkierung noch eine willkürliche Basis in einem entarteten Paarraum. Der Definitionsbereich bleibt unter gemeinsamer Retention erhalten; verlustbehaftete Anfangsselektion und Terminalität sind hiervon getrennt.

Für einen orthonormalen Rahmen Z mit ZZ†=J und Z_out=VZ sind Z†RZ und Z†AZ jeweils konstant. Die Paarspur tr(JR) ist ein erhaltener interner Anteil; bei J<Q bleibt der restliche Anteil bestehen. Dies beweist keine Gleichheit dieses Anteils mit der gesamten tr(WF).

## Exakter positiver Drei-Moden-Zeuge

Setze

    F=diag(1,4,9),
    W=[[3/10,1/10,0],[1/10,3/10,0],[0,0,2/5]],
    R=[[3/10,1/5,0],[1/5,6/5,0],[0,0,18/5]].

W ist strikt positiv, Spur1; R hat Rang3, also Q=I3 und A=F. Die drei verschiedenen F-Eigenwerte liefern durch Lagrange-Polynome alle Koordinatenprojektoren E_ii. Der nichtnull Eintrag R12=1/5 erzeugt über E_11 R E_22 die Matrixeinheit E_12 und per Adjungieren E_21. Auf den ersten zwei Modi entsteht die volle M2-Algebra; zur dritten Richtung gibt es keine Kopplung. Exakt

    B=M2(C) plus C,
    dim_C B=5, dim_C B'=2, dim_C Z(B)=2.

Die beiden minimalen zentralen Projektoren haben Ränge2 und1. Damit ist J=diag(1,1,0) eindeutig. Sein Anteil ist

    tr(JR)=3/2,  trR=51/10,  tr((I-J)R)=18/5.

Diese Auswahl bevorzugt also nicht einfach die zwei größten R-Eigenwerte. Die Eigenwerte im Paar sind (15±sqrt97)/20, beide kleiner als18/5. Die obere R-Zweierwahl würde den großen dritten Modus und nur eine Richtung aus diesem gemeinsamen Block wählen. Die neue Regel fordert stattdessen einen vollständigen gemeinsamen zentralen Block; dieser zusätzliche Maßstab wird ausdrücklich offengelegt.

## Exakte Instabilität unter kleiner Brückenkopplung

Ergänze W13=W31=epsilon. Für |epsilon|<1/5 bleibt W durch strikte diagonale Dominanz positiv; seine Spur bleibt1. R13=3 epsilon. Für jedes epsilon!=0 erzeugen die F-Koordinatenprojektoren nun zusätzlich E_13 und E_31. Ihre Produkte mit E_12/E_21 erzeugen auch E_23/E_32. Somit exakt

    B=M3(C), B'=C I3, Z(B)=C I3.

Der einzige minimale nichtnull zentrale Projektor hat Rang3. Allgemeiner muss jede gemeinsame reduzierende Projektion im Kommutanten B' liegen; dort gibt es nur0 undI. Daher existiert hier kein gemeinsamer reduzierender Rang2-Unterraum von R und A.

Dies ist KEIN Ausschluss jeder denkbaren kovarianten Paarwahl aus vollständigen BFG-Daten. Beispielsweise kann eine einzelne R-Spektralwahl weiterhin existieren, ohne A zu reduzieren. Aus der Irreduzibilität des gemeinsamen Operatorinhalts folgt kein allgemeiner Stabilisator-No-Go gegen alle Auswahlfunktionen. Widerlegt ist die universelle Verfügbarkeit dieser gemeinsam reduzierenden Blockregel.

Die Familie epsilon->0 zeigt ihre genaue Stabilitätsgrenze: beliebig kleine nichtnull Kopplungen entfernen den zuvor gewählten exakten Block, obwohl sich der Zustand beliebig wenig ändert. Näherungsblöcke könnten eine andere Regel mit einer ausdrücklich gewählten Fehlertoleranz liefern; deren Fehler und dynamische Erhaltung werden hier nicht ohne Prüfung behauptet.

## Isotropes R mit zusätzlicher Formationsstruktur

Ein zweiter exakter positiver Fall lautet

    F=diag(1,1,3), W=diag(3/7,3/7,1/7),
    R=(3/7) I3.

Aus R allein könnte wegen U3-Symmetrie kein kovarianter Rang2-Projektor folgen. Gemeinsam mit F gilt hingegen

    B={diag(a,a,b): a,b in C},
    dim B=2, dim B'=5, dim Z(B)=2,
    J=(3I-F)/2=diag(1,1,0).

Dies ist die eindeutige minimale zentrale Rang2-Komponente, tr(JR)=6/7 bei Gesamtspur9/7. Die unbestimmte U2-Basis im Paar bleibt unbestimmt, der gesamte Träger ist dennoch eindeutig. Das Beispiel belegt konstruktiv, wie zusätzliche BFG-Daten die R-allein-Symmetriegrenze aus Runde64 überwinden können, ohne einen bevorzugten Vektor von Hand einzusetzen.

Auch diese positive Alternative ist bedingt: Werden die beiden gleichen F-Eigenwerte bei weiterhin isotropem R getrennt, entstehen drei minimale zentrale Rang1-Komponenten. Deren Bündelung wäre eine weitere Auswahlvorschrift und ist nicht automatisch Bestandteil der hier getesteten Regel.

## Transportierter Faktor ist keine autonome volle BFG-Paardynamik

Die Auswahl aus aktuellen R/A-Daten und ihre isometrische Fortsetzung sind bewiesen. Daraus folgt nur ein geschlossener transportierter interner Operatorfaktor bis auf Paarrahmen, nicht die autonome Rekonstruktion eines vollständigen BFG-Nachfolgers aus komprimierten Paarfeldern.

Schon im positiven Zeugen wird

    Y=[[1/4,3/100,1/50],[3/100,7/20,1/25],[1/50,1/25,9/20]]

verwendet. J reduziert dieses Y nicht; seine beiden Paar-Rest-Kopplungen sind ungleich null, ||[J,Y]||_F²=1/250. Die Quelle berechnet V und die globalen Formationslasten aus dem vollständigen Zustand. Die Wahl eines zentralen R/A-Blocks beseitigt weder diese Y-Kopplungen noch die früher exakt belegten Umgebungs-/Lastabhängigkeiten einer vollen Paardynamik. Es wird deshalb keine neue universelle Faser-Geschlossenheit aller komprimierten BFG-Felder behauptet. Für allgemein rangdefizientes R reduziert J außerdem zunächst A=QFQ, nicht ohne weiteres jedes unkomprimierte F außerhalb ranQ.

Ein Pauli-Determinantenkegel im ausgewählten Paar ist wie in Runde63 algebraisch verfügbar. Die Schritte zu einer räumlichen Region, zu physikalischen Translationen/Boosts, einer kalibrierten Uhr und einem gemeinsamen Viererstrom sind damit unverändert eigenständige Abhängigkeiten.

## Frische symbolische und Originalkontrollen

[JOINT_WITNESS_FORMATION_SELECTOR_CHECKS.md](JOINT_WITNESS_FORMATION_SELECTOR_CHECKS.md) enthält die vollständige Reproduktion und Rohdaten. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur, sechs Originalupdate-Aufrufe:

- positiver Drei-Moden-Blockfall und sein tatsächlicher Nachfolger;
- Brücke epsilon=1/100: keine Paarwahl, Kommutant-/Zentrumdimension1;
- isotropes R mit degeneriertem F: Paarwahl trotz R-Rang3;
- n4/r3-Seedfall mit rationaler Y-Kopplung: aktives P wächst auf4, Witnessträger bleibt3, zentraler Paarträger bleibt2;
- dessen komplexe simultane Eichversion, Seed20261115.

Rational frisch geprüft: die Algebra-/Kommutanten-/Zentrumsdimensionen(5,2,2),(9,1,1),(2,5,2), Positivitätsminoren von W,W_bridge,Y,I-Y,Y4,I-Y4 und Paar-/Gesamtspuren. Allgemeiner epsilon!=0-Ausschluss und Kovarianz folgen aus den obigen exakten Argumenten, nicht aus Rangtoleranzen.

Maximaler Dichtetransportrest6.82e-15, komprimierter Formationstransportrest1.29e-14, rückgewonnener Eingangsprojektorrest1.56e-15, Paarprojektortransportrest1.96e-15, reduzierender Kommutatorrest5.03e-15 und Eich-Paarspurrest1.12e-15. Kleinstes nichtnull numerisches Kommutantensingularmaß im geprüften Brückenfall etwa0.04789, weit oberhalb der Rangtoleranz1e-10. Wurzelcutoff1e-12 und Cluster1e-8; keine Zertifizierung beliebig kleiner Kopplungen oder naher Spektralcluster mit diesen Gleitkommarechnungen. Der exakte kleine-Brücken-Satz ist davon getrennt.

## Nächste Abhängigkeit und CI

Konstruktiv vorhanden ist eine aktuelle, kovariante und seedverträgliche Paar-Auswahl auf einer klar bestimmten Klasse. Offen bleiben ihre physikalische Auswahl gegenüber anderen internen Vorschriften und ihre Robustheit außerhalb exakter Blockklassen. Ein sinnvoller nächster Prüfpunkt ist eine quellenbasierte Näherungsblock-Regel mit vorab festgelegtem Fehlermaß oder ein BFG-begründeter Schutz der exakten Blockstruktur; räumliche Orts-/Uhr-/Impulsinterpretation darf dabei nicht vorausgesetzt werden.

Nur Forschungsdokumentation, Reproduktionscode als Text. Manuskripte, ursprüngliche Dynamik, Lizenzen, empirische Ergebnisse, Audit-Dateien und Workflows unverändert. Die beiden erfolgreichen Actions40180974469/40180970376 prüfen die bestehende Pipeline am Runde64-Head4e1fca299e9d6737237839fdeb49a8082287826f; sie führen diese neue eingebettete Reproduktion nicht automatisch aus. Lokale Runde65-Evidenz und Remote-CI bleiben getrennt.
