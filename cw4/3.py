# dwa słowa o długości N z alfabetu o długości K
# k = 256
# inicjujemy tablice k
# zerujemy tylko w miesjcach gdzie są chary z A


def checkAnagrams(A,B, k):
    occurences = [0] * k
    n = len(A)
    for i in range(n):
        occurences[ord(A[i])] +=1
        occurences[ord(B[i])] -=1
    
    for i in range(n):
        if occurences[ord(A[i])] !=0 or occurences[ord(B[i])] != 0:
            return False
    return True

## albo posortować ??? ale chyba nie 