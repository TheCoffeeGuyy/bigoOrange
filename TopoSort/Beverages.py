import queue

count = 0

def topoKahn(graph, result):
    indegree = [0] * n
    for u in range(n):
        for v in graph[u]:
            indegree[v] += 1
    zeroIndegree = queue.PriorityQueue()
    for i in range(n):
        if indegree[i] == 0:
            zeroIndegree.put(i)
    
    while not zeroIndegree.empty():
        u = zeroIndegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zeroIndegree.put(v)

while True:
    try:
        count += 1

        n = int(input())
        dic = {}
        reverDic = {}
        for i in range(n):
            alcol = input()
            dic[alcol] = i
            reverDic[i] = alcol
        graph = [[] for i in range(n)]
        relation = int(input())
        for i in range(relation):
            a, b = input().split()
            graph[dic[a]].append(dic[b])
        visited = [False] * n
        result = []
        topoKahn(graph, result)
        string = f'Case #{count}: Dilbert should drink beverages in this order:'
        for res in result:
            string = string + ' ' + reverDic[res]
        string += '.'
        print(string)
        print()
        input()
    except EOFError as e:
        exit()