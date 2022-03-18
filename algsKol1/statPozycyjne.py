## jeżeli chcemy sprawdzić na jaki element bedzie stał na pozycji k w finalnie posortowanej tablicy

## 1 opcja to takie ala wyszukiwanie binarne z funkcją partition z QS

import math


def partiton(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1

A = [3, 8, 6, 4, 5, 9, 2]


def select(A, p, r,k):
    if(p == r):
        return A[k]
    else:
        q = partiton(A,p,r)
        if( q == k):
            return A[k]
        elif (q < k):
            return select(A, q+1, r, k)
        else:
            return select(A, p, q-1, k)
#print(select(A,0, len(A)- 1, 0))


## OPCJA nr 2 to algorytm magicznych piątek, czyli mediana median
# pomocniczo insertion sorcik na sortowanie małych problemów

A = [1,4,8,9,2,3,4,5,7,89,7,3,4,5,7,9,8,7,6,5]


def insertionSort(A, left, right):

    for j in range(left + 1, right + 1):
  
        selected = A[j]
        i = j-1
        while(i >= left and A[i] > selected):
            A[i+1] = A[i]
            i -=1
        A[i+1] = selected



def magicznePiatki(A, k):
    #zakłądam że listy są długosći n = 5k
    n = len(A)

    if(n < 10):
        insertionSort(A, 0, n-1)
        return A[k]

    start = 0
    end = 4

    while(end <= n -1):
        insertionSort(A, start, end)
        start += 5
        end += 5


    mediany = [A[i] for i in range(2, n, 5)]
    medianaMedian = magicznePiatki(mediany, math.ceil(len(mediany) /2))
    i = 0

    for i in range(len(mediany)):
        if(mediany[i] == medianaMedian):
            break
    return (i*5) +2
    


def partitonCustomPivot(A, p, r, custom):
    A[custom], A[r] = A[r], A[custom]
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1



def magic_select(A, p, r,k):
    if(p == r):
        return A[k]
    else:
        magic_pivot= magicznePiatki(A,k)
        q = partitonCustomPivot(A,p,r, magic_pivot)
        if( q == k):
            return A[k]
        elif (q < k):
            return magic_select(A, q+1, r, k)
        else:
            return magic_select(A, p, q-1, k)

 
   
print(magic_select(A,0, len(A) -1, 6))
print(select(A,0, len(A) -1, 6)) ##cos nie dziala ??



