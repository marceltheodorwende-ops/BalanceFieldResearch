# Vorabprotokoll: uniforme Übertragung bei kritischem Ungleichgewicht

Ausgangspunkt a2818bcf91dbc3359473b4a97b16839c727102ab; exakte positive-Last-Zwei-Niveau-Dynamik, delta=kappa epsilon, |kappa|<=1/2, r0=epsilon<=1/10. s bezeichnet wie in IMBALANCE den spektralen Mittelpunkt. Keine neuen Grundgleichungen.

Beweiskandidat: Auf dem festen Rechteck 0<=s<=1/100, 0<=r<=1/4, |delta|<=1/20 ist R(s,r,delta)-b_delta(r)=sr E(s,r,delta) mit analytisch begrenztem rationalem E. Bestimme C_R als aufgerundete exakte gewichtete Koeffizientenschranke für |E|. Bestimme analog C_L für |partial_r² log h_delta(r)|. Beide Nenneruntergrenzen müssen exakt positiv sein. Dann soll auf r<=2epsilon die Schranke b'_delta<=1+3epsilon² gelten; Bootstrap und summierbare s_j sollen Formfehler/epsilon<=C_T s0 liefern, C_T=3 C_R exp(3T), sofern C_T s0<=1/2. Prüfe s_+<=s/32 und Kernel-Logfehler <=[17epsilon²+2 C_L C_T T]s0. Kandidaten oder Beweisfehler bleiben sichtbar.

Kontrollen: exakte rationale Faktorisierung/Divisibilität und Koeffizienten-Rechteckzertifikate, explizite q_s-Identität; kappa=-1/2,0,1/2, epsilon=1/10,1/20,1/40,1/80, T=1/2, s0=epsilon^4. 80-stellige positive-s-Rekurrenzpräfixe bis s<1e-60 und anschließend Randfortsetzung mit analoger analytischer Restgrenze; diese Rechnungen sind keine langen Original-Quellaufrufe oder Intervallarithmetik. Erfasse Bootstrap-Bedingung und beide uniformen Grenzen, Zuschlag1e-10. Letzte Kontinuumsfehler je kappa <0.01 und <0.4 erster.

Originalquelle: n=2,4 mit komplexem A,F,K; je kappa=-1/2,0,1/2 und epsilon=1/10,1/20 ein vollständiger positiver-Last-Aufruf s0=epsilon^4, dazu je eine unitäre Kontrolle, insgesamt14 Quellaufrufe. Endliche exakte Rekurrenz-/Kovarianzreste <1e-10. Seed20261112. Original-Rangschwelle unverändert, Quelle nie bei Null-Last ausführen.

Erst nach dem uniformen Nachweis darf die kritische Grenzfamilie als Grenzwert der exakten mathematischen positiven-Last-Quelle bezeichnet werden. Physikalische Uhr, Raum, Sektorauswahl und Energie-Impuls-/Einstein-Interpretation bleiben offen.
