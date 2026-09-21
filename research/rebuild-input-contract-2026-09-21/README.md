# Expliziter Eingabevertrag für den skalaren Gram-Rebuild

Stand: 21. September 2026. Anschluss an [Identifizierbarkeit des nächsten Gramoperators](../next-gram-identifiability-2026-09-21/README.md). Status: bedingte mathematische Spezifikation des endlichen SA-Zweigs, keine neue universelle BFG-Herleitung. Produktionscode und historische Quellen bleiben unverändert.

## 1. Quellenbefund

Die erneut geprüften Textstellen von Unified V4 (S. 3–4, S. 9–10, insbesondere BFG-U und Gl. 39–43), Endogenous Dual Order Canonical Closure (S. 3, 8–9) und Strong Universal Reclosure (S. 7–8, 29) verlangen, dass der nächste Zustand wieder die für die Iteration benötigten Strukturdaten trägt. V4 verwendet sowohl den zustandsabhängigen Ausdruck Reclosure_X als auch die Paketnotation B_C[p], W_N[p], L_C[p]. Die erste Schreibweise lässt alte Zustandsabhängigkeit zu; die zweite zählt solche Eingaben nicht auf. Keine dieser Schreibweisen allein beweist, dass ausschließlich das nackte Paket benutzt werden darf.

Die untersuchten Stellen liefern keinen vollständigen, auswertbaren Eingabevertrag für diese drei Funktionale. Insbesondere benennt die Schreibweise X_next=C_N(Y_next)p nur den aktiven Vektor, sofern X zuvor als strukturiertes Objekt verstanden wird. Für eine vollständige Iteration müssen auch Raum, Kapazitäten und Gramdaten explizit zurückgegeben oder eindeutig daraus rekonstruiert werden.

Dies ist ein begrenzter Quellenbefund, keine Behauptung über jede Stelle des gesamten BFG-Korpus. Die verwendeten Originaldateien sind im [vorherigen Quellenmanifest](../next-gram-identifiability-2026-09-21/EVIDENCE.json) mit Hashes identifiziert. Extrahierter Text wurde geprüft; kein erneuter Layout- oder vollständiger Korpusaudit. Die bereits dokumentierte Witness-Reparatur bleibt Voraussetzung des SA-Vergleichs.

## 2. Ein zusätzlicher Normskalar genügt

Im skalaren SA-Modell gilt G_n=(1+eta_n)I. Sei p=A_n D_n das vor dem finalen Resolventen erzeugte Paket. Definiere

    N_n=||D_n||² > 0,
    q_n=||p||²/N_n.

Alle Normen dieser beiden Ausdrücke sind die ursprünglichen Hilbertraumnormen, beim Paket die direkte Summennorm beziehungsweise die dazu isometrische Supportnorm. Dann gilt exakt

    ||p||²_(G_n⊕G_n) / ||D_n||²_(G_n)
      = (1+eta_n)||p||² / ((1+eta_n)||D_n||²)
      = q_n = 2a(eta_n)² t_n.

Damit genügt neben dem bereits erzeugten Paket der eine positive Skalar N_n, um alle drei diskutierten Regeln zu berechnen. eta_n und die alte Graphenergie müssen dafür nicht zusätzlich übergeben werden. Sie waren im vorherigen Bericht als hinreichende, nicht als minimale Information genannt.

Der Skalar ist aus dem vorhandenen alten Zustand berechnet und kein neuer freier Parameter. Für den nächsten Schritt wird N_(n+1) aus D_(n+1) erneut berechnet; es entsteht kein Bedarf an einer unbegrenzten Historie. Dieser Befund gilt für die skalare Metrik. Bei allgemeinem Y kürzt sich die Graphmetrik nicht auf diese Weise heraus.

## 3. Was an dieser Information notwendig ist

Das Paketkollisionsbeispiel des vorherigen Berichts hat p in Supportkoordinaten gleich (1/2,1/2), aber N=3 beziehungsweise N=6. Daher ist q=1/6 beziehungsweise q=1/12. Jede Zusatzinformation, die beide Zustände weiterhin identifiziert, ist für die Rekonstruktion von q unzureichend.

Bei festem nichtverschwindendem p gilt außerdem N=||p||²/q. Innerhalb einer solchen Paketfaser trägt die Kenntnis von q genau die hier benötigte Information über N. N ist deshalb eine hinreichende skalare Ergänzung und ohne irgendeine trennende Information geht es nicht. Behauptet wird keine universelle minimale Kodierungsdimension für alle BFG-Modelle oder beliebige Darstellungen.

Den alten Vektor vorab auf Norm eins zu setzen behebt diesen Punkt nicht ohne weitere Festlegung: Dadurch ändert sich sein Paket. Wenn Norm und Energie als Zustandsgrößen verwendet werden, ist eine solche Normierung keine bereits bewiesene harmlose Eichwahl.

## 4. Vollständiger bedingter Rebuild-Vertrag

Der primitive alte SA-Zustand ist das strukturierte Tupel

    X=(H,Dcap,c,aleph,D,eta).

