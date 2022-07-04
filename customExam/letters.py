
from queue import PriorityQueue
from turtle import pos


L1 = ["k","k","o","o","t","t"]
E1 = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
W = "kto"

def conv(E, n):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append( (edge[1], edge[2]) ) 
        G[edge[1]].append( (edge[0], edge[2]) ) 
    return G




def letters(G,W):
    L,E = G
    n = len(L)

    Q = PriorityQueue()
    d = [[float('inf') for i in range(len(W))] for _ in range(n)]
    processed = [[False for i in range(len(W))] for _ in range(n)]

    G = conv(E,n)

    def relax(u,v,position, weight):
        nonlocal Q
        if d[v][position] > d[u][position -1] + weight:
            d[v][position] = d[u][position - 1] + weight
            Q.put( (d[v][position], (v, position)))
    
    
    for i in range(n):
        if L[i] == W[0]:
            d[i][0] = 0
            Q.put( (d[i][0], (i,0)))

    while not Q.empty():
        _, tuple = Q.get()
        idx, position = tuple
        if not processed[idx][position]:
            for v, weight in G[idx]:
                if(position + 1 < len(W)):
                    if not processed[v][position +1] and W[position +1] == L[v]:
                        relax(idx,v,position+1, weight)
            processed[idx][position] = True
    
    res = []
    for i in range(n):
        if L[i] == W[len(W) - 1]: ## do ostatniej litery mogliśmy dotrzeć tylko dobrymi literami
            res.append(d[i][len(W) - 1])
    return min(res)