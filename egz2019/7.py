L = [ 
    [ 2 ], 
    [ 2 ], 
    [ 0, 1, 3], 
    [ 2, 4 ], 
    [ 3, 5, 6 ], 
    [ 4 ], 
    [ 4 ] ]


## rozwiązaniem jest wierzhołek leżący na środku średnicy drzewa!
## pozostaje ją tylko znaleźć i zwrócić
## a średnicę znajduję poprzez odpalenie dwóch bfsów


from queue import Queue

def bfs(L,s):
    n = len(L)
    visited = [False] * n
    d = [-1] * n
    parent = [None] * n
    Q = Queue()
    d[s] = 0
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in L[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.put(v)
    return d, parent
            




def best_root(L):
    ## w pierwszej kolejności szukam średnicy drzewa
    ## wybieram se dowolny wierzchołek i lecę dfsem jak najdalej się da
    ## tam gdzie dotrę najdalej puszczam kolejnego dfsa, tym razem otrzymując ścieżkę
    picked = 0
    n = len(L)
    d1, p1 = bfs(L,picked)
    max_dist = 0
    for i in range(n):
        if d1[i] > max_dist:
            picked = i
            max_dist = d1[i]

    ## puszczam znowu bfsa na otrzymanie srednicy
    d,parent = bfs(L,picked)
    max_dist = 0
    for i in range(n):
        if d[i] > max_dist:
            picked = i
            max_dist = d[i]

    ## teraz odtwarzam średnicę        
    diameter = []
    diameter.append(picked)
    while(parent[picked] is not None):
        diameter.append(parent[picked])
        picked = parent[picked]


    ## teraz muszę zwrócić środkowy wierzchołek lub jeden z nich (jeśli parzysta ilość na średnicy
    n = len(diameter)
    return diameter[n//2]



print(best_root(L))



