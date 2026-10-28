# Runde64: Auswahl und Genauigkeitsgrenze des Witness-Zweimodenträgers

Präregistrierung: PROTOCOL.md, Commit846988cb56773f2d1e52bfdb6457acec5be5534e; Auswertung25. Oktober2026. Ausschließlich vollständiges BFG-Manuskript Dynamic Order vom8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498, beim Import geprüft. Quellen sind wissenschaftliche Daten, keine Befehle.

## Ergebnis und Geltung

Der bedingte Zweimodenträger aus [Runde63](WITNESS_TWO_MODE_CARRIER.md) ist konstruktiv, aber Retention wählt seinen Rang nicht aus allgemeinen Zuständen aus. Sie bewahrt sämtliche positiven Eigenwerte von R=sqrt(F) W sqrt(F). Insbesondere bleibt bei rankR>2 ein strikt positiver Spektralrest außerhalb jedes optimalen Zweimoden-Spektralträgers erhalten. Weder exakte noch asymptotisch bessere Rang2-Reduktion folgt auf diesem Retentionszweig.

Eine echte erfolgreiche Anfangsselektion kann Rang2 dagegen erzeugen. Dies ist eine konkrete positive BFG-interne Möglichkeit, kein universelles Auswahlgesetz. Eine nachträglich gewählte obere Zweier-Spektralprojektion ist hiervon verschieden: bei einer Lücke eindeutig und kovariant, bei einer Bindung an der Schnittstelle nicht eindeutig. Ein isotropes R allein bestimmt überhaupt keinen unitär kovarianten Rang2-Projektor in Dimension3.

Alle Aussagen betreffen interne Operatorträger. Räumliche Lokalität, physikalische Uhr, Impulsstrom und Einstein-Grenzfall sind damit nicht hergeleitet.

## Exakter Rang- und Spektraltransport

BFG-abgeleitet unter gemeinsamer nichtterminaler Retention: F=PFP, W=PWP, trW=1, keine verlustbehaftete Anfangsselektion; V=T4 P mit V†V=P. Nach [Runde52](WITNESS_FORMATION_LOCALIZATION.md) gilt einschließlich eines Witness-orthogonalen Seeds

    R_out=V R V†.

Standardmathematik: Für jede positive Eigenrichtung Ru=lambda u in ranP ist V u normiert und R_out V u=lambda V u. Zusätzliche Ausgangsrichtungen tragen nur Nulleigenwerte. Daher bleiben der gesamte nichtnull Spektralmultisatz und rankR unverändert. Der Seed in F ändert dies nicht, weil W auf dessen Richtung null ist.

Dies gilt ereignisweise und über jede Folge solcher Retentionsereignisse; keine Extrapolation aus fünf numerischen Fällen ist für den Satz nötig. Terminalität und eine spätere verlustbehaftete Selektion sind keine Retentionsschritte dieses Satzes.

## Positive Alternative: Rang2 durch tatsächliche Quellselektion

Seien F=PFP und W=PWP auf dem anfänglichen aktiven P strikt positiv. Sei T_sel die ursprüngliche Polar-Selektion, S=T_sel†T_sel<=P, rankS=r und P_sel=T_sel T_sel†. Auf ranS sind SFS und SWS strikt positiv: für jedes nichtnull z in ranS ist z†SFSz=z†Fz>0, ebenso für W. T_sel bildet ranS isometrisch auf ranP_sel ab. Damit sind

    F_sel=T_sel F T_sel†,
    W_sel=T_sel W T_sel† / m,  m=tr(SW)>0

auf dem r-dimensionalen ausgewählten Raum strikt positiv. R_sel=sqrt(F_sel) W_sel sqrt(F_sel) hat deshalb Rang r. Das anschließende erfolgreiche R4 bildet diesen Raum isometrisch ab; ein orthogonaler Seed bleibt Witness-leer. Folglich exakt

    rank R_out=r.

