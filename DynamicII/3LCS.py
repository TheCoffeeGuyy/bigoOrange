MAXN = 1002
dp = [[-1] * MAXN for i in range(MAXN)]

def LCS(s1 ,s2, m, n):
    if m == 0 or n == 0:
        dp[m][n] = 0
        return dp[m][n]
    if dp[m][n] != -1:
        return dp[m][n]
    if s1[m-1] == s2[n-1]:
        dp[m][n] = 1 + LCS(s1, s2, m-1, n - 1)
        return dp[m][n]
    else:
        dp[m][n] = max(LCS(s1, s2, m-1, n), LCS(s1, s2, m, n -1))
        return dp[m][n]

def printLCS(s1, s2, m, n):
    lengthLCS  = dp[m][n]
    result = [''] * lengthLCS
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result[lengthLCS - 1] = s1[i -1] 
            i -= 1
            j -=1 
            lengthLCS -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    print((''.join(result)))
    return (''.join(result))

# s1 = '1234567890'
# s2 = '13135789340'
# LCS(s1, s2, len(s1), len(s2))
# printLCS(s1, s2, len(s1), len(s2))

t = int(input())    

for i in range(t):
    n, m, k = map(int, input().split())
    sn, sm, sk = input().split()
    LCS(sn, sm, len(sn), len(sm))
    common = printLCS(sn, sm, len(sn), len(sm))
    dp = [[-1] * MAXN for i in range(MAXN)]
    print(LCS(sk, common, len(sk), len(common)))
