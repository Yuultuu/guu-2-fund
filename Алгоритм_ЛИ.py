from collections import deque

def lee(g, start, end):
    q = deque([start])
    dist = {start: 0}
    parent = {start: None}

    while q:
        v = q.popleft()
        if v == end:
            break
        for n in g.get(v, []):
            if n not in dist:
                dist[n] = dist[v] + 1
                parent[n] = v
                q.append(n)

    if end not in parent:
        return None

    path = []
    v = end
    while v:
        path.append(v)
        v = parent[v]

        return path[::-1], dist[end]


g = {
'A': ['B', 'C'],
'B': ['C', 'D'],
'C': ['D'],
'D': []
}

print(lee(g, 'A', 'D'))