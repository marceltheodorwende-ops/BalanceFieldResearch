# Runde68: vollständige BFG-Tupelsymmetrie und Rangregel des Tensorlifts

Präregistrierung PROTOCOL.md, Commit68e99e4af6ecff6e4670e26dac7048bc492cc736; Auswertung25. Oktober2026. Verwendet werden vorhandene BFG-Strukturen: Quellgleichung163 und Theorem8 (II90.1, PDF80) zusammen mit unitärer Quotienten-/Kovarianzstruktur II85. Keine neue Auswahlfunktion. Vollständige Quelle Dynamic Order8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370; PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498 vor Import geprüft. Quellen sind Daten.

## Ergebnis und genauer Auswahlbereich

Der uniforme Quell-Tensorlift bewahrt eine gemeinsame Kopiensymmetrie ALLER fünf aktuellen BFG-Felder, nicht nur des Witness-Formationsoperators. Daraus folgt eine exakte Rangregel: Jeder ausschließlich aus diesem aktuellen endlichen Tupel kovariant bestimmte orthogonale Projektor muss einen durch die Kopienzahl m teilbaren Rang besitzen.

Für m>=3 kann daher kein solcher aktueller Rang2-Projektor ausgewählt werden. Für m=2 ist Rang2 möglich als ganzer replizierter Basis-Rang1-Sektor. Nichtuniforme bzw. reine tau können andere Ränge zulassen; diese positiven Alternativen werden konkret geprüft. Das Ergebnis ist eine Grenze einer bestimmten aktuellen Zustandsauswahl und keine allgemeine Widerlegung der BFG, ihrer Hierarchie oder möglicher Orts-/Historienbrücken.

## Gemeinsamer Stabilisator der vollständigen Quelle

Für tau=I_m/m ist der in Gleichung163 definierte Zustand

    K_m=K tensor I_m, F_m=F tensor I_m/m,
    W_m=W tensor I_m/m, Y_m=Y tensor I_m,
    P_m=P tensor I_m.

Für jedes U in U(m) lässt G=I_n tensor U daher jedes dieser fünf Felder unverändert. Dies gilt unabhängig davon, ob die Basisfelder selbst untereinander kommutieren. Insbesondere kann ein nichtkommutierender Witness das Kopienlabel in diesem Zustand nicht unterscheiden.

Sei J(Xi) eine aus dem aktuellen Tupel allein bestimmte orthogonale Projektion mit der geforderten Kovarianz

    J(H Xi H†)=H J(Xi) H†.

Für den gemeinsamen Stabilisator G ist das Argument links unverändert. Somit muss J=GJG† für alle U gelten. Schreibe J in n mal n Basisblöcken mit jeweils m mal m Kopienmatrizen. Jeder Block muss mit allen U(m) kommutieren; diagonale Phasen beseitigen Offdiagonaleinträge, Permutationen machen die Diagonaleinträge gleich. Daher exakt

    J=J0 tensor I_m.

Hermitizität und J²=J erzwingen J0†=J0 und J0²=J0. Also

    rankJ=m rankJ0.

Dies ist eine notwendige Bedingung, keine Garantie einer eindeutigen J0-Auswahl. Weitere Symmetrien der Basisfelder können stärker einschränken. Der Beweis benutzt den gemeinsamen Stabilisator des vollständigen Xi; zusätzliche Nutzung von K,F,W,Y oderP kann diese konkrete Kopiensymmetrie nicht brechen, solange diese Felder den angegebenen uniformen Lift besitzen.

## Erhaltung durch das vollständige Quell-Update

Theorem8 besagt auf P=I,0<Y<I,F!=0, dass der vollständige Nachfolger des Lifts wieder der Lift des Basisnachfolgers ist, bis zur Tensor-/Quotientenidentifikation. Deshalb besitzt er erneut die gleiche Kopiensymmetrie. In einem anderen SVD-Rahmen wird die Gruppe mittransformiert; sie wird nicht durch Wahl einzelner SVD-Eigenvektoren beseitigt.

Die untenstehenden Kontrollen bringen alle fünf Originalnachfolger mit der vom Update gelieferten v-Isometrie in den Eingangs-Tensorrahmen zurück. Dort wird derselbe gemeinsame Stabilisator vor und nach dem Ereignis geprüft. Weder ein willkürlicher Abgleich entarteter Eigenvektoren noch bloße Erhaltung einer Spur genügt als Ersatz.

Bei einer Folge uniformer deklarierter Levelwechsel mit Gesamtkopienzahl M ist die entsprechende Gruppierung der Kopienfaktoren zulässig; alle aktuellen Felder sind Basisfelder tensor I_M, F/W zusätzlich skaliert. Dann muss der Rang eines Xi-allein kovarianten Projektors durch M teilbar sein. Insbesondere bestimmt die in II90.3 illustrierte uniforme Vierfachreplikation aus diesen aktuellen endlichen Matrizen allein kein intrinsisches Paar. Die dort zusätzlich deklarierte geometrische Einbettung ist von diesen Zustandsmatrizen getrennt zu behandeln.

## Nichtuniforme und reine tau: vorhandene positive Alternativen

Schreibe tau=sum_j t_j Pi_j mit verschiedenen Eigenwerten t_j und Multiplizitäten d_j. Die Produktgruppe der unabhängig auf ranPi_j wirkenden U(d_j) ist weiterhin gemeinsamer Stabilisator aller fünf gelifteten Felder. Unabhängige Blockphasen beseitigen Projektorkopplungen zwischen diesen Sektoren; innerhalb jedes Sektors folgt wie oben

    J=direct_sum_j(J_j tensor I_dj),
    rankJ=sum_j d_j rankJ_j.

