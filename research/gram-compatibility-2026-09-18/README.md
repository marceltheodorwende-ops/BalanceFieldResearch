# Interne Kompatibilität: G1 und B_C = D_cov c

Ausgangscommit: db36a7ca1d264ab7a3900f14af1d4283c346d30d.
Die Schreibweise „BC gleich DKF“ in der Anfrage wird als Bezug auf die bisher
diskutierte Quellenformel B_C=D_cov c gelesen, nicht als neue definierte Größe.

**Ergebnis:** G1 lässt sich unter expliziten Intertwining-Bedingungen aus dem
Gram-Rebuild herleiten. Diese Bedingungen sind in den vorhandenen BFG-Quellen
nicht allgemein bewiesen. Ohne sie ist G1 mit einer naheliegenden internen
Rekonstruktion nicht allgemein vereinbar. Ein vollständiger lokaler Kandidat
unten besteht das Formation-Gate, liefert aber G1-Last 1 und rekonstruierte Last 0.
G1 wird daher nicht als allgemeine interne BFG-Regel übernommen.

## Was aus den Quellen stammt

V2 §6 Gl.22–24 setzt B_C=D_cov c, H_C=B_C†W_N B_C und Y_C=L_C†H_C L_C.
V2 §24 fordert die konkrete vorgelagerte Konstruktion dieser Größen.
V4 S.10 Gl.39 komprimiert c und die übrigen Kapazitäten auf Ran(J), während
Gl.40 den positiven Rebuild fordert. Der G1-Vorschlag erweitert die
Kompressionsregel zusätzlich auf Y; diese Erweiterung ist kein Quellenaxiom.

Eine kovariante Ableitung eines Operatorfeldes c muss in einer konkreten
Realisierung spezifiziert werden. Der unten verwendete flache Spezialfall
D_cov=∂_t und die ortsfeste Trägerbasis sind ausdrücklich ausgewiesen. Der
Parameter t ist hier eine lokale Feldkoordinate, nicht der Rekursionsindex n.

## Bedingter interner Herleitungssatz

Schreibe zur Vereinfachung alle Zwischenräume endlichdimensional und gleich groß;
die Aussage überträgt sich mit getrennten Isometrien auf verschieden große
Zwischenräume. Sei U eine orthonormale Basis von Ran(J), P=UU† und

    B2=B_C ⊕ B_C, W2=W_N ⊕ W_N, L2=L_C ⊕ L_C.

Angenommen, die aus der neuen Kohärenzkapazität c'=U†(c⊕c)U und der neuen
kovarianten Ableitung tatsächlich rekonstruierten Faktoren B',W',L' erfüllen

    B' = D'_cov c',
    B2 U = U B',
    L2 U = U L',
    W' = U† W2 U.

Dann folgt durch Einsetzen, ohne zusätzlich G1 zu postulieren,

    L'† B'† W' B' L'
      = (B2 L2 U)† W2 (B2 L2 U)
      = U†(Y ⊕ Y)U.

Somit gilt G1 auf dieser Teilklasse. Die neue Last ist aus den gegebenen
Faktoren eindeutig. Die entscheidende zusätzliche Eigenschaft ist, dass die
Rekonstruktion mit dem Übergang auf den neuen Träger verträglich ist; insbesondere
darf B2 auf diesem Träger keine nicht mitgeführten Ausgabekanäle erzeugen.
Die Gleichung B2U=UB' ist stärker als B'=U†B2U.

Eine hinreichende konkrete Situation ist eine lokal konstante gemeinsame
invariante Trägerzerlegung für die relevanten Felder, die kovariante Ableitung
und L, mit entsprechend eingeschränktem W. Diese Situation muss nachgewiesen
werden; sie folgt nicht allein aus dem Polarzerlegungssatz. Bei einem bewegten
U müssen außerdem die Ableitungen von U und die induzierte Verbindung
berücksichtigt werden. Der Satz behauptet keine allgemeine Invarianz dieser
Teilklasse unter der nächsten BFG-Iteration.

