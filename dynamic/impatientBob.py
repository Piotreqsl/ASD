


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
    for i in range(1,n):
        if(DP[i][k] < smallest):
            smallest = DP[i][k]
    print("wynik to", smallest)


A= [[1,4], [4,16],[14,17]]
impatient(A,2)

                
            
    
        





## k = 4 nie działa
## k =2 działa 60 minut (1h)
A = [[1,5],[7,9],[6,10],[12,15]]