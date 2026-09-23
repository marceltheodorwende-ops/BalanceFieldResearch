from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import numpy as np

Array = np.ndarray

@dataclass(frozen=True)
class NumericalPolicy:
    atol: float = 1e-10
    rtol: float = 1e-9
    peripheral_tol: float = 1e-8
    rank_tol: float = 1e-10
    simple_gap_tol: float = 1e-8
    psd_tol: float = 1e-9
    novelty_tol: float = 1e-8

@dataclass
class BFGState:
    D: Array
    K: Array
    Y: Array
    R_C: Array
    generation: int = 0
    name: str = "state"
    metadata: dict[str, Any] = field(default_factory=dict)
    terminal: bool = False
    terminal_reason: str | None = None

    @property
    def dim(self) -> int:
        return int(self.D.shape[0])

@dataclass
class CoreStep:
    generation: int
    success: bool
    terminal_reason: str | None
    C: Array | None = None
    B: Array | None = None
    G: Array | None = None
    W: Array | None = None
    P: Array | None = None
    D_keep: Array | None = None
    D_up: Array | None = None
    D_out: Array | None = None
    lambda_keep: float | None = None
    lambda_up: float | None = None
    omega_keep: float | None = None
    omega_up: float | None = None
    packet: Array | None = None
    analysis: Array | None = None
    J: Array | None = None
    support_basis: Array | None = None
    K_inherited: Array | None = None
    K_successor: Array | None = None
    formation_eigenvalue: float | None = None
    formation_gap: float | None = None
    formation_vector: Array | None = None
    spectral_novelty: bool | None = None
    spectral_mismatch: float | None = None
    commutator_norm: float | None = None
    second_moment_loss: float | None = None
    diagnostics: dict[str, Any] = field(default_factory=dict)

@dataclass
class RunRecord:
    states: list[BFGState]
    steps: list[CoreStep]

    def summary(self) -> dict[str, Any]:
        successful = sum(int(s.success) for s in self.steps)
        novel = sum(int(bool(s.spectral_novelty)) for s in self.steps if s.spectral_novelty is not None)
        return {
            "states": len(self.states),
            "steps_attempted": len(self.steps),
            "successful_reclosures": successful,
            "spectrally_novel_steps": novel,
            "terminal": bool(self.states[-1].terminal) if self.states else True,
            "terminal_reason": self.states[-1].terminal_reason if self.states else "no states",
            "final_generation": self.states[-1].generation if self.states else -1,
        }
