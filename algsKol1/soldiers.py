from random import randint
## inversed quicksort
## n modified quickselect
# na poczatku znajduje element na pozycji p => elementy na lewo od p są wieksze a na prawo mniejsze
# potem w przedziale (p, len(tab)) znajdujemy q => elementy od p do q są wieksze od q a na prawo mniejsze
# i juz mamy spreparowaną tablice i gites

def partition(A,p,r,pivot):
    x = A[pivot]
    A[pivot], A[r] = A[r], A[pivot]
    i = p-1
    for j in range(p,r):
        if(A[j] >= x):
            i+=1
            A[j], A[i] = A[i], A[j]
    i+=1
    A[r], A[i] = A[i], A[r]
    return i

def quickSelect(A,p,r,index):
    if p == r:
        return A[p]
    mid = partition(A,p,r,r)
    if mid == index:
        return A[mid]
    elif mid > index:
        return quickSelect(A,p,mid-1,index)
    else:
        return quickSelect(A,mid+1,r,index)
    


def soldiers(A,p,q):
    result = [0] * (q-p+1)
    quickSelect(A,0,len(A)-1, p)
    quickSelect(A,p,len(A)-1, q)
    ind = 0
    for i in range(p,q+1):
        result[ind] = A[i]
        ind +=1
    return result

T = [randint(170, 210) for _ in range(20)]
print(soldiers(T, 5, 9))
print(sorted(T, reverse=True))