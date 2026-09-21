# Rechenkontrolle und Prüfgrenzen

Datum: 21. September 2026. Dokumentationsänderung ohne Änderung des Modellcodes.

Die Energiebeziehung wurde algebraisch aus D_next und G_next abgeleitet. Mit Python Fraction wurden die drei Tabellenzeilen exakt nachgerechnet: (g,Amplitude,E_next) = (1/5,5/12,5/6), (1/25,25/52,25/26), (1/10,5/11,10/11). Der Koeffizientenvergleich bestätigte exakt:

    (1+eta)^2(1+eta²)-8eta² = (eta-1)^2(eta²+4eta+1).

Eine ergänzende NumPy-Kontrolle mit c=diag(1,2), W=diag(2,3), L=[[1,1],[0,1]], U=[[0,-1],[1,0]], eta=0.2 ergab einen Gramresidual von 8.78e-17. Für P=diag(1,1,1,1,0), q=5/6 betrug ||R2-R1²|| etwa 1.11e-16. Diese Rundungsresiduen ergänzen die algebraischen Beweise, ersetzen sie nicht. Die Gaps 1/6 und 11/36 wurden rational bestätigt.

Kein neuer Gesamttestlauf: Die 14 gezielten und 143 gesamten Tests betreffen den früher dokumentierten Implementierungsstand 8378d8becac5780071baa4f6d3f29ba2dae09c6e. Keine neuen Messdaten, keine externe Begutachtung und keine erneute vollständige Prüfung des Quellenkorpus.
