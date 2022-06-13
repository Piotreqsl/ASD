# 2 pkt
from collections import deque

'''
0)  Obliczamy odległości między wierzchołkami alg. Floyda-Warshalla
1)  Wyznaczamy wszystkie możliwe stany układu, czyli pary (p, q) wierzchołków takich że Carol i Max się ie szachują
2)  Tworzymy nowy graf T, taki, że dla każdego stanu układu mamy wierzchołek, a jeśli da się przejść
    ze stanu (p, q) do (r, s) w jednym ruchu, to jest tam krawędź.
3)  Przeszukujemy graf T DFS-em puszczanym tylko raz w wierzchołku (x, y), jeśli dojdziemy do (y, x) to
    znaleźliśmy ścieżkę, jeśli nie, to ścieżka nie istnieje.

'''


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
    S = [[G[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:
                S[i][j] = float("inf")

    for t in range(n):
        for u in range(n):
            for w in range(n):
                if S[u][w] > S[u][t] + S[t][w]:
                    S[u][w] = S[u][t] + S[t][w]

    return S

def printTwoDim(M):
    n = len(M)
    for i in range(n):
        print(M[i])
def convertToList(M):
    adj_list =[]
    for i in range(len(M)):
        temp = []
        for j in range(len(M)):
            if(M[i][j]):
                temp.append(j)
        adj_list.append(temp)
    print(adj_list)


def keep_distance(M, x, y, d):
    n = len(M)
    S = floyd_warshall(M)

    G = [[0] * (n * n) for _ in range(n * n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if S[u][v] < d:
                continue
            for i in range(n):
                for j in range(n):
                    if i == v and j == u:
                        continue
                    if S[i][j] < d:
                        continue
                    if u == i and M[v][j] != 0: ## jeśli u-i stoję, ale przechodzę z v do j
                        G[(u * n) + v][(u * n) + j] = 1
                    elif v == j and M[u][i] != 0: ## jeśli z v do j stoję, ale przechodzę z u do i
                        G[(u * n) + v][(i * n) + v] = 1
                    elif M[u][i] != 0 and M[v][j] != 0: ## jeśli obiema mogę się ruszyć
                        G[(u * n) + v][(i * n) + j] = 1
    

    parent = bfs(G, (x * n) + y)
    print(parent)
    route = path(parent, (y * n) + x, n)

    return route

M = [[0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]]

print(keep_distance(M,0,3,2))


