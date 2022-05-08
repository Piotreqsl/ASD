from zad10ktesty import runtests
import math

## to mi sie chyba wydaje że zachłanny skoro są to kwadraty, muszę zacząć od
## najwiekszego dostępnego a potem zmniejszać odp

## jednak nie zachłanny z pierwiastkiem bo kontrargumentem będzie takie 32 - mogę wziąć 2 x 16 (bok 4)
## a algorytm z pierwiastkiem mi zwroci 5 2 1 1 1

def dywany ( N ):
    dp = [float("inf") for i in range(N+1)]
    parents = [None for i in range(N+1)]
    dp[0] = 0
    for i in range(1, N+1):
        best = float("inf")
        j = 1
        while(i - j*j >= 0):
            if(dp[i-j*j] +1 < best):
                best = dp[i-j*j] +1
                parents[i] = j
    
            j+=1
        dp[i] = best

    
    res = []
    pointer = N
    while(parents[pointer] != None):
        res.append(parents[pointer])
        pointer -= (parents[pointer] * parents[pointer])

    return res


runtests( dywany )

