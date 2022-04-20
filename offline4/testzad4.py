from zad4testy import runtests


def people(h, a, b):
    return h * (b - a)


# liczy dla kazdego budynku jaki inny moze byc bezposrednio przed nim
# wybiera ten najblizszy
def previous(A):
    n = len(A)
    p = [None] * n

    for i in range(n):
        for j in range(i):

            if A[j][2] < A[i][1]:
                if p[i] == None or A[j][1] > A[p[i]][1]:
                    p[i] = j
    return p


def selectBuildings(A, p):
    n = len(A)

    for i in range(n):
        new = []
        for j in range(4):
            new.append(A[i][j])
        new.append(i)
        A[i] = new

    A.sort(key=lambda x: x[1])
    prev = previous(A)

    # jaka max ilosc osob zmiesci sie w budynkach do idx i włącznie mając budżet p
    # gdy budynki na siebie nie nachodzą
    dp = [[0] * (p + 1) for _ in range(n)]

    for i in range(A[0][3], p + 1):
        dp[0][i] = people(A[0][0], A[0][1], A[0][2])

    for i in range(1, n):  # idx budynku
        for price in range(1, p + 1):  # aktualna cena
            h, a, b, w, idx = A[i]

            if price < w:
                dp[i][price] = dp[i - 1][price]

            else:
                if prev[i] is not None:
                    dp[i][price] = max(dp[i - 1][price], dp[prev[i]][price - w] + people(h, a, b))
                else:
                    dp[i][price] = max(dp[i - 1][price], people(h, a, b))

    bestCol = 0
    for i in range(p, -1, -1):
        if dp[n - 1][i] >= dp[n - 1][bestCol]:
            bestCol = i

    def getSolution(i, price):
        if i < 0:
            return []
        elif i == 0:
            if A[0][3] <= price:
                return [A[0][4]]
            else:
                return []
        else:
            if dp[i][price] == dp[i - 1][price]:
                return getSolution(i - 1, price)
            else:
                return getSolution(i - 1, price - A[i][3]) + [A[i][4]]

    return sorted(getSolution(n - 1, bestCol)), dp[n - 1][price]


runtests(selectBuildings)