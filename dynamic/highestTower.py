'''dany jest ciag klackow, i wybrac najdluzszy podciag taki ze kazdy zawiera sie w poprzednim'''


def tower(A):
    n = len(A)
    F = [1 for i in range(n)]

    for i in range(1,n):
        for j in range(i):
            if(A[i][0] >= A[j][0] and A[i][1] <= A[j][1]):
                F[i] = max(F[i], F[j] + 1)
                ##print("war spełnione")
    return max(F)

A = [[1,4], [0,5], [1,5], [2,6], [2,4]]
print(tower(A))