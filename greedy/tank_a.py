# algorytm
# za kazdym razem jedziemy do najbardziej oddalonej stacji w kierunku t




def minTanks(arr,L):
    n = len(arr)
    target = arr[n-1]
    if(target <= L):
        return [0]


    cur_pos = arr[0]
    cur_index = 0
    res =[arr[0]]
    while(cur_pos < target):
        further_index = -1
        next_index = cur_index +1
        if(cur_pos + L >= target):
            return res

        while(next_index < n and cur_pos + L >= arr[next_index]):
            further_index = next_index
            next_index +=1
        
        if(further_index == -1):
            print("Nie można dojechać")
            return
        else:
            cur_pos = arr[further_index]
            cur_index = further_index

        res.append(cur_pos)
        
    return res

print(minTanks([0,4,6,11], 4))
       