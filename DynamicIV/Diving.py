class Treasure:
    def __init__(self, deep, value):
        self.deep = deep
        self.value = value
while True:
    t, w = map(int,input().split())
    n = int(input())
    a = [Treasure(0, 0)]
    for i in range(n):
        d, v = map(int, input().split())
        a.append(Treasure(d, v))

    dp = [[0] * (t+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(t+1):
            if a[i].deep <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - a[i].deep*w*3] + a[i].value)
            else:
                dp[i][j] = dp[i][j-1]
        
    print(dp[n][t])
    ans = []
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i-1][t]:
            ans.append(a[i])
            t -= a[i].deep *w *3
    ans.reverse()
    print(len(ans))
    for x in ans:
        print(x.deep, x.value)

    try:
        input()
    except EOFError:
        exit()