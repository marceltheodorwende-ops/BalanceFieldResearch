"""Bounded boundary witnesses; failed candidates never exclude a family."""
from itertools import islice, product
from .certified import assess_family, _number
from .certified_search import refine_family


def assess_boundary(weight_lower, weight_upper, initial, samples, times, sensors,
                    initial_error=0, sensor_error=0, terms=24,
                    max_boxes=255, max_depth=20, max_candidates=81,
                    candidate_terms=64):
    if type(max_candidates) != int or max_candidates < 0:
        raise ValueError('Nonnegative integer candidate budget required')
    if type(candidate_terms) != int or not 0 <= candidate_terms <= 128:
        raise ValueError('Integer candidate series budget 0..128 required')
    previous = refine_family(weight_lower, weight_upper, initial, samples, times,
                             sensors, initial_error, sensor_error, terms,
                             max_boxes, max_depth)
    previous['candidate_checks'] = 0
    if previous['status'] != 'unresolved' or max_candidates == 0:
        return previous
    lo = [[_number(v) for v in row] for row in weight_lower]
    hi = [[_number(v) for v in row] for row in weight_upper]
    x = [_number(v) for v in initial]
    ex, ey = _number(initial_error), _number(sensor_error)
    xl, xu = [v-ex for v in x], [v+ex for v in x]
    for j, i in enumerate(sensors):
        observed = _number(samples[0][j])
        xl[i] = max(xl[i], observed-ey)
        xu[i] = min(xu[i], observed+ey)
    if any(l > u for l, u in zip(xl, xu)):
        return previous
    edges = [(i,j) for i in range(len(x)) for j in range(i+1,len(x))]
    intervals = [(lo[i][j],hi[i][j]) for i,j in edges] + list(zip(xl,xu))
    choices = [tuple(dict.fromkeys((l,(l+u)/2,u))) for l,u in intervals]
    for values in islice(product(*choices), max_candidates):
        a = [[_number(0) for _ in x] for _ in x]
        for (i,j),w in zip(edges,values):
            a[i][j] = a[j][i] = w
        state = list(values[len(edges):])
        r = assess_family(a,a,state,samples,times,sensors,0,sensor_error,candidate_terms)
        previous['candidate_checks'] += 1
        if r['status'] == 'compatible_witness':
            return dict(status='compatible_witness',witness=r['witness'],history=r['history'],
                        witness_source='boundary_candidates',
                        visited_boxes=previous['visited_boxes'],
                        candidate_checks=previous['candidate_checks'],candidate_terms=candidate_terms)
    return previous


if __name__ == '__main__':
    import argparse, json
    from pathlib import Path
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('results/certified_boundary.json'))
    args=p.parse_args()
    r=assess_boundary(**json.loads(args.input.read_text(encoding='utf-8'),parse_float=str))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(r['status'])
