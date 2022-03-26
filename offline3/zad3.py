#Piotr Śliperski
from zad3testy import runtests
#zadanie rozwiązane z uzyciem funkcji Quicksort z wykladu
# złozoność O(nlogn)
# pamieciowa O(logn) na stosie


def optimalQS(A, p, r):
    while(p< r):
        q = partition(A, p, r)
        if(q-p <= r-q):
            optimalQS(A,p,q-1)
            p = q+1
        else:
            optimalQS(A,q+1,r)
            r = q-1

def partition(A, p, r):
    x= A[r]
    i = p-1
    for j in range(p, r):
        if(A[j] <= x):
            i +=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def SortTab(T,P):

    optimalQS(T,0,len(T)-1)
    return T

runtests( SortTab )