from cProfile import run
from opt_sum_testy import runtests

def my_pref_sum(low,high,prefs):
    if low == 0:
        return prefs[high]
    return prefs[high] - prefs[low-1]


def my_sol(T):
    n = len(T)
    prefs = [0 for i in range(n)]
    prefs[0] = T[0]
    
    for i in range(1,n):
        prefs[i] = T[i] + prefs[i-1]

    F =[[float("-inf") for i in range(n)] for i in range(n)] ## najwieksza wartość sumując od i do j
    for i in range(1,n):
        F[i-1][i] = abs(my_pref_sum(i-1,i ,prefs))

    for j in range(2,n):
        for i in range(j-1,-1,-1):
            F[i][j] = max(abs(my_pref_sum( i,j, prefs)), min(F[i][j-1], F[i+1][j]))## albo sumuje te na pozycji i-j
                    ## albo jako sume czesciową biorę cały wynik, w sensie finalny po dodaniu
                    ## albo mniejszy ze sumowania od i do j-1, albo od i+1 do j
                    ## no i tu rozstrzygam czy bardziej warto dodać wpierw element na pozycji itej
                    ## czy element na pozycji jotej
    return F[0][n-1] ## najwieksza wartośc sumując od 0 do n-1

runtests(my_sol)