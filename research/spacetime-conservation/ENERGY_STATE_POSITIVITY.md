# Positive Zustandskompensation der K-Energie – Runde 48

## Ergebnis und genaue Kandidatengrenze

Die in Runde46 demonstrierte Energieerwartungsänderung lässt sich bei H proportional K nicht universell allein dadurch beheben, dass man eine andere positive Spur-eins-Ausgangsdichte wählt.

Für einen energieerhaltenden Zustandswechsel bei **jedem K** ist die inverse Kanalabbildung erforderlich. Sie ist zwar linear invertierbar, aber bei nichttrivialer Kohärenzdämpfung nicht positiv auf allen Dichten. Ein ausdrücklich strikt positiver Eingangszeuge zeigt noch mehr: Für einen einzelnen positiven K liegt seine Eingangsenergie bereits außerhalb des gesamten Erwartungsintervalls des ausgegebenen K. Dann kann selbst eine K-abhängig gewählte Ausgangsdichte die isolierte Energie nicht erhalten.

Das ist ein begrenzter Ausschluss einer reinen Zustandskompensation bei festgehaltener K-Energieablesung. Andere Hamiltonianabbildungen, physikalisch eingeschränkte Präparationsklassen, offene/angetriebene Systeme und zusätzliche gekoppelte Energieträger bleiben offen. Es wird keine neue Witnessdynamik eingesetzt.

Vorab: PROTOCOL.md Runde48. Ausgangspunkt sind die geprüften Quantenkandidaten I57/I68/I70 und der exakt hergeleitete volle Persistenzkanal. Nur BFG und explizite endliche Matrixrechnung.

## 1. Quelle und alternative Hypothese trennen

Im vollen ausgerichteten Persistenzsektor entwickelt die Quelle K zu Phi(K), während W und F konstant bleiben. In dieser Runde wird die tatsächliche Quellregel W_+=W nicht verändert.

Geprüft wird lediglich die mögliche zusätzliche physikalische Brückenhypothese, dass eine alternative Ausgangsdichte rho_out die Erwartung eines H=epsilon_E K+E0 I konservieren könnte. Einheit und Nullpunkt seien fest, epsilon_E!=0; wegen Spur rho=Spur rho_out=1 genügt die mathematische Bedingung

tr[rho_out Phi(K)]=tr(rho K).

Eine solche rho_out ist nicht schon durch die BFG-Quelle geliefert. Die Rechnung prüft ihre mögliche Existenz und Positivität, bevor eine solche Energiebrücke behauptet wird.

## 2. Universelle Erwartungserhaltung erzwingt den inversen Kanal

Bei festem Y,F ist Phi bezüglich der Spurpaarung selbstadjungiert. Wird ein von K unabhängig festgelegter Zustandswechsel für alle Hermiteschen K verlangt, folgt

tr[(Phi(rho_out)-rho)K]=0 für jedes K,
also Phi(rho_out)=rho.

Im Y-Eigenrahmen lautet Phi(K)_ij=h_ij K_ij mit h_ij>0. Deshalb ist die eindeutige lineare Lösung

rho_out,ij=rho_ij/h_ij.

Spur und Hermitizität bleiben dabei erhalten. Positivität folgt daraus gerade nicht.

Wähle zwei verschiedene Y-Eigenwerte mit h_ij<1 und eine kohärente reine Dichte in deren Zweimodenraum. Deren 2x2-Block wird durch die Inverse zu
(1/2)[[1,1/h_ij],[1/h_ij,1]].
Der kleinste Eigenwert ist (1-1/h_ij)/2<0.

Damit ist Phi^(-1) auf der gesamten Dichteklasse nicht positiv, sobald ein solches ungleiches Y-Paar vorhanden ist. Bei Y proportional I ist Phi=I und dieses Hindernis entfällt. Das ist eine allgemeine Sektoraussage über die hergeleitete K-Abbildung, kein allgemeiner Ausschluss alternativer Quantenbrücken.

## 3. Exakte Grenze für gemischte Zwei-Moden-Zustände

Verwende die rationalen F=I2,Y=diag(1/5,3/10) aus Runde46:
h=31/sqrt(1001)<1.

Für rho_r=(I+r sigma_x)/2, |r|<=1, hat die inverse Lösung

rho_out=(I+(r/h)sigma_x)/2,
Eigenwerte (1±r/h)/2.

Sie ist genau dann eine positive Dichte, wenn |r|<=h. Ein rein numerischer Negativitätseffekt wird damit ausgeschlossen: die Grenze ist algebraisch exakt.

Für r=1 scheitert die inverse Dichte. Sie scheitert aber auch bei **strikt positiver** Eingabe r=99/100. Die Eingangseigenwerte sind199/200 und1/200. Exakt gilt
(99/100)²-h²=200801/10010000>0,
also99/100>h und der inverse kleinste Eigenwert ist negativ.

