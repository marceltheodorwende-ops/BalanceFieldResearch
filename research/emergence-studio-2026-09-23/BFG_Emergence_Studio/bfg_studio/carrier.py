from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
from .types import BFGState, CoreStep, NumericalPolicy
from .linalg import hermitize, psd_project

class CarrierAdapter(ABC):
    @abstractmethod
    def advance(self, previous: BFGState, step: CoreStep, policy: NumericalPolicy) -> BFGState:
        raise NotImplementedError

class ReferenceGramCarrier(CarrierAdapter):
    """Deterministic demonstration carrier, not a universal empirical realization."""

    def __init__(self, contraction: float = 0.82, phase_scale: float = 0.35):
        if not (0.0 <= contraction < 1.0):
            raise ValueError("contraction must lie in [0,1)")
        self.contraction = float(contraction)
        self.phase_scale = float(phase_scale)

    def advance(self, previous: BFGState, step: CoreStep, policy: NumericalPolicy) -> BFGState:
        if not step.success or step.support_basis is None or step.formation_vector is None:
            return BFGState(
                D=previous.D.copy(), K=previous.K.copy(), Y=previous.Y.copy(),
                R_C=previous.R_C.copy(), generation=previous.generation+1,
                name=f"{previous.name}_terminal",
                metadata={**previous.metadata, "carrier":"ReferenceGramCarrier"},
                terminal=True, terminal_reason=step.terminal_reason or "reclosure failed"
            )

        V = step.support_basis
        delta_full = V @ step.formation_vector
        if np.real(np.vdot(previous.D, delta_full)) < 0:
            delta_full = -delta_full

        K_next = hermitize(V @ step.K_successor @ V.conj().T)
        Y_next = psd_project(step.analysis.conj().T @ step.analysis, floor=0.0)

        evals, U = np.linalg.eigh(step.K_successor)
        phases = np.exp(1j*self.phase_scale*evals)
        R_active = U @ np.diag(phases) @ U.conj().T
        Pe = V @ V.conj().T
        I = np.eye(previous.dim, dtype=complex)
        R_next = V @ R_active @ V.conj().T + self.contraction*(I-Pe)

        return BFGState(
            D=delta_full, K=K_next, Y=Y_next, R_C=R_next,
            generation=previous.generation+1,
            name=f"{previous.name}_g{previous.generation+1}",
            metadata={
                **previous.metadata,
                "carrier":"ReferenceGramCarrier",
                "rebuild_note":"demonstration positive-Gram carrier; not a universal empirical realization"
            }
        )
