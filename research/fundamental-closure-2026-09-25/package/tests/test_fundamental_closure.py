import numpy as np
import pytest

from bfg_lab.fundamental_closure import (
    CompletionLaw,
    FiniteState,
    IncompleteClosureLaw,
    Reconstruction,
    analysis_operator,
    closure_kernel,
    dagger,
    metric_projector,
    neutral_pair,
    peripheral_eigenbasis,
    polar_partial_isometry,
    reciprocal_weights,
    universal_update,
)


def test_neutral_pair_is_exact_partition():
    y = np.diag([0.0, 0.5, 3.0])
    c, b = neutral_pair(y)
    assert np.allclose(c + b, np.eye(3))
    assert np.all(np.linalg.eigvalsh(c) > 0)
    assert np.all(np.linalg.eigvalsh(b) >= -1e-12)


def test_reciprocal_weights_balance_products():
    load_c, load_b = 2.0, 8.0
    weight_c, weight_b = reciprocal_weights(load_c, load_b)
    assert np.isclose(weight_c + weight_b, 1.0)
    assert np.isclose(weight_c * load_c, weight_b * load_b)


def test_persistence_uses_peripheral_eigenspace():
    r = np.diag([1.0, 0.5])
    z = peripheral_eigenbasis(r)
    assert z.shape == (2, 1)
    p = z @ dagger(z)
    assert np.allclose(p, np.diag([1.0, 0.0]))


def test_metric_projector_has_declared_range_and_g_selfadjointness():
    z = np.array([[1.0], [1.0]], dtype=complex)
    g = np.diag([1.0, 3.0])
    p = metric_projector(z, g)
    assert np.allclose(p @ z, z)
    assert np.allclose(p @ p, p)
    assert np.allclose(dagger(p) @ g, g @ p)


def test_analysis_uses_endogenous_reciprocal_loads():
    y = np.diag([0.5, 2.0])
    d = np.array([1.0, 2.0], dtype=complex)
    p = np.eye(2)
    a, diag = analysis_operator(y, d, p)
    assert a.shape == (4, 2)
    assert np.isclose(diag["weight_C"] + diag["weight_B"], 1.0)
    assert np.isclose(
        diag["weight_C"] * diag["load_C"],
        diag["weight_B"] * diag["load_B"],
    )


def test_polar_partial_isometry_is_partial_isometry():
    a = np.array([[1.0, 0.0], [0.0, 0.0], [0.0, 2.0]], dtype=complex)
    j = polar_partial_isometry(a)
    s = dagger(j) @ j
    e = j @ dagger(j)
    assert np.allclose(s @ s, s)
    assert np.allclose(e @ e, e)


def test_common_positive_right_factor_cancels_from_compatible_polar_isometry():
    # Regression for the prior-art/originality boundary exposed by review.
    y = np.diag([0.2, 1.7])
    alpha, beta = 0.3, 0.7
    eye = np.eye(2)
    base = np.vstack((np.sqrt(alpha) * eye, np.sqrt(beta) * y))

    c1 = np.linalg.inv(eye + y)
    c2 = np.linalg.inv(eye + 2*y + y@y)

    j0 = polar_partial_isometry(base)
    j1 = polar_partial_isometry(base @ c1)
    j2 = polar_partial_isometry(base @ c2)

    assert np.allclose(j1, j0, atol=1e-11)
    assert np.allclose(j2, j0, atol=1e-11)


def _state():
    return FiniteState(
        D_cap=np.diag([3.0, 1.0]),
        coherence=np.diag([1.0, 2.0]),
        emergence=np.eye(2),
        d=np.array([1.0, 1.0], dtype=complex),
        R_C=np.eye(2),
        N_R=np.eye(2),
    )


def _conditional_reconstruction(state):
    n = state.dim
    # Test gauge only. This is not asserted as the universal fundamental law.
    return Reconstruction(
        B_C=np.eye(n),
        W_N=np.eye(n),
        L_C=np.eye(n),
    )


def test_closure_kernel_runs_when_reconstruction_is_supplied():
    state = _state()
    out = closure_kernel(state, _conditional_reconstruction(state))
    assert out.Y.shape == (2, 2)
    assert out.J.shape == (4, 2)
    assert out.E.shape == (4, 4)
    assert out.S.shape == (2, 2)


def test_universal_update_refuses_incomplete_completion_law():
    with pytest.raises(IncompleteClosureLaw):
        universal_update(
            _state(),
            CompletionLaw(reconstruct=_conditional_reconstruction),
        )


def test_kernel_success_is_not_falsely_promoted_to_toe_closure():
    state = _state()
    assert closure_kernel(state, _conditional_reconstruction(state)) is not None
    with pytest.raises(IncompleteClosureLaw):
        universal_update(
            state,
            CompletionLaw(reconstruct=_conditional_reconstruction),
        )


# ---------------------------------------------------------------------------
# Two-law obstruction / quotient-state regression tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    QuotientState,
    canonical_gram_factorization,
    complete_from_two_laws,
    preclosure_update,
    recursion_family,
)


def _quotient_state():
    return QuotientState(
        D_cap=np.diag([3.0, 1.0]),
        coherence=np.diag([1.0, 2.0]),
        emergence=np.eye(2),
        d=np.array([1.0, 1.0], dtype=complex),
        Y=np.eye(2),
        R_C=np.diag([1.0, 0.5]),
    )


def test_any_psd_successor_load_has_a_valid_gram_representation():
    y = np.array([[2.0, 0.3], [0.3, 1.0]], dtype=complex)
    rec = canonical_gram_factorization(y)
    assert np.allclose(rec.load(), y, atol=1e-10)


def test_preclosure_is_fixed_before_successor_load_choice():
    s = _quotient_state()
    pre = preclosure_update(s)
    assert pre.analysis.shape == (4, 2)
    assert pre.packet_support.shape == (2,)
    assert pre.formation_plus.shape == (2, 2)


def test_two_positive_successor_loads_produce_different_successor_states():
    s = _quotient_state()
    pre = preclosure_update(s)
    p = np.diag([1.0, 0.0])
    rplus = recursion_family(p, 0.5)

    out1 = complete_from_two_laws(s, pre, np.eye(2), rplus).state
    out2 = complete_from_two_laws(s, pre, 2.0 * np.eye(2), rplus).state

    assert not np.allclose(out1.d, out2.d)
    assert np.allclose(out1.Y, np.eye(2))
    assert np.allclose(out2.Y, 2.0 * np.eye(2))


def test_bounded_recursion_conditions_do_not_select_unique_decay_rate():
    p = np.diag([1.0, 0.0])
    r1 = recursion_family(p, 0.5)
    r2 = recursion_family(p, 1.0/3.0)

    assert not np.allclose(r1, r2)
    # Both share the same unit-modulus persistent eigenspace.
    z1 = peripheral_eigenbasis(r1)
    z2 = peripheral_eigenbasis(r2)
    assert np.allclose(z1 @ dagger(z1), p)
    assert np.allclose(z2 @ dagger(z2), p)
    # Both are power bounded.
    assert max(np.linalg.norm(np.linalg.matrix_power(r1, k), 2) for k in range(20)) <= 1.0 + 1e-12
    assert max(np.linalg.norm(np.linalg.matrix_power(r2, k), 2) for k in range(20)) <= 1.0 + 1e-12


# ---------------------------------------------------------------------------
# Canonical Self-Reclosure candidate tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import canonical_self_reclosure_step


def test_csr_intrinsic_gram_is_strictly_positive_on_active_carrier():
    s = QuotientState(
        D_cap=np.diag([3.0, 1.0, 1.0]),
        coherence=np.diag([1.0, 2.0, 3.0]),
        emergence=np.eye(3),
        d=np.array([1.0, 0.8, 0.5], dtype=complex),
        Y=np.array(
            [[1.0, 0.3, 0.2],
             [0.3, 1.2, 0.1],
             [0.2, 0.1, 0.8]],
            dtype=complex,
        ),
        R_C=np.diag([1.0, 0.5, 0.3]),
    )
    out = canonical_self_reclosure_step(
        s, require_simple_negative_formation=False
    )
    assert not out.terminal
    assert np.all(np.linalg.eigvalsh(out.state.Y) > 0)


def test_csr_recursion_has_exact_inherited_peripheral_space_and_strict_stable_block():
    s = QuotientState(
        D_cap=np.diag([3.0, 1.0, 1.0]),
        coherence=np.diag([1.0, 2.0, 3.0]),
        emergence=np.eye(3),
        d=np.array([1.0, 0.8, 0.5], dtype=complex),
        Y=np.array(
            [[1.0, 0.3, 0.2],
             [0.3, 1.2, 0.1],
             [0.2, 0.1, 0.8]],
            dtype=complex,
        ),
        R_C=np.diag([1.0, 0.5, 0.3]),
    )
    out = canonical_self_reclosure_step(
        s, require_simple_negative_formation=False
    )
    assert not out.terminal
    eig = np.linalg.eigvalsh(out.state.R_C)
    rank_p = np.linalg.matrix_rank(out.persistent_projector, tol=1e-9)
    assert np.sum(np.isclose(eig, 1.0, atol=1e-9)) == rank_p
    stable = eig[~np.isclose(eig, 1.0, atol=1e-9)]
    assert np.all(np.abs(stable) < 1.0)


def test_csr_has_no_free_decay_parameter():
    s = QuotientState(
        D_cap=np.diag([3.0, 1.0, 1.0]),
        coherence=np.diag([1.0, 2.0, 3.0]),
        emergence=np.eye(3),
        d=np.array([1.0, 0.8, 0.5], dtype=complex),
        Y=np.array(
            [[1.0, 0.3, 0.2],
             [0.3, 1.2, 0.1],
             [0.2, 0.1, 0.8]],
            dtype=complex,
        ),
        R_C=np.diag([1.0, 0.5, 0.3]),
    )
    a = canonical_self_reclosure_step(s, require_simple_negative_formation=False)
    b = canonical_self_reclosure_step(s, require_simple_negative_formation=False)
    assert not a.terminal and not b.terminal
    assert np.allclose(a.state.Y, b.state.Y)
    assert np.allclose(a.state.R_C, b.state.R_C)
    assert np.allclose(a.state.d, b.state.d)


def test_csr_random_finite_stability_regression():
    rng = np.random.default_rng(901)
    successes = 0
    for _ in range(100):
        n = 4
        # Random unitary basis with one protected peripheral mode.
        z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        u, _ = np.linalg.qr(z)
        stable = rng.uniform(0.05, 0.95, size=n-1)
        r_c = u @ np.diag(np.r_[1.0, stable]) @ dagger(u)

        z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        y = dagger(z) @ z / n + 0.05*np.eye(n)

        def h():
            m = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
            return (m + dagger(m))/2

        s = QuotientState(
            D_cap=h(),
            coherence=h(),
            emergence=h(),
            d=rng.normal(size=n) + 1j*rng.normal(size=n),
            Y=y,
            R_C=r_c,
        )
        out = canonical_self_reclosure_step(
            s, require_simple_negative_formation=False
        )
        if out.terminal:
            continue
        successes += 1
        assert np.all(np.linalg.eigvalsh(out.state.Y) > 0)
        assert np.linalg.norm(out.state.R_C, 2) <= 1.0 + 1e-9
        for k in (1, 2, 5, 10, 25):
            assert np.linalg.norm(
                np.linalg.matrix_power(out.state.R_C, k), 2
            ) <= 1.0 + 1e-8

    assert successes >= 95


# ---------------------------------------------------------------------------
# CSR stress audit: iteration, covariance, scalar boundary, rank and R4 geometry
# ---------------------------------------------------------------------------

from decimal import Decimal, getcontext

from bfg_lab.fundamental_closure import (
    polar_cross_stratum_projector,
    scalar_intrinsic_gram_map,
)


def _random_unitary(rng, n):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, _ = np.linalg.qr(z)
    return q


def _csr_seed(seed=17, n=4, persistent_rank=2):
    rng = np.random.default_rng(seed)

    def hermitian(scale=1.0):
        z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        return scale * (z + z.conj().T) / 2

    D = 2.0*np.eye(n) + 0.15*hermitian()
    C = 0.55*np.eye(n) + 0.08*hermitian()
    A = 0.35*np.eye(n) + 0.08*hermitian()
    d = rng.normal(size=n) + 1j*rng.normal(size=n)

    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    Y = z.conj().T @ z / n + 0.15*np.eye(n)

    U = _random_unitary(rng, n)
    vals = np.r_[np.ones(persistent_rank), rng.uniform(0.1, 0.75, n-persistent_rank)]
    R = U @ np.diag(vals) @ U.conj().T
    P = U[:, :persistent_rank] @ U[:, :persistent_rank].conj().T

    return QuotientState(
        D_cap=D, coherence=C, emergence=A, d=d, Y=Y, R_C=R, P_per=P
    )


