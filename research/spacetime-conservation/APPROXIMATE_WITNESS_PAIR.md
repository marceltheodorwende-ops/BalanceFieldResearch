# Runde66: bedingte stetige Paar-Näherung mit kontrolliertem Kommutatorfehler

Präregistriert in PROTOCOL.md, Commit53cfa470da80bf3b692a5d924528c5535123a06b; Auswertung25. Oktober2026. Ausschließlich gepinnte vollständige BFG-Quelle Dynamic Order8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498 wird beim Import geprüft. Quellen sind Daten.

## Ergebnis und Kandidatenentscheidung

Die kleine-Brücken-Grenze der exakten gemeinsamen Blockregel aus Runde65 erlaubt eine konstruktive Näherungsalternative. Auf einem dreidimensionalen R-Träger lässt sich bei zwei ausdrücklich benötigten Lücken ein eindeutiger, kovarianter Paarprojektor aus dem kleinsten gemeinsamen Kommutatorfehler bestimmen. Er existiert im geprüften Brückenfall trotz fehlendem exakten gemeinsamen Rang2-Block. Seine Abweichung vom Reduzieren der Felder besitzt eine berechenbare obere Schranke.

Die Näherung wird unter gemeinsamer Retention exakt mittransportiert. Ihr Fehler wird dabei aber ebenfalls erhalten, nicht abgebaut. Ein isotroper Kontrollfall macht die neue Vorschrift mehrdeutig, obwohl dort die exakte zentrale Regel von Runde65 funktioniert. Beide Regeln sind bedingte Kandidaten, keine universelle Auswahlhierarchie.

Die nachfolgende gleichgewichtete Fehlerfunktion ist eine offengelegte zusätzliche mathematische Auswahlentscheidung aus BFG-Daten. Sie ist weder eine von der Quelle vorgeschriebene physikalische Wirkung noch ein neuer Zeitgenerator.

## Regel und Definitionsbereich

Wie zuvor R=sqrt(F)Wsqrt(F), Q=suppR und A=QFQ auf ranQ. Beschränke diese Kandidatenregel auf rankQ=3. Auf dem reellen Hilbertraum traceloser hermitescher Matrizen mit Frobeniusprodukt definiere

    L(T)=[R,[R,T]]+[A,[A,T]].

Standardmatrixalgebra liefert Selbstadjungiertheit und

    <T,L(T)>=||[R,T]||_F²+||[A,T]||_F²>=0.

Die Identität wird durch die Spurfreiheit entfernt. Sei die kleinste Eigenzahl lambda auf diesem Raum einfach, mit Abstand Delta>0 zur nächsten. Ein zugehöriges hermitesches T mit trT=0,||T||_F=1 ist dann bis auf das Vorzeichen eindeutig.

Ordne seine drei Eigenwerte t1<=t2<=t3. Falls die beiden benachbarten Abstände verschieden sind, wähle das Paar mit dem eindeutig kleineren Abstand und dessen gesamten Rang2-Spektralprojektor J. Der Abstand g zwischen dieser Paargruppe und der übrigen Mode muss positiv sein. Eine mögliche Entartung innerhalb des ausgewählten Paares ist erlaubt; einzelne Vektoren werden nicht gewählt. Bei Schluss der L-Modenlücke oder der eindeutigen Paarwahl bleibt die Regel undefiniert.

Der Vorzeichenwechsel T->-T kehrt nur die Reihenfolge um und liefert denselben näher beieinanderliegenden Zweierträger. Eine simultane unitäre Eichtransformation transportiert L,T und den ganzen Projektor; die Wahl ist daher kovariant. Auf Bereichen mit festem R-Trägerrang, Abstand seines positiven Spektrums von null, einfacher L-Mode und getrenntem T-Paarcluster ist J lokal stetig. Dies folgt aus der Stetigkeit isolierter Spektralprojektoren. Es wird kein globaler Stabilitätsradius aus einer einzelnen numerischen Lücke abgeleitet.

