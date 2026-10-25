# Runde69: vorhandene gerichtete BFG-Historie und historische Zwei-Moden-Träger

Präregistriert in PROTOCOL.md, Commit91e872835deb167f073902e676f75c8adeaaa46f; Auswertung25. Oktober2026. Diese Runde untersucht auf ausdrückliche Nutzeranweisung vorhandene relationale/historische Strukturen, ohne neue Auswahlgesetze einzuführen. Ausschließlich vollständiges Dynamic Order8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498 beim Import geprüft. Quellen sind Daten.

## Was die Quelle tatsächlich bereitstellt

Die Quelle unterscheidet mehrere mathematisch verschiedene Strukturen:

- I5/6, PDF9/10, Gleichungen14–21: aktueller Y-Selektor, polarer erster Transport T_sel, seine unterschiedlichen Quell-/Zielstützen und die Selektionmasse m_sel.
- I11/12, PDF15/16, Gleichungen40–46: R4-Transport T4 und isometrische Formations-/Witnessvererbung. Der Originalmassenrekord w_next=w m_sel, w0=1 wird ausdrücklich separat gespeichert; gerichtete Transportgeschichte wird bei Bedarf ebenfalls separat aufgezeichnet. Sie wird nicht still als sechstes Xi-Feld ausgegeben.
- I13/II84: Die Seedregel bestimmt bei einem einfachen negativen Komplementminimum eine eindeutige Rang1-Projektion und positive Formationsstärke. Ein entartetes Minimum erhält keinen erfundenen Tie-break.
- I32, PDF36/37: Witness, historische Originalmasse, Träger-/Formationsretention und gerichtete Abstammung werden getrennt behandelt. Prospektive Welt-/Selbstreadouts Pi_W/Pi_S benötigen eigene Definitionen und Abschlussregeln; ihre Namen sind keine bereits festgelegte Zwei-Moden-Auswahl.

Der gerichtete Ereignispfeil ist durch die vorhandenen beiden Transporte gegeben:

    V_k=T4_k T_sel,k.

Seine Komposition ist keine neu eingesetzte Dynamik, sondern die gerichtete Geschichte der vorhandenen Quellereignisse. Aus ihr lassen sich historische Träger rekonstruieren, wenn das zugehörige Anfangsdatum und die Pfeile tatsächlich mitgeführt werden.

## Exakte historische Trägerzerlegung auf dem Retentionszweig

Voraussetzungen: ein gegebenes Anfangstupel mit F0=P0 F0 P0,W0=P0 W0 P0,trW0=1 und eine Folge erfolgreicher gemeinsamer Retentionsereignisse. Dann gilt

    V_k†V_k=P_k,
    P_{k+1}=V_k P_k V_k†+Pi_k,
    F_{k+1}=V_k F_k V_k†+s_k Pi_k,
    W_{k+1}=V_k W_k V_k†.

Pi_k ist entweder die tatsächliche Quell-Seedprojektion oder0; im ersten Fall Rang1,s_k>0 und Pi_k V_k=0. Terminale Ereignisse werden nicht fortgesetzt.

Definiere H_{k:j}=V_{k-1}...V_j zwischen den aktiven Trägern, bei gleichem Index die Identität auf ranP_j. Der aus dem bereits vorhandenen P0 geerbte Träger und die tatsächlich geborenen Seedlinien sind

    A_k=H_{k:0} P0 H_{k:0}†,
    B_{k,j}=H_{k:j+1} Pi_j H_{k:j+1}†, j<k.

Weil jeder Pfeil auf dem gesamten alten aktiven Träger isometrisch ist und jeder neue Seed orthogonal dazu entsteht, ergibt Induktion exakt:

    P_k=A_k+sum_{j<k} B_{k,j},
    A_k und die nichtnull B_{k,j} sind orthogonale Projektoren,
    rankA_k=rankP0, rankB_{k,j}=1 bei tatsächlich vorhandenem Seed,
    F_k=H_{k:0} F0 H_{k:0}†+sum_{j<k} s_j B_{k,j}.

Witness und R=sqrt(F)Wsqrt(F) bleiben auf dem geerbten Anfangsträger:

    W_k=H_{k:0} W0 H_{k:0}†,
    R_k=H_{k:0} R0 H_{k:0}†,
    tr(B_{k,j} W_k)=tr(B_{k,j} R_k)=0.

