# Gegenprüfung: vier CTC-SA-Auswahlregeln

Stand: 21. September 2026. Auditobjekt: eingereichter Text „CTC-SA Audit: Sind die vier neuen Modellregeln aus BFG erzwungen?“. Referenzmodell: dokumentierter Stand 8378d8becac5780071baa4f6d3f29ba2dae09c6e. Kein erneuter vollständiger Quellenkorpus-Audit, kein neuer Gesamttestlauf und keine empirische Bestätigung.

## Entscheidung

**Der konstruktive Kern ist richtig. Annahme mit den unten genannten Präzisierungen.** Die angegebenen Gegenmodelle zeigen: Die jeweils aufgeführten schwächeren Strukturbedingungen erzwingen die vier konkreten Auswahlregeln nicht. Sie widerlegen weder die Konsistenz des festgelegten CTC-SA-Modells noch beweisen sie die Unmöglichkeit einer späteren internen Herleitung aus zusätzlichen, unabhängig begründeten BFG-Prinzipien.

Angewandte Auditkriterien aus den drei BFG-Auditdokumenten, aus BFG_Audit_Complete_Edition.docx, BFG_Audit_Workflow_Master.docx und BFG_X_Context_Recovery_Protocol_Master finish.docx (lokal im Audit vom 15. September 2026 dokumentiert): Claim-State, Unterscheidbarkeit, Redescription, Quellenhierarchie, Erhalt negativer Ergebnisse und Trennung von Definition, bedingtem Beweis, Implementierung und Empirie. Es werden keine historischen Quellen oder Modellgesetze umgeschrieben.

## A. Gram-Faktorisierung: bestätigt, mit begrenztem Geltungsbereich

Für endlichdimensionale quadratische Operatoren, c>0, eta>0, W>0, invertierbares L und unitäres U liefert

    D_cov = sqrt(eta) W^(-1/2) U L^(-1) c^(-1)
    B = D_cov c
    L* B* W B L = eta I.

Der Beweis folgt unmittelbar aus B L = sqrt(eta) W^(-1/2) U. Umgekehrt ist bei dieser Gramidentität U=eta^(-1/2) W^(1/2) B L isometrisch und im quadratischen endlichen Fall unitär. Damit ist die Parametrisierung in genau diesem Bereich vollständig. Sie ist kein entsprechender Satz für beliebige rechteckige, unbeschränkte oder differentialgeometrische Operatoren.

Schon W=L=I lässt B=sqrt(eta)U zu. Zusätzlich B>=0 erzwingt B=sqrt(eta)I. Die Positivitäts- und Normalisierungsannahmen sind zusätzliche Auswahlbedingungen.

Korrekte Formulierung: **Bei vorgegebenem Y bestimmen die angeführten Gramgleichungen dessen Faktoren nicht eindeutig.** Die Nicht-Eindeutigkeit der Faktoren allein beweist keine Nicht-Eindeutigkeit des nächsten Y; dafür liefert Abschnitt B eigenständige Gegenmodelle. Gleicher Gramoperator bedeutet gleiche reduzierte Dynamik nur dort, wo die Faktoren ausschließlich über Y eingehen. Eine physikalische Eichäquivalenz ist damit nicht bewiesen. Weitere sektorbezogene Forderungen an L oder D_cov müssen separat geprüft werden.

## B. Load-Update: bestätigt, einschließlich exakter Zahlen

Setze a=eta/((1+eta)sqrt(1+eta²)), t=||PD||²/||D||² und f0=2a²t. Für eta>0 und 0<t<1 gilt 0<f0<1/4. Für einen beliebigen endlichen positiven neuen Load g und den unverändert definierten Paket- und Resolventenschritt folgt

    D_next = sqrt(2)a/(1+g) P D
    E_next/E = f0/((1+g)(1+eta)) < 1/4.

Die Alternativen g=f0² und g=f0/2 sind somit ebenso positiv, invariant und dissipativ. Beim Seed eta=1, d=5 und D=(1,1,1,1,1) ist f0=1/5:

| Regel | g | verbleibende D-Komponente | E_next |
|---|---:|---:|---:|
| f0 | 1/5 | 5/12 | 5/6 |
| f0² | 1/25 | 25/52 | 25/26 |
| f0/2 | 1/10 | 5/11 | 10/11 |

Diese Zahlen wurden rational nachgerechnet. Die Regeln liefern verschiedene Folgezustände. „Packet-load matching“ wählt die aktuelle Regel aus, formuliert aber gerade die zu begründende Identifikation als neues Axiom; es ist für sich keine unabhängige Herleitung.

## C. Stabile Eigenlinie: bestätigt

Bei einfachem Spektrum lambda1<0<lambda2<...<lambdad kann für d>=3 jede positive Eigenlinie entfernt werden, ohne den einzigen negativen Modus oder sämtliche positiven Modi zu verlieren. Die kommutierenden Kapazitäten bleiben bei dieser spektralen Restriktion kommutierend und die positive c-Schranke bleibt erhalten. Volle Unterstützung des aktiven Vektors bleibt auf den behaltenen Linien bestehen.

Eine vollständige deterministische Alternative lautet etwa: Entferne immer die kleinste positive Eigenlinie; verwende anschließend dieselben übrigen Updatevorschriften, wobei P jeweils die neu gewählte persistente Projektion ist. Bei Dimension zwei bleibt die ausdrücklich gesetzte Terminalregel U(X)=⊥ bestehen. Für K=diag(-1,2,3,4,5) entstehen damit (-1,3,4,5) statt (-1,2,3,4). Das widerlegt die Eindeutigkeit aus den genannten strukturellen Gates.

