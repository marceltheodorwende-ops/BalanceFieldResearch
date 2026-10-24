# Energieerwartung der BFG-internen Quantenkandidaten – Runde 46

## Ergebnis und physikalischer Vorbehalt

Die endliche Trägerfüllung aus Runde45 führt in einen Sektor mit erhaltener tr K. Das reicht jedoch nicht für eine konservierte physikalische Energieerwartung: Beim im Manuskript genannten Kandidaten rho_Q=W kann tr(WK) trotz konstantem Witness, konstantem Formationsbestand und konstantem tr K variieren – ohne Seed, Auswahlverlust oder Rangwechsel und sogar bei strikt positivem K.

Für festgehaltenen vollen Persistenzzustand der Nicht-Kernel-Felder gilt exakt:

tr(rho K) ist für jedes Hermitesche K im Schritt erhalten
genau dann, wenn [rho,Y]=0,

wobei rho=W oder rho=F/tr F die beiden geprüften Manuskriptkandidaten sind.

Dies widerlegt **keine allgemeine physikalische Energieablesung**. Ein physikalischer Hamiltonoperator kann unter Antrieb oder Austausch eine veränderliche Energieerwartung besitzen. Gezeigt ist die fehlende automatische Identifikation als konservierte isolierte Gesamtenergie; eine vollständige Arbeits-/Austausch-/Reservoirbilanz müsste zusätzlich aus der Quelle und einer unabhängigen Messbrücke hergeleitet werden.

Vorabprotokoll PROTOCOL.md Runde46. Ausschließlich die gepinnte BFG-Quelle und Standardmathematik. Keine Schrödinger-/Feld-/Einsteingleichung wird als zusätzliche BFG-Dynamik eingeführt.

## 1. Quellenstatus der Hypothesen

Frisch nachgelesen: I57 (PDF54) nennt rho_Q=W und rho_Q=F/tr F ausdrücklich als verschiedene zu diskriminierende Quantenbrücken. Ihre physikalische Wahl benötigt unabhängige Präparation, kalibrierte Messung und ein vorab festgelegtes Ablehnungskriterium.

I68.2 (PDF59) verlangt einen von der Quantenbrücke gelieferten energiehaltigen Hamiltonoperator und verknüpft dessen Spektraldifferenzen mit Spektroskopie. I70.2/70.6 (PDF60–61) typisiert K,F in Formationseinheiten, rho_Q dimensionslos und H in Energieeinheiten.

**Zusätzliche Identifikationshypothese dieser Kontrolle**, nicht bereits BFG-Theorem:
H=epsilon_E K+E0 I,
mit festem epsilon_E!=0 als unabhängig zu bestimmender Einheitenumrechnung und festem Nullpunkt E0. Dann ist der zugehörige Kandidat
E=tr(rho H)=epsilon_E tr(rho K)+E0.

Ein Defekt in tr(rho K) wird durch eine feste Umrechnung nur skaliert; der feste Nullpunkt verschwindet aus der Differenz. Keine Parameter werden auf Erhaltung angepasst.

## 2. Exakte Erwartungsbilanz im vollen Persistenzsektor

Voraussetzungen: P=I, 0<Y<I, positive Lasten und unterstützte zulässige F,W. Im ausgerichteten Quellrahmen sind F und W unter dem vollständigen Ereignis konstant. Der Kernel wird durch den zuvor hergeleiteten Kanal

Phi(K)=T_C K T_C+T_B K T_B

entwickelt. Die beiden T sind Hermitesche Funktionen von Y und erfüllen T_C²+T_B²=I. Daher ist Phi bezüglich der Spurpaarung selbstadjungiert:

tr(rho Phi(K))=tr(Phi(rho) K).

Weil auch rho=W bzw. F/tr F in diesem Rahmen konstant ist, gilt

Delta E_rho=tr[(Phi(rho)-rho) K].

Das ist eine exakte Bilanz derselben Quelldynamik, noch keine physikalisch kalibrierte Wärmemenge oder Arbeit.

In einer Y-Eigenbasis mit Eigenwerten y_i wirkt der Kanal als
Phi(K)_ij=h_ij K_ij,
h_ij=(alpha+beta y_i y_j)/
sqrt[(alpha+beta y_i²)(alpha+beta y_j²)].

Exakte algebraische Identität:
1-h_ij² =
alpha beta (y_i-y_j)²/
[(alpha+beta y_i²)(alpha+beta y_j²)].

Bei alpha,beta>0 ist h_ij=1 genau dann, wenn y_i=y_j; sonst0<h_ij<1. Damit Phi(rho)=rho genau dann, wenn rho keine Matrixelemente zwischen verschiedenen Y-Eigenräumen besitzt, also [rho,Y]=0.

Da die Spurpaarung auf Hermiteschen Matrizen nicht entartet ist, ist dies notwendig und hinreichend für Delta E_rho=0 **für jedes K** bei festem Nicht-Kernel-Zustand. Ein bestimmtes K kann auch außerhalb dieser Klasse zufällig Defekt0 haben; daraus folgt keine universelle Erhaltung.

Für rho=W lautet die Bedingung [W,Y]=0. Für rho=F/tr F lautet sie [F,Y]=0. Die Formationsnormierung entfernt eine frühere Nichtinvarianz von tr(FK) nicht allgemein, weil tr F in diesem Sektor konstant bleibt.

## 3. Exakter positiver Zwei-Moden-Zeuge

Wähle
P=I2, Y=diag(1/5,3/10), F=I2,
W=(I2+sigma_x/2)/2,
K_±=2I2±sigma_x.

W hat Eigenwerte1/4 und3/4; beide K haben Eigenwerte1 und3. Alle relevanten Energieoperator-/Dichtekandidaten sind somit strikt positiv. P=I bleibt voll; es gibt keinen Seed.

