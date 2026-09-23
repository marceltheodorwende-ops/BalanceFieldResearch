from __future__ import annotations
import numpy as np
from scipy.linalg import eig
from .types import BFGState, CoreStep, NumericalPolicy
from .linalg import hermitize, invsqrt_psd, blockdiag2, g_norm_sq, normalized_spectral_distance, fro_norm, power_boundedness_diagnostic

def graph_metric(Y: np.ndarray) -> np.ndarray:
    return np.eye(Y.shape[0], dtype=complex) + hermitize(Y)

def neutral_pair(Y: np.ndarray):
    I = np.eye(Y.shape[0], dtype=complex)
    C = hermitize(np.linalg.solve(I + Y, I))
    B = hermitize(Y @ C)
    return C, B

def persistent_basis(R_C: np.ndarray, G: np.ndarray, policy: NumericalPolicy):
    vals, vecs = eig(R_C)
    mask = np.abs(np.abs(vals) - 1.0) <= policy.peripheral_tol
    W0 = vecs[:, mask]
    if W0.shape[1] == 0:
        return np.zeros((R_C.shape[0], 0), dtype=complex), vals
    gram = hermitize(W0.conj().T @ G @ W0)
    W = W0 @ invsqrt_psd(gram, policy.rank_tol)
    gram2 = hermitize(W.conj().T @ G @ W)
    ev, U = np.linalg.eigh(gram2)
    keep = ev > policy.rank_tol
    if not np.any(keep):
        return np.zeros((R_C.shape[0], 0), dtype=complex), vals
    W = W @ U[:, keep] @ np.diag(1.0 / np.sqrt(ev[keep]))
    return W, vals

def graph_projector(W: np.ndarray, G: np.ndarray) -> np.ndarray:
    if W.shape[1] == 0:
        return np.zeros_like(G)
    gram = hermitize(W.conj().T @ G @ W)
    return W @ np.linalg.solve(gram, W.conj().T @ G)

def reciprocal_order(lambda_keep: float, lambda_up: float, policy: NumericalPolicy):
    if lambda_keep <= policy.atol or lambda_up <= policy.atol:
        raise ValueError("dual persistent loads must both be positive")
    S = lambda_keep + lambda_up
    return lambda_up / S, lambda_keep / S

def polar_partial_isometry(A: np.ndarray, policy: NumericalPolicy):
    U, s, Vh = np.linalg.svd(A, full_matrices=False)
    if s.size == 0:
        return np.zeros_like(A), np.zeros((A.shape[1], 0), dtype=complex), s
    threshold = max(policy.rank_tol, policy.rtol * float(s[0]))
    r = int(np.sum(s > threshold))
    if r == 0:
        return np.zeros_like(A), np.zeros((A.shape[1], 0), dtype=complex), s
    J = U[:, :r] @ Vh[:r, :]
    V = Vh.conj().T[:, :r]
    return J, V, s

def formation_gate(K_active: np.ndarray, policy: NumericalPolicy):
    if K_active.size == 0:
        return False, float("nan"), 0.0, None
    vals, vecs = np.linalg.eigh(hermitize(K_active))
    vals = vals.real
    idx = int(np.argmin(vals))
    lam0 = float(vals[idx])
    gap = float("inf") if len(vals) == 1 else float(np.sort(vals)[1] - np.sort(vals)[0])
    ok = (lam0 < -policy.atol) and (gap > policy.simple_gap_tol)
    return ok, lam0, gap, vecs[:, idx] if ok else None

