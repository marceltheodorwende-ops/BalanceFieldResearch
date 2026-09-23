from __future__ import annotations
import numpy as np
from .types import BFGState
from .linalg import hermitize

def _unitary(rng, n):
    Z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    ph = np.where(np.abs(d)>0, d/np.abs(d), 1.0)
    return Q @ np.diag(np.conj(ph))

def make_random_seed_state(dim=5, persistent_rank=3, seed=7):
    if not (2 <= persistent_rank <= dim):
        raise ValueError("persistent_rank must satisfy 2 <= rank <= dim")
    rng = np.random.default_rng(seed)
    U = _unitary(rng, dim)
    kvals = np.linspace(0.7,3.0,dim); kvals[0] = -2.0
    K = hermitize(U @ np.diag(kvals) @ U.conj().T)

    V = _unitary(rng, dim)
    yvals = np.linspace(0.05,2.2,dim)
    Y = hermitize(V @ np.diag(yvals) @ V.conj().T)

    W = _unitary(rng, dim)
    phases = np.exp(1j*rng.uniform(-0.9,0.9,persistent_rank))
    contract = np.linspace(0.35,0.75,dim-persistent_rank)
    rvals = np.concatenate([phases, contract.astype(complex)])
    R_C = W @ np.diag(rvals) @ W.conj().T

    D = rng.normal(size=dim)+1j*rng.normal(size=dim)
    D /= np.linalg.norm(D)
    return BFGState(D=D,K=K,Y=Y,R_C=R_C,name="random_seed",
                    metadata={"seed":seed,"kind":"random_noncommuting_seed"})

def make_commuting_control_state(dim=5, persistent_rank=3, seed=7):
    rng = np.random.default_rng(seed)
    U = _unitary(rng, dim)
    kvals=np.linspace(0.8,2.7,dim); kvals[0]=-2.0
    yvals=np.linspace(0.1,1.8,dim)
    K=hermitize(U@np.diag(kvals)@U.conj().T)
    Y=hermitize(U@np.diag(yvals)@U.conj().T)

    phases=np.exp(1j*np.linspace(-0.5,0.5,persistent_rank))
    contract=np.linspace(0.3,0.7,dim-persistent_rank)
    rvals=np.concatenate([phases,contract.astype(complex)])
    R_C=U@np.diag(rvals)@U.conj().T

    coeff=rng.normal(size=dim)+1j*rng.normal(size=dim)
    D=U@coeff; D/=np.linalg.norm(D)
    return BFGState(D=D,K=K,Y=Y,R_C=R_C,name="commuting_control",
                    metadata={"seed":seed,"kind":"commuting_inheritance_control"})
