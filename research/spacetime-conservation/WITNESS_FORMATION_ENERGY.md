# Witness-gewichtete Formation: erhaltener Energiekandidat über Seedereignisse – Runde 51

## Positives mathematisches Ergebnis

Die BFG-eigene Paarung

E_WF=tr(WF)

ist bei gemeinsam beibehaltenem Träger von W und F unter vollständigen nichtterminalen Ereignissen erhalten – **einschließlich echter Seed- und Rangereignisse**. Nach dem ersten vollständigen nichtterminalen Ereignis sind die dafür benötigten Quellbedingungen für die weitere Fortsetzung gegeben.

Stärker: Die gesamte Witness-gewichtete Formationsspektralverteilung und insbesondere tr(W F^p) sind dann erhalten. Die zusätzliche Seedformation liegt orthogonal zum Witness und hat in diesen Ablesungen Gewicht0.

Damit gibt es einen konkreten BFG-internen positiven Kandidaten außerhalb der zuvor ausgeschlossenen Nur-K-Klassen: **zusätzliche physikalische Hypothese** rho_Q=W, H=epsilon_F F+E0 I. Die Erhaltung folgt aus den originalen Selektions-/R4-/Seedregeln, nicht aus einem hinzugefügten Gegenkonto. Eine Joule-Kalibrierung, Zeitgeneratorrolle oder vollständige physikalische Energie-Impuls-Identifikation ist damit noch nicht hergeleitet.

Vorab: PROTOCOL.md Runde51. Ausschließlich gepinnte BFG-Quelle und Standardmathematik. Der direkte Operator F ist eine andere Ablesung als die in Runde49 geprüfte Projektion D_F(K).

## 1. Allgemeine Selektionsformel und R4-/Seedbeweis

Sei T_sel die partielle Polar-Isometrie der Selektion und
S=T_sel†T_sel, m=tr(SW)>0.

Die Quelle definiert
W_sel=T_sel W T_sel†/m,
F_sel=T_sel F T_sel†.

Auf vollständigen nichtterminalen Zweigen wirkt R4 als Isometrie auf dem ausgewählten Träger:
T4†T4=P_sel.
Die zweite Witnessmasse ist exakt1. Vor dem Seed sind
W4=T4 W_sel T4†,
F4=T4 F_sel T4†.

Das folgt aus den bereits belegten Original-R4-Identitäten; es ist keine neu vorgeschlagene Transportregel. Für den tatsächlichen Seed gilt
F_out=F4+s Pi_seed,
W_out=W4,
mit Pi_seed orthogonal zum R4-Bild S4. Daher W4 Pi_seed=0 und

tr(W_out F_out)=tr(W_sel F_sel)
               =tr(S W S F)/m.

Auch ein nichtleeres mehrdimensionales Seedkomplement ändert den Beweis nicht: der einzelne gewählte Seed liegt weiterhin außerhalb des Witnessbildes. Falls die Quelle terminal endet, wird kein Ausgangserwartungswert erfunden.

Bei Selektion mit m=1 hat positives W vollständig Träger in S. Bereits der erste Moment E_WF ist dann erhalten, denn SWS=W und tr(SWSF)=tr(WF). Für die stärkere gesamte Spektralaussage braucht man zusätzlich eine gemeinsam beibehaltene Formation, beispielsweise SFS=F.

## 2. Warum die benötigte Klasse nach dem ersten Ereignis gilt

Die Quelle liefert nach jedem vollständigen nichtterminalen Ereignis
0<Y_out<I und F_out,W_out auf P_out unterstützt.

Bei jedem folgenden Ereignis ist deshalb Q_selection=I, T_sel=P und S=P. Dann gelten gleichzeitig
SFS=F, SWS=W und m=1.

Folglich bleibt E_WF bei jeder weiteren vollständigen nichtterminalen Fortsetzung exakt gleich, unabhängig davon, ob K eine Seedbildung auslöst, ob der aktive Rang wächst oder ob der ambiente Raum schrumpft. Die endliche Trägerfüllung aus Runde45 ist hierfür nicht erst abzuwarten.

Das ist eine Erhaltung **ab dem ersten Nachfolger bzw. auf der genannten Klasse**, nicht eine unbedingte globale Erhaltung über jede mögliche ursprüngliche Rangverlustselektion.

## 3. Erhaltung der gesamten Witness-Formationsspektralverteilung

