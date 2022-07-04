from kol3atesty import runtests

from queue import PriorityQueue


def relax(d, u, v, weight):
    if d[v] > d[u] + weight:
        d[v] = d[u] + weight


def dijkstra(G, s, t):
    n = len(G)
    d = [float("inf")] * n
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
                relax(d, u, v[0], v[1])
                Q.put((d[v[0]], v[0]))


    if(d[t] == float("inf")):
        return None
    return d[t]




def spacetravel( n, E, S, a, b ):
    z = len(S)
    for i in range(z):
        for j in range(i+1, z):
            E.append((S[i], S[j], 0))
    
    G = [[] for i in range(n)]

    z = len(E)
    for i in range(z):
        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][0], E[i][2]))


    return dijkstra(G,a,b)


    # tu prosze wpisac wlasna implementacje
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )