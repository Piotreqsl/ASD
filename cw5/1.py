## problem plecakowy w czasie wielomianywm wzgledem l. przedmiotów i profitów
## najwazniejsze jest znalezienie funkcji rekurencyjnej !!!
## arguementem funkcji rekurencyjnej bedzie nie waga, a profit
## f(T,n,w) - funckja ktora przyjmuje zbior elemtentow ktore mozemy ukrasc, ile pierwszych bierzemy i max wage
## f = max(T[n].value + f(T,n-1, w - T[n].W), f(T;n-1;w)) lub 0 gdy n<=0, w <=0


weigths = [1,2,3,4,5]
profits = [1,4,6,8,9]

def f1(n,w,results):
    global weigths
    global profits
    if(n <=0  or w <= 0):
        return 0
    if(results[n][w] == 0):
        results[n][w] = max(profits[n-1] + f1(n-1, w-weigths[n-1],results), f1(n-1,w,results))
    return results[n][w]


def f(n,w):
    results = [[0 for i in range(w+1)] for j in range(n+1)]
    f1(n,w,results)
    print(results[n][w])


def knapsack(n,w):
    global weigths
    global profits

    if (n<= 0 or w <= 0):
        return 0
    return max(knapsack(n-1, w), knapsack(n-1, w - weigths[n-1])+ profits[n-1])


print(knapsack(5,9))
