'''Zadanie 1. Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami 
(wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero) 
i zwraca długość (wagę) najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane 
jest za pomocą obiektów typu Node:'''


class Node: 
    def __init__( self ): 
        self.children = 0 # liczba dzieci węzła 
        self.child = [] # lista par (dziecko, waga krawędzi) ... 
        self.f = float("-inf") ## długość najdłuższej sciezki konczącej się na tym wierzchołku (czyli od tego wierzchołka w dół)
        self.g = float("-inf") ## długość najdłuższej ścieżki w całym drzewie, (traktując node jako root, ale przechodzimy przez ten wierzchołek)

A = Node() 
B = Node() 
C = Node() 
A.children = 2 
A.child = [ (B,5), (C,-1) ]


def calc_ends(T):
    if T is None:
        return 0
    if T.children == 0:
        T.f = 0
        return 0

    for i in range(T.children):
        T.f = max(T.f, T.child[i][1] + calc_ends(T.child[i][0])) 

def calc_sec(T):
    max1 = float("-inf")
    max2 = float("-inf")

    if T.children ==0 or T.children == 1:
        T.g = 0
        return 0

    for i in range(T.children):
        if (T.child[i][1] + T.child[i][0].f > max1):
            max2 = max1
            max1 = T.child[i][1] + T.child[i][0].f
        elif (T.child[i][1] + T.child[i][0].f > max2):
            max2 = T.child[i][1] + T.child[i][0].f
    T.g = max1 + max2


def findMax(T, res):
    if T is None:
        return
    
    res[0] = max(res[0], T.f, T.g)
    for i in range(T.children):
        findMax(T.child[i][0], res)
    return



def heavy_path(T):
    calc_ends(T)
    calc_sec(T)
    res = [float("-inf")]
    findMax(T, res)
    return res[0]

print(heavy_path(A))
