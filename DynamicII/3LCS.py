MAXN = 102

def LCS(s1 ,s2, s3, m, n, k):
    if m == 0 or n == 0 or k == 0:
        dp[m][n][k] = 0
        return dp[m][n][k]
    if dp[m][n][k] != -1:
        return dp[m][n][k]
    if s1[m-1] == s2[n-1] == s3[k-1]:
        dp[m][n][k] = 1 + LCS(s1, s2, s3, m-1, n - 1, k-1)
        return dp[m][n][k]
    else:
        dp[m][n][k] = max(LCS(s1, s2, s3, m-1, n,k), LCS(s1, s2, s3, m, n -1,k), LCS(s1, s2, s3, m, n, k-1))
        return dp[m][n][k]

t = int(input())    

for i in range(t):
    n, m, k = map(int, input().split())
    sn, sm, sk = input().split()
    dp = [[[0 for j in range(MAXN)] for i in range(MAXN)] for k in range(MAXN)]
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(k + 1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif sn[i - 1] == sm[j - 1] and sm[j - 1] == sk[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    print(dp[n][m][k])