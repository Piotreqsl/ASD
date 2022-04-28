def print_solution(s, F):
  n = len(s)

  for i in range(n):
    for j in range(n-1, i+1, -1):
      if F[i][j]:
        print(s[i:j+1])
        return

def LongestPal(s):
    n = len(s)
    DP = [[0 for i in range(n)] for j in range(n)]
    ## DP[i][j] - czy jest palindromem od i do j
    ## wynik DP[0][n-1]
    DP[0][0] = True
    for i in range(1,n):
        DP[i][i] = True
        if(s[i] == s[i-1]):
            DP[i-1][i] = True
    for length in range(2,n):##dlugosc przedziału
        for i in range(n-length): ## start przedziału
            DP[i][length+i] = ((s[i] == s[length+i]) and DP[i+1][i+length-1])

    print_solution(s, DP)


    
    # kajak
s = 'romkajakan'
LongestPal(s)