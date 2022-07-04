


def rozwalka(T,L):
    if T is not None:
        rozwalka(T.left, L)
        L.append(T)
        rozwalka(T.right, L)



def ConvertTree(p):
    L = []
    rozwalka(p,L)
    n = len(L)

    for i in range(n):
        if ((2*i) + 1) < n:
            L[i].left = L[(2*i) +1]
            if( (2*i) +2 <n):
                L[i].right = L[(2*i) +2]
            else:
                L[i].right = None
        else:
            L[i].left = None
            L[i].right = None

        if((i-1) //2) >=0:
            L[i].parent = L[(i-1) //2]
        else:
            L[i].parent =None
    return L[0]