Ein rang-eins oberer Spektralfilter erzwingt hingegen P_max. Das ist eine zusätzliche Ordnungsannahme. Die Bezeichnung „export“ darf ohne eigene Herleitung nicht mit einem physikalischen Exportkanal oder jeder ursprünglichen BFG-Exportdefinition gleichgesetzt werden.

## D. Rekursionsrate: bestätigt, mit Zeit- und Beobachtungspräzisierung

Bei festem P gilt R1=P+q(I-P), R2=P+q²(I-P). Die primitive CTC-SA-Folge aus Kapazitäten, D und eta bleibt gleich, solange ihre Updatevorschriften unverändert nur P und nicht q verwenden. Die abgeleiteten Größen R und persistence_gap bleiben dagegen nicht gleich. Für den Seed sind q=5/6, q²=25/36 und die Gaps 1/6 beziehungsweise 11/36.

Bei eingefrorenem K gilt darüber hinaus **R2=R1²**. Ein Schritt der zweiten Rekursion entspricht dann zwei Schritten der ersten. Ein empirischer Ratenvergleich braucht deshalb eine unabhängig fixierte Bedeutung und Dauer des Rekursionsschritts. Ohne diese Festlegung kann eine bloße Zeitskalierung als vermeintliche Modellunterscheidung erscheinen. Dies behauptet keine solche Äquivalenz für beliebig zeitveränderliche Operatorfolgen.

Die genannte affine Spektralinvarianz gilt für ordnungserhaltende Transformationen K -> alpha K + beta I mit alpha>0; für Vergleiche innerhalb der SA-Klasse müssen auch deren Vorzeichenbedingungen erhalten bleiben. Dimensionslosigkeit und diese Invarianz wählen nicht einmal q als einzig mögliche Spektralinvariante aus. Erst bei bereits festgelegtem q und zusätzlichem affinem f mit den fortgesetzten Randwerten f(0)=0, f(1)=1 folgt f(q)=q.

## Grenzen des Gesamturteils

1. „Zulässige Alternativen“ bedeutet zulässig unter den ausdrücklich verglichenen schwächeren Bedingungen. Innerhalb der bereits definierten Klasse mit fest vorgeschriebenen vier Gesetzen sind es alternative Modelle, keine weiteren Lösungen derselben vollständigen Axiomatik.
2. Die vier Axiome wählen diese vier Regeln aus, wenn die übrige SA-Architektur schon feststeht. Sie sind keine vollständige Axiomatisierung aller BFG-Freiheiten: beispielsweise skalare Gramgeometrie, kommutierende Kapazitäten und die Terminalregel bleiben weitere Modellfestlegungen.
3. Die vorgeschlagenen Falsifikationsrouten sind Prüfideen. Es fehlen konkrete unabhängige Messabbildungen, Einheiten, Fehlergrenzen, Zeitdefinition und Daten. Aus Y allein sind die Gramfaktoren nicht unterscheidbar. Ein reiner Darstellungsstandard lässt sich dadurch nicht empirisch widerlegen.
4. Die reparierte periphere Rieszgeometrie benötigt ihre spektralen Voraussetzungen. Sie darf nicht ohne diese in allgemeine nichtnormale oder unendlichdimensionale Fälle übertragen werden.
5. Die früher berichteten 14 gezielten beziehungsweise 143 gesamten Softwaretests sind Implementierungsbefunde. Die vorliegende Prüfung fügt mathematische Gegenmodelle hinzu, keine empirischen Daten und keinen universellen Schließungsbeweis.

## Nächster Auftrag für die Audit Engine

Prüfe zunächst die Identifizierbarkeit der nächsten Gram-Skala, da die Alternativen bereits verschiedene primitive Folgezustände liefern. Verwende diesen Bericht als Korrektur des eingereichten Audits.

- Benenne eine genaue ursprüngliche BFG-Quellenstelle, die eta_next unabhängig vom gewählten Paketquotienten festlegt oder einschränkt. Unterscheide Originalaxiom, neue Hypothese und Folgerung.
- Leite daraus eine überprüfbare Bedingung an g(eta,t) her und prüfe f0, f0² und f0/2 dagegen. Eine bloße Umbenennung der gewünschten Gleichung zählt nicht als Herleitung.
- Falls keine solche Bedingung folgt, gib einen ausdrücklichen Unterbestimmtheitssatz unter den tatsächlich verwendeten Annahmen aus. Erhalte alle drei Alternativen als Vergleichsmodelle.
- Für einen empirischen Weg: definiere zuerst, wie eta_next unabhängig von der zu prüfenden Updateformel bestimmt wird; spezifiere Messfehler, Skalierung und einen vorab fixierten Ablehnungsmaßstab. Keine aus derselben Formel erzeugten Daten als Bestätigung verwenden.
- Für spätere Ratentests fixiere zusätzlich die Rekursionszeit; für Faktortests die beobachtbaren Faktoren und zulässigen Darstellungswechsel.

Erwartetes Resultat: entweder eine quellengestützte zusätzliche Einschränkung mit Beweis, ein präziser Unterbestimmtheitsbefund oder ein operationalisierter unabhängiger Prüfplan. Kein Auftrag, ein gewünschtes positives Resultat zu erzwingen.

## Ablagestatus

Diese Fassung wird als eigene Dokumentationsstufe veröffentlicht. Produktionscode und historische Dokumente bleiben unverändert. Die erneute Prüfung desselben Berichts ist keine zusätzliche unabhängige Begutachtung.

