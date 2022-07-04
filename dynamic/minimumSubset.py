'''The Post Office of Maldonia issued a new series of stamps, whose denominations in cents are a finite set D ⊂ N\{0}, with 1 ∈ D. 
Given an arbitrary value n ∈ N\{0} in cents, the problem is to find a minimum-cardinality multiset of stamps from D whose denominations add up to exactly n.'''
## zadanko z cambridge, a jakoś sie wydaje że still łatwiejsze niż na agh




D = [1, 3, 4, 5]


def minimum(D,n):
    ## zakladam że sie sumują
    F = [[0 for i in range(n+1)] for j in range(len(D))]
    l = len(D)
    F[0][D[0]] = 1
    for i in range(1,l):
        for sum in range(1,n+1):
            F[i][sum] = F[i-1][sum]
            if(D[i] <= sum):
                if(F[i-1][sum - D[i]] > 0):
                    if(F[i][sum] == 0):
                         F[i][sum] = F[i-1][sum - D[i]] + 1
                    else:
                        F[i][sum] = min(F[i-1][sum - D[i]] + 1, F[i][sum])
                elif(F[i-1][sum - D[i]]  == 0 and D[i] == sum):
                    F[i][sum] = 1
    res = []
    actual_num = F[l-1][n]
    cur_row = l-1
    cur_sum = 8
    while(actual_num > 0):
        if(cur_row > 0):
            if(F[cur_row-1][cur_sum] == F[cur_row][cur_sum]):
                cur_row -=1
            else:
                res.append(D[cur_row])
                cur_sum -= D[cur_row]
                cur_row -=1
                actual_num -=1
    print(sorted(res))
    for each in F:
        print(each)
    print(F[l-1][n])


minimum(D,8)
