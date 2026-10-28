# Feste lineare Bestandsgewichte und erhaltene Teilklassen – Runde 41

## Ergebnis

Für feste reelle, zustands- und ereignisunabhängige Koeffizienten a,b gibt es auf der zulässigen nichtterminalen BFG-Klasse **keine nichttriviale universell erhaltene Größe**
E_{a,b}=a tr(PK)+b tr F.

Das folgt aus zwei bereits exakt belegten Quellzeugen und einem einfachen Determinantenargument. Eine nachträgliche feste Umrechnung oder Umgewichtung der beiden Bestände schließt die Lücke somit nicht. Der Satz betrifft diese lineare Kandidatenklasse, nicht jede nichtlineare, historiesensitive oder zusätzliche physikalische Energieabbildung.

Zugleich sind erhaltene Teilklassen präzise abgrenzbar. Der aktive Transportrest ist spurfrei und an den nichtskalaren Anteil von PKP gekoppelt. Er ist kein allgemeiner Dissipationsterm: derselbe Quellkanal erzeugt mit zwei zulässigen K-Kandidaten entgegengesetzte Vorzeichen.

Vorabprotokoll: PROTOCOL.md Runde41. Quelle, Einheiten und kappa_F=1 wie in PHYSICAL_IDENTIFICATION.md und SOURCE_MANIFEST.json. Nur BFG und Standardmathematik; keine neue physikalische Prämisse.

## 1. Struktur des Restes

Voraussetzungen für diesen Abschnitt: Q_selection=I, Formation/Witness auf P unterstützt, Witnessspur1, Rang(P)=r, positive duale Lasten und vollständiges nichtterminales Ereignis. Damit T_selection=P, P_sel=P und ell_F=0.

Mit den tatsächlichen Analyseblöcken U_C,U_B und dem vor dem Seed transportierten Projektor S4 definiere

B4=sum_t U_t S4 U_t†, X=B4-P.

Weil alle Analysezeilenbilder in RanP liegen, gilt P U_t=U_t. Der Quellsatz RanP<=RanV und R4 liefern Rang S4=r. Die Gesamtisometrie U erfüllt U†U=I_m. Daraus folgt:

- B4>=0 und P B4 P=B4.
- tr B4=tr(S4 sum U_t†U_t)=r.
- Jeder Block U_t ist eine Kontraktion mit Bild in P; deshalb U_t U_t†<=P und B4<=sum U_t U_t†<=2P.
- X=PXP, tr X=0 und -P<=X<=P.

Die exakte Seed-Kompensation aus Runde39/40 gibt

Delta[tr(PK)+tr F]=tr(KX)=tr[(PKP-k0 P)X]

für jedes reelle k0. Der skalare Teil des aktiven Kernels trägt nichts zum Rest bei. Der Operator X kann trotz Spur0 von0 verschieden sein. Keine dieser Identitäten ordnet dem Rest ein physikalisches Raum-/Zeitmaß zu.

Als quantitative Einzelschrittschranke folgt mit k0 als Mitte der extremalen Eigenwerte von PKP auf RanP:

|Delta E_act| <= (lambda_max-lambda_min)/2 * ||X||_1
              <= r (lambda_max-lambda_min)/2.

Hier ||.||_1 ist die Spur-Norm. Dies ist eine mathematische Restschranke, kein physikalisches Energiegesetz.

## 2. Erhaltene Teilklassen – hinreichend, nicht als vollständig klassifiziert behauptet

**Aktiver Rang eins.** Dann ist B4 ein positives Vielfaches von P, dessen Spur1 ist. Also B4=P und X=0. Der kombinierte Bestand bleibt in jedem solchen nichtterminalen Ereignis erhalten, auch wenn [P,Y]!=0 und ein Seed den aktiven Rang erhöht.

**Skalarer aktiver Kernel.** Falls PKP=k0 P, ist tr(KX)=0 für jedes zulässige B4. Das verlangt keine globale Skalarität von K und keinen verschwindenden X. Es ist eine Bedingung an den Zustand, kein allgemeines Quellgesetz.

**Reduzierender Träger.** Falls zusätzlich [P,Y]=0, wirkt die Analyse ausschließlich von RanP nach RanP⊕RanP. Auf RanP kommutieren C,B und deren positive Gramnormalisierung. Der normalisierte Kanal besitzt zwei Hermitesche Funktionen von Y mit Summe ihrer Quadrate=P. Analyse-Rang m=r, S4=I_m und B4=P. Es gibt kein Seedkomplement; der kombinierte Bestand ist erhalten.

Dies sind Einzelschrittaussagen unter den genannten Voraussetzungen. Eine beliebige vorgegebene Zustandsfamilie wird dadurch nicht automatisch als unter allen zukünftigen Ereignissen invariant ausgewiesen. Bei echter Formationselektion ist der zusätzliche Term -ell_F aus Runde39 wieder mitzunehmen.

## 3. Ausschluss aller festen linearen Umgewichtungen

Schreibe A=tr(PK), M=tr F.

