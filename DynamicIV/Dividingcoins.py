t = int(input())

for i in range(t):
    m = int(input())
    a = [0] + (list(map(int ,input().split())))
    suma = sum(a)
    w = suma // 2
    dp = [0] * (w+1)
    for i in range(1, m+1):
        for j in range(w+1):
            if a[i] > j:
                dp[j] = dp[j-1]
            else:
                dp[j] =  a[i] + dp[j - a[i]]
                
    # print(dp[w], suma)
    print(suma - dp[w] * 2)
                
    