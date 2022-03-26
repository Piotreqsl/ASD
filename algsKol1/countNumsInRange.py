

accumulatinTab =[]

def countNumsConstructor(tab, k):
    global accumulatinTab
    accumulatinTab = [0] * (k+1)
    for i in range(len(tab)):
        accumulatinTab[tab[i]] +=1
    for i in range(1,k+1):
        accumulatinTab[i] += accumulatinTab[i-1]

def count_num_in_range(a,b):
    global accumulatinTab
    return accumulatinTab[b] - accumulatinTab[a-1]

A = [1,3,4,5,7,8,9,3,2,3,6,5]
countNumsConstructor(A,10)
print(count_num_in_range(4,8))    
