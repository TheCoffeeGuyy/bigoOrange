def permutation(s, l, r, permutations): 
    if l == r:
        permutations.add(''.join(s))
    else:
        for i in range(l,r):
            s[l], s[i] = s[i], s[l]
            permutation(s, l+1, r, permutations)
            s[l], s[i] = s[i], s[l]

def sieve(n):
    mark[0] = mark[1] = False
    for i in range(2, int(n**0.5) +1):
        if mark[i]:
            for j in range(2 * i, n+1, i):
                mark[j] = False
    for i in range(len(mark)):
        if mark[i]:
            primes.append(i)

def isAgPrime(prime):
    s = list(str(prime))
    if any(int(x) % 2 == 0 or int(x) == 5 for x in s):
        return False
    
    permutations = set()
    permutation(s, 0, len(s), permutations)
    for per in permutations:
        print(int(per))
        if int(per) not in primes:
            return False
    return True

print(isAgPrime(113))

maxN = 200
mark = [True] * (maxN + 1)
primes = []
# agPrimes = []
sieve(maxN)
# print(primes)
# for prime in primes:
#     if prime <= 10:
#         agPrimes.append(prime)
#     if isAgPrime(prime):
#         agPrimes.append(prime)
# print(agPrimes)