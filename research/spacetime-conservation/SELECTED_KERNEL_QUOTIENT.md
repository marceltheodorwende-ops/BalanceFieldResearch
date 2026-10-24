# Geschlossene ausgewählte Kernelreduktion bei Anfangsselektion – Runde 44

## Ergebnis

Die konstruktive Reduktion aus Runde43 lässt sich auf eine echte Anfangsselektion erweitern: Maßgeblich ist der **tatsächlich ausgewählte Kernelblock**

k_sel=P_sel K P_sel, P_sel=T_sel T_sel†.

Zusammen mit den vollen F,W,Y,P bestimmt dieser Block den vollständigen nächsten BFG-Ausgang einschließlich Seed bzw. Terminalentscheidung. Der ursprüngliche Block PKP allein genügt bei Q_selection!=I nicht allgemein.

Ein exakter n=2-Faserzeuge hat gleiche ursprüngliche aktive Kernelkompression PKP=-2P, gleiche ambiente Spur und gleiche übrige Felder, aber vollständige K-Ausgänge-1 und-3. Der Unterschied beruht auf der unveränderten Quellregel: F und W werden bei der Selektion mit T_sel transportiert; der Kernelupdate benutzt das ursprüngliche ambiente K in diag(K,K). Ein Ersatz durch T_sel K T_sel† wäre eine andere Dynamik und wird hier nicht vorgenommen.

Vorabregistrierung PROTOCOL.md Runde44. Quelle: vollständiges Dynamic-Order-Manuskript und gepinnter Originalupdate aus SOURCE_MANIFEST.json. Standardmathematik: Kompression, Polar-/SVD-Strukturen und Spektralkalkül. Keine neue physikalische Energie- oder Transportregel.

## 1. Allgemeiner ereignisbezogener Quotient

Gegeben sei ein zulässiger endlicher BFG-Eingang. Q_selection ist der durch Y bestimmte Projektor, T_sel die partielle Polar-Isometrie von Q_selection P und P_sel deren Bildprojektor.

Selektion, Formation/Witness-Transport, Lasten und Analyse hängen nicht von K ab. Auf dem positiv geladenen Analysezweig bildet der metrische Projektor P_G in RanP_sel ab; daher besitzen beide Analyseblöcke und die dünnen SVD-Blöcke U_C,U_B dasselbe Bild:

P_sel U_t=U_t.

Somit

K_+=sum_t U_t† K U_t
    =sum_t U_t† (P_sel K P_sel) U_t.

R4-Daten hängen nur von der behaltenen Nicht-Kernel-Struktur ab. Der Seed bzw. seine Terminalentscheidung wird danach aus K_+ und dem R4-Komplement bestimmt. Damit gilt das Faser-Kriterium II89 für

Pi_sel(Ξ)=(P_sel K P_sel,F,W,Y,P).

Zwei Zustände mit gleichem Pi_sel-Bild erzeugen denselben vollständigen Nachfolger bis auf zulässige SVD-Eichung. Falls ein früher Selektions-/Witness-/Last-Terminalfall eintritt, ist er bereits durch die gleichen Nicht-Kernel-Daten bestimmt. Bei Analyse/Seed-Terminalfällen bleibt der Terminalstatus Teil der reduzierten Ausgabe; ein Nachfolger wird nicht erfunden.

Dieser Quotient behält volle ambiente Geometrie, Formation, Witness und ursprünglichen Träger. Er ist keine isolierte Dynamik des ausgewählten Kernelblocks. Nach einem vollständigen nichtterminalen Ereignis gilt Q_+=I; dann stimmt der ausgewählte Block für das nächste Ereignis mit dem aktiven Block aus Runde43 überein.

## 2. Rekonstruktion und Informationsrang

Auf einem positiv geladenen Analysezweig mit ausgewähltem Rang r_s wähle eine Isometrie J mit JJ†=P_sel. Setze
Y_s=J†YJ, H_s=I+Y_s und k_s=J†KJ.

Dieselben Quellidentitäten wie in Runde43 gelten jetzt mit P_sel:

P_G C=J H_s^(-1) J†,
P_G B=J H_s^(-1) J†Y.

Aus dem vollständigen K_+ und der Analysegeometrie folgt für
Z=J† V Sigma K_+ Sigma V† J

H_s Z H_s=alpha k_s+beta Y_s k_s Y_s.

In einer Y_s-Eigenbasis mit Eigenwerten mu_i wird jeder Matrixeintrag durch Division durch alpha+beta mu_i mu_j rekonstruiert. Auf der kanonischen nichtnegativen Y-Klasse sind diese Divisoren wegen alpha>0 strikt positiv. Die ausgewählte K-Abbildung ist daher injektiv und hat reellen Rang r_s²; sie ist bei festgehaltenen Nicht-Kernel-Daten vollständig positiv und unital vom ausgewählten r_s-Raum in den m-dimensionalen Ausgaberaum.

