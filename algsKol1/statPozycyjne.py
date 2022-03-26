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
        return A[p]
    else:
        q = partiton(A,p,r)
        if( q == k):
            return A[k]
        elif (q < k):
            return select(A, q+1, r, k)
        else:
            return select(A, p, q-1, k)
print(select(A,0, len(A)- 1, 2))


## OPCJA nr 2 to algorytm magicznych piątek, czyli mediana median
# pomocniczo insertion sorcik na sortowanie małych problemów


