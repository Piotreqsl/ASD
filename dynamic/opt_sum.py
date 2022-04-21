
from opt_sum_testy import runtests

def opt_sum(T):
    def MinAbsVal(a,b):
        if abs(a) < abs(b) : 
            return a
        else:
            return b

    def MaxAbsVal(a,b):
        if abs(a) > abs(b) : 
            return a
        else:
            return b

    n = len(T)
    addedSums = [0] * (n + 1)

    #dodajemy do obecnej wartosci wartosc wszystkich poprzednich
    for i in range(1,n + 1):
        addedSums[i] = addedSums[i - 1] + T[i - 1]

    DP = [[0 for _ in range(n)] for _ in range(n)]
    # w DP[i][j] zapamiętujemy wartość sumy tymczasowej, której wartość bezwzględna
    # na danym przedziale jest minimalna (z maksymalnych)

    # rozważamy coraz dłuższe przedziały
    for length in  range(1,n):
        for start in range(n - length):
            end = start + length
            DP[start][end] = addedSums[end + 1] - addedSums[start]
            # dla każdego przedziału sprawdzamy, które 2 podprzedziały najlepiej
            # dodać do siebie (tak, by max suma tymczasowa była jak najmniejsza)
            # k jest "punktem podziału", bierzemy przedziały [start,k] oraz [k+1,end]
            best = float("inf")  
            for podzial in range(start,end):
                best = MinAbsVal(MaxAbsVal(DP[start][podzial], DP[podzial+1][end]), best)

            # do DP wpisujemy wartość z najlepszego podziału lub sumę całego przedziału,
            # jeśli jej wartość bezwzględna jest większa

            DP[start][end]= MaxAbsVal(best,DP[start][end])
    
    return abs(DP[0][n-1])

runtests(opt_sum)