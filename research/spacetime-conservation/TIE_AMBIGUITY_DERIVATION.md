# Konkurrierende Auflösung durch Formation und Witness

## Quelle und neue Frage

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik aus derselben gepinnten vollständigen positiven Persistenzquelle. Die lexikographische Auflösung nach Y/F/W aus Runde 8 bleibt eine gültige partielle mathematische Konstruktion mit ihrer bereits dokumentierten Grenzunstetigkeit. Diese Runde wiederholt sie nicht als neues Ergebnis, sondern prüft, ob Kovarianz, Persistenz und lokale Kernelkonstanz ihre Priorität gegenüber naheliegenden Alternativen erzwingen.

Die Kandidaten sind Rang-zwei-Beobachtungsflächen im vollen Raum. Sie sind nicht der ursprüngliche BFG-Träger P: Dieser bleibt im Beispiel I_3 mit Rang drei. Eine tatsächliche Quell-Rangreduktion wird nicht behauptet.

## Ein vollständig positiver, nichtisotroper Referenzzustand

Wähle n=3,Y=yI mit y>0,
F=diag(1,2,4),
W=(1/9) [[1,0,0],[0,4,-1],[0,-1,4]],
K=diag(1,2,3)/6.

F und W sind positiv, W hat Eigenwerte 1/9,3/9,5/9 und Spur eins; K ist positiv mit Spur eins. [F,W]!=0. Anders als der vollständig isotrope Grenzzeuge der letzten Runde enthält dieser Zustand also tatsächlich unterscheidende BFG-Daten.

Bei skalarer Last gilt exakt alpha=y²/(1+y²). Alle Analyse-/Kernelzweige sind skalar, deshalb im ausgerichteten vollen Update

Y_+=[2y²/((1+y)²(1+y²))]I,
F_+=F, W_+=W, K_+=K.

Die Last bleibt positiv und skalar; die Aussagen gelten induktiv für jedes endliche mathematische Persistenzereignis. Es wurde kein neues Erhaltungsgesetz eingebaut oder eine Dynamik eingefroren: Die vorhandene Quelldynamik ist auf diesem Teilbereich tatsächlich so einfach.

## Zwei natürliche, aber verschiedene partielle Selektoren

Bei entartetem Y bestimme entweder die beiden kleinsten Eigenmoden von F (Formation zuerst) oder von W (Witness zuerst). Beide zugehörigen Eigenlücken sind hier offen. Es folgt

P_F=diag(1,1,0),
P_W=[[1,0,0],[0,1/2,1/2],[0,1/2,1/2]].

Beide sind unitär kovariant aus vorhandenen Daten bestimmbar und bleiben unter jedem exakten skalaren Lastschritt konstant. Ihr Abstand ist ||P_F-P_W||_F=1. Die jeweiligen lokalen Kernelmatrizen P_F K P_F und P_W K P_W bleiben ebenfalls exakt konstant. In einem festgehaltenen Rahmen besitzt jede dieser Hermiteschen Zweimodenmatrizen vier konstante reelle Komponenten; eine physikalische Bedeutung dieser Komponenten folgt daraus nicht.

Die lokalen Spuren unterscheiden sich:

tr(P_F K)=1/2,
tr(P_W K)=7/12,
Differenz=1/12.

Damit bestimmen die geprüften Kriterien Kovarianz, exakte Persistenz und vier konstante lokale Kernelkomponenten keinen eindeutigen Paarsektor oder eindeutigen lokalen Bestand. Dies beweist nicht, dass kein weiterer quellengestützter Auswahlgrund existiert. Insbesondere wird nicht behauptet, der Quelltext schreibe Witness zuerst vor oder verbiete Formation zuerst. Gerade die mathematische Priorität ist hier die offene Auswahlentscheidung.

## Kontinuierliche natürliche Alternative als ausdrückliche Zusatzwahl

Betrachte für tau>=0 die rein mathematische Kandidatenfamilie H_tau=F+tau W und ihren unteren Rang-zwei-Projektor. tau ist ein hinzugefügter Selektorparameter, keine aus BFG hergeleitete Kopplung, keine physikalisch identifizierte Einheit und kein auf Einstein kalibrierter Wert.

Der erste Eigenwert 1+tau/9 bleibt unter dem unteren Eigenwert des 2x2-Blocks. Dessen Eigenwerte sind 3+4tau/9±sqrt(1+tau²/81). Die nötige Ordnung folgt aus

(2+tau/3)²-(1+tau²/81)=3+4tau/3+8tau²/81>0.

Der Projektor besteht aus dem ersten Modus und dem unteren Blockprojektor

(1/2)[I + [[1,tau/9],[tau/9,-1]]/sqrt(1+tau²/81)].

Exakt gilt

||P_tau-P_F||_F²=1-1/sqrt(1+tau²/81).

Bei tau=0 entsteht P_F; für tau->infty entsteht P_W. Weil F und W im Teilbereich konstant sind, erfüllen alle diese Kandidaten dieselben Kovarianz-/Persistenz-/Kernelkonstanzkriterien. Auch die lokale Spur variiert kontinuierlich zwischen den beiden ausgewiesenen Werten. Die Familie zeigt die Unterbestimmtheit dieser Kriterien, nicht die physikalische Gleichwertigkeit oder Quellenwahl beliebiger tau.

## Frische Evidenz und erhaltene Grenzen

TIE_AMBIGUITY_PROTOCOL.md vor Auswertung auf GitHub publiziert. Exakte Projektor-/Kommutator-/Spuridentitäten, skalare Quelldynamik und allgemeine tau-Blockdiagonalisierung geprüft. Sechs frische Original-Quellaufrufe: y=.05,.1,.2 plus jeweils eine simultane komplexe Eichkontrolle. Kandidaten tau=0,1,9,90 und reine W-Auswahl vor/nach jedem Schritt verglichen; vollständige Matrixkompressionen geprüft, nicht bloß deren Spur.

Feldrest 1.6653345369377348e-16, Projektorrest 0, Rest komprimierter Kernel 1.2451418823608528e-16, Eichrest 3.656632498885118e-15; vorab Schwelle 1e-10. Alle Originalträger bleiben Rang drei. Die unendliche Persistenzaussage folgt aus der exakten skalaren Rekurrenz und Invarianz, nicht aus drei numerischen Lastfällen. CI separat in CI_VALIDATION.md.

Die letzte isotrope Kovarianzgrenze wird hier nicht stillschweigend umgangen: Nichtisotrope Daten erlauben jetzt mehrere kovariante Selektoren. Sie garantieren gerade noch keine eindeutig durch die geprüften Kriterien bevorzugte Wahl. Die früheren Gedächtnis- und lückenabhängigen Stabilitätssätze bleiben gültig.

Nächste Abhängigkeit: ein im vollständigen BFG-Mechanismus belegtes Auswahlkriterium beziehungsweise eine ausdrücklich mengenwertige lokale Sektorbeschreibung; anschließend Fortsetzung/Bilanz über echte Auswahl-/Rangereignisse und räumliche Relationen. Eine weitere willkürliche Priorität oder ein frei gewähltes tau darf nicht als physikalische Herleitung ausgegeben werden. Räumlicher Transport, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen.
