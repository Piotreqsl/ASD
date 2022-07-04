### proste rozwiązanie - dla każdego punktu
## odpalamy kolejną pętle i sprawdzamy czy nie jest on dominowany 
# przez żaden inny

points =[(0,1), (3,4), (8,7), (3,7)]


def count(A):
    count = 0
    n = len(A)
    for i in range(n):
        found_dominator = 0
        for j in range(n):
            if i == j:
                continue
            if(A[j][0] > A[i][0] and A[j][1] > A[i][1]):
                found_dominator =1
                break
        if found_dominator ==0:
            print(points[i])
            count +=1
    return count

print(count(points))

## drugie rozwiazanie sortujemy najpierw po X, a jeśli równe to po y ( w kolejności malejącej)



def partition(A,p,r):
    i = p-1
    for j in range(p,r):
        if(A[j][0] >= A[r][0]):
            if(A[j][0] == A[r][0]):
                if(A[j][1] < A[r][1]):
                    continue
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def optimalQS(A, p, r):
    while(p< r):
        q = partition(A, p, r)
        if(q-p <= r-q):
            optimalQS(A,p,q-1)
            p = q+1
        else:
            optimalQS(A,q+1,r)
            r = q-1


def count_dom_points(points):
    optimalQS(points,0,len(points)-1)
    print(points)
    T = points[0]
    count = 1
    n = len(points)
    print(T)
    for i in range(1,n):
        if(T[0]> points[i][0] and T[1] > points[i][1]):
            continue
        else:
            count+=1
            T = points[i]
    return count

print(count_dom_points(points))