


from cmath import inf



def impatientBob(A,i,j,F): ## i < rozpatrywana ilość prac i ita jest ostanią wybraną len(A) , j <= k ile prac musi wziąć
    if(j == 1):
        F[i][j] = 0
        return F[i][j]
    if (j > i+1):
        F[i][j] = float("inf")
        return F[i][j]

   
    if F[i][j] is not None:
        return F[i][j]

    best = float("inf")    
    for prev in range(i):
        if(A[prev][1] <= A[i][0]):
             best = min(best, impatientBob(A,prev,j-1,F) + A[i][0] - A[prev][1])
    
    F[i][j] = best
    return F[i][j]

def bobRecursively(A,k):
    n = len(A)
    F = [[None] * (k+1) for _ in range(n+1)]
    for i in range(n):
        _ = impatientBob(A,i,k,F)
    result = float("inf")
    for i in range(n):
        if(F[i][k] is not None):
            result = min(result, F[i][k])
    return result
    

def bob_2(A,k):
    n = len(A)
    A = sorted(A, key=lambda x: x[1])
    print(A)
    F = [[inf] * (k+1) for _ in range(n)]
    for i in range(n):
        F[i][0] = 0
        F[i][1] = 0
    for i in range(1, n):
        for j in range(2,i+2):
            if j < k+1:
                for p in range(j-2, i):
                    if A[i][0] - A[p][1] >= 0:
                        F[i][j] = min(F[i][j], F[p][j-1] + A[i][0] - A[p][1])
    res = inf
    for i in range(n):
        res = min(res, F[i][k])
    return res


A = [(2,3),(4,7),(3.5,10), (11,20)]

print(bob_2(A,3))
print(bobRecursively(A,3))


                
            
    
        





## k = 4 nie działa
## k =2 działa 60 minut (1h)
A = [[1,5],[7,9],[6,10],[12,15]]