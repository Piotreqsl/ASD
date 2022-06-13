

def jumper(G,s,w):
    n = len(G)
    new_G=[[-1]*(2*n) for i in range(2*n)]

    for i in range(n):
        for j in range(n):
            if(G[i][j] != 0):
                new_G[i][j] = G[i][j]
    

    ## łącze dwie krawędzie do dwumilowych butów

    for i in range(n):
        for j in range(n):
            if(G[i][j] != 0):
                for k in range(n):
                    if(G[j][k] != 0 and k !=i):
                        if(new_G[i][n+k] == -1):
                            new_G[i][n+k] = max(G[i][j], G[j][k])
                        else:
                            new_G[i][n+k] = min(new_G[i][n+k],max(G[i][j], G[j][k]))
    
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G[i+n][j] = G[i][j]
    
    ## puszczam dijkstre z wierzchołka s i zwracam d[t] i d[t+n] (bo mogłem tam dojść zwyczajnie lub stumilowo)