**Exakter Zeuge I (Runde38):** n=3, Y=diag(1/5,2/5,3/5), v=(sqrt(3)/2,1/2,0), P=F=W=vv†, K=-diag(2,3,5). Vollständiges nichtterminales Ereignis mit
Delta A=-9/4, Delta M=9/4.
Universelle Erhaltung von E_{a,b} verlangt daher a=b.

**Exakter Zeuge II (Runde40):** der rationale n=3-Zustand aus ACTIVE_STOCK_DEFECT.md hat
Delta A+Delta M=d,
6599430384017/10^15<d<6599430384019/10^15.
Insbesondere d!=0. Unter a=b ist Delta E_{a,b}=a d, also a=b=0.

Äquivalent: Die Matrix der beiden Bestandsänderungen besitzt Determinante
det([[-9/4,9/4],[u,d-u]])=-9d/4!=0,
unabhängig davon, wie der zweite Defekt in aktive und Formationsanteile zerfällt. Das rationale Zertifikat von d genügt; separate exakte Seed-Eigenwerte sind nicht nötig. Eine frische symbolische Elimination bestätigt diese Determinante und die eindeutige Null-Lösung.

Der Satz schließt auch feste negative Gewichte ein. Ein zustandsunabhängiger additiver konstanter Nullpunkt ändert die Differenzen nicht. Nicht eingeschlossen sind neue dimensions-/rangabhängige Offsets, zustandsabhängige Gewichte, weitere Bestände oder ein physikalisch begründeter eingeschränkter Zustandsbereich. Solche Alternativen wären separat vorab zu definieren und gegen vollständige Ereignisse zu prüfen; dieser Befund liefert sie nicht.

## 4. Vorzeichen und Isotropie am selben Kanal

Behalte P,F,W,Y des rationalen Runde40-Zeugen. U, S4, B4 und X hängen in der Analyse/R4-Stufe nicht von K ab. Die zwei aktiven Diagonaleinträge von X summieren sich exakt zu0; außerhalb P ist X0.

K_1=-diag(1,2,3) gibt d>0.
K_2=-diag(2,1,3) gibt exakt -d.
K_3=-I gibt exakt0, obwohl X!=0.

Alle drei aktiven Kompressionen sind strikt negativ. Das Seedkomplement ist eindimensional, daher sind die Seedentscheidungen in allen drei Fällen eindeutig und nichtterminal. Die positive bzw. negative Gesamtänderung entsteht aus der K-Gewichtung desselben spurfrei umverteilenden Rückzugs. Es ist weder ein universeller Verlust noch eine universelle externe Energiequelle.

## 5. Frische proportionale Quellkontrollen

Vier Originalaufrufe, vorab definierte Eingaben, keine Randomsuche:

| Fall | Delta A | Delta M | Summe |
| --- | ---: | ---: | ---: |
| Rang1-Zeuge | -2.2499999999999982 | 2.249999999999999 | 8.881784197001252e-16 |
| Rang2, K_1 | -1.2503003604325187 | 1.2568997908165365 | 0.006599430384017779 |
| Rang2, K_2 | -1.7496996395674795 | 1.7431002091834626 | -0.006599430384016891 |
| Rang2, K_3 | -0.9999999999999991 | 1 | 8.881784197001252e-16 |

Alle nichtterminal. Der Rang2-Restoperator hat numerisch Eigenwerte ungefähr(-0.0167539804600555,0,+0.0167539804600553), dieselben in allen drei Fällen. Spur-/Stütz-/Positivitäts-/B4<=2P-Kontrollen und Bilanzreste liegen unter1e-12. Die Zahlen sind Rundungskontrollen der oben bewiesenen Aussagen; der Ausschluss fester Gewichte beruht auf den exakten Zeugen.

Vollständiger Prüftext und Ausgabe: [LINEAR_STOCK_CHECKS.md](LINEAR_STOCK_CHECKS.md). Keine Quell-/Audit-/Workflowdatei verändert. Kein neuer Remote-CI-Pass behauptet; letzter geprüfter Code bleibt in CI_VALIDATION.md getrennt. Wiederholung der zwei alten Zeugen ist hier durch die neue gemeinsame Gewichtsklassifikation begründet.

## 6. Nächste Abhängigkeit und physikalische Grenze

Die Suche nach einem vollständigen Energiebegriff kann nicht auf einer festen linearen Mischung nur dieser beiden Bestände beruhen, wenn sie alle hier zulässigen Seed-/Rangereignisse abdecken soll. Erhaltene Spezialfälle liefern Kontrollsektoren, aber noch keine allgemeine physikalische Identifikation.

Als nächste BFG-interne Frage bleibt, ob ein von der Quelle ausgewählter zusätzlicher beobachtbarer Bestand oder eine geschlossene, unabhängig begründete Einschränkung der Zustandsklasse den Rest mitführt. Ein allein rückblickend integriertes Gegenkonto ist keine solche Herleitung. Für Impuls fehlen weiterhin Raum-/Uhrabbildung, Symmetrie-/Generatoridentifikation und kalibrierte Messung; die lineare Bestandsklassifikation schließt diese physikalischen Lücken nicht.
