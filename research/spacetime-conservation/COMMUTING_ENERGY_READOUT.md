# Momentan kommutierende Hamiltonian-Kandidaten – Runde 49

## Ergebnis und positive Teilklasse

Eine BFG-interne Alternative zu H proportional K ist die spektrale Projektion

H_Y=D_Y(K)=sum_lambda P_lambda(Y) K P_lambda(Y).

Sie kommutiert definitionsgemäß mit dem aktuellen Y. Im vollen Persistenzsektor ist sie tatsächlich als Operator erhalten, solange der Quellschritt keine zuvor verschiedenen Y-Eigenwerte zusammenführt. Bei einer exakten neuen Eigenwertkollision kann sie jedoch zusätzliche Kernelkohärenzen aufnehmen und sich ändern.

Ein rationaler positiver Zwei-Moden-Zeuge liefert H_Y=2I vor dem Ereignis und H_Y,out=2I+(5/6)sigma_x danach. Der Witness-Erwartungswert springt von2 auf29/12, also um5/12 Formationseinheiten vor einer etwaigen Kalibrierung. Kein Seed oder Rangwechsel ist beteiligt.

Die naheliegende Alternative H_F=D_F(K) mit den aktuellen Formationseigenräumen ist ebenfalls nicht allgemein erhalten, selbst wenn F im Quellrahmen konstant bleibt. Erhaltene Teilklassen und die Möglichkeit zusätzlicher gespeicherter Spektralprojektoren bleiben ausdrücklich bestehen.

Vorab: PROTOCOL.md Runde49. Quellenbindung unverändert. **Zusätzliche Identifikationshypothese** ist nur die Benennung eines dieser Matrixausdrücke als Hamiltoniankandidat; die BFG-Quelle hat ihn hier nicht schon physikalisch ausgewählt. Keine neue Dynamik oder gefittete Energieeinheit.

## 1. Warum H_Y ohne neue Kollision funktioniert

Auf der vollen Persistenzklasse wirkt K_out=Phi(K) in einer Y-Eigenbasis durch h_lambda,mu. Innerhalb jedes Y-Eigenraums ist h_lambda,lambda=1. Daher gilt exakt

D_Y(Phi(K))=D_Y(K).

Die Quelle liefert zugleich Y_out=g_alpha(Y). Wenn g_alpha auf dem aktuellen endlichen Y-Spektrum injektiv ist, besitzen Y und Y_out dieselben Spektralräume bis auf Umbenennung/Umordnung. Dann ist

D_Yout(Phi(K))=D_Y(K),
also H_Y,out=H_Y.

Die Aussage verlangt keine bevorzugte Reihenfolge der Eigenwerte. Sie verlangt, dass keine neuen Spektralräume verschmelzen. Auf einer entsprechenden kollisionsfreien Folge gilt die Operatorerhaltung und damit auch eine konstante Erwartung gegen den im ausgerichteten Quellrahmen konstanten Witness.

Bei einer neuen Kollision kommt dagegen der exakt bestimmbare Anteil hinzu:

H_Y,out-H_Y =
sum_{lambda!=mu, g_alpha(lambda)=g_alpha(mu)}
h_lambda,mu P_lambda K P_mu.

Die Summe enthält beide geordneten Richtungen und ist insgesamt Hermitesch. Der neue Kommutant ist größer als der vorherige. Die Quelle erhält damit nicht automatisch den Operator, der jeweils neu durch Projektion auf diesen Kommutanten gebildet wird.

## 2. Exakter Kollisionszeuge

Wähle
P=I2, Y=diag(1/5,4/5), F=diag(1,3),
K=2I2+sigma_x, W=(I2+sigma_x/2)/2.

F ist strikt positiv, W hat Eigenwerte1/4 und3/4, K hat Eigenwerte1 und3. Das volle Persistenzereignis besitzt keinen Seed.

Die aus derselben Quelle berechneten Lasten sind
Lambda_C=5/2, Lambda_B=11/10,
alpha=11/36, beta=25/36.

Für die Lastfunktion g_alpha(y)=[alpha+beta y²]/(1+y)² gilt exakt

g_alpha(1/5)=g_alpha(4/5)=25/108.

Die zwei verschiedenen Y-Eigenwerte werden also durch ein tatsächliches vollständiges Quellereignis gleich. Der Kernel-Kohärenzfaktor ist gleichzeitig

h=(alpha+beta*(1/5)*(4/5))/
sqrt[(alpha+beta/25)(alpha+16beta/25)]
=5/6.

Vorher ist D_Y(K)=2I, weil Y zwei verschiedene Eigenräume besitzt. Nachher ist Y_out=(25/108)I und hat einen einzigen zweidimensionalen Spektralraum; deshalb D_Yout(K_out)=K_out=2I+(5/6)sigma_x.

Es folgt exakt
tr(W H_Y)=2,
tr(W_out H_Y,out)=29/12,
Delta E=5/12.

Der Operator H_Y ist also kein universell erhaltener Energieoperator auf der gesamten vollen BFG-Klasse. Eine feste Einheit oder ein konstanter Nullpunkt kann den nichtverschwindenden Erwartungsdefekt nur skalieren bzw. unverändert lassen.

Diese exakte Aussage benutzt **nicht** das numerische Zusammenfassen fast gleicher Eigenwerte. Die Gleichheit25/108 ist symbolisch bewiesen. In der Originalcode-Kontrolle differieren die zwei Gleitkommawerte um etwa5.6e-17; die bei der Auswertung verwendete volle Kollisionspartition ist durch den exakten Beweis fixiert.

## 3. Formationsräume als naheliegende Alternative

