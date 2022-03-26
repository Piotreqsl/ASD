

from itertools import count
from random import randint


def minmax(A):
    _min = 0
    _max = 0
    for i in range(len(A)):
        _min = min(_min, A[i][1])
        _max = max(_max, A[i][1])
    return _min, _max


def countingSort(A, minel, maxel):
    k = (maxel- minel) +1
    count = [0] *k
    n=len(A)
    B = [0] *n

    for i in range(n):
        count[A[i][1] - minel] +=1
    for i in range(1,k):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        count[A[i][1] -minel] -=1
        B[count[A[i][1] - minel]] = A[i]
    for i in range(n):
        A[i] = B[i]



def sumSort(A,B,n):
    sums = [[0,0] for i in range(n)]
    for i in range(n):
        x = i*n
        sums[i][0] = x
        sums[i][1] = 0
        for j in range(n):
            sums[i][1] += A[x + j]
    minel, maxel = minmax(sums)
    countingSort(sums, minel,maxel)
    print(sums)
    for i in range(n):
        x = i*n
        lowerBound = sums[i][0]
        for j in range(n):
            B[x+j] = A[lowerBound + j]



n = 10
A = [randint(0,100) for i in range(n*n)]
B = [0 for i in range(n*n)]
sumSort(A,B,n)
print(B)