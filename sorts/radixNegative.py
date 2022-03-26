
def counting(A,n,exp):
    cnt = [0]*10

    for i in range(n):
        index = int((A[i]/exp)%10)
        cnt[index] +=1
    
    for i in range(1, 10): # O(b)
        cnt[i] += cnt[i-1]
    
    output = [0] * n
    for i in range(n-1,-1,-1):
        index = int((A[i]/exp)%10)
        output[cnt[index]-1] = A[i]
        cnt[index] -=1
    
    for i in range(n): # O(n)
        A[i] = output[i]


def radix(A):
    _min = min(A)
    _max = max(A)
    n=len(A)
    for i in range(n): # O(n)
        A[i] -= _min

    _max -= _min

    exp = 1
    while(_max / exp > 1):
        counting(A,n,exp)
        exp *=10
    
    for i in range(n): # O(n)
     A[i] += _min

A = [99, 100, 27, 14, 0, 82, 70, 45, 14, -234, -15]


radix(A)
print(A)