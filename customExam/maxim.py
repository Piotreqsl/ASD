from maximtesty import runtests


## zauważam że sposób dotarcia do danego indeksu zależy od binarnej
## reprezentacji danej liczby

def decToBin(x):
    s = ''
    while(x > 0):
        s = str(x%2) + s
        x = x//2
    return s

def findKey(T,idx):
    bin = decToBin(idx)
    for i in range(1,len(bin)):
        if(bin[i] == '0'):
            T = T.left
        else:
            T = T.right
    return T.key




def maxim(T,X):
    _max = 0
    for i in X:
        _max = max(_max, findKey(T,i))
    return _max

runtests(maxim )