Es erfüllt die Voraussetzungen des bestehenden SA-Modells. Raum, Paket und Kapazitäten werden zunächst nach der festgelegten Projektions- und Polarregel transportiert. Der Gram-Rebuild erhält das Eingabetupel

    I_rebuild=(H_next,Dcap_next,c_next,aleph_next,p,N_old).

Sei h eine einmalig für das Modell festgelegte Funktion mit endlichen positiven Werten auf 0<q<1/4. Dann:

    q=||p||²/N_old,
    g=h(q),
    W_next=L_next=N_R,next=I,
    D_cov,next=sqrt(g)c_next^(-1),
    B_next=D_cov,next c_next=sqrt(g)I,
    Y_next=g I,
    D_next=p/(1+g).

Die Faktoren B_next, W_next und L_next wirken auf H_next; D_cov c ist hier Operatorverkettung. Diese Festlegung beansprucht keine Herleitung eines geometrischen Zusammenhangs oder einer kovarianten Ableitung. Der Rückgabewert ist

    X_next=(H_next,Dcap_next,c_next,aleph_next,D_next,g),

nicht nur der Vektor D_next. Der nächste Rekursionsoperator wird nach der bisherigen festgelegten SA-Spektralregel aus den neuen Kapazitäten berechnet. Die Terminalregel in Dimension zwei und der absorbierende Zustand bleiben Bestandteil der vollständigen Abbildung.

Die Wahl h gehört zur Modellbeschreibung und wird vor der Iteration fixiert; sie ist keine nachträglich pro Stufe wählbare Zustandskoordinate. Alle Größen im Eingabevertrag sind aus X berechenbar. Der Vertrag beschreibt die Abhängigkeiten der vorhandenen Regel expliziter; er ersetzt keine vorhandene Implementierung.

## 5. Warum die Funktionswahl weiterhin offen ist

Die drei festen Funktionen h(q)=q, h(q)=q² und h(q)=q/2 erfüllen denselben Eingabevertrag. Grampositivität, der exakte neutrale Resolvent, die transportierten Formationseigenschaften und die volle Unterstützung des Vektors bleiben bestehen. Es gilt

    E_next/E_old = q / ((1+h(q))(1+eta_old)) < 1/4.

Damit unterscheiden diese Bedingungen die Funktionen nicht. Selbst zusätzliche Forderungen nach Glattheit, strenger Monotonie auf q>0, unitärer Invarianz, gemeinsamer Skalierungsinvarianz und h(q)->0 für q->0 unterscheiden diese drei Beispiele nicht. No-Retuning verbietet den Wechsel des Gesetzes nach Ergebnisinspektion, bestimmt aber nicht das ursprüngliche Gesetz.

Eine lineare Funktion mit vorab festgelegter Normierung würde h(q)=q auswählen; die Normierung wäre jedoch zusätzlich zu begründen. Insbesondere ist q=1 kein erreichbarer SA-Paketgewinn, da q<1/4. Eine Randbedingung h(1)=1 läge außerhalb dieses Bereichs und wäre kein dort ausgeführter Test.

Somit ist jetzt die Berechenbarkeit der aktuellen Regel präzisiert. Ihre Eindeutigkeit aus den untersuchten BFG-Bedingungen ist weiterhin widerlegt; eine stärkere Originalannahme könnte dieses Ergebnis ändern, müsste aber gesondert belegt werden.

## 6. Konsequenter nächster Forschungsgegenstand

Die fehlende Norminformation ist kein Grund mehr, den SA-Rebuild als unimplementierbar einzustufen. Die noch offene Frage lautet enger: Welche zusätzliche, unabhängig begründete Bedingung legt h fest?

Für eine theoretische Lösung ist eine genaue Originalquellenstelle nötig, aus der eine weitere Gleichung für h folgt. Die Definition g=q darf nicht erneut als ihr eigener Beweis verwendet werden. Für eine empirische Auswahl muss g unabhängig identifiziert werden, etwa über eine operationalisierte neutrale Response s=1/(1+g), mit vorab fixierten Messabbildungen und Unsicherheiten. Eine reine Simulation der gewählten Funktion bestätigt deren Auswahl nicht.

Bis dahin bleibt h(q)=q die ausdrücklich gewählte Referenzregel; die Alternativen bleiben dokumentierte Gegenmodelle. Die Eingabelücke ist im endlichen SA-Modell durch einen expliziten Vertrag geschlossen. Die universelle interne Auswahl des Load-Gesetzes sowie die allgemeinen nichtnormalen und unendlichdimensionalen Probleme sind damit nicht gelöst.

## 7. Audit und Kontrolle

Angewandt: Claim-State, Unterscheidbarkeit, Redescription, Kontext-/Quellenhierarchie und Erhalt negativer Befunde aus den drei BFG-Auditvorlagen. Keine neue unabhängige Begutachtung behauptet. Ein rationaler Rechencheck der Normkürzung und Energieformel liegt in [CHECK.json](CHECK.json); er illustriert den symbolischen Beweis und ist kein empirischer Test. Keine Änderung am Modellcode und kein neuer Gesamttestlauf.
