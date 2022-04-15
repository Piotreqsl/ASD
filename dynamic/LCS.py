



def printTwoDim(a):
    for i in range(len(a)):
        print(a[i])



def LCS(A,B):
    n = len(A)
    F = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(A[i-1] == B[j -1]):
                F[i][j] = F[i-1][j-1] + 1
            else: 
                F[i][j] = max(F[i][j-1], F[i-1][j])
    printTwoDim(F)
    return F[n][n]




## recursive with memoization
## i,j to indeksy odpowiednio do szukania dla A i B
def LCSRec(A,B,result, i,j ):
    if(i == 0 or j == 0):
        return 0
    
    if(result[i][j] != 0):
        return result[i][j]
    

    if(A[i-1] == B[j-1]):
        result[i][j] = 1 + LCSRec(A,B,result, i-1, j-1)
    else:
        result[i][j] = max(LCSRec(A,B,result, i-1, j), LCSRec(A,B,result, i, j-1))
    return result[i][j]



def LCSSimplier(A,B):
    n = len(A)
    result = [[0 for i in range(n+1)] for j in range(n+1)]
    LCSRec(A,B,result,n,n)
    printTwoDim(result)
    return result[n][n]

print(LCSSimplier([1,5,3,6,3],[4,1,3,6,5]))



            