from zad7ktesty import runtests 

from collections import deque 



def BFSVisit(T,i,j):
    glebokosc = len(T)
    szerokosc = len(T[0])
    sum = T[i][j]
    T[i][j] = -1
    if(i+1 < glebokosc and T[i+1][j] > 0):
        sum += BFSVisit(T,i+1,j)
    if (i -1 >= 0 and T[i-1][j] > 0):
        sum += BFSVisit(T,i-1,j)
    if(j+1 < szerokosc and T[i][j+1] > 0):
        sum += BFSVisit(T,i,j+1)
    if (j -1 >= 0 and T[i][j-1] > 0):
        sum += BFSVisit(T,i,j-1)
    
    return sum


def solve(W, Z, i,l, results):
    if(results[i][l] != 0):
        return results[i][l]
    
    if(i == 1):
        if(W[0] <= l):
            results[i][l] = Z[0]
        else:
            results[i][l] = 0
        return results[i][l]

    exclusion = solve(W,Z, i-1,l,results)
    if(W[i-1] > l):
        results[i][l] = exclusion
        return results[i][l]
    inclusion = solve(W,Z,i-1,l-W[i-1],results) + Z[i-1]

    results[i][l] = max(exclusion, inclusion)
    return results[i][l]




def ogrodnik (T, D, Z, l):
    n = len(D)

    glebokosci = [0 for i in range(n)]

    for i in range(n):
        glebokosci[i] = BFSVisit(T, 0, D[i])

  
    results = [[0 for i in range(l+1)] for i in range(n+1)]
    
    return solve(glebokosci, Z, n, l, results)
    ##return f(glebokosci, Z, l,n, results)

runtests( ogrodnik, all_tests=True )
