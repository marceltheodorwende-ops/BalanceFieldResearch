# Klassifikation universell erhaltener K-allein-Energieoperatoren – Runde 50

## Präzises Ergebnis

Auf der strikt positiven Zwei-Moden-Kernelklasse ist eine **stetige, unitär kovariante, nur von K abhängige** Hermitesche Operatorablesung H(K), deren Witness-Erwartung in jedem vollen BFG-Persistenzzustand erhalten sein soll, notwendig von der Form

H(K)=g(tr K/2) I2.

Umgekehrt sind solche skalaren Spurfunktionen auf diesem Sektor erhalten. Sie liefern jedoch keine nichtverschwindenden spektralen Energiedifferenzen.

Dies schließt nicht Energieabbildungen H(K,Y,F,W,weitere Daten) oder solche mit ausdrücklich behaltenen historischen Richtungen aus. Auch eingeschränkte physikalische Witness-Präparationen und offene/angetriebene Energiebilanzen sind nicht umfasst. Die Stetigkeit bei skalarem K ist eine **zusätzliche Regularitätsannahme**, kein aus der Quelle bewiesenes physikalisches Gesetz.

Vorab: PROTOCOL.md Runde50. BFG-Quelle und Update unverändert. Standardmathematik: unitäre Kovarianz, Zwei-Moden-Kommutanten und Stetigkeit einer Funktionsgleichung. Keine neue Quantendynamik.

## 1. Voraussetzungen und Bedeutung der universellen Erhaltung

Betrachte H auf Herm_+(C²), also strikt positivem K, mit:

1. Nur-K-Abhängigkeit: keine versteckten Y-/F-/W-/Historienargumente.
2. Basis-Kovarianz: H(UKU†)=U H(K) U†.
3. Stetigkeit, auch bei K=tI, t>0.
4. Bei P=I,0<Y<I und positiven Lasten soll für **alle zulässigen Witnessdichten W** gelten:
   tr[W_out H(K_out)]=tr[W H(K)].

Im ausgerichteten Quellrahmen gilt W_out=W, K_out=Phi_Y,F(K). Der Kanal hängt bei festem F,Y nicht von W ab. Die universelle Spurpaarung mit W erzwingt daher

H(Phi_Y,F(K))=H(K).

Hier wird eine isoliert konservierte Witness-Energie geprüft, nicht die bloße Existenz irgendeines zeitlich veränderlichen physikalischen Hamiltonoperators. Der Satz ist insbesondere nicht aus einem Test allein mit W=I/2 oder allein mit rho_Q=F/tr F abgeleitet.

Die Kovarianz gewährleistet, dass die Aussage unter der zur Quellenanalyse verwendeten unitären Ausrichtung dieselbe bleibt. Eine bevorzugte externe Matrixbasis wird nicht eingeführt.

## 2. Kovarianz und ein schräger Quellkanal erzwingen Skalarität

Die Unitärtransformationen exp(isK) lassen K fest. Kovarianz verlangt deshalb, dass sie H(K) ebenfalls festlassen. Folglich [H(K),K]=0. Bei K=tI erzwingt volle U(2)-Symmetrie bereits H(tI)=c(t)I.

Sei nun K=tI+r sigma_z mit0<r<t. Jeder andere nichtskalare positive Zwei-Moden-Kernel ist dazu unitär äquivalent.

Wähle F=I und die Y-Achse schräg, entlang(sigma_x+sigma_z)/sqrt2, mit Eigenwerten1/5,3/10. Der tatsächlich aus der Quelle berechnete Faktor ist h=31/sqrt(1001),0<h<1. Das vollständige Quellereignis ergibt

Phi(K)=tI+r[(1-h)/2 sigma_x+(1+h)/2 sigma_z].

Wegen des nichtverschwindenden sigma_x-Anteils kommutieren K und Phi(K) nicht. Universelle Erhaltung verlangt H(Phi(K))=H(K). Kovarianz macht H(K) mit K kommutierend und H(Phi(K)) mit Phi(K) kommutierend; der gemeinsame Operator muss also mit beiden kommutieren.

Der gemeinsame Hermitesche Kommutant dieser zwei nichtkommutierenden 2x2-Matrizen ist genau die skalare Linie. Explizit: Aus der Kommutation mit sigma_z folgen verschwindende sigma_x-/sigma_y-Anteile. Die zweite Kommutation multipliziert den verbleibenden sigma_z-Anteil mit1-h!=0 und setzt ihn ebenfalls0.

Damit ist H(K) für jedes nichtskalare positive K skalar. Dieser Teil benötigt noch keine Stetigkeit. Insbesondere kann ein unstetig spektral normalisierter, aber nichtskalarer K-Operator dem Orientierungsargument nicht ausweichen.

## 3. Die verbleibende Skalarfunktion hängt nur von der Spur ab

Unitäre Kovarianz schreibt die skalare Ausgabe als
H(tI+r n·sigma)=a(t,r)I.

Wähle jetzt eine Y-Achse senkrecht zur Kernelrichtung, wieder mit den vorigen positiven Eigenwerten und F=I. Derselbe zulässige Quellkanal kontrahiert den Kontrast zu h r, ohne das Spurmittel t zu ändern. Universelle Erhaltung liefert

a(t,r)=a(t,h r).

Weil diese Identität für jeden zulässigen Eingangs-Kernel und jede solche Nicht-Kernel-Präparation gefordert ist, darf sie als Funktionsgleichung wiederholt eingesetzt werden:
a(t,r)=a(t,h^m r).

