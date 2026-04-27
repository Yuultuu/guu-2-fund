def f(g, s, e, v=None):
    if v is None: v = []
    v = v + [s]
    if s == e: return v, 0

    best = None
    for n, w in g.get(s, []):
        if n not in v:
            r = f(g, n, e, v)
            if r:
                p, d = r
                d += w
                if not best or d < best[1]:
                    best = (p, d)
    return best


g = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(f(g, 'A', 'D'))