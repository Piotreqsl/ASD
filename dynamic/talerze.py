
def printTwoDim(n):
    for i in range(len(n)):
        print(n[i])

def pascal(A,k,p):
    n = len(A)
    sums = [0]*n
    for i in range(n):
        sums[i] = [0] * k
        sums[i][0] = A[i][0]
        for j in range(1,k):
            sums[i][j] = sums[i][j-1] + A[i][j]
    ##F(i,p) = maksymalne piękno p talerzy jakie możemy uzyskać uwzględniając
    ## i pierwszych stosów
    F = [[float("-inf") for i in range(p+1)] for i in range(n+1)]
    
    for i in range(min(k,p)):
        F[1][i+1] = sums[0][i]
    

    for i in range(1,n):
        for cur_p in range(1,p+1):
         
            F[i+1][cur_p] = max(F[i+1][cur_p], F[i][cur_p])
            for prev_p in range(1,cur_p):
                F[i+1][cur_p] = max(F[i+1][cur_p], F[i][cur_p-prev_p] + sums[i][(prev_p%k)-1])
    printTwoDim(F)



A = [[1, 4, 1, 8, 5],
     [3, 1, 2, 1, 3],
     [2, 2, 3, 6, 7],
     [1, 1, 5, 4, 2]]

pascal(A,5,7)

#13
#14
#15
#16
