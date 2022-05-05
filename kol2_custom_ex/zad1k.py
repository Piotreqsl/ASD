from zad1ktesty import runtests

'''Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego
ciągu, w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w
ciągu występują same jedynki, należy założyć, że rozwiązaniem jest -1 '''


## algorytm szukania największej sumy po zamienieniu zer na jedynkę a 1 na -1



def allones(s, n):
     
    # Checking each index
    # is 0 or not.
    co = 0
     
    for i in s:
        co += 1 if i == '1' else 0
 
    return co == n


def roznica( S ):
    #Tutaj proszę wpisać własną implementację

    n = len(S)
    if(allones(S,n)):
        return -1
    maxsum = 0
    cursum = 0
    for i in range(n):
        cursum += (1 if S[i] == '0' else -1)
        if(cursum < 0):
            cursum = 0
        maxsum = max(cursum, maxsum)

    return maxsum


    

runtests ( roznica )