# Herleitungen aus der BFG-Bauform

Quellen: Structural Strong V2 §6,7,23,24; Compact V4 S.7–11 Gl.27–46.
Die Originale stehen in ../../papers, ihre Fingerabdrücke im vorigen
[Quellenregister](../prediction-audit-2026-09-18/sources.json).
Alle nachstehenden zusätzlichen Voraussetzungen sind explizit. Die Sätze sind
bedingte mathematische Resultate, keine empirischen Aussagen.

## 1. Zustandsvertrag statt bloßem Vektorupdate

Ein ausführbarer Zustand muss mindestens den Träger H, den Paketvektor d,
die Kapazitäten D,c,N, die Last Y, den rekursiven Endomorphismus R und die Daten
enthalten, aus denen die Rekonstruktionsfunktionen bestimmt werden. Die Metrik
G=I+Y ist abgeleitet. Der Träger und alle Operator-Domänen gehören zum Vertrag.
Die Notation X_next=C_N(Y_next)d_cross allein aktualisiert nur einen Vektor.
Sie ist erst dann ein vollständiger State Update, wenn die übrigen Größen
eindeutig daraus oder aus dem Vorgänger berechnet werden können.

Sind solche Funktionen F_B,F_W,F_L und F_R fest definiert, ergibt sich der
bedingte Schritt: Split und J berechnen; auf H_next=Ran(J) Kapazitäten nach
Gl.39 komprimieren; Faktoren auf diesem Träger rekonstruieren; Gramlast nach
Gl.40 bilden; d_next=(I+Y_next)^-1 d_cross; R_next=F_R(X, transportierte Daten)
berechnen. Alle Voraussetzungen des nächsten zulässigen Zustands sind zu prüfen.
Ein falscher Operator-Domain ist ein Spezifikationsfehler, keine physikalische
Terminalität. Die BFG-Gate-Ablehnung erzeugt dagegen den Terminalzustand.

Dies ist eine konditionale Spezifikation, keine Herleitung der fehlenden F.

## 2. Rekonstruktion ist aus Positivität nicht eindeutig

Für gegebene Faktoren gilt mit K=W_N^(1/2) B_C L_C die Identität Y=K†K.
Sie erzwingt Positivität, aber bestimmt K nicht. Schon W_N=L_C=1 und B_C=b
erlaubt jedes Y=|b|²; b=1 und b=2 liefern unterschiedliche neutrale Antworten.
Dieser Gegenbeweis betrifft die Behauptung, die Gram-Form allein bestimme die
Rekonstruktion. Er behauptet keine Inkonsistenz einer künftig spezifizierten F.

Selbst bei bekanntem Y bleiben Faktoren nicht eindeutig: für invertierbares S
auf dem Zwischenraum sind B'_C=B_C S und L'_C=S^-1 L_C äquivalent, da
B'_C L'_C=B_C L_C. Entsprechend kann ein Wechsel des Ausgaberaums von B_C
durch kompensierte Transformation von W_N aufgefangen werden. Ein Anspruch
auf kanonische Faktoren benötigt daher einen spezifizierten Quotienten oder
eine zusätzliche Eichwahl. Die Wahl B_C=sqrt(Y), W_N=L_C=I rekonstruiert ein
schon bekanntes Y, erklärt aber nicht Y_next aus X und ist deshalb zirkulär
als Lösung dieses Problems. V2 §24 fordert ausdrücklich ein vorgelagertes Modell.

## 3. Gram-Rebuild: endlicher Satz und Implementierung

Seien B:E→F, W:F→F hermitesch positiv semidefinit und L:H→E.
Dann H_C=B†WB und Y=L†H_C L sind hermitesch positiv semidefinit, denn

    <v,H_C v> = ||W^(1/2)Bv||² >= 0,
    <x,Yx> = ||W^(1/2)BLx||² >= 0.

Somit G=I+Y positiv definit, C=G^-1 wohldefiniert, B_N=I-C positiv
semidefinit und C+B_N=I. Durch Diagonalisierung von Y haben C und B_N
Eigenwerte 1/(1+y) und y/(1+y), y>=0. Unter unitärem Basiswechsel U auf H
transformieren Y,G,C,B_N,Z durch A→U†AU. Das ist die erforderliche
Basisunabhängigkeit in orthonormalen Koordinaten, keine allgemeine Aussage
über nichtorthonormale Koordinaten ohne mittransformierte Metrik.

`bfg_lab.gram.rebuild` implementiert genau diese Rechnung mit expliziten
Dimensions- und Endlichkeitsprüfungen. Es arbeitet numerisch, nicht mit
Intervallzertifikaten. Kleine negative Gewichtseigenwerte innerhalb der
angegebenen Toleranz werden auf null gesetzt und gezählt; die Norm einer
zulässigen Hermitisierung wird ebenfalls ausgegeben. Das Ergebnis bezieht sich
damit auf das bereinigte Gewicht. Außerhalb der Toleranz wird abgewiesen.
Die Default-Toleranz ist eine numerische Konvention, kein BFG-Axiom.

## 4. Warum Polartransport allein den rekursiven Transport nicht schließt

J:H→H_next ist auf E=supp(A†A) isometrisch und auf E-perp null.
Der Kapazitätstransport P_next(Q⊕Q)P_next ist durch Gl.39 bestimmt.
Ein rekursiver Transport ist dagegen ein Endomorphismus H_next→H_next.
J allein hat diesen Typ nicht.

Eine mögliche zusätzliche Regel wäre R_next=J R J†. Sie ist auf H_next
unitär äquivalent zur Kompression P_E R|E. Ohne R-Invarianz von E darf man
(P_E R|E)^n nicht durch P_E R^n|E ersetzen. Potenzbeschränktheit von R
überträgt sich dann nicht automatisch. Beispiel: R=[[2,1],[-2,-1]] erfüllt
R²=R und ist potenzbeschränkt. Seine Kompression auf span(e1) ist [2] und
wächst unter Iteration. Dies ist eine Warnung vor der allgemeinen
Kompressionsschlussfolgerung, keine Behauptung, dass dieses E aus jedem
BFG-Split entsteht. Für eine BFG-spezifische Regel wäre genau diese zusätzliche
Support-Invarianz oder eine andere ausreichende Stabilitätseigenschaft zu beweisen.

Ist E hingegen R-invariant und R potenzbeschränkt, so gilt
R_next^n=J(R|E)^n J† und die Potenzbeschränktheit folgt. Die Wahl dieser Regel
und der Invarianznachweis sind zusätzliche Pflichten, keine Konsequenz von J†J=P_E.

## 5. Bedingter Iterationssatz

Sei S die vollständig spezifizierte Menge zulässiger Zustände. Angenommen,
alle in 1 genannten Funktionen sind eindeutig auf ihrer erklärten Domäne,
jeder Gate-erfolgreiche Schritt liegt wieder in S, und jeder Gate-fehlgeschlagene
Schritt wird auf bot abgebildet. Setze U(bot)=bot. Dann existiert für jedes
X0 in S vereinigt {bot} genau eine Folge X_n=U^n(X0), n in N.

Beweis: X0 ist gegeben. Ist X_n eindeutig definiert, ist U(X_n) wegen der
Voraussetzungen eindeutig definiert und wieder im selben erweiterten Zustandsraum.
Induktion liefert Existenz und Eindeutigkeit für alle endlichen n. Daraus folgt
weder Konvergenz, ein unendlicher nichtterminaler Zweig, noch eine Naturrealisation.
Der offene Teil ist der Nachweis der Voraussetzungen für die BFG-Funktionen.

## 6. Nichtnormaler endlicher Fall

Für eine endliche komplexe Matrix R gilt: R ist potenzbeschränkt genau dann,
wenn alle Eigenwerte |lambda|<=1 haben und alle Jordanblöcke bei |lambda|=1
Größe eins besitzen. Beweis: äußere Eigenwerte wachsen exponentiell;
nichttriviale periphere Jordanblöcke polynomial. Innere Jordanblöcke haben
polynomial mal exponentiell abklingende Potenzen, periphere einfache Blöcke
bleiben beschränkt. Ähnlichkeit verändert nur eine feste Normkonstante.

Daraus folgt H=W_per direkt-summe E_s, mit W_per der Summe peripherer
Eigenräume und E_s der inneren verallgemeinerten Eigenräume. R^n|E_s→0;
auf W_per sind Vorwärts- und Rückwärtspotenzen beschränkt. Die Rieszprojektion
entlang E_s kommutiert mit R, ist aber im Allgemeinen nicht G-orthogonal.
Der BFG-Split kann separat die metrische Projektion
P_G=W(W†GW)^-1 W†G verwenden. Die beiden Projektionen dürfen nicht vertauscht werden.

Damit ist die vorgeschlagene korrigierte Persistenzdefinition algebraisch auf
alle endlichdimensionalen potenzbeschränkten R erweitert. Sie ist ausdrücklich
eine Korrektur der fehlerhaften Span-Definition in Gl.27, keine Behauptung,
diese gedruckte Definition sei bereits äquivalent. Ein beliebiges nichtnormales R
ohne Potenzbeschränktheit fällt nicht unter diesen Satz. Eine robuste
Fließkomma-Zertifizierung nahe defekten Einheitskreiseigenwerten ist damit nicht
geliefert; die bestehende API wird deshalb nicht durch einen bloßen eig-Aufruf erweitert.

## 7. Unendlichdimensionale Gram-Realisierung

Auf Hilberträumen sei die Komposition K=W^(1/2)BL dicht definiert und abschließbar.
Setze T=Abschluss(K). Die Form q(x)=||Tx||² auf Dom(T) ist abgeschlossen,
dicht definiert und nichtnegativ. Sie erzeugt den nichtnegativen selbstadjungierten
Operator Y=T†T. Daher sind C=(I+Y)^-1 und B_N=I-C beschränkt und positiv;
die Graphformnorm ist ||x||_G²=||x||²+||Tx||². Auf einem darin abgeschlossenen
Zeugenraum existiert die eindeutige orthogonale Projektion in dieser Norm.
Dies präzisiert V4 Gl.45–46 für die zusammengesetzte Gram-Bauform.

Die Domäne der Komposition ist explizit
{x in Dom(L): Lx in Dom(B), BLx in Dom(W^(1/2))}.
Ihre Dichtheit und Abschließbarkeit folgen nicht allein daraus, dass die
einzelnen Faktoren formal niedergeschrieben wurden. Auch die Bildung aller
nächsten Kapazitäten, Träger und Transportoperatoren muss diese Eigenschaften
erhalten. Die formale Produktform L†B†WBL darf ohne Domänennachweis nicht mit
T†T gleichgesetzt werden. V4s Resolventenkern löst diese Folgepflichten nicht.

Zusätzlich darf W_per aus 6 nicht allgemein übertragen werden: der einseitige
Shift auf l² erhält jede Norm, besitzt aber keine Eigenvektoren auf dem
Einheitskreis. Eine konkrete unendliche BFG-Realisierung benötigt daher eine
eigene Persistenzklasse und einen Iterationsnachweis. Endliche Trunkierungen
sind ohne Konvergenzsatz kein Ersatz.
