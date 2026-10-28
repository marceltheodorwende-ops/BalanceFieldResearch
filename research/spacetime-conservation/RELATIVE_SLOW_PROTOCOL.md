# Vorabprotokoll: gekoppelte nahezu isotrope relative Randdynamik

Ausgangspunkt f212f35e049d96af615a4cac57111e77b38901f3. Ausschließlich die bereits aus BFG abgeleitete mathematische Kleinlast-Randkarte R_F und ihr gleichzeitiger Kernelkanal; kein Quellenaufruf bei s=0 und keine ungeprüfte uniforme Übertragung vieler Randschritte auf die volle Quelle.

Prüfe exakt für <A>_F=0, Z=I+rA, m2=<A²>_F:
R_F(Z)-I = [rA+(r²/2)(A²-m2 I)]/(1+r²m2).
Damit kann der quadratische Formterm für allgemeines A eine schnellere relative Drift verursachen. Vorab-Gegenzeuge A=diag(-1,0,1), F=I3: A²-(2/3)I !=0.

Konstruktiver Sonderbereich: A²=I, <A>_F=0, 0<r<1. Erwartet werden exakt rplus=r/(1+r²) und der Zwei-Niveau-Kernelfaktor h(r)=1/sqrt(1+r²+r^4). Für r0=epsilon, t=N epsilon² prüfe die gekoppelte Randgrenze u(t)=r/epsilon=(1+2t)^(-1/2) und die blockübergreifende Kerneldämpfung d(t)=(1+2t)^(-1/4). Diese Grenzparameter sind mathematisch, keine physikalischen Sekunden.

Kontrollen vor Auswertung: symbolische Form-/h-Identitäten; Randiterationen bis T=1/2 mit epsilon=1/10,1/20,1/40,1/80, N=50,200,800,3200. Beide Endfehler müssen zuletzt <0.01 und <0.4 des ersten liegen. Numerik ersetzt keinen Fehler-/Konvergenzbeweis.

Quellenkontrollen: n=2,4 mit komplex gedrehtem ausgeglichenem Zwei-Niveau-A, F=I und positivem komplexem K; je vier r-Werte wie oben, s=1/1000. Je eine zusätzliche unitäre Kontrolle. Dazu vier einereignisweise n=3-Gegenzeugenaufrufe: insgesamt14 vollständige Quellaufrufe. Seed20261109. Exakte ausgerichtete Quellidentitäten und Kovarianz <1e-10, Abstand der endlichen relativen Quellenfolger zur Randkarte <0.01. Dokumentiere diese endlichen Randfehler separat. Keine 3200 vollständigen Quellevents behaupten oder numerische Rangtoleranz ändern.

Offen bleibt die uniforme Fehlerkontrolle zwischen Randkarte und autonomer positiver-s-Quelle für N~epsilon^-2, einschließlich der schnell schrumpfenden Gesamtlast, sowie physikalische Uhr, Raummaß und Viererstrom.
