## kolejności zadań

T = [ 
    [0,2,1,1], 
    [1,0,1,1], 
    [2,2,0,1], 
    [2,2,2,0] ]

def topologic_sort(G):
    n = len(G)

    def dfs(G, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs(G, v)
        res.append(u)

    visited = [False] * n
    res = []
    for u in range(n):
        if not visited[u]:
            dfs(G, u)

    res.reverse()
    return res

def topologic(G):
    n = len(G)

    def dfs(G,u):
        visited[u] = True
        
        for v in G[u]:
            if v != 0 and visited[v] == False:
                dfs(G,v)
        res.append(u)
    
    visited = [False] *n
    res = []
    for u in range(n):
        if not visited[u]:
            dfs(G,u)
    #res.reverse()
    return res



def tasks(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if(T[i][j] == 2):
                T[i][j] =0
    return topologic(T)
## teraz sortuje topologicznie

print(tasks(T))