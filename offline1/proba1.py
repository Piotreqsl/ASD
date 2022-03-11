# Piotr Śliperski
#
# Moje rozwiązanie składa się z dwóch warunków, jeżeli k=1 to wtedy przystępuję do zwykłego bubble sorta (czyli porównywania każdego elementu ze swoim sąsiadem).
# Takie podejście wymaga przejścia po calej tablicy 1 raz, więc ma złożoność O(n). W przeciwnym wypadku postępuje podobnie jak przy HeapSorcie. Ale tutaj tworzę kopiec
# o długości k+1, gdyż wiem, że każdy element jest oddalony o k. Kopiec jest kopcem minimalnym, zatem najmniejszy element znajduje się na zerowym indexie kopca.
# Następnie iteruję się aż do konca listy, konsekwetnie zdejmując najmniejsze elementy z wierzchołka kopca i dokładając kolejne. Kiedy dojdę już do konca listy
# zostaję z kopcem z kilkoma elementami koncowymi, w tym momencie dokonuje sortowania kopca i posortowanego dokladam na koniec listy wynikowej
# Moje podejście dla k != 1 zapewnia wydajność rzędu n log k

from zad1testy import Node, runtests


def left_child(index):
    return 2*index +1

def right_child(ind):
    return 2*ind + 2

def parent(index):
    return (index-1) //2



def napraw(tab, length, err_ind):
    prawy = right_child(err_ind)
    lewy = left_child(err_ind)
    min_index = err_ind
    if(lewy < length and tab[lewy] < tab[min_index]):
        min_index = lewy
    if(prawy < length and tab[prawy] < tab[min_index]):
        min_index = prawy

    if(min_index != err_ind):
        tab[err_ind], tab[min_index] = tab[min_index], tab[err_ind]
        return napraw(tab, length, min_index)
    else:
        return tab



def buduj_min_kopiec(tab):
    for i in range(parent(len(tab) -1), -1, -1):
        tab = napraw(tab, len(tab), i)
    return tab

def zdejmuj_z_kopca(tab):
    n = len(tab)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        tab = napraw(tab, i, 0)
    return tab





def proba(p,k):
    if(k==1):
        slow = p
        fast = p.next
        while(fast != None):
            if(slow.val > fast.val):
                slow.val, fast.val = fast.val, slow.val
            slow= slow.next
            fast = fast.next
        return p
        

   
    my_heap = [0 for i in range(k+1)]
    

    result = None
    result_end = None
    rozmiar = 1

    ##budowanie kopca z pierwszych k+1 elementów
    for i in range(k+1):
        my_heap[i] = p.val
        if(p.next == None):
            fixed_heap = [0 for i in range(rozmiar)]
            for i in range(rozmiar):
                fixed_heap[i] = my_heap[i]
            my_heap = fixed_heap    
            p = p.next
            break
        else:
            p = p.next
            rozmiar += 1

    
    my_heap = buduj_min_kopiec(my_heap)
    result = None
    result_end = None
    rozmiar_kopca = len(my_heap)

    while(p != None):

        kolejny = Node()
        kolejny.val = my_heap[0]
        if(result == None):
            result = kolejny
            result_end = result
        else:
            result_end.next = kolejny
            result_end = kolejny


        my_heap[0] = p.val
        my_heap = napraw(my_heap, rozmiar_kopca, 0)

    
        p = p.next
  
    
        


    left_to_remove = zdejmuj_z_kopca(my_heap)
    for i in range(len(left_to_remove) -1, -1, -1):
        kolejny = Node()
        kolejny.val = my_heap[i]
        if(result == None):
            result = kolejny
            result_end = result
        else:
            result_end.next = kolejny
            result_end = kolejny

    return result
    


runtests(proba)