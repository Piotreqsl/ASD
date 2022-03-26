## tablica zawierająca n parami róznych liczb
## algorytm który znajduje 2 takie liczby x,y takie zeby y-x = max, oraz żeby były sąsiednie

def maxspan(A):
    n = len(A)
    min_ = min(A)
    max_ = max(A)

    B = [[] for i in range(n)]
    x = (max_ - min_) //n

    for i in range(n):
        d = (A[i] -min_)//x
        B[d].append(A[i])
    
    result = 0
    prev_max = max(B[0])
    for i in range(1,n):
        if(len(B[i]) !=0):
            act_min = min(B[i])
            result = max(result, act_min - prev_max)
            prev_max =max(B[i])
    return result

A=[3,4,9,10]
maxspan(A)
print(A)

## algorytm obalony na CWICZENIACH LOLIX

