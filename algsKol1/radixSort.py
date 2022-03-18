def countingSort(A,exp):
    n = len(A)
    count = [0] * 10
    output = [0] *n 
    for i in range(n):
        index = A[i] // exp
        count[index % 10] +=1
    for i in range(1,10):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        index = A[i] // exp
        output[count[index %10] -1] = A[i]
        count[index % 10] -= 1
 
    i = 0
    for i in range(0, n):
        A[i] = output[i]




def radixSort(A):
    max1 = max(A)

    exp =1

    while(max1/exp > 1):
        countingSort(A, exp)
        exp *= 10

A = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(A)
print(A)