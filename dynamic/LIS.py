#Problem:
#	Dana jest tablica liczb, np. A=[2,-1,3,-2,5,7,11,1,2,13], indeksowana od 0 do n-1. 
#   Rozwiązaniem problemu jest długość najdłuższego podciągu rosnącego w tej tablicy. 
#   W tym przypadku jest to 6.
#
#Rozwiązanie:
#	Funkcję rekurencyjna opisująca problem:
#		f(k) - długość najdłuższego podciągu rosnącego kończącego się na A[k]
#				{ 1 	dla k=0
#		f(k) =	{
#				{ max { f(t)+1 : t < k && A[t] < A[k] }


def LIS(A): ## O(N^2)
    n = len(A)
    F = [1] * n
    maxi = 0

    for i in range(1,n):
        for j in range(i):
            if(A[i] > A[j] and F[j] + 1 > F[i]):
                F[i] = F[j] +1
        if F[i] > F[maxi]:
            maxi = i
    return F[maxi]




### Podejscie nlogn 

##bin search
def CeilIndex(A, l, r, key):
 
    while (r -l > 1):
     
        m = l + (r - l)//2
        if (A[m] == key):
            return m
        elif(A[m] > key):
            r = m
        else:
            l = m
    return l

def LISv2(A):
    n = len(A)
    lasts = [0 for i in range(n+1)]
    lasts[0] = A[0]
    length=1
    for i in range(1,n):

        if(A[i]< lasts[0]):
            lasts[0] = A[i]
            ## nowa najmniejsza wartość
        elif(A[i] > lasts[length-1]):
            ## A[i] chce rozszerzyć podciąg
            lasts[length] = A[i]
            length +=1
        else:
            lasts[CeilIndex(lasts,0,length-1,A[i])] = A[i]
    return length

print(LISv2([2,-1,3,-2,5,7,11,1,2,13]))



