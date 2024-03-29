'''
    Proszę zaimplementować funkcję: 
    int count(arr);
    Funkcja ta przyjmuje na wejściu posortowaną tablicę n liczb całkowitych, w której mogą pojawiać się duplikaty.
    Funkcja powinna zliczać ilość wystąpień różnych wartości bezwzględnych elementów występujących w tej tablicy.
    Przykład:
    Wejście: {-1, -1, 0, 0, 1, 1, 1}
    Wyjście: 2
    Wejście: {1, 1, 1}
    Wyjście: 1
'''

# ALGORYTM:
'''
    Wykorzystujemy fakt, że tablica jest posortowana, by uzyskać złożoność liniową względem liczby
    elementów, bez wykorzystania dodatkowej pamięci. Po prostu poruszamy się jednocześnie od początku i końca tablicy
    dwoma indeksami i oraz j, odpowiednio modyfikując liczbę unikatowych wystąpień elementów.
'''


def count(arr):
    i = 0
    j = len(arr)-1
    count=len(arr)
    while(i<j):
        while(i !=j and arr[i] == arr[i+1]):
            i+=1
            count-=1
        while(i!=j and arr[j] == arr[j-1]):
            j-=1
            count -=1
        if(i == j):
            break
        
        suma = arr[i] + arr[j]
        if(suma == 0):
            count -=1
            i+=1
            j-=1
        if(suma <0):
            i+=1
        elif(suma >0):
            j-=1
    return count
arr=[-5,-4,-3,-3,2,3,3,3,5,6]
print(count(arr))