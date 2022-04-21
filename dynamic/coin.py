''' 
Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm,
który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, 
nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5). 
'''

# O(T*ilosc nominalow)

# zakladam ze tablica z nominalami jest posortowana rosnaco - jesli nie, to mozemy posortowac
# zauwazmy, ze f(i)= 1 + min(f(i-nom), nom->dostepne nominaly, nasze rozwiazanie to f(n)


def coindispending( nominals, cost):
    DP = [float('inf') for i in range(cost + 1)]
    DP[0] = 0
    for i in range(1,cost + 1):
        for coin in nominals:
            if i - coin >= 0:
                DP[i] = min(DP[i], DP[i - coin] + 1)
    print(DP)


T = [1,5,8]
coindispending( T, 27 )