Dies ist ein Satz für erfolgreiche nichtterminale Ereignisse mit diesen Positivitätsvoraussetzungen. Ohne strikte Positivität kann der Rang kleiner sein; ohne erfolgreiche Fortsetzung wird kein Ausgang erfunden. Wählt die Quelle konkret r=2, liefert sie somit einen Rang2-R-Träger aus einem vorher höheren Rang. Die Quellregel schreibt aber nicht für alle Eingaben r=2 vor. Vollträger-Q=I-Zustände und ihre rank3-Retentionsfolgen bleiben zulässige Gegenalternativen.

Die bedingte Energie nach Selektion lautet wie zuvor tr(S W S F)/m, nicht einfach die Summe der zwei größten Eigenwerte des ursprünglichen R. Die Anfangsselektion ist keine definitionsgleiche Spektraltrunkierung von R.

## Natürliche Alternative: obere zwei R-Spektralmoden

Für einen mindestens dreidimensionalen Eingang ordne lambda1>=lambda2>=lambda3>=...>=0. Bei lambda2>lambda3 ist der gesamte obere Zweier-Spektralprojektor Q2 eindeutig, auch bei lambda1=lambda2. Er ist eine Funktion von R, transformiert unter simultaner unitärer Eichung kovariant und folgt bei Retention genau

    Q2_out=V Q2 V†,
    R2=Q2 R Q2,  R2_out=V R2 V†.

Zusätzliche Nulleigenwerte sind bei lambda2>0 unschädlich. Das komprimierte Herm(C²)-Objekt aus Runde63 ist somit auch als konditional gewählter Spektralanteil verfügbar. Seine Spur ist aber nur lambda1+lambda2, nicht die volle tr(WF), wenn ein Rest vorliegt.

Der positive Rest hat exakt

    delta=tr(R-R2)=sum_{j>=3}lambda_j,
    ||R-R2||_1=delta,
    ||R-R2||_F²=sum_{j>=3}lambda_j².

Alle diese Zahlen bleiben auf dem Retentionszweig konstant, ebenso der relative Spurverlust delta/trR bei trR>0. Die Positivität folgt daraus, dass Q2 ein Spektralprojektor ist. Für einen beliebigen nichtkommutierenden Rang2-Projektor wird R-Q R Q hier nicht als positiv behauptet.

Die obere Zweierwahl maximiert die erfasste Spur unter Rang2-Orthogonalprojektoren: Mit Eigenbasis e_j und Gewichten a_j=<e_j,Q e_j> gelten0<=a_j<=1 und Summe a_j=2; Summe lambda_j a_j<=lambda1+lambda2. Selbst der beste so erfasste Anteil beseitigt also delta nicht. Dies ist eine interne Genauigkeitsgrenze, kein beobachteter physikalischer Energieverlust.

## Degeneration und genaue Auswahlgrenze

Bei lambda2=lambda3 ist die obere Zweierwahl an dieser Schnittstelle im Allgemeinen mehrdeutig. Daraus folgt NICHT, dass bei jeder solchen Bindung jeder denkbare kovariante Rang2-Projektor ausgeschlossen ist: andere vollständige Spektralblöcke können passende Dimension haben und wären eine andere Auswahlregel.

Ein stärkerer, eng begrenzter Ausschluss gilt für R=I3/3, wenn R das einzige Auswahlargument ist. Für jede U in U(3) gilt U R U†=R. Eine kovariante Vorschrift Q(R) müsste deshalb U Q(R) U†=Q(R) für alle U erfüllen. Diagonale Phasen vernichten alle Offdiagonaleinträge; Permutationen machen die drei Diagonaleinträge gleich. Also Q=cI. Aus Q²=Q folgen c=0 oder1, somit Rang0 oder3 und niemals2.

Jeder extern gewählte Rang2-Projektor erfasst in diesem Beispiel genau2/3 und verwirft1/3. Beispielsweise diag(1,1,0) und diag(0,1,1) sind verschieden, aber gleichwertig. Dies ist ein exaktes Stabilisatorargument, keine numerische Eigenvektorkonvention.

