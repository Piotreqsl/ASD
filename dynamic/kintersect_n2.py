'''Zbior przedzialow A
wyznacz k przedziałów, ktorych przeciecie jest jak najdluzszym przedziałem
Zwroc liste numerow przedziałow ktore nalezą do rozw
A = [[0,4], [1,10], [6,7], [2,8]]
k = 3
wynik:
[0,1,3]
co daje przedział o przecięciu [2,4]

'''

def printTwoDim(n):
    for i in range(len(n)):
        print(n[i])


from kintersect_tests import runtests

def kintersect(A, k):
    n = len(A)
    T = [(i, A[i][0], A[i][1]) for i in range(n)]
    T.sort(key=lambda x: x[2], reverse=True)
    res = []
    max_l = float("-inf")

    if k == 1:
        res1 = [None]
        for i in range(n):
            if T[i][2] - T[i][1] > max_l:
                max_l = T[i][2] - T[i][1]
                res1[0] = T[i][0]
        return res1

    for i in range(n):
        tmp = []
        tmp.append(T[i][0])
        for j in range(n):
            if j == i:
                continue
            if T[j][1] <= T[i][1] and T[i][1] < T[j][2]:
                tmp.append(T[j][0])
                if len(tmp) == k:
                    r = min(T[j][2], T[i][2])
                    l = r - T[i][1]
                    if l > max_l:
                        max_l = l
                        res = []
                        for a in range(k):
                            res.append(tmp[a])
                    break

    return res

## kintersect recursively
## f(i,k) = najwieksze przeciecie k przedziałów, kiedy rozpatrujemy i+1 pierwszych z tablicy oraz A[i] jest brany pod uwagę

def CountIntersect(i1,i2):
    if(i1[1] <= i2[0] or i1[0] >= i2[1] or i1 == (0,0) or i2 == (0,0)):
        return (0,0)
    else:
       return (max(i1[0],i2[0]), min(i1[1],i2[1]))



def f(A,i,k,F, P):
   
    if(k == 1):
        F[i][k] = A[i]
        return F[i][k]
    if(i+1 < k):
        F[i][k] = (0,0)
        return F[i][k]
    if(F[i][k] is not None):
        return F[i][k]
    best = -1
    best_intersect = (0,0)
    best_parent = None
    for prev_i in range(i):
        prev = f(A,prev_i,k-1,F, P)
        
        new_Intersect = CountIntersect(A[i], prev)
        #print("counting intersect for", best_intersect, prev, "counted is,", new_Intersect) 
        if(new_Intersect[1] - new_Intersect[0] > best):
            best = new_Intersect[1] - new_Intersect[0]
            best_intersect = new_Intersect
            best_parent = prev_i

    P[i][k] = best_parent
    F[i][k] = best_intersect
    return F[i][k]


def getSol(P,i, k):
    if(P[i][k] != None):
        return getSol(P, P[i][k], k-1) + [i]
    else:
        return [i]

def ki(A,k):
    n = len(A)
    ##A.sort(key= lambda x: x[0], reverse= False)
    F = [[None for i in range(k+1)] for j in range(n)]
    P = [[None for i in range(k+1)] for j in range(n)]
    for j in range(n-1, -1, -1):
        _ = f(A,j,k,F, P)
    #printTwoDim(F)
    #print(A)

    best = -1
    best_intersect = (0,0)
    best_i = -1
    for i in range(n):
        rozpatrywany = F[i][k]
        if(rozpatrywany[1] - rozpatrywany[0] > best):
            best = rozpatrywany[1] - rozpatrywany[0]
            best_i = i
            best_intersect = rozpatrywany
   
    sol = getSol(P,best_i,k)
    #print("ROZW TO",best, "przy k=", k, "lensol = ", len(sol))

    return sol

    
A = [(0,4), (1,10), (6,7), (2,8)]

print(ki(A,3))
       
####

    



runtests(ki)