Für m->unendlich gilt h^m r->0. Stetigkeit bei tI gibt a(t,r)=a(t,0)=g(t). Damit folgt die behauptete Klassifikation.

**Keine eingefrorene physikalische Quellbahn:** Die wiederholte Funktionsgleichung ist keine Aussage, dass Y im tatsächlichen rekursiven Verlauf konstant bliebe. Sie folgt aus der vorab angenommenen Erhaltung für alle zulässigen Zustände, jeweils bei neu eingesetztem K. Der tatsächliche Y-Update bleibt unverändert.

Die Umkehrung ist unmittelbar: tr Phi(K)=tr K im vollen Persistenzsektor, deshalb ist jede skalare g(tr K/2)I dort erhalten. Stetigkeit von H entspricht der gewünschten Regularität von g. Über Auswahl-/Rangereignisse hinaus wird keine Spurkonservierung behauptet.

## 4. Bedeutung für einfache alternative Hamiltonianfunktionen

H=K und nichttriviale Polynome wie K² sind zwar unitär kovariant und stetig, erfüllen aber die universelle Operatorerhaltung nicht. Eine Ablesung mit normiertem traceless-Anteil kann die Spektrallücke von K künstlich festhalten, rotiert aber unter dem schrägen Quellkanal ihre Richtungen. Sie konserviert deshalb ebenfalls nicht die Erwartung für alle im Quellrahmen unveränderten Witnesszustände.

K² ist zunächst eine Matrix mit quadrierter Formationseinheit; eine Energieinterpretation benötigte einen unabhängig fixierten Umrechnungsfaktor. Solche festen Faktoren verändern die gezeigte Nichterhaltung nicht. Die Beispiele werden hier als illustrative Operatorfunktionen geprüft, nicht ohne Kalibrierung als Joule behauptet.

Die skalare Ablesung H=tr(K)I bleibt als positive mathematische Kontrolle erhalten. Alle ihre Zustände haben jedoch denselben Eigenwert; eine nichtverschwindende spektroskopische Energiedifferenz nach I68.2 wird dadurch nicht geliefert. Eine vollständige physikalische Energie-/Hamiltonianbrücke ist also nicht mit dieser Klassifikation konstruiert.

Die kommutierenden Y-/historischen Projektionsablesungen aus Runde49 sind nicht Teil der Nur-K-Klasse. Ihre erhaltenen Teilklassen und Kollisionsgrenzen bleiben unverändert gültig.

## 5. Frische proportionale Kontrollen

Drei Originalaufrufe, alle nichtterminal:

- Schräger positiver n=2-Zustand K=2I+sigma_z, W=(I+sigma_x/2)/2 mit der vorab festgelegten Y-Rotation pi/8.
- Transversaler Zustand K=2I+sigma_x bei diagonalem Y.
- Komplexe unitäre Eichversion des schrägen Falls, Seed20261101.

Die exakte schräge K-Ausgabe wird bis1.491236750938252e-15 bestätigt; ||[K,K_out]||_F=0.028544077943305157. Transversaler Ausgangskontrast0.9798162889235715 stimmt mit h überein; Vollfeld-Eichrest2.9961143025726952e-15.

Illustrative Ablesungen am schrägen Zeugen:

| Ablesung | Operatoränderungsnorm | Witness-Erwartungsänderung |
| --- | ---: | ---: |
| K | 0.020183711076428672 | 0.005045927769105951 |
| K² | 0.08553664408820669 | 0.00020369109640405725 |
| normierter traceless-Anteil | 0.014416976806831424 | 0.005097104816540521 |
| tr(K)I | 2.5121479338940403e-15 | -2.6645352591003757e-15 |

Symbolisch ist der gemeinsame Hermitesche Kommutant exakt{a0 I}. Ein erster direkter Sympy-Linsolve-Versuch brach vor Originalaufrufen mit einem algebraischen „zero divisor“-Solverfehler ab. Die Kontrolle wurde danach in die zwei transparenten Kommutatorschritte zerlegt; Division nur durch den exakt nachgewiesenen nichtverschwindenden Faktor1-h. Der frische vollständige Lauf bestand. Weder Hypothese noch Quellgleichung wurden geändert.

Vollständiger Prüftext/Ausgabe: [K_ONLY_ENERGY_CHECKS.md](K_ONLY_ENERGY_CHECKS.md). Keine Audit-/Workflow-/Originalcodeänderung und kein neuer Remote-CI-Pass behauptet. Lokale Evidenz und letzter Remote-geprüfter Code bleiben in CI_VALIDATION.md getrennt.

## 6. Nächste Abhängigkeit und Grenze

Eine nichttriviale spektrale Energieablesung lässt sich unter den genannten universellen Witness-/Kovarianz-/Regularitätsbedingungen nicht allein durch eine andere Funktion des Zwei-Moden-Kernels erhalten. Die mathematisch konstruktiven Möglichkeiten liegen außerhalb dieser Klasse: weitere quelleninterne Zustands-/Rahmendaten, explizit behaltene Historie, unabhängig begründete physikalische Präparationseinschränkungen oder eine vollständige gekoppelte Austauschbilanz.

Welche davon physikalisch ausgewählt ist, liefert der Satz nicht. M_prep, Quantenzustands-/Hamiltonianabbildung, unabhängige Energiekalibrierung und die Raum-/Uhr-/Impuls-/Lorentzbrücke bleiben gesondert offen. Es folgt keine allgemeine Widerlegung von BFG und keine vollständige Einstein-Herleitung.
