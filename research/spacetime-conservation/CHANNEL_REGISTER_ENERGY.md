# Kann das C/B-Kanalregister den Energieerwartungsrest tragen? – Runde 47

## Ergebnis und geprüfte Kandidatenklasse

Die beiden vorhandenen C/B-Kanäle liefern eine kanonische mathematische Registerdarstellung des vollen Persistenzkanals. Ihr **vollständiger Registerzustand** genügt jedoch nicht allgemein als Träger des in Runde46 nachgewiesenen Energieerwartungsrests.

Zwei strikt positive Witnesszustände können dasselbe Registerbild besitzen, aber entgegengesetzte Energiedefekte. Auch eine beliebige Hermitesche Energieablesung nur auf diesem Register – nicht bloß zwei klassische Zweigenergien – kann daher nicht für beide Zustände eine additive Gesamtenergiebilanz schließen.

Der Ausschluss betrifft die beschriebene kanonische C/B-Darstellung mit additiver system- und registerlokaler Energie. Er ist kein allgemeiner Unmöglichkeitssatz über offene Quantensysteme, andere physikalische Brücken, gekoppelte System-Register-Observablen oder eine unabhängig hergeleitete Wechselwirkungsenergie.

Vorab: PROTOCOL.md Runde47. Quelle unverändert, nur BFG und explizite endliche Matrixrechnung. Das Kanalregister wird **nicht** als schon vorhandenes physikalisches Reservoir oder neue BFG-Zustandsvariable ausgegeben.

## 1. Darstellung und tatsächliche Quelle strikt unterscheiden

Im ausgerichteten vollen Persistenzsektor gilt
Phi(K)=T_C K T_C+T_B K T_B,
mit Hermiteschen Funktionen T_C,T_B von Y und T_C²+T_B²=I.

Definiere die mathematische Isometrie
V psi=|C> tensor T_C psi+|B> tensor T_B psi.
Dann V†V=I und
Phi(K)=V†(I_register tensor K)V.

Für einen Dichtekandidaten W ist das formale komplementäre Registerbild
Gamma(W)_ab=tr(T_a W T_b), a,b in {C,B}.

Dies ist die Registermarginale der Matrix V W V† und eine mögliche mathematische Darstellung des Kanals. Die tatsächliche BFG-Quelle hat im ausgerichteten vollen Persistenzsektor aber W_+=W. Sie wird hier **nicht** durch eine neue Schrödinger-Dynamik W_+=Phi(W) ersetzt. Lediglich die Spuridentität tr(W Phi(K))=tr(Phi(W)K) erklärt, warum diese Darstellung für den Energieerwartungskandidaten untersucht werden kann.

Eine physikalische Identifikation dieses Registers benötigt eine zusätzliche, unabhängig prüfbare Brücke. Sie wird nicht aus der Existenz einer solchen Isometrie gefolgert.

## 2. Welche Information im Register fehlt

Sei Y=sum_lambda lambda P_lambda. Weil alle T_a Funktionen von Y sind,

Gamma(W)_ab =
sum_lambda t_a(lambda)t_b(lambda) tr(P_lambda W).

Das Register hängt nur von den Y-Spektralgewichten ab. Offdiagonale Witnessdaten zwischen verschiedenen Y-Eigenräumen sind unsichtbar. Die Aussage betrifft das volle komplexe 2x2-Registerbild, nicht nur dessen Diagonalwahrscheinlichkeiten.

Die Energieerwartungsänderung aus Runde46 lautet dagegen
Delta E_W=tr[W(Phi(K)-K)].
Bei K mit Matrixelementen zwischen verschiedenen Y-Eigenräumen kann sie gerade von diesen unsichtbaren Witnesskohärenzen abhängen.

Für festes K und feste Y,F ist daher eine von W unabhängige Energieobservable R auf dem Register nicht allgemein in der Lage, beide Vorzeichen dieses Defekts zu bilanzieren. Eine nach W nachträglich angepasste Observable wäre keine feste Energieablesung derselben Kandidatenklasse.

## 3. Operatorhindernis für jede registerlokale Energie

Sei R eine beliebige Hermitesche 2x2-Matrix auf dem Register, einschließlich komplexer Offdiagonalterme. Ihr Rückzug ist

D_R=V†(R tensor I)V
   =sum_ab R_ab T_a T_b.

Alle Produkte T_a T_b sind Funktionen von Y, also auch D_R. Insbesondere kann D_R keine Offdiagonalteile zwischen verschiedenen Y-Eigenräumen tragen.

Die naheliegende additive Bilanz bei festem initialem Register-Energiewert e0 wäre für alle Eingangs-W:

K+e0 I=Phi(K)+D_R.

Auf jedem Paar verschiedener Y-Eigenwerte besitzt die linke Differenz K-Phi(K) den Eintrag (1-h_ij)K_ij. Bei alpha,beta>0 ist1-h_ij>0. R und e0 können diesen Eintrag nicht erzeugen. Deshalb ist diese Operatorbilanz nur möglich, wenn [K,Y]=0.

