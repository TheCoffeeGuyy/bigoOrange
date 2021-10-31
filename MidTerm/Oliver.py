import sys
sys.setrecursionlimit(100000000)

t=0
def dfs(startTime, endTime, graph, u):
    global t
    t += 1
    startTime[u] = t
    for v in graph[u]:
        if startTime[v] == 0:
            dfs(startTime, endTime,graph,v)
    endTime[u] = t

n = int(input())
graph = [[] for _ in range(n)]
startTime = [0] * n
endTime = [0] * n
for i in range(n - 1):
    u, v= map(int, input().split())
    u -=1
    v -=1
    graph[u].append(v)
    graph[v].append(u)
dfs(startTime, endTime, graph, 0)

q = int(input())
for i in range(q):
    side, x, y = map(int, input().split())
    x -=1
    y -=1
    if side == 1:
        x, y = y, x
    if startTime[x] <= startTime[y] and endTime[x] >= startTime[y]:
        print('YES')
    else:
        print('NO')