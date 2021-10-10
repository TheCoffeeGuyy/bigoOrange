import queue

n = int(input())

graph = [[] for i in range(n+1)]
times = []
indegree = [0] * (n+1)
for i in range(1, n+1):
    ith = list(map(int, input().split()))
    times.append(ith[0])
    for j in range(ith[1]):
        first = ith[j+2]
        graph[i].append(first)
for u in range(1, n + 1):
    for v in graph[u]:
        indegree[v] += 1 
pq = queue.PriorityQueue()

for i in range(1, n+1):
    if indegree[i] == 0:
        pq.put(i)
result = []
ans = -1
i = n-1
while not pq.empty():
    u = pq.get()
    result.append(u)
    cost = times[u - 1] + i
    ans = max(ans, cost)
    i -= 1
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            pq.put(v)
# for i in range(len(result)):
#     ans = max(ans, i+times[result[i] - 1])
#     print('i' ,ans)
print(ans)
# print(times)
print(result)