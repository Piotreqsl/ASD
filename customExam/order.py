


def makeGraph(L,K):
    m = 10 ** K
    graph = [[] for i in range(m)]
    n = len(L)
    for i in range(n):
        graph[L[i] // m].append(i)

    return graph

def topologySort(G,L,K,s):

    m = 10 ** K

    def DFSVisit(G,L,u):
        visited[u] = True
        for each in G[L[u] %m]:
            if not visited[each]:
                DFSVisit(G,L,each)
        res.append(u)
    
    visited = [False] * len(G)
    res = []
    DFSVisit(G,L,s)
    res.reverse()
    return res

def order(L,K):
    G = makeGraph(L,K)

    _min = float("inf")
    idx =None
    for i in range( len(L) ):
        if L[i] < _min:
            _min = L[i]
            idx = i
    
    topology = topologySort(G,L,K,idx)
    res = []
    for each in topology:
        res.append(L[each])
    
    if len(res) != len(L):
        return None
    return res