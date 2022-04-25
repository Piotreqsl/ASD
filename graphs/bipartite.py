import re


def is_bipartite(graph,s):
    visited = [None] * len(graph)
    flag = True

    def dfs_visit(u,color):
        nonlocal graph, visited, flag

        visited[u] = color

        for v in graph[u]:
            if not flag:
                return
            if visited[v] is not None:
                if(visited[v] == color):
                    flag = False
                    return
            else:
                dfs_visit(v,(color+1)%2)
    for v in range(len(graph)):
        if visited[v] is None:
            dfs_visit(v, 0)
    return flag

# True
# graph = [[3, 5],
#          [2, 6],
#          [1],
#          [0, 4],
#          [3],
#          [0, 6],
#          [1, 5]]


# False
graph = [[],
         [2, 3],
         [1, 3],
         [1, 2]]

print(is_bipartite(graph, 0))