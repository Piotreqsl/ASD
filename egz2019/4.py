## Żaba zbigniew

## DP[i][y] - minimalna lcizba skoków jakie musi wykonać zbigniew żeby dotrzeć do i mając dokładnie y jednostek energii


A = [2,2,1,0,0,0]

def zbigniew(A):
    n = len(A)
    max_e = sum(A)
    DP = [[float("inf") for i in range(max_e+1)] for j in range(n)]
    DP[0][A[0]] = 0

    for i in range(n):
        for e in range(max_e +1):
            if(DP[i][e] != float("inf")): ## jeżeli mogę się tu dostać mając tyle energii
                for k in range(1,e+1): ## tu istotne że muszę rozważyc całą energieee
                    if(i+k < n and e - k + A[i + k] <= max_e):
                        DP[i+k][A[i+k] + e -k] = min(DP[i+k][A[i+k] + e -k], DP[i][e] + 1)
    res = min(DP[n - 1])
    return res

print(zbigniew(A))