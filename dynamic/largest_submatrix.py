'''
Dana jest macierz binarna o rozmiarze MxN. Mamy znaleźć największą kwadratową pod-macierz
składającą się wyłącznie z "1".
'''


M = [[1,0,1,1,1,1],
     [1,0,1,1,1,1],
    [ 0,1,1,1,1,1],
    [0,0,1,1,1,1]]

def largest(M):
    DP = [[-1 for i in range(len(M[0]))] for j in range(len(M))]
    for i in range(len(M[0])):
        DP[0][i] = M[0][i]
    for j in range(len(M)):
        DP[j][0] = M[j][0]

    largest = 0

    for row in range(1,len(M)):
        for column in range(1, len(M[0])):
            if M[row][column] == 0:
                DP[row][column] = 0
            else:
                DP[row][column] = 1 + min(DP[row-1][column], DP[row][column-1], DP[row-1][column-1])
                if(DP[row][column] > largest):
                    largest = DP[row][column]
    return largest

print(largest(M))