def subset_sum(A,target):
    n = len(A)
    if(target == 0): return True
    if n ==0: return False

    #F[i][j] - czy rozpatrując do itego elemetnu mamy sumę J
    # i -ity element
    # j - suma

    F = [[False for i in range(target +1)] for j in range(n)]

    F[0][A[0]] = True ## ustawiam pierwszy element i wyjebane

    for i in range(1, n):
        for j in range(1, target+1):
            # jezeli obecny element ma wartosc > od obecnej sumy
            # to niemozliwe jest jej osiagniecie (wartosci sa naturalne)
            if A[i] > j:
                F[i][j] = F[i-1][j]
            
            # w przeciwnym razie sprawdzamy czy obecna suma zostala juz osiagnieta
            # albo czy istnieje taka suma do ktorej po dodaniu obecnego elementu
            # otrzymamy obecna sume
            else:
                F[i][j] = F[i-1][j] or F[i-1][j-A[i]]
    return (F, F[n-1][target])


def get_solution(F, A, i, j):
  if i == 0:
    if F[i][j]: return [A[i]]
    return []

  if F[i-1][j]:
    return get_solution(F, A, i-1, j)
  return get_solution(F, A, i-1, j-A[i]) + [A[i]]


A = [1, 3, 4, 7, 10, 8]
target = 34

#res = subset_sum(A, target)
#if res[1]:
#  print(get_solution(res[0], A, len(A)-1, target))
#else:
#  print(res[1])

### recursive simplier
def f(A,n,s,result):
 
    if(s == 0):
        return 1
    if(n == 0):
        return 0

    if(result[n][s] != -1): ## jesli w tablicy juz mam jakąś wartosc obliczoną, to nie musze drugi raz tego liczyć, zwracam i eluwina
        return result[n][s]
    
    if(A[n-1] > s): ## jesli sam ten element jest wiekszy od sumy, to siłą rzeczy musze pominąć, nie moge go wziąć bo wypierdoli siem
        result[n][s] = f(A,n-1,s,result)
        return result[n][s]
    
    excl = f(A,n-1,s,result) ## nie biore itego elementu
    incl = f(A,n-1,s - A[n-1],result) ## biore ity element, odejmuje od sumy

    result[n][s] = max(excl, incl) ## jesli oba zero to zero, jesli choc 1 to znaczy ze sie sumije

    return result[n][s]





def subsumRec(A,n,s):
    result = [[-1 for i in range(s+1)] for j in range(n+1)]
    print(f(A,n,s,result))
    print(result)

subsumRec(A,6,9)
    


