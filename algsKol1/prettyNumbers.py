


def ctSort(tab, single):
    n = len(tab)
    output = [0] * n
    cnt = [0] *10

    if(single):
        for i in range(n):
            cnt[tab[i][1]] +=1
        for i in range(1, 10):
            cnt[i] += cnt[i-1]
        for i in range(n-1,-1,-1):
            output[cnt[tab[i][1]] -1] = tab[i]
            cnt[tab[i][1]] -=1
    else:
        for i in range(n):
            cnt[tab[i][2]] +=1
        for i in range(1, 10):
            cnt[i] += cnt[i-1]
        for i in range(n-1,-1,-1):
            output[cnt[tab[i][2]] -1] = tab[i]
            cnt[tab[i][2]] -=1
    return output

    


def prettySort(T):
    for i in range(len(T)):
        liczba = T[i]
        digits = [0]*10
        copy = liczba
        while(copy >0):
            digits[copy%10] +=1
            copy //= 10
        j = w = 0
        for index in range(10):
            if(digits[index] == 1):
                j +=1
            if(digits[index] > 1):
                w += 1
        T[i] = (liczba,j,w)
    new = ctSort(T,False)
    new = ctSort(T, True)


    for i in range(len(T)):
        T[i] = new[i]


T=[11,567788,2344,557]
prettySort(T)
print(T)
