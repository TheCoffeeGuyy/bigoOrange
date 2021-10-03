import queue

def topoKahnSort(graph, result):
    indegree =[None] + [0] * (V + 1)
    zeroIndegree = queue.PriorityQueue()

    for u in range(1, V + 1):
        for v in graph[u]:
            indegree[v] += 1 
    for i in range(1, V + 1):
        if indegree[i] == 0:
            zeroIndegree.put(i)

    while not zeroIndegree.empty():
        u = zeroIndegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zeroIndegree.put(v)
    for i in range(1, V + 1):
        if indegree[i] != 0:
            return False
    return True

V, E = map(int, input().split())
graph = [[] for i in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
result = []

if topoKahnSort(graph, result):
    for res in result:
        print(res, end=' ')
else:
    print('Sandro fails.')