Im Kollisionszeugen würde das nichtentartete F=diag(1,3) die alten Modenrichtungen weiterhin unterscheiden. Man könnte daher H_F=D_F(K) statt H_Y prüfen. Das ist eine andere Ablesung; die Quelle bestimmt damit noch keine allgemeine Priorität zwischen Y und F.

Ein vorab festgelegter Gegenfall lautet
Y=diag(1/5,3/10), F=I+sigma_x/2,
W=(I+sigma_x/2)/2, K=2I+sigma_x.

F ist positiv und bleibt im ausgerichteten vollen Quellsektor exakt konstant. Da seine Diagonaleinträge in der Y-Basis beide1 sind, ergeben die Lasten alpha=8/133 und h=31/sqrt(1001). K und F kommutieren vor und nach dem Ereignis, also

H_F,in=K,
H_F,out=Phi(K)=2I+h sigma_x.

Die Energieerwartung ändert sich von5/2 auf2+h/2. Hier ist W=F/tr F; beide in I57 genannten Zustandskandidaten stimmen daher überein. Der Defekt kann nicht durch den Wechsel zwischen diesen beiden Zustandslesungen beseitigt werden.

Der feste Formationsrahmen ersetzt somit nicht allgemein den dynamisch erforderlichen Erhaltungssatz. Eine gemeinsame oder priorisierte Rahmenkonstruktion wäre erneut auf Quellenwahl, Geschlossenheit und physikalische Bedeutung zu prüfen.

## 4. Erhaltene Alternativen und ihre Grenzen

Die kollisionsfreie aktuelle Y-Projektion bleibt als positive mathematische Teilklasse erhalten. Beispielsweise bestätigt der Kontrollzustand mit Y=diag(1/5,3/10),F=I im geprüften Ereignis H_Y,out=H_Y=2I.

Im vollen festen Sektor sind alle späteren Y_j Funktionen des Anfangs-Y_0. Seine Spektralräume können sich unter solchen Funktionen zusammenführen, aber nicht auseinander aufspalten. Deshalb kann es höchstens d_0-1 Ereignisse mit neuen Verschmelzungen geben, wenn d_0 die anfängliche Zahl verschiedener Y-Eigenwerte ist. Die aktuelle H_Y-Ablesung ist zwischen solchen Ereignissen konstant. Es wird daraus **keine uniforme obere Schranke für den Ereigniszeitpunkt der letzten Kollision** abgeleitet.

Man kann auch die ursprüngliche Spektralzerlegung als zusätzlich gespeicherte Daten festhalten:
H_tracked,j=sum_lambda P_lambda(Y_0) K_j P_lambda(Y_0).
Dieser Operator bleibt im vollen Sektor konstant. Nach einer Kollision ist diese alte Zerlegung aber nicht allein durch den dann aktuellen Y-Eigenraum bestimmt. Die Wahl/Retention solcher Projektoren ist daher von der momentanen Y-Ablesung und von einer physikalisch ausgewählten Hamiltonianabbildung zu unterscheiden. Vorhandene F-/W-Daten könnten historische Richtungen in einzelnen Zuständen auflösen; eine universelle Priorität folgt daraus nicht.

Weder die aktuelle noch die historische Konstruktion definiert bereits eine räumliche Translations-/Impulsstruktur, eine physikalische Uhr oder eine empirische Energieeinheit.

## 5. Frische Kontrollen und numerische Grenze

Vier vollständige Originalereignisse, alle nichtterminal:

1. Exakter Kollisionszeuge: alpha≈0.3055555555555555, Y_out≈(25/108)I, H_Y-Erwartung2 ->2.416666666666667.
2. Kollisionsfreier positiver Kontrollfall: Operatorrest ||H_Y,out-H_Y||_F=6.280369834735101e-16.
3. F-Projektionsgegenfall: F-Feldrest0, Operatoränderungsnorm0.028544077943305043, Erwartung2.499999999999999 ->2.4899081444617845.
4. Komplexe unitäre Eichversion des Kollisionszeugen, Seed20261031: maximaler H-Rest9.985997127080695e-16.

Symbolisch alpha11/36, exakte Kollision25/108, h5/6 und Erwartungsdefekt5/12 geprüft. Numerische Eigenraumtoleranzen werden nicht als Beweis einer Kollision verwendet; die Reproduktion behandelt den exakt belegten skalaren Ausgang ausdrücklich als einen Spektralraum und kontrolliert seinen Gleitkomma-Residuum.

Vollständiger Prüftext/Ausgabe: [COMMUTING_READOUT_CHECKS.md](COMMUTING_READOUT_CHECKS.md). Keine Audit-/Workflow-/Originalcodeänderung; kein neuer Remote-CI-Pass behauptet. Lokale Kontrollzahlen und letzter Remote-geprüfter Code bleiben in CI_VALIDATION.md getrennt.

## 6. Nächste sachliche Abhängigkeit

Ein Energieoperator, der aus der Quelle als aktuell kommutierender K-Anteil gewonnen werden soll, benötigt eine präzise Regel für Spektralverschmelzungen oder eine unabhängig begründete Einschränkung auf kollisionsfreie Zustände. Historische Labels können eine mathematische Erhaltung liefern, sind aber als zusätzlich behaltene Daten offenzulegen und physikalisch zu rechtfertigen.

Eine solche zusätzliche Ableseregel ist von der fehlenden M_prep-/Quantenzustands-/Energiekalibrierung und einer vollständigen gekoppelten Austauschbilanz zu unterscheiden. Impuls, Raumrelation, Uhr und Lorentz-/Einstein-Brücke bleiben offen. Der hier begrenzte Kandidatenvergleich entscheidet keine allgemeine Unmöglichkeit physikalischer BFG-Energie.