## Kontrollierte Abweichung vom exakten Block

Definiere den hier geprüften mathematischen Fehler

    kappa(J)=||[R,J]||_F²+||[A,J]||_F².

In einer T-Eigenbasis ist für B=R oderA

    ||[B,T]||_F²=sum_ij |B_ij|² (t_i-t_j)²,
    ||[B,J]||_F²=sum_{i,j in verschiedenen Gruppen}|B_ij|².

Jedes gruppenübergreifende |t_i-t_j| ist mindestens g. Nach Summieren beider Felder und <T,L(T)>=lambda folgt exakt

    kappa(J)<=lambda/g².

Dies ist eine Fehlergrenze der vorgeschlagenen Regel, keine Behauptung, sie minimiere kappa über sämtliche Rang2-Projektoren. Der kleinste L-Modus minimiert zunächst den Rayleighquotienten über normierte tracelose hermitesche T, nicht direkt die Projektoraufgabe.

Für den Runde65-Zeugen mit F=diag(1,4,9), W-Diagonale(3/10,3/10,2/5), W12=1/10 und W13=epsilon lautet R13=3epsilon. Der Vergleichsoperator

    T0=(diag(1,1,0)-2I/3)/sqrt(2/3)

hat Spur0 und Norm1. Seine einzige neue Kreuzkopplung gibt exakt

    <T0,L(T0)>=27 epsilon²,
    0<=lambda_min<=27 epsilon².

Bei epsilon0 ist der tracelose gemeinsame Kommutant eindimensional, die kleinste Mode einfach mit Eigenzahl0. T0 besitzt ein getrenntes Zweiercluster; der zugehörige J ist der exakte zentrale Paarblock aus Runde65. Aufgrund der Lücken existiert die Näherung daher für hinreichend kleine Störungen lokal weiter. Ein numerischer universeller epsilon-Grenzwert wird nicht behauptet. Der explizit geprüfte Wert epsilon=1/100 liegt im unten kontrollierten Definitionsbereich.

## Exakter Transport, aber keine Fehlerverbesserung

Unter gemeinsamer erfolgreicher nichtterminaler Retention gilt R_out=VRV† und A_out=VAV† auf Q_out=VQV†, V†V=P. Die Abbildung T->VTV† ist zwischen den beiden dreidimensionalen Trägerräumen eine Frobeniusisometrie und erhält Spur sowie Kommutatoren. Deshalb

    L_out(VTV†)=V L(T)V†,
    J_out=V J V†.

Alle L-Eigenzahlen, Modenlücken, T-Clusterlücken und kappa bleiben exakt konstant. Das gilt einschließlich eines Witness-leeren Seeds und auch dann, wenn der volle aktive Rang über3 wächst. Anfangsselektion oder Terminalität werden nicht als solche Retentionsschritte behandelt.

Auch tr(JR) und die im mitbewegten Paar komprimierte R-Matrix bleiben erhalten. Bei kappa>0 sind R/A aber nicht exakt durch J blockdiagonal. Der restliche Witnessinhalt und Kreuzkopplungen bleiben Teil des vollständigen Zustands. Diese interne Näherung liefert weder einen autonomen vollständigen BFG-Paarupdate noch eine Quelle dynamischer Dekohärenz oder einen räumlichen Energiefluss.

R und A haben Formationseinheiten, L und kappa entsprechende quadratische Einheiten. Ein Hamiltonian, eine Dauer in Sekunden oder physikalische Orts-/Impulskomponenten werden daraus nicht identifiziert. Andere positive relative Gewichte der beiden Kommutatorterme wären andere Kandidaten; die Quelle wählt das hier benutzte gleiche Gewicht bislang nicht physikalisch aus.

## Mehrdeutige natürliche Alternative

