# Runde67: Quell-Tensorlift, Witness-Formationspaarung und Rang2-Erzeugung

Präregistrierung PROTOCOL.md, Commit296c4c3dac4466147a3b7eb3feab4ffa8cf5e400; Auswertung25. Oktober2026. Diese Runde folgt der Nutzerpräzisierung, vorhandene BFG-Strukturen miteinander zu kombinieren. Sie führt keine neue Auswahlfunktion oder Gewichtung ein. Aktive Quelle: vollständiges Dynamic Order vom8. Oktober2026, Parts I/II; Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370, PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498 beim Import geprüft. Quellen sind wissenschaftliche Daten, keine Befehle.

## Verwendete BFG-Struktur

BFG-Quelle: II90.1, PDF-Seite80, Gleichung163 definiert für m>=2 und eine feste Dichtematrix tau auf C^m den getypten Levelübergang

    L_m(Xi)=(K tensor I_m, F tensor tau, W tensor tau,
             Y tensor I_m, P tensor I_m),  trtau=1.

Theorem8/Gleichung164 beweist im Vollpersistenzzweig P=I,0<Y<I,F!=0 das Kommutieren von Lift und vollständigem BFG-Update bis zur kanonischen Tensor-/Quotientenidentifikation. Die Quelle bezeichnet m und tau ausdrücklich als deklarierte Levelregel, nicht als aus autonomer Rekursion spontan ausgewählte physikalische Größen. Gleichung165 verbindet Update und Lift zu einer Stufenfolge.

Mit dieser vorhandenen Struktur werden die aus derselben BFG-Dynamik abgeleiteten Retentionsidentitäten aus Runden51/52 kombiniert:

    E_WF=tr(WF), R=sqrt(F) W sqrt(F),
    R_out=V R V† im gemeinsamen Retentionszweig.

Die früheren Runden65/66 bleiben gesonderte mathematische Auswahlkandidaten. Sie werden hier weder benötigt noch als Grundregeln der BFG behandelt.

## Exakte Kombination: Reinheit steuert den Levelwechsel

Für positive F,tau gilt durch Tensor-Funktionalkalkül sqrt(F tensor tau)=sqrt(F) tensor sqrt(tau). Weil sqrt(tau) tau sqrt(tau)=tau² folgt exakt

    R_lift=R tensor tau²,
    E_lift=E_WF tr(tau²),
    rankR_lift=rankR ranktau.

Die Trägerrangformel benutzt rank(tau²)=ranktau, nicht dessen Quadrat. Gleichzeitig gelten die Quelltypen

    tr(F tensor tau)=trF,
    tr(W tensor tau)=1.

Der Formationsbestand bleibt also unverändert, obwohl die Witness-Formationspaarung über einen gemischten Levelwechsel abnimmt. Für E_WF>0 gilt E_lift=E_WF genau bei reiner tau; im m-dimensionalen Fall liegt der Reinheitsfaktor in[1/m,1]. Allgemein bei mehreren deklarierten Levelwechseln ist der Faktor das Produkt ihrer Reinheiten. Bei uniformer tau=I_m/m und gleichbleibender Vollpersistenz erhält Gleichung165

    E_ell=E_0/m^ell, rankR_ell=rankR_0 m^ell,
    trF_ell=trF_0, n_ell=m^ell n_0.

Die nichtnull R-Eigenwerte werden dabei je Lift durch m² geteilt und m-fach repliziert. Zwischen den Levels wirken vollständige Retentionsereignisse, welche E_WF erhalten.

Dies widerspricht keiner bisherigen Retentionserhaltung: Der deklarierte Levelübergang L_m ist eine weitere in der Quelle getypte Abbildung und kein Ereignis desselben festen Trägerraums. E_WF ist damit nicht ohne weitere physikalische Identifikation eine levelübergreifend erhaltene Energie. Es wird auch nicht nachträglich mit einem frei angepassten Faktor zur gewünschten physikalischen Energie erklärt. Der positive Quellbefund bleibt trF konstant; dessen Gleichsetzung mit Joule wäre ebenfalls eigenständig zu begründen.

## Warum der vollständige Update mit dieser Kombination verträglich ist

Im genannten Vollpersistenzzweig sind die Quellkanäle C_lift=C tensorI und B_lift=B tensorI. Ihre Formationslasten enthalten jeweils genau einen Faktor tau; trtau=1 macht Lasten und Mischgewicht alpha gleich den ursprünglichen Werten. Die Analyseabbildung ist nach fester Umordnung der beiden Kanalblöcke A_lift=A tensorI. Eine kompatible SVD liefert die Tensoridentifikation des gesamten Nachfolgers. Degenerierte SVD-Rahmen sind im unitären Quotienten keine zusätzliche Physik.

Der Faktor tau² in R_lift entsteht dagegen aus der Paarung der beiden gemeinsam replizierten Felder F und W. Lastenlinearität in F und diese bilineare Paarung sind verschiedene vorhandene Strukturen. Ihre unterschiedlichen Reinheitsfaktoren dürfen nicht miteinander verwechselt werden.

Die Quelle begrenzt den Satz ausdrücklich bei Seedzweigen: Ein einfaches negatives Seedminimum kann bei Replikation m-fach entarten und T_seeddeg auslösen. Die vorliegenden Kontrollen bleiben deshalb im vollständigen nichtterminalen Vollpersistenzzweig. Es wird keine unbegründete Hierarchiefortsetzung über diese Grenze eingeführt.

