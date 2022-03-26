## jeżeli mamy liczby z zakresu 1..k
## jeżeli zadanko z liczbami 1...n^2 to wtedy radix

def counting_sort(A, _min, _max):
  m = _max - _min + 1
  n = len(A)
  Count = [0]*m

  for i in range(n): # O(n)
    Count[A[i]-_min] += 1

  for i in range(1, m): # O(m)
    Count[i] += Count[i-1]

  B = [0]*n
  for i in range(n-1, -1, -1): # O(n)
    B[Count[A[i]-_min]-1] = A[i]
    Count[A[i]-_min] -= 1

  for i in range(n): # O(n)
    A[i] = B[i]

  return A


A = [10, -2, 14, -9, 3, 8, 1]
print(counting_sort(A, min(A), max(A)))