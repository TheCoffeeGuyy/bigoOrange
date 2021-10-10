n, k = map(int, input().split())
visited = [False] * (n+1)
mainCourses = list(map(int, input().split()))
graph = [[] for i in range(n+1)]
for i in range(1, n+1):
    ith = list(map(int, input().split()))

    for j in range(ith[0]):
        graph[i].append(ith[j + 1])

orders = []

def dfs(u, graph, orders, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, orders, visited)
    orders.append(u)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, graph, orders, visited)
orders.reverse()
print(orders)
print(graph)