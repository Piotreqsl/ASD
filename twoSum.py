## czy w tablicy istneieje suma 
## jeżdzę sobie dwoma wskaźnikami

def findSum(tab, x):
    n = len(tab)
    i = 0
    j = n-1
    
    while(i < j):
        if(tab[i] + tab[j] < x):
            i += 1
        elif(tab[i] + tab[j] > x):
            j -= 1
        else:
            print("Suma znaleziona", tab[i], "+", tab[j])
            break
    print("Suma nieznaleziona")

findSum([2,4,6,7,8], 15)
        