## CWICZENIA 24.03
## Sortowania liniowe

## Zaimplementuj algorytm sortujący tablice z liczbami 0... n^2-1
## radix sort - sortowanie pozycyjne

def radix(A):
    n = len(A)
    B = [0] * n
    C = [0] * n
    for x in A:
        C[x%n] +=1

    for i in range(1, n):
        C[i] += C[i-1]
    
    for i in range(n-1, -1, -1):
        index = A[i]%n
        C[index] -= 1
        B[C[index]] = A[i]
        
    
    
    C = [0 for _ in range(n)]
    for x in B:
        C[x//n] +=1
    for i in range(1,n):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        k = B[i]//n
        C[k] -=1
        A[C[k]] =B[i]

A = [99,67,43,52,10,7,92,65,34,97]
radix(A)
print(A)