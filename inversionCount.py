## Rozwiązanie wykorzystuje mergeSorta
## Jeśli biorę z drugiej połowy a nie z pierwszej to do inv counta dodaje środek - lewy  (początek jest fixed)



tmp = [0]

def inversionMerge(T, p, s, k):
    global tmp
    inversions =0
    l = p
    r = s
    ind = l
    while(l < s and r < k):
        if(T[l] <= T[r]):
            tmp[ind] = T[l]
            ind += 1
            l +=1
        else:
            tmp[ind] = T[r]
            inversions += (s -l) 
            ind +=1
            r +=1
    while(l < s):
        tmp[ind] = T[l]
        l += 1
        ind +=1
    while(r < k):
        tmp[ind] = T[r]
        r += 1
        ind +=1
    
    for i in range(p, k):
        T[i] = tmp[i]
    
    return inversions



def inversionMergeSort(T,p,k):
    counter = 0 
    if( k - p == 1):
        return 0
    s = (p + k) //2
    counter += inversionMergeSort(T,p,s)
    counter += inversionMergeSort(T, s, k)
    counter += inversionMerge(T,p,s,k)
    return counter


def countInversions(T):
    global tmp
    n = len(T)
    tmp = [0 for i in range(n)]
    return inversionMergeSort(T,0,n)


print(countInversions([1,3,5,2,4,6]))