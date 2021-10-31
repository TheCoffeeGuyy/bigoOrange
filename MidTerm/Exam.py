def modularExp(a,b,m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    
    return result

m = 1000000007
t = int(input())
for i in range(t):
    n = int(input())
    res = (modularExp(2, n, m) - (1 % m)) % m
    print(res)