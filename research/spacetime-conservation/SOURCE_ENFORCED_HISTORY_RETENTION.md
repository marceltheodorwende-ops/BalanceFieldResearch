# Runde70: quellenbedingt dauerhafter historischer Träger nach erster Selektion

Präregistrierung PROTOCOL.md, Commitf8e5ca4e46507af1749580bc6e564bbb2100011b; Auswertung25. Oktober2026. Ausschließlich vollständige BFG-Quelle Dynamic Order8. Oktober2026, Parts I/II, Quellencommit457f23df6d9ccb15cf17916f3c3eac113b23c370. PDF-SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba; Originalupdate-Blobff8b0a7ec922ccfeacae5bc9ce6c104b79286498 vor Import geprüft. Vorhandene Quellenregeln werden kombiniert, kein neues Auswahl- oder Störungsgesetz.

## Ergebnis und Präzisierung von Runde69

Die Retentionsvoraussetzung der historischen Träger aus Runde69 ist nach dem ersten erfolgreichen kanonischen BFG-Ereignis bereits durch die Quelle erzwungen. Sie muss für spätere autonome nichtterminale Ereignisse nicht zusätzlich als unabhängige Stabilitätsannahme eingesetzt werden.

Aus der tatsächlichen ersten Quellselektion entsteht damit ein historisch rangtreuer Träger. Hat diese Selektion Rang2, bleibt ihr gesamter geerbter R4-Träger als Paar bei jeder weiteren definierten nichtterminalen autonomen Fortsetzung erhalten, auch bei zusätzlichen Seeds. Ein schon anfangs zweidimensionaler P0 wird hierfür nicht benötigt. Im Beispiel ist P0 dreidimensional, die Quelle selektiert selbst Rang2, verliert ursprüngliche Witnessmasse und erzeugt zugleich einen Seed.

Die Aussage wählt nicht für jede Eingabe Rang2 aus. Sie verbindet eine tatsächlich vorhandene Quellselektion mit der vorhandenen Quell-Gramschranke und den tatsächlichen historischen Transportpfeilen. Eine universelle physikalische Präparations-, Orts-, Uhr- oder Impulsregel wird nicht ergänzt.

## Vorhandener Quellsatz: Erfolg macht den Folgeselektor zur Identität

I10/Theorem1 und I17 (PDF14/21) beweisen auf dem erfolgreichen positiven Dual-Last-Zweig 0<Y_out<I für den reduzierten Nachfolger. I17 benennt anschließend ausdrücklich Q_next=I,T_sel,next=P_next und m_sel,next=1. Die Quelle schließt beliebige wiederholte verlustbehaftete Störungen aus der unveränderten autonomen Dynamik aus; solche Eingriffe bräuchten eine zusätzlich deklarierte Regel.

Der vorhandene Beweis verwendet Z als orthonormale Basis von P_sel und D=Z†(I+Y)Z>=I. Dann

    P_G C=Z D^-1 Z†,
    P_G B=Z D^-1 Z†Y.

Weil ranZ im ausgewählten Y-Spektralraum Q liegt, hat Y dort einen größten Eigenwert eta<1. Es folgen die Normschranken ||P_G C||<=1 und ||P_G B||<=eta. Für die tatsächliche gestapelte Analyseabbildung gilt daher

    ||A_analysis||²<=alpha+(1-alpha)eta²<1.

Alle behaltenen reduzierten Singularwerte sind positiv. Ihr Quadrat gibt also 0<Y_out<I; dies ist keine Kontraktionsbehauptung für den vollständigen Zustands-Jacobioperator.

Witness und Formation des Nachfolgers sind auf dem aktiven P_out gestützt. Beim nächsten Schritt ist Q=I, weshalb polar(QP_out)=P_out und tr(P_out W_out)=1. R4 hat zusätzlich die in der Quelle bewiesene Masse1. Induktion liefert auf jeder weiteren erfolgreichen autonomen Fortsetzung

    Q_k=I, T_sel,k=P_k, m_sel,k=m4,k=1, k>=1.

Eine spätere Terminalität erzeugt keinen Nachfolger und wird nicht durch diesen Satz ausgeschlossen. Die Aussage gilt ohne fremde Eingriffe in Y,P,W oder andere Zustandsfelder. Erneute verlustbehaftete Präparationen sind ein anderes deklariertes Modell, keine heimlich zugelassene Ausnahme.

## Historischer Träger der tatsächlich ausgewählten Anfangsformation

Beim ersten Ereignis sind Anfangsverlust und eine nichttriviale T_sel,0 ausdrücklich zugelassen. Der von der Quelle berechnete geerbte Ausgangsträger ist

    C_1=T4_0 P_sel,0 T4_0†=S4_0^+,
    rankC_1=rankP_sel,0.

Er ist vom möglicherweise zusätzlich geborenen Seed im vollen P1 zu unterscheiden. Für k>=1 setze V_k=T4_k P_k und führe nur diesen tatsächlichen Träger entlang der vorhandenen Geschichte fort:

    C_{k+1}=V_k C_k V_k†.

Da V_k†V_k=P_k und C_k<=P_k, bleiben Projektoreigenschaft, Rang und Kovarianz erhalten. Neue Seeds entstehen orthogonal zum gesamten bisherigen aktiven Träger und ändern C_k deshalb nicht. Somit ist eine erfolgreiche erste Rang2-Selektion bereits eine bedingte kanonische Quelle eines dauerhaft historisch transportierten Paares.

