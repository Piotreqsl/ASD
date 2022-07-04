

from queue import PriorityQueue



G = [
    [-1,6,-1,5,2],
    [-1,-1,1,2,-1],
    [-1,-1,-1,-1,-1],
    [-1,-1,4,-1,-1],
    [-1,-1,8,-1,-1]
]
P = [0,1,3]




def binSearch(A,x):
    n = len(A)
    l = 0
    r = n-1
    while(l<=r):
        q = (l+r) //2
        if(A[q] ==x):
            return q
        elif(A[q] < x):
            l = q+1
        else:
            r = q-1
    return -1

def path(parent, u):
    if parent[u] is None:
        return [u]
    return path(parent, parent[u]) + [u]


## dijkstra która w kolejce priorytetowej trzyma jeszcze aktualną ilośc paliwa
## jeżeli trafię na stacje benzynową w trakcie podróży to 
## sobie tankuje jeszcze


def dijkstra(G,s,t,bak,P):
    
    def relax(d,u,v,weight,parents):
        if(d[v] > d[u] + weight):
            d[v] = d[u] + weight
            parents[v] = u
    


    
    n = len(G)
    d = [float("inf")] * n
    parents = [None]*n
    enqueued = [True] * n

    d[s] = 0
    q = PriorityQueue()
    q.put((d[s], s, 0))
    while not q.empty():
        _,u,cb = q.get()
        if not enqueued[u]:
            continue
        if(binSearch(P,u) != -1):
            cb = bak
        enqueued[u] = False
        for v in range(n):
            if G[u][v] != -1 and enqueued[v]:
                if(cb >= G[u][v]):
                    relax(d,u,v,G[u][v],parents)
                    q.put((d[v],v,cb-G[u][v]))

    if(d[t] == float("inf")):
        return None
    return path(parents, t)
    print(d[t])




    



def jak_dojade(G,P,d,a,b):
    return dijkstra(G,a,b,d,P)

print(jak_dojade(G,P,8,0,2))