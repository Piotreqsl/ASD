from kol3btesty import runtests

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


  
    return d[t]


## dokładam jeden wierzchołek - przestrzeń powietrzna




def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    G.append([])
    air = len(G) -1
    for i in range(len(A)):
        G[air].append((i,A[i]))
        G[i].append((air, A[i]))
    
    return dijkstra(G,s,t)
    
    


    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )