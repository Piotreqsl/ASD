def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if(A[j] <= x):
            i+=1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i +1

def quickSort(A,p,r):
    while(p<r):
        mid = partition(A,p,r)
        if(mid-p < r-mid):
            quickSort(A,p,mid-1)
            p = mid+1
        else:
            quickSort(A,mid+1,r)
            r =mid-1

def checkSums(A):
    n = len(A)
    quickSort(A, 0, n-1)

    for i in range(n):
        flag = False
        dest, left, right = A[i], 0, n-1
        while (left < right):
            if left != i and right !=i:
                if(A[left] + A[right] == dest):
                    flag = True
                    break
                elif (A[left] + A[right] < dest):
                    left+=1
                else:
                    right -=1

            elif left ==i:
                left+=1
            else:
                right-=1
        if not flag:
            return False
    return True

A= [12,5,7,2,3,1,1,0,0,0]
print(checkSums(A))