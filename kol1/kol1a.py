from kol1atesty import runtests


def countingSort(A,idx):
    n = len(A)
    output = [0] *n
    count = [0] *26

    for i in range(n):
        count[ord(A[i][idx])-97] +=1
    for i in range(1,26):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        output[count[ord(A[i][idx])-97] -1] = A[i]
        count[ord(A[i][idx])-97] -=1
    for i in range(n):
        A[i] = output[i]


def radixSort(A,l):
    for i in range(l-1, -1,-1):
        countingSort(A,i)


B =["pies", "creo", "crep"]



def g(T):
    # tu prosze wpisac wlasna implementacje
    ## wpierw normalizuję czyli porównuję noramlny napis z odwróconym i wybieram ten mniejszy
    n = len(T)
    min_len = 100000
    max_len = 0
    for i in range(n):
        min_len = min(len(T[i]), min_len)
        max_len = max(len(T[i]), max_len)
        S = T[i]
        rev = S[::-1]
        if(S > rev):
            T[i] = rev
    
    no_of_buckets = max_len - min_len +1
    buckets = [[] for i in range(no_of_buckets)]
    for i in range(n):
        buckets[len(T[i]) - min_len].append(T[i])
    
    for i in range(len(buckets)):
        if(len(buckets[i]) == 0):
            continue
        radixSort(buckets[i], len(buckets[i][0]))
        
    max_popularity = 0

    for bucket in buckets:
        cur_pop = 1
        for i in range(1,len(bucket)):
            if(bucket[i] == bucket[i-1]):
                cur_pop +=1
            else:
                max_popularity = max(max_popularity, cur_pop)
                cur_pop = 1
        max_popularity = max(max_popularity, cur_pop)

    return max_popularity


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
