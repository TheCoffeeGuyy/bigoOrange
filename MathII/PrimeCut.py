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
        print(f'{n} {c}:', end=' ')
        if m < 2 * c - 1:
            for i in primes:
                print(i, end=' ')
        else:
            start = m // 2 - c+ (m % 2)
            end = m // 2 + c
            for i in range(start, end):
                print(primes[i], end=' ')
        print('\n')
    except EOFError:
        exit()