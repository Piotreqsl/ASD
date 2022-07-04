
T = [123,890,688,587,257,246]

def create_tables(P):
    tables = []
    for each in P:
        blank = [0 for i in range(10)]
        while(each > 0):
            blank[each % 10] +=1
            each = each // 10
        tables.append(blank)
    return tables


def have_comm(i,j, tables):
    for a in range(10):
        if(tables[i][a] > 0 and tables[j][a] > 0):
            return True
    return False



def createGraph(P):
    n = len(P)
    G = [[] for i in range(n)]
    tables = create_tables(P)
    for i in range(n):
        for j in range(i+1,n):
            if(have_comm(i,j,tables)):
                cost = abs(P[i] - P[j])
                G[i].append((j, cost))
                G[j].append((i, cost))
    return G

def getMinVertex(processed, distance):
    _min = float('inf')
    u = None
    for i in range(len(distance)):
        if not processed[i] and _min > distance[i]:
            _min = distance[i]
            u = i
    return u

def dijkstry( G, s, e ):
    def relax(u, v, weight):
        if D[v] > D[u] + weight:
            D[v] = D[u] + weight
            Parent[v] = u

    n = len(G)
    processed = [False] * n
    D = [float('inf')] * n
    Parent = [-1] * n
    D[s] = 0
    for i in range(n):
        u = getMinVertex(processed, D)
        if u == None:
            break
        processed[u] = True
        for v, weight in G[u]:
            if not processed[v]:
                relax(u,v,weight)
    
    return D[e]





def find_cost(P):
    n = len(P)
    G = createGraph(P)
    _min = float('inf')
    _max = -float('inf')
    minIDX = None
    maxIDX = None

    for i in range( n ):
        if P[i] > _max:
            _max = P[i]
            maxIDX = i
        
        if P[i] < _min:
            _min = P[i]
            minIDX = i

    res = dijkstry(G, minIDX, maxIDX)
    if res == float('inf'):
        return -1
    else:
        return res

print(find_cost( T ))