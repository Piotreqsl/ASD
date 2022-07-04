M = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]] 
x = 0 
y = 3 
d = 2 
from collections import deque

def path(parent, u, n):
    if parent[u] is None:
        return [(u // n, u % n)]
    return path(parent, parent[u], n) + [(u // n, u % n)]


def bfs(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    Q = deque()
    visited[s] = True
    Q.append(s)

    while len(Q) > 0:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.append(v)

    return parent




def floyd_warshall(G):
    n = len(G)
    S = [[float("inf") if G[i][j] == 0 else G[i][j] for j in range(n)] for i in range(n)]

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]
    return S


def carolMarx(M,x,y,d):
    n = len(M)
    dist = floyd_warshall(M)
    big_g = [[0 for i in range(n*n)] for j in range(n*n)]

    for u in range(n):
        for v in range(n): 
            if u == v:
                continue
            if(dist[u][v] <d ):
                continue
            for i in range(n):
                for j in range(n):
                    if(i == v and u == j): ## jeżeli to jest po prostu zmiana wspolrzednych
                        continue
                    if(dist[i][j] < d):
                        continue
                    ## teraz rozważamy możliwe przypadki zmiany tego stanu rzeczy
                    if(u ==i and M[v][j] != 0): ## przemieszcza się druga pozycja
                        big_g[(u*n) + v][(i*n) + j] = 1
                    elif(v == j and M[u][i] != 0):
                        big_g[(u*n) + v][ (i*n) + j] =1
                    elif(M[u][i] !=0 and M[i][j] !=0):
                        big_g[(u*n) + v][ (i*n) + j] =1
        parent = bfs(big_g, (x*n) + y)
        route = path(parent,(y*n) +x,n)
        return route
        

            