def test_scalar_intrinsic_gram_formula_and_strict_decrease():
    for y in (1e-6, 1e-3, 0.1, 0.5, 1.0, 3.0, 100.0):
        f = scalar_intrinsic_gram_map(y)
        assert 0.0 < f < y


def test_scalar_exact_orbit_stays_positive_but_converges_to_zero():
    # High-precision arithmetic distinguishes exact asymptotic persistence from
    # floating-point underflow/ambiguity.
    getcontext().prec = 100
    y = Decimal("1")
    previous = y
    for _ in range(12):
        y = Decimal(2) * y*y / ((Decimal(1)+y)**2 * (Decimal(1)+y*y))
        assert y > 0
        assert y < previous
        previous = y
    assert y < Decimal("1e-100")


def test_persistent_rank_never_increases_with_cached_certificate():
    s = _csr_seed(seed=21, n=5, persistent_rank=2)
    old_rank = np.linalg.matrix_rank(s.P_per, tol=1e-9)
    for _ in range(5):
        out = canonical_self_reclosure_step(
            s, require_simple_negative_formation=False
        )
        if out.terminal:
            break
        new_rank = np.linalg.matrix_rank(out.state.P_per, tol=1e-9)
        assert new_rank <= old_rank
        old_rank = new_rank
        s = out.state


def test_active_rank_bound_is_at_most_twice_persistent_rank():
    s = _csr_seed(seed=22, n=7, persistent_rank=2)
    out = canonical_self_reclosure_step(
        s, require_simple_negative_formation=False
    )
    assert not out.terminal
    assert len(out.singular_values) <= 2 * np.linalg.matrix_rank(s.P_per, tol=1e-9)


def test_r4_subspace_transport_matches_csr_surviving_persistence():
    s = _csr_seed(seed=23, n=6, persistent_rank=2)
    out = canonical_self_reclosure_step(
        s, require_simple_negative_formation=False
    )
    assert not out.terminal

    V = out.source_active_frame
    S = V @ V.conj().T
    Pold = s.P_per

    _, r4_final = polar_cross_stratum_projector(Pold, S)

    # CSR target persistence pulled back from active coordinates to source H.
    csr_final_in_source = V @ out.persistent_projector @ V.conj().T

    assert np.allclose(r4_final, csr_final_in_source, atol=1e-8)


def test_unitary_covariance_up_to_target_coordinate_gauge():
    rng = np.random.default_rng(24)
    s = _csr_seed(seed=24, n=5, persistent_rank=2)
    out = canonical_self_reclosure_step(
        s, require_simple_negative_formation=False
    )
    assert not out.terminal

    U = _random_unitary(rng, s.dim)
    su = QuotientState(
        D_cap=U@s.D_cap@U.conj().T,
        coherence=U@s.coherence@U.conj().T,
        emergence=U@s.emergence@U.conj().T,
        d=U@s.d,
        Y=U@s.Y@U.conj().T,
        R_C=U@s.R_C@U.conj().T,
        P_per=U@s.P_per@U.conj().T,
    )
    outu = canonical_self_reclosure_step(
        su, require_simple_negative_formation=False
    )
    assert not outu.terminal

    # Target SVD frames are allowed to differ by an internal unitary gauge.
    U2 = np.block([[U, np.zeros_like(U)], [np.zeros_like(U), U]])
    Q = outu.target_frame.conj().T @ U2 @ out.target_frame
    assert np.allclose(Q.conj().T @ Q, np.eye(Q.shape[0]), atol=1e-8)

    for name in ("D_cap", "coherence", "emergence", "Y", "R_C", "P_per"):
        lhs = getattr(outu.state, name)
        rhs = Q @ getattr(out.state, name) @ Q.conj().T
        assert np.allclose(lhs, rhs, atol=2e-8)

    assert np.allclose(outu.state.d, Q @ out.state.d, atol=2e-8)


def test_multistep_runtime_uses_certificate_and_never_fabricates_persistence():
    s = _csr_seed(seed=25, n=6, persistent_rank=2)
    ranks = [np.linalg.matrix_rank(s.P_per, tol=1e-9)]
    successful = 0
    for _ in range(8):
        out = canonical_self_reclosure_step(
            s, require_simple_negative_formation=False
        )
        if out.terminal:
            break
        successful += 1
        s = out.state
        ranks.append(np.linalg.matrix_rank(s.P_per, tol=1e-9))
        assert np.linalg.norm(s.R_C, 2) <= 1.0 + 1e-9
        assert np.all(np.linalg.eigvalsh(s.Y) > 0)
    assert successful >= 2
    assert all(b <= a for a, b in zip(ranks, ranks[1:]))


# ---------------------------------------------------------------------------
# Two-density rank-aware universal operator state
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    UniversalOperatorState,
    density_reciprocal_analysis,
    universal_operator_step,
    validate_universal_operator_state,
)


def _rank_one_density(v):
    v = np.asarray(v, dtype=complex)
    return np.outer(v, v.conj())


def test_density_loads_reduce_exactly_to_rank_one_vector_loads():
    y = np.array([[1.0, 0.35], [0.35, 1.3]], dtype=complex)
    p = np.eye(2, dtype=complex)
    d = np.array([1.2+0.3j, -0.7+0.4j])
    rho = _rank_one_density(d)

    a_rho, diag_rho = density_reciprocal_analysis(y, rho, p)
    a_d, diag_d = analysis_operator(y, d, p)

    assert np.allclose(a_rho, a_d, atol=1e-10)
    assert np.isclose(diag_rho["load_C"], diag_d["load_C"])
    assert np.isclose(diag_rho["load_B"], diag_d["load_B"])


def test_global_phase_disappears_from_formation_density():
    d = np.array([1.0+0.2j, -0.4+0.7j])
    theta = 0.731
    assert np.allclose(
        _rank_one_density(d),
        _rank_one_density(np.exp(1j*theta)*d),
        atol=1e-12,
    )


def _rank_increase_state():
    # Source persistence rank 1, while the cross-fed analysis has active rank 2.
    y = np.array([[1.0, 0.4], [0.4, 1.2]], dtype=complex)
    p = np.diag([1.0, 0.0]).astype(complex)
    # K=-I gives a unique negative ground on any 1D emergent sector.
    D = 2.0*np.eye(2)
    C = 0.5*np.eye(2)
    A = 0.5*np.eye(2)
    rho_f = p.copy()
    rho_w = p.copy()  # already unit trace
    r = np.diag([1.0, 0.4]).astype(complex)
    return UniversalOperatorState(
        D_cap=D,
        coherence=C,
        emergence=A,
        formation_density=rho_f,
        witness=rho_w,
        Y=y,
        R_C=r,
        P_per=p,
    )


def test_rank_aware_step_can_increase_persistent_rank_without_witness_fabrication():
    s = _rank_increase_state()
    out = universal_operator_step(s)
    assert not out.terminal, out.reason

    old_rank = np.linalg.matrix_rank(s.P_per, tol=1e-9)
    new_rank = np.linalg.matrix_rank(out.state.P_per, tol=1e-9)
    assert old_rank == 1
    assert new_rank == 2

    # Identity witness remains entirely in inherited support.
    assert np.linalg.norm(
        out.emergent_projector @ out.state.witness
    ) < 1e-9

    # Formation density has a genuine emergent component.
    emergent_mass = np.trace(
        out.emergent_projector @ out.state.formation_density
    ).real
    assert emergent_mass > 1e-8

    assert np.isclose(np.trace(out.state.witness).real, 1.0)
    assert np.all(np.linalg.eigvalsh(out.state.formation_density) >= -1e-9)
    assert np.linalg.norm(out.state.R_C, 2) <= 1.0 + 1e-9


def test_rank_aware_update_keeps_formation_and_identity_semantically_separate():
    s = _rank_increase_state()
    out = universal_operator_step(s)
    assert not out.terminal
    e = out.emergent_projector

    assert np.linalg.norm(e @ out.state.witness) < 1e-9
    assert np.trace(e @ out.state.formation_density).real > 1e-8


def test_rank_aware_state_rejects_identity_witness_outside_persistence():
    s = _rank_increase_state()
    bad = UniversalOperatorState(
        D_cap=s.D_cap,
        coherence=s.coherence,
        emergence=s.emergence,
        formation_density=s.formation_density,
        witness=0.5*np.eye(2),
        Y=s.Y,
        R_C=s.R_C,
        P_per=s.P_per,
    )
    with pytest.raises(Exception):
        validate_universal_operator_state(bad)


def test_degenerate_negative_emergent_block_triggers_no_choice_terminal():
    # Persistent rank 2, active rank 4, K=-I => 2D emergent block with
    # degenerate negative ground.
    y = np.array(
        [[2.0, 0.0, 0.4, 0.0],
         [0.0, 2.0, 0.0, 0.5],
         [0.4, 0.0, 1.0, 0.0],
         [0.0, 0.5, 0.0, 1.2]],
        dtype=complex,
    )
    p = np.diag([1.0, 1.0, 0.0, 0.0]).astype(complex)
    rho_f = p / 2.0
    rho_w = p / 2.0
    s = UniversalOperatorState(
        D_cap=2.0*np.eye(4),
        coherence=0.5*np.eye(4),
        emergence=0.5*np.eye(4),
        formation_density=rho_f,
        witness=rho_w,
        Y=y,
        R_C=np.diag([1.0, 1.0, 0.4, 0.3]).astype(complex),
        P_per=p,
    )
    out = universal_operator_step(s)
    assert out.terminal
    assert out.reason == "emergent_ground_degenerate"


def test_rank_aware_update_is_iterable_after_seeded_rank_increase():
    s = _rank_increase_state()
    out1 = universal_operator_step(s)
    assert not out1.terminal, out1.reason

    # After the first rank increase the whole 2D target is persistent. A second
    # exact step should require no emergent seed.
    out2 = universal_operator_step(out1.state)
    assert not out2.terminal, out2.reason
    assert np.linalg.matrix_rank(out2.state.P_per, tol=1e-9) == 2
    assert np.isclose(np.trace(out2.state.witness).real, 1.0)


def test_exact_active_support_contains_entire_old_persistent_space():
    rng = np.random.default_rng(311)
    for _ in range(50):
        n = 5
        p_rank = 2
        U = _random_unitary(rng, n)
        P = U[:, :p_rank] @ U[:, :p_rank].conj().T

        z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        Y = z.conj().T @ z / n + 0.2*np.eye(n)
        G = np.eye(n) + Y
        Z = U[:, :p_rank]
        Pg = metric_projector(Z, G)

        # Full-rank formation density ensures positive dual loads generically.
        rho_f = np.eye(n) / n
        A, _ = density_reciprocal_analysis(Y, rho_f, Pg)

        _, svals, vh = np.linalg.svd(A, full_matrices=False)
        rank = np.count_nonzero(svals > 1e-10 * svals[0])
        V = vh[:rank, :].conj().T
        S = V @ V.conj().T

        assert np.linalg.norm((np.eye(n)-S) @ P, 2) < 2e-8


def test_exact_generated_active_support_retains_all_supported_witness_mass():
    s = _rank_increase_state()
    out = universal_operator_step(s)
    assert not out.terminal
    assert np.isclose(out.retained_witness_mass, 1.0, atol=1e-9)


def test_generated_persistent_rank_is_nondecreasing_in_short_exact_sequence():
    s = _rank_increase_state()
    ranks = [np.linalg.matrix_rank(s.P_per, tol=1e-9)]
    for _ in range(4):
        out = universal_operator_step(s)
        assert not out.terminal, out.reason
        s = out.state
        ranks.append(np.linalg.matrix_rank(s.P_per, tol=1e-9))
    assert all(b >= a for a, b in zip(ranks, ranks[1:]))


def test_two_density_unitary_covariance_up_to_target_gauge():
    rng = np.random.default_rng(313)
    s = _rank_increase_state()
    out = universal_operator_step(s)
    assert not out.terminal

    U = _random_unitary(rng, s.dim)
    su = UniversalOperatorState(
        D_cap=U@s.D_cap@U.conj().T,
        coherence=U@s.coherence@U.conj().T,
        emergence=U@s.emergence@U.conj().T,
        formation_density=U@s.formation_density@U.conj().T,
        witness=U@s.witness@U.conj().T,
        Y=U@s.Y@U.conj().T,
        R_C=U@s.R_C@U.conj().T,
        P_per=U@s.P_per@U.conj().T,
    )
    outu = universal_operator_step(su)
    assert not outu.terminal

    # Find a target gauge by aligning eigenframes of Y; distinct singular values
    # in this deterministic example make the gauge stable up to phases.
    vals, V1 = np.linalg.eigh(out.state.Y)
    vals_u, V2 = np.linalg.eigh(outu.state.Y)
    assert np.allclose(vals, vals_u, atol=1e-9)

    # Compare unitary invariants, which are gauge-independent.
    for name in ("formation_density", "witness", "Y", "R_C", "P_per"):
        a = getattr(out.state, name)
        b = getattr(outu.state, name)
        assert np.allclose(
            np.linalg.eigvalsh((a+a.conj().T)/2),
            np.linalg.eigvalsh((b+b.conj().T)/2),
            atol=1e-8,
        )
    assert np.isclose(out.retained_witness_mass, outu.retained_witness_mass, atol=1e-9)


