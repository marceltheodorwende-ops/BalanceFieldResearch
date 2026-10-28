# Vorabprotokoll: zusätzliche Lastniveaus und transversale Empfindlichkeit

Ausgangspunkt c3002e22a47691b0675041f42a9be0b247f286dc. Prüfe den ausgeglichenen Zwei-Niveau-Unterbereich, nicht automatisch die gesamte kritische Familie. A=diag(1,1,-1,-1), F mit gleich gewichteten Blöcken; B_+=diag(1,-1,0,0), B_-=diag(0,0,1,-1), jeweils formationszentriert. Bei Z=I+rA verändert eine infinitesimale innere Blockaufspaltung eta B weder die Formationslasten noch die Normierung in erster Ordnung.

Hypothesen: Auf der Randkarte ist D R_Z[B_±]=(1±r)B_±/(1+r²). Relativ zur Basisaufspaltung r_+=r/(1+r²) hat die Störung den Faktor 1±r. Bei r0=epsilon,N epsilon²->T folgt epsilon log G_±->±(sqrt(1+2T)-1). Das betrifft Variationen am exakten Sektor, keine bereits bewiesene nichtlineare Flucht endlicher Störungen.

Positive-s-Quelle: leite die exakten relativen Tangentenfaktoren H_±=2sr g'_alpha(s(1±r))/(g_alpha(s(1+r))-g_alpha(s(1-r))) her. Die strikte Konvexität und Monotonie auf C soll H_+>1 und 0<H_-<1 liefern. Bestimme durch exakte rationale Koeffizientenabschätzung Konstanten für |partial_s log H_±| auf 0<=s<=1/100,0<=r<=1/4 und prüfe H_±(0,r)=1±r. Mit dem schon bewiesenen uniformen ausgeglichenen Formfehler soll der skalierte logarithmische Wachstumsbefund auf die positive-s-Quelle übertragen werden.

Vor Auswertung: exakte Richtungsableitungs-/Quotienten-/Grenzidentitäten und Nennerzertifikate; vier Randfolgen epsilon=1/10,1/20,1/40,1/80 bis T=1/2. Beide skalierten Logfehler zuletzt <0.02 und <0.4 erster. Eine numerische Erfolgskontrolle ist kein Ersatz für den Kokzyklusbeweis.

Originalquelle n=4 komplex gedreht, positives F=I plus Kreuzblockkopplung und positiver K. r=1/10,1/20; s=1/1000,1/10000. Pro Präparation ein Basisaufruf und zentrale +/-eta-Variationen in beiden B-Richtungen für eta=1e-4,1e-5:36 Aufrufe plus zwei unitäre Basischecks, insgesamt38. Exakte Basis-/Kovarianzreste <1e-10; je Richtungsableitung bester zentraler Fehler <1e-6, alle Schrittweitenfehler behalten. Seed20261113. Rangtoleranzen und Grundcode unverändert.

Grenzen: keine nichtlineare Langzeitstabilität oder universelle Instabilität von BFG behaupten. Insbesondere verschwindet die innere Aufspaltungsrichtung, wenn der jeweilige Block nur Dimension eins hat. Physikalische Uhr, Raummaß und vollständiger Viererstrom bleiben offen.
