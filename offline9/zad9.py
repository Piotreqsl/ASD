from zad9testy import runtests
from collections import deque

def bfs(graph, s, e, parents):
  n = len(graph)
  queue = deque()
  visited = [False]*n

  visited[s] = True
  queue.append(s)

  while queue:
    u = queue.popleft()
    for v in range(n):     
      if graph[u][v] > 0 and not visited[v]:
        visited[v] = True
        parents[v] = u

        if v == e:
          return True

        queue.append(v)

  return False


# O(V*E^2)
def ford_fulkerson(graph, src, sink):
  n = len(graph)
  copied = [[graph[i][j] for j in range(n)] for i in range(n)]

  parents = [None]*len(graph)
  max_flow = 0

  while bfs(copied, src, sink, parents):
    curr_flow = float("inf")
    
    v = sink
    while v != src:
      curr_flow = min(curr_flow, copied[parents[v]][v])
      v = parents[v]

    max_flow += curr_flow

    v = sink
    while v != src:
      u = parents[v]
      copied[u][v] -= curr_flow
      copied[v][u] += curr_flow
      v = parents[v]

  return max_flow


def highway( G,s ):
    graph_len = 0
    for e in G:
        graph_len = max(graph_len, e[1], e[0])
    graph_len +=2
    normal_graph = [[0]*graph_len for i in range(graph_len)]
    for e in G:
        normal_graph[e[0]][e[1]] = e[2]
    n = graph_len -1
    max_flow = 0
    for i in range(n):
        for j in range(i+1,n):
            if(i == s or j ==s):
                continue
            normal_graph[i][n] = 10**10
            normal_graph[j][n] = 10**10
            res = ford_fulkerson(normal_graph,s,n)
          
            max_flow = max(max_flow, res)
            normal_graph[i][n] = 0
            normal_graph[j][n] = 0


    # tu prosze wpisac wlasna implementacje
    return max_flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )