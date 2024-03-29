from math import inf


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.sum_of_edges = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def count_sum_of_edges(T):
    for e in T.edges:
        count_sum_of_edges(e)
    for i in range(len(T.edges)):
        T.sum_of_edges += T.weights[i] + T.edges[i].sum_of_edges


def find_best(root, node, best_index, best_diff):
    for i in range(len(node.edges)):
        actual_index, actual_diff = find_best(root, node.edges[i], best_index, best_diff)
        root_subtree = root.sum_of_edges - node.edges[i].sum_of_edges - node.weights[i]
        node_subtree = node.edges[i].sum_of_edges
        if(actual_diff < best_diff):
            best_diff = actual_diff
            best_index = actual_index
        if(abs(root_subtree - node_subtree) < best_diff):
            best_diff = abs(root_subtree - node_subtree)
            best_index = node.ids[i]
    return best_index, best_diff


def balance(T):
    count_sum_of_edges(T)
    best_index, best_diff = find_best(T, T, None, inf)
    return best_index