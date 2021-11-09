import sys
sys.setrecursionlimit(100000000)

MAXN = 2002
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
# s1 = '1234567890'
# s2 = '13135789340'
# print(LCS(s1, s2, len(s1), len(s2)))
t = int(input())
for i in range(t):
    agnes = list(map(int,input().split()))
    boys = []
    while True:
        b = list(map(int, input().split()))
        if b[0] == 0:
            break
        else:
            dp = [[-1] * MAXN for i in range(MAXN)]
            boys.append(LCS(agnes, b, len(agnes), len(b)))    
    print(max(boys) - 1)
    