Zusätzliche Basissymmetrien bleiben möglich; diese Rangsumme ist nur notwendig. Wird zusätzlich J<=suppR gefordert, dürfen Witness-leere tau-Nullsektoren keinen Anteil liefern. Es werden keine künstlichen Rang2-Gruppierungen als eindeutig ausgegeben.

Konkrete positive Beispiele mit Basis F=diag(1,3), W=[[1/2,1/4],[1/4,1/2]]:

- m2,uniforme tau: F_m hat einen eindeutig kleinsten Eigenwert1/2 mit gesamtem Spektralprojektor diag(1,0) tensorI2. Dieser gesamte Rang2-Träger ist kovariant und mit der Kopiensymmetrie verträglich. Eine Basis innerhalb des Paares bleibt frei.
- m3,tau=diag(1/2,1/4,1/4): Die Kopienmultiplizitäten sind1 und2. Der gesamte kleinste F_m-Spektralblock zum Eigenwert1/4 hat Rang2. Der uniforme Rang3-Teilbarkeitsausschluss gilt hier nicht; die Quelle besitzt durch tau bereits zusätzliche Operatorstruktur.
- m3,reine tau=diag(1,0,0): R_m hat bei dieser Rang2-Basis weiterhin Rang2. Sein gesamter intrinsischer Träger ist ein zulässiger Paarträger, obwohl der volle Umgebungsraum Dimension6 hat. Die vier Witness-leeren Richtungen werden nicht als zusätzliche physikalische Paaranteile ausgewählt.

Diese Beispiele belegen Verfügbarkeit im angegebenen Bereich. Sie behaupten weder eine universelle physikalische Wahl des kleinsten F-Spektrums noch eine autonome Auswahl der in der Quelle deklarierten Parameter m/tau.

## Expliziter Koordinaten-Gegenzeuge und Grenze des Satzes

Beim uniformen m3-Lift sei J_bad=diag(1,0) tensor diag(1,1,0), Rang2. Die Kopienpermutation U, die die erste und dritte Kopie vertauscht, lässt Xi vollständig unverändert, verändert aber J_bad. Exakt

    ||(I2 tensor U) J_bad (I2 tensor U†)-J_bad||_F²=2.

Damit kann dieses Koordinatenpaar keine kovariante Xi-allein-Auswahl sein. Dieselbe Aussage gilt nach simultaner komplexer Eichung; sie ist kein Artefakt der dargestellten Tensorbasis.

Der Ausschluss setzt ausdrücklich den aktuellen endlichen Zustand als alleinige Eingabe voraus. Werden zusätzliche historische Abstammungsmarkierungen, physikalische Referenzdaten oder Level-/Ortslabelprojektoren als eigenständige Daten mitgeführt, kann die Symmetrie des erweiterten Zustands kleiner sein. Die bloße Kenntnis einer Kopienzahl oder einer Tensorzerlegung wählt aber noch keine einzelne Kopienrichtung unter deren U(m)-Freiheit. Eine konkrete zusätzliche Markierungs- und Transportregel müsste aus der Quelle bestimmt und mit dem erweiterten Zustand geprüft werden. Dies darf weder stillschweigend vorausgesetzt noch als grundsätzlich unmöglich erklärt werden.

Auch andere mathematische Zielräume als orthogonale interne Projektoren werden durch diesen Satz nicht allgemein ausgeschlossen. Ein vollständiger Energie-Impuls-Strom oder ein Einstein-Grenzfall wird nicht behauptet.

## Frische Kontrollen und nächste Abhängigkeit

[TENSOR_LIFT_FULL_STATE_SYMMETRY_CHECKS.md](TENSOR_LIFT_FULL_STATE_SYMMETRY_CHECKS.md) enthält Reproduktion und Rohdaten. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur, sechs nichtterminale Originalereignisse: Basis n2, uniforme m2/m3-Lifts, degenerierte/nichtuniforme und reine m3-Lifts sowie komplexe Eichversion des uniformen m3-Lifts, Seed20261118.

Rational frisch geprüft: Kommutantendimensionen der Kopiengeneratoren4,4,8 für n2 mit uniformem m2,m3 und Kopienblöcken1+2; genauer Koordinaten-Projektordefekt²2. Numerisch: gemeinsame Symmetrie aller fünf Felder vor und nach Originalereignis; positive Rang2-Spektral-/Supportalternativen; komplexer Symmetrierest maximal3.38e-15 und Projektoränderung beim unzulässigen Paar sqrt2. Positive Projektortransportreste in den geprüften ausgerichteten Beispielen numerisch0. Toleranz1e-10,Wurzelcutoff1e-12 und Spektralcluster1e-8; keine Schwellenzertifizierung beliebig naher Spektren.

Der nächste quellengebundene Prüfpunkt ist, welche expliziten relationalen oder historischen Daten die BFG tatsächlich für eine solche Symmetriebrechung bereitstellt und wie deren eigene Transport-/Abschlussregeln lauten. Eine frei eingetragene Koordinatenmarkierung ersetzt diese Prüfung nicht. Die positiven Rang2-Erzeugungen aus Runde67 bleiben erhalten, ihre jeweiligen Voraussetzungen sind jetzt schärfer bestimmt.

Nur Forschungsdokumentation; Originaldynamik, Manuskripte, Lizenzen, empirische Ausgaben, Audit-Dateien und Workflows unverändert. Runde67-CI am exakten Ergebnishead ist separat grün dokumentiert. Diese neue eingebettete Reproduktion bleibt lokale Evidenz und wird durch die unveränderte Pipeline nicht automatisch ausgeführt.
