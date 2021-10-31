t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    r = x % k
    if r == 0:
        p = k
        q = 0
    else:
        a = x // k
        p = 1 + a - x
        q = x - a
    print(p, q)