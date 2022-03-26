def gcd(a, b):
  while b != 0:
    a, b = b, a%b
  return a


def shift_array(A, k):
  n=len(A)
  tmp = [0]*n
  for i in range(n):
      index = (i + k) %n
      tmp[index] = A[i]


  return tmp


A = [1, 2, 4, 3, 8, 6, 12]
print(shift_array(A, 4))