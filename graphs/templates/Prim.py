from queue import PriorityQueue

# O(E*log(V))
def prim_nl(graph, s=0):
  n = len(graph)
  queue = PriorityQueue()
  in_mst = [False]*n

  in_mst[s] = True # startujemy w s wiec odznaczamy
  T = [] # MST

  for v, w in graph[s]:
    queue.put((w, v, s))

  while not queue.empty():
    w, u, p = queue.get()

    if not in_mst[u]:
      T.append([p, u, w])
      in_mst[u] = True

      if len(T) == n - 1:
        return T

      for v, w in graph[u]:
        if not in_mst[v]: # jezeli jest juz w MST to krawedzie wychodzace
        # sa w kolecje lub zostaly juz przetworzone
          queue.put((w, v, u))

  # graf niespojny
  return None