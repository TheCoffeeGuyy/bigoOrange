class Cylinder:
    def __init__(self, oxy, nitro, weight):
        self.oxy = oxy
        self.nitro = nitro
        self.weight = weight

INF =1000000000
c = int(input())

for _ in range(c):
    t, a = map(int, input().split())
    n = int(input())
    # arr = [Cylinder(0,0,0)]
    arr = [Cylinder(0,0,0)]
    for i in range(n):
        o, ni, w = map(int, input().split())
        arr.append(Cylinder(o, ni, w))
    dp = [[[INF] * 1001 for i in range(80)] for j in range(22) ]
    dp[0][0][0] = 0
    for i in range(1, n+1):
        for j in range(0, t+1):
            for k in range(0, a+1):
                temp1 = dp[j][k][i-1]
                tempO = max(0, j - arr[i].oxy)
                tempN = max(0, k - arr[i].nitro)
                temp2 = dp[tempO][tempN][i-1] + arr[i].weight
                dp[j][k][i] = min(temp1, temp2)
    print(dp[t][a][n])
    if _ != c - 1:
        input()

# dp = [[[0] * 2 for i in range(3)] for j in range(4) ]
# print(dp)