Die aus F,Y bestimmten Quellgewichte ergeben
alpha=8/133, beta=125/133,
h=31/sqrt(1001)<1.

F und W bleiben exakt konstant; K_{±,+}=2I±h sigma_x. Die skalaren Ablesungen lauten:

| Kandidat | Eingang | Ausgang | Defekt |
| --- | --- | --- | --- |
| tr K_± | 4 | 4 | 0 |
| tr[(F/tr F)K_±] | 2 | 2 | 0 |
| Witness, Plus-Eingang 2I+sigma_x | 5/2 | 2+h/2 | (h-1)/2 |
| Witness, Minus-Eingang 2I-sigma_x | 3/2 | 2-h/2 | (1-h)/2 |

Die Indizes ± in dieser Tabelle bezeichnen die beiden Eingangskandidaten; das jeweilige Ausgangsereignis ist in der Ausgangsspalte angegeben. Der Betrag des Witnessdefekts ist ungefähr0.0100918555382141 Formationseinheiten vor einer etwaigen Energieumrechnung.

Bei derselben Geometrie und W=I/2 ist die Witnesserwartung dagegen konstant2; dies kontrolliert die Kommutantenbedingung.

W und F/tr F sind im ersten Zeugen verschiedene Zustandskandidaten. Dass der Formationskandidat hier einen konstanten Erwartungswert liefert, wählt ihn nicht automatisch als physikalisch richtig aus. Dies bleibt der in I57 geforderte unabhängige Brückentest; allgemeine F mit [F,Y]!=0 sind nach dem obigen Satz ebenfalls nicht universell konservierend.

## 4. Was damit als Zusatzbilanz nicht genügt

Für die beiden K_± sind sämtliche Nicht-Kernel-Eingangs- und Ausgangsfelder identisch. Die Witnessdefekte haben aber entgegengesetzte Vorzeichen. Ein universeller additiver Zustandskorrekturterm R(Y,F,W,P), der nicht von K abhängt, hat in beiden Fällen dieselbe Änderung und kann nicht beide Defekte ausgleichen.

Dies ist dieselbe typisierte Grenze wie in Runde42, jetzt für die konkrete manuskriptinterne Erwartungslesung ohne Seed-/Rangereignis. K-abhängige Arbeits-/Austauschgrößen oder andere physikalische Abbildungen werden nicht ausgeschlossen. Sie sind jedoch in diesem Zeugen nicht durch eine bloße Umdeutung von tr F, tr W oder einer K-blinden Geometrieenergie geliefert.

Die Kommutantenklasse liefert eine positive Kontrollalternative: Wenn rho bereits mit Y kommutiert, bleibt sie im vollen ausgerichteten Sektor auch mit Y_+=g(Y) kommutierend und die entsprechende Erwartung bleibt dort erhalten. Das ist eine mathematisch erhaltene Teilklasse, keine hergeleitete Messkalibrierung oder Impulsdynamik.

## 5. Frische proportionale Prüfungen

Vier Originalaufrufe, alle vollständig nichtterminal, ohne Parametersuche:

| Fall | Witness-Eingang | Witness-Ausgang | Defekt |
| --- | ---: | ---: | ---: |
| K_- | 1.5 | 1.5100918555382141 | +0.010091855538214123 |
| K_+ | 2.5 | 2.489908144461786 | -0.010091855538214123 |
| W=I/2, K_+ | 2 | 2 | 0 |
| komplexe Eichversion K_+ | 2.4999999999999996 | 2.4899081444617845 | -0.010091855538215011 |

Formationsenergieablesung jeweils2 bis Rundung; Kernelspur4 bis Rundung. Maximaler Eichrest der vollständigen ausgerichteten Felder2.0859727843219497e-15. Symbolische Kontrollen bestätigen alpha, h und die allgemeine h-Defektidentität exakt. Die bereits bekannte Kanalform wird hier gezielt auf den **physikalischen Erwartungskandidaten aus I57/I68** angewandt; keine Neuheit der allgemeinen linearen Fixpunktklassifikation behauptet.

Vollständiger Prüftext/Ausgabe: [QUANTUM_ENERGY_CHECKS.md](QUANTUM_ENERGY_CHECKS.md). Keine Audit-/Workflow-/Originalcodeänderung; kein neuer Remote-CI-Pass behauptet. Lokale Evidenz und letzter geprüfter Code bleiben in CI_VALIDATION.md getrennt.

## 6. Konkreter nächster physikalischer Prüfschritt

Für die Hypothese H=epsilon_E K+E0 I ergibt derselbe Zeuge einen relativen Spektrallückenfaktor h: die Lücke2 wird zu2h. Der Quotient ist unabhängig von festem Nullpunkt und fester Energieumrechnung. Nach I68.2 wäre das bei einer tatsächlich festgelegten Quanten-/Präparationsbrücke ein entsprechender relativer spektroskopischer Prüfwert.

Dies ist **noch keine Vorhersage für ein reales Atom oder eine vorhandene Messreihe**: M_prep muss zuerst unabhängig den BFG-Zustand bestimmen, rho_Q und H-Abbildung müssen vorab ausgewählt werden, und Uhr/Präparation/Apparatur müssen den Vergleich tragen. Ohne diese Angaben wird kein empirischer Energieaustausch behauptet.

Für eine konservierte Gesamtenergie muss außerdem festgelegt werden, ob und wie der Erwartungsdefekt in einen aus derselben Quelle hergeleiteten K-abhängigen Austausch eingeht. Impuls benötigt weiterhin räumliche Relationen und Generator-/Transformationsidentifikation. Die erhaltene Kernelspur nach Trägerfüllung allein schließt diese Aufgaben nicht.
