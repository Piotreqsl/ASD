
## albo zaczynamy poddrzewo w danym wierzchołku albo nie

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane

def through_tree(T,i,k):
    if T is None or i < 0:
        return float("-inf")
    if T.X is not None and T.X[i] is not None:
        return T.X
    if T.X is None:
        T.X = [None] * k+1
        T.X[0] = 0
    best = float("inf")
    best = max(best, through_tree(T.left, i-1, k) + T.leftval, through_tree(T.right, i-1,k) + T.rightval)
    for d in range(i-1):
        best = max(best, through_tree(T.left, i - 2 - d, k) + through_tree(T.right, d, k) + T.leftval + T.rightval)
    T.X[i] = best
    return best




def rec(T,k):
    if(T.left is not None):
        rec(T.left, k)
    if(T.right is not None):
        rec(T.right, k)
    through_tree(T,k,k)
    

def get_max(T, k, res):
    if T is not None:
        res[0] = max(res[0], T.X[k])
        get_max(T.left, k, res)
        get_max(T.right, k, res)


def valuableTree(T, k):
    rec(T, k)
    res = [float("-inf")]
    get_max(T, k, res)
    return res[0]