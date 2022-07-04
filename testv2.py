def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def dijkstry( G, s, e ):
    def relax(u, v, weight):
        if D[v] > D[u] + weight:
            D[v] = D[u] + weight
            Parent[v] = u

    n = len(G)
    processed = [False] * n
    D = [float('inf')] * n
    Parent = [-1] * n
    D[s] = 0
    for i in range(n):
        u = getMinVertex(processed, D)
        if u == None:
            break
        processed[u] = True
        for v, weight in G[u]:
            if not processed[v]:
                relax(u,v,weight)
    
    return D[e]