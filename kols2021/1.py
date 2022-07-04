
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if(A[j] <= x):
            i+=1
            A[i], A[j] = A[j], A[i]
    
    A[r], A[i+1] = A[i+1], A[r]
    return i+1


def quickSelect(A,p,r,k):
    if(p == r):
        return A[p]
    else:
        q = partition(A,p,r)
        if(q == k):
            return A[q]
        elif(q < k):
            return quickSelect(A, q+1,r,k)
        else:
            return quickSelect(A,p,q-1,k)

def print2(T):
    for el in T:
        print(el)

def Median(T):
    n = len(T)
    print2(T)

    linearT =[]
    for el in T:
        for el2 in el:
            linearT.append(el2)
    
    low_index = ((n**2)-n) //2
    high_index = (((n**2)-n) //2) + n -1


    low_val = quickSelect(linearT,0,len(linearT)-1, low_index)
    high_val = quickSelect(linearT,0,len(linearT)-1, high_index)


    ## wpisuje do tablicy
    idx = 0
    for col in range(n-1):
        for j in range(col+1,n):
            T[j][col] = linearT[idx]
            idx+=1
    for i in range(n):
        T[i][i] = linearT[idx]
        idx+=1
    
    for col in range(n-1, -1,-1):
        for row in range(col-1,-1,-1):
            T[row][col] = linearT[idx]
            idx+=1
    print("############")
    print2(T)


T = [ [2,3,5,9], [7,11,13,4], [8,17,19,23], [1,6,24,16]]
Median(T)