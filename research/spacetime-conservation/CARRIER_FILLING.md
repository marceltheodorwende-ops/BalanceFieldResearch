# Leckagerang und endliche Füllung des aktiven Trägers – Runde 45

## Ergebnis und Bedeutung

Aus den unveränderten BFG-Analyse-/R4-/Seedregeln folgt eine exakte Rangrekursion. Beginnt ein positiv geladener Analysezweig mit ausgewähltem Rang r_s, dann gilt: Entweder endet die Fortsetzung terminal, oder der aktive Projektor wird innerhalb von höchstens r_s vollständigen nichtterminalen Ereignissen zum gesamten jeweils verbleibenden Matrixraum P=I.

Insbesondere erreicht ein ausgewählter Rang-zwei-Träger spätestens nach zwei solchen Ereignissen einen vollen aktiven Raum. Ein dauerhaft echter zweidimensionaler aktiver Teilträger in einem größeren ambienten Raum wird durch den aktuellen Quellprojektor P allein daher nicht geliefert.

Dies betrifft **den Quellträger**, nicht jede denkbare zusätzliche lokale Beobachtungsfläche. Bereits untersuchte spektrale/Witness-/Formations-Paarbeobachtungen werden dadurch weder ausgewählt noch pauschal ausgeschlossen. Die Aussage ist ein aus der Quelle abgeleiteter Strukturbeweis, keine Neuheits- oder physikalische Raumzeitbehauptung.

Vorab: PROTOCOL.md Runde45. Quelle und Originalupdate: SOURCE_MANIFEST.json; aufbauend auf den bereits belegten R4-/Seed-/Folge-Q-Identitäten. Standardmathematik: Rang, Unterraumsumme und exakte endliche Rekursion.

## 1. Analyse-Rang ist ausgewählter Rang plus Leckagerang

Sei S=P_sel der tatsächlich ausgewählte orthogonale Projektor, r=rank S. Auf positiv geladenen Analysezweigen gilt mit einer Isometrie J in RanS und H_s=I+J†YJ:

P_G C=J H_s^(-1) J†,
P_G B=J H_s^(-1) J†Y.

Da alpha,beta>0 und H_s invertierbar sind, ist der adjungierte Analyseraum genau

Ran A† = Ran S + Y Ran S.

Definiere den Leckagerang
ell=rank[(I-S)YS].

Die außerhalb von RanS liegenden zusätzlichen Richtungen haben genau diese Dimension; deshalb

m=rank A=r+ell.

Außerdem ell<=r und ell<=n-r. Wegen S<=Q_selection und [Y,Q_selection]=0 gilt bei Anfangsselektion sogar ell<=rank(Q_selection)-r. Diese sind mathematische Kopplungsränge, keine räumlichen Distanzen.

Für Hermitesches Y gilt ell=0 genau dann, wenn S einen reduzierenden Unterraum von Y bildet, also [S,Y]=0.

## 2. Seedrank liefert die Defizitrekursion

Das R4-Bild S4 hat Rang r, weil RanS<=RanV. Sein Komplement im m-dimensionalen Ausgaberaum hat Dimension

dim E=m-r=ell.

Falls ell=0, ist E leer, es gibt keinen Seed, und rank P_+=r=m.

Falls ell>0, verlangt die Quelle für ein **nichtterminales** Ereignis einen einfachen strikt negativen Minimalwert. Genau ein Rang-eins-Seed wird ergänzt, unabhängig davon, ob ell1,2 oder größer ist. Dann

rank P_+=r+1.

Das ambiente Ausgangsmaß ist n_+=m. Sein noch nicht aktiver Dimensionsanteil lautet daher exakt

d_+=n_+-rank P_+=max(ell-1,0).

Bei fehlendem oder entartetem zulässigem Seed endet das Ereignis terminal; die Rangformel wird nicht als Formel eines erfundenen Nachfolgers benutzt.

## 3. Endlicher Übergang zu voller Persistenz

Nach einem vollständigen nichtterminalen Ereignis zeigt die Quelle Q_+=I und unterstützt F_+,W_+ auf P_+. In jedem folgenden nichtterminalen Schritt ist der ausgewählte Träger daher der aktuelle aktive P.

Schreibe d=n-r für seinen inaktiven Dimensionsanteil. Wegen ell<=d folgt

d_+<=max(d-1,0).

Solange d>0, sinkt das nichtnegative ganzzahlige Defizit bei jedem weiteren vollständigen nichtterminalen Ereignis um mindestens1. Es kann auch schneller sinken, weil der ambiente Raum beim Analyseupdate schrumpfen kann.

Bereits beim ersten Ereignis gilt wegen ell<=r_s:
d_1=max(ell-1,0)<=r_s-1.

Nach höchstens weiteren r_s-1 vollständigen Ereignissen ist d=0. Insgesamt also höchstens r_s Ereignisse vom ersten positiv geladenen ausgewählten Rang r_s aus, sofern nicht vorher Terminalität eintritt.

