n = int(input())

listN = list(map(int, input().split()))
f = [0 for i in range(n+1)]
# f[0] = listN[0]
for i in range(1, n+1):
    f[i] = f[i - 1] + (listN[i - 1] == 1)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    oneCount = f[r] - f[l - 1]
    zeroCount = (r - l + 1) - oneCount
    print(1 if oneCount % 2 == 1 else 0, zeroCount)