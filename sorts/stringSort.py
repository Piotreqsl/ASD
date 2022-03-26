## stringi sortuję bucketem po długości a każdego bucketa radixem

def countingSort(bucket,char):
    cnt = [0] * 26
    output = [0] * len(bucket)

    for i in range(len(bucket)):
        index = ord(bucket[i][char]) - ord('a')
        cnt[index] +=1
    for i in range(1, 26):
        cnt[i] += cnt[i-1]

    for i in range(len(bucket) -1, -1, -1):
        index = ord(bucket[i][char]) - ord('a')
        output[cnt[index] -1] = bucket[i]
        cnt[index] -=1
    for i in range(len(bucket)):
        bucket[i] = output[i]

def radixSort(Bucket, str_len):

    for i in range(str_len-1, -1,-1):
        countingSort(Bucket,i)

def min_max(A, n):
  _min = _max = len(A[0])

  for i in range(1, n-1, 2):
    if len(A[i]) < len(A[i+1]):
      curr_min = len(A[i])
      curr_max = len(A[i+1])
    else:
      curr_max = len(A[i])
      curr_min = len(A[i+1])

    if curr_min < _min: _min = curr_min
    if curr_max > _max: _max = curr_max

  if n%2 == 0:
    if len(A[-1]) < _min:
      _min = len(A[-1])
    elif len(A[-1]) > _max:
      _max = len(A[-1])

  return (_min, _max)


def stringSort(A):
    n = len(A)
    minlen, maxlen = min_max(A,n)
    buckets_no = maxlen - minlen + 1
    buckets = [[] for i in range(buckets_no)]

    for i in range(n):
        buckets[len(A[i]) - minlen].append(A[i])
    for i in range(buckets_no):
        if(len(buckets[i]) > 0):
            radixSort(buckets[i], len(buckets[i][0]))
    index = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            A[index] = buckets[i][j]
            index +=1

A = ['mama', 'mamt', 'ala', 'ma', 'kota', 'tesdt', 'fiuut', 'z', 'adsf']
stringSort(A)
print(A)