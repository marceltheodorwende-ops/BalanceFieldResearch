"""Executable finite kernel for the living BFG fundamental-closure program.

The module implements the finite theorem-level kernel and a completion-law contract.
It intentionally refuses to invent the missing universal successor law.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

import numpy as np

Array = np.ndarray


class BFGError(Exception):
    pass


class IncompleteClosureLaw(BFGError):
    pass


class InadmissibleState(BFGError):
    pass


def dagger(a: Array) -> Array:
    return np.asarray(a).conj().T


def hermitian_part(a: Array) -> Array:
    a = np.asarray(a)
    return (a + dagger(a)) / 2


def opnorm(a: Array) -> float:
    a = np.asarray(a)
    return 0.0 if a.size == 0 else float(np.linalg.norm(a, ord=2))


def is_hermitian(a: Array, tol: float = 1e-9) -> bool:
    return opnorm(a - dagger(a)) <= tol


def is_psd(a: Array, tol: float = 1e-9) -> bool:
    if not is_hermitian(a, tol):
        return False
    vals = np.linalg.eigvalsh(hermitian_part(a))
    return bool(vals.size == 0 or vals.min() >= -tol)


def neutral_pair(y: Array) -> tuple[Array, Array]:
    """BFG neutral pair C=(I+Y)^-1 and B=Y(I+Y)^-1."""
    y = np.asarray(y, dtype=complex)
    if y.ndim != 2 or y.shape[0] != y.shape[1]:
        raise InadmissibleState("Y must be square")
    if not is_psd(y):
        raise InadmissibleState("Y must be positive semidefinite")
    eye = np.eye(y.shape[0], dtype=complex)
    c = np.linalg.inv(eye + y)
    b = y @ c
    return hermitian_part(c), hermitian_part(b)


def g_norm_sq(x: Array, g: Array) -> float:
    val = np.vdot(x, g @ x)
    if abs(float(np.imag(val))) > 1e-8:
        raise InadmissibleState("G norm must be real")
    return float(np.real(val))


def reciprocal_weights(load_c: float, load_b: float) -> tuple[float, float]:
    """Unique reciprocal weights for two strictly positive loads."""
    if load_c <= 0 or load_b <= 0:
        raise InadmissibleState("reciprocal balance requires two positive loads")
    total = load_c + load_b
    return load_b / total, load_c / total


def metric_projector(z: Array, g: Array) -> Array:
    """G-orthogonal projector onto Ran(z)."""
    z = np.asarray(z, dtype=complex)
    g = np.asarray(g, dtype=complex)
    gram = dagger(z) @ g @ z
    if np.linalg.matrix_rank(gram) < gram.shape[0]:
        raise InadmissibleState("basis is not G-independent")
    return z @ np.linalg.inv(gram) @ dagger(z) @ g


def peripheral_eigenbasis(r: Array, tol: float = 1e-8) -> Array:
    """Finite diagnostic basis for the unit-modulus eigenspace.

    This is a basis of the peripheral subspace, not the generally-oblique Riesz
    projector itself.
    """
    r = np.asarray(r, dtype=complex)
    vals, vecs = np.linalg.eig(r)
    idx = np.where(np.abs(np.abs(vals) - 1.0) <= tol)[0]
    if idx.size == 0:
        return np.zeros((r.shape[0], 0), dtype=complex)
    z = vecs[:, idx]
    q, rr = np.linalg.qr(z)
    diag = np.abs(np.diag(rr))
    rank = int(np.count_nonzero(diag > tol))
    return q[:, :rank]


def polar_partial_isometry(a: Array, tol: float = 1e-12) -> Array:
    """Canonical polar partial isometry via the SVD."""
    a = np.asarray(a, dtype=complex)
    u, s, vh = np.linalg.svd(a, full_matrices=False)
    if s.size == 0:
        return np.zeros_like(a)
    threshold = max(tol, tol * float(s[0]))
    rank = int(np.count_nonzero(s > threshold))
    if rank == 0:
        return np.zeros_like(a)
    return u[:, :rank] @ vh[:rank, :]


def analysis_operator(
    y: Array,
    d: Array,
    p_g: Array,
    *,
    tol: float = 1e-12,
) -> tuple[Array, dict]:
    """Build the legacy rank-one reciprocal-weight analysis operator.

    Boundary semantics match the current density-form kernel:
      - exactly zero represented branch -> dual_load_zero_terminal;
      - positive branch whose load is below floating resolution ->
        dual_load_numerical_ambiguity.
    """
    c, b = neutral_pair(y)
    g = np.eye(y.shape[0], dtype=complex) + y
    d_c = p_g @ c @ d
    d_b = p_g @ b @ d
    load_c = g_norm_sq(d_c, g)
    load_b = g_norm_sq(d_b, g)

    exact_zero_c = np.count_nonzero(d_c) == 0
    exact_zero_b = np.count_nonzero(d_b) == 0
    if exact_zero_c or exact_zero_b:
        raise InadmissibleState("dual_load_zero_terminal")
    if load_c <= tol or load_b <= tol:
        raise InadmissibleState("dual_load_numerical_ambiguity")

    weight_c, weight_b = reciprocal_weights(load_c, load_b)
    a = np.vstack(
        (
            np.sqrt(weight_c) * (p_g @ c),
            np.sqrt(weight_b) * (p_g @ b),
        )
    )
    return a, {
        "C": c,
        "B": b,
        "G": g,
        "load_C": load_c,
        "load_B": load_b,
        "weight_C": weight_c,
        "weight_B": weight_b,
    }


def support_compression(a: Array, j: Array) -> Array:
    """Support-coordinate transport J^*(A⊕A)J."""
    a = np.asarray(a, dtype=complex)
    zero = np.zeros_like(a)
    a2 = np.block([[a, zero], [zero, a]])
    return dagger(j) @ a2 @ j


@dataclass(frozen=True)
class FiniteState:
    D_cap: Array
    coherence: Array
    emergence: Array
    d: Array
    R_C: Array
    N_R: Optional[Array] = None

    @property
    def dim(self) -> int:
        return int(np.asarray(self.D_cap).shape[0])

    def formation(self) -> Array:
        return self.coherence + self.emergence - self.D_cap


@dataclass(frozen=True)
class Reconstruction:
    B_C: Array
    W_N: Array
    L_C: Array

    def load(self) -> Array:
        h = dagger(self.B_C) @ self.W_N @ self.B_C
        return hermitian_part(dagger(self.L_C) @ h @ self.L_C)


@dataclass(frozen=True)
class ClosureKernelResult:
    Y: Array
    P_G: Array
    analysis: Array
    J: Array
    S: Array
    E: Array
    D_cap_transport: Array
    coherence_transport: Array
    emergence_transport: Array
    diagnostics: dict


@dataclass(frozen=True)
class CompletionLaw:
    reconstruct: Optional[Callable[[FiniteState], Reconstruction]] = None
    next_recursion: Optional[Callable[[FiniteState, ClosureKernelResult], Array]] = None
    next_recursion_metric: Optional[
        Callable[[FiniteState, ClosureKernelResult], Optional[Array]]
    ] = None
    next_active: Optional[Callable[[FiniteState, ClosureKernelResult], Array]] = None
    next_reconstruction: Optional[
        Callable[[FiniteState, ClosureKernelResult], Reconstruction]
    ] = None


def validate_state(s: FiniteState, tol: float = 1e-9) -> None:
    n = s.dim
    for name, a in (
        ("D_cap", s.D_cap),
        ("coherence", s.coherence),
        ("emergence", s.emergence),
        ("R_C", s.R_C),
    ):
        if np.asarray(a).shape != (n, n):
            raise InadmissibleState(f"{name} has wrong shape")
    if np.asarray(s.d).shape != (n,):
        raise InadmissibleState("d has wrong shape")
    for name, a in (
        ("D_cap", s.D_cap),
        ("coherence", s.coherence),
        ("emergence", s.emergence),
    ):
        if not is_hermitian(a, tol):
            raise InadmissibleState(f"{name} must be Hermitian")


def closure_kernel(
    s: FiniteState,
    reconstruction: Reconstruction,
) -> ClosureKernelResult:
    validate_state(s)

    y = reconstruction.load()
    if not is_psd(y):
        raise InadmissibleState("reconstructed Y is not positive semidefinite")

    z = peripheral_eigenbasis(s.R_C)
    if z.shape[1] == 0:
        raise InadmissibleState("no peripheral persistent subspace")

    g = np.eye(s.dim, dtype=complex) + y
    p_g = metric_projector(z, g)
    a, diag = analysis_operator(y, s.d, p_g)
    j = polar_partial_isometry(a)
    support = hermitian_part(dagger(j) @ j)
    range_projection = hermitian_part(j @ dagger(j))

    return ClosureKernelResult(
        Y=y,
        P_G=p_g,
        analysis=a,
        J=j,
        S=support,
        E=range_projection,
        D_cap_transport=hermitian_part(support_compression(s.D_cap, j)),
        coherence_transport=hermitian_part(support_compression(s.coherence, j)),
        emergence_transport=hermitian_part(support_compression(s.emergence, j)),
        diagnostics=diag,
    )


def universal_update(s: FiniteState, law: CompletionLaw) -> FiniteState:
    """Full finite update. Refuses to guess missing successor laws."""
    missing = [
        name
        for name, value in (
            ("reconstruct", law.reconstruct),
            ("next_recursion", law.next_recursion),
            ("next_recursion_metric", law.next_recursion_metric),
            ("next_active", law.next_active),
            ("next_reconstruction", law.next_reconstruction),
        )
        if value is None
    ]
    if missing:
        raise IncompleteClosureLaw(
            "universal BFG update is not closed; missing: " + ", ".join(missing)
        )

    rec = law.reconstruct(s)
    kernel = closure_kernel(s, rec)

    r_next = law.next_recursion(s, kernel)
    n_next = law.next_recursion_metric(s, kernel)
    d_next = law.next_active(s, kernel)

    # Calling this is mandatory: a full law must define the successor Gram data.
    _ = law.next_reconstruction(s, kernel)

    out = FiniteState(
        D_cap=kernel.D_cap_transport,
        coherence=kernel.coherence_transport,
        emergence=kernel.emergence_transport,
        d=np.asarray(d_next, dtype=complex),
        R_C=np.asarray(r_next, dtype=complex),
        N_R=None if n_next is None else np.asarray(n_next, dtype=complex),
    )
    validate_state(out)
    return out


# ---------------------------------------------------------------------------
# Generator-level quotient formulation
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class QuotientState:
    """Minimal operational state after quotienting factorization gauges.

    B_C/W_N/L_C are represented only by their positive master load Y.
    Raw N_R/R are represented only by the realized recursive operator R_C.

    P_per is an optional numerical certificate/cache for the exact peripheral
    Riesz range. It is not an extra fundamental law: mathematically it is
    derived from R_C. Keeping it prevents near-unit stable eigenvalues from
    being promoted to persistence by a floating-point tolerance.
    """
    D_cap: Array
    coherence: Array
    emergence: Array
    d: Array
    Y: Array
    R_C: Array
    P_per: Optional[Array] = None

    @property
    def dim(self) -> int:
        return int(np.asarray(self.D_cap).shape[0])

    def formation(self) -> Array:
        return self.coherence + self.emergence - self.D_cap


@dataclass(frozen=True)
class PreclosureCandidate:
    """All successor data forced before choosing Y_plus and R_C_plus.

    Operators are represented in support coordinates on the source carrier.
    The physical new carrier is Ran(J); J restricts to an isometry from Ran(S)
    onto Ran(J).
    """
    analysis: Array
    J: Array
    S: Array
    E: Array
    packet_ambient: Array
    packet_support: Array
    D_cap_plus: Array
    coherence_plus: Array
    emergence_plus: Array
    formation_plus: Array
    diagnostics: dict


@dataclass(frozen=True)
class CompletedQuotientState:
    state: QuotientState
    preclosure: PreclosureCandidate


def validate_quotient_state(s: QuotientState, tol: float = 1e-9) -> None:
    n = s.dim
    for name, a in (
        ("D_cap", s.D_cap),
        ("coherence", s.coherence),
        ("emergence", s.emergence),
        ("Y", s.Y),
        ("R_C", s.R_C),
    ):
        if np.asarray(a).shape != (n, n):
            raise InadmissibleState(f"{name} has wrong shape")
    if np.asarray(s.d).shape != (n,):
        raise InadmissibleState("d has wrong shape")
    for name, a in (
        ("D_cap", s.D_cap),
        ("coherence", s.coherence),
        ("emergence", s.emergence),
    ):
        if not is_hermitian(a, tol):
            raise InadmissibleState(f"{name} must be Hermitian")
    if not is_psd(s.Y, tol):
        raise InadmissibleState("Y must be positive semidefinite")
    if s.P_per is not None:
        p = hermitian_part(np.asarray(s.P_per, dtype=complex))
        if p.shape != (n, n):
            raise InadmissibleState("P_per has wrong shape")
        if opnorm(p @ p - p) > 10 * tol:
            raise InadmissibleState("P_per must be an orthogonal projector")
        # Certificate consistency: R_C must act as identity on the declared
        # persistent range for the CSR-generated class.
        if opnorm((s.R_C - np.eye(n, dtype=complex)) @ p) > 100 * tol:
            raise InadmissibleState("P_per is inconsistent with R_C")


def preclosure_update(s: QuotientState) -> PreclosureCandidate:
    """Maximal finite update forced by the current generator equations.

    This function stops before successor Y and successor R_C because the current
    BFG corpus does not determine those two operators uniquely.
    """
    validate_quotient_state(s)

    z = peripheral_eigenbasis(s.R_C)
    if z.shape[1] == 0:
        raise InadmissibleState("no isolated finite peripheral eigenspace represented")

    g = np.eye(s.dim, dtype=complex) + s.Y
    p_g = metric_projector(z, g)
    analysis, diag = analysis_operator(s.Y, s.d, p_g)
    j = polar_partial_isometry(analysis)
    support = hermitian_part(dagger(j) @ j)
    e = hermitian_part(j @ dagger(j))

    packet_ambient = analysis @ s.d
    packet_support = dagger(j) @ packet_ambient

    dcap_p = hermitian_part(support_compression(s.D_cap, j))
    coh_p = hermitian_part(support_compression(s.coherence, j))
    em_p = hermitian_part(support_compression(s.emergence, j))
    form_p = hermitian_part(coh_p + em_p - dcap_p)

    return PreclosureCandidate(
        analysis=analysis,
        J=j,
        S=support,
        E=e,
        packet_ambient=packet_ambient,
        packet_support=packet_support,
        D_cap_plus=dcap_p,
        coherence_plus=coh_p,
        emergence_plus=em_p,
        formation_plus=form_p,
        diagnostics=diag,
    )


def canonical_gram_factorization(y: Array) -> Reconstruction:
    """One representation of an arbitrary PSD load.

    This is a representation theorem, not a claim that the gauge is fundamental.
    """
    y = hermitian_part(np.asarray(y, dtype=complex))
    if not is_psd(y):
        raise InadmissibleState("Y must be positive semidefinite")
    vals, vecs = np.linalg.eigh(y)
    sqrt_y = (vecs * np.sqrt(np.clip(vals, 0.0, None))) @ dagger(vecs)
    eye = np.eye(y.shape[0], dtype=complex)
    return Reconstruction(B_C=sqrt_y, W_N=eye, L_C=eye)


def recursion_family(projector: Array, r: float) -> Array:
    """Explicit family proving bounded-recursion non-uniqueness."""
    projector = hermitian_part(np.asarray(projector, dtype=complex))
    if not (0.0 <= r < 1.0):
        raise ValueError("r must lie in [0,1)")
    if opnorm(projector @ projector - projector) > 1e-9:
        raise InadmissibleState("projector must be idempotent")
    eye = np.eye(projector.shape[0], dtype=complex)
    return projector + r * (eye - projector)


def complete_from_two_laws(
    source: QuotientState,
    pre: PreclosureCandidate,
    y_plus: Array,
    r_c_plus: Array,
) -> CompletedQuotientState:
    """Complete the quotient successor once the two genuinely missing laws are supplied.

    The active successor is NOT an independent choice:
        d_plus = C_N(Y_plus) packet_support.
    """
    y_plus = hermitian_part(np.asarray(y_plus, dtype=complex))
    r_c_plus = np.asarray(r_c_plus, dtype=complex)
    n = source.dim

    if y_plus.shape != (n, n) or r_c_plus.shape != (n, n):
        raise InadmissibleState("completion operators must use support-coordinate shape")
    if not is_psd(y_plus):
        raise InadmissibleState("Y_plus must be positive semidefinite")

    c_plus, _ = neutral_pair(y_plus)
    d_plus = c_plus @ pre.packet_support

    state = QuotientState(
        D_cap=pre.D_cap_plus,
        coherence=pre.coherence_plus,
        emergence=pre.emergence_plus,
        d=d_plus,
        Y=y_plus,
        R_C=r_c_plus,
    )
    validate_quotient_state(state)
    return CompletedQuotientState(state=state, preclosure=pre)


# ---------------------------------------------------------------------------
# Canonical Self-Reclosure (CSR) candidate
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CSRResult:
    terminal: bool
    reason: str
    state: Optional[QuotientState]
    persistent_projector: Optional[Array]
    singular_values: Optional[Array]
    source_active_frame: Optional[Array] = None
    target_frame: Optional[Array] = None


def _orthonormal_range(a: Array, tol: float = 1e-10) -> Array:
    """Orthonormal basis for Ran(a)."""
    a = np.asarray(a, dtype=complex)
    if a.size == 0:
        return np.zeros((a.shape[0], 0), dtype=complex)
    u, s, _ = np.linalg.svd(a, full_matrices=False)
    if s.size == 0:
        return np.zeros((a.shape[0], 0), dtype=complex)
    threshold = max(tol, tol * float(s[0]))
    rank = int(np.count_nonzero(s > threshold))
    return u[:, :rank]



def _source_persistent_basis(s: QuotientState, tol: float = 1e-10) -> Array:
    """Exact/certified persistent basis for the CSR-generated class."""
    if s.P_per is not None:
        return _orthonormal_range(s.P_per, tol=tol)
    return peripheral_eigenbasis(s.R_C, tol=max(tol, 1e-8))


def scalar_intrinsic_gram_map(y: float) -> float:
    """Exact 1D/full-persistence intrinsic-Gram update.

    f(y)=2 y^2 / ((1+y)^2 (1+y^2)).
    For every y>0, 0<f(y)<y and f(y)~2y^2 as y->0+.
    """
    y = float(y)
    if y <= 0:
        raise ValueError("y must be positive")
    return 2.0 * y * y / ((1.0 + y) ** 2 * (1.0 + y * y))


def polar_cross_stratum_projector(q_minus: Array, q_plus: Array, tol: float = 1e-10) -> tuple[Array, Array]:
    """R4-style polar transport between two orthogonal support projectors.

    Returns (T, final_projector), with T = polar(Q_plus Q_minus).
    """
    q_minus = hermitian_part(np.asarray(q_minus, dtype=complex))
    q_plus = hermitian_part(np.asarray(q_plus, dtype=complex))
    x = q_plus @ q_minus
    t = polar_partial_isometry(x, tol=tol)
    return t, hermitian_part(t @ dagger(t))


def canonical_self_reclosure_step(
    s: QuotientState,
    *,
    tol: float = 1e-10,
    require_simple_negative_formation: bool = True,
) -> CSRResult:
    """Finite BFG-only CSR candidate.

    Historical CSR candidate using the package's declared finite completions:
        - intrinsic-Gram successor load on the active carrier;
        - inherited-only polar persistence transport in this legacy CSR stratum;
        - neutral retained transverse recursion C_N(Y_plus).

    These are not relabelled as uniquely source-derived.

    The function returns a terminal result instead of inventing a tie-break.
    """
    validate_quotient_state(s, tol=max(tol, 1e-9))

    w = _source_persistent_basis(s, tol=tol)
    if w.shape[1] == 0:
        return CSRResult(True, "no_persistent_source", None, None, None)

    g = np.eye(s.dim, dtype=complex) + s.Y
    p_g = metric_projector(w, g)
    try:
        analysis, diag = analysis_operator(s.Y, s.d, p_g, tol=tol)
    except InadmissibleState as exc:
        return CSRResult(True, str(exc), None, None, None)

    u, sing, vh = np.linalg.svd(analysis, full_matrices=False)
    if sing.size == 0:
        return CSRResult(True, "zero_analysis_rank", None, None, None)
    threshold = max(tol, tol * float(sing[0]))
    rank = int(np.count_nonzero(sing > threshold))
    if rank == 0:
        reason = "zero_analysis_rank" if float(sing[0]) == 0.0 else "numerical_rank_ambiguity"
        return CSRResult(True, reason, None, None, sing)

    u_r = u[:, :rank]
    v_r = dagger(vh[:rank, :])
    sing_r = sing[:rank]

    # Matched target coordinates on H_plus = Ran(A).
    y_plus = np.diag(sing_r ** 2).astype(complex)

    def doubled(a: Array) -> Array:
        a = np.asarray(a, dtype=complex)
        z = np.zeros_like(a)
        return np.block([[a, z], [z, a]])

    dcap_plus = hermitian_part(dagger(u_r) @ doubled(s.D_cap) @ u_r)
    coherence_plus = hermitian_part(dagger(u_r) @ doubled(s.coherence) @ u_r)
    emergence_plus = hermitian_part(dagger(u_r) @ doubled(s.emergence) @ u_r)
    formation_plus = hermitian_part(
        coherence_plus + emergence_plus - dcap_plus
    )

    if require_simple_negative_formation:
        eig = np.linalg.eigvalsh(formation_plus)
        if eig.size == 0 or not (eig[0] < -tol):
            return CSRResult(True, "formation_not_negative", None, None, sing_r)
        if eig.size > 1 and not (eig[1] - eig[0] > tol):
            return CSRResult(True, "formation_ground_not_simple", None, None, sing_r)

    packet_target = dagger(u_r) @ (analysis @ s.d)

    # Surviving old persistent subspace seen through the active source support.
    surviving_coordinates = dagger(v_r) @ w
    w_plus = _orthonormal_range(surviving_coordinates, tol=tol)
    if w_plus.shape[1] == 0:
        return CSRResult(True, "persistence_annihilated", None, None, sing_r)

    p_plus = hermitian_part(w_plus @ dagger(w_plus))
    eye = np.eye(rank, dtype=complex)
    p_stable = hermitian_part(eye - p_plus)

    c_plus, _ = neutral_pair(y_plus)
    r_plus = hermitian_part(p_plus + p_stable @ c_plus @ p_stable)
    d_plus = c_plus @ packet_target

    out = QuotientState(
        D_cap=dcap_plus,
        coherence=coherence_plus,
        emergence=emergence_plus,
        d=d_plus,
        Y=y_plus,
        R_C=r_plus,
        P_per=p_plus,
    )
    validate_quotient_state(out, tol=max(tol, 1e-9))

    # Exact finite-category checks for the new axiom.
    if opnorm(r_plus) > 1.0 + 1e-8:
        raise InadmissibleState("CSR recursion is not contractive/power-bounded")

    return CSRResult(
        terminal=False,
        reason="ok",
        state=out,
        persistent_projector=p_plus,
        singular_values=sing_r,
        source_active_frame=v_r,
        target_frame=u_r,
    )


# ---------------------------------------------------------------------------
# Two-density universal operator state
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class UniversalOperatorState:
    """Phase-free finite BFG state for rank-changing continuation.

    formation_density:
        Positive, not necessarily normalized. It carries formation/profile
        magnitude and is used to generate reciprocal loads.

    witness:
        Positive unit-trace identity/continuity witness. It is transported by
        the R4 no-fabrication polar rule and never receives emergent formation
        amplitude.

    P_per:
        Optional exact/numerical certificate for the ordinary orthogonal
        projector onto the persistent subspace. It is derived state/cache, not
        an independent physical axiom.
    """
    D_cap: Array
    coherence: Array
    emergence: Array
    formation_density: Array
    witness: Array
    Y: Array
    R_C: Array
    P_per: Optional[Array] = None

    @property
    def dim(self) -> int:
        return int(np.asarray(self.D_cap).shape[0])

    def formation(self) -> Array:
        return hermitian_part(self.coherence + self.emergence - self.D_cap)


@dataclass(frozen=True)
class UniversalOperatorStep:
    terminal: bool
    reason: str
    state: Optional[UniversalOperatorState]
    retained_witness_mass: float
    inherited_projector: Optional[Array]
    emergent_projector: Optional[Array]
    emergent_seed_projector: Optional[Array]
    singular_values: Optional[Array]


def _trace_real(a: Array, tol: float = 1e-9) -> float:
    z = np.trace(np.asarray(a))
    if abs(float(np.imag(z))) > tol:
        raise InadmissibleState(f"expected real trace, got {z!r}")
    return float(np.real(z))


def _validate_orthogonal_projector(p: Array, tol: float = 1e-9) -> None:
    p = np.asarray(p, dtype=complex)
    if not is_hermitian(p, tol):
        raise InadmissibleState("projector must be Hermitian")
    if opnorm(p @ p - p) > 10 * tol:
        raise InadmissibleState("projector must be idempotent")


def validate_universal_operator_state(
    s: UniversalOperatorState,
    tol: float = 1e-9,
) -> None:
    n = s.dim
    for name, a in (
        ("D_cap", s.D_cap),
        ("coherence", s.coherence),
        ("emergence", s.emergence),
        ("formation_density", s.formation_density),
        ("witness", s.witness),
        ("Y", s.Y),
        ("R_C", s.R_C),
    ):
        if np.asarray(a).shape != (n, n):
            raise InadmissibleState(f"{name} has wrong shape")

    for name, a in (
        ("D_cap", s.D_cap),
        ("coherence", s.coherence),
        ("emergence", s.emergence),
    ):
        if not is_hermitian(a, tol):
            raise InadmissibleState(f"{name} must be Hermitian")

    if not is_psd(s.formation_density, tol):
        raise InadmissibleState("formation_density must be positive semidefinite")
    if _trace_real(s.formation_density) <= tol:
        raise InadmissibleState("formation_density must be nonzero")

    if not is_psd(s.witness, tol):
        raise InadmissibleState("witness must be positive semidefinite")
    if abs(_trace_real(s.witness) - 1.0) > 100 * tol:
        raise InadmissibleState("witness must have unit trace")

    if not is_psd(s.Y, tol):
        raise InadmissibleState("Y must be positive semidefinite")
    # The active-carrier category uses the support of the Gram, so Y should be
    # strictly positive there after a generated step.
    yvals = np.linalg.eigvalsh(hermitian_part(s.Y))
    if yvals.size and float(yvals.min()) <= -tol:
        raise InadmissibleState("Y has a negative eigenvalue")

    if s.P_per is not None:
        p = hermitian_part(np.asarray(s.P_per, dtype=complex))
        _validate_orthogonal_projector(p, tol)
        # Identity witness must be entirely persistent.
        if opnorm(s.witness - p @ s.witness @ p) > 100 * tol:
            raise InadmissibleState("witness must be supported in P_per")


def _ordinary_persistent_projector(
    s: UniversalOperatorState,
    tol: float = 1e-10,
) -> Array:
    if s.P_per is not None:
        p = hermitian_part(np.asarray(s.P_per, dtype=complex))
        _validate_orthogonal_projector(p, max(tol, 1e-9))
        return p
    z = peripheral_eigenbasis(s.R_C, tol=max(tol, 1e-8))
    if z.shape[1] == 0:
        return np.zeros((s.dim, s.dim), dtype=complex)
    return hermitian_part(z @ dagger(z))


def density_reciprocal_analysis(
    y: Array,
    formation_density: Array,
    p_g: Array,
    *,
    tol: float = 1e-12,
) -> tuple[Array, dict]:
    """Density form of the finite BFG reciprocal-load analysis map.

    This exactly extends the rank-one formula rho=d d^*:
      l_C = tr(G P C rho C P^*)
      l_B = tr(G P B rho B P^*)
    """
    y = hermitian_part(np.asarray(y, dtype=complex))
    rho = hermitian_part(np.asarray(formation_density, dtype=complex))
    if not is_psd(y):
        raise InadmissibleState("Y must be positive semidefinite")
    if not is_psd(rho):
        raise InadmissibleState("formation_density must be positive semidefinite")

    c, b = neutral_pair(y)
    g = np.eye(y.shape[0], dtype=complex) + y

    branch_c = hermitian_part(p_g @ c @ rho @ c @ dagger(p_g))
    branch_b = hermitian_part(p_g @ b @ rho @ b @ dagger(p_g))
    load_c = _trace_real(g @ branch_c)
    load_b = _trace_real(g @ branch_b)

    # Exact BFG terminality is triggered only by an exactly vanishing branch
    # energy. A merely tiny positive load is not mathematically zero; if its
    # sign/positivity cannot be resolved at floating precision, stop as a
    # numerical ambiguity rather than claiming physical terminality.
    exact_zero_c = np.count_nonzero(branch_c) == 0
    exact_zero_b = np.count_nonzero(branch_b) == 0
    if exact_zero_c or exact_zero_b:
        raise InadmissibleState("dual_load_zero_terminal")

    if load_c <= tol or load_b <= tol:
        raise InadmissibleState("dual_load_numerical_ambiguity")

    weight_c, weight_b = reciprocal_weights(load_c, load_b)
    a = np.vstack(
        (
            np.sqrt(weight_c) * (p_g @ c),
            np.sqrt(weight_b) * (p_g @ b),
        )
    )
    return a, {
        "C": c,
        "B": b,
        "G": g,
        "load_C": load_c,
        "load_B": load_b,
        "weight_C": weight_c,
        "weight_B": weight_b,
    }


def _rectangular_polar(a: Array, tol: float = 1e-10) -> Array:
    """Polar partial isometry for a rectangular map."""
    return polar_partial_isometry(a, tol=tol)


def _simple_negative_seed(
    k_target: Array,
    emergent_projector: Array,
    *,
    tol: float = 1e-10,
) -> tuple[Optional[Array], Optional[Array], str]:
    """R4 no-choice seed on the emergent target subspace.

    Returns (rho_E, Pi_E, reason).
    If the emergent subspace is zero, both operators are zero and reason='none'.
    """
    k_target = hermitian_part(np.asarray(k_target, dtype=complex))
    e = hermitian_part(np.asarray(emergent_projector, dtype=complex))
    _validate_orthogonal_projector(e, max(tol, 1e-9))
    n = e.shape[0]
    rank_e = int(np.linalg.matrix_rank(e, tol=max(tol, 1e-9)))
    if rank_e == 0:
        z = np.zeros((n, n), dtype=complex)
        return z, z, "none"

    ue = _orthonormal_range(e, tol=tol)
    h_e = hermitian_part(dagger(ue) @ k_target @ ue)
    vals, vecs = np.linalg.eigh(h_e)
    lam0 = float(vals[0])

    if not (lam0 < -tol):
        return None, None, "emergent_ground_not_negative"

    if vals.size > 1 and not (float(vals[1] - vals[0]) > tol):
        return None, None, "emergent_ground_degenerate"

    v0 = vecs[:, [0]]
    pi_local = v0 @ dagger(v0)
    pi_e = hermitian_part(ue @ pi_local @ dagger(ue))
    rho_e = (-lam0) * pi_e
    return rho_e, pi_e, "seeded"


def universal_operator_step(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
) -> UniversalOperatorStep:
    """Rank-aware finite BFG completion candidate.

    Existing/source-level ingredients:
    - positive formation density for phase-free loads;
    - repaired persistence range;
    - neutral pair and reciprocal weights;
    - polar active support;
    - R4 witness transport and emergent no-choice seed.

    Additional BFG-internal completion rules retained from this package:
    - intrinsic-Gram next load on the active carrier;
    - recursion rebuild = persistent identity block plus exact neutral
      contraction on the stable complement.

    Crucial separation:
    emergent rho_E contributes to formation_density, never to witness.
    """
    validate_universal_operator_state(s, tol=max(tol, 1e-9))
    n = s.dim

    p_per = _ordinary_persistent_projector(s, tol=tol)
    if np.linalg.matrix_rank(p_per, tol=max(tol, 1e-9)) == 0:
        return UniversalOperatorStep(
            True, "no_persistent_source", None, 0.0, None, None, None, None
        )

    g = np.eye(n, dtype=complex) + s.Y
    z = _orthonormal_range(p_per, tol=tol)
    p_g = metric_projector(z, g)

    try:
        analysis, _diag = density_reciprocal_analysis(
            s.Y, s.formation_density, p_g, tol=tol
        )
    except InadmissibleState as exc:
        return UniversalOperatorStep(
            True, str(exc), None, 0.0, None, None, None, None
        )

    u, sing, vh = np.linalg.svd(analysis, full_matrices=False)
    if sing.size == 0:
        return UniversalOperatorStep(
            True, "zero_analysis_rank", None, 0.0, None, None, None, sing
        )
    threshold = max(tol, tol * float(sing[0]))
    rank = int(np.count_nonzero(sing > threshold))
    if rank == 0:
        reason = "zero_analysis_rank" if float(sing[0]) == 0.0 else "numerical_rank_ambiguity"
        return UniversalOperatorStep(
            True, reason, None, 0.0, None, None, None, sing
        )

    u_r = u[:, :rank]
    v_r = dagger(vh[:rank, :])
    sing_r = sing[:rank]

    # Active target coordinates.
    y_plus = np.diag(sing_r ** 2).astype(complex)

    def doubled(a: Array) -> Array:
        a = np.asarray(a, dtype=complex)
        zero = np.zeros_like(a)
        return np.block([[a, zero], [zero, a]])

    dcap_plus = hermitian_part(dagger(u_r) @ doubled(s.D_cap) @ u_r)
    coherence_plus = hermitian_part(dagger(u_r) @ doubled(s.coherence) @ u_r)
    emergence_plus = hermitian_part(dagger(u_r) @ doubled(s.emergence) @ u_r)
    k_plus = hermitian_part(coherence_plus + emergence_plus - dcap_plus)

    # R4 polar continuation of the old persistent support into the active target.
    # M: source H -> target active coordinates.
    m = dagger(v_r) @ p_per
    t = _rectangular_polar(m, tol=tol)
    initial_support = hermitian_part(dagger(t) @ t)
    inherited_projector = hermitian_part(t @ dagger(t))
    eye_t = np.eye(rank, dtype=complex)
    emergent_projector = hermitian_part(eye_t - inherited_projector)

    m_keep = _trace_real(initial_support @ s.witness)
    if m_keep <= tol:
        return UniversalOperatorStep(
            True,
            "witness_annihilated",
            None,
            max(0.0, m_keep),
            inherited_projector,
            emergent_projector,
            None,
            sing_r,
        )

    witness_plus = hermitian_part(t @ s.witness @ dagger(t)) / m_keep
    witness_plus = witness_plus / _trace_real(witness_plus)

    # Unnormalized formation inheritance and independent emergent formation seed.
    inherited_formation = hermitian_part(
        t @ s.formation_density @ dagger(t)
    )

    rho_e, pi_e, seed_reason = _simple_negative_seed(
        k_plus, emergent_projector, tol=tol
    )
    if rho_e is None:
        return UniversalOperatorStep(
            True,
            seed_reason,
            None,
            m_keep,
            inherited_projector,
            emergent_projector,
            None,
            sing_r,
        )

    formation_plus = hermitian_part(inherited_formation + rho_e)
    if _trace_real(formation_plus) <= tol:
        return UniversalOperatorStep(
            True,
            "zero_formation_density",
            None,
            m_keep,
            inherited_projector,
            emergent_projector,
            pi_e,
            sing_r,
        )

    # Persistent sector = surviving old persistence + canonically seeded new
    # formation direction. They are orthogonal by construction.
    p_plus = hermitian_part(inherited_projector + pi_e)
    _validate_orthogonal_projector(p_plus, max(tol, 1e-8))

    # BFG-internal CSR recursion completion.
    c_plus, _ = neutral_pair(y_plus)
    p_stable = hermitian_part(eye_t - p_plus)
    r_plus = hermitian_part(p_plus + p_stable @ c_plus @ p_stable)

    state_plus = UniversalOperatorState(
        D_cap=dcap_plus,
        coherence=coherence_plus,
        emergence=emergence_plus,
        formation_density=formation_plus,
        witness=witness_plus,
        Y=y_plus,
        R_C=r_plus,
        P_per=p_plus,
    )
    validate_universal_operator_state(state_plus, tol=max(tol, 1e-8))

    # No-fabrication check: identity witness must have zero emergent support.
    if opnorm(emergent_projector @ witness_plus) > 100 * tol:
        raise InadmissibleState("emergent witness amplitude was fabricated")

    # Generated recursion is power-bounded by construction.
    if opnorm(r_plus) > 1.0 + 1e-8:
        raise InadmissibleState("generated recursion is not contractive")

    return UniversalOperatorStep(
        terminal=False,
        reason="ok",
        state=state_plus,
        retained_witness_mass=m_keep,
        inherited_projector=inherited_projector,
        emergent_projector=emergent_projector,
        emergent_seed_projector=pi_e,
        singular_values=sing_r,
    )


# ---------------------------------------------------------------------------
# Exact BFG Selection / Export formalization
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ClosureGainSelection:
    """Numerical realization of the exact BFG sign selector.

    Exact mathematics:
        Q_retain = 1_(0,inf)(DeltaC)
        Q_export = I - Q_retain

    In floating arithmetic an eigenvalue too close to zero is reported as an
    ambiguity instead of being silently assigned a physical sign.
    """
    ambiguous: bool
    reason: str
    retained_projector: Optional[Array]
    export_projector: Optional[Array]
    eigenvalues: Array


@dataclass(frozen=True)
class WitnessSelectionTransport:
    terminal: bool
    reason: str
    retained_mass: float
    lost_mass: float
    witness_plus: Optional[Array]
    transport: Array
    initial_support: Array
    final_support: Array


def closure_gain_selector(
    delta_c: Array,
    *,
    zero_tol: float = 1e-10,
) -> ClosureGainSelection:
    """Basis-free positive spectral selection for a supplied closure-gain operator.

    This function formalizes the already-stated BFG rule
        retain iff Delta C_A > 0,
        export iff Delta C_A <= 0.

    It does NOT derive Delta C_A itself.
    """
    delta_c = hermitian_part(np.asarray(delta_c, dtype=complex))
    if not is_hermitian(delta_c, max(zero_tol, 1e-9)):
        raise InadmissibleState("closure-gain operator must be Hermitian")

    vals, vecs = np.linalg.eigh(delta_c)

    # Exact zero belongs to export by the source rule. In floating arithmetic,
    # however, a numerically tiny value cannot be certified as exactly zero.
    if np.any(np.abs(vals) <= zero_tol):
        return ClosureGainSelection(
            ambiguous=True,
            reason="closure_gain_sign_ambiguity",
            retained_projector=None,
            export_projector=None,
            eigenvalues=vals,
        )

    positive = vals > 0.0
    if np.any(positive):
        z = vecs[:, positive]
        q_keep = hermitian_part(z @ dagger(z))
    else:
        q_keep = np.zeros_like(delta_c)

    eye = np.eye(delta_c.shape[0], dtype=complex)
    q_export = hermitian_part(eye - q_keep)

    return ClosureGainSelection(
        ambiguous=False,
        reason="ok",
        retained_projector=q_keep,
        export_projector=q_export,
        eigenvalues=vals,
    )


def witness_transport_between_projectors(
    witness: Array,
    q_minus: Array,
    q_plus: Array,
    *,
    zero_tol: float = 1e-12,
) -> WitnessSelectionTransport:
    """R4 polar witness transport for exact source/target support projectors."""
    witness = hermitian_part(np.asarray(witness, dtype=complex))
    q_minus = hermitian_part(np.asarray(q_minus, dtype=complex))
    q_plus = hermitian_part(np.asarray(q_plus, dtype=complex))

    _validate_orthogonal_projector(q_minus, 1e-8)
    _validate_orthogonal_projector(q_plus, 1e-8)

    if not is_psd(witness):
        raise InadmissibleState("witness must be positive semidefinite")
    tr = _trace_real(witness)
    if abs(tr - 1.0) > 1e-8:
        raise InadmissibleState("witness must have unit trace")
    if opnorm(witness - q_minus @ witness @ q_minus) > 1e-8:
        raise InadmissibleState("witness must be supported in source projector")

    x = q_plus @ q_minus
    t = polar_partial_isometry(x, tol=zero_tol)
    s_minus = hermitian_part(dagger(t) @ t)
    s_plus = hermitian_part(t @ dagger(t))

    m_keep = _trace_real(s_minus @ witness)
    m_keep = float(np.clip(m_keep, 0.0, 1.0))
    m_lost = 1.0 - m_keep

    if m_keep <= zero_tol:
        return WitnessSelectionTransport(
            terminal=True,
            reason="witness_annihilated",
            retained_mass=0.0,
            lost_mass=1.0,
            witness_plus=None,
            transport=t,
            initial_support=s_minus,
            final_support=s_plus,
        )

    rho_plus = hermitian_part(t @ witness @ dagger(t)) / m_keep
    rho_plus = rho_plus / _trace_real(rho_plus)

    return WitnessSelectionTransport(
        terminal=False,
        reason="ok",
        retained_mass=m_keep,
        lost_mass=m_lost,
        witness_plus=rho_plus,
        transport=t,
        initial_support=s_minus,
        final_support=s_plus,
    )


# ---------------------------------------------------------------------------
# Neutral-Contrast Selection Principle (NCS)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class NeutralContrastSelection:
    ambiguous: bool
    reason: str
    contrast: Array
    retained_projector: Optional[Array]
    export_projector: Optional[Array]
    load_eigenvalues: Array


@dataclass(frozen=True)
class NeutralContrastStep:
    terminal: bool
    reason: str
    state: Optional[UniversalOperatorState]
    retained_witness_mass: float
    selected_projector: Optional[Array]
    persistent_projector: Optional[Array]
    export_projector: Optional[Array]
    emergent_seed_projector: Optional[Array]
    singular_values: Optional[Array]


def neutral_contrast(y: Array) -> Array:
    """Exact BFG neutral contrast Z=C_N(Y)-B_N(Y).

    Z = (I-Y)(I+Y)^-1.
    """
    y = hermitian_part(np.asarray(y, dtype=complex))
    if not is_psd(y):
        raise InadmissibleState("Y must be positive semidefinite")
    c, b = neutral_pair(y)
    return hermitian_part(c - b)


def neutral_contrast_selector(
    y: Array,
    *,
    boundary_tol: float = 1e-10,
) -> NeutralContrastSelection:
    """Exact selector Q_keep = 1_(0,inf)(Z) = 1_[0,1)(Y).

    In exact mathematics the boundary is y=1 and belongs to export because
    retention requires strictly positive neutral contrast. In floating
    arithmetic, eigenvalues too close to 1 are reported as ambiguity.
    """
    y = hermitian_part(np.asarray(y, dtype=complex))
    if not is_psd(y):
        raise InadmissibleState("Y must be positive semidefinite")

    vals, vecs = np.linalg.eigh(y)
    zvals = (1.0 - vals) / (1.0 + vals)
    z = hermitian_part((vecs * zvals) @ dagger(vecs))

    if np.any(np.abs(vals - 1.0) <= boundary_tol):
        return NeutralContrastSelection(
            ambiguous=True,
            reason="neutral_contrast_boundary_ambiguity",
            contrast=z,
            retained_projector=None,
            export_projector=None,
            load_eigenvalues=vals,
        )

    keep = vals < 1.0
    if np.any(keep):
        u = vecs[:, keep]
        q_keep = hermitian_part(u @ dagger(u))
    else:
        q_keep = np.zeros_like(y)

    eye = np.eye(y.shape[0], dtype=complex)
    q_export = hermitian_part(eye - q_keep)

    return NeutralContrastSelection(
        ambiguous=False,
        reason="ok",
        contrast=z,
        retained_projector=q_keep,
        export_projector=q_export,
        load_eigenvalues=vals,
    )


def neutral_contrast_universal_step(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
    boundary_tol: float = 1e-10,
) -> NeutralContrastStep:
    """Rank-changing finite completion using the BFG neutral contrast selector.

    Epistemic status:
    - C_N, B_N and Z=C_N-B_N are canonical source BFG objects.
    - The identification "closure-positive iff Z>0" is the explicit new
      Neutral-Contrast Selection Principle of this package.
    - intrinsic-Gram Y_plus and neutral transverse recursion remain the already
      declared BFG-internal completion rules.

    The active target carrier remains the full polar carrier. Selection acts on
    which target directions are closure-positive/persistent candidates; exported
    directions remain as strictly stable transient directions.
    """
    validate_universal_operator_state(s, tol=max(tol, 1e-9))
    n = s.dim

    p_old = _ordinary_persistent_projector(s, tol=tol)
    if np.linalg.matrix_rank(p_old, tol=max(tol, 1e-9)) == 0:
        return NeutralContrastStep(
            True, "no_persistent_source", None, 0.0, None, None, None, None, None
        )

    g = np.eye(n, dtype=complex) + s.Y
    z_old = _orthonormal_range(p_old, tol=tol)
    p_g = metric_projector(z_old, g)

    try:
        analysis, _diag = density_reciprocal_analysis(
            s.Y, s.formation_density, p_g, tol=tol
        )
    except InadmissibleState as exc:
        return NeutralContrastStep(
            True, str(exc), None, 0.0, None, None, None, None, None
        )

    u, sing, vh = np.linalg.svd(analysis, full_matrices=False)
    if sing.size == 0:
        return NeutralContrastStep(
            True, "zero_analysis_rank", None, 0.0, None, None, None, None, sing
        )
    threshold = max(tol, tol * float(sing[0]))
    rank = int(np.count_nonzero(sing > threshold))
    if rank == 0:
        reason = "zero_analysis_rank" if float(sing[0]) == 0.0 else "numerical_rank_ambiguity"
        return NeutralContrastStep(
            True, reason, None, 0.0, None, None, None, None, sing
        )

    u_r = u[:, :rank]
    v_r = dagger(vh[:rank, :])
    sing_r = sing[:rank]

    # Selected intrinsic-Gram completion.
    y_pre = np.diag(sing_r ** 2).astype(complex)

    selection = neutral_contrast_selector(y_pre, boundary_tol=boundary_tol)
    if selection.ambiguous:
        return NeutralContrastStep(
            True,
            selection.reason,
            None,
            0.0,
            None,
            None,
            None,
            None,
            sing_r,
        )

    q_sel = selection.retained_projector
    q_export = selection.export_projector
    if np.linalg.matrix_rank(q_sel, tol=max(tol, 1e-9)) == 0:
        return NeutralContrastStep(
            True,
            "no_closure_positive_target_sector",
            None,
            0.0,
            q_sel,
            None,
            q_export,
            None,
            sing_r,
        )

    def doubled(a: Array) -> Array:
        a = np.asarray(a, dtype=complex)
        z = np.zeros_like(a)
        return np.block([[a, z], [z, a]])

    dcap_plus = hermitian_part(dagger(u_r) @ doubled(s.D_cap) @ u_r)
    coherence_plus = hermitian_part(dagger(u_r) @ doubled(s.coherence) @ u_r)
    emergence_plus = hermitian_part(dagger(u_r) @ doubled(s.emergence) @ u_r)
    k_plus = hermitian_part(coherence_plus + emergence_plus - dcap_plus)

    # Exact R4 overlap: source persistent sector -> selected target sector.
    overlap = q_sel @ dagger(v_r) @ p_old
    t = _rectangular_polar(overlap, tol=tol)
    s_minus = hermitian_part(dagger(t) @ t)
    s_plus = hermitian_part(t @ dagger(t))

    m_keep = _trace_real(s_minus @ s.witness)
    m_keep = float(np.clip(m_keep, 0.0, 1.0))
    if m_keep <= tol:
        return NeutralContrastStep(
            True,
            "witness_annihilated",
            None,
            0.0,
            q_sel,
            None,
            q_export,
            None,
            sing_r,
        )

    witness_plus = hermitian_part(t @ s.witness @ dagger(t)) / m_keep
    witness_plus = witness_plus / _trace_real(witness_plus)

    inherited_formation = hermitian_part(
        t @ s.formation_density @ dagger(t)
    )

    # New closure-positive selected directions that have no inherited witness.
    emergent_selected = hermitian_part(q_sel - s_plus)
    _validate_orthogonal_projector(emergent_selected, max(tol, 1e-8))

    rho_e, pi_e, seed_reason = _simple_negative_seed(
        k_plus, emergent_selected, tol=tol
    )
    if rho_e is None:
        return NeutralContrastStep(
            True,
            seed_reason,
            None,
            m_keep,
            q_sel,
            None,
            q_export,
            None,
            sing_r,
        )

    formation_plus = hermitian_part(inherited_formation + rho_e)
    if _trace_real(formation_plus) <= tol:
        return NeutralContrastStep(
            True,
            "zero_formation_density",
            None,
            m_keep,
            q_sel,
            None,
            q_export,
            pi_e,
            sing_r,
        )

    # Persist exactly what is inherited plus the unique formation seed.
    p_plus = hermitian_part(s_plus + pi_e)
    _validate_orthogonal_projector(p_plus, max(tol, 1e-8))

    # Existing BFG-internal neutral transverse recursion completion.
    c_plus, _ = neutral_pair(y_pre)
    eye = np.eye(rank, dtype=complex)
    p_stable = hermitian_part(eye - p_plus)
    r_plus = hermitian_part(p_plus + p_stable @ c_plus @ p_stable)

    state_plus = UniversalOperatorState(
        D_cap=dcap_plus,
        coherence=coherence_plus,
        emergence=emergence_plus,
        formation_density=formation_plus,
        witness=witness_plus,
        Y=y_pre,
        R_C=r_plus,
        P_per=p_plus,
    )
    validate_universal_operator_state(state_plus, tol=max(tol, 1e-8))

    if opnorm(emergent_selected @ witness_plus) > 100 * tol:
        raise InadmissibleState("selection fabricated emergent witness amplitude")
    if opnorm(r_plus) > 1.0 + 1e-8:
        raise InadmissibleState("generated recursion is not power bounded")

    return NeutralContrastStep(
        terminal=False,
        reason="ok",
        state=state_plus,
        retained_witness_mass=m_keep,
        selected_projector=q_sel,
        persistent_projector=p_plus,
        export_projector=q_export,
        emergent_seed_projector=pi_e,
        singular_values=sing_r,
    )


# ---------------------------------------------------------------------------
# Official living finite Universal State Update candidate
# ---------------------------------------------------------------------------

def _runtime_stop_semantics(reason: str) -> str:
    """Classify a runtime halt without confusing numerics with BFG terminality."""
    if "ambiguity" in reason:
        return "numerical_unresolved"
    exact_terminal = {
        "dual_load_zero_terminal",
        "no_persistent_source",
        "no_closure_positive_source_sector",
        "witness_annihilated",
        "formation_selection_annihilated",
        "zero_analysis_rank",
        "zero_formation_density",
        "emergent_ground_not_negative",
        "emergent_ground_degenerate",
    }
    if reason in exact_terminal:
        return "exact_terminal_or_no_choice_failure"
    if reason == "ok":
        return "successful_step"
    return "runtime_stop_unclassified"


@dataclass(frozen=True)
class BFGUniversalUpdateResult:
    terminal: bool
    reason: str
    state: Optional[UniversalOperatorState]
    diagnostics: dict


def bfg_universal_state_update(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
    boundary_tol: float = 1e-10,
) -> BFGUniversalUpdateResult:
    """Living finite BFG-only universal-update candidate.

    Fundamental physical content used:
      1. BFG formation capacities;
      2. exact neutral resolvents C_N/B_N;
      3. density reciprocal loads;
      4. polar reclosure;
      5. R4 witness/no-choice formation transport;
      6. Neutral-Contrast Selection Principle:
             closure-positive iff Z=C_N-B_N > 0;
      7. intrinsic-Gram next load (explicit BFG-internal completion rule);
      8. neutral transverse recursive rebuild (explicit BFG-internal completion rule).

    No external sector equation is used.

    This function is a candidate master law, not a claim that the historical
    corpus already forced every completion principle uniquely.
    """
    out = selection_first_universal_step(
        s,
        tol=tol,
        boundary_tol=boundary_tol,
    )

    diag = {
        "law": "BFG selection-first neutral-contrast finite universal update candidate",
        "epistemic_status": "conditional on declared BFG-internal completion principles",
        "terminal": out.terminal,
        "reason": out.reason,
        "runtime_stop_semantics": _runtime_stop_semantics(out.reason),
        "retained_witness_mass": out.retained_witness_mass,
        "persistent_rank_before": out.persistent_rank_before,
        "persistent_rank_after_selection": out.persistent_rank_after_selection,
        "persistent_rank_after_reclosure": out.persistent_rank_after_reclosure,
        "active_rank_after_reclosure": out.active_rank_after_reclosure,
    }

    if out.source_export_projector is not None:
        diag["source_export_rank"] = int(
            np.linalg.matrix_rank(out.source_export_projector, tol=max(tol, 1e-9))
        )

    return BFGUniversalUpdateResult(
        terminal=out.terminal,
        reason=out.reason,
        state=out.state,
        diagnostics=diag,
    )


# ---------------------------------------------------------------------------
# Selection-first universal update (A -> S_A -> T_A ordering)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SelectionFirstStep:
    terminal: bool
    reason: str
    state: Optional[UniversalOperatorState]
    source_selected_projector: Optional[Array]
    source_export_projector: Optional[Array]
    retained_witness_mass: float
    persistent_rank_before: int
    persistent_rank_after_selection: int
    persistent_rank_after_reclosure: int
    active_rank_after_reclosure: int


def selection_first_universal_step(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
    boundary_tol: float = 1e-10,
) -> SelectionFirstStep:
    """Finite BFG candidate respecting K -> C -> A -> S_A -> T_A ordering.

    Stage 1: current-state Neutral-Contrast Selection acts on the already
             persistent/attractor-supported source structure.
    Stage 2: R4 polar transport records identity/formation loss.
    Stage 3: the surviving source sector generates the next cross-fed carrier.
    Stage 4: intrinsic-Gram, emergent no-choice formation, and neutral recursive
             rebuild close the successor.

    This ordering can produce genuine persistent-rank loss without a numerical
    target-window parameter.
    """
    validate_universal_operator_state(s, tol=max(tol, 1e-9))
    n = s.dim

    p_old = _ordinary_persistent_projector(s, tol=tol)
    rank_old = int(np.linalg.matrix_rank(p_old, tol=max(tol, 1e-9)))
    if rank_old == 0:
        return SelectionFirstStep(
            True, "no_persistent_source", None, None, None, 0.0,
            rank_old, 0, 0, 0
        )

    # A -> S_A: exact selection on CURRENT BFG neutral load.
    sel = neutral_contrast_selector(s.Y, boundary_tol=boundary_tol)
    if sel.ambiguous:
        return SelectionFirstStep(
            True, sel.reason, None, None, None, 0.0,
            rank_old, 0, 0, 0
        )

    q_keep = sel.retained_projector
    q_export = sel.export_projector
    if np.linalg.matrix_rank(q_keep, tol=max(tol, 1e-9)) == 0:
        return SelectionFirstStep(
            True, "no_closure_positive_source_sector", None,
            q_keep, q_export, 0.0, rank_old, 0, 0, 0
        )

    # S_A -> T_A: exact R4 polar selection transport in the current carrier.
    selected = witness_transport_between_projectors(
        s.witness, p_old, q_keep, zero_tol=tol
    )
    p_selected = selected.final_support
    rank_selected = int(
        np.linalg.matrix_rank(p_selected, tol=max(tol, 1e-9))
    )
    if selected.terminal or rank_selected == 0:
        return SelectionFirstStep(
            True, selected.reason, None, p_selected, q_export,
            selected.retained_mass, rank_old, rank_selected, 0, 0
        )

    rho_w_selected = selected.witness_plus
    t_sel = selected.transport

    # Formation is transported without normalization; exported source formation
    # is not reintroduced into the selected closure.
    rho_f_selected = hermitian_part(
        t_sel @ s.formation_density @ dagger(t_sel)
    )
    if _trace_real(rho_f_selected) <= tol:
        return SelectionFirstStep(
            True, "formation_selection_annihilated", None,
            p_selected, q_export, selected.retained_mass,
            rank_old, rank_selected, 0, 0
        )

    # Generate the next packet only from the closure-positive surviving source.
    g = np.eye(n, dtype=complex) + s.Y
    z_sel = _orthonormal_range(p_selected, tol=tol)
    p_g = metric_projector(z_sel, g)

    try:
        analysis, _diag = density_reciprocal_analysis(
            s.Y, rho_f_selected, p_g, tol=tol
        )
    except InadmissibleState as exc:
        return SelectionFirstStep(
            True, str(exc), None, p_selected, q_export,
            selected.retained_mass, rank_old, rank_selected, 0, 0
        )

    u, sing, vh = np.linalg.svd(analysis, full_matrices=False)
    if sing.size == 0:
        return SelectionFirstStep(
            True, "zero_analysis_rank", None, p_selected, q_export,
            selected.retained_mass, rank_old, rank_selected, 0, 0
        )
    threshold = max(tol, tol * float(sing[0]))
    rank = int(np.count_nonzero(sing > threshold))
    if rank == 0:
        reason = "zero_analysis_rank" if float(sing[0]) == 0.0 else "numerical_rank_ambiguity"
        return SelectionFirstStep(
            True, reason, None, p_selected, q_export,
            selected.retained_mass, rank_old, rank_selected, 0, 0
        )

    u_r = u[:, :rank]
    v_r = dagger(vh[:rank, :])
    sing_r = sing[:rank]
    y_plus = np.diag(sing_r ** 2).astype(complex)

    def doubled(a: Array) -> Array:
        a = np.asarray(a, dtype=complex)
        zero = np.zeros_like(a)
        return np.block([[a, zero], [zero, a]])

    dcap_plus = hermitian_part(dagger(u_r) @ doubled(s.D_cap) @ u_r)
    coherence_plus = hermitian_part(dagger(u_r) @ doubled(s.coherence) @ u_r)
    emergence_plus = hermitian_part(dagger(u_r) @ doubled(s.emergence) @ u_r)
    k_plus = hermitian_part(coherence_plus + emergence_plus - dcap_plus)

    # Polar transport from the selected persistent source into the full active
    # successor carrier. By the persistence-inclusion theorem this should
    # normally retain all selected identity mass exactly.
    overlap = dagger(v_r) @ p_selected
    t_next = _rectangular_polar(overlap, tol=tol)
    s2_minus = hermitian_part(dagger(t_next) @ t_next)
    s2_plus = hermitian_part(t_next @ dagger(t_next))

    m2 = _trace_real(s2_minus @ rho_w_selected)
    m2 = float(np.clip(m2, 0.0, 1.0))
    if m2 <= tol:
        return SelectionFirstStep(
            True, "reclosure_witness_annihilated", None,
            p_selected, q_export, 0.0,
            rank_old, rank_selected, 0, rank
        )

    rho_w_plus = hermitian_part(
        t_next @ rho_w_selected @ dagger(t_next)
    ) / m2
    rho_w_plus = rho_w_plus / _trace_real(rho_w_plus)

    inherited_formation = hermitian_part(
        t_next @ rho_f_selected @ dagger(t_next)
    )

    eye_t = np.eye(rank, dtype=complex)
    emergent = hermitian_part(eye_t - s2_plus)
    _validate_orthogonal_projector(emergent, max(tol, 1e-8))

    rho_e, pi_e, seed_reason = _simple_negative_seed(
        k_plus, emergent, tol=tol
    )
    if rho_e is None:
        return SelectionFirstStep(
            True, seed_reason, None, p_selected, q_export,
            selected.retained_mass * m2,
            rank_old, rank_selected, 0, rank
        )

    rho_f_plus = hermitian_part(inherited_formation + rho_e)
    if _trace_real(rho_f_plus) <= tol:
        return SelectionFirstStep(
            True, "zero_formation_density", None, p_selected, q_export,
            selected.retained_mass * m2,
            rank_old, rank_selected, 0, rank
        )

    p_plus = hermitian_part(s2_plus + pi_e)
    _validate_orthogonal_projector(p_plus, max(tol, 1e-8))
    rank_plus = int(np.linalg.matrix_rank(p_plus, tol=max(tol, 1e-9)))

    c_plus, _ = neutral_pair(y_plus)
    p_stable = hermitian_part(eye_t - p_plus)
    r_plus = hermitian_part(p_plus + p_stable @ c_plus @ p_stable)

    state_plus = UniversalOperatorState(
        D_cap=dcap_plus,
        coherence=coherence_plus,
        emergence=emergence_plus,
        formation_density=rho_f_plus,
        witness=rho_w_plus,
        Y=y_plus,
        R_C=r_plus,
        P_per=p_plus,
    )
    validate_universal_operator_state(state_plus, tol=max(tol, 1e-8))

    if opnorm(r_plus) > 1.0 + 1e-8:
        raise InadmissibleState("selection-first recursion is not power bounded")

    return SelectionFirstStep(
        terminal=False,
        reason="ok",
        state=state_plus,
        source_selected_projector=p_selected,
        source_export_projector=q_export,
        retained_witness_mass=selected.retained_mass * m2,
        persistent_rank_before=rank_old,
        persistent_rank_after_selection=rank_selected,
        persistent_rank_after_reclosure=rank_plus,
        active_rank_after_reclosure=rank,
    )


# ---------------------------------------------------------------------------
# Exact-forward-orbit diagnostics
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class GeneratedStateCertificate:
    y_min: float
    persistent_rank: int
    formation_support_residual: float
    witness_support_residual: float
    load_C: float
    load_B: float


def raw_density_loads(
    y: Array,
    formation_density: Array,
    p_g: Array,
) -> tuple[float, float]:
    """Return the two mathematical load expressions without a zero threshold."""
    y = hermitian_part(np.asarray(y, dtype=complex))
    rho = hermitian_part(np.asarray(formation_density, dtype=complex))
    c, b = neutral_pair(y)
    g = np.eye(y.shape[0], dtype=complex) + y
    branch_c = hermitian_part(p_g @ c @ rho @ c @ dagger(p_g))
    branch_b = hermitian_part(p_g @ b @ rho @ b @ dagger(p_g))
    return _trace_real(g @ branch_c), _trace_real(g @ branch_b)


def generated_state_certificate(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
) -> GeneratedStateCertificate:
    """Numerical certificate for the post-reclosure invariant class.

    Exact theorem represented:
      - Y is strictly positive on the reduced active carrier;
      - generated formation and identity witness are supported in P_per;
      - for nonzero formation on P_per and Y>0, both reciprocal loads are >0.
    """
    validate_universal_operator_state(s, tol=max(tol, 1e-9))
    p = _ordinary_persistent_projector(s, tol=tol)
    z = _orthonormal_range(p, tol=tol)
    if z.shape[1] == 0:
        raise InadmissibleState("no persistent range")
    g = np.eye(s.dim, dtype=complex) + s.Y
    p_g = metric_projector(z, g)
    load_c, load_b = raw_density_loads(s.Y, s.formation_density, p_g)

    yvals = np.linalg.eigvalsh(hermitian_part(s.Y))
    y_min = float(yvals.min()) if yvals.size else float("inf")
    formation_res = opnorm(
        s.formation_density - p @ s.formation_density @ p
    )
    witness_res = opnorm(s.witness - p @ s.witness @ p)

    return GeneratedStateCertificate(
        y_min=y_min,
        persistent_rank=int(np.linalg.matrix_rank(p, tol=max(tol, 1e-9))),
        formation_support_residual=formation_res,
        witness_support_residual=witness_res,
        load_C=float(load_c),
        load_B=float(load_b),
    )


def scalar_intrinsic_gram_quadratic_bounds(y: float) -> tuple[float, float, float]:
    """Bounds for the scalar intrinsic-Gram map on 0<y<=1.

    y^2/4 <= f(y) <= 2 y^2.
    """
    y = float(y)
    if not (0.0 < y <= 1.0):
        raise ValueError("requires 0 < y <= 1")
    exact = scalar_intrinsic_gram_map(y)
    return y*y/4.0, exact, 2.0*y*y


# ---------------------------------------------------------------------------
# Closure-depth coordinate H = -log(Y)
# ---------------------------------------------------------------------------

def closure_depth(y: Array, *, tol: float = 1e-14) -> Array:
    """Derived Hermitian coordinate H=-log(Y) for strictly positive Y."""
    y = hermitian_part(np.asarray(y, dtype=complex))
    vals, vecs = np.linalg.eigh(y)
    if vals.size and float(vals.min()) <= tol:
        raise InadmissibleState("closure depth requires strictly positive Y")
    hvals = -np.log(vals)
    return hermitian_part((vecs * hvals) @ dagger(vecs))


def load_from_closure_depth(h: Array) -> Array:
    """Inverse coordinate Y=exp(-H)."""
    h = hermitian_part(np.asarray(h, dtype=complex))
    vals, vecs = np.linalg.eigh(h)
    yvals = np.exp(-vals)
    return hermitian_part((vecs * yvals) @ dagger(vecs))


def neutral_from_closure_depth(h: Array) -> tuple[Array, Array, Array]:
    """Return (C_N, B_N, Z) directly from H=-log(Y).

    Exact functional identities:
        Z = tanh(H/2)
        C = (I+Z)/2
        B = (I-Z)/2
    """
    h = hermitian_part(np.asarray(h, dtype=complex))
    vals, vecs = np.linalg.eigh(h)
    zvals = np.tanh(vals / 2.0)
    z = hermitian_part((vecs * zvals) @ dagger(vecs))
    eye = np.eye(h.shape[0], dtype=complex)
    c = hermitian_part((eye + z) / 2.0)
    b = hermitian_part((eye - z) / 2.0)
    return c, b, z


def scalar_closure_depth_update(h: float) -> float:
    """Scalar intrinsic-Gram update written in H=-log(y) coordinates."""
    h = float(h)
    # stable log1p form of
    # 2h - log2 + 2 log(1+e^-h) + log(1+e^-2h)
    return (
        2.0*h
        - np.log(2.0)
        + 2.0*np.log1p(np.exp(-h))
        + np.log1p(np.exp(-2.0*h))
    )


def scalar_renormalized_depth(
    h0: float,
    steps: int,
) -> float:
    """Return 2^-steps H_steps for the scalar closure-depth orbit."""
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    h = float(h0)
    for _ in range(steps):
        h = scalar_closure_depth_update(h)
    return h / (2.0 ** steps)


# ---------------------------------------------------------------------------
# Exact continuous embedding of the selected scalar intrinsic-Gram sector
# ---------------------------------------------------------------------------

def scalar_bottcher_depth_from_h(
    h: float,
    *,
    iterations: int = 60,
) -> float:
    """Renormalized closure-depth / logarithmic Böttcher coordinate.

    theta(h) = lim_{n->inf} 2^-n F_H^n(h),
    where F_H is the exact scalar closure-depth update.

    Domain used here: h >= 0, corresponding to the selected scalar sector
    0 < y <= 1.
    """
    h = float(h)
    if h < 0:
        raise ValueError("selected scalar sector requires h >= 0")
    if iterations < 1:
        raise ValueError("iterations must be positive")

    x = h
    scale = 1.0
    for _ in range(iterations):
        x = scalar_closure_depth_update(x)
        scale *= 2.0
    return x / scale


def scalar_bottcher_depth(
    y: float,
    *,
    iterations: int = 60,
) -> float:
    """theta(y) on 0<y<=1."""
    y = float(y)
    if not (0.0 < y <= 1.0):
        raise ValueError("selected scalar sector requires 0 < y <= 1")
    return scalar_bottcher_depth_from_h(
        -np.log(y),
        iterations=iterations,
    )


def scalar_bottcher_coordinate(
    y: float,
    *,
    iterations: int = 60,
) -> float:
    """Böttcher coordinate phi(y)=exp(-theta(y)).

    It is normalized by phi(y)~2y as y->0+ and satisfies
        phi(f(y)) = phi(y)^2
    in the selected scalar sector.
    """
    theta = scalar_bottcher_depth(y, iterations=iterations)
    return float(np.exp(-theta))


def _invert_scalar_bottcher_depth_h(
    target_theta: float,
    *,
    iterations: int = 60,
    bisect_steps: int = 100,
) -> float:
    """Invert h -> theta(h) on h>=0 by monotone bisection."""
    target_theta = float(target_theta)
    theta0 = scalar_bottcher_depth_from_h(0.0, iterations=iterations)
    if target_theta < theta0:
        raise ValueError("target is outside the selected scalar Böttcher range")

    lo = 0.0
    # Since theta(h) ~ h-log(2) for large h, this is a safe practical bracket.
    hi = max(1.0, target_theta + np.log(2.0) + 2.0)
    while scalar_bottcher_depth_from_h(hi, iterations=iterations) < target_theta:
        hi *= 2.0

    for _ in range(bisect_steps):
        mid = (lo + hi) / 2.0
        val = scalar_bottcher_depth_from_h(mid, iterations=iterations)
        if val < target_theta:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def scalar_recursive_time_flow_h(
    h0: float,
    tau: float,
    *,
    iterations: int = 60,
) -> float:
    """Exact continuous embedding in closure-depth coordinates.

    Define theta(h(tau)) = exp(tau) theta(h0).
    One discrete BFG scalar step is tau=log(2).
    """
    h0 = float(h0)
    tau = float(tau)
    if h0 < 0:
        raise ValueError("selected scalar sector requires h0 >= 0")
    if tau < 0:
        raise ValueError("forward recursive time requires tau >= 0")

    theta0 = scalar_bottcher_depth_from_h(h0, iterations=iterations)
    target = np.exp(tau) * theta0
    return _invert_scalar_bottcher_depth_h(
        target,
        iterations=iterations,
    )


def scalar_recursive_time_flow_y(
    y0: float,
    tau: float,
    *,
    iterations: int = 60,
) -> float:
    """Continuous selected-scalar BFG flow in the original load coordinate."""
    y0 = float(y0)
    if not (0.0 < y0 <= 1.0):
        raise ValueError("selected scalar sector requires 0 < y0 <= 1")
    h = scalar_recursive_time_flow_h(
        -np.log(y0),
        tau,
        iterations=iterations,
    )
    return float(np.exp(-h))


def scalar_recursive_time_generator_h(
    h: float,
    *,
    iterations: int = 60,
    diff_step: float = 1e-6,
) -> float:
    """Generator v_H(h)=theta(h)/theta'(h) of the exact continuous embedding.

    theta' is evaluated numerically; the mathematical definition is exact.
    """
    h = float(h)
    if h < 0:
        raise ValueError("selected scalar sector requires h >= 0")
    eps = diff_step * max(1.0, abs(h))
    if h > eps:
        tp = scalar_bottcher_depth_from_h(h + eps, iterations=iterations)
        tm = scalar_bottcher_depth_from_h(h - eps, iterations=iterations)
        deriv = (tp - tm) / (2.0 * eps)
    else:
        tp = scalar_bottcher_depth_from_h(h + eps, iterations=iterations)
        t0 = scalar_bottcher_depth_from_h(h, iterations=iterations)
        deriv = (tp - t0) / eps
    theta = scalar_bottcher_depth_from_h(h, iterations=iterations)
    if deriv <= 0:
        raise InadmissibleState("Böttcher depth must be strictly increasing")
    return float(theta / deriv)


def scalar_recursive_time_generator_y(
    y: float,
    *,
    iterations: int = 60,
    diff_step: float = 1e-6,
) -> float:
    """Generator dy/dtau of the exact continuous scalar embedding."""
    y = float(y)
    if not (0.0 < y <= 1.0):
        raise ValueError("selected scalar sector requires 0 < y <= 1")
    h = -np.log(y)
    vh = scalar_recursive_time_generator_h(
        h,
        iterations=iterations,
        diff_step=diff_step,
    )
    return float(-y * vh)


# ---------------------------------------------------------------------------
# Fixed-stratum operator Böttcher semigroup
# ---------------------------------------------------------------------------

def _spectral_apply_hermitian(a: Array, scalar_fn) -> Array:
    """Apply a real scalar function to a Hermitian matrix by spectral calculus."""
    a = hermitian_part(np.asarray(a, dtype=complex))
    vals, vecs = np.linalg.eigh(a)
    out = np.array([scalar_fn(float(x)) for x in vals], dtype=float)
    return hermitian_part((vecs * out) @ dagger(vecs))


def operator_scalar_bfg_map(y: Array) -> Array:
    """Modewise scalar intrinsic-Gram map f(Y) by spectral functional calculus.

    This is only the fixed-stratum commuting/operator lift. It is NOT the full
    noncommuting BFG master update.
    """
    y = hermitian_part(np.asarray(y, dtype=complex))
    vals = np.linalg.eigvalsh(y)
    if vals.size and (float(vals.min()) <= 0.0 or float(vals.max()) > 1.0 + 1e-12):
        raise InadmissibleState("operator scalar lift requires 0 < Y <= I")
    return _spectral_apply_hermitian(y, scalar_intrinsic_gram_map)


def operator_bottcher_depth(
    y: Array,
    *,
    iterations: int = 60,
) -> Array:
    """Theta(Y)=theta(Y) on a fixed selected spectral stratum 0<Y<=I."""
    y = hermitian_part(np.asarray(y, dtype=complex))
    vals = np.linalg.eigvalsh(y)
    if vals.size and (float(vals.min()) <= 0.0 or float(vals.max()) > 1.0 + 1e-12):
        raise InadmissibleState("operator Böttcher depth requires 0 < Y <= I")
    return _spectral_apply_hermitian(
        y,
        lambda x: scalar_bottcher_depth(x, iterations=iterations),
    )


def operator_bottcher_coordinate(
    y: Array,
    *,
    iterations: int = 60,
) -> Array:
    """Phi(Y)=exp(-Theta(Y)) on the fixed selected spectral stratum."""
    theta = operator_bottcher_depth(y, iterations=iterations)
    vals, vecs = np.linalg.eigh(theta)
    out = np.exp(-vals)
    return hermitian_part((vecs * out) @ dagger(vecs))


def operator_recursive_time_flow(
    y0: Array,
    tau: float,
    *,
    iterations: int = 60,
) -> Array:
    """Exact modewise continuous embedding for a fixed commuting stratum.

    Defined spectrally by scalar F_tau on each eigenvalue. The initial spectral
    projectors are preserved. Hence this is a fixed-stratum semigroup, not a
    rank-changing master flow.
    """
    tau = float(tau)
    if tau < 0:
        raise ValueError("forward recursive time requires tau >= 0")
    y0 = hermitian_part(np.asarray(y0, dtype=complex))
    vals, vecs = np.linalg.eigh(y0)
    if vals.size and (float(vals.min()) <= 0.0 or float(vals.max()) > 1.0 + 1e-12):
        raise InadmissibleState("operator flow requires 0 < Y <= I")
    flowed = np.array([
        scalar_recursive_time_flow_y(float(x), tau, iterations=iterations)
        for x in vals
    ])
    return hermitian_part((vecs * flowed) @ dagger(vecs))


def operator_recursive_time_generator(
    y: Array,
    *,
    iterations: int = 60,
    diff_step: float = 1e-6,
) -> Array:
    """Fixed-stratum operator generator dY/dtau=v(Y) by spectral calculus."""
    y = hermitian_part(np.asarray(y, dtype=complex))
    vals, vecs = np.linalg.eigh(y)
    if vals.size and (float(vals.min()) <= 0.0 or float(vals.max()) > 1.0 + 1e-12):
        raise InadmissibleState("operator generator requires 0 < Y <= I")
    v = np.array([
        scalar_recursive_time_generator_y(
            float(x), iterations=iterations, diff_step=diff_step
        )
        for x in vals
    ])
    return hermitian_part((vecs * v) @ dagger(vecs))


def operator_commutator(a: Array, b: Array) -> Array:
    """[A,B]."""
    a = np.asarray(a, dtype=complex)
    b = np.asarray(b, dtype=complex)
    return a @ b - b @ a


def is_fixed_spectral_stratum_compatible(
    y: Array,
    *operators: Array,
    tol: float = 1e-9,
) -> bool:
    """Strong sufficient diagnostic for simultaneous spectral closure.

    Requires 0<Y<=I and pairwise commutation of all supplied Hermitian objects.
    This certifies simultaneous diagonalizability of the declared tuple, but it
    does not by itself prove that the full BFG update preserves the tuple.
    """
    y = hermitian_part(np.asarray(y, dtype=complex))
    vals = np.linalg.eigvalsh(y)
    if vals.size and (float(vals.min()) <= tol or float(vals.max()) > 1.0 + tol):
        return False
    mats = [y] + [hermitian_part(np.asarray(a, dtype=complex)) for a in operators]
    for i in range(len(mats)):
        for j in range(i + 1, len(mats)):
            if opnorm(operator_commutator(mats[i], mats[j])) > tol:
                return False
    return True


# ---------------------------------------------------------------------------
# Exact commuting-stratum map and frozen noncommuting formation semigroup
# ---------------------------------------------------------------------------

def commuting_reciprocal_step(
    y: Array,
    formation_weights: Array,
) -> tuple[Array, float, float, float, float]:
    """Exact selected commuting-stratum load update.

    Assumptions:
      - common diagonal basis,
      - full selected persistent support,
      - 0 < y_i < 1,
      - nonnegative formation weights r_i with positive total mass.

    Global reciprocal weights couple all modes:
        L_C = sum r_i/(1+y_i)
        L_B = sum r_i*y_i^2/(1+y_i)
        alpha = L_B/(L_C+L_B)
        beta  = L_C/(L_C+L_B)
        y_i+ = (alpha + beta*y_i^2)/(1+y_i)^2
    """
    y = np.asarray(y, dtype=float).reshape(-1)
    r = np.asarray(formation_weights, dtype=float).reshape(-1)
    if y.shape != r.shape:
        raise ValueError("y and formation_weights must have the same shape")
    if np.any(y <= 0.0) or np.any(y >= 1.0):
        raise ValueError("selected commuting stratum requires 0 < y_i < 1")
    if np.any(r < 0.0) or float(np.sum(r)) <= 0.0:
        raise ValueError("formation_weights must be nonnegative with positive total mass")

    load_c = float(np.sum(r / (1.0 + y)))
    load_b = float(np.sum(r * y * y / (1.0 + y)))
    total = load_c + load_b
    alpha = load_b / total
    beta = load_c / total
    y_plus = (alpha + beta * y * y) / ((1.0 + y) ** 2)
    return y_plus, alpha, beta, load_c, load_b


def commuting_quadratic_tangent(
    x: Array,
    formation_weights: Array,
) -> Array:
    """Quadratic tangent map at the neutral boundary for the commuting stratum.

    If y=s*x with s->0+, then
        F(s*x)/s^2 -> Q_r(x)
    where
        Q_i = x_i^2 + <x^2>_r.
    """
    x = np.asarray(x, dtype=float).reshape(-1)
    r = np.asarray(formation_weights, dtype=float).reshape(-1)
    if x.shape != r.shape:
        raise ValueError("x and formation_weights must have the same shape")
    if np.any(r < 0.0) or float(np.sum(r)) <= 0.0:
        raise ValueError("formation_weights must be nonnegative with positive total mass")
    mean2 = float(np.sum(r * x * x) / np.sum(r))
    return x * x + mean2


def two_cluster_projective_profile(
    p: float,
) -> tuple[float, float]:
    """Weighted-normalized two-cluster fixed profile of the quadratic tangent map.

    p is the total normalized formation weight of cluster A; 1-p belongs to B.
    For a genuinely two-valued fixed profile:
        a = 1/(2p), b = 1/(2(1-p)).
    """
    p = float(p)
    if not (0.0 < p < 1.0):
        raise ValueError("p must lie in (0,1)")
    return 1.0 / (2.0 * p), 1.0 / (2.0 * (1.0 - p))


def frozen_reclosure_correlation(
    y: Array,
    alpha: float,
) -> Array:
    """Correlation multiplier Chi for frozen canonical polar reclosure."""
    y = np.asarray(y, dtype=float).reshape(-1)
    alpha = float(alpha)
    beta = 1.0 - alpha
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must lie in (0,1)")
    if np.any(y < 0.0):
        raise ValueError("neutral load eigenvalues must be nonnegative")
    den = np.sqrt(alpha + beta * y * y)
    return (
        alpha + beta * np.outer(y, y)
    ) / np.outer(den, den)


def frozen_formation_reclosure(
    k: Array,
    chi: Array,
) -> Array:
    """One exact frozen-geometry formation reclosure K+ = Chi o K."""
    k = np.asarray(k, dtype=complex)
    chi = np.asarray(chi, dtype=float)
    if k.shape != chi.shape:
        raise ValueError("K and Chi must have the same shape")
    return hermitian_part(chi * k)


def frozen_formation_flow(
    k0: Array,
    chi: Array,
    tau: float,
) -> Array:
    """Exact continuous vector-space embedding of frozen formation reclosure.

    One discrete reclosure corresponds to tau=log(2):
        K(tau) = Chi^(tau/log 2) o K0.

    This preserves Hermiticity. It is NOT asserted to be positive/CP on the
    positive cone for fractional tau.
    """
    k0 = np.asarray(k0, dtype=complex)
    chi = np.asarray(chi, dtype=float)
    tau = float(tau)
    if tau < 0.0:
        raise ValueError("tau must be nonnegative")
    if k0.shape != chi.shape:
        raise ValueError("K and Chi must have the same shape")
    if np.any(chi <= 0.0):
        raise InadmissibleState("continuous logarithmic embedding requires Chi_ij>0")
    power = tau / np.log(2.0)
    return hermitian_part((chi ** power) * k0)


def frozen_formation_generator(
    k: Array,
    chi: Array,
) -> Array:
    """Generator dK/dtau = (log Chi/log 2) o K."""
    k = np.asarray(k, dtype=complex)
    chi = np.asarray(chi, dtype=float)
    if k.shape != chi.shape:
        raise ValueError("K and Chi must have the same shape")
    if np.any(chi <= 0.0):
        raise InadmissibleState("generator requires Chi_ij>0")
    return hermitian_part((np.log(chi) / np.log(2.0)) * k)


def schur_fractional_multiplier_eigenvalues(
    chi: Array,
    tau: float,
) -> Array:
    """Eigenvalues of the fractional Schur multiplier matrix Chi^(tau/log 2)."""
    chi = np.asarray(chi, dtype=float)
    tau = float(tau)
    if np.any(chi <= 0.0):
        raise InadmissibleState("fractional multiplier requires positive Chi entries")
    multiplier = chi ** (tau / np.log(2.0))
    return np.linalg.eigvalsh((multiplier + multiplier.T) / 2.0)


# ---------------------------------------------------------------------------
# Schoenberg / CP-embeddability diagnostics for frozen BFG Schur reclosure
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SchurEmbeddabilityCertificate:
    embeddable: bool
    min_centered_gram_eigenvalue: float
    distance_matrix: Array
    centered_gram: Array


def schur_embeddability_certificate(
    chi: Array,
    *,
    tol: float = 1e-10,
) -> SchurEmbeddabilityCertificate:
    """Test infinite divisibility of a positive-entry correlation matrix.

    Let D_ij=-log(Chi_ij). By Schoenberg's criterion, Chi^(o t) is PSD for
    every t>=0 iff D is conditionally negative semidefinite, equivalently
        B = -1/2 J D J >= 0,
    where J=I-11^T/n.

    This is standard mathematics applied to the BFG-generated Chi.
    """
    chi = np.asarray(chi, dtype=float)
    if chi.ndim != 2 or chi.shape[0] != chi.shape[1]:
        raise ValueError('Chi must be square')
    if np.any(chi <= 0.0):
        raise InadmissibleState('Schoenberg log criterion requires positive Chi entries')
    if not np.allclose(chi, chi.T, atol=tol):
        raise InadmissibleState('Chi must be symmetric')
    if not np.allclose(np.diag(chi), 1.0, atol=tol):
        raise InadmissibleState('Chi must have unit diagonal')

    d = -np.log(chi)
    n = chi.shape[0]
    j = np.eye(n) - np.ones((n, n))/n
    b = -0.5 * j @ d @ j
    b = (b + b.T)/2.0
    eig = np.linalg.eigvalsh(b)
    min_eig = float(eig.min()) if eig.size else 0.0
    return SchurEmbeddabilityCertificate(
        embeddable=bool(min_eig >= -tol),
        min_centered_gram_eigenvalue=min_eig,
        distance_matrix=d,
        centered_gram=b,
    )


def frozen_cp_schur_flow_multiplier(
    chi: Array,
    tau: float,
) -> Array:
    """Fractional Schur multiplier when the BFG frozen channel is CP-embeddable.

    Raises if Schoenberg's criterion fails.
    """
    cert = schur_embeddability_certificate(chi)
    if not cert.embeddable:
        raise InadmissibleState('frozen Schur reclosure is not CP-embeddable by entrywise powers')
    exponent = float(tau)/np.log(2.0)
    if exponent < 0.0:
        raise ValueError('tau must be nonnegative')
    return np.asarray(chi, dtype=float) ** exponent


# ---------------------------------------------------------------------------
# Canonical two-channel angle interpolation and frozen full-state CP path
# ---------------------------------------------------------------------------

def bfg_channel_angles(
    y: Array,
    alpha: float,
) -> Array:
    """Canonical two-channel angles theta_i.

    tan(theta_i) = sqrt(beta/alpha) y_i,  alpha,beta>0.
    Then the canonical frozen BFG correlation satisfies
        Chi_ij = cos(theta_i-theta_j).
    """
    y = np.asarray(y, dtype=float).reshape(-1)
    alpha = float(alpha)
    beta = 1.0 - alpha
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must lie in (0,1)")
    if np.any(y < 0.0):
        raise ValueError("y_i must be nonnegative")
    return np.arctan(np.sqrt(beta / alpha) * y)


def frozen_angle_multiplier(
    y: Array,
    alpha: float,
    step_fraction: float,
) -> Array:
    """Canonical CP interpolation inside one frozen BFG reclosure step.

    step_fraction s in [0,1]:
        Chi_s,ij = cos(s(theta_i-theta_j)).
    Chi_0 is the all-ones identity Schur multiplier.
    Chi_1 is the exact BFG frozen correlation matrix.
    """
    s = float(step_fraction)
    if not (0.0 <= s <= 1.0):
        raise ValueError("step_fraction must lie in [0,1]")
    theta = bfg_channel_angles(y, alpha)
    delta = theta[:, None] - theta[None, :]
    return np.cos(s * delta)


def frozen_angle_suspension_multiplier(
    y: Array,
    alpha: float,
    tau: float,
) -> Array:
    """Continuous CP suspension through repeated frozen discrete reclosures.

    One BFG discrete step has recursive time log(2).
    For u=tau/log(2)=n+s, n=floor(u), s in [0,1):
        M_tau = Chi^(o n) o Chi_s.

    This path is continuous and CP for every tau>=0, and hits the exact
    n-step frozen reclosure at tau=n log(2). It is generally not a semigroup.
    """
    tau = float(tau)
    if tau < 0.0:
        raise ValueError("tau must be nonnegative")
    u = tau / np.log(2.0)
    n = int(np.floor(u + 1e-15))
    s = u - n
    # Avoid a negative/near-one fractional artifact at integer boundaries.
    if s < 1e-14:
        s = 0.0
    chi = frozen_reclosure_correlation(y, alpha)
    partial = frozen_angle_multiplier(y, alpha, s)
    return (chi ** n) * partial


def frozen_angle_capacity_flow(
    a: Array,
    y_operator: Array,
    alpha: float,
    tau: float,
) -> Array:
    """Apply the canonical frozen CP suspension to a Hermitian capacity operator.

    The computation is performed in an eigenbasis of Y and returned in the
    original basis.
    """
    a = hermitian_part(np.asarray(a, dtype=complex))
    y_operator = hermitian_part(np.asarray(y_operator, dtype=complex))
    vals, vecs = np.linalg.eigh(y_operator)
    if vals.size and float(vals.min()) < -1e-10:
        raise InadmissibleState("Y must be positive semidefinite")
    a_eig = dagger(vecs) @ a @ vecs
    mult = frozen_angle_suspension_multiplier(vals, alpha, tau)
    return hermitian_part(vecs @ (mult * a_eig) @ dagger(vecs))


def frozen_full_state_cp_path(
    s: UniversalOperatorState,
    alpha: float,
    tau: float,
    *,
    tol: float = 1e-9,
) -> UniversalOperatorState:
    """Positive continuous path for a frozen same-support BFG stratum.

    Frozen data:
      - Y,
      - R_C and P_per,
      - formation/load density rho_F,
      - identity witness rho_W,
      - reciprocal channel weight alpha (beta=1-alpha).

    Evolving data:
      - D_cap, coherence, emergence under the canonical two-channel CP path.

    This is consistent with fixed-support R4 self-continuation: in the chosen
    fixed carrier gauge, witness and inherited formation density are unchanged.
    The derived formation K=c+aleph-D evolves by the same linear CP Schur path.

    At tau=log(2), the capacity triple matches one frozen canonical Schur
    reclosure. At integer multiples, it matches repeated frozen reclosure.

    The path is generally non-Markovian/non-semigroup when Chi is not infinitely
    divisible.
    """
    validate_universal_operator_state(s, tol=tol)
    tau = float(tau)
    dcap = frozen_angle_capacity_flow(s.D_cap, s.Y, alpha, tau)
    coh = frozen_angle_capacity_flow(s.coherence, s.Y, alpha, tau)
    em = frozen_angle_capacity_flow(s.emergence, s.Y, alpha, tau)

    out = UniversalOperatorState(
        D_cap=dcap,
        coherence=coh,
        emergence=em,
        formation_density=np.array(s.formation_density, dtype=complex, copy=True),
        witness=np.array(s.witness, dtype=complex, copy=True),
        Y=np.array(s.Y, dtype=complex, copy=True),
        R_C=np.array(s.R_C, dtype=complex, copy=True),
        P_per=None if s.P_per is None else np.array(s.P_per, dtype=complex, copy=True),
    )
    validate_universal_operator_state(out, tol=tol)
    return out


def frozen_angle_local_rate_matrix(
    y: Array,
    alpha: float,
    step_fraction: float,
) -> Array:
    """Time-local coefficient Gamma_s for one canonical angle-interpolation step.

    For K_ij(s)=cos(s*Delta_ij) K_ij(0):
        dK_ij/ds = Gamma_ij(s) K_ij(s)
        Gamma_ij(s) = -Delta_ij tan(s Delta_ij).

    This is a step-local generator, not a time-homogeneous semigroup generator.
    """
    s = float(step_fraction)
    if not (0.0 <= s < 1.0 + 1e-12):
        raise ValueError("step_fraction must lie in [0,1]")
    theta = bfg_channel_angles(y, alpha)
    delta = theta[:, None] - theta[None, :]
    return -delta * np.tan(s * delta)


# ---------------------------------------------------------------------------
# Phase-anchored full-persistent state suspension
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FullPersistentEndpoint:
    state: UniversalOperatorState
    alpha: float
    beta: float
    load_C: float
    load_B: float


@dataclass(frozen=True)
class PhaseAnchoredSuspension:
    phase: float
    source: UniversalOperatorState
    target: UniversalOperatorState
    readout: UniversalOperatorState
    alpha_source: float
    beta_source: float


def _matrix_log_positive(a: Array, tol: float = 1e-12) -> Array:
    a = hermitian_part(np.asarray(a, dtype=complex))
    vals, vecs = np.linalg.eigh(a)
    if vals.size and float(vals.min()) <= tol:
        raise InadmissibleState("positive matrix logarithm requires strict positivity")
    return hermitian_part((vecs * np.log(vals)) @ dagger(vecs))


def _matrix_exp_hermitian(a: Array) -> Array:
    a = hermitian_part(np.asarray(a, dtype=complex))
    vals, vecs = np.linalg.eigh(a)
    return hermitian_part((vecs * np.exp(vals)) @ dagger(vecs))


def log_euclidean_positive_bridge(
    a0: Array,
    a1: Array,
    phase: float,
) -> Array:
    """Unitary-covariant positive endpoint bridge exp((1-s)log A0+s log A1)."""
    s = float(phase)
    if not (0.0 <= s <= 1.0):
        raise ValueError("phase must lie in [0,1]")
    l0 = _matrix_log_positive(a0)
    l1 = _matrix_log_positive(a1)
    return _matrix_exp_hermitian((1.0-s)*l0 + s*l1)


def affine_positive_bridge(
    a0: Array,
    a1: Array,
    phase: float,
) -> Array:
    """A second unitary-covariant positive bridge, used to prove non-uniqueness."""
    s = float(phase)
    if not (0.0 <= s <= 1.0):
        raise ValueError("phase must lie in [0,1]")
    return hermitian_part((1.0-s)*np.asarray(a0) + s*np.asarray(a1))


def gauge_aligned_full_persistent_endpoint(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
) -> FullPersistentEndpoint:
    """Closed-form endpoint for the full-persistent selected same-carrier stratum.

    Assumptions:
      P_per = I, R_C = I, 0<Y<I.
    The endpoint is expressed back in the source carrier gauge, rather than in
    the SVD target frame used by the generic runtime.
    """
    validate_universal_operator_state(s, tol=max(tol, 1e-9))
    n = s.dim
    eye = np.eye(n, dtype=complex)
    p = _ordinary_persistent_projector(s, tol=tol)
    if opnorm(p-eye) > 100*tol:
        raise InadmissibleState("requires full persistent support P=I")
    if opnorm(s.R_C-eye) > 100*tol:
        raise InadmissibleState("requires R_C=I in the full persistent gauge")

    vals, u = np.linalg.eigh(hermitian_part(s.Y))
    if float(vals.min()) <= tol or float(vals.max()) >= 1.0 - tol:
        raise InadmissibleState("requires strictly selected load spectrum 0<Y<I")

    rho_e = dagger(u) @ s.formation_density @ u
    rdiag = np.real(np.diag(rho_e))
    load_c = float(np.sum(rdiag/(1.0+vals)))
    load_b = float(np.sum(rdiag*vals*vals/(1.0+vals)))
    if load_c <= tol or load_b <= tol:
        raise InadmissibleState("requires positive dual loads")
    alpha = load_b/(load_c+load_b)
    beta = load_c/(load_c+load_b)

    y1_vals = (alpha + beta*vals*vals)/((1.0+vals)**2)
    y1 = hermitian_part((u*y1_vals) @ dagger(u))

    chi = frozen_reclosure_correlation(vals, alpha)

    def reclose_capacity(a: Array) -> Array:
        ae = dagger(u) @ np.asarray(a, dtype=complex) @ u
        return hermitian_part(u @ (chi*ae) @ dagger(u))

    out = UniversalOperatorState(
        D_cap=reclose_capacity(s.D_cap),
        coherence=reclose_capacity(s.coherence),
        emergence=reclose_capacity(s.emergence),
        formation_density=np.array(s.formation_density, dtype=complex, copy=True),
        witness=np.array(s.witness, dtype=complex, copy=True),
        Y=y1,
        R_C=eye,
        P_per=eye,
    )
    validate_universal_operator_state(out, tol=max(tol, 1e-8))
    return FullPersistentEndpoint(
        state=out,
        alpha=alpha,
        beta=beta,
        load_C=load_c,
        load_B=load_b,
    )


def phase_anchored_full_persistent_suspension(
    source: UniversalOperatorState,
    phase: float,
    *,
    tol: float = 1e-10,
) -> PhaseAnchoredSuspension:
    """Endpoint-exact continuous state path on a full-persistent no-event stratum.

    The discrete BFG map fixes the source and target.
    Continuum completion used inside the step:
      - capacities: canonical BFG two-channel CP angle path;
      - load: affine interpolation in closure depth H=-log Y
              (log-Euclidean positive bridge);
      - rho_F, rho_W: fixed under same-support polar self-continuation;
      - R_C=P=I: fixed.

    The load bridge is an explicit NEW CONTINUUM COMPLETION RULE. It is not
    uniquely forced by the discrete BFG equations.
    """
    ph = float(phase)
    if not (0.0 <= ph <= 1.0):
        raise ValueError("phase must lie in [0,1]")

    endpoint = gauge_aligned_full_persistent_endpoint(source, tol=tol)
    target = endpoint.state
    tau = ph*np.log(2.0)

    dcap = frozen_angle_capacity_flow(
        source.D_cap, source.Y, endpoint.alpha, tau
    )
    coh = frozen_angle_capacity_flow(
        source.coherence, source.Y, endpoint.alpha, tau
    )
    em = frozen_angle_capacity_flow(
        source.emergence, source.Y, endpoint.alpha, tau
    )

    y_ph = log_euclidean_positive_bridge(source.Y, target.Y, ph)
    eye = np.eye(source.dim, dtype=complex)

    readout = UniversalOperatorState(
        D_cap=dcap,
        coherence=coh,
        emergence=em,
        formation_density=np.array(source.formation_density, dtype=complex, copy=True),
        witness=np.array(source.witness, dtype=complex, copy=True),
        Y=y_ph,
        R_C=eye,
        P_per=eye,
    )
    validate_universal_operator_state(readout, tol=max(tol, 1e-8))

    return PhaseAnchoredSuspension(
        phase=ph,
        source=source,
        target=target,
        readout=readout,
        alpha_source=endpoint.alpha,
        beta_source=endpoint.beta,
    )


def phase_anchored_load_nonuniqueness(
    source: UniversalOperatorState,
    phase: float = 0.5,
) -> float:
    """Norm gap between two admissible endpoint-exact positive Y bridges.

    A nonzero result proves that positivity + covariance + endpoint matching do
    not uniquely determine the continuum load path.
    """
    endpoint = gauge_aligned_full_persistent_endpoint(source)
    y_log = log_euclidean_positive_bridge(source.Y, endpoint.state.Y, phase)
    y_aff = affine_positive_bridge(source.Y, endpoint.state.Y, phase)
    return opnorm(y_log-y_aff)


@dataclass(frozen=True)
class RecursivePhaseAnchorState:
    """Extended continuum state for the no-event full-persistent suspension.

    anchor is the last committed discrete BFG state (memory-like step anchor).
    phase in [0,1) is the normalized recursive closure phase.
    """
    anchor: UniversalOperatorState
    phase: float


def recursive_phase_anchor_readout(
    extended: RecursivePhaseAnchorState,
) -> UniversalOperatorState:
    """Physical/readout state associated with an anchor+phase pair."""
    return phase_anchored_full_persistent_suspension(
        extended.anchor,
        extended.phase,
    ).readout


def advance_recursive_phase_anchor(
    extended: RecursivePhaseAnchorState,
    delta_tau: float,
) -> RecursivePhaseAnchorState:
    """Markovian suspension flow on the extended anchor-phase state.

    One complete discrete BFG step corresponds to delta_tau=log(2).
    When phase reaches 1, commit the exact discrete endpoint and reset phase.
    """
    if delta_tau < 0.0:
        raise ValueError("delta_tau must be nonnegative")
    anchor = extended.anchor
    phase_total = float(extended.phase) + float(delta_tau)/np.log(2.0)
    if not (0.0 <= extended.phase < 1.0):
        raise ValueError("extended.phase must lie in [0,1)")

    n = int(np.floor(phase_total + 1e-14))
    phase = phase_total - n
    if phase >= 1.0 - 1e-13:
        n += 1
        phase = 0.0

    for _ in range(n):
        anchor = gauge_aligned_full_persistent_endpoint(anchor).state

    return RecursivePhaseAnchorState(
        anchor=anchor,
        phase=float(phase),
    )


def recursive_phase_anchor_flow(
    source: UniversalOperatorState,
    tau: float,
) -> UniversalOperatorState:
    """Convenience trajectory from phase zero."""
    ext = advance_recursive_phase_anchor(
        RecursivePhaseAnchorState(anchor=source, phase=0.0),
        tau,
    )
    return recursive_phase_anchor_readout(ext)


@dataclass(frozen=True)
class R4SameRankGeodesic:
    phase: float
    projector: Array
    transport: Array
    principal_angles: Array


def r4_same_rank_geodesic(
    p0: Array,
    p1: Array,
    phase: float,
    *,
    tol: float = 1e-10,
) -> R4SameRankGeodesic:
    """Canonical principal-angle interpolation between equal-rank supports.

    Requires full R4 overlap: no principal angle equals pi/2.
    At phase=0, transport=P0.
    At phase=1, transport=polar(P1 P0), the R4 partial isometry.
    """
    s=float(phase)
    if not (0.0<=s<=1.0):
        raise ValueError("phase must lie in [0,1]")
    p0=hermitian_part(np.asarray(p0,dtype=complex))
    p1=hermitian_part(np.asarray(p1,dtype=complex))
    _validate_orthogonal_projector(p0,max(tol,1e-9))
    _validate_orthogonal_projector(p1,max(tol,1e-9))

    z0=_orthonormal_range(p0,tol=tol)
    z1=_orthonormal_range(p1,tol=tol)
    if z0.shape[1]!=z1.shape[1]:
        raise InadmissibleState("same-rank geodesic requires equal projector ranks")
    r=z0.shape[1]
    if r==0:
        raise InadmissibleState("same-rank geodesic requires nonzero support")

    m=dagger(z1)@z0
    u,sv,vh=np.linalg.svd(m,full_matrices=False)
    sv=np.clip(sv,0.0,1.0)
    if float(sv.min())<=tol:
        raise InadmissibleState("full-overlap geodesic fails at a pi/2 principal angle")

    v=dagger(vh)
    a=z0@v
    b=z1@u
    theta=np.arccos(sv)

    w=np.zeros_like(a)
    for j in range(r):
        th=float(theta[j])
        if th<=tol:
            # At zero angle the aligned principal vectors coincide up to numerical noise.
            w[:,j]=a[:,j]
        else:
            st=np.sin(th)
            nvec=(b[:,j]-sv[j]*a[:,j])/st
            w[:,j]=np.cos(s*th)*a[:,j]+np.sin(s*th)*nvec

    # Re-orthonormalize only for floating cleanup; the analytic columns are orthonormal.
    w,_=np.linalg.qr(w)
    # QR can introduce endpoint phases/signs. Align to analytic overlap with a.
    # The subspace projector is invariant; for the transport use polar(w a^*) to
    # remove QR gauge.
    p=hermitian_part(w@dagger(w))
    x=p@p0
    t=polar_partial_isometry(x,tol=tol)
    return R4SameRankGeodesic(
        phase=s,
        projector=p,
        transport=t,
        principal_angles=theta,
    )


def r4_same_rank_density_transport(
    density: Array,
    p0: Array,
    p1: Array,
    phase: float,
    *,
    normalize: bool = False,
    tol: float = 1e-10,
) -> Array:
    """Positive continuous R4-compatible density transport along support geodesic."""
    rho=hermitian_part(np.asarray(density,dtype=complex))
    if not is_psd(rho,max(tol,1e-9)):
        raise InadmissibleState("density must be positive semidefinite")
    if opnorm(rho-np.asarray(p0)@rho@np.asarray(p0))>100*tol:
        raise InadmissibleState("density must be supported in p0")
    geo=r4_same_rank_geodesic(p0,p1,phase,tol=tol)
    out=hermitian_part(geo.transport@rho@dagger(geo.transport))
    if normalize:
        tr=_trace_real(out)
        if tr<=tol:
            raise InadmissibleState("transport annihilated normalized density")
        out=out/tr
    return out


# ---------------------------------------------------------------------------
# Local anchor elimination / phase-local continuum
# ---------------------------------------------------------------------------

def scalar_phase_readout_h(
    anchor_h: float,
    phase: float,
) -> float:
    """Closure-depth readout h(omega)=(1-omega)h_*+omega F_H(h_*)."""
    a = float(anchor_h)
    w = float(phase)
    if a < 0.0:
        raise ValueError("selected scalar closure depth requires anchor_h >= 0")
    if not (0.0 <= w <= 1.0):
        raise ValueError("phase must lie in [0,1]")
    return (1.0-w)*a + w*scalar_closure_depth_update(a)


def scalar_phase_reconstruct_anchor_h(
    current_h: float,
    phase: float,
    *,
    bisect_steps: int = 100,
) -> float:
    """Reconstruct the unique scalar anchor h_* from current (h,omega).

    On h>=0, F_H is strictly increasing, so
        G_omega(a)=(1-omega)a+omega F_H(a)
    is strictly increasing for every omega in [0,1].
    """
    h = float(current_h)
    w = float(phase)
    if h < 0.0:
        raise ValueError("selected scalar closure depth requires current_h >= 0")
    if not (0.0 <= w <= 1.0):
        raise ValueError("phase must lie in [0,1]")

    if w == 0.0:
        return h

    def g(a):
        return scalar_phase_readout_h(a, w)

    lo = 0.0
    hi = max(1.0, h + 2.0)
    while g(hi) < h:
        hi *= 2.0

    for _ in range(bisect_steps):
        mid = 0.5*(lo+hi)
        if g(mid) < h:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)


def scalar_phase_local_vector_field_h(
    current_h: float,
    phase: float,
) -> tuple[float, float]:
    """Anchor-free local vector field on (h,omega).

    d omega/d tau = 1/log(2)
    d h/d tau     = [F_H(h_*)-h_*]/log(2)
    with h_* reconstructed from current (h,omega).
    """
    a = scalar_phase_reconstruct_anchor_h(current_h, phase)
    velocity = (scalar_closure_depth_update(a)-a)/np.log(2.0)
    return float(velocity), float(1.0/np.log(2.0))


def scalar_phase_local_vector_field_y(
    current_y: float,
    phase: float,
) -> tuple[float, float]:
    """Anchor-free local vector field in the scalar load coordinate."""
    y = float(current_y)
    if not (0.0 < y <= 1.0):
        raise ValueError("selected scalar sector requires 0<y<=1")
    h = -np.log(y)
    dh, domega = scalar_phase_local_vector_field_h(h, phase)
    return float(-y*dh), domega


def scalar_phase_anchor_free_advance(
    current_h: float,
    phase: float,
    delta_tau: float,
) -> tuple[float, float]:
    """Exact advance inside one scalar no-event step without storing the anchor.

    This reconstructs the anchor from (h,omega), advances phase exactly, and
    evaluates the same suspension. It is restricted to intervals that do not
    cross a commit surface omega=1.
    """
    if delta_tau < 0.0:
        raise ValueError("delta_tau must be nonnegative")
    w = float(phase)
    if not (0.0 <= w < 1.0):
        raise ValueError("phase must lie in [0,1)")
    a = scalar_phase_reconstruct_anchor_h(current_h, w)
    w1 = w + float(delta_tau)/np.log(2.0)
    if w1 >= 1.0:
        raise InadmissibleState("advance crosses discrete commit surface")
    return scalar_phase_readout_h(a, w1), w1


@dataclass(frozen=True)
class SuspensionLocalityCertificate:
    locally_anchor_free: bool
    requires_memory_branch: bool
    phase: float
    min_singular_value: float


def suspension_locality_certificate_from_jacobian(
    jacobian: Array,
    phase: float,
    *,
    tol: float = 1e-10,
) -> SuspensionLocalityCertificate:
    """Inverse-function-theorem certificate for a finite suspension chart.

    If D_anchor I_phase is invertible, the anchor can be reconstructed locally
    from current readout + phase, so no separate anchor variable is needed in
    that chart.

    If singular, this test alone does not prove impossibility; it marks a chart
    where additional branch/memory information may be required.
    """
    j = np.asarray(jacobian, dtype=float)
    if j.ndim != 2 or j.shape[0] != j.shape[1]:
        raise ValueError("jacobian must be square")
    sv = np.linalg.svd(j, compute_uv=False)
    min_sv = float(sv.min()) if sv.size else float("inf")
    invertible = bool(min_sv > tol)
    return SuspensionLocalityCertificate(
        locally_anchor_free=invertible,
        requires_memory_branch=not invertible,
        phase=float(phase),
        min_singular_value=min_sv,
    )


def scalar_phase_readout_derivative_anchor(
    anchor_h: float,
    phase: float,
) -> float:
    """Exact derivative d G_omega(a)/da for the scalar closure-depth suspension."""
    a = float(anchor_h)
    w = float(phase)
    if a < 0.0 or not (0.0 <= w <= 1.0):
        raise ValueError
    # F_H'(h)
    fp = (
        2.0
        - 2.0/(np.exp(a)+1.0)
        - 2.0/(np.exp(2.0*a)+1.0)
    )
    return float((1.0-w) + w*fp)


def scalar_same_readout_different_phase_example(
    current_h: float,
    phase_a: float,
    phase_b: float,
) -> tuple[float, float, float, float]:
    """Construct two anchors giving the same h at two different phases.

    Returns (anchor_a, anchor_b, velocity_a, velocity_b).
    Demonstrates why phase Omega is necessary for a local reduced description.
    """
    if phase_a == phase_b:
        raise ValueError("phases must differ")
    a = scalar_phase_reconstruct_anchor_h(current_h, phase_a)
    b = scalar_phase_reconstruct_anchor_h(current_h, phase_b)
    va = (scalar_closure_depth_update(a)-a)/np.log(2.0)
    vb = (scalar_closure_depth_update(b)-b)/np.log(2.0)
    return float(a), float(b), float(va), float(vb)


# ---------------------------------------------------------------------------
# Coupled commuting suspension fold / memory-branch witness
# ---------------------------------------------------------------------------

def commuting_phase_endpoint_h(
    anchor_h: Array,
    formation_weights: Array,
) -> Array:
    """Gauge-diagonal coupled commuting endpoint in closure-depth coordinates."""
    h = np.asarray(anchor_h, dtype=float).reshape(-1)
    r = np.asarray(formation_weights, dtype=float).reshape(-1)
    y = np.exp(-h)
    yp, *_ = commuting_reciprocal_step(y, r)
    return -np.log(yp)


def commuting_phase_readout_h(
    anchor_h: Array,
    formation_weights: Array,
    phase: float,
) -> Array:
    """Log-Euclidean phase readout for the coupled commuting stratum."""
    h = np.asarray(anchor_h, dtype=float).reshape(-1)
    w = float(phase)
    if np.any(h <= 0.0):
        raise ValueError("selected multimode closure depth requires h_i>0")
    if not (0.0 <= w <= 1.0):
        raise ValueError("phase must lie in [0,1]")
    hp = commuting_phase_endpoint_h(h, formation_weights)
    return (1.0-w)*h + w*hp


def commuting_phase_tangent_h(
    anchor_h: Array,
    formation_weights: Array,
) -> Array:
    """d h/d tau along one coupled commuting suspension branch."""
    h = np.asarray(anchor_h, dtype=float).reshape(-1)
    hp = commuting_phase_endpoint_h(h, formation_weights)
    return (hp-h)/np.log(2.0)


def commuting_phase_jacobian_fd(
    anchor_h: Array,
    formation_weights: Array,
    phase: float,
    *,
    eps: float = 1e-6,
) -> Array:
    """Finite-difference anchor Jacobian of the coupled commuting phase readout."""
    h = np.asarray(anchor_h, dtype=float).reshape(-1)
    n = h.size
    j = np.empty((n,n), dtype=float)
    for k in range(n):
        step = eps*max(1.0, abs(float(h[k])))
        d = np.zeros(n, dtype=float)
        d[k] = step
        fp = commuting_phase_readout_h(h+d, formation_weights, phase)
        fm = commuting_phase_readout_h(h-d, formation_weights, phase)
        j[:,k] = (fp-fm)/(2.0*step)
    return j


def canonical_two_mode_memory_branch_witness() -> dict:
    """Deterministic constructive witness of same-(readout,phase), different tangents.

    All three anchors are in the selected two-mode stratum and map, at phase
    omega=0.86, to the same readout to floating precision but have distinct
    local tangents. This is an internal mathematical counterexample, not an
    empirical result.
    """
    r = np.array([0.11560491, 0.81916805], dtype=float)
    omega = 0.86
    anchors = [
        np.array([0.5477780109900522, 0.10675283802139944], dtype=float),
        np.array([1.2921364085108170, 0.09571786689741645], dtype=float),
        np.array([2.7981030718815405, 0.08968102378697691], dtype=float),
    ]
    readouts = [commuting_phase_readout_h(a, r, omega) for a in anchors]
    tangents = [commuting_phase_tangent_h(a, r) for a in anchors]
    return {
        "formation_weights": r,
        "phase": omega,
        "anchors_h": anchors,
        "anchors_y": [np.exp(-a) for a in anchors],
        "readouts_h": readouts,
        "tangents_dh_dtau": tangents,
    }


@dataclass(frozen=True)
class MemoryBranchLocalState:
    """Minimal conceptual local-continuum state.

    branch labels the locally invertible continuation sheet. It is not the full
    historical anchor. On an injective chart branch may be None/0.
    """
    phase: float
    branch: int


def memory_branch_local_law(
    current: Array,
    phase: float,
    branch_anchor_reconstruction,
    phase_partial,
    branch,
) -> Array:
    """Generic local law V(X,Omega,M) once a branch reconstruction is supplied.

    This is an abstract helper for finite research models:
      anchor = R_{Omega,M}(X)
      dot X  = (1/log2) partial_Omega I_Omega(anchor)

    It does not define the universal branch-update law M->M+.
    """
    anchor = branch_anchor_reconstruction(current, phase, branch)
    return np.asarray(
        phase_partial(anchor, phase),
        dtype=float,
    ) / np.log(2.0)


# ---------------------------------------------------------------------------
# Simple-fold classification and local memory-bit geometry
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SimpleFoldCertificate:
    is_simple_fold: bool
    phase: float
    singular_values: Array
    right_null: Array
    left_null: Array
    fold_curvature: float
    phase_transversality: float
    determinant_phase_derivative: float


def simple_fold_certificate(
    readout_fn,
    anchor: Array,
    phase: float,
    *,
    anchor_step: float = 2e-6,
    second_step: float = 2e-4,
    phase_step: float = 1e-6,
    singular_tol: float = 1e-7,
    nondeg_tol: float = 1e-6,
) -> SimpleFoldCertificate:
    """Numerical Whitney-fold certificate for F(anchor, phase).

    Conditions checked at fixed phase:
      1. corank exactly one;
      2. left-null projection of D^2F[v,v] is nonzero.

    Additional parameter-unfolding diagnostics:
      3. left-null projection of dF/dphase is nonzero;
      4. det(D_anchor F) crosses phase transversely.

    The first two are the local simple-fold conditions. The latter two certify
    that the chosen recursive phase unfolds the fold transversely in this chart.
    """
    a = np.asarray(anchor, dtype=float).reshape(-1)
    n = a.size
    w = float(phase)

    def jac_at(ph):
        j = np.empty((n, n), dtype=float)
        for k in range(n):
            eps = anchor_step * max(1.0, abs(float(a[k])))
            d = np.zeros(n, dtype=float)
            d[k] = eps
            fp = np.asarray(readout_fn(a + d, ph), dtype=float)
            fm = np.asarray(readout_fn(a - d, ph), dtype=float)
            j[:, k] = (fp - fm) / (2.0 * eps)
        return j

    j = jac_at(w)
    u, sv, vh = np.linalg.svd(j)
    v = vh[-1]
    ell = u[:, -1]

    f0 = np.asarray(readout_fn(a, w), dtype=float)
    eps2 = second_step
    fpp = (
        np.asarray(readout_fn(a + eps2*v, w), dtype=float)
        - 2.0*f0
        + np.asarray(readout_fn(a - eps2*v, w), dtype=float)
    ) / (eps2**2)
    curvature = float(ell @ fpp)

    dp = phase_step
    f_phase = (
        np.asarray(readout_fn(a, w + dp), dtype=float)
        - np.asarray(readout_fn(a, w - dp), dtype=float)
    ) / (2.0*dp)
    phase_trans = float(ell @ f_phase)

    det_plus = float(np.linalg.det(jac_at(w + 10.0*dp)))
    det_minus = float(np.linalg.det(jac_at(w - 10.0*dp)))
    ddet = (det_plus - det_minus)/(20.0*dp)

    corank_one = (
        np.count_nonzero(sv < singular_tol) == 1
        and (n == 1 or float(sv[-2]) > singular_tol)
    )
    simple = (
        corank_one
        and abs(curvature) > nondeg_tol
    )

    return SimpleFoldCertificate(
        is_simple_fold=bool(simple),
        phase=w,
        singular_values=sv,
        right_null=v,
        left_null=ell,
        fold_curvature=curvature,
        phase_transversality=phase_trans,
        determinant_phase_derivative=float(ddet),
    )


def canonical_two_mode_simple_fold_certificate() -> SimpleFoldCertificate:
    """Certificate at the deterministic two-mode BFG suspension fold."""
    r = np.array([0.11560491, 0.81916805], dtype=float)
    anchor = np.array(
        [1.2921364085108027, 0.09571786689741542],
        dtype=float,
    )
    phase = 0.8283584507952344

    def fn(a, w):
        return commuting_phase_readout_h(a, r, w)

    return simple_fold_certificate(fn, anchor, phase)


def local_fold_branch_coordinate(
    anchor: Array,
    fold_anchor: Array,
    right_null: Array,
) -> float:
    """Signed local sheet coordinate along the fold null direction."""
    a = np.asarray(anchor, dtype=float).reshape(-1)
    af = np.asarray(fold_anchor, dtype=float).reshape(-1)
    v = np.asarray(right_null, dtype=float).reshape(-1)
    return float(v @ (a - af))


def local_fold_branch_bit(
    anchor: Array,
    fold_anchor: Array,
    right_null: Array,
    *,
    tol: float = 1e-10,
) -> int:
    """Local two-sheet label: -1 / +1, with 0 exactly on the fold."""
    q = local_fold_branch_coordinate(anchor, fold_anchor, right_null)
    if abs(q) <= tol:
        return 0
    return 1 if q > 0.0 else -1


def minimum_binary_memory_bits(branch_count: int) -> int:
    """Information lower bound for a fixed binary encoding of N branches."""
    n = int(branch_count)
    if n < 1:
        raise ValueError("branch_count must be positive")
    return int(np.ceil(np.log2(n))) if n > 1 else 0


# ---------------------------------------------------------------------------
# Exponential branch-growth lower bound for commuting suspension memory
# ---------------------------------------------------------------------------

def fixed_alpha_endpoint_h(
    h: float,
    alpha: float,
) -> float:
    """One-mode endpoint H_+(h) when reciprocal alpha is externally fixed."""
    h = float(h)
    alpha = float(alpha)
    if h <= 0.0:
        raise ValueError("selected closure depth requires h>0")
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must lie in (0,1)")
    beta = 1.0 - alpha
    y = np.exp(-h)
    yp = (alpha + beta*y*y) / ((1.0 + y)**2)
    return float(-np.log(yp))


def fixed_alpha_phase_readout_h(
    h: float,
    alpha: float,
    phase: float,
) -> float:
    """Scalar closure-depth suspension with fixed reciprocal alpha."""
    w = float(phase)
    if not (0.0 <= w <= 1.0):
        raise ValueError("phase must lie in [0,1]")
    h = float(h)
    return float(
        (1.0-w)*h + w*fixed_alpha_endpoint_h(h, alpha)
    )


def canonical_three_root_scalar_witness() -> dict:
    """Deterministic scalar three-root witness used in the branch-growth theorem.

    Parameters:
        alpha = 0.3
        phase = 0.94
        target = 1.45

    The fixed-alpha phase readout has exactly the three listed positive roots
    within the tested selected interval. They are away from turning points, so
    their scalar derivatives are nonzero.
    """
    return {
        "alpha": 0.3,
        "phase": 0.94,
        "target": 1.45,
        "roots": np.array([
            0.4145648725801513,
            2.0117746280041270,
            5.1188241575311740,
        ], dtype=float),
    }


def dominant_mode_anchor_for_alpha(alpha: float) -> float:
    """Anchor h1 producing reciprocal alpha when only mode 1 carries load weight.

    For one weighted mode,
        alpha = y^2/(1+y^2).
    Hence y=sqrt(alpha/(1-alpha)).
    The selected requirement y<1 corresponds to alpha<1/2.
    """
    alpha = float(alpha)
    if not (0.0 < alpha < 0.5):
        raise ValueError("selected dominant-mode construction requires 0<alpha<1/2")
    y = np.sqrt(alpha/(1.0-alpha))
    return float(-np.log(y))


def exponential_branch_lower_bound(dim: int) -> int:
    """Constructive lower bound on continuation branches in dimension dim.

    The dominant-mode decoupling construction yields at least 3^(dim-1)
    branches for sufficiently small positive secondary formation weights.
    """
    n = int(dim)
    if n < 1:
        raise ValueError("dim must be positive")
    return int(3 ** max(0, n-1))


def minimum_memory_bits_from_branch_count(branch_count: int) -> int:
    """Minimum number of binary bits needed to distinguish N simultaneous branches."""
    n = int(branch_count)
    if n < 1:
        raise ValueError("branch_count must be positive")
    return int(np.ceil(np.log2(n))) if n > 1 else 0


def exponential_branch_memory_bit_lower_bound(dim: int) -> int:
    """Information lower bound implied by the 3^(dim-1) construction."""
    return minimum_memory_bits_from_branch_count(
        exponential_branch_lower_bound(dim)
    )


def decoupled_dominant_mode_target(
    dim: int,
) -> tuple[Array, Array, float, Array]:
    """Return the exact epsilon=0 branch-growth construction.

    formation weights are (1,0,...,0).
    The first anchor fixes alpha=0.3.
    Every secondary coordinate has the same fixed-alpha three-root target 1.45.

    Returns:
        formation_weights,
        target_readout_h,
        phase,
        scalar_secondary_roots
    """
    n = int(dim)
    if n < 2:
        raise ValueError("construction requires dim>=2")
    witness = canonical_three_root_scalar_witness()
    alpha = witness["alpha"]
    phase = witness["phase"]
    h1 = dominant_mode_anchor_for_alpha(alpha)

    # With only mode 1 weighted, its exact endpoint is the ordinary scalar
    # intrinsic-Gram endpoint because alpha=y1^2/(1+y1^2).
    y1 = np.exp(-h1)
    y1p = scalar_intrinsic_gram_map(y1)
    h1p = -np.log(y1p)
    target1 = (1.0-phase)*h1 + phase*h1p

    weights = np.zeros(n, dtype=float)
    weights[0] = 1.0
    target = np.full(n, witness["target"], dtype=float)
    target[0] = target1
    return weights, target, phase, witness["roots"].copy()


@dataclass(frozen=True)
class MemoryGraphCapacity:
    dimension: int
    guaranteed_branch_lower_bound: int
    minimum_binary_bits: int


def memory_graph_capacity_lower_bound(dim: int) -> MemoryGraphCapacity:
    """Lower bound for the branch-memory graph in a dim-mode commuting stratum."""
    n = int(dim)
    branches = exponential_branch_lower_bound(n)
    bits = minimum_memory_bits_from_branch_count(branches)
    return MemoryGraphCapacity(
        dimension=n,
        guaranteed_branch_lower_bound=branches,
        minimum_binary_bits=bits,
    )


def memory_graph_capacity_sequence(max_dim: int) -> list[MemoryGraphCapacity]:
    """Capacity lower bounds for dimensions 1..max_dim."""
    m = int(max_dim)
    if m < 1:
        raise ValueError("max_dim must be positive")
    return [memory_graph_capacity_lower_bound(n) for n in range(1, m+1)]


# ---------------------------------------------------------------------------
# Carrier-dimension monotonicity and repeated-rank-growth orbit
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class OrbitRankDimensionRecord:
    step: int
    carrier_dimension: int
    persistent_rank: int
    selected_rank: int
    terminal: bool
    reason: str


def repeated_rank_growth_fixture() -> UniversalOperatorState:
    """Simple deterministic 4D state with exact rank sequence 2 -> 3 -> 4.

    The carrier dimension remains 4. This is a constructive demonstration that
    repeated persistence growth is possible without carrier growth.
    """
    p = np.diag([1.0, 1.0, 0.0, 0.0]).astype(complex)
    y = np.array(
        [
            [0.30, 0.0, 0.10, 0.0],
            [0.0, 0.40, 0.0, 0.15],
            [0.10, 0.0, 0.50, 0.0],
            [0.0, 0.15, 0.0, 0.60],
        ],
        dtype=complex,
    )
    rho_f = np.diag([0.70, 0.30, 0.0, 0.0]).astype(complex)
    rho_w = np.diag([0.50, 0.50, 0.0, 0.0]).astype(complex)

    # c+aleph=I, while D has distinct positive entries, so K=I-D has
    # nondegenerate negative structure on the emergent target sectors.
    dcap = np.diag([1.50, 1.80, 2.10, 2.50]).astype(complex)
    coherence = 0.50*np.eye(4, dtype=complex)
    emergence = 0.50*np.eye(4, dtype=complex)
    r_c = p + 0.40*(np.eye(4, dtype=complex)-p)

    return UniversalOperatorState(
        D_cap=dcap,
        coherence=coherence,
        emergence=emergence,
        formation_density=rho_f,
        witness=rho_w,
        Y=y,
        R_C=r_c,
        P_per=p,
    )


def carrier_dimension_nonincrease_bound(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-10,
) -> tuple[int, int]:
    """Return (source_dim, maximal_possible_next_dim) for the current packet.

    The cross-fed analysis map has domain H, hence rank(A)<=dim(H), regardless
    of its doubled codomain H oplus H.
    """
    validate_universal_operator_state(s, tol=max(tol, 1e-9))
    return s.dim, s.dim


def orbit_rank_dimension_trace(
    s: UniversalOperatorState,
    steps: int,
    *,
    tol: float = 1e-12,
    boundary_tol: float = 1e-10,
) -> list[OrbitRankDimensionRecord]:
    """Trace exact finite runtime ranks/dimensions until terminal or step limit."""
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    cur = s
    records = []
    for k in range(steps):
        p = _ordinary_persistent_projector(cur, tol=tol)
        p_rank = int(np.linalg.matrix_rank(p, tol=max(tol, 1e-9)))
        out = bfg_universal_state_update(
            cur, tol=tol, boundary_tol=boundary_tol
        )
        records.append(
            OrbitRankDimensionRecord(
                step=k,
                carrier_dimension=cur.dim,
                persistent_rank=p_rank,
                selected_rank=int(
                    out.diagnostics.get("persistent_rank_after_selection", 0)
                ),
                terminal=out.terminal,
                reason=out.reason,
            )
        )
        if out.terminal:
            break
        if out.state.dim > cur.dim:
            raise InadmissibleState(
                "carrier dimension increased, violating rank(A)<=dim(H)"
            )
        cur = out.state

    # Include final reached state when successful.
    if records and not records[-1].terminal:
        p = _ordinary_persistent_projector(cur, tol=tol)
        records.append(
            OrbitRankDimensionRecord(
                step=len(records),
                carrier_dimension=cur.dim,
                persistent_rank=int(
                    np.linalg.matrix_rank(p, tol=max(tol, 1e-9))
                ),
                selected_rank=int(
                    np.linalg.matrix_rank(p, tol=max(tol, 1e-9))
                ),
                terminal=False,
                reason="reached",
            )
        )
    return records


def is_full_persistent_selected_state(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-9,
) -> bool:
    """Check P=I and 0<Y<I on the current finite carrier."""
    validate_universal_operator_state(s, tol=tol)
    eye = np.eye(s.dim, dtype=complex)
    p = _ordinary_persistent_projector(s, tol=tol)
    vals = np.linalg.eigvalsh(hermitian_part(s.Y))
    return bool(
        opnorm(p-eye) <= 100*tol
        and vals.size > 0
        # Exact class condition is Y>0. Do not turn a floating resolution
        # threshold into the physical definition of strict positivity.
        and float(vals.min()) > 0.0
        and float(vals.max()) < 1.0-tol
    )


def full_persistence_lock_step(
    s: UniversalOperatorState,
    *,
    tol: float = 1e-12,
) -> BFGUniversalUpdateResult:
    """Perform one step and certify the invariant full-persistent selected class."""
    if not is_full_persistent_selected_state(s, tol=max(tol, 1e-9)):
        raise InadmissibleState("state is not in the full-persistent selected class")
    out = bfg_universal_state_update(
        s, tol=tol, boundary_tol=max(tol, 1e-12)
    )
    if out.terminal:
        raise InadmissibleState(
            f"full-persistent selected state unexpectedly stopped: {out.reason}"
        )
    if out.state.dim != s.dim:
        raise InadmissibleState("full-persistence lock changed carrier dimension")
    if not is_full_persistent_selected_state(
        out.state, tol=max(tol, 1e-8)
    ):
        raise InadmissibleState(
            "full-persistent selected class was not preserved"
        )
    return out


# ---------------------------------------------------------------------------
# Reciprocal-alpha reduction of inverse fibers
# ---------------------------------------------------------------------------

def fixed_alpha_readout_y_value(
    y: float,
    alpha: float,
    phase: float,
) -> float:
    """Exponentiated within-step readout for fixed alpha.

    If x is the closure-depth readout, this returns exp(-x/phase):
        c = y^q * (alpha + beta*y^2)/(1+y)^2,
        q=(1-phase)/phase.
    """
    y = float(y)
    alpha = float(alpha)
    w = float(phase)
    if not (0.0 < y < 1.0):
        raise ValueError("selected load requires 0<y<1")
    if not (0.0 < alpha < 0.5):
        raise ValueError("selected reciprocal alpha requires 0<alpha<1/2")
    if not (0.0 < w < 1.0):
        raise ValueError("phase must lie in (0,1)")
    beta = 1.0-alpha
    q = (1.0-w)/w
    return float(
        (y**q) * (alpha + beta*y*y) / ((1.0+y)**2)
    )


def fixed_alpha_critical_polynomial_coefficients(
    alpha: float,
    phase: float,
) -> Array:
    """Cubic numerator controlling derivative of the fixed-alpha scalar inverse map.

    For
        f(y)=y^q(alpha+beta y^2)/(1+y)^2,
    sign(f') is sign of
        P(y)=q*alpha + alpha(q-2)y + beta(q+2)y^2 + q*beta y^3.

    On y>0:
      - if q>=2 (phase<=1/3), all coefficients are nonnegative and f is
        strictly increasing;
      - if q<2, Descartes' rule gives at most two positive critical roots,
        hence at most three positive inverse roots for any target.
    """
    alpha = float(alpha)
    w = float(phase)
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must lie in (0,1)")
    if not (0.0 < w < 1.0):
        raise ValueError("phase must lie in (0,1)")
    beta = 1.0-alpha
    q = (1.0-w)/w
    # ascending powers y^0..y^3
    return np.array(
        [
            q*alpha,
            alpha*(q-2.0),
            beta*(q+2.0),
            q*beta,
        ],
        dtype=float,
    )


def fixed_alpha_max_positive_inverse_roots(
    phase: float,
) -> int:
    """Sharp structural upper bound from the derivative sign polynomial."""
    w = float(phase)
    if not (0.0 < w < 1.0):
        raise ValueError("phase must lie in (0,1)")
    q = (1.0-w)/w
    return 1 if q >= 2.0 else 3


def selected_reciprocal_alpha_from_loads(
    y: Array,
    formation_weights: Array,
) -> float:
    """Global reciprocal alpha in the selected full-persistent diagonal gauge."""
    y = np.asarray(y, dtype=float).reshape(-1)
    r = np.asarray(formation_weights, dtype=float).reshape(-1)
    if y.shape != r.shape:
        raise ValueError("shape mismatch")
    if np.any(y <= 0.0) or np.any(y >= 1.0):
        raise ValueError("selected loads require 0<y_i<1")
    if np.any(r <= 0.0):
        raise ValueError("strictly positive formation weights required")
    lc = float(np.sum(r/(1.0+y)))
    lb = float(np.sum(r*y*y/(1.0+y)))
    return lb/(lc+lb)


def alpha_conditioned_sheet_upper_bound(dim: int, phase: float) -> int:
    """Number of discrete coordinate sheets over one fixed alpha."""
    n = int(dim)
    if n < 1:
        raise ValueError("dim must be positive")
    return fixed_alpha_max_positive_inverse_roots(phase) ** n


@dataclass(frozen=True)
class AlphaFiberMemoryBound:
    dimension: int
    phase: float
    continuous_memory_dimension_upper_bound: int
    discrete_sheets_per_alpha_upper_bound: int


def alpha_fiber_memory_bound(
    dim: int,
    phase: float,
) -> AlphaFiberMemoryBound:
    """Memory-structure bound for a positive-dimensional full-persistent load fiber.

    Any positive-dimensional fiber can use alpha as a continuous coordinate.
    Conditional on alpha, each of n coordinates has at most 3 inverse roots
    (or 1 for phase<=1/3).
    """
    return AlphaFiberMemoryBound(
        dimension=int(dim),
        phase=float(phase),
        continuous_memory_dimension_upper_bound=1,
        discrete_sheets_per_alpha_upper_bound=alpha_conditioned_sheet_upper_bound(
            dim, phase
        ),
    )