# ---------------------------------------------------------------------------
# Exact Selection / Export stratum law
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    closure_gain_selector,
    witness_transport_between_projectors,
)


def test_closure_gain_selector_exact_rank_decrease_case():
    delta = np.diag([2.0, -1.0, -3.0]).astype(complex)
    sel = closure_gain_selector(delta)
    assert not sel.ambiguous
    assert np.allclose(sel.retained_projector, np.diag([1.0, 0.0, 0.0]))
    assert np.allclose(sel.export_projector, np.diag([0.0, 1.0, 1.0]))


def test_closure_gain_selector_exact_rank_increase_case():
    delta = np.diag([2.0, 1.0, -3.0]).astype(complex)
    sel = closure_gain_selector(delta)
    assert not sel.ambiguous
    assert np.linalg.matrix_rank(sel.retained_projector, tol=1e-9) == 2


def test_closure_gain_selector_reports_zero_boundary_ambiguity_numerically():
    delta = np.diag([1.0, 0.0, -1.0]).astype(complex)
    sel = closure_gain_selector(delta, zero_tol=1e-12)
    assert sel.ambiguous
    assert sel.reason == "closure_gain_sign_ambiguity"


def test_selection_plus_r4_transport_records_partial_witness_loss():
    q_minus = np.eye(2, dtype=complex)
    q_plus = np.diag([1.0, 0.0]).astype(complex)
    rho = np.diag([0.7, 0.3]).astype(complex)

    out = witness_transport_between_projectors(rho, q_minus, q_plus)
    assert not out.terminal
    assert np.isclose(out.retained_mass, 0.7)
    assert np.isclose(out.lost_mass, 0.3)
    assert np.allclose(out.witness_plus, np.diag([1.0, 0.0]))


def test_selection_plus_r4_transport_terminates_on_total_identity_loss():
    q_minus = np.diag([1.0, 0.0]).astype(complex)
    q_plus = np.diag([0.0, 1.0]).astype(complex)
    rho = np.diag([1.0, 0.0]).astype(complex)

    out = witness_transport_between_projectors(rho, q_minus, q_plus)
    assert out.terminal
    assert out.reason == "witness_annihilated"
    assert np.isclose(out.retained_mass, 0.0)


def test_selection_rule_is_unitarily_covariant():
    rng = np.random.default_rng(410)
    delta = np.diag([3.0, 1.0, -2.0]).astype(complex)
    sel = closure_gain_selector(delta)
    U = _random_unitary(rng, 3)
    sel_u = closure_gain_selector(U @ delta @ U.conj().T)

    assert not sel.ambiguous and not sel_u.ambiguous
    assert np.allclose(
        sel_u.retained_projector,
        U @ sel.retained_projector @ U.conj().T,
        atol=1e-9,
    )


def test_current_bfg_state_does_not_uniquely_choose_closure_gain_selector():
    K = np.diag([-1.0, 1.0]).astype(complex)
    Y = np.eye(2, dtype=complex)

    candidate_1 = closure_gain_selector(-K)
    candidate_2 = closure_gain_selector(Y)

    assert not candidate_1.ambiguous
    assert not candidate_2.ambiguous
    assert np.linalg.matrix_rank(candidate_1.retained_projector, tol=1e-9) == 1
    assert np.linalg.matrix_rank(candidate_2.retained_projector, tol=1e-9) == 2


# ---------------------------------------------------------------------------
# Neutral-Contrast Closure Gain
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    neutral_contrast,
    neutral_contrast_selector,
    neutral_contrast_universal_step,
)


def test_neutral_contrast_matches_exact_retained_minus_complementary_pair():
    y = np.diag([0.2, 1.0, 3.0]).astype(complex)
    c, b = neutral_pair(y)
    z = neutral_contrast(y)
    assert np.allclose(z, c-b)
    assert np.allclose(
        np.diag(z).real,
        [(1-.2)/(1+.2), 0.0, (1-3)/(1+3)],
    )


def test_neutral_contrast_selector_is_exactly_y_less_than_one():
    y = np.diag([0.2, 0.9, 1.2, 4.0]).astype(complex)
    sel = neutral_contrast_selector(y, boundary_tol=1e-12)
    assert not sel.ambiguous
    assert np.allclose(
        sel.retained_projector,
        np.diag([1.0, 1.0, 0.0, 0.0]),
    )
    assert np.allclose(
        sel.export_projector,
        np.diag([0.0, 0.0, 1.0, 1.0]),
    )


def test_neutral_contrast_boundary_is_not_silently_decided_numerically():
    y = np.diag([0.5, 1.0, 2.0]).astype(complex)
    sel = neutral_contrast_selector(y, boundary_tol=1e-12)
    assert sel.ambiguous
    assert sel.reason == "neutral_contrast_boundary_ambiguity"


def _contrast_demotion_state():
    # Deterministic state discovered by a fixed random audit. Its cross-fed
    # intrinsic Gram has one eigenvalue below and one above 1.
    Y = np.array(
        [[ 5.79509886+0j,  1.83200172-0.00126817j, -1.07064170+2.62755502j],
         [ 1.83200172+0.00126817j, 1.00392931+0j,  0.60642640+0.70123496j],
         [-1.07064170-2.62755502j, 0.60642640-0.70123496j, 4.37327647+0j]],
        dtype=complex,
    )
    P_rounded = np.array(
        [[0.48764191+0j, 0.08219440+0.38908502j, 0.08026603-0.29199584j],
         [0.08219440-0.38908502j, 0.32430165+0j, -0.21945158-0.11326084j],
         [0.08026603+0.29199584j, -0.21945158+0.11326084j, 0.18805644+0j]],
        dtype=complex,
    )
    # Recover the exact rank-one projector instead of treating rounded printed
    # matrix entries as an exact projector.
    _pv, _pu = np.linalg.eigh((P_rounded + P_rounded.conj().T)/2)
    _w = _pu[:, [-1]]
    P = _w @ _w.conj().T
    d = np.array(
        [0.31558697+0.45362104j, 0.33201950-0.44138107j, 0.60239130+1.89932670j],
        dtype=complex,
    )
    # Use a simple negative formation operator K=-I so any 1D emergent selected
    # sector has a canonical seed.
    D = 2.0*np.eye(3, dtype=complex)
    C = 0.5*np.eye(3, dtype=complex)
    A = 0.5*np.eye(3, dtype=complex)

    # Rank-one source witness on the persistent line.
    vals, vecs = np.linalg.eigh(P)
    w = vecs[:, [np.argmax(vals)]]
    rho_w = w @ w.conj().T
    rho_f = np.outer(d, d.conj())

    # Any contraction with exact persistent projector P suffices for the source
    # state because P_per is the certified persistent range.
    R = P + 0.4*(np.eye(3)-P)

    return UniversalOperatorState(
        D_cap=D,
        coherence=C,
        emergence=A,
        formation_density=rho_f,
        witness=rho_w,
        Y=Y,
        R_C=R,
        P_per=P,
    )


def test_neutral_contrast_step_has_nontrivial_export_sector():
    s = _contrast_demotion_state()
    out = neutral_contrast_universal_step(s, boundary_tol=1e-8)
    assert not out.terminal, out.reason
    assert np.linalg.matrix_rank(out.export_projector, tol=1e-8) >= 1
    assert np.any(np.linalg.eigvalsh(out.state.Y) > 1.0)


def test_neutral_contrast_generated_export_does_not_fabricate_persistence():
    s = _contrast_demotion_state()
    old_rank = np.linalg.matrix_rank(s.P_per, tol=1e-8)
    out = neutral_contrast_universal_step(s, boundary_tol=1e-8)
    assert not out.terminal, out.reason
    new_rank = np.linalg.matrix_rank(out.state.P_per, tol=1e-8)

    # This deterministic case proves a nontrivial export sector, but not an
    # inherited-rank decrease. Do not overclaim more than the example shows.
    assert np.linalg.matrix_rank(out.export_projector, tol=1e-8) == 1
    assert new_rank == old_rank
    assert out.retained_witness_mass <= 1.0 + 1e-9



def test_neutral_contrast_step_preserves_no_fabricated_witness():
    s = _contrast_demotion_state()
    out = neutral_contrast_universal_step(s, boundary_tol=1e-8)
    assert not out.terminal, out.reason
    # Witness remains supported on the final persistent projector.
    p = out.state.P_per
    assert np.linalg.norm(
        out.state.witness - p @ out.state.witness @ p
    ) < 1e-8


def test_neutral_contrast_selector_is_unitarily_covariant():
    rng = np.random.default_rng(515)
    y = np.diag([0.2, 0.7, 1.4]).astype(complex)
    U = _random_unitary(rng, 3)
    s0 = neutral_contrast_selector(y)
    s1 = neutral_contrast_selector(U@y@U.conj().T)
    assert not s0.ambiguous and not s1.ambiguous
    assert np.allclose(
        s1.retained_projector,
        U@s0.retained_projector@U.conj().T,
        atol=1e-9,
    )


def test_neutral_contrast_step_random_batch_is_power_bounded_when_successful():
    rng = np.random.default_rng(516)
    successes = 0
    for _ in range(150):
        n = 4
        p_rank = 1
        U = _random_unitary(rng, n)
        P = U[:, :p_rank] @ U[:, :p_rank].conj().T
        z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
        Y = z.conj().T@z/n + 0.05*np.eye(n)
        d = rng.normal(size=n) + 1j*rng.normal(size=n)
        rho_f = np.outer(d,d.conj())
        rho_w = P / np.trace(P).real
        s = UniversalOperatorState(
            D_cap=2*np.eye(n),
            coherence=0.5*np.eye(n),
            emergence=0.5*np.eye(n),
            formation_density=rho_f,
            witness=rho_w,
            Y=Y,
            R_C=P+0.4*(np.eye(n)-P),
            P_per=P,
        )
        out = neutral_contrast_universal_step(
            s, boundary_tol=1e-9
        )
        if out.terminal:
            continue
        successes += 1
        assert np.linalg.norm(out.state.R_C, 2) <= 1.0 + 1e-8
        assert np.isclose(np.trace(out.state.witness).real,1.0,atol=1e-8)
        assert np.all(np.linalg.eigvalsh(out.state.formation_density) >= -1e-8)
    assert successes >= 120


# ---------------------------------------------------------------------------
# Official universal-update candidate wrapper
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import bfg_universal_state_update


def test_official_candidate_wrapper_matches_selection_first_step():
    s = _source_demotion_state()
    direct = selection_first_universal_step(s, boundary_tol=1e-8)
    wrapped = bfg_universal_state_update(s, boundary_tol=1e-8)

    assert wrapped.terminal == direct.terminal
    assert wrapped.reason == direct.reason
    if not wrapped.terminal:
        assert np.allclose(wrapped.state.Y, direct.state.Y)
        assert np.allclose(wrapped.state.R_C, direct.state.R_C)
        assert np.allclose(wrapped.state.witness, direct.state.witness)


def test_official_candidate_exposes_auditable_diagnostics():
    s = _rank_increase_state()
    out = bfg_universal_state_update(s)
    assert "law" in out.diagnostics
    assert "epistemic_status" in out.diagnostics
    assert out.diagnostics["terminal"] == out.terminal


# ---------------------------------------------------------------------------
# Selection-first master ordering
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import selection_first_universal_step


def _source_demotion_state():
    # Current Y has only one closure-positive eigenmode (y<1), while the
    # persistent source has rank 2. This creates an exact pre-reclosure demotion.
    Y = np.diag([0.4, 2.0, 3.0]).astype(complex)
    P = np.diag([1.0, 1.0, 0.0]).astype(complex)
    rho_w = P / 2.0

    # Put formation on both persistent modes so the retained one survives.
    rho_f = np.diag([1.0, 1.0, 0.0]).astype(complex)

    # Simple negative K on the carrier.
    D = 2.0*np.eye(3)
    C = 0.5*np.eye(3)
    A = 0.5*np.eye(3)

    return UniversalOperatorState(
        D_cap=D,
        coherence=C,
        emergence=A,
        formation_density=rho_f,
        witness=rho_w,
        Y=Y,
        R_C=P + 0.4*(np.eye(3)-P),
        P_per=P,
    )


