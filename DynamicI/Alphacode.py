while True:
    s = input()
    if s == '0':
        exit()
    dp = [0] * 5002
    dp[0] = 1
    for i in range(1, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] = dp[i-1]
        if i >= 2 and s[i - 2] != '0':
            if int(s[i-2:i]) <= 26:
                dp[i] += dp[i -2]
    print(dp[len(s)])