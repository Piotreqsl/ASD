


from cv2 import circle


def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        selected = A[i]
        j = i-1
        while(j >=0 and A[j][1] > selected[1]):
            A[j+1] = A[j]
            j-=1
        A[j+1] = selected


def min_max(A):
  _min = _max = A[0][1]
  n = len(A)

  for i in range(1, n-1, 2):
    if A[i][1] < A[i+1][1]:
      curr_min = A[i][1]
      curr_max = A[i+1][1]
    else:
      curr_max = A[i][1]
      curr_min = A[i+1][1]

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if A[-1][1] < _min:
      _min = A[-1][1]
    elif A[-1][1] > _max:
      _max = A[-1][1]

  return (_min, _max)

def findBucket(dist,n,minel,maxel):
    i = int((dist-minel)/(maxel-minel)*n)
    if(i == n):
        return i-1
    return i

def restoreArr(A):
    for i in range(len(A)):
        A[i] = A[i][0]

def bucketSort(A, n, _min, _max):
    buckets = [[] for i in range(n)]
    for i in range(n):
        buckets[findBucket(A[i][1],n,_min,_max)].append(A[i])
    for i in range(n):
        insertionSort(buckets[i])
    index = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            A[index] = buckets[i][j]
            index +=1 



def sortCircle(A):
    n = len(A)
    for i in range(n):
        A[i] = (A[i], (A[i][0]**2+A[i][1]**2)**1/2)
    minel, maxel = min_max(A)
    bucketSort(A,n,minel,maxel)
    restoreArr(A)

A = [(1, 1), (0, 0), (-1, -1), (4, 4), (-3, -100)]
sortCircle(A)
print(A)