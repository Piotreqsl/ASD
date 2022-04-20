'''Zbior przedzialow A
wyznacz k przedziałów, ktorych przeciecie jest jak najdluzszym przedziałem
Zwroc liste numerow przedziałow ktore nalezą do rozw
A = [[0,4], [1,10], [6,7], [2,8]]
k = 3
wynik:
[0,1,3]
co daje przedział o przecięciu [2,4z]

'''

## BŁEDNE NIESTETY :(())

from kintersect_tests import runtests

def count_intersect_val(A,B):
    if(A == float("-inf")):
        return float("-inf")
    start =0
    end = 0
    
    if(A[0] <= B[0]):
        start = B[0]
    else:
        start = A[0]
    if(A[1]<=B[1]):
        end = A[1]
    else:
        end = B[1]
    return end - start

def make_intersect(A,B):

    start =0
    end = 0
    if(A[0] <= B[0]):
        start = B[0]
    else:
        start = A[0]
    if(A[1]<=B[1]):
        end = A[1]
    else:
        end = B[1]
    return [start,end]

def printTwoDim(n):
    for i in range(len(n)):
        print(n[i])



def kintersect(A,k):
    n = len(A)
    for i in range(n):
        A[i] = [A[i][0], A[i][1], i]
    P = [[-1 for i in range(k+1)] for j in range(n+1)]
    #A.sort(key=lambda x: x[1], reversed=True)

    ##DP [i][k] wartość najdluższego przecięcia k przedziałów przy założeniu że badamy
    ## tylko i pierwszych oraz ity przedział jest ostatni 

    DP = [[float("-inf") for i in range(k+1)] for j in range(n+1)]

    for k in range(1,k+1):
        for n in range(1,n+1):
            if(k == 1):
                DP[n][k] = [A[n-1][0], A[n-1][1]]
                P[n][k] = n
            elif k > n:
                continue
            else:
                
                
                max_intersect = -1
                
                for prev_n in range(1,n):
                    cur_intersect = count_intersect_val(DP[prev_n][k-1],  [A[n-1][0], A[n-1][1]])
                    if(cur_intersect > max_intersect):
                        #print("k=",k,"parenta biore", A[prev_n-1])
                        max_intersect = cur_intersect
                        DP[n][k] = make_intersect(DP[prev_n][k-1], A[n-1])
                        P[n][k] = prev_n
    


    max_i = -1
    max_intersect = float("-inf")
    for i in range(1,n+1):
        if(DP[i][k] == float("-inf")):
            continue
        else:
            cur_intersect = DP[i][k][1] - DP[i][k][0]
            if(cur_intersect > max_intersect):
                max_intersect = cur_intersect
                max_i = i
    
    res = []
    for i in range(k, 0, -1):
        res.append(max_i -1)
        max_i = P[max_i][i]
    return sorted(res)


    #

A=[[0,4], [1,10], [6,7], [2,8]]
#
#kintersect(A,3)

runtests(kintersect)