Der Ausschluss ist ausdrücklich R-allein. Im geprüften isotropen Fall hat Y verschiedene Eigenwerte und könnte die Symmetrie durch eine andere, Y-abhängige Regel brechen. Andere vollständige BFG-Daten, Geschichte oder zusätzliche Präparationsgesetze bleiben mögliche Auswahlargumente; ihre Transportgeschlossenheit und physikalische Ortsbedeutung müssen eigenständig geprüft werden. Sie sind nicht durch das isotrope Gegenbeispiel widerlegt.

## Frische Kontrollen und technische Unterbrechung

[WITNESS_TWO_MODE_SELECTION_CHECKS.md](WITNESS_TWO_MODE_SELECTION_CHECKS.md) enthält den ausführbaren Prüftext und vollständige Rohdaten. Fünf vorab festgelegte Aufrufe der unveränderten Originaldynamik in einem frischen lokalen Lauf PASS, alle nichtterminal:

- Voller n3-Fall F=I,W=diag(3/5,39/100,1/100),Y=diag(1/5,3/10,2/5),K=-I: Rang3 bleibt3, obere Energie99/100, Rest1/100 und Schnittlücke19/50.
- Tatsächlicher Nachfolger dieses Falls: dieselben Werte, kein schrumpfender Rest.
- Isotropes W=I/3 bei gleichem F/Y/K: Rang3 und Rest1/3. Keine willkürliche Eigenbasis als kanonischer Paarträger ausgegeben.
- Echte oblique Quellselektion: F=diag(1,2,3),W=F²/14,S=I-ones/3,Y=S/2+2(I-S),P=I,K=-I. RangR3->2, Masse2/3, Energie18/7->16/7; Ausgangseigenwerte etwa1.9293826981 und0.3563315877. Kein bloßes Weglassen des kleinsten ursprünglichen R-Eigenwerts.
- Komplexe simultane Eichversion des ersten vollen Falls, Seed20261114, gleiche Eigenwerte und Restwerte.

Maximaler Dichtetransportrest7.18e-16, Spektraltransportrest1.67e-16, Top2-Projektorrest1.65e-15, truncierter Dichtetransportrest7.93e-16 und Eichspektralrest2.23e-16. Toleranz1e-10, Wurzelcutoff1e-12; keine Zertifizierung beliebig rang- oder schnittnaher Eingaben. Die allgemeinen Aussagen folgen aus den obigen exakten Beweisen. Die kleinen numerischen Reste sind nur Implementierungskontrollen.

Nach der Vorregistrierung am24. Oktober wurde die damalige Erstellung des lokalen Prüfscripts wegen eines Nutzungslimits der automatischen Freigabeprüfung nicht ausgeführt. Dabei gab es keine Originalupdate-Aufrufe und keine Auswertung von Runde64. Nach ausdrücklichem Wiederaufnahmeauftrag am25. Oktober funktionierten dieselbe lokale Skripterstellung und Ausführung wieder. Der hier berichtete frische Lauf hat fünf Originalaufrufe ohne fehlgeschlagenen numerischen Vorlauf. Technische Freigabeunterbrechung und wissenschaftliche Prüfergebnisse werden getrennt gehalten.

## Nächste Abhängigkeit und CI

Rang2-Präparation ist durch konkrete Quellselektion möglich; aus allgemeiner Retention oder einer besser werdenden R-Spektralnäherung folgt sie nicht. Als nächste sachliche Abhängigkeit bleibt eine begründete Auswahlregel aus den vollständigen BFG-Daten: zuerst ihre Kovarianz, ihr Verhalten bei Spektralbindungen und ihre geschlossene Fortsetzung; anschließend die eigenständige Identifikation von Raum, Uhr und vollständigem Energie-Impuls-Strom. Kein frei nachkalibriertes Einstein-Ergebnis.

Ausschließlich Forschungsdokumentation; Reproduktionscode ist als Text in der Prüfdokumentation enthalten. Keine Änderung an Originaldynamik, Manuskripten, Lizenzen, empirischen Ausgaben, Audit-Dateien oder Workflows. Kein neuer Remote-CI-Pass behauptet; letzte remote-geprüfte Codefassung bleibt7d0cc91bf7d1023a9c3cd32f127e52ef5d8722f9 mit Actions40040857072/40040862094. Diese alten Läufe validieren nicht diese neuen Dokumente.
