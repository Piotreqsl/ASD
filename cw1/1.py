#dana jest tablica 0/1/2/3....
# z wartosciami z zakresu 0 do m > n (n rozmiar tablicy)
#znajdz najmniejszą wartość ktorej nie ma w tej tablicy

#ind 0 1 2 3 4 5 6 7 8
#tab 0 1 2 3 5 7 11 13 17


#złoznosc log n


def findMin(tab):
    n = len(tab)


    low = 0
    high = n -1
    mid = 0
    while(low <= high):
        mid = (low + high) //2

        if(tab[mid] != mid):
            high = mid - 1
        
        else:
            if(tab[mid] ==0 and tab[mid+1] != mid+1):
                return mid+1
            else:
                low = mid + 1
    
    return -1

##
def rozwgarka(T):
    l = 0
    p = len(T) -1
    while l <= p:
        s = (l+p) //2
        if(T[s] == s):
            l = s +1
        else:
            p = s -1
    return l
print(rozwgarka([0,1,2,3,4,6,7,8]))

