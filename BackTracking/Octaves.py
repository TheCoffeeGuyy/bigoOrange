dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())

def backtrack (count, j, i, curLen, visited):
    if j >= n or i >= n or visited[j][i] or j < 0 or i < 0 or matrix[j][i] == '.':
        return

    if curLen == 8:
        print('xzc')
        count += 1
        visited[j][i] = False
        return
    visited[j][i] = True
    for k in range(4):
        x = dx[k] + j
        y = dy[k] + i
        backtrack(count, x, y, curLen+1, visited)
    visited[j][i] = False


for _ in range(t):
    n = int(input())
    matrix = []

    for i in range(n):
        el = list(input())
        matrix.append(el)
    
    visited = [[False for i in range(20)] for j in range(20)]

    ans = 0

    for i in range(n):
        for j in range(n):
            backtrack(count, j, i, 1, visited)

    print(count)