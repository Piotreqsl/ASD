''' Na wejściu ciąg liczbowy X, ciąg jest MR jeśli najpierw jest ściśle
malejący a potem rosnący, albo jeśli jest tylko ściśle malejący,
lub tylko ściśle rosnący

'''



from MRtesty import runtests


def mr(X):
    n = len(X)
    DPIncreasing = [1] *n
    ParentInc = [-1 for i in range(n)]

    DPDecreasing = [1] *n
    ParentDec = [-1 for i in range(n)]


    for i in range(1,n):
        for j in range(i):
            if(X[i] < X[j] and DPDecreasing[i] < DPDecreasing[j] + 1):
                DPDecreasing[i] = DPDecreasing[j] + 1
                ParentDec[i] = j
    
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
           if(X[i] < X[j] and DPIncreasing[i] < DPIncreasing[j] + 1):
                DPIncreasing[i] = DPIncreasing[j] + 1
                ParentInc[i] = j
    

    ## checking bitonic
    longest = 0
    idx = 0
    type = 'b'

    for i in range(n):
        if(DPDecreasing[i] != 1 and DPIncreasing != 1):
            if(DPDecreasing[i] + DPIncreasing[i] -1 > longest):
                idx = i
                longest = DPDecreasing[i] + DPIncreasing[i]
    
    for i in range(n):
        if DPDecreasing[i] > longest:
            idx = 0
            type = 'd'
        if DPIncreasing[i] > longest:
            idx =0
            type = 'i'

    if(type == 'b'):
        cur_i = idx
        res_dec = []
        while(cur_i != -1):
            res_dec.append(X[cur_i])
            cur_i = ParentDec[cur_i]

        res_inc = []
        cur_i = idx
        while(cur_i != -1):
            res_inc.append(X[cur_i])
            cur_i = ParentInc[cur_i]

        return res_dec[::-1] + res_inc[1:]
    
    elif(type == 'd'):
        res_dec = []
        cur_i = idx
        while(cur_i != -1):
            res_dec.append(X[cur_i])
            cur_i = ParentDec[cur_i]
        return res_dec
    
    
    elif(type == 'i'):
        res_inc = []
        cur_i = idx
        while(cur_i != -1):
            res_inc.append(X[cur_i])
            cur_i = ParentInc[cur_i]
        return res_inc


 
X = [1,10,5]
print(mr(X))   

runtests(mr)