def test_selection_first_stage_generates_exact_persistent_rank_loss():
    s = _source_demotion_state()
    out = selection_first_universal_step(s)
    assert not out.terminal, out.reason
    assert out.persistent_rank_before == 2
    assert out.persistent_rank_after_selection == 1
    assert np.isclose(out.retained_witness_mass, 0.5, atol=1e-9)


def test_selection_first_stage_records_exact_witness_loss():
    s = _source_demotion_state()
    out = selection_first_universal_step(s)
    assert not out.terminal
    assert np.isclose(out.retained_witness_mass, 0.5, atol=1e-9)
    assert np.isclose(np.trace(out.state.witness).real, 1.0, atol=1e-9)


def test_official_wrapper_uses_selection_first_ordering():
    s = _source_demotion_state()
    out = bfg_universal_state_update(s)
    assert not out.terminal, out.reason
    assert out.diagnostics["persistent_rank_before"] == 2
    assert out.diagnostics["persistent_rank_after_selection"] == 1
    assert np.isclose(out.diagnostics["retained_witness_mass"], 0.5, atol=1e-9)


# ---------------------------------------------------------------------------
# Exact dual-load terminal theorem / numerical-boundary discipline
# ---------------------------------------------------------------------------

def test_exact_y_zero_is_true_dual_load_terminal():
    y = np.zeros((2, 2), dtype=complex)
    rho = np.eye(2, dtype=complex) / 2
    p = np.eye(2, dtype=complex)
    with pytest.raises(Exception) as exc:
        density_reciprocal_analysis(y, rho, p, tol=1e-12)
    assert "dual_load_zero_terminal" in str(exc.value)


def test_exact_kernel_supported_formation_can_zero_upward_load():
    y = np.diag([0.0, 2.0]).astype(complex)
    rho = np.diag([1.0, 0.0]).astype(complex)
    p = np.eye(2, dtype=complex)
    with pytest.raises(Exception) as exc:
        density_reciprocal_analysis(y, rho, p, tol=1e-12)
    assert "dual_load_zero_terminal" in str(exc.value)


def test_tiny_positive_load_is_not_relabelled_exact_terminal():
    y = np.array([[1e-12]], dtype=complex)
    rho = np.array([[1.0]], dtype=complex)
    p = np.array([[1.0]], dtype=complex)
    with pytest.raises(Exception) as exc:
        density_reciprocal_analysis(y, rho, p, tol=1e-10)
    assert "dual_load_numerical_ambiguity" in str(exc.value)
    assert "zero_terminal" not in str(exc.value)


def test_dual_packet_energy_vanishes_when_either_exact_load_vanishes():
    # Reciprocal-balance packet energy:
    # E = 2 l_C l_B / (l_C + l_B).
    for lc, lb in ((2.0, 0.0), (0.0, 3.0)):
        s = lc + lb
        energy = 0.0 if s == 0 else 2.0 * lc * lb / s
        assert energy == 0.0


def test_positive_dual_loads_give_positive_packet_energy():
    lc, lb = 2.0, 3.0
    energy = 2.0 * lc * lb / (lc + lb)
    assert energy > 0.0


# ---------------------------------------------------------------------------
# Exact forward-orbit invariant tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    generated_state_certificate,
    raw_density_loads,
    scalar_intrinsic_gram_quadratic_bounds,
)


def test_generated_rank_increase_state_has_strict_positive_load_invariant():
    out = bfg_universal_state_update(_rank_increase_state())
    assert not out.terminal, out.reason
    cert = generated_state_certificate(out.state)
    assert cert.y_min > 0.0
    assert cert.formation_support_residual < 1e-8
    assert cert.witness_support_residual < 1e-8
    assert cert.load_C > 0.0
    assert cert.load_B > 0.0


def test_generated_demotion_state_has_strict_positive_load_invariant():
    out = bfg_universal_state_update(_source_demotion_state())
    assert not out.terminal, out.reason
    cert = generated_state_certificate(out.state)
    assert cert.y_min > 0.0
    assert cert.formation_support_residual < 1e-8
    assert cert.witness_support_residual < 1e-8
    assert cert.load_C > 0.0
    assert cert.load_B > 0.0


def test_retained_and_complementary_branch_maps_are_injective_on_persistent_space():
    rng = np.random.default_rng(620)
    for _ in range(50):
        n = 5
        p = 2
        U = _random_unitary(rng, n)
        Z = U[:, :p]
        Yraw = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
        Y = Yraw.conj().T @ Yraw / n + 0.2*np.eye(n)
        G = np.eye(n) + Y
        Pg = metric_projector(Z, G)
        C, B = neutral_pair(Y)

        AC = Pg @ C @ Z
        AB = Pg @ B @ Z
        assert np.linalg.matrix_rank(AC, tol=1e-9) == p
        assert np.linalg.matrix_rank(AB, tol=1e-9) == p


def test_successful_generated_orbit_never_reports_exact_dual_load_zero_later():
    s = _rank_increase_state()
    successful = 0
    for _ in range(10):
        out = bfg_universal_state_update(s, tol=1e-14, boundary_tol=1e-12)
        if out.terminal:
            assert out.reason != "dual_load_zero_terminal"
            break
        successful += 1
        cert = generated_state_certificate(out.state, tol=1e-14)
        assert cert.load_C > 0.0
        assert cert.load_B > 0.0
        s = out.state
    assert successful >= 1


def test_dimension_and_persistent_rank_growth_bounds_hold_for_successful_steps():
    rng = np.random.default_rng(621)
    checked = 0
    for _ in range(100):
        n = 4
        p = 1
        U = _random_unitary(rng, n)
        P = U[:, :p] @ U[:, :p].conj().T
        z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
        Y = z.conj().T @ z / n + 0.05*np.eye(n)
        d = rng.normal(size=n) + 1j*rng.normal(size=n)
        s = UniversalOperatorState(
            D_cap=2*np.eye(n),
            coherence=0.5*np.eye(n),
            emergence=0.5*np.eye(n),
            formation_density=np.outer(d,d.conj()),
            witness=P,
            Y=Y,
            R_C=P+0.4*(np.eye(n)-P),
            P_per=P,
        )
        out = bfg_universal_state_update(s, boundary_tol=1e-9)
        if out.terminal:
            continue
        checked += 1
        p0 = out.diagnostics["persistent_rank_before"]
        psel = out.diagnostics["persistent_rank_after_selection"]
        p1 = out.diagnostics["persistent_rank_after_reclosure"]
        h1 = out.diagnostics["active_rank_after_reclosure"]
        assert psel <= p0
        assert h1 <= 2*psel
        assert p1 <= psel + 1
    assert checked >= 20


def test_scalar_quadratic_bounds_are_exactly_respected():
    for y in (1e-8, 1e-4, 0.01, 0.1, 0.5, 1.0):
        lo, exact, hi = scalar_intrinsic_gram_quadratic_bounds(y)
        assert lo <= exact <= hi
        assert exact > 0.0


# ---------------------------------------------------------------------------
# Closure-depth coordinate tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    closure_depth,
    load_from_closure_depth,
    neutral_from_closure_depth,
    scalar_closure_depth_update,
    scalar_renormalized_depth,
)


def test_closure_depth_is_exact_inverse_coordinate_for_positive_load():
    y = np.array([[1.3, 0.2], [0.2, 0.7]], dtype=complex)
    h = closure_depth(y)
    y2 = load_from_closure_depth(h)
    assert np.allclose(y2, y, atol=1e-10)


def test_neutral_pair_and_contrast_match_closure_depth_tanh_form():
    y = np.array([[1.3, 0.2], [0.2, 0.7]], dtype=complex)
    h = closure_depth(y)
    c_h, b_h, z_h = neutral_from_closure_depth(h)
    c, b = neutral_pair(y)
    z = neutral_contrast(y)
    assert np.allclose(c_h, c, atol=1e-10)
    assert np.allclose(b_h, b, atol=1e-10)
    assert np.allclose(z_h, z, atol=1e-10)


def test_closure_depth_selection_sign_matches_y_less_than_one():
    y = np.diag([0.2, 0.8, 1.4, 3.0]).astype(complex)
    h = closure_depth(y)
    vals_h = np.linalg.eigvalsh(h)
    assert np.sum(vals_h > 0) == 2
    sel = neutral_contrast_selector(y)
    assert np.linalg.matrix_rank(sel.retained_projector, tol=1e-9) == 2


def test_scalar_depth_update_matches_log_of_scalar_y_update():
    for y in (0.1, 0.3, 0.7, 1.0):
        h = -np.log(y)
        hp = scalar_closure_depth_update(h)
        yp = scalar_intrinsic_gram_map(y)
        assert np.isclose(hp, -np.log(yp), rtol=1e-12, atol=1e-12)


def test_scalar_renormalized_depth_converges_numerically():
    vals = [scalar_renormalized_depth(0.0, n) for n in (12, 16, 20, 24, 28)]
    diffs = [abs(b-a) for a, b in zip(vals, vals[1:])]
    assert all(b < a for a, b in zip(diffs, diffs[1:]))
    assert diffs[-1] < 1e-6
    assert abs(vals[-1] - 0.49338728) < 1e-7


# ---------------------------------------------------------------------------
# Exact selected-scalar continuous embedding
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    scalar_bottcher_coordinate,
    scalar_bottcher_depth,
    scalar_bottcher_depth_from_h,
    scalar_recursive_time_flow_h,
    scalar_recursive_time_flow_y,
    scalar_recursive_time_generator_h,
    scalar_recursive_time_generator_y,
)


def test_scalar_map_sends_all_positive_inputs_below_or_equal_quarter():
    ys = np.logspace(-8, 8, 2000)
    vals = np.array([scalar_intrinsic_gram_map(y) for y in ys])
    assert vals.max() <= 0.25 + 1e-12


def test_scalar_map_has_reciprocal_branch_symmetry():
    for y in (0.02, 0.2, 0.7, 2.0, 7.0, 50.0):
        assert np.isclose(
            scalar_intrinsic_gram_map(y),
            scalar_intrinsic_gram_map(1.0/y),
            rtol=1e-12,
            atol=1e-12,
        )


def test_bottcher_depth_functional_equation():
    for y in (0.05, 0.2, 0.5, 0.9, 1.0):
        lhs = scalar_bottcher_depth(
            scalar_intrinsic_gram_map(y),
            iterations=55,
        )
        rhs = 2.0 * scalar_bottcher_depth(y, iterations=55)
        assert np.isclose(lhs, rhs, rtol=2e-11, atol=2e-11)


def test_bottcher_coordinate_squares_under_one_discrete_step():
    for y in (0.05, 0.2, 0.5, 0.9, 1.0):
        phi = scalar_bottcher_coordinate(y, iterations=55)
        phi_next = scalar_bottcher_coordinate(
            scalar_intrinsic_gram_map(y),
            iterations=55,
        )
        assert np.isclose(phi_next, phi*phi, rtol=2e-11, atol=2e-11)


def test_continuous_recursive_flow_exactly_recovers_one_discrete_step():
    tau = np.log(2.0)
    for y in (0.05, 0.2, 0.5, 0.9, 1.0):
        continuous = scalar_recursive_time_flow_y(
            y, tau, iterations=55
        )
        discrete = scalar_intrinsic_gram_map(y)
        assert np.isclose(continuous, discrete, rtol=2e-9, atol=2e-11)


def test_continuous_recursive_flow_has_semigroup_property():
    y0 = 0.73
    a = 0.17
    b = 0.29
    direct = scalar_recursive_time_flow_y(
        y0, a+b, iterations=55
    )
    staged = scalar_recursive_time_flow_y(
        scalar_recursive_time_flow_y(y0, a, iterations=55),
        b,
        iterations=55,
    )
    assert np.isclose(direct, staged, rtol=3e-9, atol=3e-11)


def test_recursive_time_generator_has_correct_signs():
    for y in (0.05, 0.2, 0.5, 0.9):
        gy = scalar_recursive_time_generator_y(y, iterations=50)
        gh = scalar_recursive_time_generator_h(-np.log(y), iterations=50)
        assert gy < 0.0
        assert gh > 0.0


def test_generator_matches_short_recursive_time_flow():
    y0 = 0.4
    eps = 2e-5
    y1 = scalar_recursive_time_flow_y(y0, eps, iterations=55)
    finite_difference = (y1-y0)/eps
    generator = scalar_recursive_time_generator_y(y0, iterations=55)
    assert np.isclose(finite_difference, generator, rtol=2e-4, atol=2e-6)


# ---------------------------------------------------------------------------
# Fixed-stratum operator continuum tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    operator_bottcher_coordinate,
    operator_bottcher_depth,
    operator_recursive_time_flow,
    operator_recursive_time_generator,
    operator_scalar_bfg_map,
    is_fixed_spectral_stratum_compatible,
)


def _hermitian_unitary_conjugate(diag, seed=700):
    rng = np.random.default_rng(seed)
    U = _random_unitary(rng, len(diag))
    D = np.diag(diag).astype(complex)
    return U @ D @ U.conj().T, U


def test_operator_bottcher_functional_equation_on_nontrivial_unitary_basis():
    Y, _ = _hermitian_unitary_conjugate([0.15, 0.4, 0.8], seed=701)
    lhs = operator_bottcher_depth(operator_scalar_bfg_map(Y), iterations=55)
    rhs = 2.0 * operator_bottcher_depth(Y, iterations=55)
    assert np.allclose(lhs, rhs, rtol=3e-10, atol=3e-10)


def test_operator_bottcher_coordinate_squares_by_functional_calculus():
    Y, _ = _hermitian_unitary_conjugate([0.1, 0.45, 0.9], seed=702)
    Phi = operator_bottcher_coordinate(Y, iterations=55)
    Phi_next = operator_bottcher_coordinate(
        operator_scalar_bfg_map(Y), iterations=55
    )
    assert np.allclose(Phi_next, Phi @ Phi, rtol=4e-10, atol=4e-10)


def test_operator_recursive_time_recovers_discrete_modewise_step():
    Y, _ = _hermitian_unitary_conjugate([0.12, 0.5, 0.95], seed=703)
    flowed = operator_recursive_time_flow(Y, np.log(2.0), iterations=55)
    discrete = operator_scalar_bfg_map(Y)
    assert np.allclose(flowed, discrete, rtol=5e-9, atol=5e-10)


def test_operator_recursive_time_semigroup_property():
    Y, _ = _hermitian_unitary_conjugate([0.2, 0.55, 0.85], seed=704)
    a, b = 0.13, 0.31
    direct = operator_recursive_time_flow(Y, a+b, iterations=55)
    staged = operator_recursive_time_flow(
        operator_recursive_time_flow(Y, a, iterations=55),
        b,
        iterations=55,
    )
    assert np.allclose(direct, staged, rtol=8e-9, atol=8e-10)


def test_operator_flow_is_unitarily_covariant():
    Y = np.diag([0.17, 0.52, 0.88]).astype(complex)
    rng = np.random.default_rng(705)
    U = _random_unitary(rng, 3)
    tau = 0.27
    lhs = operator_recursive_time_flow(U@Y@U.conj().T, tau, iterations=55)
    rhs = U @ operator_recursive_time_flow(Y, tau, iterations=55) @ U.conj().T
    assert np.allclose(lhs, rhs, rtol=5e-9, atol=5e-10)


def test_operator_generator_matches_short_flow():
    Y, _ = _hermitian_unitary_conjugate([0.2, 0.5, 0.8], seed=706)
    eps = 2e-5
    Y1 = operator_recursive_time_flow(Y, eps, iterations=55)
    fd = (Y1-Y)/eps
    gen = operator_recursive_time_generator(Y, iterations=55)
    assert np.allclose(fd, gen, rtol=4e-4, atol=4e-6)


def test_fixed_stratum_compatibility_accepts_commuting_tuple():
    Y = np.diag([0.2, 0.4, 0.8]).astype(complex)
    A = np.diag([1.0, 2.0, 3.0]).astype(complex)
    B = np.diag([0.1, -0.2, 0.7]).astype(complex)
    assert is_fixed_spectral_stratum_compatible(Y, A, B)


def test_fixed_stratum_compatibility_rejects_noncommuting_tuple():
    Y = np.diag([0.2, 0.4]).astype(complex)
    A = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    assert not is_fixed_spectral_stratum_compatible(Y, A)


# ---------------------------------------------------------------------------
# Coupled commuting stratum + frozen noncommuting continuum
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    commuting_reciprocal_step,
    commuting_quadratic_tangent,
    two_cluster_projective_profile,
    frozen_reclosure_correlation,
    frozen_formation_reclosure,
    frozen_formation_flow,
    frozen_formation_generator,
    schur_fractional_multiplier_eigenvalues,
)


def test_commuting_multimode_update_is_globally_coupled_not_modewise_scalar():
    y = np.array([0.2, 0.6], dtype=float)
    r = np.array([1.0, 1.0], dtype=float)
    yp, alpha, beta, lc, lb = commuting_reciprocal_step(y, r)

    independent = np.array([scalar_intrinsic_gram_map(v) for v in y])
    assert not np.allclose(yp, independent)
    assert np.isclose(alpha + beta, 1.0)
    assert lc > 0.0 and lb > 0.0


def test_commuting_selected_stratum_is_forward_invariant():
    rng = np.random.default_rng(801)
    for _ in range(200):
        n = int(rng.integers(2, 7))
        y = rng.uniform(1e-4, 0.999, size=n)
        r = rng.uniform(0.01, 2.0, size=n)
        yp, *_ = commuting_reciprocal_step(y, r)
        assert np.all(yp > 0.0)
        assert np.all(yp < 1.0)


def test_isotropic_commuting_ray_reduces_exactly_to_scalar_map():
    for y0 in (0.05, 0.2, 0.7, 0.95):
        y = np.full(5, y0)
        r = np.array([0.3, 1.1, 0.7, 2.0, 0.2])
        yp, *_ = commuting_reciprocal_step(y, r)
        expected = scalar_intrinsic_gram_map(y0)
        assert np.allclose(yp, expected, rtol=1e-12, atol=1e-12)


def test_commuting_quadratic_tangent_matches_small_scale_limit():
    x = np.array([0.7, 1.2, 1.8])
    r = np.array([0.5, 2.0, 1.0])
    q = commuting_quadratic_tangent(x, r)

    for s in (1e-3, 3e-4, 1e-4):
        yp, *_ = commuting_reciprocal_step(s*x, r)
        approx = yp/(s*s)
        assert np.allclose(approx, q, rtol=5e-3, atol=5e-3)


def test_two_cluster_projective_profile_formula_solves_quadratic_fixed_profile():
    p = 2.0/3.0
    a, b = two_cluster_projective_profile(p)
    assert np.isclose(a, 0.75)
    assert np.isclose(b, 1.5)

    # weighted profile: two thirds on a, one third on b
    mean2 = p*a*a + (1-p)*b*b
    lam_a = (a*a + mean2)/a
    lam_b = (b*b + mean2)/b
    assert np.isclose(lam_a, lam_b)


def test_frozen_reclosure_flow_recovers_one_discrete_step():
    y = np.array([0.2, 0.7, 2.0])
    chi = frozen_reclosure_correlation(y, 0.4)
    k = np.array(
        [[1.0, 0.3+0.2j, -0.4j],
         [0.3-0.2j, -0.5, 0.1],
         [0.4j, 0.1, 0.8]],
        dtype=complex,
    )
    direct = frozen_formation_reclosure(k, chi)
    flow = frozen_formation_flow(k, chi, np.log(2.0))
    assert np.allclose(flow, direct, atol=1e-12)


def test_frozen_reclosure_flow_has_semigroup_property():
    y = np.array([0.15, 0.9, 3.0])
    chi = frozen_reclosure_correlation(y, 0.35)
    k = np.array(
        [[0.2, 0.5j, 0.1],
         [-0.5j, -0.4, 0.3],
         [0.1, 0.3, 0.9]],
        dtype=complex,
    )
    a, b = 0.17, 0.31
    direct = frozen_formation_flow(k, chi, a+b)
    staged = frozen_formation_flow(
        frozen_formation_flow(k, chi, a), chi, b
    )
    assert np.allclose(direct, staged, atol=1e-12)


def test_frozen_reclosure_generator_matches_short_flow():
    y = np.array([0.2, 1.1, 4.0])
    chi = frozen_reclosure_correlation(y, 0.45)
    k = np.array(
        [[1.0, 0.4, 0.2j],
         [0.4, 0.3, -0.1],
         [-0.2j, -0.1, -0.5]],
        dtype=complex,
    )
    eps = 1e-6
    fd = (frozen_formation_flow(k, chi, eps) - k)/eps
    gen = frozen_formation_generator(k, chi)
    assert np.allclose(fd, gen, rtol=2e-5, atol=2e-6)


def test_frozen_noncommuting_frobenius_norm_is_nonincreasing():
    y = np.array([0.2, 0.8, 3.0])
    chi = frozen_reclosure_correlation(y, 0.5)
    k = np.array(
        [[0.1, 0.6, 0.2],
         [0.6, -0.3, 0.5],
         [0.2, 0.5, 0.4]],
        dtype=complex,
    )
    norms = []
    for tau in np.linspace(0.0, 2.0, 15):
        kt = frozen_formation_flow(k, chi, tau)
        norms.append(np.linalg.norm(kt, "fro"))
    assert all(b <= a + 1e-12 for a, b in zip(norms, norms[1:]))


def test_fractional_schur_interpolation_need_not_be_positive():
    # alpha=beta=1/2, y=(0.1,1,10), half a discrete step:
    # Chi^(1/2) has a negative eigenvalue.
    y = np.array([0.1, 1.0, 10.0])
    chi = frozen_reclosure_correlation(y, 0.5)
    eig = schur_fractional_multiplier_eigenvalues(
        chi, 0.5*np.log(2.0)
    )
    assert eig.min() < -1e-3


def test_fractional_schur_counterexample_determinant_is_negative():
    a = 11.0/np.sqrt(202.0)
    b = 20.0/101.0
    det = 1.0 - 2.0*a - b + 2.0*a*np.sqrt(b)
    assert det < 0.0


# ---------------------------------------------------------------------------
# Frozen Schur CP-embeddability tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    schur_embeddability_certificate,
    frozen_cp_schur_flow_multiplier,
)


def test_all_two_mode_frozen_bfg_schur_channels_are_cp_embeddable():
    rng=np.random.default_rng(901)
    for _ in range(100):
        y=rng.uniform(0.01,10.0,size=2)
        alpha=float(rng.uniform(0.01,0.99))
        chi=frozen_reclosure_correlation(y,alpha)
        cert=schur_embeddability_certificate(chi)
        assert cert.embeddable
        for tau in (0.0,0.1,0.5*np.log(2.0),np.log(2.0),2.0):
            mult=frozen_cp_schur_flow_multiplier(chi,tau)
            assert np.linalg.eigvalsh((mult+mult.T)/2).min()>=-1e-9


def test_three_mode_counterexample_fails_schoenberg_embeddability():
    y=np.array([0.1,1.0,10.0])
    chi=frozen_reclosure_correlation(y,0.5)
    cert=schur_embeddability_certificate(chi)
    assert not cert.embeddable
    assert cert.min_centered_gram_eigenvalue < -1e-6


def test_schoenberg_failure_matches_fractional_negative_multiplier():
    y=np.array([0.1,1.0,10.0])
    chi=frozen_reclosure_correlation(y,0.5)
    eig=schur_fractional_multiplier_eigenvalues(chi,0.5*np.log(2.0))
    assert eig.min() < 0.0
    with pytest.raises(Exception):
        frozen_cp_schur_flow_multiplier(chi,0.5*np.log(2.0))


# ---------------------------------------------------------------------------
# Canonical two-channel CP suspension tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    bfg_channel_angles,
    frozen_angle_multiplier,
    frozen_angle_suspension_multiplier,
    frozen_angle_capacity_flow,
    frozen_full_state_cp_path,
    frozen_angle_local_rate_matrix,
)


def test_channel_angle_representation_reproduces_bfg_chi():
    y = np.array([0.1, 0.7, 2.0, 5.0])
    alpha = 0.37
    theta = bfg_channel_angles(y, alpha)
    chi_angle = np.cos(theta[:, None] - theta[None, :])
    chi = frozen_reclosure_correlation(y, alpha)
    assert np.allclose(chi_angle, chi, atol=1e-12)


def test_angle_interpolation_is_correlation_matrix_for_all_sampled_fractions():
    y = np.array([0.1, 1.0, 10.0])
    alpha = 0.5
    for s in np.linspace(0.0, 1.0, 41):
        m = frozen_angle_multiplier(y, alpha, s)
        eig = np.linalg.eigvalsh((m + m.T)/2.0)
        assert eig.min() >= -1e-12
        assert np.allclose(np.diag(m), 1.0, atol=1e-12)


def test_angle_interpolation_hits_identity_and_exact_discrete_channel():
    y = np.array([0.2, 0.8, 3.0])
    alpha = 0.41
    m0 = frozen_angle_multiplier(y, alpha, 0.0)
    m1 = frozen_angle_multiplier(y, alpha, 1.0)
    assert np.allclose(m0, np.ones((3,3)), atol=1e-12)
    assert np.allclose(m1, frozen_reclosure_correlation(y, alpha), atol=1e-12)


