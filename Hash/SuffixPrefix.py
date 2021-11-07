# t = int(input())

# for _ in range(t):
#     s = input()
#     lenS = len(s)
#     count = 0
#     for i in range(1, lenS):
#         # print(s[0:i:1], s[lenS-i:lenS:1])
#         if s[0:i:1] == s[lenS-i:lenS:1]:
#             count += 1
#     print(f'Case {_ + 1}: {count}')
MOD = 1000000007
MAX_S = 1000001
BASE = 33
hash = MAX_S * [0]
mul = MAX_S * [0]

def doHash(s):
    hash[0] = 0
    for i in range(len):
        hash[i] = (hash[i - 1] * BASE + ord(s[i]) - 97) % MOD
# ababab
# 012345
def getHash (l, r):
    return (hash[r+1] - hash[l - 2] * BASE ** (r - l + 1)) % MOD