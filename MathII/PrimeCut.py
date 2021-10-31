def sieveOfEratosthenes(n):
    mark = [True] * (n + 1)
    mark[0] = False
    mark[1] = True
    primes = []
    for i in range(2, int(n ** 0.5) + 1):
        if mark[i]:
            for j in range(i * i, n+1, i):
                mark[j] = False
    
    for i in range(1, n + 1):
        if mark[i]:
            primes.append(i)
    
    return primes

while True:
    try:
        n, c = map(int, input().split())
        primes = sieveOfEratosthenes(n)
        m = len(primes)
        if m < 2 * c - 1:
            for i in primes:
                print(i)
        
        print(primes)
    except EOFError:
        exit()