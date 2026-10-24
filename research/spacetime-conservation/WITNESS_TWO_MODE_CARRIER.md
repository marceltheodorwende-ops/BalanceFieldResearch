# Runde63: bedingter Witness-Zweimodenträger mit exaktem Determinantenkegel

Präregistrierung PROTOCOL.md, Commit e5dde440976178fb52002539a717a96ee173f0c7; Auswertung 2026-10-24. Nur BFG: vollständiges Dynamic Order vom 8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA256 1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blob ff8b0a7ec922ccfeacae5bc9ce6c104b79286498, durch audit.load_update geprüft.

## Konstruktives Ergebnis und präzise Bedingung

Der positive Witness-Formationsoperator R=sqrt(F) W sqrt(F) aus Runde52 liefert bei rankR=2 einen BFG-intern bestimmten Zweimodenträger: seinen gesamten Träger Q_R=suppR. Unter gemeinsamer nichtterminaler Retention transportiert die Originalquelle diesen Träger isometrisch, auch wenn ein Seed den vollständigen aktiven Projektor P auf Rang3 oder höher erweitert.

Damit ist das Füllen des vollständigen aktiven Trägers aus Runde45 nicht gleichbedeutend mit dem Verlust jedes Zweimoden-Unterträgers. Der hier gewählte Unterträger stammt aus R selbst. Es gibt aber KEIN bewiesenes Quellgesetz, das rankR=2 für allgemeine Zustände auswählt, und keinen Nachweis, dass dieser Hilbert-Unterraum eine lokale räumliche Ereignisregion ist. Es handelt sich um einen konstruktiven bedingten Kandidaten.

Auf diesem Paar bleibt der positive Herm(C²)-Determinantenkegel exakt erhalten. Die bloße Pauli-Dreierkomponente ist jedoch noch kein physikalischer Impuls; eine direkte Generatoridentifikation scheitert am ausdrücklich zusätzlichen Kriterium dreier kommutierender gewöhnlicher Translationen.

## Exakter Trägertransport aus derselben Dynamik

Voraussetzungen: gemeinsame Retention wie Runde51/52, R>=0 und rankR=2. Die Originalidentität lautet

    R_out=V R V†, V†V=P, R=PRP.

Da V auf ranP isometrisch ist,

    rankR_out=rankR,
    Q_R,out=V Q_R V†.

Dies folgt aus dem Spektral-/Trägerfunktionalkalkül; eine orthogonale Seedrichtung trägt zu R_out keinen Anteil bei. Wähle eine orthonormale Paarbasis Z mit Z†Z=I2 und ZZ†=Q_R. Dann ist

    Z_out=VZ,
    X=Z† R Z,
    X_out=Z_out† R_out Z_out=X.

Die Basis ist nicht kanonisch: jedes ZU mit U in U(2) beschreibt denselben gesamten Träger. Die mitbewegte Basis gibt eine unveränderte komprimierte Matrix, andere Paarbasen unitäre Kongruenzen. Bei anfänglicher verlustbehafteter Selektion gilt diese Retentionsidentität nicht automatisch; die Auswahlgrenzen aus Runde60 bleiben bestehen.

## Pauli-Kegel und Energiekomponente

Schreibe mit den Standard-Pauli-Matrizen

    X=(p0 I+p1 sigma_x+p2 sigma_y+p3 sigma_z)/2,
    p0=trX=tr(WF),
    p_i=tr(sigma_i X).

Standardmatrixalgebra liefert

    detX=(p0²-p1²-p2²-p3²)/4.

Weil X positiv ist, gilt p0>=|p| und p0>=0. Bei positivem rank2-X liegt der Vektor strikt innerhalb dieses algebraischen Zukunftskegels, detX>0. Die Quelle bewahrt alle Eigenwerte von X und damit Spur, Determinante und quadratische Form exakt.

Dies ist ein anderer Kandidat als der früher auf Nullkegeldefekte geprüfte Kernel K: dessen nichttriviale C/B-Kanalwirkung wird hier nicht fälschlich durch den isometrischen Witness-Formationskanal ersetzt. Für R ist der Kegeltransport unter den genannten Bedingungen tatsächlich exakt.

Alle vier Koordinaten haben hier Formationseinheiten. Eine physikalische Umrechnung der drei Raumkomponenten zu Impulseinheiten, eine Geschwindigkeitsskala oder ein lokaler Energie-Impuls-Strom folgen daraus nicht.

Ein Rang1-R-Zustand kann in einem bereits gegebenen zweidimensionalen Umgebungsraum auf dem Nullkegel liegen. Sein intrinsischer Träger hat aber nur Dimension1; ein zusätzliches zweites Nullraumbein ist durch suppR allein nicht ausgewählt. Der bedingte rank2-Träger liefert deshalb nicht zugleich eine kanonische Zweimodenwahl für sämtliche Nullzustände.

## Rahmenrotation ist noch keine Beobachter-Boostbrücke

