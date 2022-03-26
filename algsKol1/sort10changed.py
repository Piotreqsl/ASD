


def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key


def countingSort(A,k):
    n = len(A)
    output = [0] * n
    count = [0] *(k+1)
    for i in range(n):
        count[A[i]] +=1
    for i in range(1,k+1):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        output[count[A[i]] -1] = A[i]
        count[A[i]] -=1
    for i in range(n):
        A[i] = output[i]



def shiftTab(A,count):
    for i in range(len(A)-count-1, -1, -1):
        A[i+count] = A[i]
        




def sort_with_10_changed(A,k):
    changed = [0]*10
    n = len(A)
    index = 0
    for i in range(n):
        if A[i] < 0 or A[i] > k:
            changed[index] = A[i]
            index+=1
            A[i] = k
    countingSort(A,k)
    insertion_sort(changed)

    negativeCount = 0

    for i in range(10):
        if(changed[i] < 0):
            negativeCount +=1
        else:
            break
    shiftTab(A,negativeCount)
    for i in range(negativeCount): # O(k)
        A[i] = changed[i]
    for i in range(negativeCount, 10):
        A[n-(10-i)] = changed[i]
    

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, -100, 25, 14, -1, -20, 99, 67, 19, 23]

sort_with_10_changed(A,9)
print(A)


