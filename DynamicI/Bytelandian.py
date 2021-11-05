maxx = 10000000

dp = [0] * maxx
def calc(n):
    if n < 3: return n
    if n < maxx and dp[n] != 0:
        return dp[n]
    result = max(calc(n//2) + calc(n//3) + calc(n//4), n)
    if n < maxx:
        dp[n] = result
    return result

while True:
    try:
        n = int(input())
        print(calc(n))
    except EOFError:
        exit()