'''
    Dane są trzy zbiory: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka a, b, c 
    z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!
'''
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if(A[j]<= x):
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def qs(A,p,r):
    if(p<r):
        pivot = partition(A,p,r)
        qs(A,p,pivot-1)
        qs(A,pivot+1,r)


def sums(A,B,C):
    qs(A,0,len(A)-1)
    qs(B,0,len(B)-1)

    for num in C:
        a = 0
        b= len(B)-1
        while(a< len(A) and b>=0):
            if(A[a]+B[b] <num):
                a+=1
            elif(A[a]+B[b] >num):
                b-=1
            else:
                return True
    return False



A=[3,4,6,8,4,2]
B=[5,8,9,15]
C=[1,2,3,4,5,3]
sums(A, B, C)
print(sums(A,B,C))
