from kol2atesty import runtests

## driver 0 - jacek
## driver 1 - marian

def f(F,przesiadki, PK, driver, point, parents):
   # if(driver == 0):
    #    print("rozważąm że do pkt kontrolnego nr", point, "dojechal jacek")

    if(point <=3 and driver == 0):
        return 0
    elif(point == 1 and driver == 1):
        return float("inf")

    if(F[point] != float("inf")):
        return F[point]
    
    best = float("inf")
    for i in range(point-1, max(point-4, 0), -1):
      
        if(driver == 0):
            re = f(F,przesiadki, PK, 1, i,parents)
            if(re < best):
                best = re
                parents[point] = i

        else:
            
            re = f(F,przesiadki, PK, 0, i, parents) + PK[przesiadki[point][0]] - PK[przesiadki[i][0]]
            if( re < best):
                best =re
                parents[point] = i
    F[point]=  best
    return F[point]




def drivers( P, B ): 
    # tu prosze wpisac wlasna implementacje

    P.append((B,True))



    n = len(P)
    for i in range(n):
        P[i] = ((P[i][0], P[i][1], i))

    ctrl_idx = 0
    for i in range(len(P)):
        if(P[i][1] == True):
            ctrl_idx = i
            break
    ctrl_points = P[ctrl_idx:]
    ctrl_points.insert(0,(0, True, 0))
    
    P.sort(key=lambda x: x[0])
    P.insert(0,(0,True, 0))
    PKPrefix = [0 for i in range(B+1)]
    for i in range(B):
        if(i <n):
            if(P[i][1] == False):
                PKPrefix[i] = PKPrefix[i-1] + 1
            else:
                PKPrefix[i] = PKPrefix[i-1]
        else:
            PKPrefix[i] += PKPrefix[i-1]
    PKPrefix[B] = PKPrefix[B-1]

    F = [float("inf") for i in range(len(ctrl_points))]
    Parents = [-1 for i in range(len(ctrl_points))]
   

    print(f(F,ctrl_points,PKPrefix,0,len(ctrl_points)-1, Parents))
    print(F)
    print(Parents)
    cur_idx = len(Parents) -1
    res = []
    while(Parents[cur_idx] != -1):
        res.append(ctrl_points[Parents[cur_idx]][2])
        cur_idx = Parents[cur_idx]

    print(res[::-1])



    return []
## generalnie liczy dobrze te punkty ale no kurwa nie ma szans żeby wyciągnać te wyniki poprawne do chuja
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )