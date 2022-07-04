

from queue import Queue

def binary_search(T, x):
    l = 0
    r = len(T) - 1
    while l <= r:
        mid = (l + r) // 2
        if T[mid] == x:
            return mid
        elif T[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1




def dfs(graph, visited, u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)





def intuse(I, x, y):
    T = []
    for i in range(len(I)):
        T.append(I[i][0])
        T.append(I[i][1])
    T.sort()
    idx = 0
    vertices = [T[0]]
    for i in range(1, len(T)):
        if(T[i] != vertices[idx]):
            vertices.append(T[i])
            idx += 1

    ## jeśli nie ma wierzchołka x lub y
    result = []
    if binary_search(vertices, x) == -1 or binary_search(vertices, y) == -1:
        return result

    x_graph = [[] for _ in range(len(vertices))]
    y_graph = [[] for _ in range(len(vertices))]
    for i in range(len(I)):
        value_1 = binary_search(vertices, I[i][0])
        value_2 = binary_search(vertices, I[i][1])
        x_graph[value_1].append(value_2) ## z x do y 
        y_graph[value_2].append(value_1) ## z y do x
    x_visited = [False] * len(vertices)
    dfs(x_graph, x_visited, binary_search(vertices, x))
    y_visited = [False] * len(vertices)
    dfs(y_graph, y_visited, binary_search(vertices, y))
    for i in range(len(I)):
        value_1 = binary_search(vertices, I[i][0])
        value_2 = binary_search(vertices, I[i][1])
        if x_visited[value_1] and y_visited[value_2]:
            result.append(i)
    return result

A = [(4, 4), (4, 10), (2, 15), (6, 16), (3, 8), (2, 14), (6, 21), (3, 1), (0, 5), (7, 15), (3, 19), (2, 17), (4, 24), (7, 10), (5, 8), (4, 21), (6, 22), (9, 27), (2, 18), (1, 6), (5, 14), (5, 13), (0, 18), (10, 16), (9, 24), (11, 24), (5, 7), (6, 14), (1, 7), (3, 19), (11, 18), (6, 9), (11, 19), (9, 27), (7, 11), (13, 17), (10, 24), (8, 16), (11, 25), (11, 25), (11, 26), (12, 30), (4, 9), (5, 11), (10, 20), (6, 12), (14, 33), (13, 18), (8, 25), (15, 26)]
print(intuse(A,1,10))