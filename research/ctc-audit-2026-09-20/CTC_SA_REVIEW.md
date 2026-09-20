# Prüfung der spektral ausgerichteten CTC-Schließung

## Ergebnis

Der eingereichte Entwurf definiert einen weitgehend nachvollziehbaren endlichen Modellzweig. Die algebraischen Formeln für Faktoren, Analyseoperator, polaren Transport, aktualisierten Parameter und Zustandsvektor stimmen. Die Zahlen des Beispiels wurden erneut exakt nachgerechnet.

Die behauptete Gesamtschließung benötigt jedoch Präzisierungen: Die Zustandsklasse muss den vorgeschriebenen Rekursionsoperator ausdrücklich enthalten; der Abbruch bei Dimension zwei ist als zusätzliche Randfallregel festzulegen; der neue Gram-Rebuild ist keine Fortsetzung des zuvor bewiesenen Gram-Kompressionssatzes. Die neuen Regeln bestimmen ein Modell, sie werden nicht durch die ursprünglichen BFG-Axiome erzwungen.

Prüfobjekt: eingereichter Text „Vollständige bedingte Schließung von Gram-Rekonstruktion, Rekursions-Rebuild und Iterationsfortsetzung“, lokal eingereichter Auditentwurf. Quellenabgleich: zuvor extrahierte Unified-V4-Architektur, insbesondere S. 5, Gleichungen 5–7, sowie Analyse, Kompression und Formationgate. Originale und GitHub bleiben unverändert.

## 1. Bestätigte Rechnungen

Unter den gewählten Regeln gilt:

    D_cov = sqrt(eta) c^(-1), W_N=L_C=I,
    B_C=sqrt(eta) I, H_C=Y_C=eta I.

Das ist eine eindeutige Faktorisierung nach Festlegung dieser Regeln. Es ist keine Eindeutigkeit unter allen möglichen Faktorisierungen und kein Nachweis einer kovarianten Ableitung im geometrischen Sinn.

Für den vorgeschriebenen Rekursionsoperator und P=I−P_max(K) gilt

    a(eta)=eta/((1+eta)sqrt(1+eta²)),
    A=a(eta)[P;P],
    J=[P;P]/sqrt(2),
    E=1/2 [[P,P],[P,P]].

Die verdoppelten Kapazitäten reduzieren diesen Range. In Supportkoordinaten werden sie auf die ersten d−1 Eigenmoden eingeschränkt. Ihre Kommutativität, die positive Untergrenze von c und die geforderte Ordnung des verbleibenden Spektrums bleiben für d≥3 erhalten.

Mit t=||PD||²/||D||² gilt wegen voller Unterstützung 0<t<1 und

    eta_next=2 a(eta)² t,
    D_next_support=sqrt(2)a(eta)/(1+eta_next) PD.

Der positive gemeinsame Vorfaktor erhält die nichtverschwindenden verbleibenden Komponenten. Der Satz für d≥3 ist nach der unten genannten Präzisierung der Zustandsklasse korrekt.

## 2. Zustandsklasse ausdrücklich vervollständigen

Abschnitt 3 führt R_C als Koordinate auf, schreibt dort aber nicht ausdrücklich R_C=R_C[K] vor. Der Beweis verwendet diese Identität bereits für den alten Zustand. Ein beliebiger R_C bei sonst gleichen Daten würde einen anderen oder keinen peripheren Raum liefern.

Ergänze deshalb als Klassenbedingung:

    R_C=(I−P_max(K))+r(K)P_max(K),
    r(K)=(lambda_(d−1)−lambda_1)/(lambda_d−lambda_1),
    Y=eta I, eta>0.

Alternativ entferne R_C aus den primitiven Koordinaten und definiere es ausdrücklich als abgeleitete Größe. Dasselbe gilt für die deklarierten Faktoren und N_R=I. Die Eigenmoden sind nach den einfachen Eigenwerten von K zu ordnen. Damit bleibt die Definition unabhängig von Eigenvektorphasen.

## 3. Der neue Gram-Rebuild ersetzt die alte Vererbungsregel

Da Y=eta I gilt, liefert Kompression des alten Gram-Operators immer

    E(Y⊕Y)E|Range = eta I_Range.

Der neue Entwurf setzt dagegen

    Y_next=eta_next I_Range.

Im Beispiel ist bereits eta=1 und eta_next=1/5. Die beiden Operatoren sind verschieden.

Tatsächlich gilt allgemein

    eta_next/eta = [2 eta/((1+eta)²(1+eta²))] t <1,

weil (1+eta)²>2 eta und t<1. Der neue Gram-Parameter sinkt also bei jedem nichtterminalen Schritt strikt. Die alte Gram-Kompressionsidentität wird in dieser Klasse in keinem solchen Schritt erfüllt.

Das macht den neuen Rebuild nicht algebraisch falsch. Es bedeutet, dass die Faktoren frisch rekonstruiert werden und D_cov_next nicht die bloße Kompression des alten D_cov ist. Der historische bedingte Gram-Vererbungssatz bleibt richtig, ist aber auf diese neue Faktoraktualisierung nicht anwendbar.

Erforderliche Kennzeichnung: „Neuer skalarer Gram-Rebuild; keine Erhaltung des alten Gram-Operators durch Kompression.“ Entsprechend dürfen frühere Stabilitätsbeweise mit G_next=(G⊕G)|Range nicht unverändert übernommen werden.

## 4. Abbruch bei Dimension zwei ist nicht allein durch eine undefinierte Zahl bewiesen

V4 schreibt einen positiven Abstand zwischen erstem und zweitem Eigenwert vor. In Dimension eins fehlt der zweite Eigenwert. Daraus folgt zunächst: Diese Formel ist dort nicht definiert. Daraus folgt nicht ohne eine Regel für fehlende Daten, dass ein boolesches Gate den Wert falsch erhält.

Ein einzelner negativer einfacher Eigenwert kann in Dimension eins durchaus isolierte Minima des Quartikfunktionals erzeugen. Für K=[−1] ist

    F(x)=−x²/2+x⁴/4

bei x=±1 minimal; F''(±1)=2>0. Fehlender zweiter Eigenwert bedeutet deshalb nicht mathematisch unmögliche Formation.

Saubere endliche Modellregel:

    Für d=2 setze U_CTC(X)=⊥, weil dieser Modellzweig
    nur Kandidaten mit mindestens zwei Eigenmoden zulässt.

Diese Randfallregel ist zulässig und macht die Totalisierung eindeutig. Sie ist als zusätzliche CTC-Festlegung beziehungsweise ausdrücklich erweiterte Gate-Definition zu kennzeichnen. Dann sind genau d0−2 nichtterminale Übergänge und der anschließende Abbruch bewiesen. Die Formulierung „keine Sonderregel erforderlich“ ist zu streichen.

## 5. Neue Modelleindeutigkeit ist keine hergeleitete Einzigartigkeit der Regeln

Die Normquote für eta_next, der größte Formationmodus als stabiler Sektor und die rationale Funktion r(K) sind explizite neue Modellentscheidungen. Basisunabhängigkeit und fehlende frei einstellbare Zahlen machen diese Entscheidungen nicht mathematisch alternativlos.

Beispielsweise bleibt auch r(K)² ein aus demselben Spektrum eindeutig bestimmter Wert in [0,1), mit derselben persistenten Dimension und ohne neuen numerischen Parameter. Das bisherige Material liefert kein Auswahlargument zwischen diesen Regeln.

Die Einstellung N_R=I und R=R_C[K] realisiert die ältere formale Gleichung MRM*. Die zusätzliche Behauptung einer vollständigen Einbettung in die Strong-Universal-Fassung durch C_E=R_C[K] benötigt einen Abgleich mit sämtlichen dortigen Definitionen von C_E und U_Omega. Positive Kontraktivität allein beweist diesen Quellenanschluss nicht.

## 6. Zusätzlicher positiver Befund: Kontraktion der neuen tatsächlichen Folge

Der neue Rebuild besitzt eine eigene, direkt beweisbare Energieabschätzung. Schreibe

    E_n=||D_n||²_(G_n).

Aus eta_next=||A_DD||²_(G⊕G)/E_n und der skalaren Metrik folgt

    E_next/E_n = eta_next/[(1+eta_next)(1+eta)].

Außerdem gilt a(eta)²≤1/8, denn

    (1+eta)²(1+eta²)−8eta²
      =(eta−1)²(eta²+4eta+1) ≥0.

Wegen t<1 ist deshalb 0<eta_next<1/4. Somit

    E_next/E_n <1/5.

Für jede existierende nichtterminale Kette folgt E_n≤5^(−n)E_0. Das ist eine nicht notwendig scharfe, aber gültige obere Abschätzung. Sie betrifft nur diesen skalaren normalen Modellzweig, keine allgemeine nichtnormale oder unendlichdimensionale Dynamik und keine unbegrenzte Fortsetzung der Gates.

## 7. Exakte Beispielkontrolle

| Neue Dimension | eta | Energie ||D||²_G |
|---|---:|---:|
| 5, Anfang | 1 | 10 |
| 4 | 1/5 | 5/6 |
| 3 | 25/624 | 625/23364 |
| 2 | 324480000/164268811201 | 3515200000000/69326858847152401 |

Die im Eingabetext angegebenen eta-Werte und D_4=(5/12)(1,1,1,1) stimmen. Frühere Energie- und Zustandswerte des Modells mit festem eta=1 gehören zu einer anderen Modellversion und dürfen nicht vermischt werden.

## Korrigierter Hauptsatz

Für die ausdrücklich definierte endliche Klasse mit kommutierenden Kapazitäten, einfachem geordnetem Formation-Spektrum, voller Unterstützung des Difference-Vektors, skalarem positivem Gram-Load und dem vorgeschriebenen R_C[K] ist der neue CTC-Schritt für d≥3 eindeutig und bildet nach C_(d−1) ab. Der neue Gram-Rebuild und der Rekursions-Rebuild sind wohldefiniert; die tatsächliche Zustandsenergie nimmt ab. Mit der zusätzlichen Terminalregel U_CTC(C_2)=⊥ und U_CTC(⊥)=⊥ entsteht eine totalisierte Iteration mit genau d0−2 nichtterminalen Übergängen.

Status: belastbarer bedingter endlicher Modellzweig nach den genannten formalen Ergänzungen. Keine quellenintern erzwungene Rekonstruktion, keine Gram-Vererbungsidentität, keine Lösung der sieben universellen BFG-Probleme.
