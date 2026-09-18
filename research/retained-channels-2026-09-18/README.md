# Verlorene Kanäle: exakte Gram-Zerlegung und Informationsgrenze

Ausgangsstand: 2e680c2d637f82d6455fa32f8ab6d8726116c22a.
Fortsetzung der G1-Kompatibilitätsprüfung; keine neue universelle Closure.

## 1. Verlustfreie Zerlegung bei W=L=I

Seien U†U=I, P=UU† und B2=B_C⊕B_C. Setze

    B_tan=U†B2U, E=(I-P)B2U.

Dann ist B2U=U B_tan+E und U†E=0. Daher gilt exakt

    U†B2†B2U = B_tan†B_tan + E†E.

Beweis: Ausmultiplizieren; die beiden gemischten Terme verschwinden wegen
U†E=0. Der gestapelte Faktor B_aug=[B_tan; E] reproduziert somit die vollständige
eingeschränkte Gramlast. Dies erfindet keinen freien Koeffizienten: E wird aus
den vorgegebenen B_C und U berechnet. Diese Identität rekonstruiert jedoch
nicht das noch fehlende vorgelagerte B_C aus einem beliebigen BFG-Zustand.

Für den bisherigen Kandidaten gilt B_tan=0 und E†E=1. Mitgeführte äußere
Kanäle liefern damit wieder Y=1 und die neutrale Paketantwort 1/4; die rein
tangentiale Rechnung liefert Y=0 und die Antwort 1/2. Der Widerspruch verschwindet
also als Buchhaltungsverlust, wenn die vollständigen Kanaldaten erhalten werden.
Das ist keine Herleitung ihrer Erhaltung als universelles BFG-Gesetz.

## 2. Minimale Information für die Last, nicht für die ganze Dynamik

Für die Gramlast genügt Delta=E†E. Jeder Faktor F mit F†F=Delta hat mindestens
rank(Delta) Ausgabezeilen, weil rank(F†F)=rank(F). Die Spektralzerlegung
Delta=V_r diag(lambda_i) V_r† mit lambda_i>0 liefert
F=diag(sqrt(lambda_i)) V_r† mit genau r=rank(Delta) Zeilen.
Die positive Quadratwurzel sqrt(Delta) ist eine eindeutige quadratische
Darstellung mit gegebenenfalls zusätzlichen Nullrichtungen; der minimale
rechteckige Faktor ist nicht als Basisdarstellung eindeutig.

Delta erhält nur die Gramenergie. Es erhält nicht die Richtung des äußeren
Kanals und reicht im Allgemeinen nicht zur Rekonstruktion späterer Kopplungen,
Ableitungen oder des Transports aus. Gleiche F†F dürfen deshalb nicht als
vollständig identische Zustände behandelt werden, solange keine entsprechende
dynamische Äquivalenz bewiesen ist.

## 3. Aus der komprimierten Kohärenz allein ist Delta nicht rekonstruierbar

Im flachen Beispiel seien S=[[0,1],[1,0]], c_a(t)=I+a t S und
u=(1,0,1,0)^T/sqrt(2). Für jedes reelle a gilt lokal, auf einem hinreichend
kleinen Intervall, c_a(t)>0. Für alle t ist

    u†(c_a(t)⊕c_a(t))u = 1,
    u†(∂_t c_a ⊕ ∂_t c_a)u = 0,
    Delta_a = a².

Somit kann keine Funktion allein des gesamten komprimierten Feldes c'(t)
(auch nicht seiner beliebig vielen Ableitungen) für alle a die richtige
Delta_a liefern: derselbe Input müsste verschiedene Outputs erzeugen.
Dieser Nichtidentifizierbarkeitssatz betrifft genau die komprimierten c-Daten,
nicht einen erweiterten Zustand, der bereits Y oder die äußeren Kanäle enthält.
Die jeweiligen Ausgangslasten Y_a=a²I sind verschieden. Es wird ausdrücklich
nicht behauptet, dass diese Familie denselben vollständigen Ausgangszustand hat.

## 4. Allgemeines positives W und rechteckige Faktoren

Für gelieferte B,W,L und eine Isometrie U in den verdoppelten Eingaberaum setze

    T=(W⊕W)^(1/2)(B⊕B)(L⊕L)U.

Für jede orthogonale Projektion Pi im so gewichteten Ausgaberaum gilt

    U†(Y⊕Y)U = T†T
             = (Pi T)†(Pi T) + ((I-Pi)T)†((I-Pi)T).

Dies folgt wiederum durch orthogonale Zerlegung und funktioniert mit
rechteckigen B und L bei passenden Domänen. Eine physikalisch ausgezeichnete
Projektion Pi wird durch diese Identität nicht bestimmt. Insbesondere darf
man die ungewichtete Kanalzerlegung nicht unverändert benutzen, wenn W
zwischen den Kanälen koppelt: dann können gemischte Terme beitragen.

Beispiel: v=(1,1), P=diag(1,0), W=[[1,1/2],[1/2,1]]. Dann ist v†Wv=3,
während (Pv)†W(Pv)+((I-P)v)†W((I-P)v)=2. Die fehlende Einheit ist der
gemischte Beitrag. Eine naive Addition ungewichteter Kanalenergien wäre falsch.

## 5. Konsequenz für den internen Zustandsvertrag

Ein verlustfreier Rebuild aus bekannten Vorgängerfaktoren ist möglich, wenn
deren Wirkung auf den aktiven Eingabeträger bis in den vollständigen
Ausgaberaum erhalten bleibt. Für die reine Lastberechnung kann das als T
oder T†T gespeichert werden. Eine semantische Rekonstruktion von B_C=D_cov c
aus dem neuen komprimierten c allein ist dadurch aber nicht gewonnen.

Der nächste offene Nachweis ist eine **geschlossene Transformationsregel**
für die erweiterten Daten unter weiteren Schritten, einschließlich D_cov,
W_N,L_C und R. Solange diese Regel nicht aus BFG folgt, bleibt Kanalmitführung
ein begründeter Erweiterungsvorschlag, keine gelöste universelle Rekonstruktion.
Insbesondere werden die sieben Probleme hier nicht als abgeschlossen gemeldet.

## Audit und Kontrolle

Die Quellenformeln sind V2 §6 Gl.22–24 und V4 S.10 Gl.39–40. Die drei Auditdateien
werden gemäß dem [Register](../prediction-audit-2026-09-18/sources.json) angewandt:
Claim-State und Redescription (Complete Edition), Wahrung negativer Befunde und
Prüfumfang (Workflow Master), Trennung von Quellen und Modellergänzung (Context
Recovery). Keiner der neuen Sätze setzt eine empirische Messbrücke voraus.

`check.py` kontrolliert mit exakter rationaler Arithmetik die beiden Teile der
Gramidentität, eine Familie identischer komprimierter Felder mit verschiedenen
Defekten und den gewichteten Gegenfall. Die dort verwendete unnormierte
Trägerrichtung wird durch ihren Normquadratfaktor 2 korrekt normalisiert.
Keine Änderung des Produktionscodes oder der Originalpaper.