def test_cp_suspension_is_continuous_across_discrete_step_boundary():
    y = np.array([0.1, 1.0, 10.0])
    alpha = 0.5
    edge = np.log(2.0)
    left = frozen_angle_suspension_multiplier(y, alpha, edge - 1e-8)
    exact = frozen_angle_suspension_multiplier(y, alpha, edge)
    right = frozen_angle_suspension_multiplier(y, alpha, edge + 1e-8)
    assert np.linalg.norm(left - exact) < 1e-7
    assert np.linalg.norm(right - exact) < 1e-7


def test_cp_suspension_hits_exact_repeated_frozen_iterates():
    y = np.array([0.2, 0.9, 2.5])
    alpha = 0.43
    chi = frozen_reclosure_correlation(y, alpha)
    for n in range(5):
        m = frozen_angle_suspension_multiplier(y, alpha, n*np.log(2.0))
        assert np.allclose(m, chi**n, atol=1e-12)


def test_nonembeddable_three_mode_case_still_has_positive_half_step_angle_path():
    y = np.array([0.1, 1.0, 10.0])
    alpha = 0.5
    angle_half = frozen_angle_multiplier(y, alpha, 0.5)
    eig_angle = np.linalg.eigvalsh(angle_half)
    assert eig_angle.min() >= -1e-12

    # Contrast with the non-positive entrywise square-root semigroup candidate.
    chi = frozen_reclosure_correlation(y, alpha)
    eig_power = np.linalg.eigvalsh(np.sqrt(chi))
    assert eig_power.min() < -1e-3


def test_angle_path_is_generally_not_a_semigroup():
    y = np.array([0.1, 1.0, 10.0])
    alpha = 0.5
    s = 0.2
    t = 0.3
    direct = frozen_angle_multiplier(y, alpha, s+t)
    composed = frozen_angle_multiplier(y, alpha, s) * frozen_angle_multiplier(y, alpha, t)
    assert not np.allclose(direct, composed)


def test_frozen_capacity_flow_preserves_positive_semidefinite_capacity():
    rng = np.random.default_rng(1001)
    y = np.diag([0.1, 0.7, 2.0]).astype(complex)
    z = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3))
    a = z.conj().T @ z
    for tau in np.linspace(0.0, 2.0*np.log(2.0), 17):
        at = frozen_angle_capacity_flow(a, y, 0.4, tau)
        assert np.linalg.eigvalsh(at).min() >= -1e-9


def test_frozen_full_state_cp_path_preserves_positive_densities_and_fixed_geometry():
    s = _rank_increase_state()
    # Freeze on the current carrier; use same-support path only.
    for tau in (0.0, 0.2, 0.5*np.log(2.0), np.log(2.0), 1.5*np.log(2.0)):
        out = frozen_full_state_cp_path(s, 0.4, tau)
        assert np.allclose(out.Y, s.Y)
        assert np.allclose(out.R_C, s.R_C)
        assert np.allclose(out.formation_density, s.formation_density)
        assert np.allclose(out.witness, s.witness)
        assert np.linalg.eigvalsh(out.formation_density).min() >= -1e-9
        assert np.linalg.eigvalsh(out.witness).min() >= -1e-9
        assert np.isclose(np.trace(out.witness).real, 1.0)


def test_frozen_full_state_formation_is_linear_combination_of_flowed_capacities():
    s = _rank_increase_state()
    tau = 0.37
    out = frozen_full_state_cp_path(s, 0.4, tau)
    k0 = s.coherence + s.emergence - s.D_cap
    kt_expected = frozen_angle_capacity_flow(k0, s.Y, 0.4, tau)
    kt_actual = out.coherence + out.emergence - out.D_cap
    assert np.allclose(kt_actual, kt_expected, atol=1e-10)


def test_local_rate_matrix_matches_short_angle_path_derivative():
    y = np.array([0.2, 0.8, 2.0])
    alpha = 0.4
    s = 0.37
    eps = 1e-6
    m = frozen_angle_multiplier(y, alpha, s)
    mp = frozen_angle_multiplier(y, alpha, s+eps)
    fd = (mp-m)/eps
    gamma = frozen_angle_local_rate_matrix(y, alpha, s)
    assert np.allclose(fd, gamma*m, rtol=2e-5, atol=2e-6)


# ---------------------------------------------------------------------------
# Phase-anchored full-state suspension tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    gauge_aligned_full_persistent_endpoint,
    phase_anchored_full_persistent_suspension,
    phase_anchored_load_nonuniqueness,
    RecursivePhaseAnchorState,
    recursive_phase_anchor_readout,
    advance_recursive_phase_anchor,
    recursive_phase_anchor_flow,
)


def _full_persistent_selected_state(seed=1101, n=3):
    rng=np.random.default_rng(seed)
    U=_random_unitary(rng,n)
    yvals=np.linspace(0.18,0.82,n)
    Y=U@np.diag(yvals)@U.conj().T

    def psd(offset=0.2):
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        return z.conj().T@z/n + offset*np.eye(n)

    rho_f=psd(0.3)
    rho_w=psd(0.1)
    rho_w=rho_w/np.trace(rho_w).real

    return UniversalOperatorState(
        D_cap=psd(0.4),
        coherence=psd(0.3),
        emergence=psd(0.2),
        formation_density=rho_f,
        witness=rho_w,
        Y=Y,
        R_C=np.eye(n,dtype=complex),
        P_per=np.eye(n,dtype=complex),
    )


def test_gauge_aligned_full_persistent_endpoint_matches_generic_update_invariants():
    s=_full_persistent_selected_state()
    closed=gauge_aligned_full_persistent_endpoint(s)
    generic=bfg_universal_state_update(s)
    assert not generic.terminal, generic.reason
    assert generic.state.dim==s.dim

    for name in ("D_cap","coherence","emergence","formation_density","witness","Y","R_C"):
        a=getattr(closed.state,name)
        b=getattr(generic.state,name)
        eva=np.linalg.eigvalsh((a+a.conj().T)/2)
        evb=np.linalg.eigvalsh((b+b.conj().T)/2)
        assert np.allclose(eva,evb,rtol=2e-8,atol=2e-8)


def test_phase_anchored_suspension_hits_exact_source_and_target():
    s=_full_persistent_selected_state(seed=1102)
    p0=phase_anchored_full_persistent_suspension(s,0.0)
    p1=phase_anchored_full_persistent_suspension(s,1.0)

    for name in ("D_cap","coherence","emergence","formation_density","witness","Y","R_C"):
        assert np.allclose(getattr(p0.readout,name),getattr(s,name),atol=1e-10)
        assert np.allclose(getattr(p1.readout,name),getattr(p1.target,name),atol=1e-10)


def test_phase_anchored_suspension_stays_selected_positive_and_normalized():
    s=_full_persistent_selected_state(seed=1103)
    for ph in np.linspace(0.0,1.0,21):
        out=phase_anchored_full_persistent_suspension(s,float(ph)).readout
        y=np.linalg.eigvalsh(out.Y)
        assert y.min()>0.0
        assert y.max()<1.0
        assert np.linalg.eigvalsh(out.formation_density).min()>=-1e-9
        assert np.linalg.eigvalsh(out.witness).min()>=-1e-9
        assert np.isclose(np.trace(out.witness).real,1.0,atol=1e-10)
        assert np.allclose(out.R_C,np.eye(out.dim),atol=1e-10)


def test_continuum_load_path_is_not_unique_under_endpoint_and_positivity_constraints():
    s=_full_persistent_selected_state(seed=1104)
    gap=phase_anchored_load_nonuniqueness(s,phase=0.37)
    assert gap>1e-5


def test_phase_anchored_suspension_is_unitarily_covariant():
    s=_full_persistent_selected_state(seed=1105)
    rng=np.random.default_rng(1106)
    U=_random_unitary(rng,s.dim)

    def conj(a):
        return U@a@U.conj().T

    su=UniversalOperatorState(
        D_cap=conj(s.D_cap),
        coherence=conj(s.coherence),
        emergence=conj(s.emergence),
        formation_density=conj(s.formation_density),
        witness=conj(s.witness),
        Y=conj(s.Y),
        R_C=conj(s.R_C),
        P_per=conj(s.P_per),
    )
    ph=0.43
    a=phase_anchored_full_persistent_suspension(s,ph).readout
    b=phase_anchored_full_persistent_suspension(su,ph).readout
    for name in ("D_cap","coherence","emergence","formation_density","witness","Y","R_C"):
        assert np.allclose(getattr(b,name),conj(getattr(a,name)),rtol=2e-8,atol=2e-8)


def test_extended_anchor_phase_flow_has_semigroup_property():
    s=_full_persistent_selected_state(seed=1107)
    e0=RecursivePhaseAnchorState(anchor=s,phase=0.0)
    a=0.37
    b=0.91
    staged=advance_recursive_phase_anchor(
        advance_recursive_phase_anchor(e0,a),b
    )
    direct=advance_recursive_phase_anchor(e0,a+b)
    assert np.isclose(staged.phase,direct.phase,atol=1e-12)
    for name in ("D_cap","coherence","emergence","formation_density","witness","Y","R_C"):
        assert np.allclose(getattr(staged.anchor,name),getattr(direct.anchor,name),rtol=2e-8,atol=2e-8)


def test_extended_phase_flow_hits_repeated_discrete_endpoints():
    s=_full_persistent_selected_state(seed=1108)
    cur=s
    for n in range(4):
        flow=recursive_phase_anchor_flow(s,n*np.log(2.0))
        for name in ("D_cap","coherence","emergence","formation_density","witness","Y","R_C"):
            assert np.allclose(getattr(flow,name),getattr(cur,name),rtol=2e-8,atol=2e-8)
        cur=gauge_aligned_full_persistent_endpoint(cur).state


def test_projector_rank_change_cannot_be_a_continuous_exact_projector_linear_bridge():
    # Rank-one to rank-two endpoint: the naive continuous matrix bridge immediately
    # leaves the exact projector manifold, illustrating the rank-event obstruction.
    p0=np.diag([1.0,0.0,0.0])
    p1=np.diag([1.0,1.0,0.0])
    pm=0.5*(p0+p1)
    assert not np.allclose(pm@pm,pm)


# ---------------------------------------------------------------------------
# Same-rank R4 support geodesic tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    r4_same_rank_geodesic,
    r4_same_rank_density_transport,
)


def _two_plane_rotated_projectors():
    e=np.eye(4,dtype=complex)
    z0=e[:,:2]
    a,b=0.23,0.51
    z1=np.column_stack([
        np.cos(a)*e[:,0]+np.sin(a)*e[:,2],
        np.cos(b)*e[:,1]+np.sin(b)*e[:,3],
    ])
    p0=z0@z0.conj().T
    p1=z1@z1.conj().T
    return p0,p1,np.array([a,b])


def test_r4_same_rank_geodesic_stays_exact_projector_and_rank():
    p0,p1,angles=_two_plane_rotated_projectors()
    for ph in np.linspace(0.0,1.0,17):
        g=r4_same_rank_geodesic(p0,p1,float(ph))
        assert np.allclose(g.projector@g.projector,g.projector,atol=1e-9)
        assert np.allclose(g.projector,g.projector.conj().T,atol=1e-9)
        assert np.linalg.matrix_rank(g.projector,tol=1e-8)==2
        assert np.allclose(np.sort(g.principal_angles),np.sort(angles),atol=1e-8)


def test_r4_same_rank_geodesic_end_transport_matches_polar_rule():
    p0,p1,_=_two_plane_rotated_projectors()
    g0=r4_same_rank_geodesic(p0,p1,0.0)
    g1=r4_same_rank_geodesic(p0,p1,1.0)
    t_expected=polar_partial_isometry(p1@p0)
    assert np.allclose(g0.projector,p0,atol=1e-9)
    assert np.allclose(g1.projector,p1,atol=1e-9)
    assert np.allclose(g0.transport,p0,atol=1e-9)
    assert np.allclose(g1.transport,t_expected,atol=1e-9)


def test_r4_same_rank_density_transport_preserves_trace_positivity_and_support():
    p0,p1,_=_two_plane_rotated_projectors()
    rho=np.diag([0.7,0.3,0.0,0.0]).astype(complex)
    for ph in np.linspace(0.0,1.0,11):
        g=r4_same_rank_geodesic(p0,p1,float(ph))
        out=r4_same_rank_density_transport(rho,p0,p1,float(ph),normalize=True)
        assert np.linalg.eigvalsh(out).min()>=-1e-9
        assert np.isclose(np.trace(out).real,1.0,atol=1e-10)
        assert np.linalg.norm(out-g.projector@out@g.projector)<1e-8


