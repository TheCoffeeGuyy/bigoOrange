t = int(input())

for _ in range(t):
    x, k = map(int, input().split())

    p = 0 
    q = k
    while q:
        if x == (p*(x/k) + q*(x/k)):
            break
        q-=1
        p += 1
    print(p, q)