
A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
def tower(A):
    ## DP[i] - najdłużsy ciąg klocków kończący się na itym
    n = len(A)
    DP = [0] * n
    DP[0] =1
    for i in range(1,n):
        DP[i] = 1
        for j in range(i):
            if(A[i][0] >= A[j][0] and A[i][1] <= A[j][1]):
                DP[i] = max(DP[i], DP[j] + 1)
    return max(DP)

print(tower(A))