
## cormen planning an investemnt strategy
## https://walkccc.me/CLRS/Chap15/Problems/15-10/

## dwie tablice  I oraz R (10 elementowe)
## I[i] mówi która inwestycja powinna być zrobiona (pełną pulą siana)
## R[i] mówi jak duzy jest zwrot w roku itym

## zaczynam pętlą po k 10 ąz do 1
## na początku szukam najoptymalniejszej inwestycji na dany rok

## potem sprawdzam czy R[k+1] +dollars_revenued*[I[k+1]] - f[1] > R[k+1] + dollarsReveneud[q,k] -f[2]
    ## czyli czy bardziej sie pyli ruszyć kasę czy nie

## w koncu otrzymuję optymalną strategię I