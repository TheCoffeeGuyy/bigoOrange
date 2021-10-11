dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

t = int(input())

def backtrack (a, r, c, visited):
    if r >= n or c >= n or visited[r][c] or r < 0 or c < 0 or matrix[r][c] == '.':
        return
    a.append((r, c))
    visited[r][c] = True
    if len(a) == 8:
        print(a)
        return
    for k in range(4):
        tempr = dx[k] + r
        tempc = dy[k] + c
        backtrack(a, tempr, tempc, visited)
    visited[r][c] = False
    a.pop()

for _ in range(t):
    n = int(input())
    matrix = []

    for i in range(n):
        el = list(input())
        matrix.append(el)
    
    visited = [[False for i in range(20)] for j in range(20)]

    ans = []
    a = []
    for i in range(n):
        for j in range(n):
            backtrack(a, i, j, visited)