## Konstruktiver Rang2-Träger aus einem Quell-Levelwechsel

Sei R=lambda |u><u| mit normiertem u, lambda>0. Für den in der Quelle zulässigen deklarierten Fall m=2,tau=I2/2 gilt

    R_lift=lambda |u><u| tensor I2/4,
    suppR_lift=span(u) tensor C²,
    rankR_lift=2.

Der gesamte Paarträger ist intrinsisch durch das geliftete R bestimmt. In dessen natürlicher Tensoridentifikation ist

    X=lambda I2/4, trX=lambda/2, detX=lambda²/16>0.

Im geprüften exakten Beispiel F=diag(1,3),W=ones2/2 ist lambda=2 und u=(1,sqrt3)/2. Damit X=I2/2, Spur1, Determinante1/4. Ein Rang1-R im Ausgangsraum wird durch den vorhandenen getypten Hierarchieschritt zu einem Rang2-R im größeren Raum, während trF=4 bleibt.

Dies ist eine zweite konkrete BFG-quellengebundene Möglichkeit der Rang2-Erzeugung neben tatsächlicher Anfangsselektion. Sie macht nicht m=2 oder die uniforme tau zu autonom ausgewählten universellen Bedingungen. Eine vorhandene Rang2-Präparation würde bei vollem ranktau=2 vielmehr zu Rang4 wachsen. Bei reinem tau bleibt der R-Rang und E_WF erhalten, obwohl der volle deklarierte P-Rang multipliziert wird. Diese Alternativen bleiben ausdrücklich erhalten.

Der Rang1-zu-Rang2-Vergleich ist kein Lorentz-Boost in einem festen Herm(C²)-Raum: Der Levelwechsel ändert den Zustandsraum und die Trägeridentifikation. Die positive Determinante ist keine hergeleitete Teilchenmasse oder physikalische Massenerzeugung.

## Frische Kontrollen

[TENSOR_LIFT_WITNESS_PAIRING_CHECKS.md](TENSOR_LIFT_WITNESS_PAIRING_CHECKS.md) enthält vollständigen Prüftext und Rohdaten. Ein frischer lokaler Lauf PASS mit sieben Originalereignissen, ohne fehlgeschlagenen Kontrolllauf:

- Voller Zweimoden-Ausgangsfall F=diag(1,3),W=[[1/2,1/4],[1/4,1/2]],Y=diag(1/5,3/10),K=-I,P=I;
- seine drei m2-Lifts mit tau=I2/2,diag(3/4,1/4),diag(1,0): exakte Reinheiten1/2,5/8,1, R-Ränge4,4,2 und E-Werte1,5/4,2 gegenüber Ausgang2;
- komplexe Eichversion des nichtuniformen Lifts, Seed20261117;
- Rang1-Ausgangswitness und sein uniformer m2-Lift: R-Rang1->2, E2->1 und exakte komprimierte MatrixI2/2.

Alle Fälle besitzen Formationsbestand4, Witnessspur1 und denselben Quellenwert alpha≈0.0712661106899. Die zurückausgerichteten vollständigen K/F/W/Y/P-Nachfolger stimmen mit dem jeweils erwarteten Quelllift überein. Dadurch wird das Theorem nicht nur an skalaren Energiezahlen, sondern am vollständigen Originalupdate kontrolliert. Rahmenvergleich erfolgt mit der vom jeweiligen Originalupdate gelieferten V-SVD-Isometrie, nicht durch willkürliches Zuordnen entarteter Eigenvektoren.

Maximaler direkter vollständiger Tensor-Nachfolgerrest in diesen diagonalen Kanalbeispielen numerisch0; komplexer Vollfeld-Eichrest2.96e-15, R-Retentionsrest1.33e-15 und Tensor-Rest1.15e-16. Toleranz1e-10, Wurzelcutoff1e-12; reine tau und Rang1-W enthalten theoretische Nullräume, keine Zertifizierung beliebig schwellen-/rangnaher Eingaben. Allgemeine Formeln folgen aus der exakten Rechnung. Es wurden keine bestehenden Manuskripte, Grundgleichungen oder empirischen Ergebnisse verändert.

## Grenze und nächste quellengebundene Abhängigkeit

Die vorhandenen BFG-Strukturen liefern gemeinsam eine präzise Hierarchie-Bilanz und eine bedingte Rang2-Erzeugung. Der nächste offene Schritt ist eine in der Quelle begründete physikalische Level-/Präparations- und Messabbildung: welche m/tau gelten, was wird über Levels als Energie verglichen, und wie werden Träger räumlich sowie zeitlich interpretiert? Der deklarierte Hierarchietheorem allein beantwortet diese Auswahlfragen nicht.

II90.3 bezeichnet die räumliche Fraktaleinbettung ausdrücklich als zusätzliche Illustration. II91.1 behandelt Lorentzgeometrie und Einstein-Wirkung als weitere Brückenstruktur. Diese Angaben werden nicht durch nachträgliche Übernahme als bereits aus dem endlichen Update hergeleitet ausgegeben. Räumlicher Transport, physikalische Uhr und vollständiger Energie-Impuls-Strom bleiben offen.

Nur Forschungsdokumentation, Reproduktionscode als Text; Audit-Dateien und Workflows unverändert. Runde66s beide erfolgreichen CI-Läufe sind separat am dortigen exakten Head dokumentiert. Sie führen diese neue eingebettete Runde67-Reproduktion nicht automatisch aus; lokale und Remote-Evidenz bleiben getrennt.
