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
    prev_start = -10
    max_licznik = 0
    for i in range(n -1):
    
      cur_start, cur_end = L[i]
      if(cur_start == prev_start):
        continue
      prev_start = cur_start

      cur_licznik = 0

      for j in range(i+1,n):
        start, end = L[j]
        if(start == cur_start):
          cur_licznik += 1
          continue
        if(start >= cur_end):
          break
        if( start < cur_end and end <= cur_end):
          cur_licznik += 1
      
      if(cur_licznik > max_licznik):
        max_licznik = cur_licznik

    return max_licznik
    
  




runtests( depth ) 
