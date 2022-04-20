def get_solution(F, cost, students, prev, i, p):
    if i == 0:
        if p >= cost[0]: return [0]
        return []
    if p >= cost[i] and prev[i] is not None and F[i][p] == F[prev[i]][p - cost[i]] + students[i]:
        return get_solution(F, cost, students, prev, prev[i], p - cost[i]) + [i]
    return get_solution(F, cost, students, prev, i - 1, p)


def select_buildings(T,maxP):
    n = len(T)
    for i in range(n):
        T[i] = [T[i][0], T[i][1], T[i][2], T[i][3], i]
    T.sort(key=lambda x: x[2])
    prev = [None] * n 
    cost = [None] * n
    students = [None] * n

    F = [[0 for i in range(maxP + 1)] for j in range(n)]
    for i in range(n):
        cost[i] = T[i][3]
        students[i] = (T[i][2] - T[i][1]) * T[i][0]
        for j in range(i-1, -1, -1):
            if(T[j][2] < T[i][1]):
                prev[i] = j
                break
    ## płacąc co najmniej cost[0] pieniedzy mozna ustawić students[0] studentów
    for p in range(cost[0], maxP +1):
        F[0][p] = students[0]
    for i in range(1,n):
      for p in range(1,maxP+1):
        F[i][p] = F[i-1][p] ## albo nie biore i tego budynku i nie buduje
            ## jesli koszt budowy tego budynku jest mniejszy lub równy
            ## oraz ten budynek miał jakiegos poprzednika
            ## to patrze 
            ## czy bardziej sie oplaca po prostu skipnać
            ## tudzież do studentów budynku poprzedniego dopisać
            ## obecnych
        if(p >= cost[i] and prev[i] is not None):
          F[i][p] = max(F[i][p], F[prev[i]][p-cost[i]] + students[i])