Für r=1/2 gilt dagegen r<h. Hier ist eine positive inverse Einzeldichte mathematisch möglich. Dieser positive Kontrollfall bleibt ausdrücklich erhalten; es wird keine Unmöglichkeit jeder einzelnen Zustandskompensation behauptet. Die inverse Einzeldichte ist trotzdem nicht die tatsächliche Quellregel W_+=W und wurde nicht als neue BFG-Dynamik eingeführt.

## 4. Noch stärkerer Einzel-K-Zeuge durch die Spektralgrenze

Halte den positiven Kernel
K=2I+sigma_x
mit Eigenwerten1 und3 fest. Die Quelle liefert
K_out=2I+h sigma_x
mit Eigenwerten2-h und2+h.

Für jede positive Spur-eins-Dichte tau gilt elementar
2-h<=tr(tau K_out)<=2+h.
Beweis: In der K_out-Eigenbasis sind die Diagonaleinträge von tau nichtnegative Gewichte mit Summe1; der Erwartungswert ist eine konvexe Kombination der beiden Eigenwerte.

Die Eingangsenergie bei rho_r ist dagegen2+r. Für r>h gilt2+r>2+h. Deshalb existiert **keine** positive Spur-eins-Ausgangsdichte tau, die bei diesem einzelnen K die Eingangsenergie erhält – selbst wenn tau von K, Geometrie oder Historie abhängen dürfte.

Für die strikt positive Eingabe r=99/100 ist die Eingangsenergie2.99, während der maximale Ausgangserwartungswert nur2+h≈2.9798162889235718 beträgt. Der positive Abstand beträgt ungefähr0.0101837110764285 vor einer Energieumrechnung.

Eine feste affine Energieablesung epsilon_E K+E0 I erhält dieses Außerhalb-des-Spektralintervalls-Hindernis. Eine zusätzliche Energiequelle, eine andere H-Abbildung oder weitere physikalische Freiheitsgrade wären andere Kandidaten und müssten vorab begründet werden.

## 5. Frische Originalkontrollen

Vier vollständige nichtterminale Originalereignisse: r=1,99/100,1/2 sowie komplexe unitäre Eichversion des99/100-Falls, Seed20261030.

| r | kleinster inverser Dichte-Eigenwert | Eingangsenergie | maximal mögliche positive Ausgangsenergie |
| --- | ---: | ---: | ---: |
| 1 | -0.010299742566334702 | 3 | 2.9798162889235718 |
| 99/100 | -0.005196745140671366 | 2.99 | 2.9798162889235718 |
| 1/2 | +0.24485012871683265 | 2.5 | 2.9798162889235718 |

Die algebraisch inverse, gegebenenfalls unphysikalisch negative Matrix reproduziert die Zielenergie in allen Fällen bis Rundung; das macht gerade die zusätzliche Positivitätsbedingung sichtbar. Der tatsächliche Witness bleibt unter dem unveränderten Originalupdate konstant und hat bei r=.99 Ausgangserwartung2.970018126034336.

Komplexer Vollfeld-Eichrest7.65897505568125e-16. Symbolischer Quadratvergleich und allgemeine inverse Eigenwertformel getrennt von numerischen Kontrollen. Vollständige Reproduktion/Ausgabe in [ENERGY_STATE_CHECKS.md](ENERGY_STATE_CHECKS.md).

Dokumentationsrunde ohne Audit-/Workflow-/Originalcodeänderung. Kein neuer Remote-CI-Pass behauptet; letzter geprüfter Code und CI bleiben separat in CI_VALIDATION.md.

## 6. Bedeutung für den nächsten physikalischen Schritt

Der Hamiltoniankandidat H proportional K kann auf der gesamten hier zulässigen Quantenpräparationsklasse nicht als isoliert konservierte Energie allein durch Umwahl des Ausgangszustands gerettet werden. Dieses Hindernis ergänzt die ausgeschlossene rein registerlokale Energieergänzung aus Runde47, ohne eine allgemeine System-Umwelt-Kopplung zu widerlegen.

Die nächste physikalische Konstruktion muss daher entweder eine unabhängig begründete eingeschränkte Präparationsklasse, eine andere H-Abbildung oder eine vollständige gekoppelte Austausch-/Arbeitsbilanz konkret festlegen. Ein nachträgliches Anpassen von Zustand, Energieeinheit oder zusätzlicher Energie auf die gewünschte Erhaltung wäre keine Ableitung.

Die fehlende unabhängige M_prep-/Quanten-/Energiebrücke bleibt von Raumrelation, Uhr und physikalischem Impuls-/Lorentztransport zu unterscheiden. Auch dieses positive Matrixresultat liefert keinen vollständigen Energie-Impuls-Strom oder Einstein-Grenzfall.