Bei gemeinsamer Trägerretention transportiert V=T4 T_sel die alten W-/F-Blöcke isometrisch. Schreibe schematisch auf dem Ausgaberaum
W_out=V W V†,
F_out=V F V† + s Pi_seed,
Pi_seed V=0.

F4 und der Seedblock haben orthogonale Träger. Für jedes p>=1 gilt daher
F_out^p=V F^p V†+s^p Pi_seed,
auf eventuellen weiteren Nullräumen entsprechend ergänzt. Der Witness sieht ausschließlich den ersten Block, also

tr(W_out F_out^p)=tr(W F^p).

Ebenso folgt für jede wohldefinierte reelle Funktion f auf den endlichen Formationsspektren
tr[W_out f(F_out)]=tr[W f(F)].

Die Wahrscheinlichkeit
mu_F^W(B)=tr[W 1_B(F)]
ist nichtnegativ, hat Gesamtmasse1 und bleibt unter der gemeinsamen Retention unverändert. Eine neue Seed-Eigenvalue trägt Witnessgewicht0 – auch dann, wenn sie mit einem alten Formationswert zusammenfällt. Es werden keine Spektrallücken, eindeutigen Eigenvektoren oder nachträglich gespeicherten Eigenlabels benötigt.

**Wichtige Grenze:** Witnessmasse m=1 allein genügt nicht für alle höheren Momente, wenn F durch die Selektion zusätzlich komprimiert wird. Allgemein lautet die korrekte Formel
tr(W_out F_out^p)=tr[SWS (SFS)^p]/m.
Die stärkere Invarianz wird hier nur bei gemeinsam behaltenem W/F, insbesondere nach dem ersten Quellereignis, behauptet.

Die Existenz vieler erhaltener Ablesungen f(F) macht den physikalischen Hamiltonoperator noch nicht eindeutig. F trägt die richtige gemeinsame Formationseinheit für den einfachsten linearen Kandidaten; die Umrechnung in Energie und die Auswahl dieser Funktion bleiben unabhängig zu begründen.

## 4. Physikalischer Kandidat und naheliegende Alternativen

I57/I70 unterscheiden Witness und normalisierte Formation als mögliche Quantenzustände. Für rho_Q=W und
H1=epsilon_F F+E0 I
ist die Erwartung
E1=epsilon_F tr(WF)+E0
auf der bewiesenen Klasse erhalten. W ist dimensionslos, F hat Formationseinheit EF; epsilon_F hätte die unabhängig zu kalibrierende Einheit Energie/EF. Noch keine Joule-Zahl ist aus dem Kernel bestimmt.

Die ebenso positive, gleich typisierte Alternative
H2=(tr F)W
hat dagegen bei gemeinsamer Retention
tr(W H2)=tr F * tr(W²).
R4 erhält die Witnessreinheit tr(W²), während tr F durch den Seed um s wächst. Folglich

Delta tr(W H2)=s tr(W²).

Ein Seed trennt damit zwei im vollen Persistenzsektor beide erhaltene Operatorablesungen. In der festen Mischklasse H_t=(1-t)F+t(tr F)W kann universelle Witness-Erhaltung auch über solche Seeds nur bei t=0 gelten. Dies wählt F innerhalb dieser einfachen Klasse aus; es beweist keine eindeutige Auswahl unter allen f(F) oder vollen Zustandsablesungen.

Auch der alternative Quantenzustand rho_Q=F/tr F mit H=F ist nicht mit der Witnesspaarung gleichzusetzen. Seine Ablesung lautet tr(F²)/tr F. Bei orthogonalem Seed mit Masse s wird sie zu
[tr(F²)+s²]/[tr F+s]
und ist nicht allgemein konstant.

Ein erhaltener positiver Erwartungswert ist zudem noch kein aus der Quelle hergeleiteter Zeittranslationsgenerator. Uhr, gekoppelte Dynamik, Präparation und instrumentelle Energieablesung bleiben zu konstruieren bzw. unabhängig zu testen.

## 5. Präzise Anfangsselektionsgrenze

Exakter Gegenfall zur unbedingten globalen Erhaltung:
P=I2,Y=diag(1/2,2),F=diag(1,3),W=I2/2,K=-I2.

Q_selection=S=diag(1,0), m=1/2. Der vollständige nichtterminale Ausgang ist eindimensional mit F_out=W_out=1. Daher

