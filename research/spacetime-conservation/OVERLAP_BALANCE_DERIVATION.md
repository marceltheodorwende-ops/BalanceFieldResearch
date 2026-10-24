# Normierte Bilanz über überlappende Paarsektoren

## Quelle und mathematische Voraussetzungen

Unter erklärten BFG-Annahmen abgeleitet mit Standardmathematik, derselbe gepinnte volle positive Persistenzkernel. Seine ausgerichtete Kernelabbildung lautet Phi(K)=sum_r T_r K T_r mit Hermiteschen positiven T_r und sum_r T_r²=I. Alle Last-/Formationsdaten, die T_r bestimmen, bleiben enthalten. Betrachtet werden pro Ereignis festgehaltene positive Effekte E_a>=0 mit sum_a E_a=I. Sie dürfen überlappen und müssen weder Projektoren noch untereinander kommutierend sein.

q_a=tr(E_a K) sind mathematische Kernelbestände. Für K>=0 sind sie nichtnegativ und sum_a q_a=tr K. Dies ist eine normierte Mehrsektor-Beschreibung, keine bereits identifizierte physikalische Energiepartition. Die frühere exakte Modenkontinuität aus Runde 9 wird hier auf überlappende positive Effekte erweitert; sie wird nicht als neues Ergebnis für orthogonale Knoten wiederholt.

## Warum die vorige Kandidatenfamilie keine vollständige normierte Überdeckung liefert

Alle Rang-zwei-Projektoren P_tau aus Runde 33 enthalten denselben Vektor e_1 im n=3-Raum. Angenommen eine endliche skalare Gewichtung erfüllt sum_a w_a P_tau_a=I. Das Erwartungswertbild auf e_1 erzwingt sum_a w_a=1. Die Spur erzwingt dagegen 2sum_a w_a=3. Das ist unmöglich, sogar mit vorzeichenbehafteten endlichen Gewichten. Mit positiven Gewichten lässt sich diese Familie daher erst recht nicht allein zu normierten Effekten eines vollständigen Raumbestands umdeuten.

Der Einwand gilt genau für diese common-line-Familie und skalare Gewichte, nicht für jede mögliche Ergänzung durch weitere Flächen oder allgemeine positive Effektoperatoren. Ihre achtparametrige gemeinsame Kernelinformation bleibt davon unberührt; Informationsgehalt und additive Normierung sind verschiedene Fragen.

## Naheliegende Alternative und Doppeltzählung

Wähle eine orthonormale Basis, beispielsweise einen nichtentarteten behaltenen F-Eigenrahmen. Für jedes Koordinatenpaar i<j sei P_ij=|i><i|+|j><j|. Jeder Basismodus erscheint in n-1 Paaren. Deshalb exakt

sum_(i<j)P_ij=(n-1)I,
E_ij=P_ij/(n-1), sum_(i<j)E_ij=I.

Die ungewichtete Paar-Spursumme ist (n-1)tr K; erst die normierte Summe ist tr K. Damit wird die Überlappung bilanziert statt mehrfach als neuer Gesamtbestand gezählt. Dies ist eine explizite mathematische Coverwahl. Weder Basis noch Überdeckung werden hier als eindeutig physikalisch ausgewählt ausgegeben.

## Exakter interner Strom direkt aus dem vollständigen Kernelkanal

Definiere den aus a ausgehenden Strom nach b durch

J_ab=sum_r Re tr(E_a T_r E_b [T_r,K]).

Für Hermitesches K ist [T_r,K] anti-Hermitesch. E_a T_r E_b+E_b T_r E_a ist Hermitesch. Die reelle Spur ihres Produkts verschwindet, daher

J_ab=-J_ba, J_aa=0.

Einsetzen von sum_b E_b=I und sum_r T_r²=I liefert

sum_b J_ab=sum_r Re tr(E_a T_r[T_r,K])
           =tr(E_a K)-tr(E_a Phi(K)).

Somit exakt

Delta q_a + sum_b J_ab=0,
sum_a Delta q_a=0.

