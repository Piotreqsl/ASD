weigths = [1,2,3,4,5]
profits = [1,4,2,4,3]

def f1(n,b,results):
    global weigths
    global profits

    if(results[n][b] != 0):
        return results[n][b]
    

    if(n == 1):
        if(weigths[0] <= b):
            results[n][b] = profits[0]
        else:
            results[n][b] = 0
        return results[n][b]
    
    exclusion = f1(n-1,b,results)

    if(weigths[n-1] > b):
        results[n][b] = exclusion
        return results[n][b]

    inclusion = f1(n-1, b-weigths[n-1] , results) + profits[n-1]

    results[n][b] = max(exclusion,inclusion)
    return results[n][b]


def printTwoDim(a):
    for i in range(len(a)):
        print(a[i])

def knapsack(n,b):
    results = [[0 for i in range(b+1)] for j in range(n+1)]
    print(f1(n,b,results))
    printTwoDim(results)

knapsack(5,10)

