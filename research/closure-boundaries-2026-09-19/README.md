# Abschluss dieser internen Ableitungsrunde: zwei weitere notwendige Voraussetzungen

Stand: 19.9.2026 (Europe/Berlin). Ausgangscommit:
5a24f8e1bb4a5e704d426be3c29f94388f20d8db.
Diese Stufe prüft die im Ledger angekündigte Aktualisierung mitgeführter Kanäle
und eine Domänenvoraussetzung der unendlichdimensionalen Einschränkung.

## A. Endlich viele lokale Ableitungsdaten bestimmen keine allgemeine Feldentwicklung

Sei S=[[0,1],[1,0]], m>=1 und a eine reelle Konstante. Definiere lokal

    c_a(t)=I+(t+a t^(m+1))S,
    D_cov=∂_t, B_a(t)=(1+(m+1)a t^m)S,
    W=L=I, Y_a(t)=(1+(m+1)a t^m)^2 I.

Für jedes feste a ist c_a(t) auf einem hinreichend kleinen Intervall um null
positiv definit. Alle c_a haben bei t=0 dieselben Ableitungen der Ordnungen
0 bis m. Insbesondere sind c(0), B(0), Y(0) gleich. Auch die bisherigen
äußeren Kanäle E(0) und deren Gramdefekt sind bei gleichem festen Träger gleich.
Dennoch ist

    ∂_t^(m+1)c_a(0)=(m+1)! a S,
    ∂_t^m Y_a(0)=2(m+1)m! a I.

Beweis: Differentiation der angegebenen Polynome. Der quadratische Term
in Y hat Grad 2m>m und trägt zur m-ten Ableitung am Ursprung nicht bei.

Daraus folgt: Für diese uneingeschränkte lokale Feldklasse gibt es keine
Funktion des m-Jets von c am Ursprung, die die nächste Ableitung für alle a
eindeutig liefert. Höhere vorgegebene endliche Ableitungsordnungen verschieben
das Problem, beseitigen es aber ohne Evolutionsgesetz nicht. Alle Beispiele
sind sogar analytisch. Eine konkrete Differentialgleichung mit ausreichenden
Anfangsdaten kann die Freiheit beseitigen; gerade diese Gleichung fehlt hier.

**Reichweite:** t ist eine lokale Feldkoordinate, nicht der Rekursionsindex n.
Dieser Satz widerlegt keine beliebige diskrete BFG-Update-Regel und beweist
nicht, dass ein vollständiger BFG-Zustand zwingend aus einem endlichen Jet
besteht. Er schließt die konkrete Abkürzung aus, aus endlich vielen bekannten
Ableitungs-/Kanaldaten ohne weitere Regel deren allgemeine lokale Entwicklung
abzuleiten. Die Verbindung zwischen lokaler Entwicklung und Rekursionsschritt
muss ebenfalls spezifiziert werden.

## B. Eine Hilbertraum-Isometrie garantiert keine zulässige Gramform-Einschränkung

Auf H=l²(N), N={1,2,...}, sei K die abgeschlossene Diagonalmultiplikation
(Kx)_n=n x_n mit Dom(K)={x: Summe n²|x_n|²<unendlich}. Dann ist
Y=K†K die positive selbstadjungierte Diagonalmultiplikation mit n².
Die zugehörige Formdomäne ist Q(Y)=Dom(K), dicht in H.

Der Vektor v=(1,1/2,1/3,...) liegt in H, aber nicht in Dom(K), denn
Summe |v_n|² konvergiert und Summe n²|v_n|²=Summe 1 divergiert.
Definiere die Isometrie U:C→H durch Uz=z v/||v||. Für z ungleich null liegt
Uz nicht in Dom(K). Daher hat die Komposition KU nur die Domäne {0} in C.
Sie ist nicht dicht definiert. Die formal eingeschränkte Form q(Uz)=||KUz||²
ist für keinen nichttrivialen z endlich. Es gibt hier keine aus dieser
Einschränkung erzeugte dicht definierte positive Gramform auf C.

Dies ist ein Gegenbeispiel gegen den Schluss „U ist eine Isometrie, also ist
der unbeschränkte Gram-Rebuild auf dem neuen Träger zulässig“. Es behauptet
nicht, dieses U werde von einem vollständig spezifizierten BFG-Generator
tatsächlich erzeugt. Ein solcher Generator müsste genau nachweisen, dass
seine Träger die erforderliche Formdomäne genügend treffen.

Eine hinreichende, stärkere Voraussetzung ist U:C→Dom(K) als beschränkte
Abbildung in der Graphnorm. Allgemeiner braucht KU einen dichten Definitionsbereich
und Abschließbarkeit; dann gilt der bereits dokumentierte Formensatz.
Diese Bedingungen müssen bei jeder Iteration erhalten bleiben.

## C. Konsequenz

Die algebraischen BFG-Bausteine liefern bedingte Sätze. Sie liefern ohne
zusätzliche konkrete Daten noch keine eindeutige universelle Entwicklung.
Die Fortsetzung einer allgemeinen Herleitung benötigt jetzt ein explizites
vorgelagertes Modell bzw. zusätzliche begründete Dynamik- und Domänenannahmen.
Weitere Matrixbeispiele oder höhere Testzahlen ersetzen diese Information nicht.

Es wird kein umfassender Unmöglichkeitssatz über BFG behauptet. Die obigen
Gegenbeispiele sind bewusst auf die jeweils angegebenen Schlussfolgerungen
begrenzt. Sie können durch stärkere Annahmen ausgeschlossen werden; deren
interne Begründung wäre dann der neue Arbeitsgegenstand.

## Audit und Verifikation

Complete Edition: genaue Claim-Grenzen, keine Verwechslung von t und n, aktive
Gegenprüfung. Workflow Master: negative Befunde und historische Stufen erhalten.
Context Recovery: keine zusätzliche Gleichung wird als vorhandenes BFG-Axiom
ausgegeben. Die drei Original-Auditquellen stehen im
[Register](../prediction-audit-2026-09-18/sources.json).

Quellenbezug: V2 §6 Gl.22–24 und §24; V4 S.11 Gl.45–46. Die neuen
Gegenbeispiele werden vollständig hergeleitet; sie sind keine Zitate aus den
Papern. `check.py` kontrolliert die Polynomkoeffizienten mit exakter rationaler
Arithmetik. Der unendliche Domänenbefund wird analytisch bewiesen und nicht
aus endlichen Trunkierungen abgeleitet. Produktionscode unverändert.