Die Vorzeichenkonvention stimmt mit der früheren ausgehenden Modenstromdefinition überein. Der Beweis braucht keine Orthogonalität oder Kommutativität der Effekte. Positivität der Effekte stellt die Interpretation als normierte nichtnegative Bestände bei K>=0 sicher; die algebraische Identität selbst verwendet nur Hermitizität und die Einszerlegung.

Der Strom enthält den vollen Kernel einschließlich Kohärenzen und die aktuellen Quellzweige. Er wird nicht als geschlossene Funktion der q_a allein ausgegeben. Die bekannten Faser-Gegenbeispiele bleiben relevant. Auch Antisymmetrie und Kontinuität wählen keinen eindeutigen physikalischen Strom: zusätzliche zirkulierende Beiträge können dieselbe Divergenz besitzen, und die Überdeckung bleibt eine Wahl.

## Was noch keine räumliche oder vollständige physikalische Bilanz ist

Die Effekte und ihre Labels bleiben hier über das Ereignis fest. Wechselnde Überdeckungen benötigen eine gesonderte Zuordnungsbilanz; tatsächliche Rang-/Seed-Ereignisse verlassen zusätzlich den herangezogenen festen Persistenzsektor. Keine solche Kopplung wird zur Zielerfüllung erfunden.

Der aktuelle J_ab ist eine aus BFG abgeleitete interne Kernelkontinuität. Ein metrischer Abstand der Sektoren, physikalische Ereignisdauern, vier Impulskomponenten, Einheiten, eine Wirkung oder eine lokale Translation-/Diffeomorphismussymmetrie sind dadurch nicht abgeleitet. Die Identität darf nicht als vollständiger Energie-Impuls-Strom oder Einstein-Grenzfall bezeichnet werden.

## Frische Evidenz

OVERLAP_BALANCE_PROTOCOL.md vor Auswertung auf GitHub publiziert. Exakte Überdeckungen für n=3,4 und common-line-Spurwiderspruch geprüft. Ein zusätzlicher exakter Matrixcheck verwendet positive normierte, nichtkommutierende Trine-Effekte im Zweimodenraum und die bereits gepinnte BFG-Krausinstanz zu Lasten 1/5,3/10 und F=I. Ihre T_r² summieren sich zu I und der Schurfaktor ist 31/sqrt(1001). Für K=I+sigma_x sind die Bestandsänderungen (-2/3,1/3,1/3)(1-31/sqrt(1001)); Antisymmetrie und Kontinuität werden exakt symbolisch überprüft. Dies ist ein algebraischer Kontrollfall der allgemeineren Effektidentität, kein zusätzlicher Original-Quellaufruf und keine neue physikalische Hypothese.

Acht frische vollständige Original-Quellaufrufe: n=3,4 je drei positive komplexe Präparationen mit nichtkommutierender Last, F-diagonalem Bezugsrahmen und W=I/n, plus je eine simultane komplexe Eichkontrolle. Die Quell-Krausoperatoren stammen aus der vorhandenen ausgerichteten Formel; die Kontinuität wird gegen das unabhängige vollständige Originalupdate verglichen. Die normierten Effekte sind drei bzw. sechs Koordinatenpaare. Unnormierte Paarbestände sind bei tr K=1 gleich 2 bzw. 3, die normierte Summe ist 1.

Kontinuitätsrest 2.7531767186819497e-16, Antisymmetrierest 3.699300751813071e-17, Überdeckungsrest 0, Gesamtbestandsrest 8.881784197001252e-16, Eichrest 1.2136532123497184e-15; vorab Schwelle 1e-10. Größter geprüfter interner Strom .0008361310309727771 mit nichtverschwindenden Bestandsänderungen. Keine Langtrajektorie oder empirische Bestätigung behauptet. CI separat in CI_VALIDATION.md.

Nächste Abhängigkeit: exakte Zuordnungsbilanz bei wechselnden Effekten und echte Fortsetzung über Auswahl-/Rangereignisse, danach eine quellengestützte räumliche und zeitliche Deutung. Allgemeine Trägerauswahl, physikalische Uhr, vollständiger Energie-Impuls-Strom und Einstein-Herleitung bleiben offen.