def test_r4_same_rank_geodesic_rejects_rank_change():
    p0=np.diag([1.0,0.0,0.0]).astype(complex)
    p1=np.diag([1.0,1.0,0.0]).astype(complex)
    with pytest.raises(Exception):
        r4_same_rank_geodesic(p0,p1,0.5)


def test_r4_same_rank_geodesic_rejects_orthogonal_overlap_loss():
    p0=np.diag([1.0,0.0]).astype(complex)
    p1=np.diag([0.0,1.0]).astype(complex)
    with pytest.raises(Exception):
        r4_same_rank_geodesic(p0,p1,0.5)


# ---------------------------------------------------------------------------
# Local anchor-elimination tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    scalar_phase_readout_h,
    scalar_phase_reconstruct_anchor_h,
    scalar_phase_local_vector_field_h,
    scalar_phase_local_vector_field_y,
    scalar_phase_anchor_free_advance,
    suspension_locality_certificate_from_jacobian,
    scalar_phase_readout_derivative_anchor,
    scalar_same_readout_different_phase_example,
)


def test_scalar_phase_anchor_reconstruction_is_exact():
    for a in (0.0, 0.1, 0.7, 2.0, 8.0):
        for w in (0.0, 0.2, 0.5, 0.8, 0.99):
            h = scalar_phase_readout_h(a, w)
            rec = scalar_phase_reconstruct_anchor_h(h, w)
            assert np.isclose(rec, a, rtol=1e-11, atol=1e-11)


def test_scalar_phase_readout_is_strictly_anchor_invertible_inside_open_step():
    for a in (0.0, 0.1, 1.0, 5.0):
        for w in (0.0, 0.3, 0.7, 0.99):
            deriv = scalar_phase_readout_derivative_anchor(a, w)
            assert deriv > 0.0


def test_scalar_anchor_free_local_vector_field_matches_suspension_derivative():
    anchor = 0.8
    phase = 0.37
    h = scalar_phase_readout_h(anchor, phase)
    dh_dtau, domega = scalar_phase_local_vector_field_h(h, phase)

    eps = 2e-6
    h2 = scalar_phase_readout_h(anchor, phase + eps/np.log(2.0))
    fd = (h2-h)/eps

    assert np.isclose(domega, 1.0/np.log(2.0), atol=1e-14)
    assert np.isclose(fd, dh_dtau, rtol=2e-6, atol=2e-8)


def test_scalar_anchor_free_local_vector_field_y_matches_h_transform():
    y = 0.42
    phase = 0.31
    h = -np.log(y)
    dy, dphase = scalar_phase_local_vector_field_y(y, phase)
    dh, dphase_h = scalar_phase_local_vector_field_h(h, phase)
    assert np.isclose(dphase, dphase_h)
    assert np.isclose(dy, -y*dh, rtol=1e-12, atol=1e-12)


def test_scalar_anchor_free_advance_matches_original_anchor_suspension():
    anchor = 1.2
    phase = 0.21
    h = scalar_phase_readout_h(anchor, phase)
    dt = 0.17
    h1, w1 = scalar_phase_anchor_free_advance(h, phase, dt)
    expected_w = phase + dt/np.log(2.0)
    expected_h = scalar_phase_readout_h(anchor, expected_w)
    assert np.isclose(w1, expected_w)
    assert np.isclose(h1, expected_h, rtol=1e-11, atol=1e-11)


def test_phase_is_necessary_same_readout_can_have_different_tangents():
    h = 1.0
    a, b, va, vb = scalar_same_readout_different_phase_example(
        h, 0.2, 0.8
    )
    assert not np.isclose(a, b)
    assert not np.isclose(va, vb)


def test_locality_certificate_accepts_invertible_chart():
    j = np.diag([1.2, 0.7, 0.3])
    c = suspension_locality_certificate_from_jacobian(j, phase=0.4)
    assert c.locally_anchor_free
    assert not c.requires_memory_branch
    assert c.min_singular_value > 0.0


def test_locality_certificate_flags_singular_chart():
    j = np.diag([1.0, 0.0, 0.5])
    c = suspension_locality_certificate_from_jacobian(j, phase=0.6)
    assert not c.locally_anchor_free
    assert c.requires_memory_branch
    assert np.isclose(c.min_singular_value, 0.0)


def test_scalar_open_step_never_requires_memory_branch_by_jacobian_criterion():
    for a in np.linspace(0.0, 6.0, 20):
        for w in np.linspace(0.0, 0.99, 15):
            deriv = scalar_phase_readout_derivative_anchor(float(a), float(w))
            c = suspension_locality_certificate_from_jacobian(
                np.array([[deriv]]),
                phase=float(w),
            )
            assert c.locally_anchor_free


# ---------------------------------------------------------------------------
# Coupled commuting fold / memory-branch tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    commuting_phase_endpoint_h,
    commuting_phase_readout_h,
    commuting_phase_tangent_h,
    commuting_phase_jacobian_fd,
    canonical_two_mode_memory_branch_witness,
)


def test_commuting_two_mode_suspension_has_explicit_same_readout_multiple_anchors():
    w = canonical_two_mode_memory_branch_witness()
    readouts = w["readouts_h"]
    for r in readouts[1:]:
        assert np.allclose(r, readouts[0], rtol=1e-12, atol=2e-12)

    anchors = w["anchors_h"]
    assert np.linalg.norm(anchors[0]-anchors[1]) > 0.1
    assert np.linalg.norm(anchors[1]-anchors[2]) > 0.1


def test_commuting_two_mode_same_readout_branches_have_different_tangents():
    w = canonical_two_mode_memory_branch_witness()
    v = w["tangents_dh_dtau"]
    assert np.linalg.norm(v[0]-v[1]) > 1.0
    assert np.linalg.norm(v[1]-v[2]) > 2.0


def test_commuting_memory_branch_witness_is_inside_selected_stratum():
    w = canonical_two_mode_memory_branch_witness()
    for y in w["anchors_y"]:
        assert np.all(y > 0.0)
        assert np.all(y < 1.0)


def test_commuting_fold_jacobian_has_near_zero_singular_value_at_deterministic_point():
    h = np.array([1.2921364085108027, 0.09571786689741542])
    r = np.array([0.11560491, 0.81916805])
    phase = 0.8283584507952344
    j = commuting_phase_jacobian_fd(h, r, phase, eps=2e-6)
    sv = np.linalg.svd(j, compute_uv=False)
    assert sv.min() < 1e-8


def test_commuting_phase_tangent_matches_phase_derivative():
    h = np.array([0.6, 0.15])
    r = np.array([0.4, 1.2])
    phase = 0.42
    tangent = commuting_phase_tangent_h(h, r)
    eps = 1e-7
    f0 = commuting_phase_readout_h(h, r, phase)
    f1 = commuting_phase_readout_h(h, r, phase + eps)
    d_by_phase = (f1-f0)/eps
    assert np.allclose(
        tangent,
        d_by_phase/np.log(2.0),
        rtol=2e-7,
        atol=2e-8,
    )


# ---------------------------------------------------------------------------
# Simple-fold / local memory-bit tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    canonical_two_mode_simple_fold_certificate,
    local_fold_branch_bit,
    local_fold_branch_coordinate,
    minimum_binary_memory_bits,
)


def test_canonical_two_mode_fold_is_simple_corank_one():
    cert = canonical_two_mode_simple_fold_certificate()
    assert cert.is_simple_fold
    assert cert.singular_values[-1] < 1e-7
    assert cert.singular_values[-2] > 1e-2


def test_canonical_two_mode_fold_has_nonzero_quadratic_curvature():
    cert = canonical_two_mode_simple_fold_certificate()
    assert abs(cert.fold_curvature) > 1e-3


def test_canonical_two_mode_fold_is_transversely_unfolded_by_phase():
    cert = canonical_two_mode_simple_fold_certificate()
    assert abs(cert.phase_transversality) > 0.1
    assert abs(cert.determinant_phase_derivative) > 0.1


def test_local_simple_fold_has_binary_sheet_coordinate():
    cert = canonical_two_mode_simple_fold_certificate()
    fold_anchor = np.array(
        [1.2921364085108027, 0.09571786689741542]
    )
    v = cert.right_null
    a_plus = fold_anchor + 1e-3*v
    a_minus = fold_anchor - 1e-3*v
    assert local_fold_branch_bit(a_plus, fold_anchor, v) == 1
    assert local_fold_branch_bit(a_minus, fold_anchor, v) == -1
    assert local_fold_branch_bit(fold_anchor, fold_anchor, v) == 0


def test_global_three_branch_example_needs_at_least_two_binary_bits_if_fixed_encoded():
    w = canonical_two_mode_memory_branch_witness()
    assert len(w["anchors_h"]) == 3
    assert minimum_binary_memory_bits(3) == 2


def test_local_fold_projected_normal_displacement_is_quadratic_to_leading_order():
    cert = canonical_two_mode_simple_fold_certificate()
    r = np.array([0.11560491, 0.81916805])
    af = np.array([1.2921364085108027, 0.09571786689741542])
    w = 0.8283584507952344
    v = cert.right_null
    ell = cert.left_null
    f0 = commuting_phase_readout_h(af, r, w)

    eps = 2e-3
    fp = commuting_phase_readout_h(af + eps*v, r, w)
    fm = commuting_phase_readout_h(af - eps*v, r, w)

    qp = float(ell @ (fp-f0))
    qm = float(ell @ (fm-f0))
    # Same leading sign and nearly equal size = local z^2 fold normal form.
    assert qp * qm > 0.0
    assert np.isclose(qp, qm, rtol=5e-2, atol=1e-8)


# ---------------------------------------------------------------------------
# Global memory-graph / exponential branch-growth tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    fixed_alpha_phase_readout_h,
    canonical_three_root_scalar_witness,
    dominant_mode_anchor_for_alpha,
    exponential_branch_lower_bound,
    exponential_branch_memory_bit_lower_bound,
    decoupled_dominant_mode_target,
    memory_graph_capacity_lower_bound,
    memory_graph_capacity_sequence,
)


def test_canonical_fixed_alpha_scalar_witness_has_three_distinct_roots():
    w = canonical_three_root_scalar_witness()
    vals = [
        fixed_alpha_phase_readout_h(h, w["alpha"], w["phase"])
        for h in w["roots"]
    ]
    assert len(w["roots"]) == 3
    assert np.all(np.diff(w["roots"]) > 0.0)
    assert np.allclose(vals, w["target"], rtol=1e-11, atol=1e-11)


def test_canonical_three_roots_are_nondegenerate():
    w = canonical_three_root_scalar_witness()
    eps = 1e-6
    derivs = []
    for h in w["roots"]:
        fp = fixed_alpha_phase_readout_h(
            h + eps, w["alpha"], w["phase"]
        )
        fm = fixed_alpha_phase_readout_h(
            h - eps, w["alpha"], w["phase"]
        )
        derivs.append((fp-fm)/(2.0*eps))
    assert min(abs(x) for x in derivs) > 1e-2


def test_dominant_mode_anchor_realizes_requested_reciprocal_alpha():
    alpha = 0.3
    h = dominant_mode_anchor_for_alpha(alpha)
    y = np.exp(-h)
    realized = y*y/(1.0+y*y)
    assert np.isclose(realized, alpha, rtol=1e-13, atol=1e-13)


def _solve_small_positive_coupled_branch_family(dim, epsilon=1e-6):
    from scipy.optimize import least_squares
    import itertools

    weights0, target, phase, roots = decoupled_dominant_mode_target(dim)
    weights = np.array(weights0, dtype=float)
    weights[1:] = epsilon

    alpha = canonical_three_root_scalar_witness()["alpha"]
    h1 = dominant_mode_anchor_for_alpha(alpha)
    solutions = []

    for combo in itertools.product(roots, repeat=dim-1):
        x0 = np.r_[h1, np.array(combo, dtype=float)]
        sol = least_squares(
            lambda h: commuting_phase_readout_h(h, weights, phase) - target,
            x0,
            bounds=(np.full(dim, 1e-8), np.full(dim, 20.0)),
            xtol=1e-12,
            ftol=1e-12,
            gtol=1e-12,
            max_nfev=3000,
        )
        residual = np.linalg.norm(
            commuting_phase_readout_h(sol.x, weights, phase) - target
        )
        assert residual < 1e-8
        if all(np.linalg.norm(sol.x-s) > 1e-5 for s in solutions):
            solutions.append(sol.x)

    return weights, target, phase, solutions


