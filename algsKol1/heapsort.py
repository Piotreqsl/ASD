def left(i):
    return 2 *i +1
def right(i):
    return 2*i +2
def parent(i):
    return (i-1) //2

def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if (l < n and A[l] > A[max_ind]):
        max_ind = l
    if( r < n and A[r] > A[max_ind]):
        max_ind =r
    
    if(max_ind != i):
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

def addToHeap(A, el):
    A.append(el)
    i = len(A) -1
    while(i > 0 and A[i] > A[parent(i)]):
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def heapSort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

A = [7,4,3,9,8]
build_heap(A)
print(A)
addToHeap(A, 10)
print(A)
heapSort(A)
print(A)