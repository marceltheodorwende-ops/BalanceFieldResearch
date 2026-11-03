# Scalar recursion: analytic proof and sharper envelope

Date: 3 November 2026. Internal analytic derivation, not independent peer review or proof-assistant verification. No priority claim is made.

Let `f(y)=2y^2/D(y)` with `D(y)=(1+y)^2(1+y^2)` and `0<y0<1`. Define `y_(k+1)=f(y_k)`.

## Proposition S1

For every finite k, `0<y_(k+1)<y_k<1`. For k>=1,

`0<y_k < 2^(-1-2^(k-1))`.

Consequently y_k tends to zero. This scalar envelope is sharper than the general multi-mode envelope in Theorem 26.4, but is proved only for the scalar recursion. It cannot be substituted into the general matrix theorem without another argument.

## Proof

For y>0 the denominator and numerator are positive. The exact identity

`D(y)-2y=(1+y^2)^2+2y^3>0`

gives `f(y)<y`. Induction preserves the domain. Furthermore,

`D(y)-8y^2=(1-y)^2(y^2+4y+1)>0` for `0<y<1`.

Thus `f(y)<1/4`, in particular `y1<1/4`. Finally `D(y)>1` for y>0, so `f(y)<2y^2`. Set `z_k=2y_k`. Then `z1<1/2` and `z_(k+1)<z_k^2`. Induction yields `z_k<(1/2)^(2^(k-1))`, which is the claimed envelope. Its right side tends to zero.

All sign steps and the induction are part of this written proof. A symbolic identity alone would not establish them.

## Proposition S2: existing stability bound rechecked

On [0,1], differentiation gives

`f'(y)=4y(1-y^3)/((1+y)^3(1+y^2)^2)`.

Therefore `0<=f'(y)<=4y/(1+y)^3<=16/27`, since

`16(1+y)^3-108y=4(2y-1)^2(y+4)>=0`.

The mean value theorem gives Lipschitz constant 16/27 on [0,1]. This rechecks the published bound; it is not claimed as new.

## Boundary and numerical controls

- At y=0 the recursion is fixed; strict positivity is inapplicable.
- At y=1, f(y)=1/4 exactly; the strict quarter inequality needs the open-domain assumption.
- At y=-1 the denominator is zero; extending the declared domain blindly fails.
- A binary64 evaluation at y=10^-200 returns zero while exact rational arithmetic returns a positive result. Floating zero is not exact terminal absorption.

The accompanying script checks five symbolic identities and 816 exact rational steps from 102 initial values. These support the written derivation; they do not constitute a Lean certificate.
