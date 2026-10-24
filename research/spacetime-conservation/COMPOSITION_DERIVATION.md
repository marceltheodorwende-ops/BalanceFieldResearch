# Exakte mehrfache Kanal-Komposition im erhaltenen Spektralrahmen

## Bereich und Herleitung
Ausschließlich die gepinnte BFG-Quelle, Vollpersistenz F>0, 0<Y<I und eine Folge im aufgelösten Bereich C. Die bisher bewiesene Form Y_k=phi_k(Y_0) erhält eine gemeinsame Eigenbasis U. Die tatsächlichen alpha_k werden aus der unveränderten Geometriefolge gewonnen; sie hängen nicht von K ab. Für diese Folge gilt

    (U† K_N U)_ab = H^(N)_ab (U† K_0 U)_ab,
    H^(N)_ab = Produkt_(k=0,...,N-1) h_ab(k),
    h_ab(k) = [alpha_k+beta_k y_a(k)y_b(k)]
              /sqrt[(alpha_k+beta_k y_a(k)^2)(alpha_k+beta_k y_b(k)^2)].

Jeder Faktor ist das Skalarprodukt zweier reeller normierter Zweikomponentenvektoren
v_a(k)=(sqrt(alpha_k),sqrt(beta_k)y_a(k))/sqrt(alpha_k+beta_k y_a(k)^2).
Damit ist H^(N) die Gram-Matrix der Tensorprodukte v_a(0) tensor ... tensor v_a(N-1). Sie ist positiv semidefinit mit Diagonale eins. Der zusammengesetzte Kanal ist vollständig positiv, unital, spurtreu und Hilbert-Schmidt-selbstadjungiert. Seine festen spektralen Diagonalkomponenten bleiben erhalten. Dies ist ein mathematischer Kernelkanal, keine physikalische Viererstromherleitung.

Unabhängige Darstellung: Für jedes binäre Wort s der Länge N setze L_s=T_(s_N-1,N-1)...T_(s_0,0). Die T sind hermitesche kommutierende Funktionen desselben Y_0; deshalb auch die L. Dann Psi_N(K)=sum_s L_s K L_s und sum_s L_s²=I. Die **festen linearen Kanalabbildungen** kommutieren. Das erlaubt keine Umordnung der vollständigen nichtlinearen BFG-Ereignisse oder ihrer endogenen alpha-Berechnung.

## Ganze effektive Populationsmatrix
In der erhaltenen Formationseigenbasis und für anfangs diagonales K_0=diag(q_0) gilt exakt q_N=P^(N)q_0 mit

    P^(N)_ij = sum_s |(L_s)_ij|²
             = sum_ab U_ia conj(U_ja) H^(N)_ab conj(U_ib) U_jb.

P^(N) ist nichtnegativ, symmetrisch und doppelt-stochastisch. Sie wird aus der ungekürzten Kanal-Komposition berechnet. Im Allgemeinen ist sie verschieden von P_(N-1)...P_0, denn dieses Produkt löscht nach jedem Ereignis die Formation-Kohärenzen. Für allgemeines anfangs nichtdiagonales K trägt zusätzlich dessen Kohärenz zur Endpopulation bei. Die effektive Matrix für diagonale Anfangszustände schafft daher keine autonome Populationsdynamik.

Der anfängliche Pfad kann als deklarierter Referenzgraph dienen. Weder die feste Spektralbasis noch diese Endpunktmatrix liefert allein eine physikalische Entfernung, Uhr oder ein universelles Ausbreitungstempo. Die einereignisweisen Bandabschätzungen in der jeweils aktuellen Y-Nachbarschaft sind nicht ungeprüft mehrschrittige Abschätzungen im anfänglichen Pfad. Ein solcher kontrollierter Satz bleibt offen.

## Frische Evidenz
[Vorabprotokoll](COMPOSITION_PROTOCOL.md), [Prüfcode](composition_audit.py), [Resultate](composition_results.json).

n=3,4,5,6, je drei Ereignisse mit Punktmassen- und komplexem positivem Kernel, plus vier unitäre Kontrollen: 28 vollständige Quellaufrufe. Die ganze effektive Matrix wurde unabhängig durch alle bis zu acht Kraus-Wörter gegen die spektrale Produktform geprüft. Quelle und beide Darstellungen stimmen an den deklarierten Kerneln überein.

Maximaler Quellrest 6.82e-15; Matrixdarstellungsrest 6.10e-15; Populationsrest 6.56e-15; stochastischer Summenrest 9.03e-15; Kovarianzrest 9.13e-16. Vorabgrenze 1e-10 unverändert. Kleine negative Gram-Eigenwerte bis etwa -4.5e-16 sind Gleitkommafehler innerhalb der ausgewiesenen absoluten Toleranz; exakte Positivität folgt aus dem Gram-Beweis.

Nach drei Ereignissen beträgt die Frobenius-Abweichung vom wiederholt dephasierten Produkt in den vier Pfadfällen etwa 1.31e-5, 2.20e-5, 2.84e-5 und 3.35e-5. Das ist eine Prüfung ganzer Matrizen entlang neuer Mehrereignisfolgen; der frühere Zwei-Moden-Gedächtniszeuge wird nicht als neues Ergebnis wiederholt. Ferngewichte bis etwa 2.8e-13 werden nur mit absoluter Fehlerkontrolle ausgewiesen, ohne daraus eine präzise relative Größenordnung oder ein neues striktes Positivitätszertifikat abzuleiten.

Keine Abbrüche oder angepassten Kriterien. Drei Ereignisse sind keine unendliche numerische Fortsetzung. Manuskript, Grundcode, empirische Ergebnisse und Lizenzen unverändert. GitHub-CI wird getrennt dokumentiert.

## Nächste Abhängigkeit
Ein zustandsabhängiger, kontrollierter Mehrereignis-Reichweitensatz bezüglich des anfänglichen Referenzgraphen oder eine andere aus BFG begründete räumliche Auswahl. Physikalische Uhrkalibrierung, vollständiger Energie-Impuls-Strom, Wirkung und Einstein bleiben offen.
