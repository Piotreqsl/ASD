from collections import deque


def check_if_full(graph):
  n = len(graph)

  for i in range(n):
    for j in range(n):
      if i != j and graph[i][j] == 0:
        return False

  return True


# O(n^2)
def bfs(graph, s):
  n = len(graph)
  queue = deque()
  visited = [False]*n # O(n)
  distances = [-1]*n # O(n)
  parents = [-1]*n # O(n)

  distances[s] = 0
  visited[s] = True
  queue.append(s)

  while queue: # O(n)
    u = queue.popleft()

    if distances[u] == 2:
      break

    for v in range(n): # O(n)
      if graph[u][v] == 1:
        if not visited[v]:
          distances[v] = distances[u] + 1
          parents[v] = u
          visited[v] = True
          queue.append(v)
        else:
          if distances[v] == 2:
            return (parents, u, v)

  return (None, None, None)


# O(n^3)
def find_cycle_length_4(graph):
  n = len(graph)

  # jezeli graf jest pelny to usuwamy jedna krawedz, inaczej dla tego przypadku algorytm nie zadziala.
  # nie zadziala poniewaz dla kazdego punktu min odleglosc bedzie rowna 1.
  # na koniec cofamy ta zmiane
  is_full = check_if_full(graph) # O(n^2)
  if is_full:
    graph[0][n-1] = 0

  # dla kazdego wierzcholka odpalamy bfsa na max odleglosc 2.
  # jezeli znajdziemy jakis wierzcholek, ktory ma odleglosc 2 od poczatkowego
  # to oznacza to, ze obecny wierzcholek przez krawedz z tym wierzcholkiem tworzy cykl o dlugosci 4
  for i in range(n): # O(n)
    parents, s, e = bfs(graph, i) # O(n^2)
    if parents != None:
      break



  if is_full:
    graph[0][n-1] = 1

  return [s, parents[s], parents[e], e]


# [5, 3, 4, 6]
graph = [[0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 0]]
print(find_cycle_length_4(graph))

### cwiki

def brute(G):
  n = len(G)
  for a in range(n):
    for b in range(a+1, n):
      counter = 0
      for i in range(0,n):
        if(i != a and i != b and G[a][i] and G[i][b]):
          counter += 1
        if counter >= 2:
          return True
  return False

print(brute(graph))
      