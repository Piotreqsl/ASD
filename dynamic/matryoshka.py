"""Sasza kolekcjonuje rosyjskie lalki - matrioszki. Każda z nich ma określoną wysokość X i szerokość Y, dane liczbami
 naturalnymi dodatnimi. Jedną matrioszkę można włożyć do drugiej, jeżeli ma od niej mniejszą zarówno wysokość, jak i szerokość.
 Sasza zastanawia się, jaki jest najdłuższy ciąg matrioszek, które może powkładać w siebie po kolei.
 Pomóż mu znaleźć odpowiedź na to pytanie.
"""

# f(i) - najdłuższy ciąg matrioszek z zewnętrzną i

# sortujemy matrioszki rosnąco po jednym wymiarze i wykonujemy lisa po drugiej patrząc czy się mieszczą




def matryoshka(A):
    n = len(A)
    A.sort(key=lambda x: x[1], reverse=True)

    F = [1] * n #każda matrioszka tworzy z sobą ciąg matrioszek długości 1
    parent = [-1] * n
    maxl = -1



  
    return result


A = [(0, 3), (0, 5), (0, 1), (0, 8), (0, 2), (0, 4), (0, 7), (0, 6), (0, 1), (0, 3)]
print(matryoshka(A))