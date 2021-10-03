def dfs (u, graph, visited, result):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, result)
    result.append(u)

V, E = map(int, input().split())

graph = [[] for i in range(V + 1)]
result = []
# for i in range(E):
#     u, v = map(int, input().split())
#     graph[u].append(v)

for x in range(1,E+1):
    line = list(map(int, input().split()))
    for i in range(1, len(line)):
        graph[x].append(line[i])

visited = [False for i in range(V + 1)]
for i in range(1,V + 1):
    if not visited[i]:
        dfs(i, graph, visited, result)
result.reverse()

print(result)
