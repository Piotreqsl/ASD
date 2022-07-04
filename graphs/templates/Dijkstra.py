from queue import PriorityQueue


def relax(d, parent, u, v, weight):
    if d[v] > d[u] + weight:
        d[v] = d[u] + weight
        parent[v] = u


def path(parent, u):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u]) + [u]


def dijkstra(G, s, t):
    n = len(G)
    d = [float("inf")] * n
    parent = [None] * n
    enqueued = [True] * n
    Q = PriorityQueue()



    d[s] = 0
    cnt = 0
    Q.put((d[s], s))
    while not Q.empty() and cnt < n:
        _, u= Q.get()
        if not enqueued[u]:
            continue
        enqueued[u] = False
        cnt += 1
        for v in G[u]:
            if enqueued[v[0]]:
                relax(d, parent, u, v[0])
                Q.put((d[v[0]], v[0]))


    route = path(parent, t)
    return route, d[t]


G = [[(1, 9)],
     [(0, 9), (2, 10), (6, 8)],
     [(1, 10), (3, 4)],
     [(2, 4), (4, 5)],
     [(3, 5), (5, 6)],
     [(4, 6), (6, 7)],
     [(2, 8), (5, 7)]]
print(dijkstra(G, 0, 2))