Sobald P=I bei Q=I erreicht ist, bleibt diese volle Persistenzstruktur unter weiteren vollständigen Quellereignissen erhalten: m=n, kein Seedkomplement und P_+=I. Die zuvor bewiesene sektorielle tr K-Erhaltung und konstante Formationsspur gelten dort. Damit wird die skalare Kernelspur nach einem solchen endlichen nichtterminalen Übergang erhalten; daraus folgt keine physikalische Energieeinheit oder vollständige Viererbilanz.

Die Beweisführung verwendet exakten Rang und exakte Arithmetik. Numerischer Rangverlust nahe0 oder Toleranz-Terminalität ist kein Gegenbeweis dieser Aussage; umgekehrt wird ein numerisch beendeter Lauf nicht als unendliche physikalische Geschichte ausgegeben.

## 4. Ausgewählter Rang zwei

Es gibt nur folgende erste nichtterminale Fälle:

| Leckagerang ell | ambiente Ausgangsdimension m | aktiver Ausgangsrang | Defizit |
| --- | ---: | ---: | ---: |
| 0 | 2 | 2 | 0 |
| 1 | 3 | 3 | 0 |
| 2 | 4 | 3 | 1 |

Im dritten Fall hat das nächste Ereignis ell<=1. Bei ell0 wird der ambiente Raum auf Dimension3 verkleinert und vollständig aktiv; bei ell1 wird der vorhandene vierdimensionale Raum vollständig aktiv. Ein eventuelles Seed-Terminal endet stattdessen.

Ein aktiver Rang zwei bleibt somit nur im ersten Fall Rang zwei; dann ist er nach dem Ereignis der **gesamte** zweidimensionale Matrixraum. Bei Kopplung an weitere Richtungen wächst der aktive Rang durch den Seed auf mindestens3. Dies verhindert, den ursprünglichen P ohne weitere Konstruktion als dauerhaft lokales Herm(C²)-Energie-Impuls-Feld in einem größeren persistenten Träger zu verwenden.

Es ist keine Zunahme physikalischen Raums behauptet: die ambiente Dimension nimmt nicht zu. „Füllung“ bezeichnet das Aufschließen des aktiven Rangs an den verbleibenden ambienten Rang, einschließlich möglicher Verkleinerung des ambienten Raums.

## 5. Frische symbolische und originale Kontrollen

Vier exakte rationale Blockbeispiele prüfen ell=0,1,2 bei r=2 und ell=3 bei r=3. Ihre gestapelten Zeilenräume [S;SY] besitzen exakt Rang r+ell.

Sieben vorab festgelegte Originalereignisse, alle nichtterminal:

| Kontrollfamilie | Folge (n,r,ell) -> (m,r_+) |
| --- | --- |
| reduzierender n4/r2-Träger | (4,2,0) -> (2,2) |
| rationaler n3/r2-Zeuge | (3,2,1) -> (3,3) |
| komplexer n4/r2-Fall | (4,2,2) -> (4,3), danach (4,3,1) -> (4,4) |
| komplexer n6/r3-Fall | (6,3,3) -> (6,4), dann (6,4,2) -> (6,5), dann (6,5,1) -> (6,6) |

Damit werden sowohl die kurze Rang-zwei-Grenze als auch die scharfe Drei-Ereignisfolge in einer Rang-drei-Familie kontrolliert. Alle Rank-/Defizitassertionen bestanden; maximaler Frobeniusrest ||P-I||_F bei behaupteter voller Füllung<1.3e-15. Numerische Rangtoleranz der Leckagekontrollen1e-10; das allgemeine Ergebnis folgt aus dem Beweis, nicht aus dieser Toleranz.

Zufallsseed der beiden komplexen Familien20261028; keine Suche nach erfolgreichen Fällen. Vollständige Reproduktion/Ausgabe: [CARRIER_FILLING_CHECKS.md](CARRIER_FILLING_CHECKS.md). Endliche Präfixe bleiben als solche bezeichnet; es wurden keine langen numerischen Historien bei unterlaufenden Lasten erzwungen.

Dokumentationsrunde ohne Audit-/Workflow-/Originalcodeänderung. Kein neuer Remote-CI-Pass behauptet; letzter geprüfter Code und CI sind in CI_VALIDATION.md separat festgehalten.

## 6. Nächste Abhängigkeit

Die ursprünglichen BFG-Analyse-/Seedträger liefern zwar eine geschlossene ausgewählte Kernelbeschreibung, aber im Rang-zwei-Fall keine dauerhafte echte lokale Paarfläche innerhalb eines größeren aktiven Raums. Eine solche Paarfläche müsste aus zusätzlichen quelleninternen Beobachtungsdaten ausgewählt und unter der Dynamik geschlossen fortgesetzt werden; frühere Selektor-/Fasergrenzen bleiben dafür relevant.

Alternativ ist der volle endliche Matrixträger die mathematisch geschlossene Beschreibung. Ihn als physikalische Raumzeit oder seine skalaren Spuren als Energie/Impuls zu identifizieren verlangt weiterhin räumliche Relationen, Uhr, Messabbildung und passende Symmetrie-/Transformationsregeln. Die endliche Rangrekursion allein entscheidet diese physikalische Brücke nicht.
