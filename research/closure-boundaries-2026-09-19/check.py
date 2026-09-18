"""Exact coefficient checks; the Hilbert-domain claim uses the analytic proof."""
from fractions import Fraction as Q
from math import factorial

for m in range(1, 9):
    for a in (Q(-2), Q(0), Q(1,3), Q(5)):
        # Scalar coefficients of c-I and of the derivative factor multiplying S.
        c=[Q(0)]*(m+2)
        c[1]=1
        c[m+1]=a
        derivative=[(i+1)*c[i+1] for i in range(m+1)]
        y=[Q(0)]*(2*m+1)
        for i,x in enumerate(derivative):
            for j,z in enumerate(derivative):
                y[i+j]+=x*z
        assert c[:m+1]==[0,1]+[0]*(m-1)
        assert y[0]==1
        assert y[m]*factorial(m)==2*(m+1)*factorial(m)*a
        assert c[m+1]*factorial(m+1)==factorial(m+1)*a
print('32 exact polynomial cases passed; no finite truncation used as an infinite-domain proof.')