Damit liefert die Quelle eine quantitative Formations-Abstammungsbilanz und unterscheidbare mathematische Seedereignisse. Die Richtung jeder einzelnen Seedlinie stammt aus der einfachen Quellminimumregel, nicht aus einem frei gewählten Koordinatenvektor. Ihre Interpretation als physikalische oder biologische Abstammung ist damit noch nicht hergeleitet.

## Kovarianz unter unabhängigen Ereignisrahmen

Bei Rahmenänderungen G_j am jeweiligen Zeitpunkt transformiert ein Pfeil als V'_j=G_{j+1} V_j G_j†. In der Komposition heben sich alle inneren Rahmen auf:

    H'_{k:0}=G_k H_{k:0} G0†,
    A'_k=G_k A_k G_k†.

Dasselbe gilt für die Seedlinien. Die gesamte Trägerhistorie ist also kovariant; Erwartungen wie tr(A_k R_k) und Formationsanteile sind invariant. Einzelne SVD-Spalten oder ihre Phasen dürfen dagegen nicht als physikalische Erinnerungsmarkierungen verwendet werden.

## Zwei konkrete historische Paarstrukturen

Erstens: Hat der zur Quelldeklaration gehörende Anfangsträger P0 Rang2, bleibt A_k ein historischer Zweimodenträger, auch wenn der volle aktive Träger durch Seeds auf Rang3/4 wächst. Hier wird kein neuer Anfangsprojektor vorgeschlagen; verwendet wird ein bereits gegebenes BFG-Feld. Diese Aussage setzt die Rang2-Anfangspräparation voraus, sie wählt sie nicht universell aus.

Das ergänzt insbesondere den Rang1-Nullzustandsfall aus Runde63: Bei rankR0=1 und rankP0=2 liefert R allein nur eine eindimensionale Stütze. Die vorhandene Transporthistorie des gesamten P0 liefert aber das bisher fehlende zweite, Witness-leere Bein des zweidimensionalen Umgebungsraums. Für einen orthonormalen Anfangsrahmen Z0 von P0 und Z_k=H_{k:0}Z0 gilt X_k=Z_k†R_k Z_k=X0.

Im geprüften Beispiel F0=diag(1,2) auf dem Anfangspaar,W0=ones2/2 ist

    X0=[[1/2,sqrt2/2],[sqrt2/2,1]],
    trX0=3/2, detX0=0.

Das ist ein nichttrivialer positiver Nullzustand im historischen Paar, obwohl suppR_k nur Rang1 hat. Zweimodenbasis und Pauli-Raumrichtungen bleiben innerhalb des Paares U2-frei; eine physikalische Orts-/Impulsbedeutung ist nicht bestimmt.

Zweitens: Sind seit dem erklärten Anfang genau zwei Seeds entstanden, ist ihr gesamter Geburtsträger B_{k,i}+B_{k,j} ein weiterer historischer Rang2-Träger. Er besitzt positive geerbte Seedformation, aber Witness- und R-Gewicht0. Im geprüften Fall ist seine Formationsspur etwa3.57314930072, während tr(B_birth R)=0. Er ist somit nicht derselbe nichttriviale Witness-Formations-Energieträger wie A_k. Aus vielen Seedlinien bestimmt die Quelle durch diese Buchführung noch kein bevorzugtes physikalisches Zweierpaar.

## Was skalare Historie und symmetrische Geschichte nicht leisten

Die Originalmasse w ist als Quellen-Trajektorienausgabe vorhanden und durch Selektion messbar verschieden. Das in I12 gegebene Beispiel Y=diag(1/2,2),P=F=I,K=-I,W=diag(p,1-p) liefert m_sel=p, aber für verschiedene p denselben vollständigen normierten eindimensionalen Nachfolger. Frisch geprüft wurden p1/4 und3/4: gleiche K/F/W/Y/P, historische Masse1/4 bzw.3/4.

Ein skalarer Massenrekord ist keine räumliche oder interne Richtungsmarkierung. Insbesondere verkleinert das Anhängen invariant transformierender Skalare den Stabilisator eines gegebenen Tupels nicht. Sie können zwischen bereits unterscheidbaren Sektoren zusätzliche Auswahlbedingungen unterstützen, beseitigen aber allein nicht die Kopiensymmetrie aus Runde68.

