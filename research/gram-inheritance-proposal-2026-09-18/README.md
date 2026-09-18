# Vorschlag G1: Vererbung der Gramform auf dem neuen Träger

Status: **zusätzliches Closure-Postulat zur Prüfung**, kein aus den vorhandenen
BFG-Papern bewiesenes Gesetz. Ausgangsstand: 64fdb181419e23ca21194b520ac657e3b7476256.
Der Auftrag ist, eine begründete Regel gegen die Rekonstruktionsmehrdeutigkeit
zu entwickeln. Hier wird eine konkrete Regel mit bedingtem Eindeutigkeitsbeweis
vorgelegt; ihre physikalische und vollständige BFG-Verträglichkeit ist offen.

## Herkunft und genaue neue Annahme

V4 S.10 Gl.39 komprimiert die verdoppelten Kapazitäten auf H_next=Ran(J).
Gl.40 fordert hingegen einen Gram-Rebuild aus nicht ausgeschriebenen Funktionen.
V2 §6 Gl.22–24 enthält die Gram-Bauform; §24 fordert deren vorgelagerte Konstruktion.
Keine dieser Stellen verlangt bereits, die *Gramlast* nach Gl.39 zu transportieren.

**Postulat G1:** Auf dem neuen Träger bleibt die quadratische Gramform des
verdoppelten Vorgängers unverändert eingeschränkt. Für jedes z in H_next gilt

    <z,Y_next z> = <z,(Y ⊕ Y)z>.

Dies überträgt ein bereits verwendetes Transportprinzip auf eine weitere Größe.
Es führt keinen einstellbaren Skalenparameter ein, ist aber selbst eine neue
Modellwahl. Parameterfreiheit beweist weder Einzigartigkeit unter allen möglichen
Closure-Regeln noch Naturgültigkeit. Die Normierung stammt aus dem vorgegebenen Y.

## Bedingter Eindeutigkeitssatz (endliche Dimension)

Sei Y>=0 hermitesch, J eine partielle Isometrie und P=JJ† die orthogonale
Projektion auf H_next. Unter G1 existiert genau ein hermitescher Operator
auf H_next mit der geforderten Form, nämlich

    Y_next = P(Y ⊕ Y)P | H_next.

Beweis: Für z in H_next gilt Pz=z, daher erfüllt die Kompression die Gleichung.
Sie ist positiv, da ihre quadratische Form nichtnegativ ist. Sind T1,T2 zwei
hermitesche Lösungen, verschwindet <z,(T1-T2)z> für jedes z. Die
Polarisationsidentität liefert alle Matrixelemente gleich null, also T1=T2.
Eine Übereinstimmung nur am tatsächlich beobachteten Paket z würde hierfür
nicht genügen; G1 verlangt sie ausdrücklich für **alle** Trägerrichtungen.

Für eine orthonormale Trägerbasis U lautet die Rechenform

    Y_next,coord = U†(Y ⊕ Y)U.

Bei U→UV mit unitärem V transformiert sie durch V†Y_next,coord V.
Damit ist das Ergebnis unabhängig von der gewählten orthonormalen Basis.
Dies ist keine Identifikation mit JYJ†: letzteres ist eine andere Transportregel.

## Gramfaktoren existieren, sind aber nicht kanonisch rekonstruiert

Sei bisher Y=L†B†WBL. Eine Darstellung der G1-Last in U-Koordinaten ist

    B_tilde = (B ⊕ B)(L ⊕ L)U,
    W_tilde = W ⊕ W,
    L_tilde = I.

Einsetzen ergibt exakt U†(Y⊕Y)U. Diese Faktoren zeigen die positive
Gram-Darstellbarkeit. Sie sind keine Herleitung der ursprünglichen Semantik
B_C=D_cov c und keine eindeutige Auswahl unter allen Faktorisierungen.
Die Transformationsfreiheit der Zwischenräume bleibt bestehen. G1 schließt
somit die Last-Mehrdeutigkeit im erweiterten Modell, nicht automatisch Problem 2
mit allen BFG-Bedeutungsanforderungen.

