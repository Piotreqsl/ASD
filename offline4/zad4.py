###Piotr Śliperski
## rozwiązanie w oparciu o programowanie dynamiczne
## Na początku doklejam do każdego z budynków jego index w tablicy wejściowej - przyda się do rozwiązania
## potem sortuję tablice wzgledem końca budynków
## Potem ustalam tablice pomocnicze, costs i students - wykonując obliczenia zawarte w tresci zadania
## oraz previus - służąca do spamiętania ostatniego niekolidującego budynku
## ustalam tablicę F
## 
## F[i][p] maksymalna liczba osob jaka wejdzie do i pierwszych budynków
## przy koszcie p
##
## oraz wypełniam pierwzy jej wiersz, który jest trywialny
## nastepnie przechodzę pętlą po wszystkich wartościach n i po wszystkich kosztach p
## kroki wypełniania są opisane w komentarzu w pętli
## w ostatniej linii tabeli F (uwzgedniającej wszystkie budnyki) sprawdzam jaki jest najmniejszy koszt zawierający najwiekszą liczbe studentów
## Finalna pętla while, służy do pozyskania wyniku z tabeli F
## w przypadku, gdy zauważam że algorytm wziął do sumy jakis budynek, to cofam się z wykorzystaniem tablicy previous
## zwracam posortowaną tablicę z indexami, tak jak w poleceniu


## złożoność sortowania nlogn
## złożoność przejrzenia tablicy(n*p + c*n)
## c to stała wynikająca z przeglądania tablicy w celu uzupełnienia tablic testowych

from zad4testy import runtests

def makePrevious(T,previous):
    n=len(T)
    for i in range(n):
        for j in range(i-1,-1,-1):
            if(T[j][2] < T[i][1]):
                previous[i] = j
                break



def printTwoDim(n):
    for i in range(len(n)):
        print(n[i])

def select_buildings(T,p):
    ##doklejam indeksy w tablicy wejściowej
    n = len(T)
    for i in range(n):
        T[i] = [T[i][0], T[i][1], T[i][2], T[i][3], i]

    
    T.sort(key=lambda x: x[2])
    ## tworze tablice pomocnicze do prog dynamicznego
    costs = [T[i][3] for i in range(n)]
    students = [(T[i][0] * (T[i][2] - T[i][1])) for i in range(n)]

    previous = [None for i in range(n)]
    makePrevious(T,previous)

    ## F[i][p] maksymalna liczba osob jaka wejdzie do i pierwszych budynków
    ## przy koszcie p
    F = [[0 for i in range(p+1)] for i in range(n)]
  
    ## wypelniam pierwszą linię
    for i in range(costs[0], p+1):
        F[0][i] = students[0]
    ### za koszt budynku T[0] lub wiekszy mozemy ulokować studnets[0] uczniów

    for i in range(1,n):
        for cena in range(1,p+1):
            if(cena < costs[i]): ## cena danego budynku przewyższa aktualnie rozważaną, pomijamy
                F[i][cena] = F[i-1][cena]

            else:
                if previous[i] != None: ## jeśli budynek ma poprzednika, to muszę go rozważyć (albo pomijam budowanie budynku, albo buduję)
                    F[i][cena] = max(F[i-1][cena], F[previous[i]][cena - costs[i]] + students[i])
                else: ## jeśli nie ma, to albo mogę wybudować budynek jako jedyny obecnie, albo pominąć budowanie go
                    F[i][cena] = max(F[i-1][cena], students[i])
    best = 0
    for i in range(p, -1, -1):
        if F[n - 1][i] >= F[n - 1][best]:
            best = i
    
    res = []
    cur_row = n-1
    cur_cena = best

    while  cur_row is not None and cur_row >= 0 :
        if cur_row == 0 :
            if T[cur_row][3] <= cur_cena:
                res.append(T[cur_row][4])
                break
            else:
                break
        else:
            if F[cur_row][cur_cena] == F[cur_row-1][cur_cena]:
                cur_row = cur_row-1
            else:
                res.append(T[cur_row][4])
                cur_cena = cur_cena - costs[cur_row]
                cur_row = previous[cur_row]
                
                
                
    return sorted(res)
  



    # tu prosze wpisac wlasna implementacje
    #return [0]

runtests( select_buildings )