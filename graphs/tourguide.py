from queue import PriorityQueue

graph = [[(1, 2), (2, 5)],
            [(2, 1), (3, 7)],
            [(4, 3)],
            [(5, 1)],
            [(3, 2), (5, 5)],
            []]





def dijkstra_tour_guide(G,s ,t): ## zwróce tylko min trase

    def relax(u,v,weight):
        if(distances[v] < min(distances[u], weight)):
            distances[v] = min(distances[u], weight)
            return True
        return False

    n = len(G)
    queue = PriorityQueue()
    distances = [float("-inf")] * n

    distances[s] = float("inf")
    queue.put((distances[s],s))

    while not queue.empty():
        u = queue.get()[1] ## wierzchołek

        
        for v, weight in G[u]:
            if(relax(u,v,weight)):
                queue.put((distances[v], v))
    print(distances)
    return distances

dijkstra_tour_guide(graph,0,3)