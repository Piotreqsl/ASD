def GCD(a,b):
    while b!=0:
        a,b =b, a%b
    return a



def leftRotate(arr, k):
    n = len(arr)
    k = k % n #for certainty
    gcd = GCD(n,k)
    for i in range(gcd):
        temp = arr[i]
        j =i
        while 1:
            next = j +k
            if next>=n:
                next = next -n
            if next == i:
                break
            arr[j] = arr[next]
            j=next
        arr[j] = temp
A= [1,2,3,4,5,6,7,8,9]
leftRotate(A,1)
print(A) 