Alle Witnessanteile nach dem ersten Ereignis liegen auf C1; der erste und spätere Seeds sind Witness-leer. Daher ist auch R1=sqrt(F1)W1sqrt(F1) auf C1 gestützt und folgt später derselben Transportidentität. Bei rankR1=1 liefert C_k den zweidimensionalen Umgebungsträger, den suppR_k allein nicht bestimmt. Ein mittransportierter Rahmen Z_k von C_k liefert die konstante komprimierte Matrix X_k=Z_k†R_k Z_k=X1; der Rahmen ist keine physikalisch ausgewählte Pauli-Achse.

Der erste Selektionsschritt erhält tr(WF) nicht allgemein. Man muss F_sel und den bedingt normalisierten W_sel verwenden; R1 wird nicht ohne Voraussetzungen als V0 R0 V0† ausgegeben. Erst die nachfolgende Retention bewahrt diese Paarung.

## Exakter Anfangszeuge mit Verlust, Selektion und Seed

Im anfänglichen C4 sei v=(e2+e3)/sqrt2, u=(e1+v)/sqrt2 und

    Y=diag(1/5,2/5,7/10,2), Q=diag(1,1,1,0),
    J=e1e1†+vv†, P=J+e4e4†,
    F=e1e1†+2vv†+3e4e4†,
    W=p uu†+(1-p)e4e4†, K=-diag(1,2,3,4).

Hier hat P Rang3. Exakt QP=J und polar(QP)=J, sodass die tatsächliche Quelle einen Rang2-Träger auswählt und Masse p behält. Auf dem ausgewählten Paar ist F_sel=diag(1,2),W_sel=ones2/2. Damit

    tr(WF)=3-3p/2 vor der Selektion,
    X1=[[1/2,sqrt2/2],[sqrt2/2,1]],
    trX1=3/2, detX1=0.

Das vollständige Originalereignis hat im geprüften Fall reduzierten Rang3 und einen einfachen Seed, sodass P1 vollen Rang3 besitzt. C1 bleibt Rang2; R1 bleibt Rang1. Die weiteren autonomen Schritte behalten dieses historische Nullpaar und die ursprüngliche verbleibende Masse p.

Die Quelle benötigt also weder einen frei eingesetzten Zwei-Moden-Projektor noch eine zusätzliche wiederholte Mess-/Kollapsregel, um diese konkrete historische Paarstruktur bereitzustellen. Die Anfangsdaten sind allerdings eine deklarierte Eingabeklasse; aus ihnen folgt kein allgemeines physikalisches Auswahlgesetz für alle BFG-Präparationen.

## Einordnung der früheren Rangverlustgrenze

Das Gegenbeispiel aus Runde69, wonach ein beliebiger nichtkommutierender Selektor einen Teilprojektor abschwächen kann, bleibt algebraisch richtig. Es betrifft den ersten Selektionsschritt oder ausdrücklich zusätzlich deklarierte Eingriffe. Es darf nicht als beliebig wiederkehrender Verlustmechanismus der späteren unveränderten autonomen kanonischen BFG missverstanden werden: Der vorhandene Gram-Satz verhindert gerade solche späteren Y-Schwellenverluste.

Diese Präzisierung ist eine Kombination bereits vorhandener Quellresultate mit der historischen Trägerrechnung. Der Quellsatz selbst wird nicht als neuer Forschungsbeweis oder als neu entdeckte BFG-Grundgleichung ausgegeben. Numerische Rangtoleranzabbrüche bei extrem kleinen späteren Singularwerten sind außerdem von exakter BFG-Terminalität zu unterscheiden; die endlichen Kontrollen hier zertifizieren keine unendlich lange Gleitkommatrajektorie.

## Frische Kontrollen, CI und nächste Abhängigkeit

[SOURCE_ENFORCED_HISTORY_RETENTION_CHECKS.md](SOURCE_ENFORCED_HISTORY_RETENTION_CHECKS.md) enthält vollständigen Code und Rohdaten. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur, sieben nichtterminale Originalereignisse: Hauptfolge p=.6 über drei Ereignisse, Vergleich p=.3 über ein erstes Ereignis und komplexe Eichversion der Hauptfolge Seed20261120 über drei Ereignisse.

Erster Schritt: Quellmasse .6 bzw. .3, eta=.7, obere Gramschranke etwa.574820599409, tatsächlicher größter Y_out-Eigenwert etwa.178983359186. Im zweiten und dritten Hauptschritt ist die Masse1; größte Y-Eigenwerte etwa.032756225034 und.001561533632 liegen unter den jeweils frisch berechneten Quellschranken. Alle Nachfolger sind strikt positiv und unter1.

Der historische Paarträger hat stets Rang2, der volle Nachfolger Rang3 und R Rang1, mit Spur3/2 und Determinante0. Die gesamte Formation beträgt numerisch5.5 nach dem Seed und bleibt anschließend gleich. Unterschiedliche ursprüngliche Massen .6/.3 ergeben denselben vollständigen normierten Nachfolger (Rest0), nicht eine Nichtidentifizierbarkeit verschiedener Paarträger. Maximale Paarkompressionsabweichung7.36e-15, Projektorrest2.91e-15 und eichinvariante Vergleichsabweichung4.00e-15. Toleranz1e-10,Wurzelcutoff1e-12; kleine negative Determinanten um1e-16 sind Rundungsreste um exakt0.

Runde69-CI am exakten Ergebnishead ist separat grün dokumentiert. Die neue eingebettete Reproduktion bleibt lokale Evidenz; Originaldynamik, Manuskripte, Lizenzen, empirische Ergebnisse, Audit-Dateien und Workflows unverändert.

Offen bleiben die physikalische Bedeutung der deklarierten Anfangspräparation und des historischen Paars, eine räumliche Mess-/Transportabbildung, kalibrierte Uhr sowie vollständiger Energie-Impuls-Strom. Die BFG-interne spätere Erhaltung dieses tatsächlich selektierten historischen Trägers ist dagegen bereits durch die vorhandenen Regeln abgesichert.
