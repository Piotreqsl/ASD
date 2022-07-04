

def lamps(n,L):
    cur_blue = 0
    max_blue = 0
    alllamps = [0 for i in range(n)]

    for i in range(len(L)):
        for j in range(L[i][0], L[i][1]+1):
            if(alllamps[j] == 0):
   
                alllamps[j] =1
            elif(alllamps[j] == 1):
                cur_blue +=1
      
                alllamps[j] = 2
            elif(alllamps[j] == 2):
                cur_blue -=1
                alllamps[j] = 0
        max_blue = max(max_blue, cur_blue)
    return max_blue

print(lamps(8, [(0,4), (2,6)]))