Umgekehrt gilt bei [K,Y]=0 bereits Phi(K)=K; R=e0 I_register erfüllt das additive Schema trivial. Die hier geprüfte Registerergänzung behebt also gerade keinen der nichtkommutierenden Energiedefekte. Eine konstante Einheitenumrechnung oder ein konstanter Nullpunkt ändert dieses Offdiagonalhindernis nicht.

Eine unitäre Umbenennung der Registerbasis hilft nicht: Gamma wird nur unitär konjugiert und der gesamte verfügbare Satz von Rückzügen bleibt derselbe.

## 4. Exakter positiver Zeuge mit gleichem vollständigem Registerbild

Wie in Runde46:
P=I2, F=I2, Y=diag(1/5,3/10),
alpha=8/133, beta=125/133.

Die beiden hergeleiteten Kanaloperatoren lauten exakt

T_C=diag(sqrt(8/13),sqrt(32/77)),
T_B=diag(sqrt(5/13),sqrt(45/77)).

Ihre Quadrate summieren sich zu I. Der transversale Faktor ist
h=31/sqrt(1001)<1.

Für j=x oder y halte K=2I+sigma_j fest und wähle die beiden Witnesszustände
W_±=(I±sigma_j/2)/2.
Beide haben Eigenwerte1/4 und3/4; K hat Eigenwerte1 und3.

Für alle vier Witnessfälle ist das vollständige Registerbild **exakt dieselbe Matrix**

Gamma=1/1001 [[516,155 sqrt(10)],[155 sqrt(10),485]].

Die Energieerwartungen sind jedoch
E_±=2±1/2,
E_{±,out}=2±h/2,
Delta E_±=±(h-1)/2.

Der Betrag ist ungefähr0.0100918555382141, die Vorzeichen sind entgegengesetzt. Eine gleiche Registerenergieänderung kann nicht beide kompensieren. Auch nichtlineare reine Ablesefunktionen desselben Gamma-Bildes würden diese beiden Witnessfälle nicht unterscheiden; dies ist ein Informationsargument, keine angenommene physikalische Nichtlinearität.

Es gibt hier weder Seed noch Rangwechsel oder Formationstransportverlust. Der Unterschied ist keine positive Lastreserve: die Source-F/Y-Lasten sind für beide Witnesszustände dieselben, und selbst das vollständige Kanalregister enthält die nötige Kohärenzinformation nicht.

## 5. Frische Originalkontrollen

Vier vollständige Originalereignisse, keine Parametersuche:

| Achse | Witnessvorzeichen | Erwartung vorher | Erwartung nachher | Defekt |
| --- | ---: | ---: | ---: | ---: |
| x | - | 1.5 | 1.5100918555382141 | +0.010091855538214123 |
| x | + | 2.5 | 2.489908144461786 | -0.010091855538214123 |
| y | - | 1.5 | 1.5100918555382141 | +0.010091855538214123 |
| y | + | 2.5 | 2.489908144461786 | -0.010091855538214123 |

Alle Ereignisse nichtterminal; Witness bleibt im ausgerichteten Quellrahmen konstant. Die vollständigen Registermatrizen stimmen numerisch exakt überein (Differenzrest0). Zusätzlich symbolisch geprüft: Isometriebedingung, Gamma-Gleichheit, h sowie verschwindende Offdiagonalen des Rückzugs einer beliebigen komplex Hermiteschen Registerenergie.

Vollständiger Prüftext/Ausgabe: [CHANNEL_REGISTER_CHECKS.md](CHANNEL_REGISTER_CHECKS.md). Der allgemeine Operatorbeweis ist von numerischen Kontrollen getrennt. Dokumentationsrunde ohne Audit-/Workflow-/Originalcodeänderung; kein neuer Remote-CI-Pass behauptet. Letzter geprüfter Code und CI bleiben in CI_VALIDATION.md separat.

## 6. Nächste Abhängigkeit

Die naheliegende Erklärung „Energie geht in die C/B-Zweige“ ist als additive registerlokale Bilanz für diese Kandidatenklasse nicht ausreichend – selbst unter Beibehaltung des vollständigen zweidimensionalen Kanalregisterzustands.

Eine weitergehende Erklärung müsste eine aus BFG begründete K- und kohärenzabhängige System-Register-Kopplung oder eine andere physikalisch ausgewählte Energieablesung liefern. Das bloße Erfinden einer passenden Wechselwirkungsenergie nach Kenntnis des Defekts wäre keine Herleitung. Die Quelle bestimmt bisher in dieser Untersuchung weder eine solche physikalische Kopplung noch die nötigen Maße und Kalibrierungen.

Rho_Q-/H-Abbildung, unabhängige Präparation, Energie- und Uhrkalibrierung sowie die räumliche Impuls-/Lorentzbrücke bleiben offen. Dieser begrenzte Kanalregisterbefund liefert keinen vollständigen Energie-Impuls-Strom und keinen Einstein-Grenzfall.
