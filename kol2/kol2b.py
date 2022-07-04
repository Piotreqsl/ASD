from kol2btesty import runtests



def f(F,oc,point, can_use_jump, T):
    if(point == 0):
        return 0
    if(F[point][can_use_jump] != float("inf")):
        return F[point][can_use_jump]

    best = float("inf")
    #print("calling func", point, can_use_jump)
    if(can_use_jump == 1):
        ## szukam stacji w odległości (T, 2T] kilometrów
        cur_idx = point -1 ## point to index stacji
        cur_pos = oc[point][0]
        while cur_idx >=0:
            alleged_pos = oc[cur_idx][0]
            if(cur_pos - alleged_pos > T and cur_pos - alleged_pos <= 2*T):
                best = min(best,f(F,oc,cur_idx,0,T) + oc[cur_idx][1])
            if(cur_pos-alleged_pos > 2*T):
                break
            cur_idx -=1
        
        ## lub nie używam tera bonusu
        cur_idx = point -1
        while(cur_idx >= 0):
            alleged_pos = oc[cur_idx][0]
            if(cur_pos - alleged_pos <= T):
                best = min(best,f(F,oc,cur_idx,1,T) + oc[cur_idx][1])
            if(cur_pos-alleged_pos > T):
                break
            cur_idx -=1
    elif(can_use_jump == 0):
        cur_idx = point -1
        cur_pos = oc[point][0]
        while(cur_idx >= 0):
            alleged_pos = oc[cur_idx][0]
            if(cur_pos - alleged_pos <= T):
                best = min(best,f(F,oc,cur_idx,0,T) + oc[cur_idx][1])
            if(cur_pos-alleged_pos > T):
                break
            cur_idx -=1
    
    F[point][can_use_jump] = best
    return best







def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje
    O.insert(0,0)
    O.append(L)
    C.insert(0,0)
    C.append(0)

    #print(O)
    
    n = len(C)
    oc = [(O[i], C[i]) for i in range(n)]
    oc.sort()
    #print(oc)
    F =[[float("inf"), float("inf")] for i in range(n)]

    return f(F,oc,len(oc)-1, 1, T)

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
