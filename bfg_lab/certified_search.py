"""Bounded exact-rational subdivision of the certified reference family."""
from collections import deque
from .certified import assess_family, _number


def refine_family(weight_lower, weight_upper, initial, samples, times, sensors,
                  initial_error=0, sensor_error=0, terms=24,
                  max_boxes=256, max_depth=20):
    if type(max_boxes) != int or max_boxes < 1 or type(max_depth) != int or max_depth < 0:
        raise ValueError('Positive integer box budget and nonnegative integer depth required')
    # Validate all measurement and model inputs before constructing the search.
    root_result = assess_family(weight_lower, weight_upper, initial, samples, times,
                                sensors, initial_error, sensor_error, terms)
    lo = [[_number(v) for v in row] for row in weight_lower]
    hi = [[_number(v) for v in row] for row in weight_upper]
    x = [_number(v) for v in initial]; ex = _number(initial_error)
    root = (lo, hi, [v-ex for v in x], [v+ex for v in x], 0, '')
    queue = deque([root]); excluded = []; unresolved = []; visited = 0
    while queue and visited < max_boxes:
        a, b, xl, xu, depth, path = queue.popleft()
        center = [(l+u)/2 for l, u in zip(xl, xu)]
        radius = max((u-l)/2 for l, u in zip(xl, xu))
        result = root_result if visited == 0 else assess_family(
            a, b, center, samples, times, sensors, radius, sensor_error, terms)
        visited += 1
        if result['status'] == 'compatible_witness':
            return dict(status='compatible_witness', witness=result['witness'],
                        history=result['history'], visited_boxes=visited, witness_path=path)
        if result['status'] == 'healthy_family_excluded':
            excluded.append(dict(path=path, certificate=result['certificate']))
            continue
        coordinates = [(b[i][j]-a[i][j], 'weight', i, j)
                       for i in range(len(x)) for j in range(i+1, len(x))]
        coordinates += [(xu[i]-xl[i], 'initial', i, i) for i in range(len(x))]
        width, kind, i, j = max(coordinates, key=lambda c: c[0])
        if depth >= max_depth or width == 0 or result.get('reason') == 'series_budget_insufficient':
            unresolved.append(dict(path=path, reason=result.get('reason'), depth=depth))
            continue
        for side in (0, 1):
            ca = [row.copy() for row in a]; cb = [row.copy() for row in b]
            cl = xl.copy(); cu = xu.copy()
            if kind == 'weight':
                mid = (a[i][j]+b[i][j])/2
                target = cb if side == 0 else ca
                target[i][j] = target[j][i] = mid
            else:
                mid = (xl[i]+xu[i])/2
                (cu if side == 0 else cl)[i] = mid
            queue.append((ca, cb, cl, cu, depth+1, path+str(side)))
    pending = [box[-1] for box in queue]
    return dict(status='unresolved' if pending or unresolved else 'healthy_family_excluded',
                reason='search_incomplete' if pending or unresolved else 'all_leaves_excluded',
                visited_boxes=visited, excluded_leaves=excluded,
                unresolved_leaves=unresolved, pending_paths=pending)


if __name__ == '__main__':
    import argparse, json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('results/certified_search.json'))
    args = parser.parse_args()
    result = refine_family(**json.loads(args.input.read_text(encoding='utf-8'), parse_float=str))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(result['status'])
