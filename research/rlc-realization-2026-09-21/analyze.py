"""Exploratory RLC reconstruction; Python 3 + NumPy, no BFG fitting."""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent


def impedance(f, parameters):
    r, l, c = parameters
    w = 2 * np.pi * np.asarray(f)
    return (r + 1j*w*l) / (1 + 1j*w*c*(r + 1j*w*l))


def residual(theta, f, z):
    difference = (impedance(f, np.exp(theta)) - z) / np.abs(z)
    return np.r_[difference.real, difference.imag]


def fit(f, z, initial):
    theta = np.log(initial)
    damping = 1e-3
    for iteration in range(200):
        e = residual(theta, f, z)
        step = 1e-5
        jac = np.column_stack([
            (residual(theta + np.eye(3)[j]*step, f, z)
             - residual(theta - np.eye(3)[j]*step, f, z))/(2*step)
            for j in range(3)
        ])
        grad = jac.T @ e
        if np.linalg.norm(grad, ord=np.inf) < 1e-9:
            return np.exp(theta), iteration, float(np.linalg.norm(grad, ord=np.inf))
        delta = np.linalg.solve(jac.T@jac + damping*np.eye(3), -grad)
        candidate = theta + delta
        if np.max(np.abs(candidate)) > 100:
            damping *= 10
            continue
        new_e = residual(candidate, f, z)
        if new_e @ new_e < e @ e:
            theta = candidate
            damping = max(damping/3, 1e-12)
        else:
            damping *= 10
    raise RuntimeError('Optimizer did not reach gradient tolerance')


def metrics(f, z, parameters):
    error = impedance(f, parameters)-z
    return {
        'complex_rmse_ohm': float(np.sqrt(np.mean(np.abs(error)**2))),
        'relative_complex_rms': float(np.sqrt(np.mean(np.abs(error/z)**2))),
        'maximum_relative_complex_error': float(np.max(np.abs(error/z))),
    }


def main():
    raw = (ROOT/'rlc_circuit.json').read_bytes()
    assert hashlib.md5(raw).hexdigest() == '0d8f9939685d435c7475aed873a6ba99'
    data = json.loads(raw)
    f = np.asarray(data['f'], dtype=float)
    z = np.asarray(data['z_real']) + 1j*np.asarray(data['z_imag'])
    assert len(f) == len(z) and len(f) > 3
    assert np.isfinite(f).all() and np.isfinite(z).all() and (f > 0).all()
    assert len(np.unique(f)) == len(f) and (np.abs(z) > 0).all()
    assert np.allclose(data['omega'], 2*np.pi*f, rtol=1e-12)
    assert np.allclose(data['z_modulus'], np.abs(z), rtol=1e-12)
    assert np.allclose(data['z_phase'], np.angle(z), atol=1e-12)
    # Independent parallel-admittance expression from Kirchhoff's current law.
    nominal = np.array([0.0097, 0.005, 2.2e-6])
    w = 2*np.pi*f
    independent = 1/(1/(nominal[0]+1j*w*nominal[1])+1j*w*nominal[2])
    assert np.allclose(impedance(f, nominal), independent, rtol=1e-12)
    assert impedance(np.array([0.]), nominal)[0] == nominal[0]
    order = np.argsort(f)
    f, z = f[order], z[order]
    train = np.arange(len(f)) % 2 == 0
    runs = [fit(f[train], z[train], initial) for initial in
            [nominal, [9.7, .005, 2.2e-6], [1., .002, 1e-6]]]
    parameters = runs[0][0]
    assert all(np.allclose(parameters, r[0], rtol=1e-5) for r in runs)
    # Synthetic recovery checks parameter inference, not empirical validation.
    recovered, _, _ = fit(f, impedance(f, [7., .004, 3e-6]), [1., .005, 2e-6])
    assert np.allclose(recovered, [7., .004, 3e-6], rtol=1e-6)
    r, l, c = parameters
    state_matrix = np.array([[0., -1/c], [1/l, -r/l]])
    poles = np.linalg.eigvals(state_matrix)
    assert np.all(poles.real < 0)
    result = {
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'numpy_version': np.__version__,
        'points': len(f), 'frequency_range_hz': [float(f.min()), float(f.max())],
        'minimum_real_impedance_ohm': float(z.real.min()),
        'low_frequency_point': {'f_hz': float(f[0]), 'real_ohm': float(z[0].real), 'imag_ohm': float(z[0].imag)},
        'nominal_parameters': dict(zip(['R_ohm','L_henry','C_farad'], nominal.tolist())),
        'nominal_all_points': metrics(f,z,nominal),
        'nominal_interpolation_check': metrics(f[~train],z[~train],nominal),
        'continuous_poles_per_second': [[float(v.real),float(v.imag)] for v in poles],
        'fitted_parameters': dict(zip(['R_ohm','L_henry','C_farad'], parameters.tolist())),
        'fit_objective': 'equal per-frequency relative complex squared residual; not a likelihood',
        'split': 'ascending frequencies: even zero-based indices train, odd interpolation check; exploratory, not blind',
        'train_points': int(train.sum()), 'check_points': int((~train).sum()),
        'fitted_train': metrics(f[train],z[train],parameters),
        'fitted_interpolation_check': metrics(f[~train],z[~train],parameters),
        'optimizer_runs': [{'parameters':r[0].tolist(),'iterations':r[1],'gradient_inf':r[2]} for r in runs],
        'synthetic_recovery_parameters': recovered.tolist(),
        'limitations': ['one spectrum', 'no independently established per-point uncertainty',
                       'no observed BFG reclosure transitions', 'no BFG load-law selection'],
    }
    (ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