def canonical_reclosure(state: BFGState, policy: NumericalPolicy | None = None) -> CoreStep:
    policy = policy or NumericalPolicy()
    if state.terminal:
        return CoreStep(state.generation, False, state.terminal_reason or "already terminal")

    D = np.asarray(state.D, dtype=complex)
    K = hermitize(np.asarray(state.K, dtype=complex))
    Y = hermitize(np.asarray(state.Y, dtype=complex))
    R = np.asarray(state.R_C, dtype=complex)
    n = len(D)

    yvals = np.linalg.eigvalsh(Y).real
    if float(np.min(yvals)) < -policy.psd_tol:
        return CoreStep(state.generation, False, "Y is not positive semidefinite",
                        diagnostics={"min_eig_Y": float(np.min(yvals))})

    r_admission = power_boundedness_diagnostic(
        R,
        unit_tol=policy.peripheral_tol,
        grouping_tol=max(10.0*policy.peripheral_tol,1e-7),
        svd_rtol=max(policy.rtol,1e-10),
    )
    if not r_admission["power_bounded"]:
        return CoreStep(
            state.generation,
            False,
            "R_C fails finite power-boundedness admission",
            diagnostics={"recursive_admission":r_admission},
        )

    C, B = neutral_pair(Y)
    G = graph_metric(Y)
    W, rval = persistent_basis(R, G, policy)
    if W.shape[1] == 0:
        return CoreStep(state.generation, False, "no numerical bounded non-decay persistent sector",
                        C=C, B=B, G=G, diagnostics={"R_eigenvalues": rval})

    P = graph_projector(W, G)
    I = np.eye(n, dtype=complex)
    D_keep = P @ C @ D
    D_up = P @ B @ D
    D_out = (I-P) @ B @ D
    lk = g_norm_sq(D_keep, G)
    lu = g_norm_sq(D_up, G)
    try:
        wk, wu = reciprocal_order(lk, lu, policy)
    except ValueError:
        return CoreStep(state.generation, False, "dual-order failure: one persistent load vanished",
                        C=C, B=B, G=G, W=W, P=P, D_keep=D_keep, D_up=D_up,
                        D_out=D_out, lambda_keep=lk, lambda_up=lu)

    packet = np.concatenate([np.sqrt(wk)*D_keep, np.sqrt(wu)*D_up])
    A = np.vstack([np.sqrt(wk)*(P@C), np.sqrt(wu)*(P@B)])
    J, V, svals = polar_partial_isometry(A, policy)
    if V.shape[1] == 0:
        return CoreStep(state.generation, False, "polar support is empty",
                        C=C, B=B, G=G, W=W, P=P, analysis=A, J=J)

    K_plus_full = hermitize(J.conj().T @ blockdiag2(K) @ J)
    K_inh = hermitize(V.conj().T @ K @ V)
    K_succ = hermitize(V.conj().T @ K_plus_full @ V)

    gate, lam0, gap, e0 = formation_gate(K_succ, policy)
    delta = np.sqrt(-lam0)*e0 if e0 is not None else None
    mismatch = normalized_spectral_distance(K_succ, K_inh)
    novelty = bool(mismatch > policy.novelty_tol)

    Y_active = hermitize(V.conj().T @ Y @ V)
    comm = Y_active @ K_inh - K_inh @ Y_active
    comm_norm = fro_norm(comm)
    loss = float(np.real(np.trace(K_inh@K_inh) - np.trace(K_succ@K_succ)))
    py_comm = fro_norm(P@Y - Y@P)

    packet_norm = g_norm_sq(packet[:n],G) + g_norm_sq(packet[n:],G)
    input_norm = g_norm_sq(D,G)

    return CoreStep(
        generation=state.generation, success=bool(gate),
        terminal_reason=None if gate else "formation gate failed",
        C=C,B=B,G=G,W=W,P=P,D_keep=D_keep,D_up=D_up,D_out=D_out,
        lambda_keep=lk,lambda_up=lu,omega_keep=wk,omega_up=wu,
        packet=packet,analysis=A,J=J,support_basis=V,
        K_inherited=K_inh,K_successor=K_succ,
        formation_eigenvalue=lam0,formation_gap=gap,formation_vector=delta,
        spectral_novelty=novelty,spectral_mismatch=mismatch,
        commutator_norm=comm_norm,second_moment_loss=loss,
        diagnostics={
            "persistent_rank": int(W.shape[1]),
            "support_rank": int(V.shape[1]),
            "neutral_partition_residual": fro_norm(C+B-I),
            "reciprocal_balance_residual": abs(wk*lk-wu*lu),
            "graph_projector_residual": fro_norm(P.conj().T@G-G@P),
            "packet_norm_sq": packet_norm,
            "input_norm_sq": input_norm,
            "crossfed_gain": float(np.sqrt(packet_norm/max(input_norm, policy.atol))),
            "PY_commutator_norm": py_comm,
            "schur_stratum_compatible": bool(py_comm <= 100*policy.atol),
            "polar_singular_values": svals,
        }
    )
