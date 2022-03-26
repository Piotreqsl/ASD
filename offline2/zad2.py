# Piotr Śliperski

# Tworzę nowe tablice start i end, gdzie będe przechowywał posortowane początki i konce przedziałow, zeby rozroznic ktory poczatek nalezy do ktorego konca
# stosuje drugie pole index (index jest z kolejnosci wejsciowej). Tablice start i end sortuję Quicksortem wg pierwszej pozycji.
# Następnie tworze tablice z indexami, ktore beda odpowiadały początkom i koncom przedziałow. We finalnej pętli iteruję sie po całej tablicy po raz ostatni, aby
# uzyskać liczbę przedziałów z mniejszym lub równym końcem oraz z mniejszym lub równym początkiem, odejmując te dwie wartości dostaję liczbę przedziałow zawierajacych się
# w konkretnym przedziale.
#
# Złożonośc to złozonosc sortowania + iteracji po posortowanej O(n) + 0(nlogn)

from zad2testy import runtests
def partition(T, low, high):

    pivot = T[high][0]
    i = low - 1
    for j in range(low, high):
        if T[j][0] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[high] = T[high], T[i + 1]
    return i + 1


def quicksort(T, low, high):


    while low < high:
        q = partition(T, low, high)
        if(q-low <= high-q):
          quicksort(T,low, q-1)
          low = q +1
        else:
          quicksort(T, q+1, high)
          high = q-1



def depth(L):
  n = len(L)
  start = [0] * n
  end = [0] * n
  start_indexes = [0] * n
  end_indexes = [0] * n
  for i in range(n):
    start[i] = [L[i][0], i]
    end[i] = [L[i][1], i]

    
  quicksort(start,0,n-1)
  quicksort(end,0,n-1)

#

  #printmy(start)

  for i in range(n):
    start_indexes[start[i][1]] = i
    end_indexes[end[i][1]] = i
  #print(start_indexes)
  
  max = -1
  for i in range(n):
        bottom = start_indexes[i]
        while bottom > 0 and start[bottom - 1][0] == start[bottom][0]:
            bottom -= 1

        top = end_indexes[i]
        while top < n - 1 and end[top + 1][0] == end[top][0]:
            top += 1

        res = top - bottom
        if res > max:
            max = res



  return max



runtests( depth ) 