E_WF,in=2,
E_WF,out=1,
tr(SWSF)/m=(1/2)/(1/2)=1.

Der Unterschied ist die konkrete Konditionierung der ausgewählten Witness-/Formationsteile. Die Quellen-Witnessmasse wird nicht ohne zusätzliche Instrumentbrücke als physikalische Detektionswahrscheinlichkeit interpretiert, und der weggefallene Beitrag wird nicht als bereits identifizierte physikalische Exportenergie bezeichnet. Eine vollständige Anfangs-/Umweltbilanz bleibt offen.

## 6. Frische Originalkontrollen

Fünf vorab festgelegte unterschiedliche Zustände, final alle nichtterminal:

| Fall | E_WF vorher | E_WF nachher | wesentliche Grenze/Alternative |
| --- | ---: | ---: | --- |
| rationaler n3/r2-Seedzeuge | 0.71 | 0.7100000000000003 | Seedformation1.2568997908165356 |
| anfängliche Rangverlustselektion | 2 | 1 | m=1/2, exakte Konditionierungsformel |
| voller positiver n2-Fall | 2 | 2 | H2-Erwartung2.5 ebenfalls konstant |
| komplexer n4/r2-Seedfall | 4.941012642844755 | 4.941012642844755 | Seedformation13.572867421344021 |
| komplexe Eichversion | 4.941012642844755 | 4.941012642844756 | gleiche gewichtete Momente |

Im rationalen Seedzeugen wächst die H2-Erwartung von0.71 auf1.338449895408268; die alternative Formationsdichte-Energie von0.828450704225352 auf1.0296228097929387. E_WF bleibt gleich. Die höheren Witnessmomente p=2,3 bleiben in den gemeinsam behaltenen Fällen ebenfalls gleich.

Im vollen n2-Fall besitzen F=diag(1,3) und (tr F)W=2I+sigma_x dieselben Eigenwerte1,3, aber ihre Witness-Erwartungen sind2 und2.5. Diese Differenz ist unitär invariant bei gleichzeitigem Basiswechsel aller Felder. Gleiches Spektrum und sektorielle Erhaltung allein wählen deshalb keine eindeutige physikalische Operatorablesung; die zusätzliche Seedbilanz diskriminiert die beiden Kandidaten.

Maximaler normierter Moment-/Selektionsformelrest im finalen Lauf2.4997881780332166e-15, maximaler Witness-Seed-Überlapprest1.7057136075561954e-16, normierter Eichmomentrest3.845827966204958e-16. Vollständige Reproduktion/Ausgabe: [WITNESS_FORMATION_CHECKS.md](WITNESS_FORMATION_CHECKS.md).

Prüfverlauf transparent: ein erster Lauf bestand für die fünf Testzustände; danach wurde die Assertion für höhere Momente ausdrücklich auf gemeinsame F/W-Retention statt nur m≈1 eingegrenzt. Der nächste Lauf bestand die Rechnungen, brach aber bei JSON-Serialisierung eines NumPy-Bools ab. Nach Umwandlung in Python-bool bestand der vollständige finale Lauf. Damit15 Originalaufrufe insgesamt auf fünf unterschiedlichen Zuständen, fünf im finalen Lauf. Keine Änderung der Quelle und kein numerisches Gegenresultat verschwiegen.

Dokumentationsrunde ohne Audit-/Workflow-/Originalcodeänderung; kein neuer Remote-CI-Pass behauptet. Lokale Evidenz und letzter Remote-geprüfter Code bleiben separat in CI_VALIDATION.md.

## 7. Nächster notwendiger physikalischer Schritt

Der direkte Formationsoperator mit Witnesszustand ist jetzt ein mathematisch begründeter Kandidat, der echte Seed-/Rangereignisse übersteht. Die positive nächste Prüfung muss deshalb konkret rho_Q=W und H proportional F mit einer unabhängig bestimmten BFG-Präparation und Energieablesung verbinden – einschließlich der anfänglichen Selektionskonditionierung und einer Generator-/Uhrkonstruktion, falls H als Hamiltonoperator gemeint ist.

Die Erhaltung erklärt noch keinen räumlichen Energiefluss oder drei Impulskomponenten. Der vollständige Energie-Impuls-Strom, Lorentztransport und Einstein-Grenzfall bleiben offen. Der neue Invariantensatz ist hierfür ein Ansatzpunkt, keine abgeschlossene physikalische Identifikation.
