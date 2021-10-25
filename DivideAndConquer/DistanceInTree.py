# n, k = map(int, input().split())

# graph = [[] for i in range(n+1)]
# for _ in range(n-1):
#     a, b = map(int, input().split())

#     graph[a].append(b)
#     graph[b].append(a)
# # print(graph)

# def backtrack(piece, vertex, k):
#     piece.append(vertex)
#     visited[vertex] = True
#     if len(piece) == k + 1:
#         copy = piece.copy()
#         copy.sort()
#         strcopy = ''
#         for c in copy:
#             strcopy += str(c)
#         ans.add(strcopy)
#     else:
#         for v in graph[vertex]:
#             if not visited[v]:
#                 backtrack(piece, v, k)
#     visited[vertex] = False
#     piece.pop()
# ans = set()
# visited = [False] * (n+1)
# for vertex in range(1,n+1):
#     piece = []
#     backtrack(piece, vertex, k)

# print(len(ans))

count ={}
count[-1] = 0
print(count)