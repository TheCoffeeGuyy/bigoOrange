def LCS(f1,f2,m,n):
    if m == 0 or n == 0:
        dp[m][n] = 0
        return dp[m][n]
    if dp[m][n] != -1:
        return dp[m][n] 
    if f1[m - 1] == f2[n -1]:
        dp[m][n] = 1 + LCS(f1, f2, m-1,n-1)
        return dp[m][n] 
    else:
        dp[m][n] = max(LCS(f1, f2, m-1,n), LCS(f1,f2,m,n-1))
        return dp[m][n] 
    
def path(f1, f2, m, n):
    res = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if f1[i - 1] == f2[j -1]:
            res += f1[i - 1]
            i -= 1
            j-= 1 
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
            res += f1[i]
        else:
            j-=1
            res += f2[j]
    while i > 0:
        res += f1[i-1]
        i -=1
    while j > 0:
        res += f2[j-1]
        j -=1
    return res[::-1]
                

while True:
    try:
        f1, f2 = input().split()
        dp = [[-1] * 101  for j in range(101)]
        LCS(f1,f2,len(f1),len(f2))
        print(path(f1,f2,len(f1),len(f2)))
    except EOFError:
        exit()