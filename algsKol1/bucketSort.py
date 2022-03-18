## Kiedy mamy równomierny rozkład liczb np z zakresu [0,1] czyli floaty
## to wtedy warto uzyc bucketa, counting nam nie zadziała,
## bo bierzemy indexy na podstawie liczb (intow), a tu mamy floaty

# kazdy bucket mozemy se juz posortowac insertem ;)

def insertionSort(b):
    for i in range(1, len(b)):
        selected = b[i]
        j = i-1
        while(j >= 0 and b[j] > selected):
            b[j + 1] = b[j]
            j -=1
        b[j+1] = selected

def bucketSort(A):
    arr = []
    buckets_num = 10 # kazde wiadro na przeział 0-0.1, 0.1-0.2 itp
    for i in range(buckets_num):
        arr.append([])
    for j in A:
        index = int(j * buckets_num)
        arr[index].append(j)
    for i in range(buckets_num):
        insertionSort(arr[i])
    k = 0
    for i in range(buckets_num):
        for j in range(len(arr[i])):
            A[k] = arr[i][j]
            k +=1
    
A = [0.01, 0.3, 0.05, 0.8, 0.48]
bucketSort(A)
print(A)