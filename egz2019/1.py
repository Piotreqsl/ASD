## wyspy

from queue import PriorityQueue


def relax(d,u,v,weight):
    if(d[v] > d[u] + weight):
        d[v] = d[u]+weight




## pierwsza wersja ze zmodowaną dijkstrą (zapisuję jak dotarłem do danego wierzchołka i wybieram inną opcje transportu)
def dijkstra1(G,s,t):
    n = len(G)
    d = [float("inf")] *n
    enqueued = [[True, True, True]] * n

    d[s]= 0
    q = PriorityQueue()
    q.put((0,s,-1)) ## trzeci parametr to ostatni środek transportu -1 - mogę wybrać dowolny 0 - dojechałem mostem, 1- dojechałem wodą, 2 - dojechałem powietrzem
    while not q.empty():
        _,u,type = q.get()
        if not enqueued[u][type]:
            continue
        enqueued[u][type] = False
        for v in range(n):
            if(G[u][v] > 0):
                if(G[u][v] == 1 and type != 0):
                    relax(d,u,v,1)
                    q.put((d[v],v,0))
                if(G[u][v] == 5 and type != 1):
                    relax(d,u,v,5)
                    q.put((d[v],v,1))
                if(G[u][v] == 8 and type != 2):
                    relax(d,u,v,8)
                    q.put((d[v],v,2))
    return d[t]


def islands(G,A,B):
    return dijkstra1(G,A,B)



#########################################################################################################################
## druga wersja z roztrojeniem wierzchołków
def min_d(d, enqueued, n):
    best = float("inf")
    vert = None
    for u in range(n):
        if d[u] < best and enqueued[u]:
            best = d[u]
            vert = u
    return vert


def dijkstra(G, s, t, n_):
    n = len(G) ## w tym wypadku to jest 3*n_
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


def islands2(G,A,B):
    n = len(G)
    big_G = [[0 for i in range(3*n)] for i in range(3*n)]

    for i in range(n):
        for j in range(n):
                if(G[i][j] == 1):
                    big_G[n+i][j] = 1
                    big_G[2*n+i][j] = 1
                if(G[i][j] == 5):
                    big_G[i][n+j] = 5
                    big_G[2*n+i][n+j] = 5
                if(G[i][j] == 8):
                    big_G[i][2*n+j] = 8
                    big_G[n+i][2*n+j] = 8

    res = min(dijkstra(big_G, A, B, n), dijkstra(big_G, n + A, B, n), dijkstra(big_G, 2 * n + A, B, n))
    if res == float("inf"):
        return None
    return res









G1 = [ [0,5,1,8,0,0,0 ], [5,0,0,1,0,8,0 ], [1,0,0,8,0,0,8 ], [8,1,8,0,5,0,1 ], [0,0,0,5,0,1,0 ], [0,8,0,0,1,0,5 ], [0,0,8,1,0,5,0 ] ]

print(islands(G1,5,2))
print(islands2(G1, 5, 2))