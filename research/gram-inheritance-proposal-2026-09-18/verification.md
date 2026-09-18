# Algebraische Kontrollfälle

Für Y=diag(2,5) und die orthonormalen Spalten
u1=(3/5,0,0,4/5), u2=(0,1,0,0) ist U†U=I und

    U† diag(2,5,2,5) U = diag(98/25,5).

Die Matrix ist positiv und ihr Spektrum liegt in [2,5]. Die nichttriviale
erste Komponente ist 2*(9/25)+5*(16/25)=98/25.
Für das frühere skalare Beispiel ist die eingeschränkte Last 1 und der
Folgezustand 1/4, während Last 4 G1 verletzt.

Diese Rechnungen wurden mit Python fractions.Fraction exakt kontrolliert;
die Assertions zu Orthonormalität und komprimierter Matrix bestanden (Exit 0).
Dies überprüft Kontrollfälle; der allgemeine Satz folgt aus dem Beweis in README.md.
Produktionscode unverändert, daher keine neue Software-Gesamtsuite ausgeführt.
