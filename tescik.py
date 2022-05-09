def MinPalindromeCuts(s):
    n = len(s)
    
    C = [0]* (n+1)


   
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
         dp[i][i] = True
    max_length = 1
    start = 0
    for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
    longestString = s[start:start+max_length]
    
    for i in range(n):
        if (dp[0][i] == True):
            C[i] = 0;
        else:
            C[i] = float("inf");
            for j in range(i):
                if(dp[j][i] == True):
                    C[i] = min(C[i], 1+ C[j])

    print(longestString)
    return C[n-1]
    

str = "ababbbabbababa"
print(MinPalindromeCuts(str))