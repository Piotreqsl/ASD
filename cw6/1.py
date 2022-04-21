# wycinanie co drugiego drzewa pozdr
#
# f(i) - max zysk do itego drzewa wlacznie
'''funkcja z cwików
def Las(C,n):
    T=[-1 for i in range n]



'''





from re import I


def printSol(F,c,profit):
    n = len(c)
    res = []
    ## kandytatem jest pierwszy z różną wartością w F[i], jakieś zmiany tam zachodziłu
    i = n-1
    while i > 0 and F[i] == F[i-1]:
        i-=1
    res.append(c[i]) # ten brzegowy

    while i >= 0: 
        j = i

        ## znajdujemy tego z odp c[i], wiemy że tego wzieliśmy
        while j >=0 and F[j] + c[i] != F[i]:
            j-=1
        if j < 0:
            break
        # pomijamy tych o tej samej wartosci w F co kandydat,
        # szukany bedzie pierwszym z ta wartoscia
        while j > 0 and F[j] == F[j-1]:
            j -= 1
        res.append(c[j])
        i=j
    for i in range(len(res)-1,-1,-1):
        print(res[i], end=' ')




def blackForest(c):
    n = len(c)
    if (n ==1):
        return c[0]
    # F[i] - max zysk do i-tego drzewa wlacznie
    F = [0]*n

    F[0] = c[0]
    F[1] = max(c[1], F[0])

    for i in range(2,n):
        F[i] = max(F[i-1], F[i-2] +c[i])

    return(F[-1], F)

c = [56, 2, 14, 3, 1, 91]

profit, F = blackForest(c)
printSol(F, c, profit)