## Exakter Verlustterm im einfachen Fall

Für W=L=I und B'=U†B2U gilt

    Y_G1 - Y_rekonstruiert
      = U†B2†B2U - (U†B2U)†(U†B2U)
      = U†B2†(I-P)B2U
      = E†E,  E=(I-P)B2U.

Der Unterschied ist positiv semidefinit. Gleichheit gilt genau dann, wenn
E=0. Das ist eine notwendige und hinreichende Bedingung in dieser ausdrücklich
begrenzten Situation. Für allgemeines W,L ist diese einfache Formel nicht
ohne zusätzliche Kompatibilitätsbedingungen übertragbar.

## Vollständiger lokaler Gegenfall

Auf H=R² setze S=[[0,1],[1,0]] und für |t|<1

    c(t)=I+tS, D_cov=∂_t, B_C=S,
    W_N=L_C=I, Y=S†S=I,
    d=e1, R=diag(1,1/2), Differenzkapazität=3I, Neutralkapazität=I.

c(t) ist im angegebenen Intervall positiv definit. Bei t=0 ist c=I.
Der persistente Raum ist span(e1), P_G=diag(1,0), C_N=B_N=I/2.
Beide Lasten und Gewichte sind 1/2. Der aktive Polarträger wird durch

    u=(1,0,1,0)^T/sqrt(2)

aufgespannt; in dessen Koordinaten ist das Paket 1/2. Komprimierte Kapazitäten
sind 3,1,1, daher Formation K=-1 mit einfacher isolierter Mode; der stabile
Persistenzabstand ist 1/2. Das Gate besteht, ohne eine Konvention für ein
leeres stabiles Komplement zu benötigen. Y, R und der aktive Träger sind hier
lokal t-unabhängig.

Nun ist c'(t)=u†(c(t)⊕c(t))u=1. Die induzierte Verbindung ist bei konstanter
Basis und flachem Ausgangstransport null. Also

    B'_C=∂_t c'=0, W'_N=L'_C=1, Y'_rekonstruiert=0.

G1 liefert dagegen u†I_4u=1. Tatsächlich ist
(S⊕S)u=(0,1,0,1)^T/sqrt(2) orthogonal zu u und hat Norm eins: E†E=1.
Die jeweilige neutrale Folgeantwort auf das Paket wäre 1/2 bzw. 1/4.

Dies ist ein Gegenfall gegen die *allgemeine Gleichsetzung* beider Verfahren
in der deklarierten flachen lokalen Klasse. Es ist keine vollständige
Realisierung sämtlicher BFG-Axiome oder ein Gegenbeispiel gegen alle denkbaren
anderen Definitionen von D'_cov. Wenn eine andere BFG-interne Ableitungsregel
diesen Fall ausschließen soll, muss sie ausdrücklich konstruiert werden.

## Konsequenz und nächste Beweispflicht

Eine echte bedingte Herleitung liegt jetzt für kompatible Trägerabbildungen
vor. Eine allgemeine Herleitung liegt nicht vor; der Gegenfall verhindert es,
G1 bloß umzubenennen und als internen Satz auszugeben.

Zu klären ist nun, ob BFG die notwendige Invarianz erzwingt oder ob die
Rekonstruktion die außerhalb des komprimierten Trägers liegenden Kanäle als
eigene Daten behalten muss. Letzteres würde den Zustandsvertrag erweitern;
es ist noch keine in den Quellen nachgewiesene Regel. Die Wahl eines beliebigen
W' kann den Gegenfall nicht retten: für B'=0 bleibt B'†W'B'=0.
Auch eine bloße Änderung von L' kann diesen Nulloperator nicht beseitigen.

Produktionscode und bisherige Quellen werden nicht geändert. Das Ergebnis
präzisiert, unter welchen zusätzlichen Bedingungen G1 brauchbar ist und wo
es als allgemeine Closure ausscheidet.
