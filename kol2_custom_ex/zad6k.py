
from zad6ktesty import runtests 

def haslo ( S ):

    n = len(S)
    F = [0 for i in range(n)]
    F[0] =1


    integersingle = int(S[1])
    if(integersingle != 0):
        F[1] =  F[0]
    integerDouble = int(S[1-1:2])

    if(0 < integerDouble < 27):
        F[1] +=1

    for i in range(2,n):
        integersingle = int(S[i])
        if(integersingle != 0):
            F[i] =  F[i-1] 
        integerDouble = int(S[i-1:i+1])
        if(integerDouble == 0):
            return 0
        if(S[i-1] == '0'):
            continue
        if(integerDouble < 27 ):
            F[i] = F[i] +  F[i-2]
            

    return F[n-1]

runtests ( haslo )