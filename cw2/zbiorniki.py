def partition(A,p,r):
    x = A[r][0]
    i = p-1
    for j in range(p,r):
        if(A[j][0] <= x):
            i+=1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1


def quickSort(A, p, r):
    while(p <=r):
        q = partition(A, p, r)
        if(q-p <= r-q):
            quickSort(A,p, q-1)
            p = q +1
        else:
            quickSort(A, q+1, r)
            r=q-1

def zbiorniki(L, wody):
    n = len(L)
    tab = []
    for i in range(n):
        tab.append((L[i][0], 'd'))
        tab.append((L[i][1], 'g'))
    n = len(tab)
    quickSort(tab, 0, n-1)
    filled =0
    cur_pojemnosc = 0
    wlano = 0
    cur_index = 0
    indicator = 0
    while(cur_index < n):
        wlano += cur_pojemnosc
        if(wlano > wody):
            break
        while(cur_index < n and tab[cur_index][0] == indicator):
            if(tab[cur_index][1] == 'd'):
                cur_pojemnosc +=1
            else:
                filled +=1
                cur_pojemnosc -=1
            cur_index +=1
        indicator +=1

    print(filled)


L = [[0,3], [4,8], [2,4], [5,9]]
zbiorniki(L, 12)