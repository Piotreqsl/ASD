'''Given string str, write a program to partition str such that 
every substring of the partition is a palindrome. 
Return the minimum cuts needed for a palindrome partitioning of str.'''

##DP[i][j] czy string na pozycji i-j jest palindrome
## 
    


def MinPalindromeCuts(s):
    n = len(s)
    
    isPal = s == s[::-1]
    if(isPal):
        return 0
    
    C = [0]* (n+1)


   
    DP=[[False for i in range(n)] for j in range(n)]
    for i in range(1,n):
        DP[i][i] = True
        if(s[i-1] == s[i]):
            DP[i-1][i] = True
    DP[0][0] = True

    for length in range(2,n):
        for i in range(n - length):
            DP[i][length + i] = ((s[i] == s[length+i]) and DP[i+1][i+length-1])
    
    for i in range(n):
        if (DP[0][i] == True):
            C[i] = 0;
        else:
            C[i] = float("inf");
            for j in range(i):
                if(DP[j][i] == True):
                    C[i] = min(C[i], 1+ C[j])
                    #C[i] = 1 + C[j];




    return C[n-1]

str = "ababbbabbababa"
print(MinPalindromeCuts(str))
