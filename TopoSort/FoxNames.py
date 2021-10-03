import queue

n = int(input())
graph = [[] for i in range(26)]
names = []
for i in range(n):
    name = input()
    names.append(name)

for i in range(1, len(names)):    
    first = list(names[i-1])
    second = list(names[i])
    indexFirst = 0
    indexSecond = 0
    while indexFirst < len(first) and indexSecond < len(second):
        ordFirst = ord(first[indexFirst]) - ord('a')
        ordSecond = ord(second[indexSecond]) - ord('a')
        if ordFirst == ordSecond:
            indexFirst +=1
            indexSecond +=1
        elif ordFirst < ordSecond:
            graph[ordFirst].append(ordSecond)
            break
        elif ordFirst > ordSecond:
            graph[ordFirst].append(ordSecond)
            break
        if indexFirst >= len(second):
            print('Impossible')
            exit()
result = []
# print('>>>', graph)
def topoKahnSort(graph, result):
    indegree = [0] * 26
    for u in range(26):
        for v in graph[u]:
            indegree[v] += 1

    zeroIndegree = queue.PriorityQueue()
    for i in range(26):
        if indegree[i] == 0:
            zeroIndegree.put(i)
    # print('indegree', indegree)
    
    while not zeroIndegree.empty():
        u = zeroIndegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zeroIndegree.put(v)
    for i in range(26):
        if indegree[i] != 0:
            return False
    return True

if topoKahnSort(graph, result):
    result = list(map(lambda x: chr(x + ord('a')), result))
    print(''.join(result))
else:
    print('Impossible')

