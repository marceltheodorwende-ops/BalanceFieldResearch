# Vorabprotokoll: kontinuierliche Interpolation eines BFG-Ereignisses

Ausgangspunkt e75c7ed634dc0632da2334dd1ca282522fd6db27. Prüfe einen eingefrorenen Vollpersistenz-Kernelkanal, ohne eine kontinuierliche Geometriegleichung einzuführen.

Kandidat A: zeitlich homogener Schur-Ansatz mit positiven reellen Multiplikatoren h_ab(t)=h_ab^t. Teste vollständige Positivität am exakt vorab benannten C-Zeugen Y=diag(3/20,1/5,4/15), F=diag(1,1,57/92), W=I/3, K=ones(3,3)/3. Erwartete alpha=1/26; die Gram-Matrix hat h12=h23=7/(5 sqrt(2)), h13=24/25. Bestimme den exakten Determinant des eintragsweisen Halbpotenz-Ansatzes. Ein negativer Wert verwirft nur diesen Interpolationsansatz.

Alternativen: konvexe Interpolation (1-s) Id+s Phi sowie winkelbasierte Gram-Interpolation cos[s(theta_a-theta_b)], theta_a=atan(sqrt(beta/alpha)y_a), s in [0,1]. Beweise Positivität und gleiche Endpunkte; prüfe Verschiedenheit am Zeugen sowie fehlende Halbzeitschritt-Semigruppengleichung. Keine alternative als physikalische Zeit auswählen.

Frische Kontrollen: exakte alpha-/Determinantenrechnung; ein vollständiger Zeugen-Quellaufruf; zwölf komplexe Präparationen (vier je n=3,4,5) auf C und drei zusätzliche unitäre Quellkontrollen, insgesamt 16 Aufrufe. Zwischenwerte s=1/4,1/2,3/4 für beide Alternativen; Gram-PSD >=-1e-10 und Endpunkt-/Kovarianzreste <1e-10. Seed 20261106. Negative Halbpotenz-Eigenwerte nur im exakten Zeugen als erwartetes Resultat verlangen, keine universelle Behauptung für jede Präparation.

Abgrenzung: festes Ereignis und fester linearer Kernelkanal, keine Interpolation der gesamten BFG-Geometrie, keine Sekunden, Hamiltonfunktion, räumlicher Viererstrom oder Einstein-Gleichung. Kein allgemeines No-Go für andere kontinuierliche Einbettungen.
