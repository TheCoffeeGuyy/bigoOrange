dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def backtrack (a, r, c):
    a.append(r * n + c)
    visited[r][c] = True
    if len(a) == 8:
        sliceA = a.copy()
        sliceA.sort()
        cleanAns = ''
        for el in sliceA:
            cleanAns += str(el)
        ans.add(cleanAns)
    else:
        for k in range(4):
            tempr = dx[k] + r
            tempc = dy[k] + c
            if tempr in range(n) and tempc in range(n) and not visited[tempr][tempc] and matrix[tempr][tempc] != '.':
                backtrack(a, tempr, tempc)
    a.pop()
    visited[r][c] = False

t = int(input())

for _ in range(t):
    n = int(input())
    matrix = []

    for i in range(n):
        el = list(input())
        matrix.append(el)
    
    visited = [[False for i in range(20)] for j in range(20)]

    ans = set()
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != '.':
                a = []
                backtrack(a, i, j)
    print(len(ans))
