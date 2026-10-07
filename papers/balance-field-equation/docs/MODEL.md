# State and transition structure

## Finite state

On a finite complex Hilbert space $H$, the state is

$$\Xi=(K,\rho_F,\rho_W,Y,P).$$

| Component | Type and role |
| --- | --- |
| $K$ | Hermitian formation/kernel operator |
| $\rho_F$ | Positive formation operator, not required to have unit trace |
| $\rho_W$ | Positive trace-one witness operator on the declared carrier |
| $Y$ | Positive semidefinite internal load/Gram operator |
| $P$ | Orthogonal carrier projector |

Simultaneous unitary coordinate changes represent the same state class. Original witness mass and directed transport history are trajectory records; they are not recovered from normalized witness data alone.

## Update order

1. Spectral selection $Q=\mathbf1_{[0,1)}(Y)$.
2. Canonical polar transport of $QP$, selected carrier and conditional witness mass.
3. Positive internal metric $G=I+Y$ and its metric selection projector.
4. Formation-dependent dual loads and endogenous analysis weights.
5. Ambient analysis $A:H\to H\oplus H$ and a reduced positive-singular-value SVD.
6. Successor formation/kernel geometry and load $Y_+$.
7. R4 carrier realignment and inheritance of formation and witness.
8. Complement formation: continuation when the complement is zero; otherwise a unique admissible negative seed or a named terminal outcome.
9. Successor on the unitary quotient with its endogenous dimension.

For a selected-carrier orthonormal frame $Z$ and $D=Z^\dagger GZ$,

$$P_G=ZD^{-1}Z^\dagger G,\qquad C=G^{-1},\qquad B=I-C.$$

The analysis uses the ambient input space. Replacing it with a carrier-restricted operator changes the model and its conclusions. The original PDF specifies weights, loads, dimensions and terminal gates in detail.

## Geometry acting back on geometry

The explicit feedback path is

$$Y\longrightarrow G,C,B,P_G\longrightarrow\Lambda_C,\Lambda_B,\alpha,\beta\longrightarrow A\longrightarrow Y_+.$$

Formation and carrier variables also enter this path. Geometric feedback alone is not a proof that every state is stable. On the declared scalar branch,

$$y_+=\frac{2y^2}{(1+y)^2(1+y^2)},\qquad 0<y<1,$$

and $0<y_+<y$. Full-state neutral directions and endogenous derivative paths must be treated separately.

## Dependency order of proposed physical transitions

Level 0/Urfeld → finite state and scalar order readout → internal geometric recursion → calibrated event time and Lorentzian spacetime/gravity → quantum instruments and particle parameters → atoms → molecules → biological organization → functional world/self organization → phenomenal interpretation.

This is an order of dependencies, not a proved universal emergence chain. A positive internal metric does not itself supply Lorentzian spacetime. Atoms precede molecular and biological applications; operational transition maps remain required at each physical step.

For discrete projected dynamics, the typed condition is

$$\Pi\circ\mathcal U_\Xi=\mathcal U_\Psi\circ\Pi.$$

A continuous projected model instead requires a calibrated duration and a flow:

$$\Pi(\mathcal U_\Xi(\Xi_k))=\varphi_F^{\Delta t_k}(\Pi(\Xi_k)).$$

Neither condition becomes established merely by naming $\Pi$ or a clock.
