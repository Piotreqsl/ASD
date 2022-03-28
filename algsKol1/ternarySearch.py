def search(A,x):
    p = 0
    r = len(A)-1
    while(p<=r):
        mid1=p+(r-p)//3
        mid2=r-(r-p)//3

        if(A[mid1] ==x):
            return mid1
        elif(A[mid2] == x):
            return mid2
        if(x<A[mid1]):
            r=mid1-1
        elif(x>A[mid2]):
            p = mid2+1
        else:
            p = mid1+1
            r = mid2-1
    return -1
A =[1,2,3,4,5,6]
print(search(A,4))