from math import *
def komiwojazer(T):
    n = len(T)
    D = [[0 for _ in range(n)] for _ in range(n)]
    F = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            D[i][j] = dist((T[i][1], T[i][2]), (T[j][1], T[j][2]))
    F[0][1] = D[0][1]
    res = inf
    for i in range(n-2,-1,-1):
        res = min(res,tspf(i,n-1,F,D)+D[i][n-1])
    print(F)
    return res
def tspf(i,j,F,D):
    if F[i][j] != inf:
        return F[i][j]
    if i == j-1:
        res = inf
        for k in range(j-1):
            res = min(res,tspf(k,j-1,F,D)+D[k][j])
        F[j-1][j] = res
    else: #i<j-1
        F[i][j] = tspf(i,j-1,F,D) + D[j-1][j]
    return F[i][j]

C = [["A", 0, 2], ["B", 4, 3], ["C", 2, 4], ["D", 3, 1], ["E", 1, 3],["F",0.5,-2]]
C = sorted(C, key=lambda x: x[1])
print(komiwojazer(C))