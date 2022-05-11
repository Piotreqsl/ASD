"""Rozwazmy ciag (a0, . . . , an−1) liczb naturalnych. Załózmy, ze został podzielony
na k spójnych podciagów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1). Przez wartosc i-go podciagu
rozumiemy sume jego elementów a przez najgorszy podciag rozumiemy podciag o najmniejszej wartosci (rozstrzygajac
remisy w dowolny sposób). Wartoscia podziału jest wartosc jego najgorszego podciagu. Zadanie
polega na znalezienie podziału ciagu (a0, . . . , an−1) o maksymalnej wartosci."""

# f(m , p) - największa wartość najgorszego podziału dzieląc p pierwszych liczb na m spójnych podciągów

# f(m, p) = max(min(f(p - i, m - 1), sum(j = i + 1, p)T[i])); 0 <= i <= p - m


# A DP based Python3 program for
# painter's partition problem
 
# function to calculate sum between
# two indices in list
def sum(arr, start, to):
    total = 0
    for i in range(start, to + 1):
        total += arr[i]
    return total
 
# bottom up tabular dp
def findMax(arr, n, k):
     
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
 
    # 2 to k partitions
    for i in range(2, k + 1): # 2 to n boards
        for j in range(2, n + 1):
             
            # track minimum
            best = 100000000
             
            # j-1 th separator before position arr[p=1..j]
            for p in range(1, j + 1):
                best = min(best, max(dp[i - 1][p],
                                 sum(arr, p, j - 1)))    
 
            dp[i][j] = best
 
    # required
    return dp[k][n]
 
# Driver Code
arr = [5,10,30,20,15]
n = len(arr)
k = 3
print(findMax(arr, n, k))