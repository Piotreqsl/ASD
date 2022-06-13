# Piotr Śliperski

from zad8testy import runtests


## Algorytm jest bardzo podobny do omawianego na wykładzie algorytmu Kruskala
## Jedyne co go modyfikuje, to fakt że zaczynam szukać drzewa od różnych krawędzi początkowych (zgodnie z posortowaniem)
## W ten sposób wiem że daną krawędź (początkową) na pewno biorę i obliczam minimalną różnicę wag tego drzewa rozpinającego
## Algorytmy union i find są typowe dla algorytmu kruskala.
## Jedyna róznica względem tych z wykładu to taka, że nie operuje na Nodea'ch
## Zauważyłem ze ich dzialanie znacząco spowalnia program




def find_set(parents,x) :
    if(x != parents[x]):
        parents[x] = find_set(parents,parents[x])
    return parents[x] 


def union(parents, ranks,x,y):
    x=find_set(parents,x)
    y=find_set(parents,y)

    if ranks[x] > ranks[y] :
        parents[y] =x
    elif ranks[y] > ranks[x]:
        parents[x] = y
    else:
        parents[x] =y
        ranks[y] +=1


def Kruskal(edges, n):
    ranks = [0 for _ in range(n)]
    parents = [i for i in range(n)]
  
    
    edges_used =  0
    min_cost = float("inf")
 


    for start in range(len(edges)): 
        for i in range(start,len(edges)):
            edge = edges[i]
            # wierzchołki połączone aktualnie rozważaną krawędzią
            u=edge[0]
            v=edge[1]
            
            if find_set(parents,u) != find_set(parents,v) :
                union(parents, ranks,u,v)
                edges_used+=1
            if(edges_used == n-1):
                min_cost = min(min_cost, edge[2] - edges[start][2]) ## Wiem że na pewno wziąłem wierzchołęk na pozycji start, oraz ten na którym sie zatrzymaliśmy
                break
        
        if(edges_used != n-1): ## pętle mogę przerwać ponieważ rozpatruję graf pełny
            break
            
            
        edges_used = 0
        ranks = [0 for _ in range(n)]
        parents = [i for i in range(n)]



    return min_cost


### funkcja zamiennik do tej z biblioteki math, nie wiem czy można było jej uzywać...
def ceil(n):
    return int(-1 * n // 1 * -1)



def calculate_len(P1, P2):
    return ceil(((P1[0] - P2[0]) ** 2 + (P1[1] -P2[1]) ** 2) ** (1/2))



def highway( A ):


    n = len(A) ## liczba miast
    if(n <= 1):
        return 0

    pos_edges = []
    for i in range(n):
        for j in range(i+1,n): ## tworze graf pełny z wagami - odległosciami miedzy miastami
            pos_edges.append((i,j,calculate_len(A[i], A[j])))
    
    pos_edges.sort(key= lambda x : x[2])




    # tu prosze wpisac wlasna implementacje

    #print(pos_edges)
    return Kruskal(pos_edges,n)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )