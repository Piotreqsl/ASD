


from cmath import inf


def printTwoDim(n):
    for i in range(len(n)):
        print(n[i])

def impatient(A, k):
    n = len(A)
    ##F[I][J] - minimalna liczba minut jakie musi czekać,
    ## jesli wybierze j  prac sposórd  pierwszych elementów
    ## i zeby ji była ostatnią wybraną

    ## j < k

    DP = [[inf for j in range(k+1)] for i in range(n+1)]
    
    for j in range(k+1): ## jesli wybierze jedna pracę to nic nie musi czekać
        DP[0][j] = 0

    for j in range(n+1):
        DP[j][0] = 0

    for i in range(n):
        DP[i+1]

    for j in range(1,k+1):
        for i in range(1,n+1):
                if(j == 1):
                    DP[i][j] = A[i-1][0] ## bo pierwszy el
                    continue
                if(j > i):
                    continue
                for prev_i in range(1,i):
                    if(A[prev_i-1][1] <= A[i-1][0]):
                        DP[i][j] = min(DP[i][j], DP[prev_i][j-1] + (A[i-1][0] - A[prev_i-1][1]))
    printTwoDim(DP)

    smallest = inf
    for i in range(1,n+1):
        if(DP[i][k] < smallest):
            smallest = DP[i][k]
    print("wynik to", smallest)



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
#impatient(A,2)
#print(bob_2(A,2))
print(bobRecursively(A,3))


                
            
    
        





## k = 4 nie działa
## k =2 działa 60 minut (1h)
A = [[1,5],[7,9],[6,10],[12,15]]