Die Aussagen beziehen sich auf die vollständige K-Ausgabe und die vollständige behaltene Geometrie, nicht auf Spurwerte allein. Vier Kernelkoordinaten bei r_s=2 begründen weder eine ausgewählte physikalische Raumzeitdimension noch eine Energie-Impuls-Deutung.

## 3. Exakter Zweimoden-Gegenzeuge gegen ursprüngliches PKP

Wähle
Y=diag(1/2,2), Q_selection=diag(1,0),
v=(1,1)/sqrt(2), P=F=W=vv†,
L=diag(1,-1), K_±=-2I±L.

Dann gilt PLP=0 und tr L=0. Somit haben beide Zustände
PK_±P=-2P, tr K_±=-4,
sowie exakt gleiche F,W,Y,P. Sie sind strikt negative Hermitesche Kernel und zulässige Eingaben.

Die Selektion ist T_sel=e1 v†, P_sel=e1 e1†=Q_selection. Sie transportiert F und W auf P_sel, mit Witnessmasse1. Die Lasten sind
Lambda_C=2/3, Lambda_B=1/6,
alpha=1/5, beta=4/5.

Beide Analysekanäle haben nur eine nichtverschwindende Zeile/Spalte. Die dünne Analyse besitzt Rang1, U_C=e1/sqrt(2), U_B=e1/sqrt(2) und
Y_+=8/45.
R4 hat Rang1; es gibt kein Seedkomplement. Folglich sind beide vollständigen Ereignisse nichtterminal, aber

K_{±,+}=e1† K_± e1=-2±1.

Das sind die verschiedenen skalaren Ausgänge-1 und-3. Der ursprüngliche aktive Quotient aus Runde43 scheitert also tatsächlich außerhalb seiner angegebenen Q=I-Klasse, nicht nur mangels eines Beweises. Der neue ausgewählte Quotient unterscheidet die Fälle durch k_sel und bleibt geschlossen.

Zum Vergleich: T_sel K_± T_sel†=-2P_sel in beiden Fällen. Würde man diesen transportierten Kernel anstelle des ursprünglichen ambienten K in die Analyse einsetzen, verschwände genau der Quellunterschied. Eine solche Änderung wäre eine zusätzliche Modellregel, keine Herleitung aus dem gegenwärtigen BFG-Update.

## 4. Frische proportionale Kontrollen

Fünf vorab bestimmte Originalaufrufe:

- Die beiden exakten Gegenzeugen: numerische K-Ausgänge-2.9999999999999987 und-0.9999999999999996; alpha0.2 und Y_+=0.17777777777777778 stimmen mit1/5 und8/45 überein.
- Dieselbe Geometrie mit K=-2I und K+H, H=[[0,.2],[.2,.4]]. Hier P_sel H P_sel=0, während PHP!=0. Die vollständigen Nachfolger sind in der ausgeführten Rechnung exakt gleich (maximaler Feldrest0).
- Komplexer n=4/r=2-Zustand, Seed20261027, Y=diag(.2,.4,.7,1.4): echte Q!=I-Selektion, Abstand ||P_sel-P||_F=0.5879532154901501, ausgewählter Rang2, Ausgangsdimension3. Vollständiges Ereignis nichtterminal; ausgewählte Rekonstruktion bis1.8099701721069553e-14, Stützrest9.55213790351541e-16, Unitalitätsrest1.1369878428188828e-15.

Alle fünf Fälle nichtterminal und Prüfassertionen bestanden. Symbolische Kontrollen prüfen PLP=0, QLQ=Q, alpha1/5 und Ausgangslast8/45 exakt. Vollständige Reproduktion/Ausgabe in [SELECTED_KERNEL_CHECKS.md](SELECTED_KERNEL_CHECKS.md).

Dokumentationsrunde: keine Änderungen an Auditcode, Workflow, Originaldynamik, Manuskripten oder empirischen Ergebnissen; kein neuer Remote-CI-Pass behauptet. Lokale Kontrollen und letzter Remote-geprüfter Code bleiben in CI_VALIDATION.md getrennt.

## 5. Nächste Abhängigkeit

Der für das Ereignis relevante Kernelträger ist nun ohne zusätzliche Auswahlregel durch die vorhandene BFG-Selektion bestimmt. Sein Rang ist jedoch variabel und nicht generell zwei. Zudem beschreibt die Rekonstruktion nur die K-Information bei voller behaltenen Nicht-Kernel-Struktur.

Die nächste konstruktive Frage betrifft eine quellenbasierte lokale Rang-zwei-Unterstruktur oder ein kohärentes System solcher Strukturen, das diese ausgewählte K-Information und die Rangereignisse geschlossen mitführt. Die bereits bewiesenen Auswahl-/Mehrsektor-Grenzen bleiben dabei erhalten. Raumrelation, physikalische Uhr, kalibrierte Energie-/Impulsablesung und Lorentztransport folgen aus diesem Quotienten nicht automatisch.
