# Vorabprotokoll: gemeinsame Kleinlast-Randkarte

Ausgangscommit 5140f9963f3f4c200c934a44a6c9f5ad4755a5eb. Vollpersistenz, F>0, Y=sZ, s=tr(FY)/trF und tr(FZ)/trF=1, Z>0. Prüfe den gemeinsamen s->0-Grenzfall bei fester relativer Last Z.

Hypothesen: Mit mu2=tr(FZ²)/trF gilt alpha=s²mu2+O(s³), Yplus=s²(mu2 I+Z²)+O(s³), splus=2mu2 s²+O(s³), Zplus->(mu2 I+Z²)/(2mu2). Der Kernelkanal geht dagegen gegen einen im Allgemeinen nichttrivialen Kanal mit T_C0=sqrt(mu2)(mu2 I+Z²)^(-1/2), T_B0=Z(mu2 I+Z²)^(-1/2). Die relative Form und F bestimmen die Grenzdynamik; s=0 ist eine mathematische Randkarte, kein regulärer Quellenaufruf.

Vorabzeuge: n=2, F=I, Z=diag(1/2,3/2), W=I/2,K=ones/2; mu2=5/4, Zplus-Grenze=diag(3/5,7/5), Grenz-h12=4/sqrt(21)<1. Vergleiche denselben F,W,K entlang Z=I: dort ist der Kanal exakt Id. Beide Y-Pfade gehen gegen null; prüfe die unterschiedlichen Kernelgrenzen.

Kontrollen: exakte rationale Zeugen-alpha-/Y-Grenzen; n=2-Zeuge und komplexe Präparationen n=3,4, je s=1/20,1/40,1/80,1/160; drei zusätzliche unitäre Kontrollen sowie vier skalare Z=I-Kontrollen, insgesamt19 vollständige Quellaufrufe. Seed20261108. Erfasse Fehler von alpha/s², splus/s², Zplus und Kplus zu den Grenzformeln; verlange letzten Fehler <0.4 erster, sofern erster >1e-10, und letzten Fehler <0.1. Exakte endliche Quell-/Koordinatenrekonstruktion und Kovarianz <1e-10; bewahre große, aber konvergierende Asymptotikfehler. Der Zeugen-Kernelsprung darf bei kleinstem s nicht unter die Hälfte seines strikt positiven Grenzwerts fallen.

Keine universelle kontinuierliche Zeit, kein auf Quelle s=0 ausgeführtes Ereignis, keine beliebig lange numerische Randtrajektorie und kein vollständiger Energie-Impuls-/Einstein-Schluss. Eine gemeinsame nahezu isotrope Skalierung bleibt als gesonderte Folgefrage offen.
