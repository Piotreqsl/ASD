def preprocessArr(A):
  for x in range(len(A)):
    count = [0] * 10
    liczba = A[x]
    while(liczba > 0):
      count[liczba%10] +=1
      liczba = liczba //10
    single, multi = 0, 0
    for i in range(10):
      if(count[i] == 1):
        single +=1
      elif(count[i] > 1):
        multi +=1
    A[x] = [A[x], single, multi]

def sortByMulti(A):
  n = len(A)
  count = [0] * 10
  B = [0] * n
  for i in range(n):
    count[A[i][2]] +=1
  for i in range(1,10):
    count[i] += count[i-1]
  for i in range(n-1 ,-1, -1):
    B[count[A[i][2]]- 1] = A[i]
    count[A[i][2]] -=1
  for i in range(n):
    A[-i-1] = B[i]

def sortBySingle(A):
  n = len(A)
  count = [0] * 10
  B = [0] * n
  for i in range(n):
    count[A[i][1]] +=1
  for i in range(1,10):
    count[i] += count[i-1]
  for i in range(n-1,-1,-1):
    B[count[A[i][1]] -1] = A[i]
    count[A[i][1]] -=1
  for i in range(n):
    A[-i-1] = B[i]


def prettySort(A):
  preprocessArr(A)
  sortByMulti(A)
  sortBySingle(A)
  print(A)


T=[11,567788,2344,557]
prettySort(T)


