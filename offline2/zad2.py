from zad2testy import runtests


## WYJEBAĆ TO
from zad2testy import printmy

def less(int1, int2):

  if(int1[0] < int2[0]):
    return True
  elif (int1[0] > int2[0]):
    return False
  else:
    if(int1[1] >= int2[1]):
      return True
    else:
      return False
  

def partit(tab, low, high):
    a = low + 1
    b = high 
    osiowy = tab[low]
    while(True):
      while(less(tab[a], osiowy)):
        if(a == high):
          break
        a +=1
      while(less(osiowy, tab[b])):
        if(b == low):
          break
        b -= 1
      if (a >= b):
        break
      tab[a], tab[b] = tab[b], tab[a]
    tab[low], tab[b] = tab[b], tab[low]
    return b



def sort(L, low, high):
  while(low < high):
    j = partit(L, low, high)
    sort(L, low, j-1)
    low = j+1





def depth(L):
    n = len(L)
    sort(L,0, n-1)
    #printmy(L)

    for i in range(n):
      L[i].append(True)
    
    max = 0
    for i in range(n):
      if(L[i][2] == True):
        count = 0
        for j in range(i+1, n):
          if(L[i][1] >= L[j][0]):
            if(L[i][1] >= L[j][1]):
              L[j][2] = False
              count +=1

          else:
            break
        if(count > max):
          max = count
    return max

    
  




runtests( depth ) 