Für R=(3/7)I3 und F=A=diag(1,1,3) besteht der gemeinsame Kommutant aus einem M2-Block und einem Skalar. Er hat Dimension5; nach Entfernen der Identität bleiben vier tracelose Nullmoden von L. Somit ist die kleinste Mode nicht einfach und diese Näherungsregel undefiniert.

Runde65s minimale zentrale Rang2-Projektion existiert dort dennoch eindeutig. Die neue Regel ist also kein überall definierter Ersatz. Bei Lückenverlust wird keine willkürliche Nullmode ausgewählt. Der begrenzte Fehlschlag ist kein Ausschluss anderer BFG-interner Auswahlregeln.

## Frische Prüfung und Korrekturprotokoll

[APPROXIMATE_WITNESS_PAIR_CHECKS.md](APPROXIMATE_WITNESS_PAIR_CHECKS.md) enthält vollständigen Prüftext und Rohdaten. Exakt rational geprüft: L-Ränge auf dem vollen9-dimensionalen Operatorraum7/8/4 für Nullbrücke/Brücke/Isotropie, entsprechend tracelose Nullitäten1/0/4; Rayleighwert27epsilon². Fünf verschiedene Originalereignisse: Brücke und tatsächlicher Nachfolger, n4/r3-Seed-Brücke, komplexe Eichversion Seed20261116 und isotrope Mehrdeutigkeit. Alle nichtterminal.

Beim Brückenfall gilt numerisch

    lambda≈0.00229348675031 < 27/10000,
    Delta≈0.145064994129,
    g≈1.21822978358,
    kappa≈0.00153707387766 <= lambda/g²≈0.00154538897444.

Der Folgeupdate und der Seedtransport erhalten diese positiven Fehlerwerte. Aktives P wächst im Seedfall auf4, der R-Träger bleibt3. Isotropie zeigt vier numerische Nullmoden bis Rundung und korrekt keine Wahl. Maximaler L-Spektraltransportrest1.57e-13, Paarprojektorrest2.74e-15 und Eichinvariantenrest1.26e-14. Toleranz1e-10, Wurzelcutoff1e-12, Lückenprüfung1e-8; keine beliebig nahen Rang-/Moden-/Clusterschlüsse zertifiziert.

Erster lokaler Lauf PASS mit fünf Originalaufrufen. Eine zusätzliche, nicht in Assertions benutzte Koordinatenabstands-Ausgabe verglich das gewählte Paar auch nach Rahmenwechseln noch mit einer festen ursprünglichen Diagonalmatrix; sie ist dort kein kovarianter Abstandsvergleich. Diese irreführende Zusatzdiagnose wurde entfernt. Danach vollständiger frischer PASS mit unveränderten fünf Fällen/Assertions, erneut fünf Originalaufrufen; insgesamt10 Aufrufe, final5. Kein fehlgeschlagener mathematischer Kontrolllauf, keine Änderung der Quelle oder Anpassung von Eingaben zur Zielerfüllung. Die Korrektur und der erneute Lauf bleiben dokumentiert.

## Nächste Abhängigkeit und CI

Vorhanden ist eine bedingte stetige interne Paar-Auswahl mit quantitativem Reduktionsfehler. Offen sind ihre physikalische Auswahl gegenüber anderen Gewichten/Regeln, ein Schutz ihres Lückenbereichs bei nichtretentiven Ereignissen und räumliche Orts-/Uhr-/Impulsabbildungen. Die Quelle verbessert den gemessenen Näherungsfehler auf dem geprüften Retentionszweig gerade nicht; eine angenommene Relaxation wäre zusätzliche Dynamik.

Nur Forschungsdokumentation; Originaldynamik, Manuskripte, Lizenzen, empirische Ausgaben, Audit-Dateien und Workflows unverändert. Runde65-CI am Head5c8ea4f583da11859b7a065c40ea295d43316917 ist separat grün dokumentiert. Diese neue eingebettete Reproduktion bleibt lokale Evidenz, kein daraus abgeleiteter neuer Remote-CI-Pass.
