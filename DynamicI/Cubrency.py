cubes = [i * i * i for i in range(1, 22)]
dp = [0] * (10000 +1)
dp[0] = 1
for i in range(len(cubes)):
    for j in range(cubes[i], 10000 + 1):
        dp[j] = dp[j] + dp[j - cubes[i]]
while True:
    try:
        total = int(input())
        print(dp[total])
    except EOFError:
        exit()
