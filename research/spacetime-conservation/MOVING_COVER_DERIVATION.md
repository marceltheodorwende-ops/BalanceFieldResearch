# Wechselnde Effekte: dynamischer Strom und Zuordnungsänderung

## Quelle und Voraussetzungen

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik aus derselben gepinnten vollständigen positiven Persistenzquelle. Der aktuelle Kernelkanal ist Phi(K)=K_+=sum_r T_r K T_r mit Hermiteschen T_r und sum T_r²=I. Die Umgebungsdaten zur Bestimmung der T_r bleiben erhalten. Die Dimension n bleibt fest; Ausgabe und Eingabe werden im bereits definierten ausgerichteten Rahmen verglichen.

Es gibt zwei positive normierte Effektlisten E_a und E'_a mit denselben zugeordneten Labels, sum E_a=sum E'_a=I. Die heutige Rechnung behandelt einen Effektwechsel innerhalb des festen Raums, nicht ein neues Gesetz für echte Seed-/Rangereignisse. Welche Listen aus der Quelle gewählt werden sollen, wird nicht durch die Bilanzidentität entschieden.

## Exakte Bilanz mit neuem Zuordnungsterm

Die beobachteten Bestände lauten q_a=tr(E_a K), q'_a=tr(E'_a K_+). Der ausgehende Quellstrom mit alten Effekten ist wie in Runde 36

J_ab(E,K)=sum_r Re tr(E_a T_r E_b[T_r,K]),
J_ab=-J_ba.

Exaktes Addieren und Subtrahieren von tr(E_a K_+) ergibt

q'_a-q_a=tr[E_a(K_+-K)]+tr[(E'_a-E_a)K_+].

Der erste Term ist durch die vorige volle Kernelkontinuität -sum_b J_ab(E,K). Also

Delta q_a+sum_b J_ab(E,K)=R_after,a,
R_after,a=tr[(E'_a-E_a)K_+].

Wegen der beiden Einszerlegungen gilt sum_a R_after,a=0. Der Term ist eine Änderung der Zuordnung zu lokalen Beständen, keine neu erfundene physikalische Reserve. Er muss mitgeführt werden, wenn lokale Bestandsänderungen als dynamischer Austausch interpretiert werden sollen. Die Gesamtspur bleibt innerhalb des vollen Persistenzsektors weiterhin erhalten.

## Zwei gleichwertige Zerlegungen und Kreuzterm

Alternativ kann mathematisch erst die neue Liste an K ausgewertet und dann dieselbe Quelldynamik betrachtet werden:

Delta q_a+sum_b J_ab(E',K)=R_before,a,
R_before,a=tr[(E'_a-E_a)K].

Beide Identitäten sind exakt. Ihre Differenz ist

R_after,a-R_before,a=tr[(E'_a-E_a)(K_+-K)],
sum_b[J_ab(E',K)-J_ab(E,K)]=R_before,a-R_after,a.

Damit ist eine Zerlegung in dynamische und zuordnungsbedingte Änderung nicht ohne Angabe der verwendeten Liste bzw. Reihenfolge eindeutig. Das sind zwei algebraische Zerlegungen desselben Zustandsvergleichs, keine zwei konkurrierenden physikalischen Zeitordnungen. Der berechnete Kreuzterm darf nicht unterschlagen oder nachträglich als zusätzlicher physikalischer Impuls angepasst werden.

## Reiner Zuordnungszeuge mit unverändertem vollständigem Kernel

Nimm n=3, Y=.1I,F=diag(1,2,4),W=I/3,K=diag(1/5,3/10,1/2). Die volle skalare Lastdynamik lässt K exakt unverändert; ihre Kernelzweige sind skalar. Deshalb J_ab(E,K)=0 für jede alte Effektliste.

Als alte Liste dienen die drei normierten Koordinatenpaare E_12,E_13,E_23=P_ij/2. Die neue Liste ist R E_ij R^dagger mit einer Rotation R um pi/4 in Moden 1,2. Das ist eine ausdrücklich vorgegebene mathematische Umzuordnung, kein als quellenausgewählt ausgegebener räumlicher Transport. Exakt

Delta q=R_after=R_before=(0,1/40,-1/40),
K_+-K=0,
J_ab=0.

Lokale Bestandsänderung allein beweist somit keinen dynamischen Strom. Der Zeuge widerlegt nicht die korrekte Kontinuitätsgleichung mit Zuordnungsterm; er zeigt, warum die feste-Effekt-Version nicht unbesehen auf wechselnde Listen übertragen werden darf.

## BFG-interne wechselnde Listen im numerischen Test

Die sechs allgemeinen Quellkontrollen verwenden als nachvollziehbare, aber nicht physikalisch privilegierte Wahl die normierten Koordinatenpaar-Effekte im geordneten Eigenrahmen von K bzw. K_+. Die Projektoren sind phasenunabhängig. Die Eigenlücken beider Kernel werden vor jedem Vergleich geprüft, damit die verwendeten Labels innerhalb der Präparation eindeutig sind. Dies behauptet keine globale Fortsetzung dieser Wahl durch Eigenwertkollisionen; die früheren Stabilitätsgrenzen bleiben gültig.

Die T_r werden in beiden Zerlegungen aus demselben aktuellen BFG-Zustand berechnet. Eine neue Liste ersetzt keinen Eingangsparameter der Quelldynamik und erzeugt keine veränderte physikalische Entwicklung.

## Frische Evidenz

MOVING_COVER_PROTOCOL.md vor Auswertung auf GitHub publiziert. Der allgemeine Beweis ist die explizite Spurzerlegung oben. Der reine Zuordnungszeuge wurde exakt mit rationalen Matrizen und einer algebraischen pi/4-Rotation geprüft.

Neun frische Original-Quellaufrufe: n=3,4 mit je drei positiven komplexen Präparationen, zwei simultane komplexe Eichkontrollen und ein zusätzlicher skalarer Originalzeuge. Positive K, nichtkommutierende komplexe Last, F-diagonaler Bezugszustand und W=I/n in den allgemeinen Fällen. Alle benutzten Kernel-Eigenlücken lagen über vorab 1e-8. Beide Bilanzzerlegungen, Kreuzterm, verschwindende Summe der Zuordnungsterme und Kovarianz wurden separat geprüft.

Bilanzrest 9.696223316445207e-16, Eichrest 1.6855774988216096e-15, Rest des reinen Zuordnungszeugen 1.391243901732968e-16; vorab Schwelle 1e-10. Im reinen Zeugen ist die dynamische Stromnorm numerisch exakt 0, während die Zuordnungsterme ungefähr (0,.025,-.025) betragen. In den allgemeinen Fällen sind Kreuzterme und Zuordnungsänderungen nicht null; alle Werte bleiben im JSON erhalten. Keine Langtrajektorie oder Rank-Cutoff-Fortsetzung behauptet. CI separat in CI_VALIDATION.md.

Nächste Abhängigkeit: lokale Bilanz über echte Auswahl-/Seed-/Rangereignisse mit unterschiedlichen Trägerräumen, statt bloßer Neuetikettierung im festen Raum; danach quellengestützte räumliche und zeitliche Deutung. Diese Zuordnungsidentität liefert noch keinen physikalischen Raumtransport, keine Uhr, keinen vollständigen Energie-Impuls-Strom und keinen Einstein-Grenzfall.
