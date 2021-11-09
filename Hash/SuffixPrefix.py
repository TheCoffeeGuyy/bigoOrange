MOD = 1000000007
MAX_S = 1000001
BASE = 33
hash = MAX_S * [0]
mul = [0] * MAX_S

def doHash(s):
    hash[0] = 0
    n = len(s)
    for i in range(1, n + 1):
        hash[i] = (hash[i - 1] * BASE + ord(s[i - 1]) - 97) % MOD
def getHash (l, r):
    return (hash[r] - hash[l - 1] * mul[r - l + 1]) % MOD

mul[0] = 1
for i in range(1, MAX_S):
    mul[i] = (mul[i - 1] * BASE) % MOD

t = int(input())
for k in range(t):
    s = input()
    doHash(s)
    count = 0
    lens = len(s)
    # print(hash)
    for i in range(1, lens):
        if getHash(1,i) == getHash(lens - i + 1, lens):
            count += 1
    print(f'Case {k+1}: {count}')
