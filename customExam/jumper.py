

from queue import PriorityQueue


G=[[0, 1, 200, 200, 200, 200],
              [1, 0, 2, 200, 200, 200],
              [200, 2, 0, 40, 200, 200],
              [200, 200, 40, 0, 40, 200],
              [200, 200, 200, 40, 0, 117],
              [200, 200, 200, 200, 117, 0]]
s = 1
to =5




def relax(d, parent, u, v, weight):
    if d[v] > d[u] + weight:
        d[v] = d[u] + weight
        parent[v] = u


def path(parent, u,n):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u], n) + [u %n]


def dijkstra(G, s, t, n_):
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
        for i in range(n):
            if enqueued[i] and G[u][i] > 0:
                relax(d, parent, u, i, G[u][i])
                Q.put((d[i], i))

    if(d[t] < d[t+n_]):
        route = path(parent, t, n_)
        return route, d[t]
    else:
        route = path(parent, t + n_, n_)
        return route, d[t+n_]
    




## tworze sobie podwójny graf
## wierzchołki +n to te do których dotarłem dwumilowymi butami

def jumper(G,s,w):
    n= len(G)
    big_G = [[0 for i in range(2*n)] for j in range(2*n)]

    for i in range(n):
        for j in range(n):
            big_G[i][j] = G[i][j]
    
    for u in range(n):
        for v in range(n):
            if(G[u][v] > 0):
                for z in range(n):
                    if(z != u and z!=v and G[v][z] > 0):
                        big_G[u][n+z] = max(G[u][v], G[v][z])
    
    ## teraz te dwumilowe łącze ze zwykłymi
    for i in range(n):
        for j in range(n):
            if(G[i][j] > 0):
                big_G[i+n][j] = G[i][j] 

    return dijkstra(big_G,s,w,n)


print(jumper(G,s,to))

