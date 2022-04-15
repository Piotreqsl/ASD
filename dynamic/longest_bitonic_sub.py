'''
Dana jest tablica, mamy znaleźć najdłuższy podciąg (niekoniecznie spójny), 
którego elementy są najpierw posortowane rosnąco, a następnie malejąco, np.
[4,2,5,7,6,9,1] -> [2,5,7,9,1]
'''

''' 
Tworzymy dwie pomocnicze tablice - jedna przechowująca pod indeksem i najdłuższy podciąg 
rosnący kończący się w arr[i] oraz druga, przechowująca najdłuższy podciąg zaczynający się w arr[i].
Następnie sprawdzamy dla każego indeksu wartość sumy inc[i] + dec[i] - 1 oraz wybieramy największą z nich.
Jest to długość szukanego podciągu.
'''

def longest(arr):
    n = len(arr)
    inc = [1]*n
    parent_inc=[-1]*n
    dec = [1]*n
    parent_dec = [-1]*n

    for i in range(1,n):
        for j in range(i):
            if(arr[i] > arr[j] and 1+inc[j] > inc[j]):
                inc[i] =  1+inc[j]
                parent_inc[i] = j

    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if(arr[j]<arr[i] and 1+dec[j] > dec[i]):
                dec[i] =  1+dec[j]
                parent_dec[i] = j
    
    
    longest = float("-inf")
    longest_i=1



    for i in range(n) :
        if(inc[i] + dec[i] - 1 >= longest):
            longest = inc[i] + dec[i] - 1
            longest_i = i

    res_inc = []
    
    cur_i = longest_i
    while(cur_i != -1):
        res_inc.append(arr[cur_i])
        cur_i = parent_inc[cur_i]
    


    res_dec = []
    cur_i = longest_i
    while(cur_i != -1):
        res_dec.append(arr[cur_i])
        cur_i = parent_dec[cur_i]

    print(res_inc[::-1], res_dec)
    return longest

print(longest([4,2,5,7,6,9,1]))