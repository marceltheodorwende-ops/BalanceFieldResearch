# Informationsgehalt einer beschrifteten Familie lokaler Paarsektoren

## Quelle und Fragestellung

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik aus derselben gepinnten positiven Persistenzquelle. Aus Runde 33 werden F=diag(1,2,4), W=[[1,0,0],[0,4,-1],[0,-1,4]]/9 und Y=yI übernommen. Der originale Quellträger bleibt I_3 mit Rang drei. Die Kandidaten P_tau stammen als zusätzliche mathematische Auswahlfamilie aus F+tau W, tau>=0; der Grenzfall ist die reine W-Auswahl. Kein tau wird als physikalische Kopplung ausgewählt.

Geprüft wird jetzt die natürliche Alternative, alle Kandidaten gemeinsam zu behalten. Entscheidend: Die Familie ist beschriftet. Zu jeder Matrix P K P bleibt bekannt, zu welchem Projektor P sie gehört. Das Vergessen der Projektorlabels wäre eine andere Quotientenbildung mit eigenem Geschlossenheitsproblem und wird nicht stillschweigend vorgenommen.

## Exakter reell-linearer Rang der Kandidatenfamilie

Bei festen F,W,Y definiere L(K)=(P K P)_P auf Herm(C³), einem neundimensionalen reellen Vektorraum. Drei Familienmitglieder genügen für den beobachteten Rang:

P_F=diag(1,1,0),
P_12=[[1,0,0],[0,4/5,2/5],[0,2/5,1/5]],
P_W=[[1,0,0],[0,1/2,1/2],[0,1/2,1/2]].

P_12 ist der untere Projektor von F+12W, nicht eine nachträglich angepasste Quellauswahl. Auf der Standardbasis aus drei Diagonalmatrizen und je realem/imaginärem Hermiteschem Offdiagonalpaar hat die gemeinsame Kompressionsabbildung exakt reellen Rang 8. Ihr eindimensionaler Kern wird erzeugt von

J=i(|2><3|-|3><2|).

Auch die gesamte kontinuierliche P_tau-Familie sieht J nicht: Jeder P_tau besteht aus dem ersten Modus und einem reellen Vektor in der 2/3-Ebene, und ein solcher Vektor hat Erwartungswert null gegen die rein imaginäre antisymmetrische J-Richtung. Exakt P_tau J P_tau=0. Weil bereits drei Mitglieder Rang 8 erreichen, besitzt die ganze Familie genau diesen einen Kern und Rang 8.

Damit speichert die gemeinsame Familie im Allgemeinen acht reelle Kernelparameter, nicht vier. Bei zusätzlich festgehaltener Spur eins hat ihr sichtbarer affiner Bereich Dimension 7: Die unsichtbare Richtung ist spurlos und die sichtbaren Daten bestimmen die Spur. Diese Zählung betrifft ausschließlich den Kernel bei festgehaltenem F,W,Y, nicht die Dimension des gesamten BFG-Zustands und noch keine Raumzeitdimension.

## Positive Faser und tatsächliche Geschlossenheit im geprüften Teilsektor

Setze K_plus=I/3+J/12 und K_minus=I/3-J/12. Beide sind positiv mit Eigenwerten 1/4,1/3,5/12 und Spur eins. Sie haben dieselben sämtlichen beschrifteten P_tau-Kompressionen, sind aber verschiedene volle Kernel:

||K_plus-K_minus||_F=sqrt(2)/6.

Bei Y=yI bleibt im vollständigen ausgerichteten BFG-Schritt K unverändert und F,W bleiben erhalten. Daher bleiben beide Familienbilder gleich, auch nach dem Schritt und nach jedem endlichen skalaren Persistenzereignis. Die unsichtbare Phase ist hier eine echte verlorene Koordinate, aber kein Gegenbeispiel gegen Faser-Geschlossenheit: In diesem beschränkten Sektor trennt die Zukunft die beiden Familienbilder gerade nicht. Eine allgemeine Geschlossenheit außerhalb dieses Sektors wird daraus nicht abgeleitet.

Es wird ebenfalls keine physikalische Gleichwertigkeit der beiden vollen Zustände behauptet. Andere zulässige Beobachtungsflächen könnten J sehen; beispielsweise die Koordinatenfläche der Moden 2,3 komprimiert J auf sich selbst.

## Natürliche Alternative: alle beschrifteten Rang-zwei-Flächen

Die Familie sämtlicher Rang-zwei-Projektoren ist sogar injektiv auf Herm(C^n), n>=3. Beweis: Ist H!=0 Hermitesch, gibt es einen Eigenvektor v mit v^dagger H v!=0. Wähle eine zweidimensionale Fläche, die v enthält, mit Projektor P. Dann v^dagger P H P v=v^dagger H v!=0. Somit können nicht alle Kompressionen verschwinden.

Konstruktiv genügen die Koordinatenpaarflächen span(e_i,e_j), um alle Diagonalen und reellen/imaginären Offdiagonalen zu rekonstruieren. Für n=3 bestätigt der Audit exakt Rang 9 aus den drei Koordinatenpaaren. Die volle beschriftete Familie trägt deshalb n² reelle Kernelparameter, bei Spur eins n²-1. Sie beseitigt die willkürliche einzelne Paarwahl, aber reduziert den Kernel nicht automatisch auf Herm(C²) mit vier reellen Komponenten.

Dies ist weder ein Verbot einer anders begründeten vierdimensionalen Reduktion noch ein allgemeines Transport-No-Go. Es zeigt präzise, dass das bloße Sammeln der konkurrierenden Paarsektoren die fehlende physikalische Trägerauswahl nicht von selbst ersetzt. Überlappende Kompressionen sind außerdem nicht ohne weitere Bilanz als disjunkte lokale Bestände addierbar; eine solche Bilanz wird hier nicht erfunden.

## Frische Evidenz

PAIR_FAMILY_PROTOCOL.md vor Auswertung auf GitHub publiziert. Exakte reell-lineare Ränge 8 und 9, Nullraum J, positive Fasereigenwerte und allgemeine P_tau-J-Identität geprüft. Acht frische Original-Quellaufrufe: y=.05,.1,.2 mit beiden K-Fasermitgliedern (sechs) und zwei simultane komplexe Eichkontrollen. Gleiche Familienbilder, erhaltener versteckter Zustand und tatsächliche volle Felder vor/nach Schritt verglichen.

Kompressionsrest 1.777224365758701e-16, Rest verborgener Kernelidentitäten 1.962615573354719e-16, F-/W-Feldrest 0, Eichrest 5.613110562242644e-16; vorab Schwelle 1e-10. Die endliche Originalevidenz wird nicht als numerische unendliche Trajektorie ausgegeben; die Persistenz folgt aus der exakt skalaren Dynamik. CI separat in CI_VALIDATION.md.

Nächste Abhängigkeit: eine quellengestützte Reduktion mit nachgewiesener Faser-Geschlossenheit und passender Bilanz über überlappende oder wechselnde Sektoren, statt bloß vier Parameter pro beliebigem Paar zu zählen. Vorige lokale Gedächtnis- und Stabilitätssätze bleiben gültig. Allgemeine Trägerauswahl, räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen.
