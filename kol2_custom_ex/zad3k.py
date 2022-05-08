from zad3ktesty import runtests

'''Dla każdego ciągu n liczb możemy obliczyć k-ładną sumę (Zakładamy, że k <= n). Poprzez
k-ładną sumę rozumiemy minimalną sumę pewnych liczb wybranych w ten sposób, że z
każdych k kolejnych elementów wybraliśmy przynajmniej jeden z nich (w szczególności
oznacza to, że dla k=1 musimy wybrać wszystkie elementy, a dla k=n wystarczy wybrać
jeden, najmniejszy z nich). Proszę napisać algorytm, który dla zadanej tablicy liczb
naturalnych oraz wartości k oblicza k-ładną sumę. '''


## ciag sie konczy


def ksuma( T, k ):
    n=len(T)
    if(k == 1):
        return sum(T)
    if k == n:
        return min(T)
    F = [float("inf") for i in range(n)]


    F[0] = T[0]
    for i in range(1,n):
        last_considered_idx = max(0, i-k)
        min_av = float("inf")
        for p in range(last_considered_idx, i):
            min_av = min(min_av, F[p])
        F[i] = T[i] + min_av
        if(i < k):
            F[i] = min(F[i], T[i])


    
    #3print(F)
    result = float("inf")
    for i in range(n-k, n):
        #print(F[i])
        result = min(result, F[i])

        


    #print(F)

    #Tutaj proszę wpisać własną implementację
    return result
    
runtests ( ksuma )