from random import randint
from math import log, ceil, inf

def insertionSort(A):
        n = len(A)
        selected = A[n-1]
        j = n-2
        while(j >=0 and A[j][0] > selected[0]):
            A[j+1] = A[j]
            j-=1
        A[j+1] = selected

def bin_search(A,x):
    n = len(A)
    if(n == 0):
        return None
    else:
        l = 0
        r = n-1
        while( l <= r):
            s = (l +r) //2
            if(A[s][0] == x):
                return s
            elif(A[s][0] < x):
                l = s+1
            else:
                r = s-1
    return None


def countingSort(A):
    n = len(A)
    maxno = ceil(log(n, 2)) + 1
    count = [0] * maxno

    output = [0] * n
    for i in range(n):
        count[A[i]] +=1
    for i in range(1, maxno):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        output[count[A[i]]-1] = A[i]
        count[A[i]] -=1
    for i in range(n):
        A[i] = output[i]
    

def sortLogn(A):
    uniques =[]
    count = 0

    for element in A:
        res = bin_search(uniques, element)
        if(res is None):
            uniques.append([element,1])
            insertionSort(uniques)
        else:
            uniques[res][1] +=1
    #printuje uniqes z krotnosciami
    index = 0
    for i in range(len(uniques)):
        for j in range(uniques[i][1]):
            A[index] = uniques[i][0]
            index +=1







n = 100
_n = ceil(log(n, 2))
A = [randint(0, _n) for i in range(n)]
sortLogn(A)
print(A)