## jeżeli mamy liczby z zakresu 1..k
## jeżeli zadanko z liczbami 1...n^2 to wtedy radix

def countingSort(A, k):
    n = len(A)
    count = [0] * (k+1)
    output_arr = [0] * n
    for i in range(n):
        count[A[i]] +=1
    for i in range(1,k+1):
        count[i] += count[i-1]
    
    for i in range(n-1,-1,-1):
        output_arr[count[A[i] -1]] == A[i]
        count[A[i]] -=1
    A = output_arr
    


A = [1 ,6,7,8,9,4]
countingSort(A,10)
print(A)