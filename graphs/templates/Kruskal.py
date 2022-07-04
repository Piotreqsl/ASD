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

    ## zakładam że edges są posortowane rosnąco wedlee wag
    edges.sort(key= lambda x : x[2])
    ranks = [0 for _ in range(n)]
    parents = [i for i in range(n)]
    edges_used =  0


    for i in range(len(edges)):
        edge = edges[i]
        # wierzchołki połączone aktualnie rozważaną krawędzią
        u=edge[0]
        v=edge[1]
            
        if find_set(parents,u) != find_set(parents,v) :
            union(parents, ranks,u,v)
            edges_used+=1
            ## tu można appednować gdzieś te listy

        if(edges_used == n-1):
            break
    return