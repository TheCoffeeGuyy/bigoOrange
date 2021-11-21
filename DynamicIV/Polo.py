
class Subject:
    def __init__(self, p, w):
        self.p = p
        self.w = w

t = int(input())

for i in range(t):
    n, w = map(int, input().split())
    a = [Subject(0, 0)]
    for _ in range(n):
        c, p, t = map(int ,input().split())
        a.append(Subject(c *p, t))
    
    dp = [[0] * (w+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(w+1):
            if a[i].w <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - a[i].w] + a[i].p)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][w])