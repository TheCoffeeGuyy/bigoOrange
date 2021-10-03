V, E = map(int, input().split())

graph = [[] for i in range(V + 1)]

for x in range(1,E+1):
    line = list(map(int, input().split()))
    for i in range(1, len(line)):
        graph[x].append(line[i])

visited = [False] * (V + 1)
decreaseOrderList = []
result = [0] * (V + 1)

def dfs(u, graph, visited, decreaseOrderList):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited,decreaseOrderList)
    
    decreaseOrderList.append(u)

for i in range(1, V + 1):
    if not visited[i]:
        dfs(i, graph, visited, decreaseOrderList)

decreaseOrderList.reverse()
for i in range(1, len(decreaseOrderList)):
    result[decreaseOrderList[i]] = decreaseOrderList[i-1]

for i in range(1, len(result)):
    print(result[i])