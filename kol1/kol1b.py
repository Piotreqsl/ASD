from kol1btesty import runtests


def countingSort(A,idx,maxlen):
    n = len(A)
    count = [0] * (maxlen)
    output = [0] * n

    for i in range(n):
        count[A[i][idx]] +=1
    
    for i in range(1,maxlen):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        output[count[A[i][idx]] -1] = A[i]
        count[A[i][idx]] -=1
    
    for i in range(n):
        A[i] = output[i]


def radixSort(A,maxlen):
    for i in range(25,-1,-1):
        countingSort(A,i,maxlen)



def createTab(S):
    tab = [0 for i in range(26)]
    for i in range(len(S)):
        tab[ord(S[i])-97] +=1
    return tab

def f(T):
    ## zamiast napisów tworzę sygnatury czyli tab,ice 26 literowe
    n = len(T)
    max_len = 0
    for i in range(n):
        max_len = max(max_len, len(T[i]))
        T[i] = createTab(T[i])
       
 
    radixSort(T,max_len)
    #print(T)

    cur = 1
    best = 0
    for i in range(1,len(T)):
        if (T[i] == T[i-1]):
            cur+=1
        else:
            best = max(best, cur)
            cur = 1

    return max(best,cur)
  
    ## teraz sortuje te tablice pozycyjnie radix sortem


    return 0


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
