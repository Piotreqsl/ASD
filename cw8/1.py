## czy graf jest dwudzielny

import queue


def czy_dwudzileny(graph)
    n = len(graph)
    visited = [False for i in range(n)]
    part = [None for i in range(n)]
    visited[0] = True
    part[0] = True

    q= queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in range(len(graph[u])):
            if(visited[graph[u][i]]):
                if(part[graph[u][i]] == part[u]):
                    return False

            visited[graph[u][i]] = True
            part[graph[u][i]] = not part[u]
            q.put(graph[u][i])