@pytest.mark.parametrize("dim,expected", [(2,3), (3,9), (4,27), (5,81)])
def test_small_positive_coupling_preserves_exponential_branch_family(dim, expected):
    weights, target, phase, solutions = _solve_small_positive_coupled_branch_family(dim)
    assert np.all(weights > 0.0)
    assert len(solutions) == expected
    assert expected == exponential_branch_lower_bound(dim)


def test_memory_bit_lower_bound_grows_linearly_with_dimension():
    seq = memory_graph_capacity_sequence(8)
    branches = [x.guaranteed_branch_lower_bound for x in seq]
    bits = [x.minimum_binary_bits for x in seq]
    assert branches == [1, 3, 9, 27, 81, 243, 729, 2187]
    assert bits == [0, 2, 4, 5, 7, 8, 10, 12]


def test_no_dimension_independent_fixed_memory_state_count_from_branch_lower_bound():
    # For any proposed finite branch-label count N, choose n large enough that
    # 3^(n-1) > N.
    for proposed_states in (2, 4, 16, 256, 10000):
        n = 1
        while exponential_branch_lower_bound(n) <= proposed_states:
            n += 1
        assert exponential_branch_lower_bound(n) > proposed_states


# ---------------------------------------------------------------------------
# Carrier-dimension monotonicity / repeated-rank-growth orbit tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    repeated_rank_growth_fixture,
    carrier_dimension_nonincrease_bound,
    orbit_rank_dimension_trace,
    is_full_persistent_selected_state,
    full_persistence_lock_step,
)


def test_cross_fed_successor_carrier_dimension_cannot_exceed_source_dimension():
    rng = np.random.default_rng(1201)
    checked = 0
    for _ in range(200):
        n = int(rng.integers(3, 7))
        p = int(rng.integers(1, n+1))
        U = _random_unitary(rng, n)
        P = U[:, :p] @ U[:, :p].conj().T

        V = _random_unitary(rng, n)
        Y = V @ np.diag(rng.uniform(0.05, 0.85, size=n)) @ V.conj().T

        z = rng.normal(size=(p,p)) + 1j*rng.normal(size=(p,p))
        rf_local = z.conj().T@z + 0.1*np.eye(p)
        Z = U[:, :p]
        rho_f = Z @ rf_local @ Z.conj().T

        w = rng.normal(size=(p,p)) + 1j*rng.normal(size=(p,p))
        rw_local = w.conj().T@w + 0.1*np.eye(p)
        rw_local /= np.trace(rw_local).real
        rho_w = Z @ rw_local @ Z.conj().T

        D = np.diag(np.linspace(1.4, 2.6, n)).astype(complex)
        C = 0.5*np.eye(n)
        A = 0.5*np.eye(n)
        R = P + 0.4*(np.eye(n)-P)

        s = UniversalOperatorState(
            D_cap=D,
            coherence=C,
            emergence=A,
            formation_density=rho_f,
            witness=rho_w,
            Y=Y,
            R_C=R,
            P_per=P,
        )
        out = bfg_universal_state_update(s, tol=1e-12, boundary_tol=1e-10)
        if out.terminal:
            continue
        checked += 1
        assert out.state.dim <= s.dim

    assert checked >= 50


def test_repeated_rank_growth_fixture_realizes_two_successive_rank_increases():
    s0 = repeated_rank_growth_fixture()
    o1 = bfg_universal_state_update(s0, tol=1e-12, boundary_tol=1e-10)
    assert not o1.terminal, o1.reason
    assert o1.state.dim == 4
    assert o1.diagnostics["persistent_rank_before"] == 2
    assert o1.diagnostics["persistent_rank_after_reclosure"] == 3

    o2 = bfg_universal_state_update(o1.state, tol=1e-12, boundary_tol=1e-10)
    assert not o2.terminal, o2.reason
    assert o2.state.dim == 4
    assert o2.diagnostics["persistent_rank_before"] == 3
    assert o2.diagnostics["persistent_rank_after_reclosure"] == 4


def test_repeated_rank_growth_fixture_reaches_full_persistence_lock():
    s0 = repeated_rank_growth_fixture()
    s1 = bfg_universal_state_update(
        s0, tol=1e-12, boundary_tol=1e-10
    ).state
    s2 = bfg_universal_state_update(
        s1, tol=1e-12, boundary_tol=1e-10
    ).state

    assert is_full_persistent_selected_state(s2)

    s3 = full_persistence_lock_step(s2).state
    assert s3.dim == 4
    assert np.linalg.matrix_rank(s3.P_per, tol=1e-9) == 4
    assert is_full_persistent_selected_state(s3)


def test_orbit_trace_never_increases_carrier_dimension():
    s0 = repeated_rank_growth_fixture()
    trace = orbit_rank_dimension_trace(
        s0, 6, tol=1e-14, boundary_tol=1e-12
    )
    dims = [r.carrier_dimension for r in trace]
    assert all(b <= a for a, b in zip(dims, dims[1:]))
    assert dims[:3] == [4, 4, 4]


def test_full_persistence_selected_class_keeps_all_load_eigenvalues_below_one():
    s0 = repeated_rank_growth_fixture()
    s1 = bfg_universal_state_update(s0).state
    s2 = bfg_universal_state_update(s1).state
    assert is_full_persistent_selected_state(s2)

    cur = s2
    # Two further steps remain well resolved in double precision. Exact
    # mathematics continues beyond this; later floating stops are numerical
    # load-resolution ambiguity, not loss of the invariant class.
    for _ in range(2):
        out = full_persistence_lock_step(cur, tol=1e-14)
        vals = np.linalg.eigvalsh(out.state.Y)
        assert np.all(vals > 0.0)
        assert np.all(vals < 1.0)
        assert np.linalg.matrix_rank(out.state.P_per, tol=1e-9) == out.state.dim
        cur = out.state


# ---------------------------------------------------------------------------
# Reciprocal-alpha inverse-fiber reduction tests
# ---------------------------------------------------------------------------

from bfg_lab.fundamental_closure import (
    fixed_alpha_readout_y_value,
    fixed_alpha_critical_polynomial_coefficients,
    fixed_alpha_max_positive_inverse_roots,
    selected_reciprocal_alpha_from_loads,
    alpha_conditioned_sheet_upper_bound,
    alpha_fiber_memory_bound,
)


def test_fixed_alpha_derivative_polynomial_matches_numeric_derivative_sign():
    alpha = 0.3
    phase = 0.94
    coeff = fixed_alpha_critical_polynomial_coefficients(alpha, phase)

    for y in (0.05, 0.2, 0.5, 0.85):
        eps = 1e-7
        fp = fixed_alpha_readout_y_value(y+eps, alpha, phase)
        fm = fixed_alpha_readout_y_value(y-eps, alpha, phase)
        dnum = (fp-fm)/(2.0*eps)
        poly = sum(coeff[k]*(y**k) for k in range(4))
        assert np.sign(dnum) == np.sign(poly)


def test_phase_at_or_below_one_third_has_monotone_fixed_alpha_inverse_map():
    for phase in (0.05, 0.2, 1.0/3.0):
        assert fixed_alpha_max_positive_inverse_roots(phase) == 1
        coeff = fixed_alpha_critical_polynomial_coefficients(0.3, phase)
        assert np.all(coeff >= -1e-14)


def test_high_phase_allows_at_most_three_fixed_alpha_inverse_roots():
    for phase in (0.4, 0.7, 0.94, 0.99):
        assert fixed_alpha_max_positive_inverse_roots(phase) == 3


def test_canonical_three_root_witness_saturates_fixed_alpha_bound():
    w = canonical_three_root_scalar_witness()
    assert fixed_alpha_max_positive_inverse_roots(w["phase"]) == 3
    vals = [
        fixed_alpha_readout_y_value(
            np.exp(-h), w["alpha"], w["phase"]
        )
        for h in w["roots"]
    ]
    assert np.allclose(vals, vals[0], rtol=1e-11, atol=1e-11)


def test_selected_reciprocal_alpha_is_below_half():
    y = np.array([0.1, 0.4, 0.9])
    r = np.array([0.2, 1.0, 0.7])
    alpha = selected_reciprocal_alpha_from_loads(y, r)
    assert 0.0 < alpha < 0.5


def test_alpha_conditioned_sheet_bound_is_three_to_dimension_at_high_phase():
    assert alpha_conditioned_sheet_upper_bound(1, 0.94) == 3
    assert alpha_conditioned_sheet_upper_bound(4, 0.94) == 81
    assert alpha_conditioned_sheet_upper_bound(5, 0.2) == 1


def test_positive_dimensional_fiber_memory_uses_at_most_one_continuous_alpha_coordinate():
    b = alpha_fiber_memory_bound(4, 0.94)
    assert b.continuous_memory_dimension_upper_bound == 1
    assert b.discrete_sheets_per_alpha_upper_bound == 81


# ---------------------------------------------------------------------------
# Package consistency / governance regression tests
# ---------------------------------------------------------------------------

def test_package_manifest_references_only_existing_files():
    from pathlib import Path
    import re

    repo = Path(__file__).resolve().parents[1]
    text = (repo / "INTEGRATION.md").read_text(encoding="utf-8")
    listed = re.findall(
        r"^(research/[^\s`]+|bfg_lab/[^\s`]+|tests/[^\s`]+)$",
        text,
        re.M,
    )
    assert listed
    assert all((repo / p).exists() for p in listed)


def test_claim_register_has_unique_ids():
    from pathlib import Path
    import re
    from collections import Counter

    repo = Path(__file__).resolve().parents[1]
    text = (
        repo / "research" / "bfg-fundamental-closure" / "CLAIMS.md"
    ).read_text(encoding="utf-8")
    ids = re.findall(r"\|\s*(F\d{3})\s*\|", text)
    assert ids
    assert all(c == 1 for c in Counter(ids).values())


def test_stress_jsons_use_current_boundary_schema_and_parse():
    from pathlib import Path
    import json

    repo = Path(__file__).resolve().parents[1]
    research = repo / "research" / "bfg-fundamental-closure"
    for name in ("CSR_STRESS_RESULTS.json", "NEUTRAL_CONTRAST_STRESS_RESULTS.json"):
        data = json.loads((research / name).read_text(encoding="utf-8"))
        assert "terminal_or_boundary_counts" in data
        assert "runtime_stop_semantics_counts" in data
        assert "status_note" in data

    neutral = json.loads(
        (research / "NEUTRAL_CONTRAST_STRESS_RESULTS.json").read_text(encoding="utf-8")
    )
    assert "dual_load_failure" not in neutral["terminal_or_boundary_counts"]


def test_authoritative_docs_use_two_density_master_state_and_completion_status():
    from pathlib import Path

    repo = Path(__file__).resolve().parents[1]
    research = repo / "research" / "bfg-fundamental-closure"
    master = (research / "MASTER_STATE.md").read_text(encoding="utf-8")
    law = (research / "FUNDAMENTAL_CLOSURE_LAW.md").read_text(encoding="utf-8")
    contract = (research / "BFG_ONLY_CONTRACT.md").read_text(encoding="utf-8")

    assert r"\rho_F" in master and r"\rho_W" in master
    assert "DECLARED FINITE COMPLETION" in law
    assert "Intrinsic-Gram successor load" in contract
    assert "Neutral-Contrast Selection" in contract
    assert "Neutral transverse recursion" in contract


def test_legacy_vector_analysis_uses_current_dual_load_boundary_labels():
    y = np.zeros((1, 1), dtype=complex)
    d = np.array([1.0], dtype=complex)
    p = np.eye(1, dtype=complex)
    with pytest.raises(Exception) as exc:
        analysis_operator(y, d, p, tol=1e-12)
    assert "dual_load_zero_terminal" in str(exc.value)


def test_stress_semantics_counts_equal_ambiguity_reason_counts():
    from pathlib import Path
    import json

    repo = Path(__file__).resolve().parents[1]
    research = repo / "research" / "bfg-fundamental-closure"
    for name in ("CSR_STRESS_RESULTS.json", "NEUTRAL_CONTRAST_STRESS_RESULTS.json"):
        data = json.loads((research / name).read_text(encoding="utf-8"))
        ambiguity = sum(
            v for k, v in data["terminal_or_boundary_counts"].items()
            if "ambiguity" in k
        )
        assert data["runtime_stop_semantics_counts"]["numerical_unresolved"] == ambiguity


def test_authoritative_selection_interval_includes_zero_load_spectral_mode_before_load_gate():
    from pathlib import Path

    repo = Path(__file__).resolve().parents[1]
    law = (
        repo / "research" / "bfg-fundamental-closure" / "FUNDAMENTAL_CLOSURE_LAW.md"
    ).read_text(encoding="utf-8")
    assert r"\mathbf1_{[0,1)}(Y)" in law
    assert r"\mathbf1_{(0,1)}(Y)" not in law
