"""Reproduce three equation-based 3D figures for the BFG synthesis preprint.

These are deterministic mathematical surfaces, not natural-system measurements.
"""
from pathlib import Path
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm, colors
import numpy as np


HERE = Path(__file__).resolve().parent
FIGURES = HERE / 'figures'
FIGURES.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9,
                     'axes.labelsize': 9, 'figure.facecolor': 'white'})


def save_surface(filename, x, y, z, xlabel, ylabel, zlabel, title,
                 cmap, elev, azim, floor, overlay=None):
    fig = plt.figure(figsize=(7.15, 4.65), dpi=240)
    ax = fig.add_subplot(111, projection='3d')
    norm = colors.Normalize(vmin=float(np.min(z)), vmax=float(np.max(z)))
    ax.plot_surface(x, y, z, cmap=cmap, norm=norm, linewidth=0,
                    antialiased=True, rcount=150, ccount=150,
                    alpha=.94, rasterized=True)
    ax.contour(x, y, z, zdir='z', offset=floor, levels=12,
               cmap=cmap, linewidths=.58)
    if overlay is not None:
        overlay(ax)
    ax.set(xlabel=xlabel, ylabel=ylabel, zlabel=zlabel,
           zlim=(floor, float(np.max(z))), title=title)
    ax.view_init(elev=elev, azim=azim)
    ax.set_box_aspect((1, 1, .65))
    ax.xaxis.pane.set_facecolor((.96, .97, .98, 1))
    ax.yaxis.pane.set_facecolor((.96, .97, .98, 1))
    ax.zaxis.pane.set_facecolor((.96, .97, .98, 1))
    cb = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax,
                      shrink=.63, pad=.10, aspect=20)
    cb.ax.tick_params(labelsize=7)
    fig.subplots_adjust(left=.00, right=.90, top=.92, bottom=.03)
    out = FIGURES / filename
    fig.savefig(out, dpi=240, facecolor='white')
    plt.close(fig)
    return out


axis = np.linspace(-1.7, 1.7, 171)
x, y = np.meshgrid(axis, axis)
formation = -.5*x*x + y*y + .25*(x*x+y*y)**2
assert np.isclose(-.5+.25, -.25)
f2 = save_surface('figure2_level0_formation_3d.png', x, y, formation,
                  'formed coordinate x', 'transverse coordinate y',
                  r'$F_0(x,y)$', 'Level-0 quartic formation; K₀ = diag(−1, 2)',
                  'viridis', 26, -59, -.35,
                  overlay=lambda a: a.scatter([-1, 1], [0, 0], [-.25, -.25],
                                              color='#C0392B', s=28, depthshade=False))

dgrid = np.linspace(-1, 1, 171)
egrid = np.linspace(-1.1, 1.1, 171)
D, eta = np.meshgrid(dgrid, egrid)
J = (D-eta)**2+eta**2
assert np.allclose(.5*dgrid**2, (dgrid-dgrid/2)**2+(dgrid/2)**2)
f3 = save_surface('figure3_neutral_tangent_3d.png', D, eta, J,
                  'source displacement D', 'neutral coordinate η',
                  r'$J_{tan}(D,\eta)$', 'Quadratic neutral completion; H* = M = 2, L = 1',
                  'cividis', 27, -64, -.14,
                  overlay=lambda a: a.plot(dgrid, dgrid/2, dgrid**2/2,
                                           color='#C0392B', lw=2.5))

load_axis = np.linspace(0, 3, 171)
y1, y2 = np.meshgrid(load_axis, load_axis)
defect = (y1-y2)**2/((1+y1*y1)*(1+y2*y2))
assert np.max(np.abs(np.diag(defect))) < 1e-14
f4 = save_surface('figure4_neutral_novelty_3d.png', y1, y2, defect,
                  'neutral eigenvalue y₁', 'neutral eigenvalue y₂',
                  r'$1-\chi_{12}^2$', 'Schur novelty defect; α = β = 1',
                  'magma', 25, -55, -.055,
                  overlay=lambda a: a.plot(load_axis, load_axis,
                                           np.zeros_like(load_axis),
                                           color='#18A999', lw=2.3))

result = {
    'status': 'deterministic equation evaluation; not an empirical simulation',
    'grid_points_per_axis': 171,
    'figure2': {'path': f2.relative_to(HERE).as_posix(),
                'K0_eigenvalues': [-1, 2], 'global_minima': [[-1, 0], [1, 0]],
                'minimum_energy': -.25},
    'figure3': {'path': f3.relative_to(HERE).as_posix(),
                'H_star': 2, 'M': 2, 'L': 1,
                'analytical_valley': 'eta=D/2; min J=D²/2'},
    'figure4': {'path': f4.relative_to(HERE).as_posix(),
                'alpha': 1, 'beta': 1,
                'diagonal_defect_max_abs': float(np.max(np.abs(np.diag(defect))))},
}
(HERE / 'MATHEMATICAL_FIGURES_RESULTS.json').write_text(
    json.dumps(result, indent=2, allow_nan=False)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
