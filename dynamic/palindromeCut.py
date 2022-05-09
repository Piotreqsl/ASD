'''Given string str, write a program to partition str such that 
every substring of the partition is a palindrome. 
Return the minimum cuts needed for a palindrome partitioning of str.'''

##DP[i][j] czy string na pozycji i-j jest palindrome
## 
    


from torch import long


def MinPalindromeCuts(s):
    n = len(s)
    
    isPal = s == s[::-1]
    if(isPal):
        return 0
    
    C = [0]* (n+1)

    start = 0
    longest = 1
   
    DP=[[False for i in range(n)] for j in range(n)]
    for i in range(1,n):
        DP[i][i] = True
        if(s[i-1] == s[i]):
            start = i-1
            longest = 2
            DP[i-1][i] = True
    DP[0][0] = True

    for length in range(2,n):
        for i in range(n - length):
            if((s[i] == s[length+i]) and DP[i+1][i+length-1]):
                start = i
                longest = length
                DP[i][length + i] = True
    
    for i in range(n):
        if (DP[0][i] == True):
            C[i] = 0;
        else:
            C[i] = float("inf");
            for j in range(i):
                if(DP[j][i] == True):
                    C[i] = min(C[i], 1+ C[j])
                    #C[i] = 1 + C[j];

    longestString = s[start:start+longest+1]
    print(longestString)


    return C[n-1]

str = "ababbbabbababa"
print(MinPalindromeCuts(str))
