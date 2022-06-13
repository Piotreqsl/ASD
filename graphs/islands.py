
def min_d(d, enqueued, n):
    best = float("inf")
    vert = None
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t, n_):
    n = len(G)
    d = [(float("inf"))] * n
    enqueued = [True] * n

    d[s] = 0
    for i in range(n):
        u = min_d(d, enqueued, n)
        if u is None:
            continue
        enqueued[u] = False

        for v in range(n):
            if 0 < G[u][v] and d[u] + G[u][v] < d[v] and enqueued[v]:
                d[v] = G[u][v] + d[u]

    ## zwracam minumum z możliwych opcji dotarcia tam
    ## most, statek, samolot
    return min(d[t], d[n_ + t], d[2 * n_ + t])


def islands(G, A, B):
    n = len(G)
    big_G = [[0] * (3 * n) for _ in range(3 * n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                ## jeśli most to wtedy do i mogę albo przypłynąć albo przylecieć
                big_G[n + i][j] = 1
                big_G[2 * n + i][j] = 1
            elif G[i][j] == 5:
                ## jeśli do j przypływam to do i musiałem albo przyjść albo przylecieć
                big_G[i][n + j] = 5
                big_G[2 * n + i][n + j] = 5
            elif G[i][j] == 8:
                ### jeśli do j przylatuję to do i musiałem albo przyjść albo przypłynąć
                big_G[i][2 * n + j] = 8
                big_G[n + i][2 * n + j] = 8
    ## albo startuje mostem, albo statkiem, albo samolotem
    res = min(dijkstra(big_G, A, B, n), dijkstra(big_G, n + A, B, n), dijkstra(big_G, 2 * n + A, B, n))
    if res == float("inf"):
        return None
    return res



