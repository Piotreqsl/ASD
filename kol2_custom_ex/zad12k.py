from zad12ktesty import runtests 

def printTwoDim(a):
    for i in range(len(a)):
        print(a[i])



## można też  sumy prefiksowe co jest pożądane wsm
# function to calculate sum between
# two indices in list
def sum(arr, start, to):
    total = 0
    for i in range(start, to + 1):
        total += arr[i]
    return total
 
# bottom up tabular dp
def findMax(arr, k):
    n = len(arr)
    # initialize table
    dp = [[0 for i in range(n + 1)]
             for j in range(k + 1)]
 
    # base cases
    # k=1
    for i in range(1, n + 1):
        dp[1][i] = sum(arr, 0, i - 1)
 
    # n=1
    for i in range(1, k + 1):
        dp[i][1] = arr[0]
 

    ## DP[k][p] - p pierwszych liczb podzielone na k elementów
    # 2 to k partitions
    for i in range(2, k + 1): # 2 to n boards
        for j in range(2, n + 1):
             
            # track minimum
            best = float("inf")
             
            # i-1 th separator before position arr[p=1..j]
            for p in range(1, j + 1):
                best = min(best, max(dp[i - 1][p],
                                 sum(arr, p, j - 1)))    
 
            dp[i][j] = best
 
    # required
    return dp[k][n]

runtests ( findMax,all_tests=True )