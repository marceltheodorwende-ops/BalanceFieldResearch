# Vorabprotokoll: endliche innere Blockaufspaltung

Ausgangspunkt 9bffe41bc268a1cb520feb43cb26fda9efaf19e1. Prüfe F=I plus zulässige Kreuzblockkopplung, A=diag(1,1,-1,-1), B_+=diag(1,-1,0,0), B_-=diag(0,0,1,-1), Z=I+rA+bB_sigma. Dabei 0<r<=1/4 und q=b/r. Dies ist eine konkrete höherdimensionale BFG-Präparation, keine universelle Störungsklasse.

Hypothese der exakten Randkarte: mu=1+r²+b²/2, r_+=(r+sigma b²/4)/mu, b_+=(1+sigma r)b/mu, also q_+/q=(1+sigma r)/(1+sigma q²r/4). Im oberen Fall soll für 0<q<2 eine monotone Zunahme ohne Kreuzung q=2 gelten. Im unteren Fall soll 0<q<=1/2,r<=1/4 eine invariant kontrahierende relative Störungsmenge bilden.

Nichtlinearer endlicher Austritt: Starte r0=epsilon, q0=epsilon². Prüfe für T=2 den ersten Austritt aus r<1/4,q<1/2. Solange kein Austritt vorliegt, soll r_j>=epsilon/sqrt(1+(5/2)j epsilon²) und q_(j+1)>=q_j(1+epsilon/3) gelten. Daraus folgt die obere Austrittszeit ceil(log[(1/2)/q0]/log(1+epsilon/3)), sofern diese <=2/epsilon² liegt. Beide Austrittsarten zählen; nicht nachträglich nur einen Pfad behalten.

Kontrollen: exakte symbolische Randrekurrenzen, Faktorisierungen und rationale Vergleichsungleichungen; epsilon=1/10,1/20,1/40,1/80, maximal N=2/epsilon² Randschritte. Dokumentiere Austritt, obere Zeitschranke und den nicht austretenden unteren Vergleich. Lange Randzahlen sind keine Original-Quelltrajektorien.

Positive-s-Quelle: Prüfe für geordnete drei Lastwerte mittels strikter Konvexität der echten g_alpha-Abbildung die nichtlineare obere q-Zunahme und untere q-Abnahme bei jedem Ereignis auf C. Eine quantitative lange Quellen-Austrittszeit wird ohne weitere uniforme Störungskontrolle nicht behauptet.

Originalkontrollen n=4 komplex gedreht, F>0 nichtkommutierend,K>=0: r=1/10,1/20; q=1/10,1/2; sigma=+/-1; s=1/1000,1/10000, insgesamt16 Quellaufrufe plus zwei unitäre Lastchecks=18. Vergleiche mit unabhängig rational berechneten vollständigen Y-Folgewerten; absolute Quellen-/Kovarianzreste <1e-10, normierte r/b-Reste <1e-8. Prüfe beide q-Richtungen und erhaltene Reihenfolge. Seed20261114. Keine Grundcode-/Toleranzänderung.

Grenzen: Der nichtlineare Austritt wird für die erklärte Randkarte geprüft, keine allgemeine physikalische Instabilität oder positive-s-Langzeitflucht vorausgesetzt. Die untere Kontraktion und die offenen Quellen-/Raum-/Uhr-/Viererstrom-Brücken bleiben sichtbar.
