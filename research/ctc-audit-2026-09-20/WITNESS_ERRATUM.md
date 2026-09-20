# Erratum: persistenter Raum in Unified V4, Gleichung 27

## Gegenbeispiel

Die lineare Hülle aller vorwärts beschränkten, nichtverschwindenden Orbits definiert nicht den peripheren Spektralraum. Für R=diag(1,1/2) haben e1 und e1+e2 beschränkte nichtverschwindende Orbits. Damit enthält ihr Spann auch e2, obwohl R^k e2 gegen null geht. Die linke Definition in V4 (27) liefert den ganzen Raum, die behauptete rechte Spektralcharakterisierung nur span(e1).

Bei endlichdimensionaler globaler Potenzbeschränktheit, nichtnulligem semisimplem peripherem Raum und strikt stabilem Komplement ist dieser Widerspruch allgemein: Für jeden stabilen Vektor s und einen persistenten p≠0 sind p und p+s Witnessvektoren; ihre Differenz ist s. Die Spannbildung nimmt daher den stabilen Raum wieder auf.

## Reparierte Definition und Grenzen

Arbeite zunächst auf einem endlichdimensionalen komplexen Hilbertraum mit potenzbeschränktem R und nichtleerem peripherem Spektrum sigma_per={lambda:|lambda|=1}. Für reelle Daten verwende die Komplexifizierung und den zugehörigen reellen invarianten Raum.

Definiere P_R als Rieszprojektor um genau den isolierten peripheren Spektralblock und W=Ran(P_R). Die Kontur liegt im Resolventengebiet. Potenzbeschränktheit schließt nichttriviale periphere Jordanblöcke aus. Deshalb ist W die direkte Summe der Eigenräume mit |lambda|=1.

Der Fall eines leeren stabilen Spektrums ist nicht instabil: R=I hat W=H. Ein Gate mit max über das stabile Spektrum braucht dafür eine ausdrückliche Konvention. Dieses Erratum legt keine allgemeine Gate-Konvention für alle BFG-Modelle fest. Im SA-Zweig ist für jeden Zustand d≥2 ein stabiler Modus vorhanden.

## Dynamische Äquivalenz als Satz

Unter den obigen endlichen Voraussetzungen ist W genau der Raum der Anfangswerte beidseitig beschränkter vollständiger Orbits x_(k+1)=R x_k, k in Z.

Beweis: Auf dem semisimplen peripheren Raum ist R invertierbar und alle ganzzahligen Potenzen sind gleichmäßig beschränkt, da eine Diagonalisierung nur Eigenwerte vom Betrag eins enthält. Das liefert vollständige beschränkte Orbits für jedes x in W.

Umgekehrt projiziere einen solchen Orbit mit I−P_R auf den stabilen invarianten Raum. Für jedes m gilt s_0=R_s^m s_(−m). Die Folge s_(−m) ist beschränkt und ||R_s^m||→0, somit s_0=0. Dies umfasst auch nilpotente stabile Blöcke und Eigenwert null. Bei leerem stabilen Raum ist diese Richtung unmittelbar erfüllt.

Diese Äquivalenz ist keine Behauptung über alle unendlichdimensionalen Operatoren.

## Metrischer Projektor

Für G=G*>0 und eine Vollrangbasismatrix Z von W lautet der verwendete G-orthogonale Projektor

    P_G=Z(Z*GZ)^(-1)Z*G.

Er besitzt dasselbe Bild wie P_R, ist aber im Allgemeinen ein anderer Operator. P_R kommutiert mit R; P_G ist G-selbstadjungiert und G-kontraktiv. Gleichheit gilt genau dann, wenn der stabile Spektralraum das G-orthogonale Komplement von W ist. Für Keep/Upward wird P_G verwendet, nicht ohne Beweis der Rieszprojektor.

## Auswirkung

Die ursprüngliche Spann-Definition wird ersetzt, nicht nachträglich als gleichwertig interpretiert. Das historische diagonale Beispiel 5→4→3→2 verwendet die reparierte spektrale Fassung und eine zusätzliche Rekursionsregel. Es ist kein Beweis für V4 in seiner unveränderten ursprünglichen Form. Auch frühere Reviewrunden hatten diesen Fehler zunächst übersehen; die vorliegende Korrektur hält diesen negativen Befund fest.
