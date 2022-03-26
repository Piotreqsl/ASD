def merge(A,p,s,k):
    l = p
    r = s
    ind = l
    tmp = [0] * len(A)
    while(l < s and r < k):
        if(A[l] <= A[r]):
            tmp[ind] = A[l]
            ind +=1
            l +=1
        else:
            tmp[ind] = A[r]
            r +=1
            ind +=1
    while(l<s):
        tmp[ind] = A[l]
        ind +=1
        l +=1
    while(r<k):
        tmp[ind] = A[r]
        ind +=1
        r +=1
    for i in range(p, k):
        A[i] = tmp[i]


        

def mergeSort(A, p,r):
    if (r-p <= 1):
        return
    s= (r+p) //2
    mergeSort(A,p,s)
    mergeSort(A,s,r)
    merge(A,p,s,r)

A= [0,3,4,67,5,3,2]
mergeSort(A,0,len(A))
print(A)
