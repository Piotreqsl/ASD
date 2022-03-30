def partiton(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1

A = [3, 8, 6, 4, 5, 9, 2]


def select(A, p, r,k):
    if(p == r):
        return A[p]
    else:
        q = partiton(A,p,r)
        if( q == k):
            return A[k]
        elif (q < k):
            return select(A, q+1, r, k)
        else:
            return select(A, p, q-1, k)


def Median(T):
    n = len(T)

    linearT =[]
    for el in T:
        for el2 in el:
            linearT.append(el2)

    low_index = ((n**2)-n) //2
    high_index = (((n**2)-n) //2) + n -1


    low_val = select(linearT,0,len(linearT)-1, low_index)
    high_val = select(linearT,0,len(linearT)-1, high_index)

    ## no i teraz powpisywać se do tablicy odpowiednio
    print(low_val, high_val)

T = [ [2,3,5], [7,11,13], [17,19,23]]
Median(T)