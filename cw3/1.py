# ZD Lider ciągu
# 227115223
# jeżeli usuniemy 2 rózne (sic! różne) to lider sie nie zmieni
# usuwamy po 2 różne i jak nam zostanie coś to szukamy wsrod nich jako kandydatów rozw są w pliku majority el


# 1 kartkowka HEAP !!
# sortowanie quicksort

def QuickSort(A, p, r):
    if(p<r):
        q = partition(A,p,r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

def partition(A, p, r):
    x= A[r]
    i = p-1
    for j in range(p, r):
        if(A[j] <= x):
            i +=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

A = [5,4,3,8,9]
#QuickSort(A, 0, 4)
#print(A)


#def iterative QS

def iterativeQS(A):
    size = len(A)
    stack = []
    stack.append((0, size-1))
    while(len(stack) > 0):
        p,r = stack.pop()
        if(p<r):
            q = partition(A,p,r)
            stack.append((p, q-1))
            stack.append((q+1, r))



#quick sort z optymalnym kopcem

def optimalQS(A, p, r):
    while(p< r):
        q = partition(A, p, r)
        if(q-p <= r-q):
            optimalQS(A,p,q-1)
            p = q+1
        else:
            optimalQS(A,q+1,r)
            r = q-1


optimalQS(A, 0, 4)
print(A)
    





