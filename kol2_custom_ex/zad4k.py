from zad4ktesty import runtests

def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    ## dp[i][j] - minimalny koszt dojścia na pozycję i j 
    n = len(T)
    DP = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        DP[0][i] = DP[0][i-1] + T[0][i]
        DP[i][0] = DP[i-1][0] + T[i][0]
    for i in range(1,n):
        for j in range(1,n):
            DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + T[i][j]
    
    return DP[n-1][n-1]

    return 0

runtests ( falisz )
