'''PROM DŁUGOŚCI L i tablica długości samochodów wjeżdzają po kolei'''


'''
f(A,j,k,i) j,k - miejsca na pasie lewym i prawym, i - ile rozważąmy

if (A[i] > j and A[i] > k) return 0
albo ładujemy na lewy jesli prawy nie pomieści
albo na prawy jesli lewy nie pomieści
albo na oba próbujemy jeśli można na oba

'''

A = [5,3,2,7,9]