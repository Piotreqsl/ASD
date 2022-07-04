


def opt_sum(tab):

    def minAbsVal(a,b):
        if abs(a) < abs(b):
            return a
        else:
            return b

    def maxAbsVal(a,b):
        if abs(a) > abs(b):
            return a
        else:
            return b

        


    n = len(tab)
    DP = [[0 for i in range(n)] for j in range(n)]

    ##DP[i][j] - maksymalna wartość bezwględna wyniku tymczasowego w sumie

    ## sumy prefikowe
    addedSums = [0] * (n + 1)

    #dodajemy do obecnej wartosci wartosc wszystkich poprzednich
    for i in range(1,n + 1):
        addedSums[i] = addedSums[i - 1] + tab[i - 1]

    
    for length in range(1, n):
        for start in range(n-length):
            end = start+length
            DP[start][end] = addedSums[end + 1] - addedSums[start]

            best = float("inf")
            for k in range(start, end):
                best = minAbsVal(maxAbsVal(DP[start][k], DP[k+1][end]), best)
            
            DP[start][end]= maxAbsVal(best,DP[start][end])

            
    return DP[0][n-1]


print(abs(opt_sum([1,-5,2])))