Eine andere orthonormale Paarbasis ZU verändert X zu U† X U. Diese U(2)-Wirkung hält p0 fest und dreht das Pauli-Tripel mit einer SO(3)-Matrix; sie ist im algebraischen Lorentzraum der räumliche Rotationsuntergruppe zugeordnet. Sie bestimmt keine zusätzliche nichtkompakte physikalische Beobachtertransformation.

Zum Vergleich ist eine SL(2)-Kongruenz A X A† für detA=1 ebenfalls determinantenerhaltend, aber nicht allgemein spurerhaltend. Exakt:

    X=I2/2, A=diag(sqrt2,1/sqrt2),
    detX=det(A X A†)=1/4,
    p0(X)=1, p0(A X A†)=5/4,
    p3(A X A†)=3/4.

Dieser algebraische Boost ist kein unitärer Quellenrahmenwechsel und nicht durch die gemeinsame Retentionsidentität als zusätzliche Ereignisdynamik ausgewählt. Das Fehlen eines solchen Boosts in dieser speziellen Transportdarstellung widerlegt keine denkbare Lorentz-kovariante physikalische Brücke: Beobachterwechsel und Ereignisentwicklung sind verschiedene Aufgaben. Die Quelle muss eine physikalische Beobachter-/Messabbildung zusätzlich begründen.

## Warum die direkte Pauli-Impulsdeutung nicht genügt

Zusätzliches physikalisches Vergleichskriterium, kein BFG-Axiom: Wenn drei räumliche Translationen die gewöhnliche abelsche Gruppe darstellen, müssen ihre drei selbstadjungierten Generatoren paarweise kommutieren. Das folgt schon durch Differenzieren der Gleichheit der beiden Reihenfolgen der unitären Verschiebungen.

Direkt P_i=kappa sigma_i mit kappa!=0 ergibt hingegen

    [P_i,P_j]=2i kappa² epsilon_ijk sigma_k !=0.

Identitätsanteile ändern diesen Kommutator nicht. Allgemeiner sind zwei hermitesche Zweimodenoperatoren aI+b·sigma und cI+d·sigma genau bei b×d=0 kommutierend. Ein ganzes paarweise kommutierendes Tripel besitzt daher eine gemeinsame Pauli-Achse:

    P_i=a_i I+b_i sigma_n.

Seine Erwartungen lesen nur eine Blochrichtung, nicht drei unabhängig variierende Komponenten des vollständigen Pauli-Tripels. Das schließt die direkte Identifikation des gesamten Tripels als drei solche Impulsgeneratoren aus. Es schließt keine größeren Translationsdarstellungen, externen Impulslabels, andere Zustandsbrücken oder eine zusätzliche räumliche Struktur aus.

Damit bleibt eine klare positive Struktur bestehen: bedingter interner Zweimodenträger und exakter Determinantenkegel. Der Schritt zu physikalischem Impuls braucht jedoch mehr als diese algebraische Form.

## Frische Originalkontrollen und Grenzen

[WITNESS_TWO_MODE_CHECKS.md](WITNESS_TWO_MODE_CHECKS.md) enthält vollständige symbolische Rechnung und Rohdaten. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur, fünf Originalereignisse:

- Voller n2-Fall F=diag(1,3), W=[[.5,.25],[.25,.5]]: p=(2,sqrt3/2,0,-1), detX=9/16; unverändert.
- Voller n2-Rang1-W=ones2/2: detX=0 und quadratische Form0 im gegebenen Umgebungspaar, nicht als intrinsischer rank2-Träger ausgegeben.
- Rationaler n3/r2-Seedfall mit nichtkommutierendem W: aktiver Rang steigt auf3, R-Träger bleibt2, detX0.0966 und quadratische Form0.3864.
- Ein weiteres Retentionsereignis dieses Seedfalls bewahrt den transportierten R-Unterträger.
- Komplexe simultane Eichversion des Seedfalls, Seed20261113, bestätigt dieselben Pauliwerte in entsprechend mittransformiertem Paarrahmen.

Maximaler R-Transportrest1.68e-15, Träger-/Kompressionsrest2.34e-15, Koordinatenrest1.56e-15 und Eichkoordinatenrest1.23e-15. Quadratwurzel-Nullraumcutoff1e-12 dient den theoretischen Nullrichtungen; die kleinen Zahlen sind Gleitkommakontrollen und keine Zertifizierung beliebig schwellen-/rangnaher Fälle. Allgemeiner Trägertransport, Pauli-Determinante und Kommutatorhindernis folgen aus den exakten Matrixidentitäten.

## Nächste Abhängigkeit

Zu prüfen bleibt eine BFG-interne physikalische Begründung der Rang2-Präparation bzw. Paarwahl, ihrer räumlichen Lokalität und einer unabhängigen Translations-/Beobachter-/Uhrstruktur. Der transportierte R-Träger ist ein konkreter Kandidat, löst diese Auswahlfragen aber nicht. Ein vollständiger Energie-Impuls-Strom oder Einstein-Grenzfall wird nicht behauptet.

Nur Forschungsdokumentation; ursprüngliche Manuskripte, Grundgleichungen, Lizenzen und empirische Ergebnisse unverändert, keine Audit-/Workflowänderung und kein neuer Remote-CI-Pass.