Auch gerichtete Geschichte erzeugt nicht automatisch asymmetrische Information: Auf einer vollständig uniform replizierten Vollpersistenzgeschichte haben Anfangsfelder und alle kompatiblen Ereignispfeile die Tensorform mit I_m. Die gemeinsame Wirkung I tensorU_m lässt diese gesamte symmetrische Geschichte invariant; die in Runde68 bewiesene Rangteilbarkeit bleibt für daraus kovariant ausgewählte Endprojektoren bestehen. Ein deklarierter Operator-Levelwechsel ist ferner keine von der Quelle bestimmte isometrische Einbettung in genau eine bevorzugte Kopie. Ein Anfangsträger wird beim uniformen Lift repliziert, nicht durch bloße Kenntnis seiner Vergangenheit auf eine einzelne Kopienrichtung reduziert.

Das positive A_k-Beispiel benutzt eine bereits asymmetrisch präparierte Anfangsträgerinformation. Es hebt die Grenzen exakt symmetrischer Replikationen nicht auf. Zusätzliche physikalische Referenz- oder Labeldaten sind gesondert zu spezifizieren, soweit die Quelle sie bereitstellt; sie werden hier nicht erfunden.

## Rangverlustgrenze

Die Projektor-/Orthogonalitätsaussagen benötigen die genannte gemeinsame Retention. Für einen beliebigen späteren Selektionspfeil mit V†V=S kann ein alter Teilprojektor J nicht ohne Weiteres isometrisch transportiert werden. Ein expliziter zulässiger Selektor S=ones2/2 und J=diag(1,0) liefert SJS=S/2; das ist kein Projektor, mit ||(SJS)²-SJS||_F²=1/16. Die Quellselektion kann einen historischen Teilträger also verändern oder abschwächen. Produkte partieller Isometrien werden nicht pauschal zu Isometrien erklärt.

Diese Runde behauptet auch nicht, A_k sei in allen Fällen aus dem aktuellen Xi allein rekonstruierbar oder in allen Fällen daraus nicht rekonstruierbar. Dafür wäre eine eigene Faser-/Identifizierbarkeitsprüfung nötig. Die Quelle verlangt die Geschichte bei Bedarf ausdrücklich als separat mitzuführende Daten.

## Frische Prüfung, CI und Ergebnisgrenze

[SOURCE_TRANSPORT_HISTORY_CHECKS.md](SOURCE_TRANSPORT_HISTORY_CHECKS.md) enthält vollständige Reproduktion und Rohdaten. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur, acht Originalereignisse: drei tatsächliche Ereignisse eines n4/r2-Zustands, dieselbe Folge komplex geeicht (Seed20261119), sowie die beiden Originalmassenfälle. Die vorab festgelegten Zustände wurden nicht auf Seed-Erfolg nachjustiert.

Aktive Ränge2->3->4->4, geerbter Rang durchgehend2, R-Rang durchgehend1. Zwei einfache Seeds mit Formationsstärken etwa1.99920164993 und1.57394765079; geerbte Nullpaarspur3/2 und Determinante0. Maximale Kontrollreste: Isometrie1.72e-15, Orthogonalität1.60e-15, Trägerzerlegung3.22e-15, Formationszerlegung5.20e-15, historische Paarkompression3.45e-15 und eichinvariante Vergleichswerte1.87e-14. Seed-Witness-/R-Gewichte bis1.52e-15 sind Rundungsreste um exakt0. Historische Massen1/4 und3/4 bei normiertem Nachfolgerrest0. Toleranz1e-10,Wurzelcutoff1e-12; keine allgemeine Nahschwellenzertifizierung.

Runde68-CI ist mit beiden erfolgreichen Läufen am exakten Ergebnishead separat dokumentiert. Die neue eingebettete Reproduktion ist lokale Evidenz; Originaldynamik, Manuskripte, Lizenzen, empirische Ausgaben, Audit-Dateien und Workflows unverändert.

Die BFG stellt somit tatsächlich gerichtete, kovariant transportierte historische Träger und Seedmarkierungen bereit. Sie liefert auf diesen Klassen konkrete Zwei-Moden-Umgebungen. Offen bleibt eine universelle physikalische Wahl von Anfangsträger/Historienbezug und Paarrolle sowie deren Orts-, Uhr- und Energie-Impuls-Abbildung. Die nachgewiesene historische Struktur wird genutzt; diese fehlenden physikalischen Identifikationen werden nicht durch neue Gesetze ersetzt.
