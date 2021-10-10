import functools

t = int(input())
def sol():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(32):
        bestSubset = list(filter(lambda x: (x >> i) & 1, a))
        # for j in range(len(bestSubset)):
        #     andAll &= bestSubset[j]
        andAll = functools.reduce(lambda x, y: x&y, bestSubset, 0x7FFFFFFF)
        if ((andAll & (andAll - 1)) == 0) and andAll != 0:
            print('YES')
            return
    print('NO')
for _ in range(t):
    sol()
