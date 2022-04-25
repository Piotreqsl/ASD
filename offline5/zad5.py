## Piotr Śliperski
## Algorytm opiera sie na podstawowym wykorzystaniu kolejki priorytetowej
## przechodzę jeden raz całą listę dokładając do kolejki punkty ze stacjami
## Kiedy stanie się tak, że moje paliwo wynosić będzie zero
## wtedy wybieram najlepsza dostepną stację którą minąłem
##
## Dowód poprawności:
## zakładam że na polu 0 jest k paliwa
## zatem na k-tym polu moje paliwo wynosić będzie zero
## najoptymalniejsza stacja z przedziału 0-k stoi na miejscu i (i<=k)
## zatem tankując na niej miałbym 
## T[0] - i + T[i] - (k - i) paliwa
## jak widzimy i się zredukowały oraz T[0] = k
## więc mogę dowolnie wybierać najoptymalniejsze stacje
## z dostępnego zasięgu i na pozycji k będe miał 
## T[i] paliwa


from zad5testy import runtests

from queue import PriorityQueue

def plan(T):
    n = len(T)
    fuel = 0

    q = PriorityQueue()

    res = [0]
    for i in range(n):
        fuel -=1
        if(i ==0):
            fuel = T[0]
            continue

        if(i == n-1):
            break

        if(T[i] != 0):
            q.put(( -1* T[i], i))

        if(fuel == 0):
            top = q.get()
            res.append(top[1])
           # print("tankuje z", top[0])
            fuel =  -1 * top[0]
        
        
            


    # tu prosze wpisac wlasna implementacje
    return sorted(res)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )