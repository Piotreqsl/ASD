

from queue import PriorityQueue




def Dijsktra(G,s,t):
    def relax( u, v, weight):
    
        if(distances[v] > distances[u] + weight):
            distances[v] = distances[u] + weight
            parent[v] = u
    def path(u):
        if parent[u] is None:
            return [u]
        return path(parent[u]) + [u]
    


    n = len(G)
    distances = [float("inf")] *n
    distances[s] = 0
    enqueued = [True] * n
    parent = [None] * n

    PQ = PriorityQueue()
    PQ.put((distances[s], s))


    while (not PQ.empty()):
        w, u = PQ.get()
        if not enqueued[u]:
            continue
        enqueued[u] = False

        for v in G[u]:
            if(enqueued[v[0]]):
                relax(u,v[0],v[1])
                PQ.put((distances[v[0]], v[0]))
  
    return distances


def paths(G,s,t):
    n = len(G)
    dist_from_s = Dijsktra(G,s,t)
    dist_from_t = Dijsktra(G,t,s)
    counter = 0
    SHORTEST_PATH = dist_from_s[t]
    for i in range(n):
        for j in range(len(G[i])):
            if(dist_from_s[i] + dist_from_t[G[i][j][0]] + G[i][j][1] == SHORTEST_PATH):
                counter+=1
    return counter

    pass




G = [   [(1,2), (2,4)],
        [(0,2), (3,11), (4,3)],
        [(0,4), (3,13)],
        [(1,11), (2,13), (5,17), (6,1)],
        [(1,3), (5,5)],
        [(3,17), (4,5), (7,7)],
        [(3,1), (7,3)],
        [(5,7), (6,3)]]



print(paths(G,0,7))