## Prüfung am bisherigen Gegenbeispiel

Im eindimensionalen Ausgangsbeispiel Y=1 ist Y⊕Y=I_2. Daher ist die Einschränkung
auf jeden eindimensionalen H_next gleich 1. G1 wählt zwingend Y_next=1 und
d_next=(1+1)^-1(1/2)=1/4. Der konkurrierende Rebuild Y_next=4 verletzt G1.
Die frühere Nicht-Eindeutigkeit aus Gl.37–41 allein bleibt trotzdem ein gültiger
Befund: Erst das neue Postulat unterscheidet die beiden Möglichkeiten.

## Neue überprüfbare Grenze: kein Anwachsen der Lastnorm

Für mI<=Y<=MI gilt nach Verdoppelung und Kompression

    m I_next <= Y_next <= M I_next.

Insbesondere ||Y_next||<=||Y||; bei iterierter G1-Regel wachsen obere
Lastspektralgrenzen nicht an. Außerdem dim(H_next)=rank(J)<=dim(H).
G1 kann deshalb aus einem endlichen Startträger keine wachsende Trägerdimension
und keine unbeschränkt zunehmende Lastnorm erzeugen. Diese Einschränkungen
müssen gegen den beabsichtigten BFG-Realisierungsanspruch geprüft werden.
Die Normgrenze allein beweist keine Konvergenz der gesamten Zustandsfolge.

Wenn BFG für eine konkrete Anwendung Spektralwachstum verlangt, wäre G1 dort
ungeeignet. Es wäre methodisch falsch, dann nachträglich eine freie Skalierung
einzuführen und weiterhin dieselbe parameterfreie Regel zu behaupten.

## Was damit erreicht ist und was als Nächstes zu prüfen ist

Erreicht: eine aus der BFG-Transportarchitektur motivierte, explizite zusätzliche
Regel; Eindeutigkeit der Folge-Last unter dieser Regel; positive Faktorisierung;
ein analytisch gelöstes Gegenbeispiel und eine harte Spektralgrenze.

Offen: Herleitung von G1 aus unabhängig begründeten Grundannahmen; Vereinbarkeit
mit B_C=D_cov c; vollständige Zustands- und R_next-Regel; nichtnormale
Persistenz unter diesem Transport; unendlichdimensionale Domänenfragen;
empirische Messbrücke. Eine Eigenständigkeit oder Überlegenheit gegenüber
Standard-Kompressionsdynamik ist nicht nachgewiesen.

Nächste Beweispflicht ist die semantische Verträglichkeit: Folgt die G1-Form
aus einer präzisen Transformation von D_cov, c, W_N und L_C, ohne diese Größen
nur nachträglich auf ein gewünschtes Y_next zurechtzulegen? Falls nicht,
bleibt G1 ein separat gekennzeichnetes Modellpostulat. Die bestehende
Produktionsrekursion wird deshalb durch diesen Vorschlag nicht ersetzt.

## Audit

Complete Edition: Quellenfolge, neues Postulat und bedingter Satz getrennt;
kein Eindeutigkeitsanspruch außerhalb G1. Workflow Master: keine Änderung der
Originale oder historischen Ergebnisse; negative Konsequenzen dokumentiert.
Context Recovery: V4 Gl.39 ist Motivation, Gl.40 kein vorgetäuschter Beweis von G1.
Die Original-Auditdateien sind im
[Quellenregister](../prediction-audit-2026-09-18/sources.json) identifiziert.

Analytische Kontrollen: Einsetzen der Faktoren, Polarisationsargument,
Rayleigh-Schranken und das eindimensionale Gegenbeispiel. Ein zusätzlicher
rechteckiger rationaler Kontrollfall wird in verification.md dokumentiert.
Keine vollständige Lösung der sieben Probleme und keine empirische Bestätigung.
